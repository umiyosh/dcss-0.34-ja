# コードメッセージ: `l-crawl.cc`

[コードメッセージ一覧](README.md)

自動生成。原本・辞書を変更して共通生成コマンドで更新する。
API接続済みは採用済み・実表示確認済みを意味しない。

## 1. L66 — 動的・未対応式（要調査・要改修）

呼出: `jtrans` / [原本 L66](../../crawl-ref/source/l-crawl.cc#L66)

### 未解決の式（断片を翻訳キーにしない）

```text
string(source, length)
```

## 2. L81 — 動的・未対応式（要調査・要改修）

呼出: `jtrans_format` / [原本 L81](../../crawl-ref/source/l-crawl.cc#L81)

### 未解決の式（断片を翻訳キーにしない）

```text
string(source, length)
```

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 3. L113 — 動的・未対応式（要調査・要改修）

呼出: `mprf` / [原本 L113](../../crawl-ref/source/l-crawl.cc#L113)

### 未解決の式（断片を翻訳キーにしない）

```text
static_cast<msg_channel_type>(ch)
```

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 4. L1423 — 未訳・API未接続

呼出: `mprf` / [原本 L1423](../../crawl-ref/source/l-crawl.cc#L1423)

### 原文（静的キー）

```text
%s
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 5. L1443 — 未訳・API未接続

呼出: `mprf` / [原本 L1443](../../crawl-ref/source/l-crawl.cc#L1443)

### 原文（静的キー）

```text
call_dlua: cannot pass non-scalars yet (TODO)
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。
