import tempfile
import unittest
from pathlib import Path

from translation_review import (
    DescriptionParseError,
    load_translation_catalog,
    parse_description_text,
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


if __name__ == "__main__":
    unittest.main()
