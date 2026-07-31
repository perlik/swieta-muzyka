# Psalm 19 — prompty kadrów (Etap 3)

Audio: 238,3 s (3:58). Źródło czasów: `txt/napisy.srt` (Etap 2, wokal izolowany, 17 wpisów). 16 kadrów, każdy 10–20 s, pokrycie 0:00–3:58,3 bez przerw. Start każdego kadru ~1 s przed startem ilustrowanej frazy (lead), poza kadrem 1 (start 0:00).

**Łuk kolorystyczny:** kadry 1–4 chłodny pastelowy świt (light sky blue, ivory, gentle rose) → kadry 5–12 narastające złoto (pale gold, warm golden light) → kadry 13–16 świetlista biel (luminous white, radiant white-gold).

**Nić przewodnia:** małe złote piórko — pojawia się w kadrze 1, wraca w kadrach 4 (obok gołębicy), 10 (zakładka w księdze światła), 14 (prowadzi po drodze), a w kadrze 16 spoczywa i okazuje się częścią wielkich skrzydeł światła na horyzoncie.

**Pattern breaki:** kadr 7 (~1:29, niemal abstrakcyjny łuk słońca wet-on-wet) i kadr 11 (~2:28, abstrakcyjny rozkwit serca wet-on-wet).

**Baranki/owce:** 0/16 kadrów (limit 25% zachowany z zapasem).

**Kadr na miniaturę: Kadr 2** — decyzja użytkownika: twarz pięknej kobiety z profilu po prawej stronie kadru (wyjątek od zasady ukrytych twarzy), na tle przejścia dnia w noc; twarz w górnej połowie, dolna 1/3 spokojna pod napis.

## Stały negative prompt (wszystkie kadry)

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, face, facing camera, front view, detailed face, eye contact, wings attached to chest, wings growing from front of body, wings, feathered wings, angel wings
```

---

## Kadr 1 — 0:00,0 → 0:15,8 (15,8 s) · plan szeroki · nić: piórko (intro)

Linijki (SRT 1, wokal od 0:04,8): „Niebiosa głoszą chwałę Twoją, Panie, / a gwiazdy niosą rąk Twoich działanie."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Vast pre-dawn heavens declaring glory: an immense luminous sky filled with soft glowing stars and swirling ribbons of pale gold light streaming down toward a sleeping pastel valley, a great radiant burst of white-gold light breaking open above the horizon, one small golden feather drifting down through the starlight, main subject composed in the upper half of the frame, the lower third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details in the lower part (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 2 — 0:15,8 → 0:27,3 (11,5 s) · plan średni · **baza miniatury** · WYJĄTEK: widoczna twarz kobiety z profilu (decyzja użytkownika)

Linijki (SRT 2, wokal od 0:16,8): „Dzień dniowi wieść przekazuje wspaniałą, / noc nocy szepcze o tym, co przetrwało."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Portrait of a beautiful young woman seen in perfect side profile, positioned on the right side of the frame, facing left toward a luminous horizon where golden day melts into starry twilight, delicate serene facial features, eyes gently lowered, peaceful expression, long flowing hair drifting into ribbons of pale gold light and soft stars, warm white-gold glow tracing the line of her profile, her face composed in the upper right of the frame, the lower third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details in the lower part (space reserved for a text overlay), single figure, correct anatomy, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt tylko dla tego kadru** (bez wykluczeń twarzy — twarz ma być widoczna; profil pilnowany wykluczeniami ujęcia frontalnego; dodane strażniki jakości twarzy):

```
crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, deformed face, ugly face, asymmetrical face, facing camera, front view, eye contact, wings, feathered wings, angel wings
```

### Kadr 2 — wariant B (twarz zwrócona prosto w kamerę)

Alternatywne ujęcie do wyboru na miniaturę: ta sama scena i kompozycja (kobieta po prawej, dolna 1/3 spokojna), ale kobieta patrzy prosto w obiektyw.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Portrait of a beautiful young woman positioned on the right side of the frame, facing the viewer directly, gentle eye contact with the camera, delicate serene facial features, soft peaceful gaze, symmetrical beautiful face, long flowing hair drifting into ribbons of pale gold light and soft stars, behind her a luminous horizon where golden day melts into starry twilight, warm white-gold glow illuminating her face, her face composed in the upper right of the frame, the lower third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details in the lower part (space reserved for a text overlay), single figure, correct anatomy, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt dla wariantu B** (bez wykluczeń ujęcia frontalnego — kontakt wzrokowy jest zamierzony; strażniki jakości twarzy zostają):

```
crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, deformed face, ugly face, asymmetrical face, crossed eyes, lazy eye, extra fingers, wings, feathered wings, angel wings
```

## Kadr 3 — 0:27,3 → 0:45,1 (17,8 s) · plan szeroki (panorama)

Linijki (SRT 3+4, wokal od 0:28,3): „Bez słów, bez mowy, w ciszy nieustannej, / ich głos po całej ziemi jest słyszany." + refren: „Niebo nam śpiewa Twą świętą chwałę, / a Twoje Prawo jest doskonałe."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Sweeping panorama of the earth seen from high above, a pastel patchwork of valleys, hills, rivers and a distant sea under a singing sky, translucent ribbons and waves of golden light flowing silently outward across the whole land to the farthest horizon like a soundless song touching every corner of the earth, the sky above opening in soft cascades of radiance, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 4 — 0:45,1 → 1:00,7 (15,6 s) · detal · nić: piórko

Linijki (SRT 5, wokal od 0:46,1): „Duszę zmęczoną wzmacnia i podnosi, / w Twoim słowie serce me radość głosi."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close detail of a white dove rising inside a warm column of golden light, lifted gently by two tender hands of pure light emerging from the glow beneath it, tiny sparks of gold swirling upward, a small golden feather floating beside the dove, soft mist at the bottom dissolving in the warmth, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 5 — 1:00,7 → 1:14,7 (14,0 s) · plan szeroki z postacią

Linijki (SRT 6, wokal od 1:01,7): „Tam słońcu namiot wznosisz w wysokości, / skąd jak pan młody wychodzi z komnaty."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A magnificent glowing tent-pavilion of light set high among rose and gold morning clouds, its shimmering curtains parting like a festive gate, a radiant figure in a bright ceremonial robe stepping out of the doorway, seen from behind, face hidden in light, no wings, a nimbus of white-gold light around the figure, rays streaming from the open pavilion across the sky, single figure, correct anatomy, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 6 — 1:14,7 → 1:28,9 (14,2 s) · plan średni

Linijki (SRT 7, wokal od 1:15,7): „Jak siłacz w biegu, pełen swej radości, / przemierza niebo, blaskiem tka swe szaty."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A radiant angelic figure running joyfully across the open sky, seen from the side as a bright silhouette against the light, face turned away, no wings, halo of white-gold light above the head, his flowing robe woven from long ribbons of sunlight trailing and weaving behind him across the clouds, warm golden trail marking his path, single figure, correct anatomy, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 7 — 1:28,9 → 1:43,8 (14,9 s) · plan szeroki · **pattern break** (niemal abstrakcyjny)

Linijki (SRT 8, wokal od 1:29,9): „Obiega niebo od krańca do krańca, / i nic nie ukryje się przed żarem słońca."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Almost abstract wet-on-wet watercolor: one immense arc of molten gold light spanning the entire sky from horizon to horizon, painted in flowing luminous washes, beneath it a soft warm pastel landscape of hills, river and orchard all glowing in the sun's warmth, no place left untouched by the light, radiant golden washes bleeding into ivory sky, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 8 — 1:43,8 → 1:58,1 (14,3 s) · plan średni · bez postaci

Linijki (SRT 9, refren, wokal od 1:44,8): „Niebo nam śpiewa Twą świętą chwałę, / a Twoje Prawo jest doskonałe."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Two luminous stone tablets of the Law standing on a gentle hilltop, glowing softly from within with warm white-gold light, above them the whole sky opening in great cascades of golden radiance pouring down like sung praise, translucent ribbons of light rising from the pastel valley below like voices joining the song, tiny sparks of gold drifting in the beams, no figures, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 9 — 1:58,1 → 2:13,9 (15,8 s) · detal (perspektywa pierwszoosobowa)

Linijki (SRT 10, wokal od 1:59,1): „Duszę zmęczoną wzmacnia i podnosi, / w Twoim słowie serce me radość głosi."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. First-person view: two luminous hands of pure light reaching out toward the viewer, cradling and gently lifting a small glowing heart of warm gold light up out of soft grey mist into brightening rays, the mist dissolving as the heart rises, sparks of joy scattering around it, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 10 — 2:13,9 → 2:27,7 (13,8 s) · plan średni · nić: piórko (zakładka)

Linijki (SRT 11, wokal od 2:14,9): „Świadectwo Twoje pewne, niezawodne, / prostemu sercu daje mądrość pogodną."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A great open book with pages of soft golden light resting on a cloud, a small golden feather lying across the open pages like a bookmark, an angel seen from behind with head bowed over the book, face not visible, no wings, halo of white-gold light above the head, gentle streams of light flowing up from the pages into the angel's bowed silhouette, single figure, correct anatomy, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 11 — 2:27,7 → 2:41,5 (13,8 s) · **pattern break** (abstrakcja wet-on-wet)

Linijki (SRT 12, wokal od 2:28,7): „Twe przykazania serce rozweselą, / a jasny nakaz oczom blasku udzieli."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Almost abstract wet-on-wet watercolor: a glowing heart-shaped bloom of warm golden light bursting open like a flower in the center of flowing washes of gold, rose and ivory, petals of light and tiny bright sparks scattering joy outward to the very edges of the canvas, pure radiant color in joyful motion, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 12 — 2:41,5 → 2:55,7 (14,2 s) · plan szeroki · bez postaci

Linijki (SRT 13, wokal od 2:42,5): „Bojaźń przed Tobą czysta trwa bez końca, / a Twe wyroki prawdą lśnią jak słońce."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A radiant balance scale woven of pure white-gold light hovering high in the sky and shining like a sun, its great soft beams of truth falling over an endless chain of luminous pastel mountain peaks stretching beyond the horizon, crystal-clear bright air full of reverent stillness, tiny sparks of gold drifting in the rays, no figures, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 13 — 2:55,7 → 3:09,8 (14,1 s) · detal

Linijki (SRT 14, wokal od 2:56,7): „Cenniejsze niż najczystsze złoto ziemi, / i słodsze niż miód, którym się karmimy."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of luminous white, white-gold light, ivory and a whisper of pale rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close luminous still life: a golden honeycomb with honey slowly dripping and a small heap of pure gold beside it, both gently outshone by a scroll of glowing white-gold light hovering above them, the scroll's radiance clearly brighter and more precious than the gold below, soft warm glow filling the whole scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 14 — 3:09,8 → 3:24,6 (14,8 s) · plan średnio-szeroki · nić: piórko

Linijki (SRT 15, wokal od 3:10,8): „Twa sługa przez nie mądrze prowadzona, / a w ich pełnieniu czeka ją korona."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of luminous white, white-gold light, ivory and a whisper of pale rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A gentle path paved with glowing light winding through soft luminous hills toward the horizon, an angel in flowing ivory robes walking the path away from the viewer, seen from behind, face not visible, no wings, halo of white-gold light above the head, far ahead above the path a radiant crown of rays shining in the bright sky, a small golden feather drifting along the path just ahead of the angel, single figure, correct anatomy, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 15 — 3:24,6 → 3:39,2 (14,6 s) · plan średni

Linijki (SRT 16, wokal od 3:25,6): „Oczyść mnie z grzechów przede mną ukrytych, / niech duch mój będzie z pychy mej obmyty."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of luminous white, white-gold light, ivory and a whisper of pale rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A soft waterfall of pure white-gold light pouring down from above onto a kneeling figure seen from behind, head bowed, face not visible, no wings, halo of gentle light, the figure's robes turning bright ivory as the light washes over them, thin grey veils of mist lifting away from the figure and dissolving into the radiance, single figure, correct anatomy, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 16 — 3:39,2 → 3:58,3 (19,1 s) · plan szeroki · kadr finałowy pod ekran końcowy · nić: piórko (finał — część skrzydeł)

Linijki (SRT 17, wokal od 3:40,2 do 3:52,9 + instrumentalny ogon do 3:58,3): „Niech słowa ust mych i serca westchnienia / miłe Ci będą, Skało zbawienia."

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of luminous white, white-gold light, ivory and a whisper of pale rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Serene finale: a vast still landscape dissolved in luminous white-gold light, a soft glowing rock formation rising gently at the far left edge of the frame, at its foot a small golden feather coming to rest, revealed as part of great soft wings of light folded along the left horizon as a landscape motif, the centre and right of the frame kept clean and calm with only smooth washes of luminous white and pale gold sky, no important details in the center or right side of the frame, dreamy soft focus. 16:9 cinematic composition.
```
