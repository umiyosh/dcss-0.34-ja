"""Parse DCSS resources and generate deterministic translation reviews."""

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


class DescriptionParseError(ValueError):
    """Raised when a description resource does not follow the text format."""


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

    def entry(self, key: str) -> DescriptionEntry | None:
        """Return the last entry for a key, matching the game database."""
        return next(
            (entry for entry in reversed(self.entries) if entry.key == key),
            None,
        )


@dataclass(frozen=True)
class TranslationResource:
    """An English resource and its optional Japanese translation file."""

    name: str
    source: DescriptionDocument
    translation: DescriptionDocument | None


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
) -> DescriptionDocument:
    """Parse one DCSS ``dat/descript`` file without changing its content."""
    entries: list[DescriptionEntry] = []
    duplicate_keys: list[DuplicateKey] = []
    first_lines: dict[str, int] = {}
    pending_key_comments: list[str] = []
    key_comments: tuple[str, ...] = ()
    body_comments: list[str] = []
    body_lines: list[str] = []
    key: str | None = None
    key_line = 0

    def finish_entry() -> None:
        nonlocal key, key_line, key_comments, body_comments, body_lines
        if key is None:
            return
        if not body_lines:
            raise _parse_error(path, key_line, f"entry {key!r} has no body")
        if key in first_lines:
            if not allow_duplicate_keys:
                raise _parse_error(
                    path,
                    key_line,
                    f"duplicate key {key!r}; first defined at line "
                    f"{first_lines[key]}",
                )
            duplicate_keys.append(DuplicateKey(
                key=key,
                first_line=first_lines[key],
                line=key_line,
            ))

        entries.append(DescriptionEntry(
            key=key,
            body="".join(body_lines).rstrip("\r\n"),
            key_line=key_line,
            key_comments=key_comments,
            body_comments=tuple(body_comments),
        ))
        first_lines.setdefault(key, key_line)
        key = None
        key_line = 0
        key_comments = ()
        body_comments = []
        body_lines = []

    for line_number, line in enumerate(text.splitlines(keepends=True), start=1):
        stripped = line.strip()
        if _is_malformed_delimiter(line):
            raise _parse_error(path, line_number, "malformed delimiter")
        if stripped == "%%%%":
            finish_entry()
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
            body_lines.append(line)

    finish_entry()
    return DescriptionDocument(
        path=path,
        entries=tuple(entries),
        duplicate_keys=tuple(duplicate_keys),
    )


def parse_description_file(
        path: Path,
        *,
        allow_duplicate_keys: bool = False,
) -> DescriptionDocument:
    """Read and parse a UTF-8 description resource."""
    return parse_description_text(
        path.read_text(encoding="utf-8"),
        path,
        allow_duplicate_keys=allow_duplicate_keys,
    )


def load_translation_catalog(descript_dir: Path) -> TranslationCatalog:
    """Load English resources and matching Japanese files in name order."""
    resources = []
    for source_path in sorted(descript_dir.glob("*.txt")):
        translation_path = descript_dir / "ja" / source_path.name
        resources.append(TranslationResource(
            name=source_path.stem,
            source=parse_description_file(
                source_path,
                allow_duplicate_keys=True,
            ),
            translation=(parse_description_file(
                translation_path,
                allow_duplicate_keys=True,
            )
                         if translation_path.is_file() else None),
        ))
    return TranslationCatalog(resources=tuple(resources))


def _effective_entries(document: DescriptionDocument) -> tuple[
        DescriptionEntry, ...]:
    """Return last-wins entries in their effective file order."""
    last_indexes = {
        entry.key: index for index, entry in enumerate(document.entries)
    }
    return tuple(
        entry for index, entry in enumerate(document.entries)
        if last_indexes[entry.key] == index
    )


def _fenced_text(text: str) -> str:
    """Render text without interpreting DCSS tags or embedded Lua as Markdown."""
    longest_run = max(
        (len(match.group()) for match in re.finditer(r"`+", text)),
        default=0,
    )
    fence = "`" * max(3, longest_run + 1)
    return f"{fence}text\n{text}\n{fence}"


def _resource_counts(resource: TranslationResource) -> tuple[int, int, int]:
    entries = _effective_entries(resource.source)
    translated = sum(
        resource.translation is not None
        and resource.translation.entry(entry.key) is not None
        for entry in entries
    )
    return len(entries), translated, len(entries) - translated


def render_translation_resource(resource: TranslationResource) -> str:
    """Render one resource as a stable, line-addressable Markdown review."""
    source_path = f"crawl-ref/source/dat/descript/{resource.name}.txt"
    translation_path = (
        f"crawl-ref/source/dat/descript/ja/{resource.name}.txt"
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

    for index, entry in enumerate(entries, start=1):
        translation = (
            resource.translation.entry(entry.key)
            if resource.translation is not None else None
        )
        translation_source = (
            f"`{translation_path}:{translation.key_line}`"
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
            f"- English source: `{source_path}:{entry.key_line}`",
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


def render_review_index(catalog: TranslationCatalog) -> str:
    """Render the deterministic index for all generated resource reviews."""
    lines = [
        "# 翻訳レビュー用ビュー",
        "",
        "> このディレクトリは自動生成です。直接編集しないでください。",
        "> 再生成: `python3 crawl-ref/source/util/translation_review.py`",
        "",
        "英語原文と現在の日本語訳をresource単位で並べたレビュー用ビューです。",
        "翻訳の正本は `crawl-ref/source/dat/descript/` 以下のresourceです。",
        "",
        "| Resource | Entries | Translated | Untranslated | Japanese file |",
        "|---|---:|---:|---:|:---:|",
    ]
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
) -> tuple[Path, ...]:
    """Generate an index and one Markdown review for each English resource."""
    catalog = load_translation_catalog(descript_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    generated = [output_dir / "README.md"]
    generated[0].write_text(render_review_index(catalog), encoding="utf-8")
    for resource in catalog.resources:
        output_path = output_dir / f"{resource.name}.md"
        output_path.write_text(
            render_translation_resource(resource),
            encoding="utf-8",
        )
        generated.append(output_path)
    return tuple(generated)


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
        "--output-dir",
        type=Path,
        default=repository_root / "translation-review",
    )
    args = parser.parse_args(argv)
    generated = generate_translation_reviews(
        args.descript_dir,
        args.output_dir,
    )
    print(f"Generated {len(generated) - 1} resource views in "
          f"{args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
