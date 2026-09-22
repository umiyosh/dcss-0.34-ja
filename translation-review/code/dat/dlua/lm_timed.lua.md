# コードメッセージ: `dat/dlua/lm_timed.lua`

[コードメッセージ一覧](../../README.md)

自動生成。原本・辞書を変更して共通生成コマンドで更新する。
API接続済みは採用済み・実表示確認済みを意味しない。

## 1. L84 — 動的・未対応式（要調査・要改修）

呼出: `crawl.mpr` / [原本 L84](../../../../crawl-ref/source/dat/dlua/lm_timed.lua#L84)

### 未解決の式（断片を翻訳キーにしない）

```text
dgn.feature_desc_at(x, y, "The") .. " vanishes " ..
                "just as you enter it!"
```

## 2. L92 — 動的・未対応式（要調査・要改修）

呼出: `crawl.mpr` / [原本 L92](../../../../crawl-ref/source/dat/dlua/lm_timed.lua#L92)

### 未解決の式（断片を翻訳キーにしない）

```text
util.expand_entity(self.props.entity, self.props.disappear) or
                 dgn.feature_desc_at(x, y, "The") .. " disappears!"
```

## 3. L95 — 未訳・API接続済み

呼出: `crawl.mpr` / [原本 L95](../../../../crawl-ref/source/dat/dlua/lm_timed.lua#L95)

### 原文（静的キー）

```text
The walls and floor vibrate strangely for a moment.
```

### 日本語

未訳（英語にフォールバック）。
