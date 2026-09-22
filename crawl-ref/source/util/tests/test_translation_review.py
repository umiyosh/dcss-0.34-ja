import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from translation_review import (
    DescriptionParseError,
    REGENERATION_COMMAND,
    REPAIR_SKILL,
    REPAIR_SKILL_PATH,
    TranslationResource,
    TranslationReviewVerificationError,
    generate_translation_reviews,
    load_translation_catalog,
    parse_description_text,
    render_translation_resource,
    verify_translation_reviews,
)


class ParseDescriptionTextTest(unittest.TestCase):
    def test_preserves_entry_content_and_classifies_comments(self):
        document = parse_description_text(
            """# Alias heading
%%%%
alias key

<target key>
%%%%
lua key

# This comment is not player-facing text.
:nowrap
{{
local description = "first line"

return description .. " second line"
}}
%%%%
""",
            Path("fixture.txt"),
        )

        self.assertEqual([entry.key for entry in document.entries],
                         ["alias key", "lua key"])
        self.assertEqual(document.entries[0].body, "<target key>")
        self.assertEqual(document.entries[0].key_line, 3)
        self.assertEqual(document.entries[0].key_comments,
                         ("# Alias heading\n",))
        self.assertEqual(
            document.entries[1].body,
            ':nowrap\n{{\nlocal description = "first line"\n\n'
            'return description .. " second line"\n}}',
        )
        self.assertEqual(document.entries[1].body_comments,
                         ("# This comment is not player-facing text.\n",))

    def test_rejects_duplicate_keys_with_both_locations(self):
        with self.assertRaisesRegex(
                DescriptionParseError,
                r"fixture\.txt:6: duplicate key 'same key'.*line 2"):
            parse_description_text(
                """%%%%
same key

first
%%%%
same key

second
%%%%
""",
                Path("fixture.txt"),
            )

    def test_preserves_and_reports_duplicates_when_explicitly_allowed(self):
        document = parse_description_text(
            """%%%%
same key

first
%%%%
same key

second
%%%%
""",
            Path("fixture.txt"),
            allow_duplicate_keys=True,
        )

        self.assertEqual([entry.body for entry in document.entries],
                         ["first", "second"])
        self.assertEqual(document.entry("same key").body, "second")
        self.assertEqual(len(document.duplicate_keys), 1)
        duplicate = document.duplicate_keys[0]
        self.assertEqual((duplicate.key, duplicate.first_line, duplicate.line),
                         ("same key", 2, 6))

    def test_rejects_incomplete_entries_and_malformed_delimiters(self):
        cases = {
            "missing body": (
                "%%%%\nkey without a body\n%%%%\n",
                r"fixture\.txt:2: entry 'key without a body' has no body",
            ),
            "malformed delimiter": (
                "%%%%\nkey\n\nbody\n%%%% extra\n",
                r"fixture\.txt:5: malformed delimiter",
            ),
        }

        for name, (text, message) in cases.items():
            with self.subTest(name=name):
                with self.assertRaisesRegex(DescriptionParseError, message):
                    parse_description_text(text, Path("fixture.txt"))

    def test_accepts_first_entry_without_an_opening_delimiter(self):
        document = parse_description_text(
            "key\n\nbody\n%%%%\nnext key\n\nnext body\n",
            Path("fixture.txt"),
        )

        self.assertEqual([entry.key for entry in document.entries],
                         ["key", "next key"])


class LoadTranslationCatalogTest(unittest.TestCase):
    def test_loads_resources_in_order_and_represents_missing_translation_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            descript_dir = Path(temp_dir)
            (descript_dir / "ja").mkdir()
            (descript_dir / "b.txt").write_text(
                "%%%%\nb key\n\nEnglish B\n%%%%\n", encoding="utf-8")
            (descript_dir / "a.txt").write_text(
                "%%%%\na key\n\nEnglish A\n%%%%\n", encoding="utf-8")
            (descript_dir / "ja" / "a.txt").write_text(
                "%%%%\na key\n\n日本語A\n%%%%\n", encoding="utf-8")

            catalog = load_translation_catalog(descript_dir)

            self.assertEqual([resource.name for resource in catalog.resources],
                             ["a", "b"])
            self.assertEqual(catalog.resources[0].translation.entries[0].body,
                             "日本語A")
            self.assertIsNone(catalog.resources[1].translation)
            self.assertEqual(catalog, load_translation_catalog(descript_dir))

    def test_loads_all_current_files_without_modifying_them(self):
        descript_dir = Path(__file__).resolve().parents[2] / "dat" / "descript"
        paths = tuple(sorted(descript_dir.glob("*.txt"))) + tuple(
            sorted((descript_dir / "ja").glob("*.txt")))
        before = {path: path.read_bytes() for path in paths}

        catalog = load_translation_catalog(descript_dir)

        after = {path: path.read_bytes() for path in paths}
        self.assertEqual(len(catalog.resources), 23)
        self.assertEqual(
            sum(resource.translation is not None
                for resource in catalog.resources),
            15,
        )
        self.assertTrue(all(resource.source.entries
                            for resource in catalog.resources))
        self.assertEqual(catalog, load_translation_catalog(descript_dir))
        self.assertEqual(before, after)


class RenderTranslationResourceTest(unittest.TestCase):
    def test_renders_alias_lua_tags_multiline_and_untranslated_entries(self):
        source = parse_description_text(
            """# Alias heading
%%%%
alias key

<target key>
%%%%
lua key

:nowrap
{{
return "<yellow>first line</yellow>\\nsecond line"
}}
%%%%
untranslated key

English only
%%%%
""",
            Path("source.txt"),
        )
        translation = parse_description_text(
            """%%%%
alias key

<訳の参照先>
%%%%
lua key

:nowrap
{{
return "<yellow>1行目</yellow>\\n2行目"
}}
%%%%
""",
            Path("ja/source.txt"),
        )

        rendered = render_translation_resource(TranslationResource(
            name="source",
            source=source,
            translation=translation,
        ))

        self.assertEqual(
            rendered,
            """# `source.txt` 翻訳レビュー

> このファイルは自動生成です。直接編集せず、英語・日本語resourceを更新してください。
> 再生成: `python3 crawl-ref/source/util/translation_review.py`

- Resource: `crawl-ref/source/dat/descript/source.txt`
- Japanese resource: `crawl-ref/source/dat/descript/ja/source.txt`
- Entries: 3
- Translated: 2
- Untranslated: 1

## Entry 1

- Resource: `crawl-ref/source/dat/descript/source.txt`
- English key: `alias key`
- English source: `crawl-ref/source/dat/descript/source.txt:3`
- Japanese source: `crawl-ref/source/dat/descript/ja/source.txt:2`

### English

```text
<target key>
```

### 日本語

```text
<訳の参照先>
```

---

## Entry 2

- Resource: `crawl-ref/source/dat/descript/source.txt`
- English key: `lua key`
- English source: `crawl-ref/source/dat/descript/source.txt:7`
- Japanese source: `crawl-ref/source/dat/descript/ja/source.txt:6`

### English

```text
:nowrap
{{
return "<yellow>first line</yellow>\\nsecond line"
}}
```

### 日本語

```text
:nowrap
{{
return "<yellow>1行目</yellow>\\n2行目"
}}
```

---

## Entry 3

- Resource: `crawl-ref/source/dat/descript/source.txt`
- English key: `untranslated key`
- English source: `crawl-ref/source/dat/descript/source.txt:14`
- Japanese source: 未訳

### English

```text
English only
```

### 日本語

```text
（未訳）
```
""",
        )

    def test_uses_only_the_runtime_effective_duplicate_source_entry(self):
        source = parse_description_text(
            "%%%%\nsame key\n\nold body\n%%%%\nsame key\n\ncurrent body\n",
            Path("duplicate.txt"),
            allow_duplicate_keys=True,
        )

        rendered = render_translation_resource(TranslationResource(
            name="duplicate",
            source=source,
            translation=None,
        ))

        self.assertNotIn("old body", rendered)
        self.assertEqual(rendered.count("- English key: `same key`"), 1)
        self.assertIn("current body", rendered)
        self.assertIn("- Japanese resource: なし", rendered)


class GenerateTranslationReviewsTest(unittest.TestCase):
    def test_writes_resource_views_and_index_deterministically(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            descript_dir = root / "descript"
            output_dir = root / "translation-review"
            (descript_dir / "ja").mkdir(parents=True)
            (descript_dir / "b.txt").write_text(
                "%%%%\nb key\n\nEnglish B\n%%%%\n", encoding="utf-8")
            (descript_dir / "a.txt").write_text(
                "%%%%\na key\n\nEnglish A\n%%%%\n", encoding="utf-8")
            (descript_dir / "ja" / "a.txt").write_text(
                "%%%%\na key\n\n日本語A\n%%%%\n", encoding="utf-8")

            generated = generate_translation_reviews(
                descript_dir,
                output_dir,
            )
            first = {path.name: path.read_bytes() for path in generated}
            generated_again = generate_translation_reviews(
                descript_dir,
                output_dir,
            )
            second = {path.name: path.read_bytes()
                      for path in generated_again}

            self.assertEqual([path.name for path in generated],
                             ["README.md", "a.md", "b.md"])
            self.assertEqual(first, second)
            self.assertIn(
                b"| [a.txt](a.md) | 1 | 1 | 0 | yes |",
                first["README.md"],
            )
            self.assertIn(
                b"| [b.txt](b.md) | 1 | 0 | 1 | no |",
                first["README.md"],
            )
            self.assertIn("日本語A", first["a.md"].decode("utf-8"))
            self.assertIn("（未訳）", first["b.md"].decode("utf-8"))


class VerifyTranslationReviewsTest(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        self.descript_dir = self.root / "descript"
        self.output_dir = self.root / "translation-review"
        (self.descript_dir / "ja").mkdir(parents=True)
        (self.descript_dir / "source.txt").write_text(
            "%%%%\nsource key\n\nEnglish source\n%%%%\n",
            encoding="utf-8",
        )
        (self.descript_dir / "ja" / "source.txt").write_text(
            "%%%%\nsource key\n\n日本語訳\n%%%%\n",
            encoding="utf-8",
        )
        generate_translation_reviews(self.descript_dir, self.output_dir)

    def test_repair_skill_is_available_at_reported_path(self):
        repository_root = Path(__file__).resolve().parents[4]

        self.assertTrue((repository_root / REPAIR_SKILL_PATH).is_file())

    def test_accepts_current_views_without_modifying_them(self):
        before = {
            path: path.read_bytes()
            for path in self.output_dir.iterdir()
        }

        resource_count = verify_translation_reviews(
            self.descript_dir,
            self.output_dir,
        )

        after = {
            path: path.read_bytes()
            for path in self.output_dir.iterdir()
        }
        self.assertEqual(resource_count, 1)
        self.assertEqual(before, after)

    def test_detects_translation_change_without_regeneration(self):
        translation_path = self.descript_dir / "ja" / "source.txt"
        translation_path.write_text(
            "%%%%\nsource key\n\n更新した日本語訳\n%%%%\n",
            encoding="utf-8",
        )

        with self.assertRaises(TranslationReviewVerificationError) as raised:
            verify_translation_reviews(self.descript_dir, self.output_dir)

        message = str(raised.exception)
        self.assertIn("changed:", message)
        self.assertIn("source.md", message)
        self.assertIn(REGENERATION_COMMAND, message)
        self.assertIn(REPAIR_SKILL, message)
        self.assertIn(REPAIR_SKILL_PATH, message)
        self.assertNotIn(
            "更新した日本語訳",
            (self.output_dir / "source.md").read_text(encoding="utf-8"),
        )

    def test_accepts_views_after_regeneration(self):
        (self.descript_dir / "ja" / "source.txt").write_text(
            "%%%%\nsource key\n\n更新した日本語訳\n%%%%\n",
            encoding="utf-8",
        )
        generate_translation_reviews(self.descript_dir, self.output_dir)

        self.assertEqual(
            verify_translation_reviews(self.descript_dir, self.output_dir),
            1,
        )

    def test_reports_stale_missing_and_unexpected_views(self):
        (self.output_dir / "source.md").write_text(
            "stale\n", encoding="utf-8")
        (self.output_dir / "README.md").unlink()
        (self.output_dir / "removed.md").write_text(
            "unexpected\n", encoding="utf-8")

        with self.assertRaises(TranslationReviewVerificationError) as raised:
            verify_translation_reviews(self.descript_dir, self.output_dir)

        message = str(raised.exception)
        self.assertIn("missing:", message)
        self.assertIn("README.md", message)
        self.assertIn("changed:", message)
        self.assertIn("source.md", message)
        self.assertIn("unexpected:", message)
        self.assertIn("removed.md", message)
        self.assertIn(REGENERATION_COMMAND, message)
        self.assertIn(REPAIR_SKILL, message)
        self.assertIn(REPAIR_SKILL_PATH, message)
        self.assertEqual(
            (self.output_dir / "source.md").read_text(encoding="utf-8"),
            "stale\n",
        )

    def test_rejects_non_deterministic_generation(self):
        original_generate = generate_translation_reviews
        call_count = 0

        def generate_with_drift(descript_dir, output_dir):
            nonlocal call_count
            call_count += 1
            generated = original_generate(descript_dir, output_dir)
            if call_count == 2:
                generated[0].write_text(
                    "different\n", encoding="utf-8")
            return generated

        with patch(
                "translation_review.generate_translation_reviews",
                side_effect=generate_with_drift):
            with self.assertRaises(
                    TranslationReviewVerificationError) as raised:
                verify_translation_reviews(
                    self.descript_dir,
                    self.output_dir,
                )

        message = str(raised.exception)
        self.assertIn("non-deterministic", message)
        self.assertIn(REPAIR_SKILL, message)
        self.assertIn(REPAIR_SKILL_PATH, message)


if __name__ == "__main__":
    unittest.main()
