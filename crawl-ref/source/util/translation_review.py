"""Parse DCSS description resources for generated translation reviews."""

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
