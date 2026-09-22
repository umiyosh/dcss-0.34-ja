# コードメッセージ: `throw.cc`

[コードメッセージ一覧](README.md)

自動生成。原本・辞書を変更して共通生成コマンドで更新する。
API接続済みは採用済み・実表示確認済みを意味しない。

## 1. L290 — 未訳・API未接続

呼出: `mpr` / [原本 L290](../../crawl-ref/source/throw.cc#L290)

### 原文（静的キー）

```text
You have nothing you can fire or use right now.
```

### 日本語

未訳（英語にフォールバック）。

## 2. L332 — 未訳・API未接続

呼出: `mprf` / [原本 L332](../../crawl-ref/source/throw.cc#L332)

### 原文（静的キー）

```text
You cannot throw/fire anything while %s.
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 3. L342 — 未訳・API未接続

呼出: `mprf` / [原本 L342](../../crawl-ref/source/throw.cc#L342)

### 原文（静的キー）

```text
You cannot shoot with your %s while %s.
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 4. L746 — 未訳・API未接続

呼出: `mprf` / [原本 L746](../../crawl-ref/source/throw.cc#L746)

### 原文（静的キー）

```text
You %s %s%s.
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 5. L836 — 動的・未対応式（要調査・要改修）

呼出: `mpr` / [原本 L836](../../crawl-ref/source/throw.cc#L836)

### 未解決の式（断片を翻訳キーにしない）

```text
make_stringf("%s%s %s %s.",
                         mons->name(DESC_THE).c_str(),
                         teleport ? " magically" : "",
                         thrown ? "throws" : "shoots",
                         article_a(ratk.atk.projectile_name()).c_str()).c_str()
```
