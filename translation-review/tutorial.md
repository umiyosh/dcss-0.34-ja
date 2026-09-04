# `tutorial.txt` 翻訳レビュー

> このファイルは自動生成です。直接編集せず、英語・日本語resourceを更新してください。
> 再生成: `python3 crawl-ref/source/util/translation_review.py`

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- Japanese resource: `crawl-ref/source/dat/descript/ja/tutorial.txt`
- Entries: 88
- Translated: 81
- Untranslated: 7

## Entry 1

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial intro`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:2`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:2`

### English

```text
You can reread all messages at any time with
<input>$cmd[CMD_REPLAY_MESSAGES]</input>. Also, press <input>Space</input>
<localtiles> or <input>left click</input> with mouse</localtiles> to clear the
<cyan>--more--</cyan> prompts.
```

### 日本語

```text
<input>$cmd[CMD_REPLAY_MESSAGES]</input>
でいつでもメッセージを読み返すことができます。そして、
<cyan>--more--</cyan>表示を<input>Space</input>を押してクリアしてください。
```

---

## Entry 2

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial death`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:9`
- Japanese source: 未訳

### English

```text
You die...

In Crawl, death is a sad but common occurrence. Note that there's usually
something you could have done to survive, for example by using some kind of
item, running away, resting between fights, or by avoiding combat entirely.
Keep trying, eventually you'll prevail!
```

### 日本語

```text
（未訳）
```

---

## Entry 3

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 start`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:22`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:8`

### English

```text
In this lesson you're going to learn how to move around and explore a level.
You can move <localtiles>by clicking somewhere with your <input>Mouse</input>,
or </localtiles>with the <input>arrow keys</input>.
```

### 日本語

```text
このレッスンでは移動の方法と階層の探索について学んでもらいます。
あなたは任意の地点<localtiles>を<input>マウス</input>でクリックするか、
任意の方向<localtiles>に<input>矢印キー</input>を使って移動出来ます。
```

---

## Entry 4

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 go_on`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:28`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:14`

### English

```text
You're doing great! Now, explore a bit until you reach the next blue square.
```

### 日本語

```text
素晴らしい!では次の青いパネルまでもう少し探索を続けてください。
```

---

## Entry 5

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 diagonal`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:32`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:18`

### English

```text
:nowrap
Move diagonally with the <input>number pad</input> (try Numlock on/off)<localtiles>,</localtiles> <console>or the </console><input>vi keys</input><console>.</console><localtiles>, or <input>mouse</input>.</localtiles>

  Numpad:     <w>7 8 9</w>       vi-keys: <w>   $cmd[CMD_MOVE_UP_LEFT] $cmd[CMD_MOVE_UP] $cmd[CMD_MOVE_UP_RIGHT]</w><localtiles>    Mouse:     <w>click</w> on the floor</localtiles>
               \|/                     \|/
              <w>4</w>-<w>.</w>-<w>6</w> <w>                  $cmd[CMD_MOVE_LEFT]</w>-<w>.</w>-<w>$cmd[CMD_MOVE_RIGHT]</w>
               /|\                     /|\
              <w>1 2 3</w> <w>                  $cmd[CMD_MOVE_DOWN_LEFT] $cmd[CMD_MOVE_DOWN] $cmd[CMD_MOVE_DOWN_RIGHT]</w>
```

### 日本語

```text
:nowrap
あなたは<input>テンキー</input> (Numlockキーで切り替え)または、<input>viキー</input> を使って斜め方向に移動できます。

  テンキー:     <w>7 8 9</w>             viキー:   <w>$cmd[CMD_MOVE_UP_LEFT] $cmd[CMD_MOVE_UP] $cmd[CMD_MOVE_UP_RIGHT]</w>
                 \|/                         \|/
                <w>4</w>-<w>.</w>-<w>6</w> <w>                      $cmd[CMD_MOVE_LEFT]</w>-<w>.</w>-<w>$cmd[CMD_MOVE_RIGHT]</w>
                 /|\                         /|\
                <w>1 2 3</w> <w>                      $cmd[CMD_MOVE_DOWN_LEFT] $cmd[CMD_MOVE_DOWN] $cmd[CMD_MOVE_DOWN_RIGHT]</w>

<localtiles>同様に<input>マウスクリック</input>でも移動することが可能です</localtiles>
```

---

## Entry 6

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 shiftmove`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:43`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:31`

### English

```text
A quicker way to “run” through a corridor is to press <input>Shift</input>
along with the <input>number pad</input> (try Numlock on/off) or <input>vi
keys</input>.
```

### 日本語

```text
通路を素早く『走って』移動するには<input>Shift</input>を押しながら、
<input>テンキー</input>(Numlockキーで切り替え)、
または<input>viキー</input>を押してください。
```

---

## Entry 7

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 downstairs`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:49`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:37`

### English

```text
When standing on a staircase leading downwards, you can enter the next level
with <input>$cmd[CMD_GO_DOWNSTAIRS]</input><localtiles> or with
a <input>left click</input> on your character</localtiles>.
```

### 日本語

```text
下り階段の上に立っているとき、<input>$cmd[CMD_GO_DOWNSTAIRS]</input>
<localtiles> を押すか、
キャラクターの上で<input>Shift+クリック</input>を押すことで次の階層へ移動します。
```

---

## Entry 8

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 levelmap`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:55`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:43`

### English

```text
What's this? To find out where you are, <tiles>have a look at the
<w>minimap</w> to the right of the screen.</tiles><localtiles> You can have a
closer look at a part of the map with a <input>right mouse click</input> and
also can travel there with a <input>left click</input>.</localtiles><webtiles>
You can </webtiles><nomouse>enter the overmap view with
<input>$cmd[CMD_DISPLAY_MAP]</input> and then move the cursor around to look
around the level. You also can travel wherever your cursor is pointing by
pressing <input>.</input> or <input>Enter</input>. Press <input>Escape</input>
to return to the normal game mode.</nomouse>
```

### 日本語

```text
これは何事だ？あなたが何処にいるかを知るには、
<tiles>画面右の<w>ミニマップ</w>を見てください。</tiles>
<localtiles>あなたはマップを<input>右クリック</input>で詳細に見ることができ、
<input>左クリック</input>で指定した地点までトラベルすることができます。
</localtiles><webtiles></webtiles>
 <nomouse><input>$cmd[CMD_DISPLAY_MAP]</input>で階層マップが閲覧でき、
カーソルを動かしてマップを見渡すことができます。<input>.</input>、
または<input>Enter</input>を押すことで、
カーソルのある地点までトラベルすることもできます。
<input>Escape</input>を押すと通常のゲームモードに戻ります。</nomouse>
```

---

## Entry 9

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 autoexplore`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:67`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:56`

### English

```text
Exploring manually can get tedious after a while, so you might want to let that
happen automatically. Try it by pressing <input>$cmd[CMD_EXPLORE]</input>
<localtiles>, or by clicking on 'autoexplore', the first button in the command
bar below the minimap.</localtiles>.
```

### 日本語

```text
ゲームに慣れてくると手動での探索が面倒に思えて、
自動で探索できないものかと思うかもしれません。
<input>$cmd[CMD_EXPLORE]</input>を押して見てください。
```

---

## Entry 10

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 exclusion`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:74`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:62`

### English

```text
Some dangerous ground is marked with <w>exclusions</w>. Autotravel
<localtiles>(including <input>mouseclick</input>!) </localtiles>will not lead
you into exclusions. Instead you will automatically stop.

However, autoexplore will move you safely around exclusions: so, you can safely
continue by pressing <input>$cmd[CMD_EXPLORE]</input>.
```

### 日本語

```text
幾らかの危険な地形は <w>exclusions</w> でマークされています。
自動探索では<localtiles>(<input>マウスクリック</input>も含めて!)
</localtiles>除外エリアに侵入することはできません。

しかし、自動探索では安全に除外エリア付近を移動するので、
もう一度<input>$cmd[CMD_EXPLORE]</input>を押して探索を続けてください。
```

---

## Entry 11

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 autoexplore_announce`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:83`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:71`

### English

```text
Autoexplore will stop when you first see items or dungeon features, like these
stairs. To travel directly to the stairs, you can
<localtiles><input>click</input> on them; or you can </localtiles>press
<input>$cmd[CMD_DISPLAY_MAP]</input> to enter the map overview, then
<input><<</input> to move the cursor to the nearest up-stairs, and
<input>Enter</input> to go there.
```

### 日本語

```text
自動探索は施設やアイテムの存在を知らせるため停止することがあります。
階段へ直接移動するには、<localtiles>階段を<input>クリック</input>するか、
</localtiles><input>$cmd[CMD_DISPLAY_MAP] << Enter</input>を押してください。
```

---

## Entry 12

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 tutorial_end`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:92`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:77`

### English

```text
Congratulations! You've completed the first lesson!

To exit the tutorial, simply go up these stairs with
<input>$cmd[CMD_GO_UPSTAIRS]</input><localtiles> or by
<input>left clicking</input> on your character</localtiles>. Confirm the
resulting prompt with an uppercase <input>Y</input>.
```

### 日本語

```text
おめでとう！あなたは最初のレッスンをやり遂げました！

チュートリアルを終了するには、<input>$cmd[CMD_GO_UPSTAIRS]</input>
<localtiles>か、キャラクターの上で<input>Shift+クリック</input>
</localtiles>で階段を上ってください。
その際に現れる入力プロンプトには大文字の<input>Y</input>を入力してください。
```

---

## Entry 13

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 newlevel`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:101`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:86`

### English

```text
A new level! To begin with, head over to that door to the right.

Also, remember: You can reread old messages with
<input>$cmd[CMD_REPLAY_MESSAGES]</input>.
```

### 日本語

```text
新しい階層へようこそ！まずは右手のドアの先へ行きましょう。

<input>$cmd[CMD_REPLAY_MESSAGES]</input>で前のメッセージを読み返せることも覚えておいてください。
```

---

## Entry 14

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 door`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:108`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:92`

### English

```text
You can open a closed door by walking into it.
```

### 日本語

```text
閉じたドアはその方向へ移動することによって開けることが可能です。
```

---

## Entry 15

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 close_door`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:112`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:96`

### English

```text
To close an open door, press <input>$cmd[CMD_CLOSE_DOOR]</input>.
```

### 日本語

```text
開いたドアを閉じるには、<input>$cmd[CMD_CLOSE_DOOR]</input> を押してください。
```

---

## Entry 16

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 water`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:116`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:100`

### English

```text
Note how you can move through shallow but not through deep water.
```

### 日本語

```text
浅い水たまりは歩いて渡れますが、
深い水は渡ることができないことに注意してください。
```

---

## Entry 17

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 upstairs`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:120`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:105`

### English

```text
When standing on a staircase leading upwards, you can enter the previous level
with <input>$cmd[CMD_GO_UPSTAIRS]</input><localtiles> or by
<input>left clicking</input> on your character</localtiles>.
```

### 日本語

```text
上り階段の上に立っているとき、<input>$cmd[CMD_GO_UPSTAIRS]</input>
<localtiles>を押す、
またはキャラクターの上で<input>Shift+クリック</input>を押すことで次の階層へ移動します。
```

---

## Entry 18

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial1 exit`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:126`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:111`

### English

```text
:nowrap
<white>Tutorial 1 summary: Movement</white>

<yellow>Movement commands</yellow>
   Numpad:       <w>7 8 9</w>           vi-keys:    <w>$cmd[CMD_MOVE_UP_LEFT] $cmd[CMD_MOVE_UP] $cmd[CMD_MOVE_UP_RIGHT]</w>
                  \|/                         \|/
                 <w>4</w>-<w>.</w>-<w>6</w>                       <w>$cmd[CMD_MOVE_LEFT]</w>-<w>.</w>-<w>$cmd[CMD_MOVE_RIGHT]</w>
                  /|\                         /|\
                 <w>1 2 3</w>                       <w>$cmd[CMD_MOVE_DOWN_LEFT] $cmd[CMD_MOVE_DOWN] $cmd[CMD_MOVE_DOWN_RIGHT]</w>

  <input>Shift + direction</input> moves you several squares in this direction.<localtiles>
  You also can move by <input>clicking</input> somewhere in sight or on the <w>minimap</w>.</localtiles>

<yellow>Staircases</yellow>
  <input>$cmd[CMD_GO_UPSTAIRS]</input>  go back to the previous level
  <input>$cmd[CMD_GO_DOWNSTAIRS]</input>  enter the next level
  <input>$cmd[CMD_DISPLAY_MAP]></input>/<input>$cmd[CMD_DISPLAY_MAP]<<</input> travel to the nearest up/downstairs

<yellow>Doors</yellow> can be opened by walking into them
  <input>$cmd[CMD_CLOSE_DOOR]</input>  close an open door

<yellow>Travel</yellow><localtiles>
  mouseclick on the <w>minimap</w></localtiles><nomouse>
  <input>$cmd[CMD_DISPLAY_MAP]</input>  enter the level map, travel with <input>Enter</input></nomouse>
  <input>$cmd[CMD_EXPLORE]</input>  autoexplore
```

### 日本語

```text
:nowrap
<yellow>移動コマンド</yellow>
  テンキー:      <w>7 8 9</w>             viキー:   <w>$cmd[CMD_MOVE_UP_LEFT] $cmd[CMD_MOVE_UP] $cmd[CMD_MOVE_UP_RIGHT]</w>
                  \|/                         \|/
                 <w>4</w>-<w>.</w>-<w>6</w>                       <w>$cmd[CMD_MOVE_LEFT]</w>-<w>.</w>-<w>$cmd[CMD_MOVE_RIGHT]</w>
                  /|\                         /|\
                 <w>1 2 3</w>                       <w>$cmd[CMD_MOVE_DOWN_LEFT] $cmd[CMD_MOVE_DOWN] $cmd[CMD_MOVE_DOWN_RIGHT]</w>

  <input>Shift + 方向</input> は指定した方向へ数マス移動します。<localtiles>
  視界内の任意の地点や <input>ミニマップ</input> を <input>クリック</input> しても移動出来ます。</localtiles>

<yellow>階段</yellow>
  <input>$cmd[CMD_GO_UPSTAIRS]</input>  上の階層へ移動する
  <input>$cmd[CMD_GO_DOWNSTAIRS]</input>  次の階層へ移動する
  <input>$cmd[CMD_DISPLAY_MAP]></input>/<input>$cmd[CMD_DISPLAY_MAP]<<</input>  最寄りの階段へトラベル

<yellow>ドア</yellow>
  ドアのある方向に移動することで開く
  <input>$cmd[CMD_CLOSE_DOOR]</input>  開いたドアを閉める

<yellow>トラベル</yellow><localtiles>
  <input>ミニマップ</input>上をクリック</localtiles><nomouse>
  <input>$cmd[CMD_DISPLAY_MAP]</input>  階層マップを開き、<input>Enter</input>でトラベル</nomouse>
  <input>$cmd[CMD_EXPLORE]</input>  自動探索

                                 <cyan>この画面は <input>任意のキー</input> を押すと終了します...</cyan>
```

---

## Entry 19

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 start`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:157`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:140`

### English

```text
This lesson will teach you about monsters and fighting. First, we need a
weapon! Go and grab the one lying over there.
```

### 日本語

```text
このレッスンではモンスターと戦闘について学びます。まず武器が必要です！
向こうに落ちている武器を拾ってみてください。
```

---

## Entry 20

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 pickup_weapon`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:162`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:145`

### English

```text
Pick up this weapon<localtiles> by clicking on it in the inventory panel, and
then wield it by clicking on it again. Alternatively, pick it up</localtiles>
with <input>$cmd[CMD_PICKUP]</input> or <input>g</input> and then wield it with
<input>$cmd[CMD_EQUIP]</input>.
```

### 日本語

```text
<input>$cmd[CMD_PICKUP]</input> または <input>g</input> を押して武器を拾い、
 <input>$cmd[CMD_WIELD_WEAPON]</input> で装備してください。<localtiles> また、
どちらの行動もインベントリパネルを <input>クリック</input> して実行できます。
</localtiles>
```

---

## Entry 21

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 melee`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:169`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:152`

### English

```text
To attack a monster with your bare hands or wielded weapon, simply walk into
it.
```

### 日本語

```text
素手か武器を用いてモンスターに攻撃するには、
単純にモンスターの方へ移動してください。
```

---

## Entry 22

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 resting`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:174`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:157`

### English

```text
Very good! You can heal by resting with <input>$cmd[CMD_REST]</input>
<localtiles>, or by clicking the 'rest' button in the command bar below the
minimap</localtiles>. This will make you rest until your health is full, but
will be interrupted by important events.
```

### 日本語

```text
よく出来ました!
<input>$cmd[CMD_REST]</input>で休息をとることでHPの減少を回復することができます。
これは100ターンの間休息を取りますが、様々な重大な出来事が起きると中断されます。
```

---

## Entry 23

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 wait`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:181`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:163`

### English

```text
Rather than storm the room and get swarmed by monsters, you can also step back
and wait (with <input>$cmd[CMD_WAIT]</input><localtiles> or by
<input>clicking</input> on your character</localtiles>) for them to come to you.
```

### 日本語

```text
突撃してモンスターに囲まれるのではなく、
一歩引いて彼らが近づいてくるまで待つ(<input>$cmd[CMD_WAIT]</input>)
こともできます。
```

---

## Entry 24

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 resting_reminder`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:187`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:169`

### English

```text
Remember, you can rest up with <input>$cmd[CMD_REST]</input>.
```

### 日本語

```text
<input>$cmd[CMD_REST]</input>で休息を取ることを忘れずに。
```

---

## Entry 25

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 compare_monster_desc`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:191`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:173`

### English

```text
Examine these monsters (<localtiles>via <input>mouseover</input></localtiles>
<nomouse>by pressing <input>$cmd[CMD_LOOK_AROUND]</input> to enter examine mode,
and then <input>$cmd[CMD_TARGET_CYCLE_FORWARD]</input> to cycle through nearby
monsters</nomouse>)
and compare their descriptions (<localtiles>with <input>rightmouseclick</input></localtiles>
<nomouse>by pressing <input>$cmd[CMD_TARGET_DESCRIBE]</input> while selecting
them in examine mode</nomouse>)
to find out which of these cages is safer to fight through.
```

### 日本語

```text
:nowrap
モンスターを調査して見ましょう。(<localtiles><input>マウスオーバー</input></localtiles><nomouse> <input>$cmd[CMD_LOOK_AROUND]$cmd[CMD_TARGET_CYCLE_FORWARD]</input>を押す</nomouse>)
そして両者の説明文を比べてみて、(<localtiles><input>右クリック</input></localtiles><nomouse><input>$cmd[CMD_LOOK_AROUND]$cmd[CMD_TARGET_DESCRIBE]</input></nomouse>) どちらの檻を押し通るべきか判断してください。
```

---

## Entry 26

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 downstairs`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:203`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:179`

### English

```text
Well done! After resting to full health continue to the next level with
<input>$cmd[CMD_GO_DOWNSTAIRS]</input><localtiles> or by <input>clicking</input>
on your character</localtiles>.
```

### 日本語

```text
よく出来ました！休憩をとって体力を全回復させてから、
<input>$cmd[CMD_GO_DOWNSTAIRS]</input>で次の階層へ移動してください。
```

---

## Entry 27

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 newlevel`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:209`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:184`

### English

```text
Remember: You can reread old messages with
<input>$cmd[CMD_REPLAY_MESSAGES]</input>.
```

### 日本語

```text
<input>$cmd[CMD_REPLAY_MESSAGES]</input>で前のメッセージを読み返すことができます、
お忘れなく。
```

---

## Entry 28

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 boomerangs`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:214`
- Japanese source: 未訳

### English

```text
Now, for ranged combat! Pick up these boomerangs with
<input>$cmd[CMD_PICKUP]</input> or <input>g</input><localtiles>, or by
<input>mouseclick</input>,</localtiles> and continue.
```

### 日本語

```text
（未訳）
```

---

## Entry 29

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 throwing`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:220`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:195`

### English

```text
You can fire your boomerangs at a monster with <input>$cmd[CMD_FIRE]</input>
<localtiles> or by <input>clicking</input> on them in the inventory
panel</localtiles>. To confirm the auto-targeted monster, press
<input>$cmd[CMD_TARGET_SELECT]</input> or <input>Enter</input>. You can skip
this and fire at the closest monster with <input>shift-tab</input> or <input>p</input>.
```

### 日本語

```text
<input>$cmd[CMD_FIRE]</input>を押して、
<localtiles>または持ち物欄の投げ矢を<input>クリック</input>して</localtiles>モンスターに投げ矢を発射することができます。
自動で選択されたモンスターに発射する場合、
<input>$cmd[CMD_TARGET_SELECT]</input>または<input>Enter</input>を押してください。
```

---

## Entry 30

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 wield_bow`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:228`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:202`

### English

```text
Pick up this shortbow and wield it with <input>$cmd[CMD_EQUIP]</input>
<localtiles> or by <input>mouseclick</input></localtiles>.
```

### 日本語

```text
弓を拾い、<input>$cmd[CMD_WIELD_WEAPON]</input>
<localtiles>または<input>マウスクリック</input></localtiles>で装備してください。
```

---

## Entry 31

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 firing`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:233`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:207`

### English

```text
Firing arrows from your wielded shortbow works a bit differently from throwing boomerangs.
Use <input>$cmd[CMD_PRIMARY_ATTACK]</input><localtiles> or <input>mouseclick</input>
</localtiles>. You can change the targeted monster by pressing
<input>$cmd[CMD_TARGET_CYCLE_FORWARD]</input> while in target mode. The worm is
harmless behind the lava, so concentrate on the dummy which can fire at you.
Again, confirm your choice with <input>$cmd[CMD_TARGET_SELECT]</input> or
<input>Enter</input>.
```

### 日本語

```text
装備した弓を用いて矢を打ち出すことは投げ矢を投げることと同様に<input>$cmd[CMD_FIRE]</input>
<localtiles>、または<input>クリック</input></localtiles> から行います。
ターゲットモード中に<input>$cmd[CMD_TARGET_CYCLE_FORWARD]</input>を押すことで、
対象になるモンスターを変更することが出来ます。
ワームは溶岩の先にいて無害ですので、
あなたに攻撃してくるダミーに集中して攻撃しましょう。
攻撃を開始するには<input>$cmd[CMD_TARGET_SELECT]</input>、
または<input>Enter</input>を押して下さい。
```

---

## Entry 32

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 travel_reminder`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:244`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:218`

### English

```text
Remember that you can autoexplore using <input>$cmd[CMD_EXPLORE]</input>.
```

### 日本語

```text
<input>$cmd[CMD_EXPLORE]</input>で自動探索ができることを覚えておきましょう。
```

---

## Entry 33

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 explore`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:248`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:222`

### English

```text
Find the exit! Remember that you can autoexplore using
<input>$cmd[CMD_EXPLORE]</input>.
```

### 日本語

```text
出口を探せ!<input>$cmd[CMD_EXPLORE]</input>で自動探索ができます。
```

---

## Entry 34

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 tutorial_end`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:253`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:226`

### English

```text
Congratulations! You've survived your first batch of monsters! To exit the
tutorial, simply go down these stairs.
```

### 日本語

```text
おめでとうございます!あなたはモンスターの群れから生き延びました!
チュートリアルを終了するには階段を降りて下さい。
```

---

## Entry 35

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial2 exit`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:258`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:231`

### English

```text
:nowrap
<white>Tutorial 2 summary: Combat</white>

<yellow>Weapons<console> <cyan>)</cyan></console></yellow>
  <input>$cmd[CMD_PICKUP]</input>  pick up an item
  <input>$cmd[CMD_EQUIP]</input>  equip an item<localtiles>
  You can also do this by <input>clicking</input> on the weapon in your inventory.</localtiles>
  <input>$cmd[CMD_QUIVER_ITEM]</input>  adjust your quiver

<yellow>Monsters</yellow><localtiles>
  <input>mouseover</input>  examine a monster
  <input>rightclick</input> read a more detailed description</localtiles><nomouse>
  <input>$cmd[CMD_LOOK_AROUND]</input>  examine a monster
  <input>$cmd[CMD_LOOK_AROUND]$cmd[CMD_TARGET_DESCRIBE]</input> read a more detailed description</nomouse>
  <input>$cmd[CMD_PRIMARY_ATTACK]</input> fire held weapon
  <input>$cmd[CMD_FIRE]$cmd[CMD_TARGET_SELECT]</input> fire quiver at pre-targeted monster
  <input>shift-tab</input>, <input>p</input> fire quiver at closest monster
  <input>$cmd[CMD_FIRE]$cmd[CMD_TARGET_CYCLE_FORWARD]</input> target another monster<localtiles>
  You can also fire a missile by <input>clicking</input> on it, then confirming the target with <input>Enter</input>.</localtiles>

<yellow>Resting</yellow>
  <input>$cmd[CMD_WAIT]</input>  wait and rest a single turn
  <input>$cmd[CMD_REST]</input>  wait and rest up to 100 turns
```

### 日本語

```text
:nowrap
<yellow>武器<console> <cyan>)</cyan></console></yellow>
  <input>$cmd[CMD_PICKUP]</input>  アイテムを拾う
  <input>$cmd[CMD_WIELD_WEAPON]</input>  武器を装備する<localtiles>
  インベントリ内の武器を <input>クリック</input> しても可能です。</localtiles>

<yellow>モンスター</yellow><localtiles>
  <input>マウスオーバー</input> モンスターを調べる
  <input>右クリック</input> 詳しい説明を読む</localtiles><nomouse>
  <input>$cmd[CMD_LOOK_AROUND]</input>  モンスターを調べる
  <input>$cmd[CMD_LOOK_AROUND]$cmd[CMD_TARGET_DESCRIBE]</input> 詳しい説明を読む</nomouse>
  <input>$cmd[CMD_FIRE]$cmd[CMD_TARGET_SELECT]</input> ターゲットに射撃
  <input>$cmd[CMD_FIRE]$cmd[CMD_TARGET_CYCLE_FORWARD]</input> ターゲット切り替え<localtiles>
  インベントリ内の矢弾を <input>クリック</input> することでも射撃ができ、 <input>Enter</input>でターゲットを決定できます。</localtiles>

<yellow>休息</yellow>
  <input>$cmd[CMD_WAIT]</input>  1ターン待機して休息する
  <input>$cmd[CMD_REST]</input>  100ターン待機して休息する

                                 <cyan>この画面は <input>任意のキー</input> を押すと終了します...</cyan>
```

---

## Entry 36

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 start`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:287`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:254`

### English

```text
In this lesson you're going to learn about items and how to use them.
```

### 日本語

```text
このレッスンではアイテムとその使い方について学んでいきましょう。
```

---

## Entry 37

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 armour`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:291`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:258`

### English

```text
Pick up these boots with <input>$cmd[CMD_PICKUP]</input> and wear them with
<input>$cmd[CMD_EQUIP]</input>.<localtiles> Or simply <input>mouseclick</input>
on them in the inventory panel.</localtiles>
```

### 日本語

```text
<input>$cmd[CMD_PICKUP]</input>でブーツを拾い、
<input>$cmd[CMD_WEAR_ARMOUR]</input>で装備してください。また、
インベントリ内のブーツを<input>クリック</input>しても装備できます。
```

---

## Entry 38

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 autopickup`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:297`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:264`

### English

```text
Some types of items<tiles>, marked with a green frame,</tiles> are picked up
automatically as you step on them.
```

### 日本語

```text
<tiles>緑の枠で囲まれた</tiles>
数種類のアイテムはそのマスに移動した際に自動で拾われます。
```

---

## Entry 39

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 scroll`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:302`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:269`

### English

```text
Many items are unidentified when you find them. One way to find out what they
do is to use them. Try reading this scroll with <input>$cmd[CMD_READ]</input>
<localtiles> or with <input>mouseclick</input> in the inventory
panel</localtiles>.
```

### 日本語

```text
多くのアイテムは発見した時点では未鑑定です。
それらの効果を判別する方法の1つはそれを使用することです。
試しに<input>$cmd[CMD_READ]</input><localtiles>、
またはインベントリ内で<input>クリック</input>して巻物を読んでみましょう
</localtiles>。
```

---

## Entry 40

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 scroll_noautopickup`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:309`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:277`

### English

```text
Autopickup does not work if there's a monster around. You can either pick up
this scroll now with <input>$cmd[CMD_PICKUP]</input><localtiles> or
<input>clicking</input> on your character,</localtiles> or you can fight the
nearby enemy and pick it up afterwards.
```

### 日本語

```text
周囲にモンスターが居る場合、自動拾いは行われません。あなたは
<input>$cmd[CMD_PICKUP]</input>で<localtiles>
またはあなたのキャラクターを<input>クリック</input> することで、</localtiles>
巻物を今すぐ拾うか、近くのモンスターと戦闘後に拾うかのどちらかを選択できます。
```

---

## Entry 41

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 ego_weapon`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:316`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:284`

### English

```text
An item described as <lightblue>runed</lightblue> or
<lightblue>glowing</lightblue> will always be enchanted, or have special
properties, or both. Once you step on top of such an item, its properties will
be revealed to you.
```

### 日本語

```text
<lightblue>ルーンが刻まれた</lightblue>または<lightblue>輝く</lightblue>と描写されたアイテムは全て魔術が付与されているか、
特別な能力を持っているか、あるいはその両方の性質を持っています。
このシミターを装備して(<input>$cmd[CMD_WIELD_WEAPON]</input>で<localtiles>、
またはインベントリ内で<input>クリック</input></localtiles>)
どのようなものか判別してみましょう。
```

---

## Entry 42

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 inventory`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:323`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:292`

### English

```text
To view the description of your new weapon, find and select it in your
inventory (<input>$cmd[CMD_DISPLAY_INVENTORY]</input>). <localtiles>You can
also <input>mouseover</input> or <input>right click</input> it in the inventory
panel. </localtiles>Notice that all the item commands also work from the item
description screens.
```

### 日本語

```text
インベントリ内から選択して、
新しい武器の説明を見てみましょう(<input>$cmd[CMD_DISPLAY_INVENTORY]</input>)
 。
<localtiles>インベントリ内で<input>マウスオーバー</input>または<input>右クリック</input>でも可能です。
</localtiles>
全てのアイテムコマンドは説明文画面からでも実行できる点に注目して下さい。
```

---

## Entry 43

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 battle`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:334`
- Japanese source: 未訳

### English

```text
Once you've successfully managed to poison a monster, it is sometimes best to
retreat and let the poison do the work. Don't forget to retreat to heal too, if
necessary.
```

### 日本語

```text
（未訳）
```

---

## Entry 44

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 downstairs`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:340`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:301`

### English

```text
Well fought! If necessary, rest up with <input>$cmd[CMD_REST]</input>, then
continue downwards with <input>$cmd[CMD_GO_DOWNSTAIRS]</input><localtiles> or
with a <input>click</input> on your character</localtiles>.
```

### 日本語

```text
良い戦いでした! 必要であれば <input>$cmd[CMD_REST]</input> で休息を取り、
<input>$cmd[CMD_GO_DOWNSTAIRS]</input> <localtiles> または階段の上で
<input>Shift-クリック</input> </localtiles>で階段を降りて先に進んで下さい。
```

---

## Entry 45

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 command_help`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:346`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:307`

### English

```text
If the many commands are too confusing, you can also look them up in the
command help <input>$cmd[CMD_DISPLAY_COMMANDS]</input>. <localtiles>A number of
commands are also available in the clickable <w>command panel</w> to the right
of the screen. </localtiles>Rereading old messages with
<input>$cmd[CMD_REPLAY_MESSAGES]</input> is available as usual.
```

### 日本語

```text
多くのコマンドが煩わしく感じるなら、
<input>$cmd[CMD_DISPLAY_COMMANDS]</input>でコマンドヘルプを参照して下さい。
<localtiles>多くのコマンドは画面右の <w>コマンドパネル</w>
からクリックすることでも実行することが出来ます。</localtiles>
<input>$cmd[CMD_REPLAY_MESSAGES]</input>から以前のメッセージを読み返すことは例によって有効です。
```

---

## Entry 46

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 trap`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:354`
- Japanese source: 未訳

### English

```text
Traps can have a variety of unpleasant effects, such as alerting monsters or
teleporting you into danger. Some traps are permanent and will always be
revealed as part of the map, but other traps can be triggered by exploring new
tiles, and won't exist after being triggered. If there's no way around, you'll
have to trigger the trap and deal with the consequences.
```

### 日本語

```text
（未訳）
```

---

## Entry 47

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 potion`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:362`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:315`

### English

```text
Potions may provide vital healing or useful enchantments, but some have less
desirable effects. You can quaff this potion with
<input>$cmd[CMD_QUAFF]</input><localtiles> or with
<input>mouseclick</input></localtiles> to discover what it does.
```

### 日本語

```text
<input>$cmd[CMD_QUAFF]</input><localtiles>または<input>クリック</input>
</localtiles>で薬を飲むことが出来ます。
```

---

## Entry 48

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 artefact_armour`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:369`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:320`

### English

```text
Items with <w>unusual names</w> are artefacts. Artefacts can have a number of
special properties. Some unique artefacts (such as this cloak) are always
identified and may have special properties that cannot be found anywhere else!
Others are generated with a random selection of properties, and are
unidentified until you step on top of them. Try equipping this cloak with
<input>$cmd[CMD_EQUIP]</input><localtiles> or <input>mouseclick</input>
in the inventory panel</localtiles>.
```

### 日本語

```text
<w>珍しい</w> 名前のアイテムはアーティファクトです。
アーティファクトは多くの特別な能力を持っています。
例えばこのクロークのようないくらかのアイテムは有名で能力が鑑定済みになりますが、
一方でランダムな能力を持ち、効果の分からないものも存在します。
<input>$cmd[CMD_WEAR_ARMOUR]</input><localtiles>、
またはインベントリ内で<input>クリック</input></localtiles>
でこのクロークを装備してみてください。
```

---

## Entry 49

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 wand_fire`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:381`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:330`

### English

```text
You can evoke a wand with <input>$cmd[CMD_EVOKE]</input><localtiles> or with
<input>mouseclick</input> in the inventory panel</localtiles>.
```

### 日本語

```text
<input>$cmd[CMD_EVOKE]</input>
<localtiles>またはインベントリ内を<input>mouseclick</input>すること</localtiles>でワンドを発動させることが出来ます。
```

---

## Entry 50

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 wand_digging`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:387`
- Japanese source: 未訳

### English

```text
A wand of digging can destroy rock walls. Use
<input>$cmd[CMD_LOOK_AROUND]][$cmd[CMD_TARGET_DESCRIBE]</input> <localtiles>or
<input>mouseover</input>/<input>right click</input> </localtiles>to check wall
types.
```

### 日本語

```text
（未訳）
```

---

## Entry 51

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 amulet`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:394`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:335`

### English

```text
Jewellery is put on with <input>$cmd[CMD_EQUIP]</input><localtiles>
or with <input>mouseclick</input> in the inventory panel</localtiles>.
```

### 日本語

```text
装飾品は<input>$cmd[CMD_WEAR_JEWELLERY]</input><localtiles>
またはインベントリ内で<input>クリック</input>
</localtiles>で装備することができます。幾つかの装飾品は装備した際に鑑定されます。
その他の装飾品は別の手段で鑑定しなければなりません。
```

---

## Entry 52

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 drop`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:399`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:350`

### English

```text
This amulet would be very powerful if your character had a god to worship,
but here and now, it's useless. You may want to drop it with
<input>$cmd[CMD_DROP]</input><localtiles> or by
<input>Shift-leftclicking</input> it in the inventory panel</localtiles>.
```

### 日本語

```text
この護符は役立たずだ。これを捨てたいのであれば<input>$cmd[CMD_DROP]</input>
<localtiles>またはインベントリ内で <input>Shift-クリック</input>
</localtiles>を押してください。
```

---

## Entry 53

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 gold`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:406`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:356`

### English

```text
Gold can be spent in shops. It takes no inventory space and cannot be dropped.
```

### 日本語

```text
金貨は店で使用することができます。金貨は重量に加算されず、
落とすことも出来ません。
```

---

## Entry 54

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 shop`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:410`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:361`

### English

```text
Shops offer a variety of items, but they don't buy items from anyone.
```

### 日本語

```text
店は様々な種類のアイテムを販売しています。しかし、
彼らはアイテムの買い入れは行っていません。
```

---

## Entry 55

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 enter_shop`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:414`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:366`

### English

```text
To enter this shop, press <input>$cmd[CMD_GO_UPSTAIRS]</input><localtiles> or
<input>click</input> on your character</localtiles>. To buy items,
select them with their hotkey, hit <input>Enter</input> and confirm with
<input>y</input>es. You can switch to description mode with <input>!</input>.
```

### 日本語

```text
店に入るには<input>$cmd[CMD_GO_UPSTAIRS]</input><localtiles>
またはキャラクター上で<input>Shift-クリック</input>
</localtiles>を押してください。
アイテムを購入するにはアイテムに割り当てられた文字を選択し、
<input>Enter</input> を押して、<input>y</input>esで確定してください。
<input>!</input>で説明文を読むこともできます。
```

---

## Entry 56

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 autoexplore_reminder`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:423`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:375`

### English

```text
Remember, you can explore the level automatically with
<input>$cmd[CMD_EXPLORE]</input><localtiles> or by <input>clicking</input> the
autoexplore command button in the <w>command panel</w></localtiles>.
```

### 日本語

```text
<input>$cmd[CMD_EXPLORE]</input><localtiles>または<w>command
panel</w>の自動探索ボタンを<input>クリック</input>すること</localtiles>で階層内を自動探索できることをお忘れなく。
```

---

## Entry 57

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 go_shopping`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:429`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:380`

### English

```text
You now have enough gold to do some serious shopping! The quickest way back to
the shop is by searching for it. Type <input>$cmd[CMD_SEARCH_STASHES]</input>,
and then enter “<w>shop</w>”. Select the result to start travelling.<localtiles>
You can also <input>click</input> on the search button in the command panel, or
use the minimap to return to the shop.</localtiles>
```

### 日本語

```text
あなたは今本格的な買い物に十分な金額を所持しています!店に戻る最も速い手段は検索することです。
<input>$cmd[CMD_SEARCH_STASHES]</input>を押して、
「<w>shop</w>」と入力してください。結果を選択すると自動で移動を開始します。
<localtiles>同様にコマンドパネルの検索ボタンを<input>クリック</input>するか、
ミニマップを利用して店に戻ることも可能です。</localtiles>
```

---

## Entry 58

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 optional_battle`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:441`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:388`

### English

```text
Warning, this way leads to <lightred>a difficult battle</lightred>. You may
choose to use what you've learned so far in a fight, or try to reach the other
exit on the island. Either way, it may be a good idea to do some shopping, if
you haven't already.
```

### 日本語

```text
警告！この先には<lightred>過酷な戦い</lightred>が待ち受けています。
あなたは今までの戦闘で学んだことを実践するか、
小島にあるもう一つの出口への到達を試みるかを選ばなくてはなりません。
もしまだ買い物を済ませていないのであれば、何か購入したほうが良いでしょう。
```

---

## Entry 59

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 tutorial_end`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:448`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:395`

### English

```text
Well done! To exit the tutorial, simply go down these stairs.
```

### 日本語

```text
よく出来ました!チュートリアルを終了するには階段を降りて下さい。
```

---

## Entry 60

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial3 exit`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:452`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:399`

### English

```text
:nowrap
<white>Tutorial 3 summary: Items</white>

<yellow>Item commands</yellow>
  <input>$cmd[CMD_PICKUP]</input>  pick up an item
  <input>$cmd[CMD_DROP]</input>  drop an item
  <input>$cmd[CMD_EQUIP]</input>  equip armour, weapons, and jewellery
  <input>$cmd[CMD_UNEQUIP]</input>  unequip armour, weapons, and jewellery
  <input>$cmd[CMD_READ]</input>  read a scroll
  <input>$cmd[CMD_QUAFF]</input>  quaff a potion
  <input>$cmd[CMD_EVOKE]</input>  evoke a wand

  Use and (un)equip commands are also available from item descriptions in the inventory menu (<input>$cmd[CMD_DISPLAY_INVENTORY]</input>).<localtiles>
  And of course, <input>mouseclicks</input> also work.</localtiles>

<yellow>Other</yellow>
  <input>$cmd[CMD_DISPLAY_COMMANDS]?</input> access the command help
  <input>$cmd[CMD_EXPLORE]</input>  explore automatically
  <input>$cmd[CMD_SEARCH_STASHES]</input> search for items/features previously seen<localtiles>
  Several of these commands can also be executed by clicking in the <w>command panel</w>.</localtiles>
```

### 日本語

```text
:nowrap
<yellow>アイテムコマンド</yellow>
  <input>$cmd[CMD_PICKUP]</input>  アイテムを拾う
  <input>$cmd[CMD_WEAR_ARMOUR]</input>  防具を装備する
  <input>$cmd[CMD_READ]</input>  巻物を読む
  <input>$cmd[CMD_WIELD_WEAPON]</input>  武器を装備する
  <input>$cmd[CMD_QUAFF]</input>  薬を飲む
  <input>$cmd[CMD_EVOKE]</input>  ワンドを発動する
  <input>$cmd[CMD_WEAR_JEWELLERY]</input>  装飾品を装備する
  <input>$cmd[CMD_REMOVE_JEWELLERY]</input>  装飾品を外す
  <input>$cmd[CMD_DROP]</input>  アイテムを落とす
  これらのコマンドはインベントリ(<input>$cmd[CMD_DISPLAY_INVENTORY]</input>)からも使用することができ、アイテム説明文からも同様に可能です。<localtiles>
  そしてもちろん、 <input>クリック</input> でも可能です。</localtiles>

<yellow>その他</yellow>
  <input>$cmd[CMD_DISPLAY_COMMANDS]?</input> コマンドヘルプを見る
  <input>$cmd[CMD_RESISTS_SCREEN]</input>  キャラクター情報を表示する
  <input>$cmd[CMD_USE_ABILITY]</input>  能力を使用する
  <input>$cmd[CMD_EXPLORE]</input>  自動探索
  <input>$cmd[CMD_SEARCH_STASHES]</input> 既知のアイテム/施設を検索<localtiles>
  幾つかのコマンドは <w>コマンドパネル</w> をクリックして実行することができます。</localtiles>

                                 <cyan>この画面は <input>任意のキー</input> を押すと終了します...</cyan>
```

---

## Entry 61

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 start`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:479`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:425`

### English

```text
In this lesson you're going to learn how to memorise and cast spells.
```

### 日本語

```text
このレッスンでは魔法の記憶と詠唱の方法を学んでいきます。
```

---

## Entry 62

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 spellbook`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:483`
- Japanese source: 未訳

### English

```text
You can memorise a spell from your spell library with
<input>$cmd[CMD_MEMORISE_SPELL]</input><localtiles> or by
<input>clicking</input> on the memorisation tab and selecting the spell
tile</localtiles>. At experience level 1, only level 1 spells are available to
you. This will change as you gain experience. To find new spells, find and pick
up spellbooks, and the spells will be added to your library.
```

### 日本語

```text
（未訳）
```

---

## Entry 63

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 spellcasting`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:492`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:429`

### English

```text
To cast a spell, first memorise it with <input>$cmd[CMD_MEMORISE_SPELL]</input>.
You can then cast it with <input>$cmd[CMD_CAST_SPELL]</input><localtiles> or by
<input>clicking</input> on the spell tile</localtiles>.

Press <input>$cmd[CMD_CAST_SPELL]</input>, then press <input>?</input> to get a
list of your spells.
```

### 日本語

```text
 <input>$cmd[CMD_CAST_SPELL]</input><localtiles>
または呪文タイルを<input>クリック</input>
</localtiles>で呪文を唱えることができます。
<input>$cmd[CMD_CAST_SPELL]</input>で覚えている呪文の一覧を参照できます。

魔力が足りなくなってしまった場合は安全な場所に退避して、
<input>$cmd[CMD_REST]</input>
<localtiles>またはコマンドパネル内の休息アイコンを<input>クリック</input>して</localtiles>休息を取りましょう。
```

---

## Entry 64

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 spellquivering`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:504`
- Japanese source: 未訳

### English

```text
Spells, like ammo, are shown in the quiver slot, so you can use
<input>$cmd[CMD_QUIVER_ITEM]</input> to ready a spell in the quiver. Use
<input>$cmd[CMD_FIRE]</input> or <input>shift-tab</input> to fire the currently
quivered spell.

Once you are out of magic points, retreat and rest to regain them with
<input>$cmd[CMD_REST]</input><localtiles> or by <input>clicking</input> the
rest icon in the command panel</localtiles>.
```

### 日本語

```text
（未訳）
```

---

## Entry 65

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 ring_power`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:514`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:440`

### English

```text
Put on this ring with <input>$cmd[CMD_EQUIP]</input><localtiles> or
by <input>clicking</input> it in the inventory panel</localtiles>, and then
rest up to your new full potential.
```

### 日本語

```text
この指輪を<input>$cmd[CMD_WEAR_JEWELLERY]</input>で<localtiles>
またはインベントリ内で<input>クリック</input>して</localtiles>装備し、
新たな力を存分に振るえるよう休息をとってください。
```

---

## Entry 66

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 undead`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:520`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:446`

### English

```text
Unlike most monsters, zombies and skeletons do not regenerate health.
<localtiles> You can also attempt to re-cast the last spell you used by
pressing <input>Ctrl+leftclick</input> on the monster.</localtiles>
```

### 日本語

```text
他のモンスターとは違い、アンデッドは体力が回復することがなく、
彼らがどれほどの傷を負っているのか確かめることはできません。
<localtiles>話しは変わりますが、
モンスターの上で<input>Ctrl+クリック</input>を押すことでも呪文を唱えることができます。
</localtiles>
```

---

## Entry 67

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 spell_success`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:528`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:454`

### English

```text
To check your spell proficiency, press <input>$cmd[CMD_DISPLAY_SPELLS]</input>
<localtiles> or <input>mouseover</input> over your memorised
spells</localtiles>. Compare your spell failure rates before and after wearing
this ring.
```

### 日本語

```text
<input>$cmd[CMD_DISPLAY_SPELLS]</input><localtiles> 、
または覚えている呪文に<input>マウスオーバー</input>
</localtiles>であなたの呪文の熟練度を知ることが出来ます。
この杖を装備する前と後の呪文の成功率を比べてみてください。
```

---

## Entry 68

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 mephitic_cloud`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:535`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:461`

### English

```text
Mephitic Cloud is a level 3 spell, so you can't memorise it yet. To level up
quickly, here are more training dummies — without stones to throw this time.

At experience level 3, you'll be able to increase one of your stats — choosing
<input>I</input>ntelligence will help your spellcasting even further.
```

### 日本語

```text
悪臭の雲はレベル3の呪文なので、あなたはまだ覚えることができません。
すぐにレベルを上げるため、
たくさんのトレーニング用のかかしが用意されています-今回は投擲用の石は無しです。

レベル3になると、ステータスを1つ強化することができます-<input>I</input>を押して、
知力を選ぶことは呪文詠唱の更なる助けになります。
```

---

## Entry 69

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 meph_reminder`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:543`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:470`

### English

```text
Don't forget to memorise your newly-available spell, by pressing
<input>$cmd[CMD_MEMORISE_SPELL]</input><localtiles> or by
<input>clicking</input> on the memorisation tab and selecting the spell
tile</localtiles>!
```

### 日本語

```text
<input>$cmd[CMD_MEMORISE_SPELL]</input>を押す<localtiles>、
または呪文の記憶タブを<input>クリック</input>して、
覚えたい呪文のタイルを選ぶことで</localtiles>、
新たに使えるようになった呪文を記憶することを忘れずに!
```

---

## Entry 70

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 aiming_clouds`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:550`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:477`

### English

```text
Mephitic Cloud covers an area in noxious fumes when cast, and you'll be able to
see the area it affects as you target it. Try to catch multiple enemies in a
single cloud in order to be more efficient with your magic.
```

### 日本語

```text
悪臭の雲は詠唱すると範囲内を有害なガスで覆い、
その範囲は狙いをつける際に知ることができます。魔法を効率よく使うために、
一発の雲で多くの敵を巻き込んでみましょう。
```

---

## Entry 71

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 forget_spell`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:556`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:483`

### English

```text
Gaining experience levels and raising your Spellcasting skill gives you spell
slots to spend on spells. You can also <w>forget a memorised spell</w> to make
space for a new one by reading a scroll of amnesia. Read the scroll (with
<input>$cmd[CMD_READ]</input><localtiles> or by
<input>clicking</input> on it</localtiles>), and then select the spell you want
to forget. You can relearn forgotten spells from your spell library later, as
long as you have spell slots available.
```

### 日本語

```text
経験レベルと呪文詠唱スキルが上昇することで呪文を記憶するための記憶容量を得ることができます。
新たな呪文を記憶するために<input>呪文を忘れる</input> ことも可能です。
呪文を忘れる最も簡単な手段は忘却の巻物を使用することです。
巻物を読み(<input>$cmd[CMD_READ]</input><localtiles>、
または忘却の巻物を<input>クリック</input>して</localtiles>)、
忘れたい呪文を選択してください。
```

---

## Entry 72

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 memorise2`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:566`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:492`

### English

```text
After forgetting one of your old spells to make space, memorise this new spell
with <input>$cmd[CMD_MEMORISE_SPELL]</input><localtiles> or by
<input>clicking</input> on the memorisation tab and selecting the spell
tile</localtiles>. Then try your new spell and summon some demonic allies!
```

### 日本語

```text
繰り返しになりますが、<input>$cmd[CMD_MEMORISE_SPELL]</input><localtiles>、
または呪文の記憶タブを<input>クリック</input>して呪文を選択</localtiles>で新たに呪文を記憶することができます。
するとあなたはアンデッドの軍勢を得ることができます!
```

---

## Entry 73

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 displace_allies`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:573`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:498`

### English

```text
Did you notice you can swap positions with your allies by moving into them?
Among other things, displacing a friendly creature can be a good way to escape
a fight.
```

### 日本語

```text
あなたのしもべのいる方向へ向かって移動することで自分と位置を交換することができることにはお気づきですか?
とりわけ、友好的なモンスターと位置を入れ替えることは戦いから逃げる良い手段です。
```

---

## Entry 74

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 order_allies`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:579`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:503`

### English

```text
Try to let your allies do the killing! If necessary, you can order them about
with <input>$cmd[CMD_SHOUT]</input>. Before opening this gate, you may want to
wait with <input>$cmd[CMD_WAIT]</input> until your allies have caught
up with you. Your summons will only stick around for a short time, so don't
wait too long, or summon some new ones before starting a fight.
```

### 日本語

```text
しもべに敵を殺害させてみましょう!必要であれば、
<input>$cmd[CMD_SHOUT]</input>でしもべに命令することができます。
この門を開ける前に<input>$cmd[CMD_WAIT]</input>で待機してしもべがあなたに追いつくまで待つこともできます。
```

---

## Entry 75

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 heavy_armour`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:587`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:509`

### English

```text
Heavy armour really hampers spellcasting. Try putting on that mail and shield
(with <input>$cmd[CMD_EQUIP]</input><localtiles> or by
<input>clicking</input> on them</localtiles>), and compare your spellcasting
failure rates with <input>$cmd[CMD_DISPLAY_SPELLS]</input><localtiles> or by
<input>mouseovering</input> your memorised spells</localtiles>. You can take
armour off again with <input>$cmd[CMD_UNEQUIP]</input><localtiles> or,
again, via <input>mouseclick</input></localtiles>.
```

### 日本語

```text
重い鎧は呪文の詠唱を大きく阻害します。試しに鎧と盾を身につけ(
<input>$cmd[CMD_WEAR_ARMOUR]</input><localtiles>、
または装備したいアイテムを<input>クリック</input></localtiles>)、
<input>$cmd[CMD_DISPLAY_SPELLS]</input><localtiles>、
または記憶している呪文に<input>マウスオーバー</input>
</localtiles>で呪文の成功率を比較してみて下さい。
<input>$cmd[CMD_REMOVE_ARMOUR]</input><localtiles>、
または<input>クリック</input></localtiles>で装備を外すことができます。
```

---

## Entry 76

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 resting_reminder`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:598`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:520`

### English

```text
Make sure you are at full health and magic points before entering a new area.
If necessary, rest up with <input>$cmd[CMD_REST]</input><localtiles> or by
<input>mouseclick</input> in the command panel</localtiles>.

You can only summon a limited number of allies at once from any given spell,
so try to take advantage of a wide range of spells. For example, your summoned
imps are resistant to poison, so you can cast Mephitic Cloud to fight alongside
them without harming your allies.
```

### 日本語

```text
新たなエリアに入る前に体力と魔力をしっかりと最大まで回復しておきましょう。
必要であれば、<input>$cmd[CMD_REST]</input><localtiles>、
またはコマンドパネルの休憩タブを<input>クリック</input>
</localtiles>で休息を取りましょう。

また、アンデッドは呼吸をしませんので、
しもべに影響を与えることなく悪臭の雲を使用することができます。
```

---

## Entry 77

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 tutorial_end`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:609`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:530`

### English

```text
Congratulations, you're a real wizard now! To exit the tutorial, simply go down
these stairs.
```

### 日本語

```text
おめでとうございます、
あなたはもう立派な魔法使いです!チュートリアルを終了するには階段を降りてください。
```

---

## Entry 78

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial4 exit`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:614`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:535`

### English

```text
:nowrap
<white>Tutorial 4 summary: Magic</white>

<yellow>Spellcasting commands</yellow>
  <input>$cmd[CMD_MEMORISE_SPELL]</input>  learn a new spell
  <input>$cmd[CMD_DISPLAY_SPELLS]</input>  check spell proficiency
  <input>$cmd[CMD_CAST_SPELL]</input>  cast a spell<localtiles>
  You can also learn new spells via the <w>memorisation tab</w>.
  You can cast memorised spells via <input>leftclick</input>, and read their descriptions and check your spell proficiency by <input>mouseover</input> or <input>rightclick</input></localtiles>
  <input>$cmd[CMD_QUIVER_ITEM]</input>  adjust your quiver

  <input>$cmd[CMD_REST]</input>  rest up to 100 turns to regain magic points and health
  <input>$cmd[CMD_SHOUT]</input>  order allies
  <input>$cmd[CMD_UNEQUIP]</input>  take off equipment
```

### 日本語

```text
:nowrap
<yellow>魔法コマンド</yellow>
  <input>$cmd[CMD_MEMORISE_SPELL]</input>  新たに呪文を記憶する
  <input>$cmd[CMD_DISPLAY_SPELLS]</input>  呪文の熟練度を表示する
  <input>$cmd[CMD_CAST_SPELL]</input>  呪文を唱える
<localtiles>      <w>呪文の記憶タブ</w>からでも呪文を記憶することができます。
     記憶している呪文を<input>クリック</input>することでも呪文を唱えることができ、
<input>マウスオーバー</input>または<input>右クリック</input>で呪文の説明と熟練度を参照できます。
</localtiles>

  <input>$cmd[CMD_READ]</input>  魔法書の説明文を読む、忘却の巻物で呪文を忘れる
  <input>$cmd[CMD_REST]</input>  100ターン休息して魔力と体力を回復させる。
  <input>$cmd[CMD_SHOUT]</input>  しもべに命令する
  <input>$cmd[CMD_REMOVE_ARMOUR]</input>  防具を外す


                                 <cyan>この画面は<w>任意のキー</w>を押すと終了します...</cyan>
```

---

## Entry 79

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 start`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:635`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:555`

### English

```text
In this lesson you're going to learn about gods and how to use their powers.
```

### 日本語

```text
このレッスンでは神々とその能力の使い方について学んでいきましょう。
```

---

## Entry 80

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 dungeon_overview`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:639`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:559`

### English

```text
Up ahead is an altar to Trog the Wrathful! Trog is just one of many gods. In a
real game, you can check <input>$cmd[CMD_DISPLAY_OVERMAP]</input><localtiles>
or <input>click the dungeon overmap button</input> in the command
panel</localtiles> for a list of all altars and other interesting features
found so far.
```

### 日本語

```text
この先にあるのは怒れるトログの祭壇です。トログは数多くいる神々の一柱です。
実際のゲームでは、<input>$cmd[CMD_DISPLAY_OVERMAP]</input><localtiles>、
またはコマンドパネル内の <input>ダンジョン全体図ボタンをクリック</input>
</localtiles>からそれまでに発見した全ての祭壇や施設の一覧を見ることができます。
```

---

## Entry 81

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 altar`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:647`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:566`

### English

```text
You can pray on an altar with <input>$cmd[CMD_GO_DOWNSTAIRS]</input>
<localtiles> (or by <input>left clicking</input> on your character)</localtiles>
to get an idea what a god offers you, and to join the faith. If
you press <input>!</input><localtiles> or
<input>rightclick</input></localtiles> on the religion screen, you can see a
more detailed description.

Confirm your choice with <input>J</input> or <input>Enter</input>.
```

### 日本語

```text
祭壇の上で<input>$cmd[CMD_PRAY]</input>を押すと、<localtiles>
(または<input>コマンドパネル内をクリック</input>するか、
キャラクターを<input>Shift-クリック</input>)</localtiles>
その神があなたにどのような恩恵をもたらすのか知ることができ、
入信することができます。その画面を表示している際に、
<input>!</input>を押す<localtiles>、
または<input>右クリック</input>する</localtiles>ことで、
あなたの信仰する神についてのより詳細な説明を見ることができます。

大文字の<input>Y</input>を押してあなたの選択を確かなものにしてください。
```

---

## Entry 82

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 religion`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:658`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:579`

### English

```text
Have a look at your current religious standing with
<input>$cmd[CMD_DISPLAY_RELIGION]</input><localtiles> (or via the <w>religion
button</w> in the command panel, or by <input>Shift-rightclicking</input> on
the player tile)</localtiles>. Again, pressing <input>!</input><localtiles> or
<input>rightclicking</input></localtiles> will bring up a more detailed
description of your god.
```

### 日本語

```text
<input>$cmd[CMD_DISPLAY_RELIGION]</input>で現在の信仰を見ることができる<localtiles>(コマンドパネルの<w>religion
button</w>から、
またはキャラクターの上で<input>Shift-クリック</input>)</localtiles>。
加えて<input>!</input><localtiles>または<input>右クリック</input>
</localtiles>で信仰する神のより詳細な説明を参照することができます。
```

---

## Entry 83

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 piety_on_kill`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:667`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:587`

### English

```text
Some gods really like it if you kill monsters in their name. Let the slaughter
begin!
```

### 日本語

```text
幾柱かの神々は彼らの名のもとにおいてのモンスターの殺害を非常に好みます。さぁ、
虐殺の始まりだ!
```

---

## Entry 84

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 berserk`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:672`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:603`

### English

```text
Against particularly tough foes, you may want to use Trog's Berserk power with
<input>$cmd[CMD_USE_ABILITY]</input><localtiles> or via the <w>command
panel</w></localtiles>.
```

### 日本語

```text
特に強力な敵に相対するとき、<input>$cmd[CMD_USE_ABILITY]</input>
<localtiles>または<w>command
panel</w>から</localtiles>トログの狂戦士化の力を行使しようと思うに違いない。
```

---

## Entry 85

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 exhaustion`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:678`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:609`

### English

```text
A berserker rage is truly exhausting. After it ends, you cannot berserk again
for a short while and are slowed. It's best to rest with
<input>$cmd[CMD_REST]</input><localtiles> (or via the
<w>command panel</w>)</localtiles> until you feel fit again.
```

### 日本語

```text
狂戦士の怒りを使用すると非常に疲労してしまいます。
疲労している間は狂戦士化することができず、減速もします。
<input>$cmd[CMD_REST]</input><localtiles>
(または<w>コマンドパネル</w>から)</localtiles>で体調がもとに戻るまで休息をとるのが最善でしょう。
```

---

## Entry 86

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 berserk2`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:685`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:616`

### English

```text
Berserk is also really useful against multiple enemies — as long as you don't
run out of steam in-between.
```

### 日本語

```text
狂戦士化は複数の敵を相手にする場合にも非常に有効だ-その効果が無くなるまでの間の話ではあるが。
```

---

## Entry 87

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 tutorial_end`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:690`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:620`

### English

```text
Congratulations! You've finished the last tutorial lesson and are now ready for
the real game. Good luck!

To exit the tutorial, just go down these stairs.
```

### 日本語

```text
おめでとうございます!あなたは最後のレッスンを終え、
ゲーム本編をプレイする準備ができました。ご武運を!

チュートリアルを終了するには、階段を下りてください。
```

---

## Entry 88

- Resource: `crawl-ref/source/dat/descript/tutorial.txt`
- English key: `tutorial5 exit`
- English source: `crawl-ref/source/dat/descript/tutorial.txt:697`
- Japanese source: `crawl-ref/source/dat/descript/ja/tutorial.txt:627`

### English

```text
:nowrap
<white>Tutorial 5 summary: Religion</white>

<yellow>Religious commands</yellow>
  <input>$cmd[CMD_GO_DOWNSTAIRS]</input>  pray at an altar to join a god
  <input>$cmd[CMD_USE_ABILITY]</input>  use a divine ability
  <input>$cmd[CMD_DISPLAY_RELIGION]</input>  check your religious standing<localtiles>
  A <input>rightclick</input> on the player tile will also bring up the religion screen.</localtiles>

<yellow>Resting</yellow>
  <input>$cmd[CMD_WAIT]</input>  wait and rest a single turn
  <input>$cmd[CMD_REST]</input>  wait and rest up to 100 turns

<yellow>Other commands</yellow>
  <input>$cmd[CMD_DISPLAY_OVERMAP]</input> display an overview of the dungeon
  <input>$cmd[CMD_DISPLAY_COMMANDS]/</input>  search the description database
```

### 日本語

```text
:nowrap
<yellow>信仰関連のコマンド</yellow>
  <input>$cmd[CMD_PRAY]</input>  祭壇に祈りを捧げ入信する、死体を捧げる
  <input>$cmd[CMD_USE_ABILITY]</input>  神の力を行使する
  <input>$cmd[CMD_DISPLAY_RELIGION]</input>  あなたの信仰の評価を確認する<localtiles>
  キャラクターを<input>右クリック</input>することでも信仰画面が表示される。</localtiles>

<yellow>休息</yellow>
  <input>$cmd[CMD_WAIT]</input>  1ターン待機し、休息する
  <input>$cmd[CMD_REST]</input>  100ターン待機し、休息する

<yellow>その他のコマンド</yellow>
  <input>$cmd[CMD_DISPLAY_OVERMAP]</input> ダンジョンの概観を表示する
  <input>$cmd[CMD_DISPLAY_COMMANDS]/</input>  解説一覧から探す

                                 <cyan>この画面は<input>任意のキー</input>を押すと終了します...</cyan>
```
