import tempfile
import unittest
from pathlib import Path

from code_message_review import (
    extract_code_messages,
    generate_code_reviews,
    load_message_translations,
    message_key,
    validate_message_translation,
)


class ExtractCodeMessagesTest(unittest.TestCase):
    def test_cpp_literals_comments_raw_strings_and_format_arguments(self):
        text = r'''// mpr("comment");
void test()
{
    mpr("You " /* adjacent */ "blink.");
    mprf(MSGCH_WARN, "%s hits for %d damage.", name, damage);
    mprf(MSGCH_GOD, 1, R"msg(You say "hello".)msg");
    mpr("Line\n\"quote\"");
    const char *code = "mpr(\"not a call\")";
}
'''
        messages = extract_code_messages(text, Path("message.cc"))
        self.assertEqual([message.text for message in messages], [
            "You blink.", "%s hits for %d damage.", 'You say "hello".',
            'Line\n"quote"',
        ])
        self.assertEqual(messages[0].line, 4)
        self.assertEqual(messages[1].call, "mprf")
        self.assertEqual(messages[0].expression,
                         '"You " /* adjacent */ "blink."')

    def test_keeps_dynamic_expressions_as_unresolved_not_partial_text(self):
        messages = extract_code_messages('''
mpr("You " + action);
mprf(MSGCH_WARN, flag ? "Yes" : "No");
mpr(message);
mprf(MSGCH_WARN, format, value);
simple_monster_message(*mon, " growls!");
simple_god_message(" is pleased.");
wu_jian_sifu_message("Well done!");
''', Path("combat.cc"))
        self.assertEqual([message.text for message in messages[:4]],
                         [None, None, None, None])
        self.assertIn('flag ? "Yes" : "No"', messages[1].expression)
        self.assertEqual([message.text for message in messages[4:]],
                         [" growls!", " is pleased.", "Well done!"])

    def test_cpp_declarations_and_member_calls_are_not_messages(self):
        messages = extract_code_messages('''
void mpr(const string &text);
void mprf(const char *format, ...) { write(format); }
void simple_god_message(const char *event, bool possessive) {}
obj.mpr("not the global function");
obj->mpr("not the global function either");
mpr("Actual call.");
''', Path("message.cc"))
        self.assertEqual([message.text for message in messages],
                         ["Actual call."])

    def test_lua_long_strings_escapes_comments_and_dynamic_expressions(self):
        text = '''-- crawl.mpr("comment")
--[=[ crawl.mpr("long comment") ]=]
crawl.mpr("You blink.", "plain")
crawl.mpr([=[A "long"\nmessage.]=])
crawl.mpr('You \\'blink\\'.')
crawl.mpr("You " .. action)
crawl.mpr(string.format("%s hits!", name))
'''
        messages = extract_code_messages(text, Path("dat/dlua/test.lua"))
        self.assertEqual([message.text for message in messages], [
            "You blink.", 'A "long"\nmessage.', "You 'blink'.", None, None,
        ])
        self.assertEqual(messages[1].line, 4)

    def test_unsupported_literals_do_not_silently_become_wrong_keys(self):
        messages = extract_code_messages(r'''
mpr(L"wide literal");
mpr("unknown\qescape");
mpr("unterminated);
''', Path("edge.cc"))
        self.assertEqual(len(messages), 3)
        self.assertTrue(all(message.text is None for message in messages))

    def test_translation_apis_preserve_keys_and_nested_lookup_visibility(self):
        messages = extract_code_messages('''
mpr(jtrans("You blink."));
mpr(jtransf("You hit %s.", name));
mpr("prefix " + jtrans("You move."));
mprf("%s", jtrans("You stop.").c_str());
''', Path("api.cc"))
        self.assertEqual([message.text for message in messages], [
            "You blink.", "You hit %s.", None, "You move.",
            "%s", "You stop.",
        ])
        self.assertEqual([message.lookup for message in messages],
                         [True, True, False, True, False, True])
        self.assertTrue(messages[1].formatted)
        self.assertFalse(messages[0].formatted)

    def test_lua_format_uses_lookup_key_not_outer_dynamic_expression(self):
        messages = extract_code_messages('''
crawl.mpr(crawl.jtrans("You blink."))
crawl.mpr(string.format(crawl.jtrans_format("You hit %s."), name))
''', Path("dat/dlua/api.lua"))
        self.assertEqual([message.text for message in messages],
                         ["You blink.", "You hit %s."])
        self.assertTrue(all(message.lookup for message in messages))
        self.assertTrue(messages[1].formatted)


class MessageDictionaryTest(unittest.TestCase):
    def test_ignores_preamble_and_preserves_whitespace_only_key(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "messages.txt"
            path.write_text("preamble\nignore me\n%%%%\n \n\n空白\n%%%%\n",
                            encoding="utf-8")
            self.assertEqual(load_message_translations(path),
                             {" ": ("空白", 4)})

    def test_exact_runtime_keys_and_textdb_last_wins(self):
        self.assertEqual(message_key(" A\\B\n\t\r"), " A\\\\B\\n\\t\\r")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "messages.txt"
            self.assertEqual(load_message_translations(path), {})
            path.write_text(
                "# heading\n%%%%\n A \\n\n\n最初\n%%%%\n A \\n\n\n"
                "# comment\n最後  \n\n%%%%\n", encoding="utf-8")
            self.assertEqual(load_message_translations(path),
                             {" A \\n": ("最後\n", 7)})

    def test_printf_contract_including_unsafe_formats(self):
        self.assertTrue(validate_message_translation(
            "%s hits for %04d, %.*f%%.", "%sは%04d、%.*f%%。"))
        for original, translated in [
                ("%s %d", "%d %s"), ("%04d", "%d"), ("%s", "%n"),
                ("%d", "%1$d"), ("%d", "%"), ("%*3d", "%*3d"),
                ("100%", "100%"), ("%%", "%")]:
            with self.subTest(original=original, translated=translated):
                self.assertFalse(validate_message_translation(original,
                                                              translated))


class GenerateCodeReviewsTest(unittest.TestCase):
    def test_missing_source_directory_is_not_reported_as_empty_coverage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with self.assertRaisesRegex(ValueError, "source directory"):
                generate_code_reviews(root / "missing", root / "review")

    def test_deterministic_views_preserve_sources_and_link_call_sites(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "crawl-ref/source"
            source.mkdir(parents=True)
            cpp = source / "message.cc"
            cpp.write_text('mpr("You blink.");\nmpr(message);\n',
                           encoding="utf-8")
            lua = source / "dat/dlua/test.lua"
            lua.parent.mkdir(parents=True)
            lua.write_text('crawl.mpr("Lua message.")\n', encoding="utf-8")
            excluded = source / "contrib/ignored.cc"
            excluded.parent.mkdir()
            excluded.write_text('mpr("Excluded.");\n', encoding="utf-8")
            before = {path: path.read_bytes() for path in source.rglob("*")
                      if path.is_file()}
            first = root / "first"
            second = root / "second"
            generated = generate_code_reviews(source, first)
            generate_code_reviews(source, second)
            self.assertEqual(
                [path.relative_to(first).as_posix() for path in generated],
                ["README.md", "dat/dlua/test.lua.md", "message.cc.md"],
            )
            self.assertEqual(
                {path.relative_to(first): path.read_bytes()
                 for path in generated},
                {path.relative_to(second): path.read_bytes()
                 for path in second.rglob("*.md")},
            )
            self.assertEqual(before, {path: path.read_bytes() for path in before})
            view = (first / "message.cc.md").read_text(encoding="utf-8")
            self.assertIn("You blink.", view)
            self.assertIn("未訳", view)
            self.assertIn("動的", view)
            self.assertIn("../../crawl-ref/source/message.cc#L1", view)
            index = (first / "README.md").read_text(encoding="utf-8")
            self.assertIn("message.cc.md", index)
            self.assertIn("dat/dlua/test.lua.md", index)
            self.assertIn("対象外", index)
            self.assertNotIn("Excluded.", index)

    def test_dictionary_translation_is_not_confused_with_runtime_connection(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "message.cc").write_text(
                'mpr("You blink.");\nmpr(jtrans("You blink."));\n'
                'mpr(jtrans("100% certain."));\n', encoding="utf-8")
            dictionary = source / "dat/database/ja/messages.txt"
            dictionary.parent.mkdir(parents=True)
            dictionary.write_text(
                "%%%%\nYou blink.\n\nあなたは瞬間移動した。\n"
                "%%%%\n100% certain.\n\n100%確かだ。\n", encoding="utf-8")
            output = root / "review"
            generate_code_reviews(source, output)
            view = (output / "message.cc.md").read_text(encoding="utf-8")
            self.assertIn("訳あり・API未接続", view)
            self.assertIn("訳あり・API接続済み", view)
            self.assertIn("あなたは瞬間移動した。", view)
            self.assertIn("../../crawl-ref/source/dat/database/ja/messages.txt#L2",
                          view)

    def test_incompatible_format_translation_fails_generation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "message.cc").write_text(
                'mpr(jtransf("You hit %s.", name));\n', encoding="utf-8")
            dictionary = source / "dat/database/ja/messages.txt"
            dictionary.parent.mkdir(parents=True)
            dictionary.write_text(
                "%%%%\nYou hit %s.\n\nあなたは%dを攻撃した。\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError,
                                        "incompatible translation format"):
                generate_code_reviews(source, root / "review")


if __name__ == "__main__":
    unittest.main()
