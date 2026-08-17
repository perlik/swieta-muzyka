# Psalm 130 — prompty do obrazków (Etap 3)

Audio: `audio/audio.wav`, 5:56 (355,58 s, 48 kHz). Podstawa czasowa: `txt/napisy.srt` (25 wpisów, czasy Whispera). Kadrów: **25**, każdy 12–20 s, pokrycie 0:00–5:56 bez dziur. Granice kadrów ustawione z wyprzedzeniem ~1 s względem startu ilustrowanej frazy (pierwszy kadr od 0:00).

**Uwaga do struktury zaśpiewanej wersji:** Suno zaśpiewało tekst dokładnie wg `lirycs.txt` — 50 linijek w 25 wpisach po 2 (V1 ×3, PC, CH ×2, V2 ×3, PC, CH ×2, V3 ×3, CH ×2, Bridge ×2, CH ×2, Outro ×4). Bez dośpiewek i pominięć.

**Uwaga do kadru 1:** wpis 2 zaczyna się w 0:22, więc kadr 1 dostaje pełne 20 s (górny limit długości), a kadr 2 wyprzedzenie 2 s zamiast standardowej ~1 s — inaczej kadr 1 miałby 21 s i łamał limit.

**Łuk kolorystyczny (psalm nocnego czuwania — od głębokości do świtu):** chłodna, świetlista lawendowo-błękitna noc z kością słoniową i różem (kadry 1–6) → złoto lamp i światła rosnące w nocy (7–12) → przedświt, coraz więcej ciepłego złota (13–17) → promieniste biało-złote rozlanie (18–21) → wschód słońca i niemal czysta świetlista biel (22–25).

**Nić przewodnia:** małe złote piórko — opada ze światła w głąb rozpadliny (kadr 2), unosi się wśród rozpuszczających się łańcuchów (9), sunie po murach ku wschodowi (14), spoczywa na tafli sadzawki (19), wzlatuje w powietrze wschodu słońca (22), w finale okazuje się częścią wielkich skrzydeł światła nad doliną (25).

**Pattern breaki:** kadry 6 (1:15), 12 (2:38), 18 (4:01) i 23 (5:10).

**Limit baranków:** 0 kadrów z barankami/owcami na 25 = 0% ≤ 25% (rolę „ja" psalmu pełnią: gołębica — kadry 3, 15, 19, 24, perspektywa pierwszoosobowa — kadry 2, 8, 14, oraz symbole chronione: świeca, lampa, namiot, serce). Motyw duchowy: ~17/25 kadrów (~70%), reszta czyste pejzaże.

**Kadr na miniaturę: Kadr 1 (psalmistka).**

---

## Stały negative prompt (kadry 2–25)

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, face, facing camera, front view, detailed face, eye contact, wings attached to chest, wings growing from front of body
```

Kadr 1 (psalmistka) ma własny, osobny negative prompt — stoi przy kadrze 1. **Nie łączyć go ze stałym.**

---

## Kadr 1 — 0:00–0:20 (plik: `0m00s-0m20s`) — **PSALMISTKA, BAZA MINIATURY** — zbliżenie

Frazy (wpis 1): „Wołam Cię, Panie, z ciemności bezdennej / Z dna mego smutku, z nocy tej bezsennej"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. On the right side of the frame, a large close-up of the face of a young woman, the psalmist, her whole figure kept entirely within the right half of the composition, a woman of about 20 to 22 years old, clearly a grown adult woman and not a teenager, with fully adult facial proportions - a longer oval face, defined cheekbones, a slender defined jawline and eyes of normal adult proportion to the face, a plain modest devout young woman, wholesome and innocent, no makeup at all, her lips calmly and completely closed, her expression calm serene and composed, positioned clearly in the right side of the frame with her whole head and shoulders contained within the right half of the composition, her face filling the right half while the entire left half of the frame opens into flowing washes of soft light and pale sky with no figure in it, her head turned in a gentle three-quarter angle so both the front and the side of her face are visible, her long soft light golden blonde hair, fair wheat blonde and clearly lighter and paler than the golden halo behind her, simple and untouched, drifting sideways as if caught by a soft wind, a soft radiant halo of pure golden light glowing behind her head like a ring of pale fire, no wings anywhere on her body, wearing a simple modest plain dress with a high closed neckline covering her shoulders, her eyes wide open and clearly visible, looking straight into the camera in direct eye contact with the viewer despite the angled pose, a calm composed prayerful gaze, her serene adult face softly painted in luminous watercolor, her soul calling out to the Lord from the depths of a sleepless night, waiting for the dawn of His mercy, entirely innocent and prayerful, nothing sensual or glamorous, main subject composed in the upper half of the frame, the lower left third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details there (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt TYLKO dla tego kadru (kompletny blok — nie doklejać stałego negative promptu!):**

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, wings attached to chest, wings growing from front of body, closed eyes, eyes shut, half-closed eyes, downcast eyes, looking away, gaze averted, blindfold, sexy, sensual, seductive, sultry, alluring, glamour, fashion model, beauty photography, makeup, lipstick, glossy lips, parted lips, open mouth, pouting, bare shoulders, cleavage, low neckline, tight clothing, provocative pose, child, little girl, kid, teenager, adolescent, schoolgirl, childlike face, round baby face, chubby cheeks, puffy cheeks, freckles, small childlike features, oversized doe eyes, mature woman, middle-aged, elderly, dark hair, black hair, brown hair, brunette, auburn hair, red hair, ginger hair, grey hair, dyed hair
```

## Kadr 2 — 0:20–0:35 (plik: `0m20s-0m35s`) — plan szeroki — nić przewodnia (piórko #1)

Frazy (wpis 2): „Zabłądziłam daleko, upadłam nisko / Niech Twoje ucho będzie mi tak blisko"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. First-person view from the floor of an immense deep ravine painted in soft luminous lavender blue and ivory mist, far above a small opening of warm golden light where the night sky parts, a faint winding path lost high on the distant rim, the warm radiant light bending and leaning far down into the ravine as if heaven itself leaned close to listen, a single small golden feather drifting slowly down from the light high above into the quiet depth, the deep walls painted gentle and safe with no menace, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 3 — 0:35–0:48 (plik: `0m35s-0m48s`) — detal

Frazy (wpis 3): „Usłysz głos mój, który z głębi się wyrywa / Zobacz duszę, co we łzach Ciebie wzywa"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of a single white dove bursting upward out of soft shadowed blue depths toward pale golden light high above, wings stretched in a strong upward beat, luminous teardrops scattered in the air around it catching the light and turning into tiny golden sparks as they rise, thin veils of lavender mist parting before the dove, the soul tearing itself free of the deep and calling toward heaven, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 4 — 0:48–1:02 (plik: `0m48s-1m02s`) — plan średni

Frazy (wpis 4): „Panie mój, Panie, nachyl się nade mną / Usłysz mój szept, gdy wokół tak ciemno"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast night sky of soft luminous lavender blue bending low like a great tender vault over a single small candle flame standing on a quiet twilight hillside, the heavens arching down so close that a warm band of pale golden light nearly touches the little flame, one thin glowing thread of light rising from the flame like a whisper reaching the bent sky, immense gentle closeness between the great sky and the tiny light, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 5 — 1:02–1:15 (plik: `1m02s-1m15s`) — plan szeroki

Frazy (wpis 5): „Z głębokości wołam do Ciebie, Panie / Usłysz mój głos, usłysz moje błaganie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A wide dramatic view of a deep twilight gorge from whose hidden floor a great column of luminous white-gold light bursts upward, breaking through softly parting clouds into a warm golden opening of heaven, the cry from the depths made visible as rising light, small sparks of gold ascending inside the column like carried words, the gorge walls painted in gentle luminous lavender blue with no darkness or menace, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 6 — 1:15–1:30 (plik: `1m15s-1m30s`) — plan średni, minimalny — **PATTERN BREAK** (wet-on-wet)

Frazy (wpis 6): „Czuwam wśród nocy, aż przyjdzie świtanie / Dusza ma czeka na Twoje zmiłowanie"

```
Breathtaking watercolor painting, rich watercolor textures, wet-on-wet washes bleeding softly into one another, minimal serene composition, airy pastel palette of ivory white, soft lavender blue, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Almost abstract minimal nightscape, a vast calm expanse of deep luminous lavender blue night filling nearly the whole frame, at the far eastern horizon one thin fragile ribbon of pale silver-gold first light, and in the near foreground a single small oil lamp flame burning steadily at the edge of the composition, keeping watch, the immense quiet night and the tiny faithful flame both waiting for the dawn, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 7 — 1:30–1:42 (plik: `1m30s-1m42s`) — detal

Frazy (wpis 7): „Gdybyś pamiętał, Panie, wszystkie winy / Nie ostałabym się ani godziny"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of a great ancient stone tablet standing like an open ledger, covered in long columns of dark handwritten marks of guilt, beside it an old hourglass whose pale sand has almost run out, cool lavender shadow lying softly over the scene, yet at the tablet's edges the dark marks already beginning to blur and thin where a warm forgiving light from above touches the stone, the record too heavy for anyone to stand before, gently starting to fade, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 8 — 1:42–1:57 (plik: `1m42s-1m57s`) — plan szeroki

Frazy (wpis 8): „Któż by się ostał, gdy Ty grzechy liczysz / Kto by śmiał stanąć przed Twoim obliczem"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. An immense radiant gate of white-gold glory standing high among parted clouds, blazing with gentle overwhelming light, and far below a vast empty plain of soft lavender mist where no one is able to stand before that brightness, first-person view from low on the plain looking up at the towering luminous presence, the light immense and holy yet warm and without menace, thin veils of mist bowing and flowing low across the empty ground, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 9 — 1:57–2:11 (plik: `1m57s-2m11s`) — detal — nić przewodnia (piórko #2)

Frazy (wpis 9): „Lecz u Ciebie, Panie, jest przebaczenie / Co uczy bojaźni, budzi uwielbienie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of heavy dark chains wrapped around a small glowing heart of warm golden light, the chains dissolving link by link into swarms of pale golden petals that rise upward like awakening praise, a single small golden feather lifted gently among the rising petals, warm forgiving light pouring down from above and melting every shackle it touches, reverent awe and released joy in one image, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 10 — 2:11–2:25 (plik: `2m11s-2m25s`) — plan średni

Frazy (wpis 10): „Panie mój, Panie, nachyl się nade mną / Usłysz mój szept, gdy wokół tak ciemno"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A small white tent standing alone in a night meadow of soft lavender blue grasses, sheltered beneath a vast translucent dome of warm golden light bending low over it like a protecting hand, the dome's glow resting gently on the tent cloth, pale stars visible far beyond the luminous canopy, thin wisps of night mist stopped softly at the dome's edge, the intimate closeness of heaven bowed down over one small dwelling, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 11 — 2:25–2:38 (plik: `2m25s-2m38s`) — plan szeroki

Frazy (wpis 11): „Z głębokości wołam do Ciebie, Panie / Usłysz mój głos, usłysz moje błaganie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, soft lavender blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Wide view looking down into a great gorge in the deep of night, its hidden floor no longer dark - a rising tide of warm golden light already filling the lower depths and climbing slowly up the lavender blue walls, the cry from the depths being answered from within, soft clouds of luminous mist drifting across the opening, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 12 — 2:38–2:52 (plik: `2m38s-2m52s`) — plan szeroki — **PATTERN BREAK** (wet-on-wet)

Frazy (wpis 12): „Czuwam wśród nocy, aż przyjdzie świtanie / Dusza ma czeka na Twoje zmiłowanie"

```
Breathtaking watercolor painting, rich watercolor textures, wet-on-wet washes bleeding softly into one another, dramatic composition, airy pastel palette of ivory white, soft lavender blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Almost abstract night of flowing indigo-lavender watercolor washes streaming slowly sideways like the long hours of a watch, and from one edge of the frame a deep warm bloom of pale gold spreading into the blue like dawn soaking into night, the two colors meeting in soft feathered wet edges, time itself painted as patient waiting, one faint small spark of light held steady within the blue like a soul awake in the dark, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 13 — 2:52–3:05 (plik: `2m52s-3m05s`) — detal

Frazy (wpis 13): „Złożyłam nadzieję w Twoim świętym słowie / I czekam na Ciebie, aż mi odpowiesz"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, warm pale gold, soft lavender blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of a great ancient book lying open in the quiet lavender night, its pages glowing softly from within, the letters written in living golden light, a few luminous letters lifting gently off the page and rising into the air like the first words of an answer, a small radiant heart of pale gold resting trustingly in the valley of the open pages, warm light pooling around the book, hope laid down upon the holy word, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 14 — 3:05–3:19 (plik: `3m05s-3m19s`) — plan szeroki — nić przewodnia (piórko #3)

Frazy (wpis 14): „Jak strażnik co nocą na murach czuwa / I pierwszego światła na niebie szuka"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, warm pale gold, soft lavender blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. First-person view from the top of ancient stone ramparts in the last hours of night, the weathered pale parapet stretching away along the city wall, a bronze brazier of warm steady flame burning beside the parapet, and far beyond the dark peaceful land the eastern horizon holding a thin growing band of pale gold first light, a single small golden feather drifting along the rampart toward the east, the whole scene leaning toward the coming morning, watchful and calm, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 15 — 3:19–3:34 (plik: `3m19s-3m34s`) — plan średni

Frazy (wpis 15): „Tak moja dusza wygląda Cię w ciemności / Bo po nocy przyjdziesz ze swą światłością"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, warm pale gold, soft lavender blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A white dove perched on the weathered stone edge of a rampart at the end of the night, its head turned toward the eastern sky where the first true rays of pale gold light reach across the land and touch its wings, the dove's white feathers slowly kindling into warm gold wherever the light lands, the darkness visibly thinning all around, quiet certainty that the light is coming, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 16 — 3:34–3:47 (plik: `3m34s-3m47s`) — plan szeroki

Frazy (wpis 16): „Z głębokości wołam do Ciebie, Panie / Usłysz mój głos, usłysz moje błaganie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, warm pale gold, soft lavender blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A wide view of the great gorge at the turning of night into morning, warm radiant light now pouring down from the brightening sky into the depths, flooding the ravine floor with gold so that the once-deep darkness glows from within, soft veils of morning mist rising out of the gorge like released sighs, the walls washed in pale gold and gentle rose, the deep place utterly transformed by descending light, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 17 — 3:47–4:01 (plik: `3m47s-4m01s`) — plan średni

Frazy (wpis 17): „Czuwam wśród nocy, aż przyjdzie świtanie / Dusza ma czeka na Twoje zmiłowanie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, warm pale gold, soft lavender blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A small stone watch-house on a quiet hill, its single eastern window glowing with a calm lamp flame, and beyond it the horizon now distinctly bright with the swelling pale gold promise of dawn, the roofline and hill still resting in soft lavender shadow while the eastern sky warms from blue into gold, the little faithful light and the great coming light facing one another across the peaceful land, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 18 — 4:01–4:15 (plik: `4m01s-4m15s`) — detal — **PATTERN BREAK** (eksplozja rozkwitającej farby)

Frazy (wpis 18): „U Ciebie łaska, obfite odkupienie / Większe niż wina, głębsze niż zwątpienie"

```
Breathtaking watercolor painting, rich watercolor textures, wet-on-wet washes bleeding softly into one another, dramatic composition, airy pastel palette of ivory white, radiant white-gold, warm pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. An overwhelming spring of liquid white-gold light bursting upward and outward in great blooming explosions of radiant watercolor, cascades of luminous gold pouring over the rim of an ancient stone basin and flooding outward without end, the last thin washes of deep blue and shadow being swallowed and dissolved by the spreading gold, abundance beyond measure, redemption deeper and wider than any darkness it covers, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 19 — 4:15–4:29 (plik: `4m15s-4m29s`) — plan średni — nić przewodnia (piórko #4)

Frazy (wpis 19): „Czekaj na Pana, duszo umęczona / Bo żadna noc nie jest nieskończona"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, radiant white-gold, warm pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A weary white dove resting on a smooth pale stone at the edge of a still glassy pool in the first grey-gold light before sunrise, its small body settled and calm after the long night, the last pale stars reflected in the quiet water beside a single small golden feather resting weightlessly on the glassy surface, the eastern sky beyond the pool already softening from lavender into warm rose and gold, the night visibly ending, tender rest and promise, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 20 — 4:29–4:42 (plik: `4m29s-4m42s`) — plan szeroki

Frazy (wpis 20): „Z głębokości wołam do Ciebie, Panie / Usłysz mój głos, usłysz moje błaganie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, radiant white-gold, warm pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast wide valley in the final moments before sunrise, a slow radiant tide of warm golden morning light rising and flowing into it from the east like a flood filling every hollow, the deepest folds of the valley kindling one after another as the gold reaches them, thin morning mists lifting and glowing, the whole deep land rising out of darkness into light, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 21 — 4:42–4:56 (plik: `4m42s-4m56s`) — detal

Frazy (wpis 21): „Czuwam wśród nocy, aż przyjdzie świtanie / Dusza ma czeka na Twoje zmiłowanie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, minimal serene composition, airy pastel palette of ivory white, pale lavender, warm rose and radiant gold, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of the vast pre-dawn sky alone, a single brilliant morning star burning quiet and clear in a field of pale lavender melting into warm rose and gold, the soft dark rim of distant hills only at the very bottom edge of the frame, the hush of the last minute of night, the whole sky one expectant held breath before the sun, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 22 — 4:56–5:10 (plik: `4m56s-5m10s`) — plan szeroki — nić przewodnia (piórko #5)

Frazy (wpis 22): „Już niebo na wschodzie powoli jaśnieje / Noc się kończy, wraca do serca nadzieja"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of luminous white, radiant white-gold, ivory white and warm pale rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Sunrise breaking at last, great radiant beams of white-gold light bursting over the eastern hills and streaming across a waking valley, the sky blooming from rose and lavender into triumphant luminous gold, long soft shadows melting away down the slopes, a single small golden feather rising and dancing high into the bright morning air on the warm wind, the night visibly over, hope pouring back into the world, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 23 — 5:10–5:24 (plik: `5m10s-5m24s`) — plan średni — **PATTERN BREAK** (konstelacja świateł)

Frazy (wpis 23): „Niech czeka Twój lud jak ja dziś czekałam / Bo łaskę i dobroć u Ciebie spotkałam"

```
Breathtaking watercolor painting, rich watercolor textures, loose glowing dabs and blooms of color, dramatic composition, airy pastel palette of luminous white, radiant white-gold, ivory white and warm pale rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Almost abstract wide scene of countless small warm lamp flames kindling one after another across a waking valley beneath the sunrise, each flame a soft round glow of gold in the dissolving blue-grey morning mist, scattered across the land like a constellation come down to earth, a whole people who kept watch through the night now answering the dawn with their little lights, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 24 — 5:24–5:37 (plik: `5m24s-5m37s`) — plan średni

Frazy (wpis 24): „U Pana jest miłość i moc odkupienia / On wszystkie nasze grzechy w przebaczenie zmienia"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of luminous white, radiant white-gold, ivory white and warm pale rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. In full warm morning light, a field of dark heavy stones lifting from the earth and dissolving in mid-air into a rising flight of white doves, each stone unraveling into soft white wings and golden mist the moment the light touches it, the flock climbing joyfully into the radiant white-gold sky, the land beneath left clean and glowing, sins changed into forgiveness before the viewer's eyes, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 25 — 5:37–5:56 (plik: `5m37s-5m56s`) — plan szeroki, FINAŁ (pod ekran końcowy) — nić przewodnia (piórko → skrzydła)

Frazy (wpis 25): „Dusza ma czeka na Twoje zmiłowanie / Dusza ma czeka na Twoje zmiłowanie" + instrumentalne wybrzmienie do 5:56

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, serene composition, airy pastel palette of luminous white, radiant white-gold, ivory white and a whisper of pale rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Immense soft wings of pure white-golden light spread high across the top of the sky over a broad valley now fully bathed in serene morning radiance, the wings a vast heavenly landscape of light and not attached to any figure, small golden feathers drifting up from the peaceful land and dissolving into the great wings as if returning home, the entire scene settling into calm even washes of luminous white-gold, the center and right side of the frame kept intentionally simple and clear with only smooth quiet light and no details there, the wing edges resting near the borders of the composition, total morning peace, dreamy soft focus. 16:9 cinematic composition.
```

---

**Kadr na miniaturę: Kadr 1 (psalmistka).**

Suma kontrolna pokrycia: 0:00–5:56, 25 kadrów, długości 12–20 s (min 12 s — kadr 7, max 20 s — kadr 1; ostatni kadr 19 s), bez dziur i nakładek. Rytm skali: nigdzie więcej niż dwa kadry tej samej skali pod rząd.
