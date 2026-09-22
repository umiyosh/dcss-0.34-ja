# コード内メッセージの翻訳レビュー

[翻訳レビュー入口](../README.md)

[指摘方法](../../crawl-ref/docs/develop/translation-review.md) / [翻訳の問題を報告](https://github.com/umiyosh/dcss-0.34-ja/issues/new?template=translation-review.yml)

原本からの自動生成。1ファイルをメタIssueとし、到達性・表示経路を確認した未訳3エントリーずつを子Issue・PRにする。

認識した呼出 4108 / 静的キー 3705 / 動的・未対応式 403 / 翻訳API参照 7。

同じ文の複数呼出も各行に載せるため、件数は翻訳すべき文章の総数・完了率ではない。

## 抽出範囲と限界

- C++: `crawl-ref/source/*.cc`, `*.h` の `mpr`, `mprf`, `simple_monster_message`, `simple_god_message`, `wu_jian_sifu_message` と `jtrans` / `jtransf` / `jtrans_format`。
- Lua: `crawl-ref/source/dat/**/*.lua` の `crawl.mpr`, `crawl.jtrans`, `crawl.jtrans_format`。
- コメント・引用・括弧を区別した字句解析。C++の連結リテラル、raw文字列、Luaの長い文字列を認識する。コンパイラではない。
- 条件式、変数、文字列の動的結合、書式引数、未知の構文は原式を残して要調査とする。C++ mprfの型解決はしないため、チャネル変数等のoverloadは未解決になり得る。
- 対象外: 上記以外の関数、マクロ展開、C++サブディレクトリ、Luaを埋め込む.des等、UI/メニュー、Tiles/WebTiles独自表示。この一覧だけで全表示の網羅・到達性を保証しない。
- 訳ありでもAPI未接続ならゲーム表示は変わらない。API接続済みでも人間の採用・実表示確認は別途必要。
- 辞書は `crawl-ref/source/dat/database/ja/messages.txt`。原文キーは大文字小文字・前後空白を維持し、改行等をescapeする。
- 行末空白を含む値は、空白を失わないJSON表記で表示する。通常の文はtext表記とし、原本・翻訳キーは変更しない。
- 再生成: `python3 crawl-ref/source/util/translation_review.py`。

## ファイル別

| 原本 | 静的キー | 動的・未対応式 | 翻訳API参照 |
| --- | ---: | ---: | ---: |
| [ability.cc](ability.cc.md) | 92 | 7 | 0 |
| [abyss.cc](abyss.cc.md) | 14 | 0 | 0 |
| [acquire.cc](acquire.cc.md) | 11 | 0 | 0 |
| [actor.cc](actor.cc.md) | 10 | 0 | 0 |
| [adjust.cc](adjust.cc.md) | 8 | 0 | 0 |
| [areas.cc](areas.cc.md) | 7 | 0 | 0 |
| [arena.cc](arena.cc.md) | 17 | 3 | 0 |
| [art-func.h](art-func.h.md) | 44 | 4 | 0 |
| [artefact.cc](artefact.cc.md) | 1 | 0 | 0 |
| [attack.cc](attack.cc.md) | 12 | 1 | 0 |
| [attitude-change.cc](attitude-change.cc.md) | 2 | 2 | 0 |
| [beam.cc](beam.cc.md) | 142 | 12 | 0 |
| [behold.cc](behold.cc.md) | 6 | 0 | 0 |
| [chardump.cc](chardump.cc.md) | 3 | 0 | 0 |
| [cloud.cc](cloud.cc.md) | 12 | 0 | 0 |
| [clua.cc](clua.cc.md) | 1 | 0 | 0 |
| [command.cc](command.cc.md) | 4 | 0 | 0 |
| [ctest.cc](ctest.cc.md) | 3 | 0 | 0 |
| [dactions.cc](dactions.cc.md) | 6 | 0 | 0 |
| [dat/clua/autofight.lua](dat/clua/autofight.lua.md) | 7 | 4 | 0 |
| [dat/clua/automagic.lua](dat/clua/automagic.lua.md) | 10 | 2 | 0 |
| [dat/clua/delays.lua](dat/clua/delays.lua.md) | 0 | 2 | 0 |
| [dat/dlua/init.lua](dat/dlua/init.lua.md) | 0 | 2 | 0 |
| [dat/dlua/layout/geoelf.lua](dat/dlua/layout/geoelf.lua.md) | 42 | 2 | 0 |
| [dat/dlua/layout/geoelf_corridors.lua](dat/dlua/layout/geoelf_corridors.lua.md) | 12 | 1 | 0 |
| [dat/dlua/layout/geoelf_rooms.lua](dat/dlua/layout/geoelf_rooms.lua.md) | 8 | 4 | 0 |
| [dat/dlua/lm_door.lua](dat/dlua/lm_door.lua.md) | 0 | 2 | 0 |
| [dat/dlua/lm_fog.lua](dat/dlua/lm_fog.lua.md) | 0 | 8 | 0 |
| [dat/dlua/lm_mon_prop.lua](dat/dlua/lm_mon_prop.lua.md) | 1 | 0 | 0 |
| [dat/dlua/lm_monst.lua](dat/dlua/lm_monst.lua.md) | 0 | 2 | 0 |
| [dat/dlua/lm_timed.lua](dat/dlua/lm_timed.lua.md) | 1 | 2 | 1 |
| [dat/dlua/lm_tmsg.lua](dat/dlua/lm_tmsg.lua.md) | 0 | 1 | 0 |
| [dat/dlua/lm_trig.lua](dat/dlua/lm_trig.lua.md) | 1 | 1 | 0 |
| [dat/dlua/lm_trove.lua](dat/dlua/lm_trove.lua.md) | 16 | 25 | 0 |
| [dat/dlua/sprint.lua](dat/dlua/sprint.lua.md) | 0 | 1 | 0 |
| [dat/dlua/tutorial.lua](dat/dlua/tutorial.lua.md) | 0 | 2 | 0 |
| [dat/dlua/util.lua](dat/dlua/util.lua.md) | 0 | 1 | 0 |
| [dat/lua-wiz/damtally.lua](dat/lua-wiz/damtally.lua.md) | 0 | 1 | 0 |
| [database.cc](database.cc.md) | 7 | 1 | 1 |
| [dbg-asrt.cc](dbg-asrt.cc.md) | 8 | 0 | 0 |
| [dbg-maps.cc](dbg-maps.cc.md) | 6 | 0 | 0 |
| [dbg-scan.cc](dbg-scan.cc.md) | 36 | 0 | 0 |
| [dbg-util.cc](dbg-util.cc.md) | 16 | 4 | 0 |
| [death-curse.cc](death-curse.cc.md) | 2 | 4 | 0 |
| [decks.cc](decks.cc.md) | 23 | 3 | 0 |
| [delay.cc](delay.cc.md) | 43 | 1 | 0 |
| [delay.h](delay.h.md) | 8 | 0 | 0 |
| [describe-god.cc](describe-god.cc.md) | 1 | 0 | 0 |
| [dgl-message.cc](dgl-message.cc.md) | 6 | 1 | 0 |
| [dgn-overview.cc](dgn-overview.cc.md) | 8 | 2 | 0 |
| [dgn-shoals.cc](dgn-shoals.cc.md) | 4 | 0 | 0 |
| [directn.cc](directn.cc.md) | 34 | 1 | 0 |
| [dungeon.cc](dungeon.cc.md) | 27 | 0 | 0 |
| [duration-data.h](duration-data.h.md) | 12 | 0 | 0 |
| [end.cc](end.cc.md) | 2 | 0 | 0 |
| [evoke.cc](evoke.cc.md) | 31 | 1 | 0 |
| [exclude.cc](exclude.cc.md) | 2 | 0 | 0 |
| [fearmonger.cc](fearmonger.cc.md) | 2 | 0 | 0 |
| [files.cc](files.cc.md) | 33 | 1 | 0 |
| [fineff.cc](fineff.cc.md) | 23 | 6 | 0 |
| [ghost.cc](ghost.cc.md) | 1 | 0 | 0 |
| [glwrapper-ogl.cc](glwrapper-ogl.cc.md) | 8 | 0 | 0 |
| [god-abil.cc](god-abil.cc.md) | 178 | 10 | 0 |
| [god-blessing.cc](god-blessing.cc.md) | 0 | 1 | 0 |
| [god-companions.cc](god-companions.cc.md) | 16 | 2 | 0 |
| [god-conduct.cc](god-conduct.cc.md) | 9 | 4 | 0 |
| [god-passive.cc](god-passive.cc.md) | 16 | 0 | 0 |
| [god-prayer.cc](god-prayer.cc.md) | 6 | 0 | 0 |
| [god-wrath.cc](god-wrath.cc.md) | 49 | 10 | 0 |
| [hints.cc](hints.cc.md) | 12 | 0 | 0 |
| [hiscores.cc](hiscores.cc.md) | 1 | 0 | 0 |
| [initfile.cc](initfile.cc.md) | 33 | 0 | 0 |
| [invent.cc](invent.cc.md) | 4 | 0 | 0 |
| [item-name.cc](item-name.cc.md) | 1 | 0 | 0 |
| [item-prop.cc](item-prop.cc.md) | 1 | 1 | 0 |
| [item-use.cc](item-use.cc.md) | 67 | 19 | 0 |
| [items.cc](items.cc.md) | 48 | 13 | 0 |
| [l-colour.cc](l-colour.cc.md) | 1 | 0 | 0 |
| [l-crawl.cc](l-crawl.cc.md) | 2 | 3 | 2 |
| [l-debug.cc](l-debug.cc.md) | 2 | 0 | 0 |
| [l-dgn.cc](l-dgn.cc.md) | 1 | 0 | 0 |
| [l-dgnmon.cc](l-dgnmon.cc.md) | 2 | 0 | 0 |
| [l-item.cc](l-item.cc.md) | 3 | 0 | 0 |
| [l-you.cc](l-you.cc.md) | 2 | 0 | 0 |
| [luaterp.cc](luaterp.cc.md) | 4 | 0 | 0 |
| [macro.cc](macro.cc.md) | 11 | 1 | 0 |
| [main.cc](main.cc.md) | 72 | 1 | 0 |
| [makeitem.cc](makeitem.cc.md) | 4 | 0 | 0 |
| [map-knowledge.cc](map-knowledge.cc.md) | 3 | 0 | 0 |
| [mapdef.cc](mapdef.cc.md) | 9 | 0 | 0 |
| [mapmark.cc](mapmark.cc.md) | 9 | 0 | 0 |
| [maps.cc](maps.cc.md) | 8 | 0 | 0 |
| [melee-attack.cc](melee-attack.cc.md) | 93 | 6 | 0 |
| [message-stream.cc](message-stream.cc.md) | 1 | 1 | 0 |
| [message.cc](message.cc.md) | 41 | 1 | 3 |
| [misc.cc](misc.cc.md) | 3 | 0 | 0 |
| [mon-abil.cc](mon-abil.cc.md) | 25 | 2 | 0 |
| [mon-act.cc](mon-act.cc.md) | 55 | 5 | 0 |
| [mon-aura.cc](mon-aura.cc.md) | 2 | 0 | 0 |
| [mon-behv.cc](mon-behv.cc.md) | 5 | 3 | 0 |
| [mon-cast.cc](mon-cast.cc.md) | 100 | 21 | 0 |
| [mon-clone.cc](mon-clone.cc.md) | 6 | 0 | 0 |
| [mon-death.cc](mon-death.cc.md) | 59 | 15 | 0 |
| [mon-ench.cc](mon-ench.cc.md) | 90 | 4 | 0 |
| [mon-explode.cc](mon-explode.cc.md) | 1 | 0 | 0 |
| [mon-movetarget.cc](mon-movetarget.cc.md) | 15 | 0 | 0 |
| [mon-pathfind.cc](mon-pathfind.cc.md) | 13 | 0 | 0 |
| [mon-place.cc](mon-place.cc.md) | 11 | 0 | 0 |
| [mon-poly.cc](mon-poly.cc.md) | 7 | 1 | 0 |
| [mon-project.cc](mon-project.cc.md) | 14 | 1 | 0 |
| [mon-speak.cc](mon-speak.cc.md) | 0 | 1 | 0 |
| [mon-tentacle.cc](mon-tentacle.cc.md) | 11 | 0 | 0 |
| [mon-transit.cc](mon-transit.cc.md) | 1 | 0 | 0 |
| [mon-util.cc](mon-util.cc.md) | 8 | 3 | 0 |
| [monster.cc](monster.cc.md) | 66 | 15 | 0 |
| [movement.cc](movement.cc.md) | 38 | 2 | 0 |
| [mutation.cc](mutation.cc.md) | 22 | 1 | 0 |
| [nearby-danger.cc](nearby-danger.cc.md) | 4 | 0 | 0 |
| [ng-init.cc](ng-init.cc.md) | 5 | 0 | 0 |
| [notes.cc](notes.cc.md) | 1 | 0 | 0 |
| [orb.cc](orb.cc.md) | 7 | 0 | 0 |
| [ouch.cc](ouch.cc.md) | 37 | 2 | 0 |
| [player-act.cc](player-act.cc.md) | 8 | 1 | 0 |
| [player-equip.cc](player-equip.cc.md) | 126 | 3 | 0 |
| [player-notices.cc](player-notices.cc.md) | 4 | 2 | 0 |
| [player-reacts.cc](player-reacts.cc.md) | 31 | 2 | 0 |
| [player-stats.cc](player-stats.cc.md) | 6 | 3 | 0 |
| [player.cc](player.cc.md) | 172 | 19 | 0 |
| [potion.cc](potion.cc.md) | 34 | 3 | 0 |
| [prompt.cc](prompt.cc.md) | 5 | 0 | 0 |
| [quiver.cc](quiver.cc.md) | 21 | 1 | 0 |
| [randbook.cc](randbook.cc.md) | 3 | 0 | 0 |
| [ranged-attack.cc](ranged-attack.cc.md) | 11 | 1 | 0 |
| [religion.cc](religion.cc.md) | 78 | 22 | 0 |
| [shopping.cc](shopping.cc.md) | 9 | 0 | 0 |
| [shout.cc](shout.cc.md) | 21 | 1 | 0 |
| [show.cc](show.cc.md) | 1 | 0 | 0 |
| [skill-menu.cc](skill-menu.cc.md) | 1 | 0 | 0 |
| [skills.cc](skills.cc.md) | 11 | 0 | 0 |
| [species.cc](species.cc.md) | 1 | 0 | 0 |
| [spl-book.cc](spl-book.cc.md) | 15 | 1 | 0 |
| [spl-cast.cc](spl-cast.cc.md) | 36 | 4 | 0 |
| [spl-clouds.cc](spl-clouds.cc.md) | 7 | 0 | 0 |
| [spl-damage.cc](spl-damage.cc.md) | 92 | 9 | 0 |
| [spl-goditem.cc](spl-goditem.cc.md) | 31 | 2 | 0 |
| [spl-miscast.cc](spl-miscast.cc.md) | 1 | 1 | 0 |
| [spl-monench.cc](spl-monench.cc.md) | 18 | 2 | 0 |
| [spl-other.cc](spl-other.cc.md) | 23 | 2 | 0 |
| [spl-selfench.cc](spl-selfench.cc.md) | 18 | 1 | 0 |
| [spl-summoning.cc](spl-summoning.cc.md) | 139 | 3 | 0 |
| [spl-transloc.cc](spl-transloc.cc.md) | 62 | 3 | 0 |
| [spl-util.cc](spl-util.cc.md) | 4 | 0 | 0 |
| [spl-vortex.cc](spl-vortex.cc.md) | 4 | 0 | 0 |
| [stairs.cc](stairs.cc.md) | 58 | 4 | 0 |
| [startup.cc](startup.cc.md) | 0 | 3 | 0 |
| [stash.cc](stash.cc.md) | 4 | 0 | 0 |
| [state.cc](state.cc.md) | 0 | 2 | 0 |
| [tags.cc](tags.cc.md) | 24 | 0 | 0 |
| [target-compass.cc](target-compass.cc.md) | 2 | 0 | 0 |
| [teleport.cc](teleport.cc.md) | 6 | 1 | 0 |
| [terrain.cc](terrain.cc.md) | 7 | 2 | 0 |
| [throw.cc](throw.cc.md) | 4 | 1 | 0 |
| [tiledgnbuf.cc](tiledgnbuf.cc.md) | 0 | 1 | 0 |
| [tilereg-skl.cc](tilereg-skl.cc.md) | 3 | 0 | 0 |
| [tilesdl.cc](tilesdl.cc.md) | 2 | 0 | 0 |
| [tileweb.cc](tileweb.cc.md) | 1 | 0 | 0 |
| [timed-effects.cc](timed-effects.cc.md) | 19 | 0 | 0 |
| [transform.cc](transform.cc.md) | 19 | 5 | 0 |
| [traps.cc](traps.cc.md) | 60 | 4 | 0 |
| [travel.cc](travel.cc.md) | 35 | 5 | 0 |
| [view.cc](view.cc.md) | 2 | 1 | 0 |
| [viewmap.cc](viewmap.cc.md) | 5 | 0 | 0 |
| [windowmanager-sdl.cc](windowmanager-sdl.cc.md) | 2 | 0 | 0 |
| [wiz-dgn.cc](wiz-dgn.cc.md) | 32 | 3 | 0 |
| [wiz-dump.cc](wiz-dump.cc.md) | 3 | 0 | 0 |
| [wiz-fsim.cc](wiz-fsim.cc.md) | 12 | 6 | 0 |
| [wiz-item.cc](wiz-item.cc.md) | 54 | 4 | 0 |
| [wiz-mon.cc](wiz-mon.cc.md) | 68 | 4 | 0 |
| [wiz-you.cc](wiz-you.cc.md) | 57 | 1 | 0 |
| [wizard.cc](wizard.cc.md) | 13 | 0 | 0 |
| [xom.cc](xom.cc.md) | 58 | 4 | 0 |
| [zot.cc](zot.cc.md) | 11 | 0 | 0 |
