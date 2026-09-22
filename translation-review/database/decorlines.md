# `decorlines.txt` 翻訳レビュー

> このファイルは自動生成です。直接編集せず、英語・日本語resourceを更新してください。
> 再生成: `python3 crawl-ref/source/util/translation_review.py`

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- Japanese resource: なし
- Entries: 132
- Translated: 0
- Untranslated: 132

## Entry 1

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `default peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:3`](../../crawl-ref/source/dat/database/decorlines.txt#L3)
- Japanese source: 未訳

### English

```text
{{
  -- Wisps can drink potions, so no need for another message here.
  if you.transform() == "death" or you.race() == "Mummy" then
    if crawl.one_chance_in(3) then
      return "You briefly stare at the drinking fountain and sigh."
    else
      return "__NONE"
    end
  elseif you.transform() == "storm" then
    return "The fountain crackles underneath you."
  else
    return "You take a small sip from the fountain. Refreshing.";
  end
}}

{{
  if you.transform() == "storm" then
    return "Small shocks surge through the fountain."
  elseif you.transform() == "wisp" then
    return "Your reflection flickers strangely in the water."
  elseif crawl.coinflip() or you.god() == "Okawaru" then
    return "You briefly stop to wash @your_hands@."
  else
    return "You briefly stop to clean @your_weapon@."
  end
}}

w:1
You see @any_graffiti@ on the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 2

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `default fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:35`](../../crawl-ref/source/dat/database/decorlines.txt#L35)
- Japanese source: 未訳

### English

```text
The fountain briefly ripples from your approaching presence.

w:1
You see @any_graffiti@ on the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 3

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `default peaceful fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:42`](../../crawl-ref/source/dat/database/decorlines.txt#L42)
- Japanese source: 未訳

### English

```text
{{
  if you.transform() == "death" or you.race() == "Mummy" then
    if crawl.one_chance_in(3) then
      return "You briefly stare at the sparkling fountain and sigh."
    else
      return "__NONE"
    end
  elseif you.transform() == "storm" then
    return "The fountain curiously crackles underneath you."
  elseif crawl.coinflip() or you.god == "Zin" or you.god == "Cheibriados" then
    return "The fountain pulses with strange @any_colour_pattern@, and you decide not to drink from it."
  else
    return "You take a small sip from the fountain. @sparkling_message@"
  end
}}

w:1
You see @any_graffiti@ on the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 4

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `sparkling_message`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:63`](../../crawl-ref/source/dat/database/decorlines.txt#L63)
- Japanese source: 未訳

### English

```text
You feel fleetingly lighter.

You feel a fleeting jolt of bravery.

You feel nauseous for a moment.

Your emotions uncomfortably twist.
```

### 日本語

```text
（未訳）
```

---

## Entry 5

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `default fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:76`](../../crawl-ref/source/dat/database/decorlines.txt#L76)
- Japanese source: 未訳

### English

```text
The sparkling fountain shimmers a faint @any_colour@.

w:1
You see @any_graffiti@ on the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 6

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `default fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:83`](../../crawl-ref/source/dat/database/decorlines.txt#L83)
- Japanese source: 未訳

### English

```text
{{
   if you.can_smell() then
     return "You smell the mouldering metallic scent of the fountain's ceaseless blood."
   elseif you.god() == "Trog" then
     return "You make sure not to track any more blood on yourself."
   else
     return "You make sure not to track any blood on yourself."
   end
}}

Miniscule mosquitoes swarm blood-drunk across the fountain's surface.

w:3
Your reflection in the fountain of blood stares back at you in silent [judgement|horror].

w:3
The fountain of blood pulses in murmuring sobs.

w:1
The blood fountain gushes with blood, as blood fountains often do.
```

### 日本語

```text
（未訳）
```

---

## Entry 7

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `default fountain_eyes`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:107`](../../crawl-ref/source/dat/database/decorlines.txt#L107)
- Japanese source: 未訳

### English

```text
The fountain's eyes stare blankly through you.

The fountain's eyes stare idly in all directions.

The fountain's eyes stare into nothing.
```

### 日本語

```text
（未訳）
```

---

## Entry 8

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `default peaceful dry_fountain`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:115`](../../crawl-ref/source/dat/database/decorlines.txt#L115)
- Japanese source: 未訳

### English

```text
w:1
You see @any_graffiti@ on the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 9

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `default dry_fountain`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:120`](../../crawl-ref/source/dat/database/decorlines.txt#L120)
- Japanese source: 未訳

### English

```text
w:1
You see @any_graffiti@ on the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 10

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Ashenzari peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:125`](../../crawl-ref/source/dat/database/decorlines.txt#L125)
- Japanese source: 未訳

### English

```text
You attempt to scry through the fountain, but the Dungeon's magics reject you.
```

### 日本語

```text
（未訳）
```

---

## Entry 11

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Ashenzari fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:129`](../../crawl-ref/source/dat/database/decorlines.txt#L129)
- Japanese source: 未訳

### English

```text
You catch brief visions of the Dungeon's past in the fountain's reflection.
```

### 日本語

```text
（未訳）
```

---

## Entry 12

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Beogh fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:133`](../../crawl-ref/source/dat/database/decorlines.txt#L133)
- Japanese source: 未訳

### English

```text
You look at your reflection in the fountain and see a proud orc.
```

### 日本語

```text
（未訳）
```

---

## Entry 13

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Beogh fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:138`](../../crawl-ref/source/dat/database/decorlines.txt#L138)
- Japanese source: 未訳

### English

```text
You look at your [shimmering|glittering] reflection in the fountain and see a proud orc.
```

### 日本語

```text
（未訳）
```

---

## Entry 14

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Cheibriados fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:142`](../../crawl-ref/source/dat/database/decorlines.txt#L142)
- Japanese source: 未訳

### English

```text
You briefly disapprove of the fountain's mystically arrhythmic flow.
```

### 日本語

```text
（未訳）
```

---

## Entry 15

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Cheibriados peaceful dry_fountain`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:146`](../../crawl-ref/source/dat/database/decorlines.txt#L146)
- Japanese source: 未訳

### English

```text
You briefly muse on the calm stillness of an empty fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 16

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Dithmenos fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:150`](../../crawl-ref/source/dat/database/decorlines.txt#L150)
- Japanese source: 未訳

### English

```text
You scoff at the overwrought melodramatics of this fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 17

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Elyvilon peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:154`](../../crawl-ref/source/dat/database/decorlines.txt#L154)
- Japanese source: 未訳

### English

```text
You approve of the purity and functionality of this drinking fountain.

@default peaceful fountain_blue@
```

### 日本語

```text
（未訳）
```

---

## Entry 18

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Fedhas peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:160`](../../crawl-ref/source/dat/database/decorlines.txt#L160)
- Japanese source: 未訳

### English

```text
You briefly survey the algae on the fountain's rim. They seem healthy.
```

### 日本語

```text
（未訳）
```

---

## Entry 19

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Fedhas peaceful fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:164`](../../crawl-ref/source/dat/database/decorlines.txt#L164)
- Japanese source: 未訳

### English

```text
You briefly survey the algae on the fountain's rim. They shimmer back.
```

### 日本語

```text
（未訳）
```

---

## Entry 20

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Fedhas peaceful fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:168`](../../crawl-ref/source/dat/database/decorlines.txt#L168)
- Japanese source: 未訳

### English

```text
You briefly survey the mould on the fountain's rim. It seems... concerning.
```

### 日本語

```text
（未訳）
```

---

## Entry 21

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Fedhas peaceful fountain_eyes`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:172`](../../crawl-ref/source/dat/database/decorlines.txt#L172)
- Japanese source: 未訳

### English

```text
You briefly survey the mould on the fountain's rim. It possibly surveys back.
```

### 日本語

```text
（未訳）
```

---

## Entry 22

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Gozag peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:176`](../../crawl-ref/source/dat/database/decorlines.txt#L176)
- Japanese source: 未訳

### English

```text
You look for coins within the fountain, but they're all too worthless to bother.
```

### 日本語

```text
（未訳）
```

---

## Entry 23

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Gozag peaceful fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:180`](../../crawl-ref/source/dat/database/decorlines.txt#L180)
- Japanese source: 未訳

### English

```text
@Gozag peaceful fountain_blue@
```

### 日本語

```text
（未訳）
```

---

## Entry 24

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Gozag fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:184`](../../crawl-ref/source/dat/database/decorlines.txt#L184)
- Japanese source: 未訳

### English

```text
w:2
You flinch at the exorbitant financial cost of maintaining this fountain.

@default fountain_blood@
```

### 日本語

```text
（未訳）
```

---

## Entry 25

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Hepliaklqana fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:191`](../../crawl-ref/source/dat/database/decorlines.txt#L191)
- Japanese source: 未訳

### English

```text
The fountain's ripples stir distant, transient memories.
```

### 日本語

```text
（未訳）
```

---

## Entry 26

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Hepliaklqana dry_fountain`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:195`](../../crawl-ref/source/dat/database/decorlines.txt#L195)
- Japanese source: 未訳

### English

```text
You swear to never forget your legacy as this fountain's builders were forgotten.
```

### 日本語

```text
（未訳）
```

---

## Entry 27

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Hepliaklqana peaceful fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:199`](../../crawl-ref/source/dat/database/decorlines.txt#L199)
- Japanese source: 未訳

### English

```text
You observe a moment of silence for whomever's blood flows through this fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 28

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Ignis fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:203`](../../crawl-ref/source/dat/database/decorlines.txt#L203)
- Japanese source: 未訳

### English

```text
The fountain's water lightly sizzles in your presence.

w:1
The dying flame fearfully flickers in the reflection of the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 29

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Ignis fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:210`](../../crawl-ref/source/dat/database/decorlines.txt#L210)
- Japanese source: 未訳

### English

```text
The fountain's sparkling water lightly sizzles and shimmers in your presence.

w:1
The dying flame fearfully flickers in the reflection of the sparkling fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 30

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Ignis fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:217`](../../crawl-ref/source/dat/database/decorlines.txt#L217)
- Japanese source: 未訳

### English

```text
The fountain's blood briefly boils in your presence.
```

### 日本語

```text
（未訳）
```

---

## Entry 31

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Jiyva peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:225`](../../crawl-ref/source/dat/database/decorlines.txt#L225)
- Japanese source: 未訳

### English

```text
You stop to admire the sparkling slime slowly growing over the fountain's rim.
```

### 日本語

```text
（未訳）
```

---

## Entry 32

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Jiyva fountain_eyes`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:229`](../../crawl-ref/source/dat/database/decorlines.txt#L229)
- Japanese source: 未訳

### English

```text
Your genes instinctively attempt to commune with the fountain's eyes and fail.

A few eyes on the fountain briefly shift into confused golden shades.
```

### 日本語

```text
（未訳）
```

---

## Entry 33

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Kikubaaqudgha peaceful dry_fountain`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:235`](../../crawl-ref/source/dat/database/decorlines.txt#L235)
- Japanese source: 未訳

### English

```text
You muse upon the day when the entire world will share this fountain's fate.
```

### 日本語

```text
（未訳）
```

---

## Entry 34

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Lugonu peaceful fountain_eyes`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:239`](../../crawl-ref/source/dat/database/decorlines.txt#L239)
- Japanese source: 未訳

### English

```text
You muse on Lugonu's promise to warp all of reality as thoroughly as this fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 35

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Makhleb peaceful fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:243`](../../crawl-ref/source/dat/database/decorlines.txt#L243)
- Japanese source: 未訳

### English

```text
You stop to admire the quantity of blood running through this fountain.

Your mind is briefly consumed by the idea of bathing in this fountain.

You anoint yourself with the fountain's blood.

You briefly wash @your_weapon@ in the fountain with ritualistic fervour.
```

### 日本語

```text
（未訳）
```

---

## Entry 36

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Nemelex Xobeh peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:253`](../../crawl-ref/source/dat/database/decorlines.txt#L253)
- Japanese source: 未訳

### English

```text
You toss an ancient coin into the fountain for a little extra luck.
```

### 日本語

```text
（未訳）
```

---

## Entry 37

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Nemelex Xobeh peaceful fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:257`](../../crawl-ref/source/dat/database/decorlines.txt#L257)
- Japanese source: 未訳

### English

```text
You toss an ancient coin into the fountain for some extra glamorous luck.
```

### 日本語

```text
（未訳）
```

---

## Entry 38

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Okawaru peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:261`](../../crawl-ref/source/dat/database/decorlines.txt#L261)
- Japanese source: 未訳

### English

```text
You briefly wash @your_weapon@ with practiced discipline.
```

### 日本語

```text
（未訳）
```

---

## Entry 39

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Qazlal peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:265`](../../crawl-ref/source/dat/database/decorlines.txt#L265)
- Japanese source: 未訳

### English

```text
w:5
You scoff at such attempts to contain the uncontrollable elements.

@Qazlal fountain_blue@
```

### 日本語

```text
（未訳）
```

---

## Entry 40

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Qazlal fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:272`](../../crawl-ref/source/dat/database/decorlines.txt#L272)
- Japanese source: 未訳

### English

```text
The fountain bubbles and surges in the storm.
```

### 日本語

```text
（未訳）
```

---

## Entry 41

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Qazlal fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:276`](../../crawl-ref/source/dat/database/decorlines.txt#L276)
- Japanese source: 未訳

### English

```text
The fountain bubbles and surges violently in the storm.
```

### 日本語

```text
（未訳）
```

---

## Entry 42

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Qazlal fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:280`](../../crawl-ref/source/dat/database/decorlines.txt#L280)
- Japanese source: 未訳

### English

```text
The fountain's blood bubbles and surges in the storm.
```

### 日本語

```text
（未訳）
```

---

## Entry 43

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Ru peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:284`](../../crawl-ref/source/dat/database/decorlines.txt#L284)
- Japanese source: 未訳

### English

```text
The water in the fountain reflects the world, which is itself a mere reflection.
```

### 日本語

```text
（未訳）
```

---

## Entry 44

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Ru peaceful fountain_eyes`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:288`](../../crawl-ref/source/dat/database/decorlines.txt#L288)
- Japanese source: 未訳

### English

```text
w:2
The eyes in the fountain cannot see the truth any more than any other material.

@default fountain_eyes@
```

### 日本語

```text
（未訳）
```

---

## Entry 45

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Sif Muna peaceful fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:295`](../../crawl-ref/source/dat/database/decorlines.txt#L295)
- Japanese source: 未訳

### English

```text
You struggle to determine the manifold diluted potions present in the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 46

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Sif Muna peaceful fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:299`](../../crawl-ref/source/dat/database/decorlines.txt#L299)
- Japanese source: 未訳

### English

```text
You struggle to identify the manner of creatures' blood used in this fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 47

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Sif Muna peaceful fountain_eyes`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:303`](../../crawl-ref/source/dat/database/decorlines.txt#L303)
- Japanese source: 未訳

### English

```text
You idly identify at least [five|six] types of eyes growing in the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 48

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Trog peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:307`](../../crawl-ref/source/dat/database/decorlines.txt#L307)
- Japanese source: 未訳

### English

```text
{{
if you.transform() == "wisp" then
  return "Your reflection in the fountain writhes with quiet rage."
elseif you.transform() == "fungus" then
  return "You briefly stop and wring some of the blood out of your mycelia."
else
  return "You briefly stop and wash some of the blood off your face."
end
}}
```

### 日本語

```text
（未訳）
```

---

## Entry 49

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Uskayaw peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:319`](../../crawl-ref/source/dat/database/decorlines.txt#L319)
- Japanese source: 未訳

### English

```text
You do an impromptu, brief dance in the water, like the crinaeae of old.
```

### 日本語

```text
（未訳）
```

---

## Entry 50

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Uskayaw fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:324`](../../crawl-ref/source/dat/database/decorlines.txt#L324)
- Japanese source: 未訳

### English

```text
The fountain of blood pulses a joyous rhythm of life and death.
```

### 日本語

```text
（未訳）
```

---

## Entry 51

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Vehumet fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:328`](../../crawl-ref/source/dat/database/decorlines.txt#L328)
- Japanese source: 未訳

### English

```text
You sense the potent destructive power at rest in within this fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 52

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Wu Jian peaceful fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:332`](../../crawl-ref/source/dat/database/decorlines.txt#L332)
- Japanese source: 未訳

### English

```text
You briefly muse on the need to flow like the water through this fountain.

w:5
The fountain is calm. The water trickles softly. Here one can find peace.
```

### 日本語

```text
（未訳）
```

---

## Entry 53

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Xom fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:340`](../../crawl-ref/source/dat/database/decorlines.txt#L340)
- Japanese source: 未訳

### English

```text
Harmless butterflyfish stare at you from within the fountain.

w:1
For a brief moment, you thought you saw Xom summoned an eel in this fountain.

w:1
For a terrifying moment, you swear Xom summoned a kraken in this fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 54

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Xom fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:350`](../../crawl-ref/source/dat/database/decorlines.txt#L350)
- Japanese source: 未訳

### English

```text
Shimmering and harmless butterflyfish glower at you from within the fountain.

w:1
For a brief moment, you swear Xom called forth a formless jellyfish here.
```

### 日本語

```text
（未訳）
```

---

## Entry 55

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Xom fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:357`](../../crawl-ref/source/dat/database/decorlines.txt#L357)
- Japanese source: 未訳

### English

```text
Harmless vampiric butterflyfish glare at you from within the fountain.

w:1
For a terrifying moment, you swear Xom placed a vampire kraken in this fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 56

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Yredelemnul fountain_blue`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:364`](../../crawl-ref/source/dat/database/decorlines.txt#L364)
- Japanese source: 未訳

### English

```text
A miniscule dead [mosquito|moth] on the fountain's rim briefly twitches under your umbra.
```

### 日本語

```text
（未訳）
```

---

## Entry 57

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Yredelemnul fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:368`](../../crawl-ref/source/dat/database/decorlines.txt#L368)
- Japanese source: 未訳

### English

```text
@Yredelemnul fountain_blue@
```

### 日本語

```text
（未訳）
```

---

## Entry 58

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Yredelemnul fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:372`](../../crawl-ref/source/dat/database/decorlines.txt#L372)
- Japanese source: 未訳

### English

```text
You dismiss the blood in this fountain as useless to your harvest.
```

### 日本語

```text
（未訳）
```

---

## Entry 59

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Zin fountain_sparkling`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:376`](../../crawl-ref/source/dat/database/decorlines.txt#L376)
- Japanese source: 未訳

### English

```text
You avert your eyes from the scattered magic in the fountain's sparkles.
```

### 日本語

```text
（未訳）
```

---

## Entry 60

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `Zin fountain_eyes`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:380`](../../crawl-ref/source/dat/database/decorlines.txt#L380)
- Japanese source: 未訳

### English

```text
You avert your eyes from the unclean eyes pooled in the fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 61

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `The Shining One fountain_blood`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:384`](../../crawl-ref/source/dat/database/decorlines.txt#L384)
- Japanese source: 未訳

### English

```text
You quietly vow to avenge the poor creatures bled out for this fountain.
```

### 日本語

```text
（未訳）
```

---

## Entry 62

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:389`](../../crawl-ref/source/dat/database/decorlines.txt#L389)
- Japanese source: 未訳

### English

```text
You reach down and sample @_fruit_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 63

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:393`](../../crawl-ref/source/dat/database/decorlines.txt#L393)
- Japanese source: 未訳

### English

```text
You reach down and sample @_meat_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 64

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:397`](../../crawl-ref/source/dat/database/decorlines.txt#L397)
- Japanese source: 未訳

### English

```text
You reach down and sample @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 65

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `_fruit_and_reaction_`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:401`](../../crawl-ref/source/dat/database/decorlines.txt#L401)
- Japanese source: 未訳

### English

```text
an apple. Crisp.

an apricot. Delicious.

a banana. Delicious.

a choko. Bland.

some grapes. Delicious.

some lychee. Delicately sweet.

an orange. Delicious.

some rambutans. Delicious.

some strawberries. Delicious.

a snozzcumber. Putrid!


a tomato. Savoury.

a cherimoya. Tangy!

a mango. Yummy.

a tamarind. Juicy!
```

### 日本語

```text
（未訳）
```

---

## Entry 66

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `_meat_and_reaction_`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:435`](../../crawl-ref/source/dat/database/decorlines.txt#L435)
- Japanese source: 未訳

### English

```text
a smoked eel. Savoury!

a yak sausage. Delicious.

a cured ham hock. Salty.

some adder jerky. Delicious.

a slice of magically-preserved pepperoni pizza. Delicious.

w:6
some smoked snail. Delicious.

w:6
some death yak haggis. Delicious.

w:6
some alligator jerky. Delicious.

w:6
some cured dream mutton. Ephemeral.

w:6
a slice of magically-preserved Pandemonium pizza. Delectable.

w:2
a candy-coated scorpion. Crunchy.

w:2
a pickled kraken tentacle. Astonishing!

w:2
a cured hell ham hock. Spicy!

w:2
some shrike confit. Tangy!

w:2
a century hydra egg. An acquired taste.
```

### 日本語

```text
（未訳）
```

---

## Entry 67

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `_baked_good_and_reaction_`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:480`](../../crawl-ref/source/dat/database/decorlines.txt#L480)
- Japanese source: 未訳

### English

```text
w:24
some spriggan [bread loaf|tarts|rock buns|scones|biscuits|hardtack]. Delicious.

w:14
an orcish [pirog|pastel de nata|bizcocho]. Tasty.

w:14
some elven [shortbread|rye rolls]. Refined.

some merfolk [baklava|tsoureki]. Decadent.

a stuffed naga paratha. Phenomenal.

a draconian baguette. Hearty and warming.

w:6
some [dwarven|kobold|kobold] pretzels. Scrumptious.

w:6
some choko cake. Less bland than expected!

w:2
some [trollish|giant|giant] [wittenberger|grovbrød]. Savoury.

w:2
some tengu anpan. Delightful.

w:2
some ghoulish sourdough. A strange taste.

w:2
some vault guards' spare rations. Filling.

w:2
a strangely fresh circus pie. Mirthful.

w:2
some starflower jam biscuits. A disquieting taste.
```

### 日本語

```text
（未訳）
```

---

## Entry 68

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `carnivore fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:529`](../../crawl-ref/source/dat/database/decorlines.txt#L529)
- Japanese source: 未訳

### English

```text
You peruse the fruit pile and shrug.
```

### 日本語

```text
（未訳）
```

---

## Entry 69

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `carnivore baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:533`](../../crawl-ref/source/dat/database/decorlines.txt#L533)
- Japanese source: 未訳

### English

```text
You peruse the pile and make a meat sandwich with @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 70

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `short fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:538`](../../crawl-ref/source/dat/database/decorlines.txt#L538)
- Japanese source: 未訳

### English

```text
You root around and sample @_fruit_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 71

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `short meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:542`](../../crawl-ref/source/dat/database/decorlines.txt#L542)
- Japanese source: 未訳

### English

```text
You root around and sample @_meat_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 72

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `short baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:546`](../../crawl-ref/source/dat/database/decorlines.txt#L546)
- Japanese source: 未訳

### English

```text
You root around and sample @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 73

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `stone fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:550`](../../crawl-ref/source/dat/database/decorlines.txt#L550)
- Japanese source: 未訳

### English

```text
You pestle and swallow @_fruit_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 74

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `stone meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:554`](../../crawl-ref/source/dat/database/decorlines.txt#L554)
- Japanese source: 未訳

### English

```text
You pestle and swallow @_meat_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 75

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `stone baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:558`](../../crawl-ref/source/dat/database/decorlines.txt#L558)
- Japanese source: 未訳

### English

```text
You mill down and swallow @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 76

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `inediate fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:562`](../../crawl-ref/source/dat/database/decorlines.txt#L562)
- Japanese source: 未訳

### English

```text
You briefly stare at the fruit pile and sigh.
```

### 日本語

```text
（未訳）
```

---

## Entry 77

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `inediate meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:566`](../../crawl-ref/source/dat/database/decorlines.txt#L566)
- Japanese source: 未訳

### English

```text
You briefly stare at the meat pile and sigh.
```

### 日本語

```text
（未訳）
```

---

## Entry 78

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `inediate baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:570`](../../crawl-ref/source/dat/database/decorlines.txt#L570)
- Japanese source: 未訳

### English

```text
You briefly stare at the breadstuffs pile and sigh.
```

### 日本語

```text
（未訳）
```

---

## Entry 79

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `draconian fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:575`](../../crawl-ref/source/dat/database/decorlines.txt#L575)
- Japanese source: 未訳

### English

```text
You reach down and sample @_fruit_and_reaction_@

w:1
You reach down and sample a dragonfruit. You feel vaguely uncomfortable.
```

### 日本語

```text
（未訳）
```

---

## Entry 80

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `felid fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:582`](../../crawl-ref/source/dat/database/decorlines.txt#L582)
- Japanese source: 未訳

### English

```text
You dice up an apple and nibble upon it. Bland.

You dice up a banana and nibble upon it. Bland.

You pick out some berries and nibble upon them. Bland.
```

### 日本語

```text
（未訳）
```

---

## Entry 81

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `felid meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:591`](../../crawl-ref/source/dat/database/decorlines.txt#L591)
- Japanese source: 未訳

### English

```text
You nibble upon @_meat_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 82

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `felid baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:595`](../../crawl-ref/source/dat/database/decorlines.txt#L595)
- Japanese source: 未訳

### English

```text
You nibble upon @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 83

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `gargoyle fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:599`](../../crawl-ref/source/dat/database/decorlines.txt#L599)
- Japanese source: 未訳

### English

```text
@stone fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 84

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `gargoyle meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:603`](../../crawl-ref/source/dat/database/decorlines.txt#L603)
- Japanese source: 未訳

### English

```text
@stone meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 85

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `gargoyle baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:607`](../../crawl-ref/source/dat/database/decorlines.txt#L607)
- Japanese source: 未訳

### English

```text
@stone baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 86

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `kobold fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:611`](../../crawl-ref/source/dat/database/decorlines.txt#L611)
- Japanese source: 未訳

### English

```text
@carnivore fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 87

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `kobold meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:615`](../../crawl-ref/source/dat/database/decorlines.txt#L615)
- Japanese source: 未訳

### English

```text
@short meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 88

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `kobold baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:619`](../../crawl-ref/source/dat/database/decorlines.txt#L619)
- Japanese source: 未訳

### English

```text
@carnivore baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 89

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `mummy fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:623`](../../crawl-ref/source/dat/database/decorlines.txt#L623)
- Japanese source: 未訳

### English

```text
@inediate fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 90

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `mummy meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:627`](../../crawl-ref/source/dat/database/decorlines.txt#L627)
- Japanese source: 未訳

### English

```text
@inediate meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 91

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `mummy baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:631`](../../crawl-ref/source/dat/database/decorlines.txt#L631)
- Japanese source: 未訳

### English

```text
@inediate baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 92

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `oni fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:635`](../../crawl-ref/source/dat/database/decorlines.txt#L635)
- Japanese source: 未訳

### English

```text
You reach down and grab @_fruit_and_reaction_@ You go for seconds.
```

### 日本語

```text
（未訳）
```

---

## Entry 93

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `oni baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:639`](../../crawl-ref/source/dat/database/decorlines.txt#L639)
- Japanese source: 未訳

### English

```text
You reach down and grab @_baked_good_and_reaction_@ You go for seconds.
```

### 日本語

```text
（未訳）
```

---

## Entry 94

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `poltergeist fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:643`](../../crawl-ref/source/dat/database/decorlines.txt#L643)
- Japanese source: 未訳

### English

```text
@inediate fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 95

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `poltergeist meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:647`](../../crawl-ref/source/dat/database/decorlines.txt#L647)
- Japanese source: 未訳

### English

```text
@inediate meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 96

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `poltergeist baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:651`](../../crawl-ref/source/dat/database/decorlines.txt#L651)
- Japanese source: 未訳

### English

```text
@inediate baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 97

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `revenant fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:655`](../../crawl-ref/source/dat/database/decorlines.txt#L655)
- Japanese source: 未訳

### English

```text
@inediate fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 98

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `revenant meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:659`](../../crawl-ref/source/dat/database/decorlines.txt#L659)
- Japanese source: 未訳

### English

```text
@inediate meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 99

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `revenant baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:663`](../../crawl-ref/source/dat/database/decorlines.txt#L663)
- Japanese source: 未訳

### English

```text
@inediate baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 100

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `spriggan fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:667`](../../crawl-ref/source/dat/database/decorlines.txt#L667)
- Japanese source: 未訳

### English

```text
@short fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 101

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `spriggan meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:671`](../../crawl-ref/source/dat/database/decorlines.txt#L671)
- Japanese source: 未訳

### English

```text
You root around, looking for pizza, but fail to find any.

w:4
You find a slice of magically-preserved pizza, and pick the meat off. Delicious!
```

### 日本語

```text
（未訳）
```

---

## Entry 102

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `spriggan baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:678`](../../crawl-ref/source/dat/database/decorlines.txt#L678)
- Japanese source: 未訳

### English

```text
You root around and eagerly enjoy @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 103

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `tengu baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:682`](../../crawl-ref/source/dat/database/decorlines.txt#L682)
- Japanese source: 未訳

### English

```text
You reach down and peck at @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 104

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `troll fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:686`](../../crawl-ref/source/dat/database/decorlines.txt#L686)
- Japanese source: 未訳

### English

```text
@oni fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 105

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `troll baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:690`](../../crawl-ref/source/dat/database/decorlines.txt#L690)
- Japanese source: 未訳

### English

```text
@oni baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 106

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `amphisbaena fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:696`](../../crawl-ref/source/dat/database/decorlines.txt#L696)
- Japanese source: 未訳

### English

```text
You distend one of your jaws to swallow @_fruit_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 107

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `amphisbaena meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:700`](../../crawl-ref/source/dat/database/decorlines.txt#L700)
- Japanese source: 未訳

### English

```text
You distend one of your jaws to swallow @_meat_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 108

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `amphisbaena baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:704`](../../crawl-ref/source/dat/database/decorlines.txt#L704)
- Japanese source: 未訳

### English

```text
You distend one of your jaws to swallow @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 109

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `bat fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:708`](../../crawl-ref/source/dat/database/decorlines.txt#L708)
- Japanese source: 未訳

### English

```text
You slurp up @_fruit_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 110

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `bat baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:712`](../../crawl-ref/source/dat/database/decorlines.txt#L712)
- Japanese source: 未訳

### English

```text
You swoop down and nibble at @_baked_good_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 111

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `blade fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:716`](../../crawl-ref/source/dat/database/decorlines.txt#L716)
- Japanese source: 未訳

### English

```text
You try to grab some fruit with your blades, but fail!

w:4
You use your hands like chopsticks to delicately eat @_fruit_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 112

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `blade meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:723`](../../crawl-ref/source/dat/database/decorlines.txt#L723)
- Japanese source: 未訳

### English

```text
You try to grab some meat with your blades, but fail!

You skewer and sample @_meat_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 113

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `death fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:729`](../../crawl-ref/source/dat/database/decorlines.txt#L729)
- Japanese source: 未訳

### English

```text
@inediate fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 114

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `death meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:733`](../../crawl-ref/source/dat/database/decorlines.txt#L733)
- Japanese source: 未訳

### English

```text
@inediate meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 115

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `death baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:737`](../../crawl-ref/source/dat/database/decorlines.txt#L737)
- Japanese source: 未訳

### English

```text
@inediate baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 116

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `dragon fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:741`](../../crawl-ref/source/dat/database/decorlines.txt#L741)
- Japanese source: 未訳

### English

```text
You devour @_fruit_and_reaction_@

w:1
You devour a dragonfruit. You feel vaguely uncomfortable.
```

### 日本語

```text
（未訳）
```

---

## Entry 117

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `maw fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:748`](../../crawl-ref/source/dat/database/decorlines.txt#L748)
- Japanese source: 未訳

### English

```text
You devour half the fruit pile! It's not enough.
```

### 日本語

```text
（未訳）
```

---

## Entry 118

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `maw meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:754`](../../crawl-ref/source/dat/database/decorlines.txt#L754)
- Japanese source: 未訳

### English

```text
You devour half the meat pile! It's not enough.
```

### 日本語

```text
（未訳）
```

---

## Entry 119

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `maw baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:758`](../../crawl-ref/source/dat/database/decorlines.txt#L758)
- Japanese source: 未訳

### English

```text
You devour half the baked goods pile! It's not enough.
```

### 日本語

```text
（未訳）
```

---

## Entry 120

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `pig fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:762`](../../crawl-ref/source/dat/database/decorlines.txt#L762)
- Japanese source: 未訳

### English

```text
@short fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 121

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `pig meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:766`](../../crawl-ref/source/dat/database/decorlines.txt#L766)
- Japanese source: 未訳

### English

```text
@short meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 122

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `pig baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:770`](../../crawl-ref/source/dat/database/decorlines.txt#L770)
- Japanese source: 未訳

### English

```text
@short baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 123

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `statue fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:774`](../../crawl-ref/source/dat/database/decorlines.txt#L774)
- Japanese source: 未訳

### English

```text
@stone fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 124

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `statue meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:778`](../../crawl-ref/source/dat/database/decorlines.txt#L778)
- Japanese source: 未訳

### English

```text
@stone meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 125

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `statue baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:782`](../../crawl-ref/source/dat/database/decorlines.txt#L782)
- Japanese source: 未訳

### English

```text
@stone baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 126

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `storm fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:786`](../../crawl-ref/source/dat/database/decorlines.txt#L786)
- Japanese source: 未訳

### English

```text
You reach down and electrolyse @_fruit_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 127

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `storm meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:790`](../../crawl-ref/source/dat/database/decorlines.txt#L790)
- Japanese source: 未訳

### English

```text
You reach down and electrolyse @_meat_and_reaction_@
```

### 日本語

```text
（未訳）
```

---

## Entry 128

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `tree fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:794`](../../crawl-ref/source/dat/database/decorlines.txt#L794)
- Japanese source: 未訳

### English

```text
@short fruit cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 129

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `tree meat cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:798`](../../crawl-ref/source/dat/database/decorlines.txt#L798)
- Japanese source: 未訳

### English

```text
@short meat cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 130

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `tree baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:802`](../../crawl-ref/source/dat/database/decorlines.txt#L802)
- Japanese source: 未訳

### English

```text
@short baked goods cache@
```

### 日本語

```text
（未訳）
```

---

## Entry 131

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `vampire fruit cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:806`](../../crawl-ref/source/dat/database/decorlines.txt#L806)
- Japanese source: 未訳

### English

```text
You root around, looking for a blood orange, but fail to find any.

w:4
You reach down and find a blood orange. Delicious.
```

### 日本語

```text
（未訳）
```

---

## Entry 132

- Resource: `crawl-ref/source/dat/database/decorlines.txt`
- English key: `vampire baked goods cache`
- English source: [`crawl-ref/source/dat/database/decorlines.txt:813`](../../crawl-ref/source/dat/database/decorlines.txt#L813)
- Japanese source: 未訳

### English

```text
You reach down and sample @_baked_good_and_reaction_@ Not filling, though, alas.
```

### 日本語

```text
（未訳）
```
