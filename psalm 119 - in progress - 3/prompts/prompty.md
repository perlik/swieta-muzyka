# Psalm 119 — prompty do obrazków (Etap 3)

Czas trwania audio: **403 s (6:43)**. Rozdzielczość docelowa: **2560×1440 (2K), 16:9**.
Granice kadrów wyznaczone na bazie dokładnych znaczników z `txt/napisy.srt` (38 wpisów, 0:00–6:39), z wyprzedzeniem obrazu (lead) ~1 s względem startu ilustrowanej frazy; Kadr 1 zaczyna się o 0:00, ostatni kadr kończy się dokładnie na końcu audio (6:43 — po ostatnim wpisie napisów zostaje ~4 s instrumentalnego wybrzmienia, objęte kadrem finałowym). Wpisy 7–9, 16–18, 24–26 i 31–33 to krótkie (2–5 s) echa wokalne „Twoje słowo…" między refrenami — **nie mają osobnych kadrów**, są wchłonięte w sąsiednie kadry, żeby utrzymać regułę 10–20 s. **26 kadrów**, każdy 10–20 s, pokrycie ciągłe 0:00–6:43 bez dziur i nakładek.

Łuk kolorystyczny (dramaturgia Psalmu 119 — od czystego świtu, przez złoto Słowa, przez noc rozświetloną lampą, do bieli powrotu do domu): Kadry 1–6 (0:00–1:33) chłodny pastelowy świt — kość słoniowa, jasny błękit nieba, delikatny róż, złoto tylko w aureoli i lampie → Kadry 7–17 (1:33–4:31) coraz cieplejsze złoto dominuje (ożywienie z prochu, złoto i miód Słowa, refreny lampy); sceny nocne malowane łagodnym lawendowym błękitem rozświetlonym złotem → Kadry 18–21 (4:31–5:28) most: najcichszy moment tuż przed świtem — lawendowy błękit z pierwszą linią złota na horyzoncie, przechodzący w świt → Kadry 22–26 (5:28–6:43) niemal czysta świetlista biel-złoto (radiant white-gold, luminous white) — pokój, odnaleziona owca, powrót do domu, finał.

Nić przewodnia: **małe złote piórko** — wprowadzone w Kadrze 3 (unosi się nad skarbem Słowa ukrytym w sercu), powraca w Kadrze 7 (unosi się z prochu razem z ożywającym światłem), w Kadrze 13 (dryfuje przy Słowie trwającym na wieki w niebie), w Kadrze 21 (pattern break — niesione strumieniem złotego światła), a w finale (Kadr 25) okazuje się jednym z piór wielkich skrzydeł światła nad doliną.

Pattern breaki (niemal abstrakcyjne wet-on-wet): Kadry 7, 14 i 21 (starty 1:33 / 3:28 / 5:08 — mniej więcej co 100–115 s: ożywienie z prochu, płacz serca zamieniony w radość, splatanie się strumieni Słowa w jedną drogę).

Baranki/owce: **1 kadr z owieczką (Kadr 23) = 1/26 ≈ 4% ≤ 25%** — wers 176 mówi dosłownie „błądziłam jak owca", więc owca musi być w kadrze (zasada wierności tekstowi); poza tym rolę „ja" psalmu pełnią lampa, droga, perspektywa pierwszoosobowa i gołębica.

Kadr psalmistki (jedyna widoczna twarz w filmie, zawsze Kadr 1): **Kadr 1** — kanoniczny, stały kadr otwierający i jednocześnie baza miniatury.

Motyw duchowy (symbolika Boża): Kadry 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 23, 24, 25 (22 z 26 ≈ 85%); czyste pejzaże/oddech: Kadry 2, 19, 22, 26 (4 z 26 ≈ 15%). Proporcja celowo przesunięta w stronę symboliki względem docelowych ~70/30: tekst Psalmu 119 w niemal każdej linijce mówi wprost o Słowie, prawie, lampie i świetle, a utwór praktycznie nie ma partii instrumentalnych — zasada wierności tekstowi (nadrzędna) wymusza symbol Słowa/światła w prawie każdym kadrze.

Rytm skali ujęć (maks. dwa te same pod rząd): zbliżenie, szeroki, detal, średni, średni, szeroki, detal, średni, detal, szeroki, detal, szeroki, średni, detal, średni, szeroki, średni, detal, szeroki, średni, detal, szeroki, średni, szeroki, średni, szeroki. (Jedyny powtórzony sąsiad to Kadry 4–5, oba średnie — dozwolone dwa pod rząd, bez trzech.)

**Kadr na miniaturę: Kadr 1 (psalmistka)**

---

## Stały negative prompt (do każdej generacji)

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, face, facing camera, front view, detailed face, eye contact, wings attached to chest, wings growing from front of body, angel, angelic figure, choir of angels
```

Wyjątek: w Kadrze 1 (psalmistka) pomijamy z powyższego pozycje `face, facing camera, front view, detailed face, eye contact` oraz `angel, angelic figure, choir of angels` — reszta zostaje (szczegóły przy kadrze).

---

## Kadr 1 — 0:00 → 0:17 (17s) · plik `0m00s-0m17s` — **baza miniatury**

**Tekst:** „Szczęśliwi, co czyste drogi wybierają, co prawem Twym żyją i w nim wytrwają." (napisy: 0:00–0:18, kotwica tematyczna — kadr kanoniczny)
**Skala:** duże zbliżenie na twarz (close-up) · **Kolor:** chłodna paleta otwarcia — kość słoniowa, jasny błękit
**Treść:** kanoniczny, obowiązkowy kadr psalmistki — głos śpiewający psalm; spokojna, pogodna twarz młodej kobiety o **jasnych blond włosach**, z miękką złotą aureolą, bez skrzydeł, w bezpośrednim kontakcie wzrokowym z widzem; **psalmistka po prawej stronie kadru**, lewa połowa otwarta na rozmyte światło; dolna lewa część kadru celowo spokojna pod tekst miniatury.
**Negative prompt (tylko ten kadr) — gotowy do skopiowania.** Poniższy blok jest kompletny: stały negative prompt **bez** pozycji `face, facing camera, front view, detailed face, eye contact` i `angel, angelic figure, choir of angels`, z doklejonymi dopiskami tego kadru. Wklejasz to i nic więcej — nie łącz go ze stałym negative promptem, bo wtedy wrócą usunięte pozycje i zabiją twarz oraz kontakt wzrokowy.

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, wings attached to chest, wings growing from front of body, closed eyes, eyes shut, half-closed eyes, downcast eyes, looking away, gaze averted, blindfold, sexy, sensual, seductive, sultry, alluring, glamour, fashion model, beauty photography, makeup, lipstick, glossy lips, parted lips, open mouth, pouting, bare shoulders, cleavage, low neckline, tight clothing, provocative pose, child, little girl, kid, teenager, adolescent, schoolgirl, childlike face, round baby face, chubby cheeks, puffy cheeks, freckles, small childlike features, oversized doe eyes, mature woman, middle-aged, elderly, dark hair, black hair, brown hair, brunette, auburn hair, red hair, ginger hair, grey hair, dyed hair
```

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Large close-up of the face of a young woman, the psalmist, a woman of about 20 to 22 years old, clearly a grown adult woman and not a teenager, with fully adult facial proportions - a longer oval face, defined cheekbones, a slender defined jawline and eyes of normal adult proportion to the face, a plain modest devout young woman, wholesome and innocent, no makeup at all, her lips calmly and completely closed, her expression calm serene and composed, positioned clearly in the right side of the frame with her whole head and shoulders contained within the right half of the composition, her face filling the right half while the entire left half of the frame opens into flowing washes of soft light and pale sky with no figure in it, her head turned in a gentle three-quarter angle so both the front and the side of her face are visible, her long soft light golden blonde hair, fair wheat blonde and clearly lighter and paler than the golden halo behind her, simple and untouched, drifting sideways as if caught by a soft wind, a soft radiant halo of pure golden light glowing behind her head like a ring of pale fire, no wings anywhere on her body, wearing a simple modest plain dress with a high closed neckline covering her shoulders, her eyes wide open and clearly visible, looking straight into the camera in direct eye contact with the viewer despite the angled pose, a calm composed prayerful gaze, her serene adult face softly painted in luminous watercolor, her whole bearing radiating the quiet happiness of one who has chosen the pure way and lives faithfully within God's law, entirely innocent and prayerful, nothing sensual or glamorous, main subject composed in the upper half of the frame, the lower left third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details there (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 2 — 0:17 → 0:31 (14s) · plik `0m17s-0m31s`

**Tekst:** „I moja ścieżka czysta pozostanie, gdy słowa Twojego strzegę nieustannie." (napisy: 0:18–0:32)
**Skala:** plan szeroki (kadr-bohater otwarcia) · **Kolor:** chłodny pastelowy świt — kość słoniowa, jasny błękit
**Treść:** najbardziej spektakularny pejzaż otwarcia — nieskazitelnie czysta, jasna ścieżka wijąca się przez mgliste pastelowe wzgórza ku wschodowi słońca; wielki łagodny snop światła z nieba omywa ścieżkę i utrzymuje ją czystą.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A pristine ivory-white path winding through soft misty pastel hills toward a pale rising dawn, the path immaculately clean and glowing faintly as if freshly washed with light, a vast gentle shaft of radiant light descending from the morning sky and sweeping along the path, keeping it pure and bright while thin veils of blue mist drift aside from its passage, distant meadows waking in cool ivory and sky blue, composed as a grand spectacular opening vista, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 3 — 0:31 → 0:44 (13s) · plik `0m31s-0m44s` — nić przewodnia: wprowadzenie piórka

**Tekst:** „Twą mowę jak skarb w moim sercu ukryłam, bym nigdy przeciw Tobie już nie zgrzeszyła." (napisy: 0:32–0:45)
**Skala:** detal · **Kolor:** chłodna paleta z pierwszym ciepłym blaskiem skarbu
**Treść:** dosłowny skarb w sercu — wewnątrz miękko świecącego, półprzejrzystego serca z różowo-złotego światła spoczywa mały złoty zwój Słowa jak ukryty klejnot; nad skarbem unosi się po raz pierwszy małe złote piórko.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close detail of a large translucent heart of soft rose-gold light floating amid cool ivory and pale blue washes, and hidden safely inside the glowing heart a small golden scroll resting like a precious secret jewel in a treasure chamber, tiny sparks of warm light drifting around it like guarded pearls, the heart's luminous walls sheltering the treasure from the cool mist outside, a small golden feather drifting slowly just above the glowing heart, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 4 — 0:44 → 0:59 (15s) · plik `0m44s-0m59s`

**Tekst:** „Jestem gościem, Panie, na tej obcej ziemi. Niech miłość Twa czuwa nad krokami mymi." (napisy: 0:45–1:00)
**Skala:** plan średni · **Kolor:** chłodna paleta, kopuła złota nad namiotem
**Treść:** mały namiot pielgrzyma na rozległej obcej równinie pod ogromnym niebem, osłonięty półprzejrzystą kopułą bladozłotego światła; obok ścieżka, na której każdy ślad kroku łagodnie świeci — miłość czuwająca nad krokami.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A small humble pilgrim's tent pitched on a vast open foreign plain beneath an immense pale sky, the little tent sheltered under a translucent dome of pale golden light glowing softly around it like a watchful canopy, a narrow path passing beside the tent where each single footprint in the dust glows gently with warm gold as if love itself were watching over every step, the far plain dissolving into cool blue mist and unfamiliar distant hills, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 5 — 0:59 → 1:13 (14s) · plik `0m59s-1m13s`

**Tekst (refren):** „Twoje słowo jest lampą dla stóp moich, Panie. Twoje słowo jest światłem, gdy ciemność nastanie." (napisy: 1:00–1:14)
**Skala:** plan średni, perspektywa pierwszoosobowa · **Kolor:** lawendowy zmierzch rozświetlony złotem lampy
**Treść:** centralny obraz psalmu — widz patrzy „oczami" psalmistki: kamienna ścieżka o zmierzchu, tuż przed widzem unosi się nisko nad ziemią promienna oliwna lampa, jej ciepłe złote światło kładzie się kręgiem dokładnie na najbliższych kamieniach pod stopy; dalej łagodny lawendowy błękit zmierzchu, nigdy groźny.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. First-person view down a smooth stone path at dusk, a radiant antique oil lamp hovering low over the ground just ahead of the viewer, its warm golden flame casting a perfect circle of light exactly onto the next few stepping stones at foot level, the glowing stones inviting the very next step, beyond the lamp's circle the path fading into a gentle lavender-blue evening lit by a few faint watercolor stars, the darkness soft and peaceful rather than threatening, the lamp's glow the one steady certainty on the way, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 6 — 1:13 → 1:33 (20s) · plik `1m13s-1m33s`

**Tekst:** „Prowadzi mnie wiernie przez noc i przez cienie. W Twym słowie jest droga, w Twym słowie zbawienie." + echa „Twoje słowo…" (napisy: 1:14–1:28 + echa 1:28–1:35)
**Skala:** plan szeroki · **Kolor:** łagodna lawendowa noc rozświetlona łańcuchem złota
**Treść:** nocna dolina w miękkim lawendowym błękicie, przez którą wije się jedna droga oświetlona łańcuchem złotych świateł lamp; cienie po bokach drogi rozpływają się tam, gdzie dosięga je blask.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A wide night valley painted in soft lavender-blue, one winding road crossing the whole valley marked by a faithful chain of small golden lamp lights glowing at even intervals into the far distance, the gentle shadows on either side of the road dissolving into pale mist wherever the golden glow reaches them, luminous soft stars scattered above rolling hills, the lit road reading as the only sure way through the peaceful night, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 7 — 1:33 → 1:52 (19s) · plik `1m33s-1m52s` — pattern break · nić przewodnia

**Tekst:** echo „Twoje słowo…" + „Gdy dusza ma w prochu leżała bez siły, to słowa Twe, Panie, znów mnie ożywiły." (napisy: echo 1:35–1:39, wers 1:39–1:53)
**Skala:** detal, niemal abstrakcyjny wet-on-wet · **Kolor:** szarość prochu przechodząca w rozkwitające złoto (początek fazy złotej)
**Treść:** kulminacja emocjonalna — z szaro-beżowych, ciężkich plam prochu na dole kadru wykwita ku górze rozlewające się złoto-różowe światło jak farba rozkwitająca w wodzie: ożywienie duszy przez Słowo; razem ze światłem unosi się z prochu małe złote piórko.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Nearly abstract wet-on-wet dreamscape: heavy grey-beige washes of dust lying low across the bottom of the frame like a soul fallen to the ground without strength, and out of that dust a magnificent bloom of golden-rose light rising and unfurling upward like ink blossoming through water, glowing tendrils of warm gold spreading life back into the cool pigment around them, a small golden feather lifting slowly out of the dust and rising with the light, soft melting gradients, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 8 — 1:52 → 2:06 (14s) · plik `1m52s-2m06s`

**Tekst:** „Dobrze mi, że w życiu zaznałam poniżenia, bo przez nie przyjęłam Twoje pouczenia." (napisy: 1:53–2:07)
**Skala:** plan średni · **Kolor:** cieplejsze złoto, łąka po deszczu
**Treść:** nisko przygięty do ziemi kwiat na łące prostuje się w padającym z nieba miękkim deszczu złotego światła — poniżenie, które staje się pouczeniem i podnosi.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A single slender flower in a wide meadow bent low, its head pressed almost to the ground, and a soft shimmering rain of warm golden light falling from a bright opening in the sky directly onto it, the flower visibly straightening and lifting its head again beneath the gentle luminous rain, drops of light clinging to its petals like dew, the surrounding meadow washed in fresh pale gold after the rain, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 9 — 2:06 → 2:20 (14s) · plik `2m06s-2m20s`

**Tekst:** „Twe prawo mi droższe niż złoto na świecie, a mowa Twa słodsza niż miód zebrany w lecie." (napisy: 2:07–2:21)
**Skala:** detal · **Kolor:** szczyt ciepłego złota i miodu
**Treść:** dosłowne złoto i miód: po jednej stronie stos złotych monet namalowany blado i matowo, obok promienny zwój Słowa świecący mocniej niż wszystkie monety; z plastra miodu spływa gęsty złoty miód łapiący światło — a mowa Boża słodsza i cenniejsza od obu.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Rich close detail still life: on one side a heap of gold coins painted deliberately pale and dull, their shine faded, beside them a radiant open scroll glowing with pure warm light far brighter than all the treasure, and on the other side a golden honeycomb with thick luminous honey slowly dripping and catching the summer light in amber threads, bees absent, the scroll's glow outshining both the gold and the honey, warm golden watercolor washes flooding the whole scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 10 — 2:20 → 2:35 (15s) · plik `2m20s-2m35s`

**Tekst:** „Jestem gościem, Panie, na tej obcej ziemi. Niech miłość Twa czuwa nad krokami mymi." (napisy: 2:21–2:36)
**Skala:** plan szeroki · **Kolor:** ciepłe złoto wieczoru
**Treść:** droga pielgrzyma przez rozległe obce pola w wieczornym świetle; z nieba pochyla się nad drogą wielka łagodna dłoń ze światła, czuwająca nad każdym krokiem — kroki na drodze świecą tam, gdzie sięga jej cień z blasku.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A long pilgrim road crossing vast unfamiliar evening fields toward far hazy hills, and high above the road an immense gentle open hand formed entirely of soft golden light leaning down from the sky, its glowing palm hovering protectively over the way, a trail of single footprints along the road lighting up warmly one after another beneath the watching hand, the foreign land wide and strange but bathed in calm amber light, no human figure anywhere, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 11 — 2:35 → 2:49 (14s) · plik `2m35s-2m49s`

**Tekst (refren):** „Twoje słowo jest lampą dla stóp moich, Panie. Twoje słowo jest światłem, gdy ciemność nastanie." (napisy: 2:36–2:50)
**Skala:** detal · **Kolor:** złoto lampy w lawendowym zmierzchu
**Treść:** zbliżenie samej lampy — stara oliwna lampa stojąca na przydrożnym kamieniu, jej płomień spokojny i pewny; krąg ciepłego światła na bruku ścieżki i źdźbłach trawy, dalej miękki granat-lawenda wieczoru.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Intimate close-up of an antique oil lamp standing on a smooth wayside stone at the edge of a path, its single flame burning perfectly calm and steady, a warm circle of golden lamplight spilling across the worn path stones and the nearest blades of grass at foot level, every pebble inside the circle rendered in loving watercolor detail, beyond the light's reach only soft peaceful lavender dusk, the flame reflected faintly in the polished stone, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 12 — 2:49 → 3:09 (20s) · plik `2m49s-3m09s`

**Tekst:** „Prowadzi mnie wiernie przez noc i przez cienie. W Twym słowie jest droga, w Twym słowie zbawienie." + echa „Twoje słowo…" (napisy: 2:50–3:03 + echa 3:03–3:10)
**Skala:** plan szeroki · **Kolor:** lawendowa noc, rzeka złota, brama światła
**Treść:** nocna dolina, w której droga staje się rzeką płynnego złotego światła, wijącą się między wzgórzami aż do otwartej bramy z czystego światła w obłokach na horyzoncie — w Twym słowie droga i zbawienie.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A sweeping night valley in gentle lavender-blue where the road itself has become a river of flowing molten golden light, winding luminous between soft dark-lavender hills all the way to the horizon, and there at the valley's end a tall open gate of pure radiant light standing among glowing clouds, its doorway pouring pale gold across the sky, the river of light leading faithfully and unbroken from the foreground to the shining gate, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 13 — 3:09 → 3:28 (19s) · plik `3m09s-3m28s` — nić przewodnia

**Tekst:** echo „Twoje słowo…" + „Twe słowo na wieki trwa w niebie, mój Panie. Choć wszystko przemija, ono nie ustanie." (napisy: echo 3:10–3:16, wers 3:16–3:29)
**Skala:** plan średni · **Kolor:** ciepłe złoto ponad chmurami
**Treść:** ponad chmurami — promienny zwój Słowa osadzony wysoko wśród świetlistych obłoków i gwiazd, trwający nieporuszenie; w dole pod chmurami majaczą i rozpływają się jak mgła przemijające krajobrazy i pory roku; przy zwoju dryfuje złote piórko.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. High above the clouds a great radiant scroll of golden light enthroned motionless among luminous cumulus and soft watercolor stars, shining steady and eternal, while far below through gaps in the cloud floor faint fleeting landscapes and passing seasons dissolve like mist - fields fading, rivers shifting, blossoms scattering into vapor - everything passing away except the scroll whose light never wavers, a small golden feather drifting calmly beside its glowing edge, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 14 — 3:28 → 3:42 (14s) · plik `3m28s-3m42s` — pattern break

**Tekst:** „Gdyby mi Twe prawo radości nie dało, zginęłabym dawno, gdy serce płakało." (napisy: 3:29–3:43)
**Skala:** detal, niemal abstrakcyjny wet-on-wet · **Kolor:** błękit łez rozpuszczający się w różowo-złotą radość
**Treść:** blade błękitne smugi jak spływające łzy rozpuszczają się i rozkwitają w promieniującą różowo-złotą radość wokół małego, niegasnącego serca ze światła — prawo, które dało radość płaczącemu sercu.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Nearly abstract wet-on-wet dreamscape: pale blue watery streaks flowing downward like falling tears through soft wet pigment, and at the centre a small steadfast heart of warm golden light that does not go out, the blue tear-washes melting and blooming into radiant rose-gold wherever they touch the heart's glow, joy spreading outward through the wet paper in widening warm rings, sorrow visibly transfigured into light, soft melting gradients, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 15 — 3:42 → 3:57 (15s) · plik `3m42s-3m57s`

**Tekst:** „Jak bardzo miłuję Twoje prawo, Boże. Rozważam je co dzień o każdej porze." (napisy: 3:43–3:58)
**Skala:** plan średni · **Kolor:** złoto przechodzące przez wszystkie pory dnia
**Treść:** jeden ogród przechodzący miękko przez cały kadr od świtu, przez złote południe, po lawendową noc z gwiazdami — a pośrodku, niezmienny przez wszystkie pory, jeden świecący zwój Słowa rozważany o każdej godzinie.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. One continuous garden landscape flowing softly across the frame through every hour of the day - pale rose dawn on the left melting into radiant golden noon at the centre and into gentle lavender night with faint stars on the right - and standing constant in the middle of the garden through all the changing hours a single glowing open scroll of light on a simple stone, its warm radiance identical at dawn, at noon and at night, blossoms and grasses shifting hue around it while its glow never changes, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 16 — 3:57 → 4:11 (14s) · plik `3m57s-4m11s`

**Tekst (refren):** „Twoje słowo jest lampą dla stóp moich, Panie. Twoje słowo jest światłem, gdy ciemność nastanie." (napisy: 3:58–4:12)
**Skala:** plan szeroki · **Kolor:** złote kamienie w lawendowym zmierzchu
**Treść:** długa ścieżka z kamiennych stopni przez wieczorne wzgórza — każdy kamień rozświetla się ciepłym złotem po kolei, jakby światło niewidzialnej lampy szło przodem i zapalało drogę pod stopy.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A long path of flat stepping stones climbing across dusky lavender hills, the stones lighting up one after another with warm inner gold as an unseen lamp's glow travels ahead along the way, the nearest stones burning brightest and the chain of lit stones curving far into the evening distance like a necklace of light laid over the land, soft blue dusk resting peacefully on the meadows either side, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 17 — 4:11 → 4:31 (20s) · plik `4m11s-4m31s`

**Tekst:** „Prowadzi mnie wiernie przez noc i przez cienie. W Twym słowie jest droga, w Twym słowie zbawienie." + echa „Twoje słowo…" (napisy: 4:12–4:25 + echa 4:25–4:32)
**Skala:** plan średni · **Kolor:** noc lawendowa, cienie rozpływające się w złocie
**Treść:** biała gołębica (dusza prowadzona) leci nisko wzdłuż oświetlonej lampami nocnej drogi; smugi cienia po obu stronach zwijają się i rozpływają w złotym świetle w miarę jej przelotu — cienie ustępujące przed Słowem.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A single white dove flying low and steady along a lamplit road through the night, warm golden lamplight pooling on the road beneath its wings, and on either side soft wisps of grey-lavender shadow visibly curling away and dissolving into pale gold light as the dove passes, the shadows retreating gently defeated rather than menacing, the road ahead of the dove already glowing and clear, calm watercolor stars above, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 18 — 4:31 → 4:42 (11s) · plik `4m31s-4m42s`

**Tekst:** echo „Twoje słowo…" + „Ty jesteś ucieczką, Ty jesteś mą tarczą i słowa Twe zawsze w drodze mi wystarczą." (napisy: echo 4:32–4:36, wers 4:36–4:43)
**Skala:** detal · **Kolor:** początek mostu — cichy lawendowy błękit, złoto tarczy
**Treść:** najcichszy moment utworu — wielka okrągła tarcza z ciepłego złotego światła pochylona nad małym, drżącym płomykiem, osłaniająca go przed wirującymi smugami wiatru i mgły; minimalna, intymna kompozycja.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of soft lavender blue, ivory white, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Quiet intimate close scene: a great round shield formed of warm translucent golden light leaning protectively over one small fragile candle flame burning on bare ground, swirling ribbons of cool wind and lavender mist streaming around the shield's curved edge and parting harmlessly to either side, the tiny flame perfectly still and safe inside the sheltered calm, minimal composition with vast soft empty washes around the single protected light, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 19 — 4:42 → 4:54 (12s) · plik `4m42s-4m54s`

**Tekst:** „Zanim świt zabłyśnie, wołam Cię z ufnością i nocą powtarzam Twą mowę z miłością." (napisy: 4:43–4:55)
**Skala:** plan szeroki · **Kolor:** przedświt — lawendowy błękit z pierwszą linią bladego złota
**Treść:** godzina przed świtem: uśpione lawendowe wzgórza, na horyzoncie pierwsza cienka linia bladego złota; na wzgórzu mały dom z jednym ciepło rozświetlonym oknem — ktoś czuwa nocą nad Słowem, wołając ku nadchodzącemu świtowi.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of soft lavender blue, ivory white, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. The quiet hour before dawn: sleeping hills bathed in deep gentle lavender-blue, the last watercolor stars fading, and along the far horizon the first thin breathless line of pale gold announcing the coming sunrise, on one hill a small solitary house with a single window glowing warm amber in the darkness, its faithful light kept burning through the whole night, thin ribbons of mist resting in the valleys, everything hushed and waiting in trust for the dawn, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 20 — 4:54 → 5:08 (14s) · plik `4m54s-5m08s`

**Tekst (refren):** „Twoje słowo jest lampą dla stóp moich, Panie. Twoje słowo jest światłem, gdy ciemność nastanie." (napisy: 4:55–5:09)
**Skala:** plan średni · **Kolor:** złoto lampy stapiające się ze świtem
**Treść:** refren o świcie — lampa na ścieżce, której ciepłe światło stapia się z pierwszymi promieniami wschodzącego słońca zalewającymi drogę; światło lampy i światło świtu stają się jednym.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. An antique oil lamp glowing on a wayside stone as dawn finally breaks, the sun's first long golden rays flooding down the path from the brightening horizon and flowing together with the lamp's warm circle of light until the two glows merge seamlessly into one radiance on the stones, morning mist turning to gold above the road, the lamplight and the sunrise indistinguishable where they meet, the whole path awash in new warm light, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 21 — 5:08 → 5:28 (20s) · plik `5m08s-5m28s` — pattern break · nić przewodnia

**Tekst:** „Prowadzi mnie wiernie przez noc i przez cienie. W Twym słowie jest droga, w Twym słowie zbawienie." + echa „Twoje słowo…" (napisy: 5:09–5:22 + echa 5:22–5:29)
**Skala:** detal, niemal abstrakcyjny wet-on-wet · **Kolor:** strumienie płynnego złota w rozpuszczonym błękicie
**Treść:** ostatni pattern break — strumienie płynnego złotego światła splatają się przez rozmyte lawendowo-błękitne plamy w jedną szeroką, jaśniejącą drogę; małe złote piórko niesione jasnym nurtem.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Nearly abstract wet-on-wet dreamscape: many slender streams of molten golden light flowing and braiding themselves through soft dissolving lavender-blue washes, gradually weaving together into one single broad shining way of light crossing the whole frame, the last stray wisps of blue melting into its brightness, a small golden feather carried gently along the luminous current like a leaf on a stream, soft melting gradients, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 22 — 5:28 → 5:47 (19s) · plik `5m28s-5m47s`

**Tekst:** echo „Twoje słowo…" + „Wielki pokój mają, co Twe prawo kochają i o nic w ciemności się nie potykają." (napisy: echo 5:29–5:34, wers 5:34–5:48)
**Skala:** plan szeroki · **Kolor:** początek finałowej bieli-złota — świetlisty poranek pokoju
**Treść:** wielki pokój — rozległy, pogodny poranny pejzaż: szeroka, gładka droga z kości słoniowej i światła przez spokojne łąki, bez jednego kamienia, o który można by się potknąć; cała dolina skąpana w białozłotym świetle.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, luminous palette of radiant white-gold, ivory white, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast serene morning landscape filled with great peace: one broad perfectly smooth road of ivory and soft light flowing through tranquil sunlit meadows, not a single stone or obstacle anywhere on its surface, gentle white-gold light bathing the whole valley evenly so that no shadow remains to stumble in, calm groves and soft distant hills resting under a luminous pearl sky, an atmosphere of complete unhurried safety, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 23 — 5:47 → 6:01 (14s) · plik `5m47s-6m01s`

**Tekst:** „Błądziłam jak owca, co drogę zgubiła. Odnajdź swą służebnicę, bym z Tobą chodziła." (napisy: 5:48–6:02)
**Skala:** plan średni · **Kolor:** biel-złoto, snop światła odnalezienia
**Treść:** dosłowna owca z wersu 176 (jedyny kadr z owieczką w filmie): samotna biała owieczka na skraju mglistego pola, odnaleziona przez ciepły snop białozłotego światła schodzący z nieba wprost na nią; za nią delikatnie jaśnieje ścieżka powrotna.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, luminous palette of radiant white-gold, ivory white, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A single small white lamb standing at the misty edge of a wide field where the path has faded away, its head lifted, found at last by one warm shaft of white-gold light descending from an opening in the sky directly upon it, the mist around the lamb melting away in the beam's gentle radiance, and behind the lamb the lost path home beginning to glow again faintly through the thinning fog, tender and hopeful, no human figure, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 24 — 6:01 → 6:15 (14s) · plik `6m01s-6m15s`

**Tekst:** „Bo słów Twych, mój Panie, nie zapominałam i do Twego domu wrócić zawsze chciałam." (napisy: 6:02–6:16)
**Skala:** plan szeroki · **Kolor:** biel-złoto powrotu
**Treść:** dom Ojca — promienisty dom na wzgórzu z szeroko otwartymi drzwiami, z których wylewa się białozłote światło; droga wspina się prosto do progu, okna ciepło rozświetlone, niebo świetliste — powrót do domu.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, luminous palette of radiant white-gold, ivory white, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A radiant house set high on a gentle hill, its door standing wide open and pouring warm white-gold light down the hillside like a welcome, every window glowing softly, a winding road climbing straight and unbroken from the foreground meadows up to the open threshold, banners of luminous mist drifting around the hilltop, the whole sky above the house alight with pale gold and pearl white, painted as the longed-for homecoming at the end of the long way, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 25 — 6:15 → 6:31 (16s) · plik `6m15s-6m31s` — nić przewodnia: finał piórka

**Tekst (refren finałowy):** „Twoje słowo jest lampą dla stóp moich, Panie. Twoje słowo jest lampą dla stóp moich, Panie." (napisy: 6:16–6:32)
**Skala:** plan średni · **Kolor:** apoteoza — radiant white-gold
**Treść:** apoteoza lampy — płomień lampy na drodze rozkwita w górę w ogromną jasność, a nad doliną i drogą rozpościerają się wielkie skrzydła z białozłotego światła (motyw krajobrazowy, nie postać); wśród ich piór jaśnieje najmocniej jedno małe złote piórko — to z całego filmu.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, luminous palette of radiant white-gold, ivory white, pale gold and luminous white, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. The lamp on the path at the centre of the valley blossoming upward, its small flame unfurling into an immense soft pillar of white-gold radiance, and out of that light two vast majestic wings of pure white-gold light spreading wide across the sky over the whole valley and the shining road below, the wings a glorious feature of the heavens themselves and not attached to any figure or body, and among their countless luminous feathers one small golden feather glowing brightest of all, the entire landscape flooded with triumphant gentle light, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 26 — 6:31 → 6:43 (12s) · plik `6m31s-6m43s` — kadr finałowy pod ekran końcowy

**Tekst:** „Twoje słowo jest lampą dla stóp moich, Panie." + instrumentalne wybrzmienie (napisy: 6:32–6:39, ogon audio do 6:43)
**Skala:** plan szeroki · **Kolor:** niemal czysta świetlista biel — luminous white
**Treść:** finał pod elementy ekranu końcowego — niemal jednolita przestrzeń świetlistej bieli i bladego złota, w której droga miękko rozpływa się w czyste światło; jedyny delikatny akcent (mały blask lampy) przy LEWEJ krawędzi kadru, środek i prawa część możliwie czyste i spokojne.

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, luminous palette of radiant white-gold, ivory white, pale gold and luminous white, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast almost uniform expanse of luminous white and palest gold light, the faint trace of a road dissolving softly upward into pure radiance until land and sky become one gentle glow, only the softest gradations of ivory, white-gold and pearl across the frame, one small tender glow of a distant lamp kept close to the far left edge of the frame, the centre and right side of the composition intentionally calm, clean and free of any detail, an atmosphere of complete fulfilment and rest, dreamy soft focus. 16:9 cinematic composition.
```
