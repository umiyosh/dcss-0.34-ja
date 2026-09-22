# コードメッセージ: `spl-miscast.cc`

[コードメッセージ一覧](README.md)

自動生成。原本・辞書を変更して共通生成コマンドで更新する。
API接続済みは採用済み・実表示確認済みを意味しない。

## 1. L72 — 動的・未対応式（要調査・要改修）

呼出: `mpr` / [原本 L72](../../crawl-ref/source/spl-miscast.cc#L72)

### 未解決の式（断片を翻訳キーにしない）

```text
msg + attack_strength_punctuation(dam)
```

## 2. L349 — 未訳・API未接続

呼出: `simple_god_message` / [原本 L349](../../crawl-ref/source/spl-miscast.cc#L349)

### 原文（静的キー）

```text
 protects you from your miscast necromantic spell!
```

### 日本語

未訳（英語にフォールバック）。

主語等を別途結合する部分文。日本語の語順・文法を含む表示経路の改修が必要。
