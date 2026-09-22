# コードメッセージ: `mon-behv.cc`

[コードメッセージ一覧](README.md)

自動生成。原本・辞書を変更して共通生成コマンドで更新する。
API接続済みは採用済み・実表示確認済みを意味しない。

## 1. L785 — 未訳・API未接続

呼出: `mpr` / [原本 L785](../../crawl-ref/source/mon-behv.cc#L785)

### 原文（静的キー）

```text
It's been too long! Stop travelling.
```

### 日本語

未訳（英語にフォールバック）。

## 2. L1121 — 未訳・API未接続

呼出: `mprf` / [原本 L1121](../../crawl-ref/source/mon-behv.cc#L1121)

### 原文（静的キー）

```text
%s attack snaps %s out of %s fear.
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 3. L1184 — 未訳・API未接続

呼出: `mprf` / [原本 L1184](../../crawl-ref/source/mon-behv.cc#L1184)

### 原文（静的キー）

```text
%s snaps out of %s daze.
```

### 日本語

未訳（英語にフォールバック）。

書式と引数の対応を確認する。引数に含まれる英語の名称・句は別途対応が必要。

## 4. L1462 — 未訳・API未接続

呼出: `simple_monster_message` / [原本 L1462](../../crawl-ref/source/mon-behv.cc#L1462)

### 原文（静的キー）

```text
 passes through the gate.
```

### 日本語

未訳（英語にフォールバック）。

主語等を別途結合する部分文。日本語の語順・文法を含む表示経路の改修が必要。

## 5. L1466 — 動的・未対応式（要調査・要改修）

呼出: `simple_monster_message` / [原本 L1466](../../crawl-ref/source/mon-behv.cc#L1466)

### 未解決の式（断片を翻訳キーにしない）

```text
make_stringf(" %s the %s.",
                dir == CMD_GO_UPSTAIRS     ? "goes up" :
                dir == CMD_GO_DOWNSTAIRS   ? "goes down"
                                           : "takes",
                feat_is_escape_hatch(feat) ? "escape hatch"
                                           : "stairs").c_str()
```

主語等を別途結合する部分文。日本語の語順・文法を含む表示経路の改修が必要。

## 6. L1476 — 動的・未対応式（要調査・要改修）

呼出: `simple_monster_message` / [原本 L1476](../../crawl-ref/source/mon-behv.cc#L1476)

### 未解決の式（断片を翻訳キーにしない）

```text
make_stringf(" %s the shaft.",
                mon->airborne() ? "goes down"
                                : "jumps into").c_str()
```

主語等を別途結合する部分文。日本語の語順・文法を含む表示経路の改修が必要。

## 7. L1482 — 未訳・API未接続

呼出: `mpr` / [原本 L1482](../../crawl-ref/source/mon-behv.cc#L1482)

### 原文（静的キー）

```text
The shaft crumbles and collapses.
```

### 日本語

未訳（英語にフォールバック）。

## 8. L1499 — 動的・未対応式（要調査・要改修）

呼出: `simple_monster_message` / [原本 L1499](../../crawl-ref/source/mon-behv.cc#L1499)

### 未解決の式（断片を翻訳キーにしない）

```text
make_stringf(" donates %s equipment to the cause.",
                        mon->pronoun(PRONOUN_POSSESSIVE).c_str()).c_str()
```

主語等を別途結合する部分文。日本語の語順・文法を含む表示経路の改修が必要。
