# Psalm 98 — prompty do obrazków (Etap 3)

Audio: `audio/audio.wav`, 5:15 (314,8 s, 48 kHz). Podstawa czasowa: `txt/napisy.srt` (22 wpisy, czasy Whispera). Kadrów: **22**, każdy 12–20 s, pokrycie 0:00–5:14 bez dziur (ostatni kadr kończy się na 5:14 — audio wystaje 0,79 s i skrypt Etapu 8 sam dociągnie ostatni kadr do końca dźwięku). Granice kadrów ustawione z wyprzedzeniem ~1 s względem startu ilustrowanej frazy (pierwszy kadr od 0:00; wokal wchodzi ~0:09, wcześniej nucone intro).

**Uwaga do zaśpiewanej wersji (potwierdzone transkrypcją izolowanego wokalu `vocals.wav` — obie transkrypcje zgodne):** Suno śpiewa **całą zwrotkę 1 innym tekstem** niż `lirycs.txt`: „Widziałam cuda, które Bóg objawił / gdy od łez smutku ziemię swą wybawił / Zwycięstwo dała Prawica Święta / Jego potęgę każdy pamięta / Ukazał światu swoje zbawienie / budząc we wszystkich wielkie zdumienie". Refren śpiewany jest jako „Śpiewajcie Panu pieśń nową" (raz, bez powtórki) oraz „Niech rzeki klaszczą w dłonie / góry wołają, morze z nami tonie" (zamiast „niech morze i świat cały z nami śpiewają" — 6/6 wystąpień w obu transkrypcjach). Po zwrotce 3 **nie ma refrenu** (od razu bridge), outro kończy się na „a rzeki klaszczą i góry się śmieją" bez finałowego podwójnego „Śpiewajcie Panu…". Kadry rozpisane wg `napisy.srt`, nie wg `lirycs.txt`.

**WYJĄTEK — kadr 1 bez psalmistki (decyzja użytkownika 2026-08-16, tylko ten film):** kadr otwierający to **jeden konkretny element — złota harfa ze strunami światła po prawej stronie kadru** (wzorzec: tarcza odbijająca strzały z Psalmu 91, korona z Psalmu 45), namalowany w **kontrastujących barwach z przeciwległych biegunów koła barw** (rozżarzone złoto ↔ nasycony świetlisty fiolet), żeby miniatura była vivid i odróżniała się w browse od złota na lazurze Psalmu 45. Obowiązkowy kadr psalmistki przeniesiony do **kadru 20** (outro „O Tobie, mój Panie, śpiewam pieśń nową / serce jak harfę niosę przed Tobą"). Reszta serii wraca do standardu (psalmistka = kadr 1).

**Łuk kolorystyczny (psalm radosnego uwielbienia):** kadr 1 celowo najbardziej nasycony (vivid złoto na fiolecie — baza miniatury) → chłodniejszy pastelowy świt z przewagą light sky blue i ivory (2–4) → coraz cieplejsze złoto pieśni i grania (5–9) → pełne ciepłe złoto z różem (10–15) → głębokie bursztynowe złoto nadchodzącego Pana (16–17) → radiant white-gold, niemal czysta świetlista biel (18–22).

**Nić przewodnia:** świetlista wstęga melodii — „pieśń nowa" jako widzialna złota wstęga światła: rodzi się ze strun harfy (kadr 1), wznosi się z doliny ku koronie (5), płynie od strun i rogu w krainy (8), pisze pieśń na niebie (11), biegnie w dal z rozkwitającymi cudami (21), w finale rozpływa się w świcie przy lewej krawędzi (22).

**Pattern breaki:** kadry 4 (0:47, wet-on-wet dobroć rozlana po krańce ziemi), 12 (2:42, wet-on-wet klaszczące rzeki) i 16 (3:36, wet-on-wet nadchodzący Pan); kadr 19 dodatkowo minimalny.

**Limit baranków:** 0 kadrów z barankami/owcami na 22 = 0% ≤ 25%. Motyw duchowy: ~17/22 kadrów (~77%), reszta czyste pejzaże.

**Kadr na miniaturę: Kadr 1 (złota harfa na fiolecie — WYJĄTEK, bez psalmistki).** Kadr psalmistki (20) NIE jest bazą miniatury w tym filmie.

---

## Stały negative prompt (kadry 1–19 i 21–22)

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, face, facing camera, front view, detailed face, eye contact, wings attached to chest, wings growing from front of body
```

Kadr 20 (psalmistka) ma własny, osobny negative prompt — stoi przy kadrze 20. **Nie łączyć go ze stałym.**

---

## Kadr 1 — 0:00–0:20 (plik: `0m00s-0m20s`) — **BAZA MINIATURY (harfa, vivid)** — plan średni

Frazy (wpis 1): „Widziałam cuda, które Bóg objawił / Gdy od łez smutku ziemię swą wybawił"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, vivid complementary palette of radiant glowing gold and deep saturated luminous violet purple, bold warm against cool color contrast, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. On the right side of the frame, a single magnificent golden harp of pure glowing gold, kept entirely within the right half of the composition, its frame blazing like a rising sun and its strings drawn as taut rays of brilliant white-gold light, sparks and small radiant wonders - tiny stars, comets and blossoms of light - bursting from the strings as they play by themselves against a rich vivid violet purple watercolor sky glowing with magenta and amethyst light, thin ribbons of golden melody flowing upward from the strings and swirling around the harp as if a new song rises to heaven, the harp rendered large and unmistakable as the one clear subject, positioned clearly in the right side of the frame while the entire left half of the frame opens into flowing washes of saturated violet and amethyst light with no object in it, luminous wet watercolor blooms where the gold bleeds into the violet, main subject composed in the upper half of the frame, the lower left third of the frame intentionally calm and simple - only soft washes of violet mist and faint golden glow, no important details there (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 2 — 0:20–0:34 (plik: `0m20s-0m34s`) — plan szeroki

Frazy (wpis 2): „Zwycięstwo dała Prawica Święta / Jego potęgę każdy pamięta"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A great open right hand formed of pure golden light reaching down from softly parted morning clouds over a wide waking valley, rays of victory streaming from the luminous palm across the land, banners of soft light unfurling in the sky around it like memories of triumph, the whole valley below catching the glow on rivers and hills, cool pastel dawn blues around the warm radiance, majestic and gentle at once, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 3 — 0:34–0:47 (plik: `0m34s-0m47s`) — plan średni

Frazy (wpis 3): „Ukazał światu swoje zbawienie / Budząc we wszystkich wielkie zdumienie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Vast curtains of pearl and sky blue cloud drawn apart across the heavens like the veils of a great stage, revealing behind them a blazing gate of white-gold radiance - salvation shown openly to the world, its light spilling down onto distant lands and hills at the horizon, flocks of white birds rising from the land in wonder toward the revealed glory, beams of light touching every far corner of the scene, awe and amazement painted as light, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 4 — 0:47–1:01 (plik: `0m47s-1m01s`) — detal — **PATTERN BREAK** (wet-on-wet)

Frazy (wpis 4): „Pan wspomniał na dobroć dla ludu swojego / Ujrzały krańce ziemi zbawienie Jego"

```
Breathtaking wet-on-wet watercolor painting, rich flowing textures, colors bleeding freely into each other in dramatic blooms, warm liquid gold, amber, ivory and gentle rose pigment pouring from the top of the frame and spreading outward like remembered goodness flooding the earth, the golden flow reaching and overflowing the very edges of the frame - the ends of the earth touched by light, small blossoms of rose and pale gold opening wherever the warmth arrives, soft glimpses of a curved horizon beneath the flowing color, almost abstract, luminous and overflowing with kindness, no figures, full bleed with paint covering the entire canvas edge to edge, no white paper borders, radiant and uplifting. 16:9 cinematic composition.
```

## Kadr 5 — 1:01–1:16 (plik: `1m01s-1m16s`) — plan szeroki — nić przewodnia (wstęga #2)

Frazy (wpis 5): „Śpiewajcie Panu pieśń nową / Bo cuda uczynił prawicą swoją"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, ivory white, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A bright morning valley from which a single long ribbon of golden melody-light rises singing into the sky, purely abstract luminous line with no letters and no readable writing, spiraling joyfully upward toward a crown of pure rays shining above the clouds like a gentle sun, and from within the crown's radiance an open hand of soft light scattering small wonders - falling stars and blossoms of light drifting down over the land, the new song rising and the wonders descending in one great exchange of joy, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 6 — 1:16–1:31 (plik: `1m16s-1m31s`) — plan szeroki

Frazy (wpis 6): „Niech rzeki klaszczą w dłonie / Góry wołają, morze z nami tonie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, ivory white, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A jubilant living landscape: silver-blue rivers leaping upward in symmetric arcs of sparkling spray like clapping hands of water, tall mountains on both sides with summits bursting into rays of golden light as if shouting for joy, and at the far horizon a radiant sea swelling and shining, its waves rising to join the song, spray and droplets of light filling the air like applause, the whole earth making music together, exuberant and alive, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 7 — 1:31–1:45 (plik: `1m31s-1m45s`) — plan średni

Frazy (wpis 7): „Wykrzykuj Panu radośnie, ziemio cała / Wesel się śpiewaj, graj Mu na chwałę"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, ivory white, gentle rose and light spring green, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A blossoming orchard meadow erupting with joy in warm morning light, fruit trees bursting into clouds of white and rose blossom all at once, petals and sparks of golden light shooting upward from the grass like shouts of gladness, streams of tiny glowing notes rising from the whole field into the bright sky, the very ground seeming to sing and celebrate, overflowing springtime jubilation, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 8 — 1:45–2:00 (plik: `1m45s-2m00s`) — detal — nić przewodnia (wstęga #3)

Frazy (wpis 8): „Niech przy dźwięku harfy pieśń popłynie / Niech róg zawoła w każdej krainie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of glowing golden harp strings stretched across the frame with a ribbon of luminous melody flowing out from them like a river of light, and beside them a great golden horn raised toward the sky, its call painted as widening rings of soft golden light rolling out over a glimpse of distant lands and hills far below, the ribbon of song and the rings of the horn traveling together into every country on the horizon, festive and solemn joy, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 9 — 2:00–2:13 (plik: `2m00s-2m13s`) — plan średni

Frazy (wpis 9): „Zagrajcie przed Królem naszym Panem / Z sercem otwartym i rozśpiewanym"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Before a majestic throne of white-gold radiance crowned with gentle rays, instruments of light are gathered as if mid-song - a golden lyre, a slender trumpet and a small drum, all shimmering and playing by themselves with sparks of melody rising from their strings and bells, and floating above them a single large open heart of warm ivory-gold light, wide open toward the throne and overflowing with tiny glowing notes, worship painted as music and light, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 10 — 2:13–2:28 (plik: `2m13s-2m28s`) — plan szeroki

Frazy (wpis 10): „Pan wspomniał na dobroć dla ludu swojego / Ujrzały krańce ziemi zbawienie Jego"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of pale gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. The wide curve of the earth seen from high above soft golden clouds at daybreak, the farthest edges of every land and sea catching a rising tide of warm golden light, a single great shaft of radiance descending from an opening in the sky onto the world below like salvation shown to the ends of the earth, small distant hills, coasts and islands all glowing in answer, immense tenderness over the whole horizon, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 11 — 2:28–2:42 (plik: `2m28s-2m42s`) — plan średni — nić przewodnia (wstęga #4)

Frazy (wpis 11): „Śpiewajcie Panu pieśń nową / Bo cuda uczynił prawicą swoją"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of radiant gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Across a glowing evening-gold sky the luminous ribbon of melody writes the new song in flowing calligraphic curves of pure light, purely abstract shining line work with no letters and no readable writing, and where the ribbon curls it blooms into small wonders - stars, comets and flowers of light unfolding from the line, above it a gentle crown of rays parting the clouds and a soft hand of golden light releasing more sparks of wonder along the ribbon's path, the sky itself becoming a written song of praise, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 12 — 2:42–2:54 (plik: `2m42s-2m54s`) — plan szeroki — **PATTERN BREAK** (wet-on-wet)

Frazy (wpis 12): „Niech rzeki klaszczą w dłonie / Góry wołają, morze z nami tonie"

```
Breathtaking wet-on-wet watercolor painting, rich flowing textures, colors bleeding freely into each other in dramatic blooms, silver blue, turquoise and radiant gold pigment splashing upward from the bottom of the frame in great symmetric arcs like rivers clapping their hands, triangles of amber and gold rising behind them like singing mountains, sprays of golden droplets bursting where the arcs meet, a glowing horizon line of molten gold like a shining sea, almost abstract, ecstatic and celebratory, no figures, full bleed with paint covering the entire canvas edge to edge, no white paper borders, radiant and uplifting. 16:9 cinematic composition.
```

## Kadr 13 — 2:54–3:08 (plik: `2m54s-3m08s`) — plan szeroki

Frazy (wpis 13): „Niech szumi morze i wszystko, co żyje / Niech serce świata dla Pana bije"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of pale gold, warm golden light, soft turquoise and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A luminous sea alive with movement under a golden sky, sparkling waves full of leaping fish and gliding white seabirds, dolphins arcing through the glittering water, and above the sea, held in the light of the sky, a great glowing heart of warm rose-gold light pulsing gently like the beating heart of the whole world, rings of soft radiance spreading from each beat across the water and the air, everything that lives moving in rhythm with it, majestic and tender, no human figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 14 — 3:08–3:22 (plik: `3m08s-3m22s`) — plan średni

Frazy (wpis 14): „Niech każdy człowiek na ziemi zaśpiewa / Niech radość wszystkie domy dziś rozgrzewa"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of pale gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A gentle hillside village in warm golden evening light, every single home with its windows glowing amber-warm from within, thin ribbons of golden song rising from open windows and chimneys like visible singing, the streams of melody meeting and weaving together above the rooftops into one bright braid of light ascending into the sky, gardens and lanes washed in the warmth spilling from the houses, joy warming every home, no people visible in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 15 — 3:22–3:36 (plik: `3m22s-3m36s`) — plan szeroki (perspektywa pierwszoosobowa)

Frazy (wpis 15): „I ja zaśpiewam z całym stworzeniem / Bo ujrzałam sama Jego zbawienie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of pale gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. First-person view standing in tall golden meadow grass, one's own path of light opening forward through the field toward a blazing gate of white-gold radiance revealed on the horizon, all creation turned toward it - deer standing still at the meadow's edge bathed in the glow, flocks of white birds streaming overhead toward the light, trees bowing gently in a warm wind, ribbons of song rising from the grass on every side as if the whole field sings together with the viewer, the sensation of seeing salvation with one's own eyes, no human figure in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 16 — 3:36–3:49 (plik: `3m36s-3m49s`) — plan szeroki — **PATTERN BREAK** (wet-on-wet)

Frazy (wpis 16): „Bo Pan nadchodzi, ziemia to czuje / Sprawiedliwością świat swój obdaruje"

```
Breathtaking wet-on-wet watercolor painting, rich flowing textures, colors bleeding freely into each other in dramatic blooms, a vast tide of deep amber, molten gold and warm rose light flooding in from the horizon and rolling toward the viewer across darker honey-toned fields, the wave of radiance making the land bloom wherever it passes - veins of gold and small flowers of light spreading through the washes like the earth trembling with joy at the coming of its King, the sky above opening in great soft blooms of ivory and gold, almost abstract, immense and hopeful, no figures, full bleed with paint covering the entire canvas edge to edge, no white paper borders, radiant and uplifting. 16:9 cinematic composition.
```

## Kadr 17 — 3:49–4:03 (plik: `3m49s-4m03s`) — detal

Frazy (wpis 17): „Przychodzi, aby wszystko naprawić / Każdą łzę otrzeć i pokój zostawić"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of radiant gold, warm golden light, ivory white and the gentlest rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of a single crystal tear suspended in soft warm light, touched from above by one gentle fingertip of a hand formed of pure golden light, and at the touch the tear transforming into a radiant pearl of white-gold glow, tiny sparks of light drifting from it like sorrow turning to peace, beside it a white dove settling calmly with a small olive branch, deep hush and consolation filling the whole frame, everything broken being quietly made whole, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 18 — 4:03–4:17 (plik: `4m03s-4m17s`) — plan szeroki

Frazy (wpis 18): „Śpiewajcie Panu pieśń nową / Bo cuda uczynił prawicą swoją"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of white-gold, luminous white, warm gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast panorama of the whole land singing: countless slender columns of golden light rising from hills, valleys and shores like the pipes of one great organ of praise, all converging high above toward a magnificent crown of pure rays blazing gently at the top of the sky, small wonders - stars and blossoms of light - raining softly down between the columns in answer, heaven and earth joined in one new song, immense, glorious and jubilant, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 19 — 4:17–4:29 (plik: `4m17s-4m29s`) — plan szeroki — **minimalny**

Frazy (wpis 19): „Niech rzeki klaszczą w dłonie / Góry wołają, morze z nami tonie"

```
Breathtaking watercolor painting, rich watercolor textures, soft flowing washes, serene minimal composition, radiant palette of white-gold, luminous white and the palest rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Minimal serene scene of one single flowing line of liquid gold light running across a vast glowing white-gold sky, the line rising and falling gently like the silhouette of mountains, then curling into soft wave-crests like a river and the sea joined in one unbroken melody, tiny sparks of light lifting from its crests like quiet applause, everything else pure luminous wash and stillness, quiet and eternal, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 20 — 4:29–4:43 (plik: `4m29s-4m43s`) — **PSALMISTKA** — zbliżenie (w tym filmie NIE jest bazą miniatury — patrz nagłówek)

Frazy (wpis 20): „O Tobie, mój Panie, śpiewam pieśń nową / Serce jak harfę niosę przed Tobą"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. On the right side of the frame, a large close-up of the face of a young woman, the psalmist, her whole figure kept entirely within the right half of the composition, a woman of about 20 to 22 years old, clearly a grown adult woman and not a teenager, with fully adult facial proportions - a longer oval face, defined cheekbones, a slender defined jawline and eyes of normal adult proportion to the face, a plain modest devout young woman, wholesome and innocent, no makeup at all, her lips calmly and completely closed, her expression calm serene and composed, positioned clearly in the right side of the frame with her whole head and shoulders contained within the right half of the composition, her face filling the right half while the entire left half of the frame opens into flowing washes of soft light and pale sky with no figure in it, her head turned in a gentle three-quarter angle so both the front and the side of her face are visible, her long soft light golden blonde hair, fair wheat blonde and clearly lighter and paler than the golden halo behind her, simple and untouched, drifting sideways as if caught by a soft wind, a soft radiant halo of pure golden light glowing behind her head like a ring of pale fire, no wings anywhere on her body, wearing a simple modest plain dress with a high closed neckline covering her shoulders, her eyes wide open and clearly visible, looking straight into the camera in direct eye contact with the viewer despite the angled pose, a calm composed prayerful gaze, her serene adult face softly painted in luminous watercolor, singing a new song to her Lord with her heart carried before Him like a harp, a faint small glowing heart of golden light drifting in the air near her like a tiny harp of light, entirely innocent and prayerful, nothing sensual or glamorous, main subject composed in the upper half of the frame, the lower left third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details there (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt TYLKO dla tego kadru (kompletny blok — nie doklejać stałego negative promptu!):**

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, wings attached to chest, wings growing from front of body, closed eyes, eyes shut, half-closed eyes, downcast eyes, looking away, gaze averted, blindfold, sexy, sensual, seductive, sultry, alluring, glamour, fashion model, beauty photography, makeup, lipstick, glossy lips, parted lips, open mouth, pouting, bare shoulders, cleavage, low neckline, tight clothing, provocative pose, child, little girl, kid, teenager, adolescent, schoolgirl, childlike face, round baby face, chubby cheeks, puffy cheeks, freckles, small childlike features, oversized doe eyes, mature woman, middle-aged, elderly, dark hair, black hair, brown hair, brunette, auburn hair, red hair, ginger hair, grey hair, dyed hair
```

## Kadr 21 — 4:43–4:56 (plik: `4m43s-4m56s`) — detal — nić przewodnia (wstęga #5)

Frazy (wpis 21): „Będę śpiewała o Twoich cudach / Dopóki pieśń żyje w moich ustach"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of white-gold, warm gold, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. The luminous golden ribbon of melody flowing on across a vast glowing white-gold sky without end, purely abstract shining line with no letters and no readable writing, and all along its endless length small radiant wonders blooming one after another - tiny stars, comets and flowers of light kindling from the ribbon and drifting into the far distance as long as the song lives, the line stretching away over the horizon into pure light, quiet devotion and unending praise, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 22 — 4:56–5:14 (plik: `4m56s-5m14s`) — plan szeroki — kadr finałowy pod ekran końcowy

Frazy (wpis 22 + instrumentalne wybrzmienie do końca audio 5:14,8): „Cała ziemia czeka na Ciebie z nadzieją / A rzeki klaszczą i góry się śmieją"

```
Breathtaking watercolor painting, rich watercolor textures, soft flowing washes, serene composition, radiant palette of luminous white-gold, ivory white and the palest rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast calm expanse of luminous white-gold morning sky over a still, softly glowing land waiting in hope, gentle silver threads of distant rivers catching the light and low hills resting on the far horizon, near the left edge of the frame a tender warm glow of sunrise where the last faint ribbon of golden melody dissolves into the dawn, the center and right side of the frame completely calm, simple and free of any details, pure restful light and peaceful expectation, dreamy soft focus. 16:9 cinematic composition.
```
