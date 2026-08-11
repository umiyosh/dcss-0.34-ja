# Repository Guidelines

## Project Purpose

このリポジトリは Dungeon Crawl Stone Soup 0.34 の日本語版を作るための
翻訳プロジェクトである。会話、Issue、PR、レビューは日本語で行う。

upstream 由来の `crawl-ref/source/dat/descript/ja/` には旧い部分訳が残って
いるが、本プロジェクトで検証・採用済みの翻訳とはみなさない。0.34 の英語原文、
実装、ゲーム内到達性と照合してから再利用する。

## Repository Layout

- `crawl-ref/source/`: C++ 本体、Lua、ビルド用 `Makefile`
- `crawl-ref/source/dat/descript/*.txt`: 現行の英語説明と翻訳キー
- `crawl-ref/source/dat/descript/ja/*.txt`: 日本語訳の配置先
- `crawl-ref/source/dat/database/`: 会話、名称、ヘルプなどの実行時テキスト
- `crawl-ref/docs/develop/translation.txt`: upstream の翻訳形式
- `crawl-ref/docs/`: プレイヤー向け・開発者向け文書
- `.github/workflows/ci.yml`: 正規のビルド・テストマトリクス

## Translation Rules

1. 翻訳対象は未訳件数だけで決めない。英語キーが0.34で有効か、対象がゲーム内で
   到達可能か、種別・unique性などの実装属性が何かを確認して範囲を確定する。
2. ファンタジー世界の語感を優先し、現代的・事務的な直訳を避ける。同じ固有名詞、
   種族、神、呪文、アイテム、状態には一貫した訳語を使う。
3. 旧版や既存 `ja/` の訳は、英語キーと本文の意味が一致する場合だけ候補として使う。
   版差分を確認せず機械的にコピーしない。
4. `%%%%`、英語キー、`<alias>`、`{{ ... }}`、書式指定子、タグ、改行の意味を
   保持する。キー名そのものは翻訳しない。
5. 引用文は原則として翻訳せず、原語と出典を保つ。翻訳を載せる場合は訳者情報も
   残す。詳細は `crawl-ref/docs/develop/translation.txt` に従う。
6. 説明文以外の表示を扱うときは、`dat/descript/ja/` だけを見て完了としない。
   実際の表示経路、C++/Lua、`dat/database/`、設定、Tiles/WebTiles を確認する。

## Worktree and Change Workflow

- default branch は `develop`。新規変更は `git fetch origin` 後の
  `origin/develop` から、リポジトリ直下の `.wt/` に専用 worktree を作る。
- primary checkout では編集・commitしない。既存の専用 worktree がある場合は
  その worktree と既存PRを継続する。
- 変更前に近い実装・翻訳を3〜5件確認し、命名、文体、データ形式を合わせる。
- 変更は翻訳テーマや到達可能な機能単位で小さく分ける。無関係な機械置換を混ぜない。
- ユーザーが調査のみ、PR不要、一時停止を指定しない限り、検証、commit、push、
  PR作成、GitHub Actions確認まで完遂する。mergeは明示確認なしに行わない。

## Validation

変更範囲に応じて、少なくとも次を確認する。

- 全変更: `git diff --check`
- テキスト・ソース変更: `crawl-ref/source/util/checkwhite -n <changed-files>`
- 翻訳変更: 英語キーとの対応、区切り、alias、Lua、書式指定子を差分で確認する
- プレイヤー表示変更: Console または Tiles を `language = ja` で起動し、対象画面を
  実際に確認する
- C++/Lua変更: 影響するビルドとテストをローカルで実行する
- PR後: `.github/workflows/ci.yml` の GitHub Actions が成功するまで確認する

`crawl-ref/source/util/txc` は現状 Python 2 構文を含み、Python 3 では実行できない。
修正されるまでは検証済み扱いの根拠にしない。

代表的なコマンド:

```sh
make -C crawl-ref/source -j4
make -C crawl-ref/source TILES=y -j4
make -C crawl-ref/source FULLDEBUG=1 -j4
make -C crawl-ref/source FULLDEBUG=1 test
```

ビルドした実行ファイルは `dat/` と `docs/` を解決できるよう、通常は
`crawl-ref/source/` を作業ディレクトリとして起動する。

## Commits and Pull Requests

- Conventional Commits 1.0.0 に従い、英語の命令形タイトルを使う。
- PR本文は日本語で、変更理由、主な変更、実行した検証、未検証事項、関連Issueを
  記載する。
- 翻訳PRでは対象範囲の決め方、採用した既存訳、意図的に対象外とした項目を明示する。
- 画面上の表示を変えた場合だけ、必要に応じてスクリーンショットを添える。
