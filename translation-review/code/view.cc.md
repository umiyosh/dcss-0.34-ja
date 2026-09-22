# コードメッセージ: `view.cc`

[コードメッセージ一覧](README.md)

自動生成。原本・辞書を変更して共通生成コマンドで更新する。
API接続済みは採用済み・実表示確認済みを意味しない。

## 1. L1042 — 動的・未対応式（要調査・要改修）

呼出: `mprf` / [原本 L1042](../../crawl-ref/source/view.cc#L1042)

### 未解決の式（断片を翻訳キーにしない）

```text
"Select layers to display:\n"
                           "<%s>(m)onsters</%s>|"
                           "<%s>(p)layer</%s>|"
                           "<%s>(i)tems</%s>|"
                           "<%s>(c)louds</%s>"
#ifndef USE_TILE_LOCAL
                           "|"
                           "<%s>monster (w)eapons</%s>|"
                           "<%s>monster (h)ealth</%s>"
#endif
```

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 2. L1069 — 未訳・API未接続

呼出: `mprf` / [原本 L1069](../../crawl-ref/source/view.cc#L1069)

### 原文（静的キー）

```text
Press 'a' to toggle all layers. Press any other key to exit.
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 3. L1130 — 未訳・API未接続

呼出: `mprf` / [原本 L1130](../../crawl-ref/source/view.cc#L1130)

### 原文（静的キー）

```text
Restoring view layers.
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。
