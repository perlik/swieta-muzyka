# Psalm 34 — prompty do obrazków (Etap 3)

Granice kadrów wyznaczone na bazie dokładnych znaczników z `txt/napisy.srt`, z wyprzedzeniem obrazu (lead) ~1 s względem startu ilustrowanej frazy. Kadr 1 zaczyna się o 0:00. Ostatni wpis SRT kończy się o 4:09,0, audio trwa 250,5 s — instrumentalny ogon (~1,5 s) pokrywa przedłużony kadr finałowy (Kadr 18) do 4:10,5.

**Kadr psalmistki: Kadr 1** (specjalne życzenie na ten utwór — psalmistka otwiera teledysk zamiast pojawiać się w środku).

Nić przewodnia: **małe złote piórko** — pojawia się w intro (Kadr 1), przewija się przez sceny (Kadry 3, 5, 9, 13, 16), a w finale (Kadr 18) okazuje się częścią wielkich skrzydeł.

Pattern breaki (niemal abstrakcyjne wet-on-wet): Kadry 7 i 14 (co ~90 s); Kadr 17 półabstrakcyjny.

Motyw duchowy (symbolika Boża / Jezus / psalmistka): Kadry 1, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18 (~83%); czyste pejzaże: Kadry 2, 10, 11 (~17%).

Limit baranków/owieczek: baranek występuje tylko w Kadrach 12 i 16 (2/18 = 11% — poniżej limitu 25%).

Łuk kolorystyczny: Kadry 1–5 chłodny pastelowy świt (light sky blue, ivory) → Kadry 6–12 ciepłe blade złoto (pale gold, warm golden light) → Kadry 13–18 świetlista biel (radiant white-gold, luminous white).

Wers „Anioł Pański obozuje wokół bogobojnych" (Kadr 9) zilustrowany zgodnie z zakazem aniołów: wielkie skrzydła światła nad obozowiskiem jako bezosobowy motyw krajobrazowy — żadnej postaci anioła.

Rozdzielczość docelowa: **2560×1440 (2K), 16:9.**

## Stały negative prompt (do każdej generacji poza Kadrem 1)

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, face, facing camera, front view, detailed face, eye contact, wings attached to chest, wings growing from front of body
```

## Negative prompt wyłącznie dla Kadru 1 (psalmistka — twarz dozwolona)

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, wings attached to chest, wings growing from front of body
```

---

## Kadr 1 — 0:00,0 → 0:12,0 (12,0 s) · plik `0m00s-0m12s` — **KADR PSALMISTKI** · **baza miniatury**

**Tekst:** „Będę Pana wysławiać po wszystkie dni" (napisy: 0:00,0–0:13,0). Pierwsza osoba — psalmistka śpiewająca chwałę otwiera teledysk (życzenie użytkownika). Nić przewodnia: złote piórko unosi się obok twarzy. Skomponowany pod miniaturę: twarz w górnej połowie, dolna 1/3 spokojna.

**Skala:** duże zbliżenie (extreme close-up).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Large close-up of a beautiful young woman psalmist filling most of the frame, her head in a gentle three-quarter turn showing the front and side of her face, long flowing hair streaming as if in a soft wind, her eyes looking directly into the camera despite the turned head, serene joyful expression of someone singing praise, a soft halo of pure golden light glowing behind her head, no wings, a single small golden feather drifting in the air beside her face, painted softly and reverently in luminous washes, main subject composed in the upper half of the frame, the lower third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details in the lower part (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** wersja dla Kadru 1 (patrz wyżej — bez wykluczeń twarzy, bez dodawania fraz anielskich).

---

## Kadr 2 — 0:12,0 → 0:27,0 (15,0 s) · plik `0m12s-0m27s`

**Tekst:** „W moich ustach na zawsze Jego chwała brzmi / Niech słyszą to cisi i niech się radują" (napisy: 0:13,0–0:28,0). Pieśń chwały rozchodząca się nad krajobrazem o świcie; radość cichych — ptaki wzbijające się w niebo.

**Skala:** szeroki plan. Czysty pejzaż.

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue and gentle rose with touches of pale gold, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Vast serene valley at pastel dawn, ribbons of golden light flowing across the sky like a visible song of praise, a flock of small white birds rising joyfully from flowering meadows into the pale blue morning sky, soft mist glowing ivory and rose in the valley, sense of quiet hearts awakening to joy, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 3 — 0:27,0 → 0:42,0 (15,0 s) · plik `0m27s-0m42s`

**Tekst:** „Razem wywyższmy imię, co nas ratuje / Szukałam Pana, a On mi odpowiedział" (napisy: 0:28,0–0:43,0). Szukanie i odpowiedź: gołębica wzlatująca ku niebu i snop światła schodzący jej naprzeciw. Nić przewodnia: piórko.

**Skala:** plan średni. Motyw duchowy (snop światła, gołębica).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A single white dove flying upward through soft pastel clouds, searching, while a great warm shaft of golden light breaks through the sky and descends to meet her like an answer from heaven, the dove bathed in the meeting point of light, a small golden feather drifting down along the light beam, sky of light blue and ivory glowing with hope, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 4 — 0:42,0 → 0:55,0 (13,0 s) · plik `0m42s-0m55s`

**Tekst:** „Od wszystkich lęków wybawił, jak obiecał / Spójrzcie na Pana, niech twarze zajaśnieją" (napisy: 0:43,0–0:56,0). Lęki jako mgły rozpraszające się w świetle wschodu; rozjaśnienie oddane kwiatami otwierającymi się ku słońcu (bez postaci ludzkich).

**Skala:** detal. Motyw duchowy (światło rozpraszające lęk).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of delicate white and rose wildflowers opening their petals toward a rising radiant sun, the last pale grey wisps of morning mist dissolving and melting away in the warm light, dew drops glowing like tiny golden lamps on the petals, every flower turned toward the light as if a face brightening with joy, fears evaporating into shining air, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 5 — 0:55,0 → 1:09,0 (14,0 s) · plik `0m55s-1m09s`

**Tekst:** „Ci, co Mu zaufali, wstydu nie zaznają / Skosztujcie i zobaczcie, jak dobry jest Pan" (napisy: 0:56,0–1:10,0). Refren — „skosztujcie" dosłownie: nakryty stół dobroci w snopie niebiańskiego światła. Nić przewodnia: piórko na stole.

**Skala:** plan średni. Motyw duchowy (snop światła).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A simple wooden table set outdoors with fresh golden bread, a jar of glowing honey, ripe pale-gold fruit and a cup of clear water, a wide warm shaft of heavenly light falling from above onto the table like an invitation to taste, a small golden feather resting gently on the white linen tablecloth, soft meadow and pastel sky beyond, atmosphere of generous goodness, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 6 — 1:09,0 → 1:23,0 (14,0 s) · plik `1m09s-1m23s`

**Tekst:** „Szczęśliwy, kto ufność złożył u Jego bram / Skosztujcie i zobaczcie, jak dobry jest Pan" (napisy: 1:10,0–1:24,0). Bramy Pana — otwarta brama światła w obłokach.

**Skala:** szeroki plan. Motyw duchowy (otwarta brama światła).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold and warm golden light with soft sky blue, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Majestic open gate of pure golden light standing among luminous clouds, its tall arches formed of woven rays of light, wide open and welcoming, a soft glowing path of pale gold leading toward the gate across gentle clouds, warm radiance streaming through the opening, sky of ivory and pale blue glowing with promise, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 7 — 1:23,0 → 1:35,0 (12,0 s) · plik `1m23s-1m35s` — **pattern break**

**Tekst:** „On z lęku wybawia i leczy z ran" (napisy: 1:24,0–1:36,0). Niemal abstrakcyjne wet-on-wet: rany (róż) zalewane uzdrawiającym złotem i bielą.

**Skala:** detal / abstrakcja. Motyw duchowy (dłoń światła).

**Prompt:**

```
Breathtaking watercolor painting, rich wet-on-wet watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Almost abstract healing vision: soft crimson and rose watercolor blooms like old wounds being gently washed over and closed by flowing waves of warm gold and luminous ivory light, a tender translucent hand formed of pure light touching the colors and turning every dark stain into shining amber and white, paint bleeding and merging on wet paper, atmosphere of deep comfort and healing, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 8 — 1:35,0 → 1:48,0 (13,0 s) · plik `1m35s-1m48s`

**Tekst:** „Ubogi zawołał, a Pan usłyszał głos / Z każdej niedoli wyrwał i odmienił los" (napisy: 1:36,0–1:49,0). Uboga chatka w dolinie, wołanie usłyszane — snop światła schodzący wprost na nią.

**Skala:** plan średnio-szeroki. Motyw duchowy (snop światła z nieba).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and light sky blue, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A small humble cottage with a softly glowing window standing alone in a quiet valley, a single thin thread of hearth smoke rising like a prayer, and from the parting clouds above a magnificent wide shaft of warm golden light descending directly onto the little house, embracing it completely, the meadows around slowly turning from pale blue shadow into blooming gold, destiny visibly changing, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 9 — 1:48,0 → 2:01,0 (13,0 s) · plik `1m48s-2m01s`

**Tekst:** „Anioł Pański obozuje wokół bogobojnych / Osłania i ocala z rąk wrogów zbrojnych" (napisy: 1:49,0–2:02,0). Zgodnie z zakazem aniołów: wielkie skrzydła światła rozpięte nad obozowiskiem namiotów jako bezosobowy motyw krajobrazowy — żadnej postaci. Nić przewodnia: piórko.

**Skala:** szeroki plan. Motyw duchowy (wielkie skrzydła nad krajobrazem).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and soft lavender blue, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A peaceful camp of glowing ivory tents in a gentle lavender-blue evening landscape, warm golden campfire light spilling between the tents, and arching high above the whole camp a pair of immense translucent wings made of pure golden light spanning the entire sky like a protective canopy over the land, the wings a vast luminous landscape feature not attached to any figure, a small golden feather floating down toward the tents, complete safety and calm, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 10 — 2:01,0 → 2:15,0 (14,0 s) · plik `2m01s-2m15s`

**Tekst:** „Choć lwy młode głodują, ich siła się chwieje / Kto szuka Pana, w dobru pokłada nadzieję" (napisy: 2:02,0–2:16,0). Dosłownie: młode lwy — blade, słabnące sylwetki rozpływające się we mgle, a łąka za nimi kwitnie w świetle.

**Skala:** plan średni. Czysty pejzaż z motywem lwów.

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and soft grey-blue, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Pale ghostly silhouettes of young lions wandering weak and fading at the misty grey-blue edge of the frame, their outlines softly dissolving into morning fog and losing strength, while beyond them a wide sunlit meadow overflows with golden abundance, flowering grasses and warm radiant light, the contrast of fading hunger and blooming goodness, threats melting harmlessly into light, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 11 — 2:15,0 → 2:28,0 (13,0 s) · plik `2m15s-2m28s`

**Tekst:** „Skosztujcie i zobaczcie, jak dobry jest Pan / Szczęśliwy, kto ufność złożył u Jego bram" (napisy: 2:16,0–2:29,0). Refren, 2. wystąpienie — wariant motywu bram z Kadru 6: złota droga wśród sadu owocowego prowadząca ku świetlistej bramie.

**Skala:** szeroki plan. Czysty pejzaż z bramą w tle.

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold and warm golden light with gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A winding path of warm golden light leading through an orchard heavy with ripe glowing fruit, apple and fig trees offering their sweetness along the way, and far at the end of the path a shining open gate of light on the horizon wrapped in luminous ivory clouds, the whole landscape tasting of goodness, invitation and trust, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 12 — 2:28,0 → 2:44,0 (16,0 s) · plik `2m28s-2m44s`

**Tekst:** „Skosztujcie i zobaczcie, jak dobry jest Pan / On z lęku wybawia i leczy z ran" (napisy: 2:29,0–2:45,0). Uzdrowienie uosobione: Jezus (twarz ukryta, od tyłu) pochylony nad zranionym barankiem. Baranek nr 1 z 2.

**Skala:** plan średnio-bliski. Motyw duchowy (postać Jezusa, baranek).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Jesus in a simple luminous white robe seen from behind, face turned away and hidden in soft light, kneeling gently over a small wounded white lamb lying on golden grass, his hands of warm light resting tenderly on the lamb whose wounds close and glow with soft gold under his touch, painted softly and reverently, warm healing radiance surrounding them both, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 13 — 2:44,0 → 2:57,0 (13,0 s) · plik `2m44s-2m57s`

**Tekst:** „Pójdźcie, posłuchajcie, nauczę was drogi / Bojaźni Pańskiej, co odmienia progi" (napisy: 2:45,0–2:58,0). Droga nauki: świetlisty szlak prowadzący przez rozjaśniony próg otwartych drzwi. Nić przewodnia: piórko. Początek fazy biało-złotej.

**Skala:** szeroki plan. Motyw duchowy (droga światła, próg).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of radiant white-gold, ivory white and warm golden light with hints of soft rose, luminous heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A luminous path of white-gold light winding across a gentle landscape toward an old stone doorway standing open in a garden wall, the worn threshold of the door glowing and transformed into shining gold, warm light pouring through the open door from the other side, a small golden feather drifting along the path as if leading the way, atmosphere of gentle teaching and invitation, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 14 — 2:57,0 → 3:12,0 (15,0 s) · plik `2m57s-3m12s` — **pattern break**

**Tekst:** „Bóg blisko jest tych, których serce skruszone / I tych ocala, co na duchu zgnębione" (napisy: 2:58,0–3:13,0). Niemal abstrakcyjny detal: skruszone serce z różowego światła scalane złotem w dłoniach ze światła.

**Skala:** detal / abstrakcja. Motyw duchowy (serce, dłonie światła).

**Prompt:**

```
Breathtaking watercolor painting, rich wet-on-wet watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of radiant white-gold, ivory white, warm golden light and gentle rose, luminous heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Almost abstract close-up of a broken heart shape painted in soft rose watercolor, its cracks being filled and mended with veins of flowing liquid gold like kintsugi, held tenderly in two great cupped hands formed entirely of warm translucent light, golden light spilling through the healed cracks brighter than before, colors bleeding softly on wet paper, atmosphere of closeness and rescue, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 15 — 3:12,0 → 3:26,0 (14,0 s) · plik `3m12s-3m26s`

**Tekst:** „Wiele nieszczęść spada na sprawiedliwego / Lecz Pan go wyrywa z ucisku każdego" (napisy: 3:13,0–3:27,0). Burza rozstępująca się; biały ptak wyrywany z fal ku górze w snopie światła — fale różowieją i złocą się.

**Skala:** szeroki plan. Motyw duchowy (snop światła ratujący).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of radiant white-gold, ivory white, warm golden light and soft lavender blue, luminous heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Soft lavender-grey storm clouds parting wide open over a restless pastel sea, and through the opening a mighty column of white-gold light reaching down and lifting a single white bird up out of the waves, the bird rising safely inside the shaft of light with drops of water turning to gold around its wings, the storm dissolving into rose and ivory glow at the edges, rescue in motion, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 16 — 3:26,0 → 3:41,0 (15,0 s) · plik `3m26s-3m41s`

**Tekst:** „On strzeże starannie każdej jego kości / I żadnej nie pozwoli złamać w nawałności" (napisy: 3:27,0–3:42,0). Ochrona w nawałnicy: baranek nietknięty w kopule złotego światła, wichura rozprasza się wokół. Baranek nr 2 z 2. Nić przewodnia: piórko bezpieczne wewnątrz kopuły.

**Skala:** plan średnio-bliski. Motyw duchowy (kopuła światła, baranek).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of radiant white-gold, ivory white, warm golden light and gentle rose, luminous heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A small white lamb resting completely unharmed and peaceful inside a glowing dome of warm golden light, while outside the dome soft grey-lavender storm winds and rain swirl and break apart harmlessly against the radiance, every gust dissolving into sparks of pale gold, a small golden feather floating safely beside the lamb inside the light, perfect careful protection, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 17 — 3:41,0 → 3:55,0 (14,0 s) · plik `3m41s-3m55s`

**Tekst:** „Zło zgładzi grzesznika, co świętość znieważa / Nie spotka go kara ani zatracenie" (napisy: 3:42,0–3:56,0). Półabstrakcyjnie: cień zła wyparowuje przy krawędzi kadru, pękające okowy rozpływają się w drobiny światła — wyzwolenie sług Pana.

**Skala:** detal / półabstrakcja. Motyw duchowy (światło pochłaniające mrok).

**Prompt:**

```
Breathtaking watercolor painting, rich wet-on-wet watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of radiant white-gold, luminous white and warm golden light with a whisper of soft grey at one edge, heavenly light flooding the canvas, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast flood of luminous white-gold light filling the canvas, at the far left edge the last pale grey shadow evaporating like morning mist into nothing, and in the light broken shackles and chains dissolving into thousands of tiny golden sparks that rise upward like freed birds, evil simply melting away, freedom and deliverance painted in pure light, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

## Kadr 18 — 3:55,0 → 4:10,5 (15,5 s) · plik `3m55s-4m10s` — **kadr finałowy (pod ekran końcowy)**

**Tekst:** „Kto w Panu, kto w Panu znajduje schronienie" (napisy: 3:56,0–4:09,0) + instrumentalny ogon do 4:10,5. Finał nici przewodniej: złote piórko okazuje się częścią wielkich skrzydeł. Schronienie: mały świetlisty namiot przy lewej krawędzi pod łukiem skrzydeł. Środek i prawa strona czyste (ekran końcowy).

**Skala:** bardzo szeroki plan. Motyw duchowy (wielkie skrzydła, schronienie).

**Prompt:**

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, serene composition, airy pastel palette of radiant white-gold, luminous white and pale ivory with the faintest warm rose glow, overwhelming gentle heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast tranquil expanse of luminous white-gold light and soft glowing clouds, near the left edge of the frame one immense wing of golden light arches down over a tiny radiant tent sheltered beneath it, and among the great feathers of the wing one small golden feather glows brighter than the rest, finally home as part of the whole, the center and right side of the frame kept clean and calm as pure soft light with no prominent details, deep peace of refuge, dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt:** stały.

---

**Kadr na miniaturę: Kadr 1** — psalmistka z aureolą złotego światła i kontaktem wzrokowym wprost w kamerę to najmocniejszy, najczytelniejszy w małym rozmiarze motyw serii (ludzka twarz przyciąga wzrok na siatce miniatur skuteczniej niż pejzaż), a kadr jest już skomponowany pod miniaturę: twarz w górnej połowie, dolna 1/3 spokojna (miejsce na napis „Psalm 34 śpiewany").
