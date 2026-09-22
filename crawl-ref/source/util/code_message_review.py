"""Conservative, deterministic reviews for C++ and Lua message call sites.

This is a lexer, not a compiler or a reachability analysis. Unsupported
expressions remain visible for a human to investigate; they never become
partial translation keys.
"""

import re
from dataclasses import dataclass
from pathlib import Path


CPP_CALLS = {
    "mpr", "mprf", "simple_monster_message", "simple_god_message",
    "wu_jian_sifu_message", "jtrans", "jtransf", "jtrans_format",
}
LUA_CALLS = {"crawl.mpr", "crawl.jtrans", "crawl.jtrans_format"}
TRANSLATORS = {"jtrans", "jtransf", "jtrans_format", "crawl.jtrans",
               "crawl.jtrans_format"}
FORMATTED = {"mprf", "jtransf", "jtrans_format", "crawl.jtrans_format"}
DICTIONARY = Path("dat/database/ja/messages.txt")
FORMAT_TOKEN = re.compile(
    r"%(?:%|[-+ #0]*(?:\*|[0-9]+)?(?:\.(?:\*|[0-9]*))?"
    r"(?:hh|ll|[hljztL])?[diouxXfFeEgGaAcsp])"
)


@dataclass(frozen=True)
class CodeMessage:
    """One recognized call, including unresolved dynamic expressions."""

    line: int
    call: str
    expression: str
    text: str | None
    lookup: bool = False
    formatted: bool = False


@dataclass(frozen=True)
class _Token:
    kind: str
    raw: str
    value: str | None
    start: int
    end: int
    line: int


def _unescape(text: str, lua: bool) -> str | None:
    result = bytearray()
    position = 0
    escapes = {"a": 7, "b": 8, "f": 12, "n": 10, "r": 13, "t": 9,
               "v": 11, "\\": 92, '"': 34, "'": 39, "?": 63}
    try:
        while position < len(text):
            char = text[position]
            position += 1
            if char != "\\":
                result.extend(char.encode("utf-8"))
                continue
            char = text[position]
            position += 1
            if char in escapes:
                result.append(escapes[char])
            elif char in "\r\n":
                if char == "\r" and text[position:position + 1] == "\n":
                    position += 1
                if lua:
                    result.append(10)
            elif lua and char == "z":
                while position < len(text) and text[position].isspace():
                    position += 1
            elif char == "x":
                pattern = r"[0-9a-fA-F]{2}" if lua else r"[0-9a-fA-F]+"
                match = re.match(pattern, text[position:])
                if not match:
                    return None
                result.append(int(match[0], 16))
                position += len(match[0])
            elif char in "0123456789" and (lua or char in "01234567"):
                pattern = r"[0-9]{0,2}" if lua else r"[0-7]{0,2}"
                rest = re.match(pattern, text[position:])[0]
                result.append(int(char + rest, 10 if lua else 8))
                position += len(rest)
            elif char in "uU":
                pattern = (r"\{([0-9a-fA-F]+)\}" if lua else
                           r"([0-9a-fA-F]{%d})" % (4 if char == "u" else 8))
                match = re.match(pattern, text[position:])
                if not match:
                    return None
                result.extend(chr(int(match[1], 16)).encode("utf-8"))
                position += len(match[0])
            else:
                return None
        return result.decode("utf-8")
    except (ValueError, IndexError, UnicodeError):
        return None


def _long_bracket(text: str, start: int) -> tuple[int, str] | None:
    opening = re.match(r"\[(=*)\[", text[start:])
    if not opening:
        return None
    begin = start + len(opening[0])
    end = text.find("]" + opening[1] + "]", begin)
    if end < 0:
        return len(text), ""
    value = text[begin:end]
    if value.startswith("\r\n"):
        value = value[2:]
    elif value.startswith(("\r", "\n")):
        value = value[1:]
    return end + len(opening[1]) + 2, value


def _tokens(text: str, lua: bool) -> list[_Token]:
    tokens = []
    position = 0
    line = 1
    while position < len(text):
        start = position
        char = text[start]
        kind = "punct"
        value = None
        if char.isspace():
            match = re.match(r"\s+", text[start:])
            position += len(match[0])
            kind = "skip"
        elif (lua and text.startswith("--", start)
              or not lua and text.startswith("//", start)):
            long = _long_bracket(text, start + 2) if lua else None
            if long:
                position = long[0]
            else:
                end = text.find("\n", start)
                position = len(text) if end < 0 else end
            kind = "skip"
        elif not lua and text.startswith("/*", start):
            end = text.find("*/", start + 2)
            position = len(text) if end < 0 else end + 2
            kind = "skip"
        elif lua and (long := _long_bracket(text, start)):
            position, value = long
            kind = "string"
        elif not lua and (raw := re.match(
                r'(u8|u|U|L)?R"([^\s()\\]{0,16})\(', text[start:])):
            end = text.find(")" + raw[2] + '"', start + len(raw[0]))
            position = len(text) if end < 0 else end + len(raw[2]) + 2
            if end >= 0 and raw[1] in (None, "u8"):
                value = text[start + len(raw[0]):end]
            kind = "string"
        elif (quoted := re.match(
                r"(['\"])" if lua else r"(?:u8|u|U|L)?(['\"])",
                text[start:])):
            quote = quoted[1]
            begin = start + len(quoted[0])
            position = begin
            while position < len(text):
                if text[position] == "\\":
                    position += 2
                elif text[position] == quote:
                    break
                else:
                    position += 1
            closed = position < len(text)
            if closed and (lua or quoted[0] in ('"', 'u8"')):
                value = _unescape(text[begin:position], lua)
            position = min(len(text), position + int(closed))
            kind = "string" if lua or quote == '"' else "character"
        elif char.isalpha() or char == "_":
            match = re.match(r"[\w]+", text[start:])
            position += len(match[0])
            kind = "identifier"
        else:
            position += 2 if text[start:start + 2] in ("->", "::") else 1
        raw_text = text[start:position]
        if kind != "skip":
            tokens.append(_Token(kind, raw_text, value, start, position, line))
        line += raw_text.count("\n")
    return tokens


def _arguments(tokens: list[_Token], opening: int
               ) -> tuple[list[list[_Token]], int]:
    arguments = []
    current = []
    stack = [")"]
    pairs = {"(": ")", "[": "]", "{": "}"}
    for position in range(opening + 1, len(tokens)):
        token = tokens[position]
        if token.raw in pairs and token.kind == "punct":
            stack.append(pairs[token.raw])
        elif token.raw == stack[-1] and token.kind == "punct":
            stack.pop()
            if not stack:
                arguments.append(current)
                return arguments, position
        if token.raw == "," and len(stack) == 1:
            arguments.append(current)
            current = []
        else:
            current.append(token)
    arguments.append(current)
    return arguments, len(tokens) - 1


def _call_at(tokens: list[_Token], position: int, lua: bool
             ) -> tuple[str, int] | None:
    token = tokens[position]
    if token.kind != "identifier":
        return None
    if lua:
        if (position + 3 < len(tokens) and token.raw == "crawl"
                and tokens[position + 1].raw == "."
                and tokens[position + 3].raw == "("):
            name = "crawl." + tokens[position + 2].raw
            if name in LUA_CALLS:
                return name, position + 3
        return None
    if (token.raw not in CPP_CALLS or position + 1 >= len(tokens)
            or tokens[position + 1].raw != "("):
        return None
    if position and tokens[position - 1].raw in (
            ".", "->", "::", "void", "bool", "string", "char"):
        return None
    return token.raw, position + 1


def _literal(expression: list[_Token], lua: bool
             ) -> tuple[str | None, bool, bool]:
    if not expression:
        return None, False, False
    if (lua and len(expression) >= 4
            and [token.raw for token in expression[:4]]
            == ["string", ".", "format", "("]):
        arguments, closing = _arguments(expression, 3)
        if closing == len(expression) - 1:
            value, lookup, formatted = _literal(arguments[0], lua)
            if lookup and formatted:
                return value, lookup, formatted
    call = _call_at(expression, 0, lua)
    if call and call[0] in TRANSLATORS:
        arguments, closing = _arguments(expression, call[1])
        if closing != len(expression) - 1:
            return None, True, call[0] in FORMATTED
        value, _, _ = _literal(arguments[0], lua)
        return value, True, call[0] in FORMATTED
    if (all(token.kind == "string" and token.value is not None
            for token in expression) and (not lua or len(expression) == 1)):
        return "".join(token.value for token in expression), False, False
    return None, False, False


def extract_code_messages(text: str, path: Path) -> tuple[CodeMessage, ...]:
    """Extract known calls; dynamic/unrecognized arguments have text=None."""
    lua = path.suffix == ".lua"
    tokens = _tokens(text, lua)
    messages = []
    covered_lookups = set()
    position = 0
    while position < len(tokens):
        call = _call_at(tokens, position, lua)
        if not call:
            position += 1
            continue
        name, opening = call
        arguments, closing = _arguments(tokens, opening)
        if (not arguments or not arguments[0]
                or arguments[0][0].raw in ("const", "msg_channel_type")):
            position = closing + 1
            continue
        if tokens[position].start in covered_lookups:
            position += 1
            continue
        index = 1 if name == "simple_monster_message" else 0
        if name == "mprf" and arguments[0][0].raw.startswith("MSGCH_"):
            index = 1
            if len(arguments) > 2 and _literal(arguments[1], lua)[0] is None:
                # Only accept a clear integer parameter before the format.
                if all(token.raw.isdigit() or token.raw == "-"
                       for token in arguments[1]):
                    index = 2
        if index >= len(arguments) or not arguments[index]:
            position = closing + 1
            continue
        argument = arguments[index]
        value, lookup, formatted = _literal(argument, lua)
        if lookup:
            for candidate in range(len(argument)):
                wrapped = _call_at(argument, candidate, lua)
                if wrapped and wrapped[0] in TRANSLATORS:
                    covered_lookups.add(argument[candidate].start)
                    break
        if name in TRANSLATORS:
            lookup = True
        messages.append(CodeMessage(
            tokens[position].line, name,
            text[argument[0].start:argument[-1].end], value,
            lookup, formatted or name in FORMATTED,
        ))
        position += 1
    return tuple(messages)


def message_key(text: str) -> str:
    """Encode the exact runtime key without case or whitespace changes."""
    return (text.replace("\\", "\\\\").replace("\n", "\\n")
            .replace("\r", "\\r").replace("\t", "\\t"))


def load_message_translations(path: Path) -> dict[str, tuple[str, int]]:
    """Read exact-key TextDB, retaining the last definition like runtime."""
    if not path.exists():
        return {}
    entries = {}
    key = None
    key_line = 0
    body = []
    in_entry = False

    def finish():
        if key is not None:
            entries[key] = ("\n".join(body).lstrip("\n"), key_line)

    for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), 1):
        if line.startswith("#"):
            continue
        if line.startswith("%%%%"):
            finish()
            key = None
            body = []
            in_entry = True
        elif not in_entry:
            continue
        elif key is None:
            if line:
                key, key_line = line, line_number
        else:
            body.append(line.rstrip())
    finish()
    return entries


def _format_tokens(text: str) -> tuple[str, ...] | None:
    result = []
    position = 0
    while position < len(text):
        if text[position] != "%":
            position += 1
            continue
        match = FORMAT_TOKEN.match(text, position)
        if not match:
            return None
        result.append(match[0])
        position = match.end()
    return tuple(result)


def validate_message_translation(original: str, translation: str) -> bool:
    """Require exactly preserved, safe printf tokens (including %%)."""
    tokens = _format_tokens(original)
    return tokens is not None and tokens == _format_tokens(translation)


def _fence(text: str, language: str = "text") -> str:
    runs = [len(match[0]) for match in re.finditer(r"`+", text)]
    fence = "`" * max(3, max(runs, default=0) + 1)
    return f"{fence}{language}\n{text}\n{fence}"


def _source_link(path: Path, line: int, view: Path) -> str:
    prefix = "../" * (2 + len(view.parent.parts))
    return f"{prefix}crawl-ref/source/{path.as_posix()}#L{line}"


def _state(message: CodeMessage, translation: str | None) -> str:
    if message.text is None:
        return "動的・未対応式（要調査・要改修）"
    if message.lookup:
        return "訳あり・API接続済み" if translation else "未訳・API接続済み"
    return "訳あり・API未接続" if translation else "未訳・API未接続"


def _render_file(path: Path, messages: tuple[CodeMessage, ...],
                 translations: dict[str, tuple[str, int]]) -> str:
    view = Path(path.as_posix() + ".md")
    index = "../" * len(view.parent.parts) + "README.md"
    lines = [f"# コードメッセージ: `{path.as_posix()}`", "",
             f"[コードメッセージ一覧]({index})", "",
             "自動生成。原本・辞書を変更して共通生成コマンドで更新する。",
             "API接続済みは採用済み・実表示確認済みを意味しない。", ""]
    for number, message in enumerate(messages, 1):
        key = message_key(message.text) if message.text is not None else None
        translated = translations.get(key)
        translation = translated[0] if translated else None
        if (translation and message.formatted and message.text is not None
                and not validate_message_translation(message.text,
                                                     translation)):
            raise ValueError(
                f"{path}:{message.line}: incompatible translation format: {key}"
            )
        lines.extend([
            f"## {number}. L{message.line} — {_state(message, translation)}",
            "", f"呼出: `{message.call}` / "
            f"[原本 L{message.line}]({_source_link(path, message.line, view)})",
            "", "### 原文（静的キー）" if message.text is not None
            else "### 未解決の式（断片を翻訳キーにしない）", "",
            _fence(message.text if message.text is not None
                   else message.expression), "",
        ])
        if message.text is not None:
            lines.extend(["### 日本語", ""])
            if translation:
                lines.extend([
                    f"[辞書 L{translated[1]}]"
                    f"({_source_link(DICTIONARY, translated[1], view)})", "",
                    _fence(translation), "",
                ])
            else:
                lines.extend(["未訳（英語にフォールバック）。", ""])
        if message.formatted:
            lines.extend([
                "書式と引数の対応を確認する。引数に含まれる英語の名称・句は"
                "別途対応が必要。", "",
            ])
        if message.call in ("simple_monster_message", "simple_god_message"):
            lines.extend([
                "主語等を別途結合する部分文。日本語の語順・文法を含む"
                "表示経路の改修が必要。", "",
            ])
    return "\n".join(lines)


def generate_code_reviews(source_dir: Path, output_dir: Path
                          ) -> tuple[Path, ...]:
    """Generate per-source views and an honest coverage inventory."""
    if not source_dir.is_dir():
        raise ValueError(f"missing source directory: {source_dir}")
    paths = set(source_dir.glob("*.cc")) | set(source_dir.glob("*.h"))
    paths.update((source_dir / "dat").rglob("*.lua"))
    translations = load_message_translations(source_dir / DICTIONARY)
    files = []
    for source in sorted(paths):
        path = source.relative_to(source_dir)
        messages = extract_code_messages(source.read_text(encoding="utf-8"),
                                         path)
        if messages:
            files.append((path, messages))
    output_dir.mkdir(parents=True, exist_ok=True)
    generated = [output_dir / "README.md"]
    all_messages = [message for _, messages in files for message in messages]
    static = sum(message.text is not None for message in all_messages)
    dynamic = len(all_messages) - static
    connected = sum(message.lookup for message in all_messages)
    lines = [
        "# コード内メッセージの翻訳レビュー", "",
        "[翻訳レビュー入口](../README.md)", "",
        "原本からの自動生成。1ファイルをメタIssueとし、到達性・表示経路を"
        "確認した未訳3エントリーずつを子Issue・PRにする。", "",
        f"認識した呼出 {len(all_messages)} / 静的キー {static} / "
        f"動的・未対応式 {dynamic} / 翻訳API参照 {connected}。", "",
        "同じ文の複数呼出も各行に載せるため、件数は翻訳すべき文章の"
        "総数・完了率ではない。", "",
        "## 抽出範囲と限界", "",
        "- C++: `crawl-ref/source/*.cc`, `*.h` の `mpr`, `mprf`, "
        "`simple_monster_message`, `simple_god_message`, "
        "`wu_jian_sifu_message` と `jtrans` / `jtransf` / `jtrans_format`。",
        "- Lua: `crawl-ref/source/dat/**/*.lua` の `crawl.mpr`, "
        "`crawl.jtrans`, `crawl.jtrans_format`。",
        "- コメント・引用・括弧を区別した字句解析。C++の連結リテラル、"
        "raw文字列、Luaの長い文字列を認識する。コンパイラではない。",
        "- 条件式、変数、文字列の動的結合、書式引数、未知の構文は"
        "原式を残して要調査とする。C++ mprfの型解決はしないため、"
        "チャネル変数等のoverloadは未解決になり得る。",
        "- 対象外: 上記以外の関数、マクロ展開、C++サブディレクトリ、"
        "Luaを埋め込む.des等、UI/メニュー、Tiles/WebTiles独自表示。"
        "この一覧だけで全表示の網羅・到達性を保証しない。",
        "- 訳ありでもAPI未接続ならゲーム表示は変わらない。"
        "API接続済みでも人間の採用・実表示確認は別途必要。",
        "- 辞書は `crawl-ref/source/dat/database/ja/messages.txt`。"
        "原文キーは大文字小文字・前後空白を維持し、改行等をescapeする。",
        "- 再生成: `python3 crawl-ref/source/util/translation_review.py`。", "",
        "## ファイル別", "",
        "| 原本 | 静的キー | 動的・未対応式 | 翻訳API参照 |",
        "| --- | ---: | ---: | ---: |",
    ]
    for path, messages in files:
        relative = Path(path.as_posix() + ".md")
        destination = output_dir / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(_render_file(path, messages, translations),
                               encoding="utf-8")
        generated.append(destination)
        known = sum(message.text is not None for message in messages)
        lookups = sum(message.lookup for message in messages)
        lines.append(f"| [{path.as_posix()}]({relative.as_posix()}) "
                     f"| {known} | {len(messages) - known} | {lookups} |")
    known_keys = {message_key(message.text) for message in all_messages
                  if message.text is not None}
    unused = sorted(set(translations) - known_keys)
    if unused:
        lines.extend(["", "## 対応する静的呼出を確認できない辞書キー", "",
                      "未使用とは断定しない。対象外・動的な経路も確認する。", ""])
        for key in unused:
            lines.extend([_fence(key), ""])
    generated[0].write_text("\n".join(lines) + "\n", encoding="utf-8")
    return tuple(generated)
