"""Parse DCSS resources and generate deterministic translation reviews."""

import argparse
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path


REGENERATION_COMMAND = (
    "python3 crawl-ref/source/util/translation_review.py"
)
REPAIR_SKILL = "$translation-review-repair"
REPAIR_SKILL_PATH = (
    ".agents/skills/translation-review-repair/SKILL.md"
)
ASCII_LOWER = str.maketrans(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")


class DescriptionParseError(ValueError):
    """Raised when a description resource does not follow the text format."""


class TranslationReviewVerificationError(RuntimeError):
    """Raised when committed translation reviews are not reproducible."""


@dataclass(frozen=True)
class DescriptionEntry:
    """One player-facing description and its non-player-facing comments."""

    key: str
    body: str
    key_line: int
    key_comments: tuple[str, ...] = ()
    body_comments: tuple[str, ...] = ()


@dataclass(frozen=True)
class DuplicateKey:
    """A repeated key retained for runtime-compatible catalog loading."""

    key: str
    first_line: int
    line: int


@dataclass(frozen=True)
class DescriptionDocument:
    """Parsed entries from one description resource file."""

    path: Path
    entries: tuple[DescriptionEntry, ...]
    duplicate_keys: tuple[DuplicateKey, ...] = ()
    textdb: bool = False

    def lookup_key(self, key: str) -> str:
        """TextDB canonicalizes ASCII keys before storing and querying."""
        return key.translate(ASCII_LOWER) if self.textdb else key

    def entry(self, key: str) -> DescriptionEntry | None:
        """Return the last entry for a key, matching the game database."""
        return next(
            (entry for entry in reversed(self.entries)
             if self.lookup_key(entry.key) == self.lookup_key(key)),
            None,
        )


@dataclass(frozen=True)
class TranslationResource:
    """An English resource and its optional Japanese translation file."""

    name: str
    source: DescriptionDocument
    translation: DescriptionDocument | None
    data_directory: str = "descript"


@dataclass(frozen=True)
class TranslationCatalog:
    """All reviewable description resources in deterministic name order."""

    resources: tuple[TranslationResource, ...]

    def resource(self, name: str) -> TranslationResource | None:
        """Return a resource by its filename stem."""
        return next((item for item in self.resources if item.name == name), None)


def _parse_error(path: Path, line: int, message: str) -> DescriptionParseError:
    return DescriptionParseError(f"{path}:{line}: {message}")


def _is_malformed_delimiter(line: str) -> bool:
    stripped = line.strip()
    if stripped.startswith("%%%%"):
        return stripped != "%%%%"
    return bool(stripped) and set(stripped) == {"%"}


def parse_description_text(
        text: str,
        path: Path,
        *,
        allow_duplicate_keys: bool = False,
        textdb: bool = False,
) -> DescriptionDocument:
    """Parse a resource; textdb mode follows database.cc::_parse_text_db."""
    entries: list[DescriptionEntry] = []
    duplicate_keys: list[DuplicateKey] = []
    first_lines: dict[str, int] = {}
    pending_key_comments: list[str] = []
    key_comments: tuple[str, ...] = ()
    body_comments: list[str] = []
    body_lines: list[str] = []
    key: str | None = None
    key_line = 0
    in_entry = not textdb

    def finish_entry() -> None:
        nonlocal key, key_line, key_comments, body_comments, body_lines
        if key is None:
            return
        if not body_lines and not textdb:
            raise _parse_error(path, key_line, f"entry {key!r} has no body")
        lookup_key = key.translate(ASCII_LOWER) if textdb else key
        if lookup_key in first_lines:
            if not allow_duplicate_keys:
                raise _parse_error(
                    path,
                    key_line,
                    f"duplicate key {key!r}; first defined at line "
                    f"{first_lines[lookup_key]}",
                )
            duplicate_keys.append(DuplicateKey(
                key=key,
                first_line=first_lines[lookup_key],
                line=key_line,
            ))

        entries.append(DescriptionEntry(
            key=key,
            body="".join(body_lines).rstrip("\r\n"),
            key_line=key_line,
            key_comments=key_comments,
            body_comments=tuple(body_comments),
        ))
        first_lines.setdefault(lookup_key, key_line)
        key = None
        key_line = 0
        key_comments = ()
        body_comments = []
        body_lines = []

    for line_number, line in enumerate(text.splitlines(keepends=True), start=1):
        stripped = line.strip(" \t\r\n") if textdb else line.strip()
        if not textdb and _is_malformed_delimiter(line):
            raise _parse_error(path, line_number, "malformed delimiter")
        if (line.startswith("%%%%") if textdb else stripped == "%%%%"):
            finish_entry()
            in_entry = True
            continue
        if not in_entry:
            continue

        if key is None:
            if not stripped:
                continue
            if line.startswith("#"):
                pending_key_comments.append(line)
                continue
            key = stripped
            key_line = line_number
            key_comments = tuple(pending_key_comments)
            pending_key_comments = []
            continue

        if line.startswith("#"):
            body_comments.append(line)
        elif not stripped and not body_lines:
            continue
        else:
            body_lines.append(line.rstrip(" \t\r\n") + "\n" if textdb else line)

    finish_entry()
    return DescriptionDocument(
        path=path,
        entries=tuple(entries),
        duplicate_keys=tuple(duplicate_keys),
        textdb=textdb,
    )


def parse_description_file(
        path: Path,
        *,
        allow_duplicate_keys: bool = False,
        textdb: bool = False,
) -> DescriptionDocument:
    """Read and parse a UTF-8 description resource."""
    return parse_description_text(
        path.read_text(encoding="utf-8"),
        path,
        allow_duplicate_keys=allow_duplicate_keys,
        textdb=textdb,
    )


def load_translation_catalog(
        descript_dir: Path, *, textdb: bool = False,
) -> TranslationCatalog:
    """Load English resources and matching Japanese files in name order."""
    resources = []
    for source_path in sorted(descript_dir.glob("*.txt")):
        if textdb and source_path.name == "messages.txt":
            # The empty English registration file belongs to the code catalog.
            continue
        translation_path = descript_dir / "ja" / source_path.name
        resources.append(TranslationResource(
            name=source_path.stem,
            source=parse_description_file(
                source_path,
                allow_duplicate_keys=True,
                textdb=textdb,
            ),
            translation=(parse_description_file(
                translation_path,
                allow_duplicate_keys=True,
                textdb=textdb,
            )
                         if translation_path.is_file() else None),
            data_directory="database" if textdb else "descript",
        ))
    return TranslationCatalog(resources=tuple(resources))


def _effective_entries(document: DescriptionDocument) -> tuple[
        DescriptionEntry, ...]:
    """Return last-wins entries in their effective file order."""
    last_indexes = {
        document.lookup_key(entry.key): index
        for index, entry in enumerate(document.entries)
    }
    return tuple(
        entry for index, entry in enumerate(document.entries)
        if last_indexes[document.lookup_key(entry.key)] == index
    )


def _fenced_text(text: str) -> str:
    """Render text without interpreting DCSS tags or embedded Lua as Markdown."""
    longest_run = max(
        (len(match.group()) for match in re.finditer(r"`+", text)),
        default=0,
    )
    fence = "`" * max(3, longest_run + 1)
    return f"{fence}text\n{text}\n{fence}"


def _translation_entry(
        resource: TranslationResource, key: str,
) -> DescriptionEntry | None:
    entry = resource.translation.entry(key) if resource.translation else None
    # Empty translations fall back to English in both runtime query paths.
    return entry if entry and entry.body else None


def _resource_counts(resource: TranslationResource) -> tuple[int, int, int]:
    entries = _effective_entries(resource.source)
    translated = sum(
        _translation_entry(resource, entry.key) is not None
        for entry in entries
    )
    return len(entries), translated, len(entries) - translated


def render_translation_resource(resource: TranslationResource) -> str:
    """Render one resource as a stable, line-addressable Markdown review."""
    data_path = f"crawl-ref/source/dat/{resource.data_directory}"
    source_path = f"{data_path}/{resource.name}.txt"
    translation_path = (
        f"{data_path}/ja/{resource.name}.txt"
    )
    entries = _effective_entries(resource.source)
    total, translated, untranslated = _resource_counts(resource)
    japanese_resource = (
        f"`{translation_path}`" if resource.translation is not None else "なし"
    )
    sections = [
        f"# `{resource.name}.txt` 翻訳レビュー",
        "",
        "> このファイルは自動生成です。直接編集せず、英語・日本語resourceを更新してください。",
        "> 再生成: `python3 crawl-ref/source/util/translation_review.py`",
        "",
        f"- Resource: `{source_path}`",
        f"- Japanese resource: {japanese_resource}",
        f"- Entries: {total}",
        f"- Translated: {translated}",
        f"- Untranslated: {untranslated}",
    ]

    def source_location(path: str, line: int) -> str:
        label = f"`{path}:{line}`"
        if resource.data_directory == "database":
            return f"[{label}](../../{path}#L{line})"
        return label

    for index, entry in enumerate(entries, start=1):
        translation = _translation_entry(resource, entry.key)
        translation_source = (
            source_location(translation_path, translation.key_line)
            if translation is not None else "未訳"
        )
        translation_body = (
            translation.body if translation is not None else "（未訳）"
        )
        if index > 1:
            sections.extend(("", "---"))
        sections.extend((
            "",
            f"## Entry {index}",
            "",
            f"- Resource: `{source_path}`",
            f"- English key: `{entry.key}`",
            f"- English source: {source_location(source_path, entry.key_line)}",
            f"- Japanese source: {translation_source}",
            "",
            "### English",
            "",
            _fenced_text(entry.body),
            "",
            "### 日本語",
            "",
            _fenced_text(translation_body),
        ))

    return "\n".join(sections) + "\n"


def render_review_index(
        catalog: TranslationCatalog, *, data_directory: str = "descript",
        include_database: bool = False, include_code: bool = False,
) -> str:
    """Render the deterministic index for all generated resource reviews."""
    database = data_directory == "database"
    prefix = "../../" if database else "../"
    lines = [
        "# 台詞・実行時データの翻訳レビュー" if database else "# 翻訳レビュー用ビュー",
        "",
        "> このディレクトリは自動生成です。直接編集しないでください。",
        "> 再生成: `python3 crawl-ref/source/util/translation_review.py`",
        "> 指摘方法: [GitHub-native翻訳レビュー運用]"
        f"({prefix}crawl-ref/docs/develop/translation-review.md)",
        "> [翻訳の問題を報告]"
        "(https://github.com/umiyosh/dcss-0.34-ja/issues/new?"
        "template=translation-review.yml)",
        "",
        "英語原文と現在の日本語訳をresource単位で並べたレビュー用ビューです。",
        f"翻訳の正本は `crawl-ref/source/dat/{data_directory}/` 以下のresourceです。",
    ]
    if database:
        lines.extend((
            "",
            "[全体の一覧に戻る](../README.md)",
            "",
            "台詞・掛け声・神の発言と、それらが参照する名称・語句、ヘルプ等を含みます。",
            "`w:` の重み、空行による候補区切り、`@...@`、チャンネル指定はそのまま表示します。",
            "Entriesは有効キー数であり、台詞の本数ではありません。1キーに複数候補を含みます。",
            "Translatedは空でない訳が存在する件数で、査読済み・ゲームでの表示確認済みを意味しません。",
            "C++/Luaに埋め込まれたメッセージはこの一覧には含みません。",
        ))
    elif include_database or include_code:
        lines.extend(("", "## 対象別の入口", ""))
        if include_database:
            lines.append("- [台詞・実行時データ](database/README.md)")
        if include_code:
            lines.append("- [コード内メッセージ](code/README.md)")
        lines.extend(("", "## 説明文", ""))
    lines.extend((
        "",
        "| Resource | Entries | Translated | Untranslated | Japanese file |",
        "|---|---:|---:|---:|:---:|",
    ))
    for resource in catalog.resources:
        total, translated, untranslated = _resource_counts(resource)
        japanese_file = "yes" if resource.translation is not None else "no"
        lines.append(
            f"| [{resource.name}.txt]({resource.name}.md) | {total} | "
            f"{translated} | {untranslated} | {japanese_file} |"
        )
    return "\n".join(lines) + "\n"


def generate_translation_reviews(
        descript_dir: Path,
        output_dir: Path,
        *,
        database_dir: Path | None = None,
        code_source_dir: Path | None = None,
) -> tuple[Path, ...]:
    """Generate an index and one Markdown review for each English resource."""
    catalog = load_translation_catalog(descript_dir)
    if database_dir is not None and not database_dir.is_dir():
        raise FileNotFoundError(database_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    generated = [output_dir / "README.md"]
    generated[0].write_text(render_review_index(
        catalog, include_database=database_dir is not None,
        include_code=code_source_dir is not None,
    ), encoding="utf-8")
    for resource in catalog.resources:
        output_path = output_dir / f"{resource.name}.md"
        output_path.write_text(
            render_translation_resource(resource),
            encoding="utf-8",
        )
        generated.append(output_path)
    if database_dir is not None:
        database_catalog = load_translation_catalog(database_dir, textdb=True)
        database_output = output_dir / "database"
        database_output.mkdir(parents=True, exist_ok=True)
        index_path = database_output / "README.md"
        index_path.write_text(render_review_index(
            database_catalog, data_directory="database"), encoding="utf-8")
        generated.append(index_path)
        for resource in database_catalog.resources:
            output_path = database_output / f"{resource.name}.md"
            output_path.write_text(render_translation_resource(resource),
                                   encoding="utf-8")
            generated.append(output_path)
    if code_source_dir is not None:
        from code_message_review import generate_code_reviews
        generated.extend(generate_code_reviews(
            code_source_dir, output_dir / "code"))
    return tuple(generated)


def _output_snapshot(output_dir: Path) -> dict[str, bytes]:
    """Return all generated files below an output directory."""
    if not output_dir.is_dir():
        return {}
    return {
        path.relative_to(output_dir).as_posix(): path.read_bytes()
        for path in sorted(output_dir.rglob("*"))
        if path.is_file()
    }


def _snapshot_differences(
        expected: dict[str, bytes],
        actual: dict[str, bytes],
) -> tuple[tuple[str, str], ...]:
    """Describe missing, unexpected, and changed generated files."""
    differences = []
    for path in sorted(expected.keys() | actual.keys()):
        if path not in actual:
            kind = "missing"
        elif path not in expected:
            kind = "unexpected"
        elif expected[path] != actual[path]:
            kind = "changed"
        else:
            continue
        differences.append((kind, path))
    return tuple(differences)


def _display_output_path(output_dir: Path, relative_path: str) -> str:
    path = (output_dir / relative_path).resolve()
    try:
        return path.relative_to(Path.cwd().resolve()).as_posix()
    except ValueError:
        return str(path)


def _verification_error(
        title: str,
        differences: tuple[tuple[str, str], ...],
        output_dir: Path,
) -> TranslationReviewVerificationError:
    details = "\n".join(
        f"  - {kind}: {_display_output_path(output_dir, path)}"
        for kind, path in differences
    )
    return TranslationReviewVerificationError(
        f"{title}\n"
        f"Differing files:\n{details}\n"
        f"Regenerate with: {REGENERATION_COMMAND}\n"
        f"To repair with a local coding agent, ask it to use "
        f"{REPAIR_SKILL}.\n"
        f"Skill instructions: {REPAIR_SKILL_PATH}"
    )


def verify_translation_reviews(
        descript_dir: Path,
        output_dir: Path,
        *,
        database_dir: Path | None = None,
        code_source_dir: Path | None = None,
) -> int:
    """Verify committed reviews match two independent generations."""
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        first_dir = temp_root / "first"
        second_dir = temp_root / "second"
        options = {}
        if database_dir is not None:
            options["database_dir"] = database_dir
        if code_source_dir is not None:
            options["code_source_dir"] = code_source_dir
        generate_translation_reviews(descript_dir, first_dir, **options)
        generate_translation_reviews(descript_dir, second_dir, **options)
        first = _output_snapshot(first_dir)
        second = _output_snapshot(second_dir)

        nondeterministic = _snapshot_differences(first, second)
        if nondeterministic:
            raise _verification_error(
                "Translation review generation is non-deterministic.",
                nondeterministic,
                output_dir,
            )

        committed = _output_snapshot(output_dir)
        stale = _snapshot_differences(first, committed)
        if stale:
            raise _verification_error(
                "Committed translation review views are not current.",
                stale,
                output_dir,
            )
        return sum(Path(path).name != "README.md" for path in first)


def main(argv: list[str] | None = None) -> int:
    """Generate the repository's translation review views."""
    repository_root = Path(__file__).resolve().parents[3]
    parser = argparse.ArgumentParser(
        description="Generate Markdown views for DCSS translation review.",
    )
    parser.add_argument(
        "--descript-dir",
        type=Path,
        default=repository_root / "crawl-ref/source/dat/descript",
    )
    parser.add_argument(
        "--database-dir",
        type=Path,
        default=repository_root / "crawl-ref/source/dat/database",
    )
    parser.add_argument(
        "--code-source-dir",
        type=Path,
        default=repository_root / "crawl-ref/source",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=repository_root / "translation-review",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify committed views without modifying them",
    )
    args = parser.parse_args(argv)
    if args.check:
        try:
            resource_count = verify_translation_reviews(
                args.descript_dir,
                args.output_dir,
                database_dir=args.database_dir,
                code_source_dir=args.code_source_dir,
            )
        except TranslationReviewVerificationError as error:
            parser.exit(1, f"{error}\n")
        print(f"Verified {resource_count} resource views in "
              f"{args.output_dir}")
        return 0
    generated = generate_translation_reviews(
        args.descript_dir,
        args.output_dir,
        database_dir=args.database_dir,
        code_source_dir=args.code_source_dir,
    )
    count = sum(path.name != "README.md" for path in generated)
    print(f"Generated {count} resource views in "
          f"{args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
