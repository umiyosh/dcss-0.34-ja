# コードメッセージ: `god-blessing.cc`

[コードメッセージ一覧](README.md)

自動生成。原本・辞書を変更して共通生成コマンドで更新する。
API接続済みは採用済み・実表示確認済みを意味しない。

## 1. L159 — 動的・未対応式（要調査・要改修）

呼出: `simple_god_message` / [原本 L159](../../crawl-ref/source/god-blessing.cc#L159)

### 未解決の式（断片を翻訳キーにしない）

```text
make_stringf(" blesses %s with %s.",
                                    whom.c_str(), blessing.c_str()).c_str()
```

主語等を別途結合する部分文。日本語の語順・文法を含む表示経路の改修が必要。
