import tempfile
import unittest
from pathlib import Path

from code_message_review import (
    extract_code_messages,
    generate_code_reviews,
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


class GenerateCodeReviewsTest(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
