# Psalm 45 — prompty do obrazków (Etap 3)

Audio: `audio/audio.wav`, 5:33 (333,3 s, 48 kHz). Podstawa czasowa: `txt/napisy.srt` (24 wpisy, czasy Whispera). Kadrów: **24**, każdy 12–18 s, pokrycie 0:00–5:33 bez dziur. Granice kadrów ustawione z wyprzedzeniem ~1 s względem startu ilustrowanej frazy (pierwszy kadr od 0:00).

**Uwaga do zaśpiewanej wersji:** Suno w obu pre-chorusach śpiewa „Łaska i pokój z Twych słów cicho spływa / W nich Boża miłość na wieki spoczywa" zamiast zapisanego w `lirycs.txt` „Wdzięk się rozlewa na Twych wargach, Panie…" (potwierdzone transkrypcją izolowanego wokalu `vocals.wav` w obu miejscach). Kadry 4 i 10 rozpisane wg faktycznie śpiewanego tekstu z `napisy.srt`, nie wg `lirycs.txt`.

**WYJĄTEK — kadr 1 bez psalmistki (decyzja użytkownika 2026-08-16, tylko ten film):** kadr otwierający to **jeden konkretny element — złota korona królewska po prawej stronie kadru** (wzorzec: tarcza odbijająca strzały z Psalmu 91), namalowany w **kontrastujących barwach z przeciwległych biegunów koła barw** (rozżarzone złoto ↔ nasycony lazurowy błękit), żeby miniatura była vivid. Obowiązkowy kadr psalmistki przeniesiony do **kadru 16** (bridge „Piękno królewskiej córki…"). Reszta serii wraca do standardu (psalmistka = kadr 1).

**Łuk kolorystyczny (psalm weselny, królewski):** kadr 1 celowo najbardziej nasycony (vivid złoto na lazurze — baza miniatury) → chłodniejszy pastelowy poranek z przewagą light sky blue i ivory (2–5) → coraz cieplejsze złoto namaszczenia i ogrodu (6–12) → ciepłe weselne złoto z różem (13–19) → radiant white-gold, niemal czysta świetlista biel chwały (20–24).

**Nić przewodnia:** złote pióro pisarza („język mój biegnie jak pióro pisarza") — pisze wstęgi światła (kadr 2), opada w strumieniu łaski (4), dryfuje wśród grających strun pałacu (9), towarzyszy słuchającej córce (13), pisze pieśń pokoleń (21), w finale wznosi się ku przemienionej koronie i jego melodia wtapia się w jej promienie (23).

**Pattern breaki:** kadry 6 (1:12, wet-on-wet olejek radości), 11 (2:23, wet-on-wet piękno Króla) i 17 (3:45, niemal abstrakcyjna złota tkanina); kadr 21 dodatkowo minimalny.

**Limit baranków:** 0 kadrów z barankami/owcami na 24 = 0% ≤ 25%. Motyw duchowy: ~17/24 kadrów (~70%), reszta czyste pejzaże.

**Kadr na miniaturę: Kadr 1 (złota korona na lazurze — WYJĄTEK, bez psalmistki).** Kadr psalmistki (16) NIE jest bazą miniatury w tym filmie.

---

## Stały negative prompt (kadry 1–15 i 17–24)

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, face, facing camera, front view, detailed face, eye contact, wings attached to chest, wings growing from front of body
```

Kadr 16 (psalmistka) ma własny, osobny negative prompt — stoi przy kadrze 16. **Nie łączyć go ze stałym.**

---

## Kadr 1 — 0:00–0:17 (plik: `0m00s-0m17s`) — **BAZA MINIATURY (korona, vivid)** — plan średni

Frazy (wpis 1): „Z serca mojego dobre słowo płynie / Śpiewam dla króla w tej cichej godzinie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, vivid complementary palette of radiant glowing gold and deep saturated luminous azure blue, bold warm against cool color contrast, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. On the right side of the frame, a single magnificent royal crown of pure glowing gold, kept entirely within the right half of the composition, the crown blazing like a rising sun with long golden rays and sparks of light streaming from its points against a rich vivid azure blue watercolor sky, thin ribbons of golden light like a sung melody flowing upward from below and swirling around the crown as if a song rises toward the King, the crown rendered large and unmistakable as the one clear subject, positioned clearly in the right side of the frame while the entire left half of the frame opens into flowing washes of saturated azure blue and turquoise light with no object in it, luminous wet watercolor blooms where the gold bleeds into the blue, main subject composed in the upper half of the frame, the lower left third of the frame intentionally calm and simple - only soft washes of azure mist and faint golden glow, no important details there (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 2 — 0:17–0:31 (plik: `0m17s-0m31s`) — detal — nić przewodnia (pióro #1)

Frazy (wpis 2): „Język mój biegnie jak pióro pisarza / Gdy piękno twoje moja pieśń powtarza"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of a large elegant golden quill feather gliding swiftly across a parchment of pale morning sky, writing not ink but flowing calligraphic ribbons of glowing golden light, purely abstract luminous line work with no letters and no readable writing, and where the shining strokes curve they bloom into small images of beauty - tiny white blossoms, stars and rays unfolding from the lines, the quill alive with joyful motion as if racing to keep up with a song, soft washes of dawn blue around it, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 3 — 0:31–0:46 (plik: `0m31s-0m46s`) — plan szeroki

Frazy (wpis 3): „Przyszłam ci dzisiaj śpiewać pieśń weselną / W sercu swym niosę miłość niepodzielną"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. First-person view of a long wedding path strewn thickly with white flower petals, garlands of white blossoms and pale ribbons arching over the path like a bridal way, the path leading across a soft morning meadow toward a distant radiant palace of light on the horizon, and floating above the path ahead a single small radiant heart of warm ivory-gold light, whole and undivided, carried forward toward the palace, gentle sky blue morning light over everything, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 4 — 0:46–0:59 (plik: `0m46s-0m59s`) — plan średni — nić przewodnia (pióro #2)

Frazy (wpis 4, tekst faktycznie śpiewany): „Łaska i pokój z twych słów cicho spływa / W nich Boża miłość na wieki spoczywa"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. From softly parted luminous clouds a quiet gentle stream of golden light flows down like a slow silent waterfall of grace into a calm green valley, a white dove gliding peacefully down along the stream of light, and where the light comes to rest on the land soft flowers of light bloom and remain glowing, love settling on the earth to stay forever, a single small golden feather drifting slowly down inside the luminous stream, deep hush and peace over the whole scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 5 — 0:59–1:12 (plik: `0m59s-1m12s`) — plan szeroki

Frazy (wpis 5): „Tyś najpiękniejszy królu uwielbiony / Tron twój o Boże na wieki niewzruszony"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, light sky blue, pale gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A majestic throne of radiant white-gold light standing utterly unshaken on a high rock rising above a sea of soft morning clouds, above the throne a crown of pure rays blazing gently like a sun, broad beams of light descending from it across the clouds, the rock and throne immovable and eternal while the clouds drift and part around them, grandeur and holy beauty, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 6 — 1:12–1:25 (plik: `1m12s-1m25s`) — plan średni — **PATTERN BREAK** (wet-on-wet)

Frazy (wpis 6): „Umiłowałeś drogę sprawiedliwości / Więc Bóg cię namaścił olejkiem radości"

```
Breathtaking wet-on-wet watercolor painting, rich flowing textures, colors bleeding freely into each other in dramatic blooms, warm liquid gold, amber, rose and ivory pigment pouring from the top of the frame downward like streams of anointing oil made of light, the golden streams blossoming into flowers of rose and pale gold wherever they fall, a faint soft suggestion of a crown near the bottom receiving the flowing gold, almost abstract, luminous and overflowing with joy, no figures, full bleed with paint covering the entire canvas edge to edge, no white paper borders, radiant and uplifting. 16:9 cinematic composition.
```

## Kadr 7 — 1:25–1:43 (plik: `1m25s-1m43s`) — plan szeroki

Frazy (wpis 7): „Wyruszasz bronić prawdy i pokory / Sprawiedliwość niesiesz jak światło z góry"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, ivory white, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A single noble rider in a simple flowing bright robe on a white horse, seen fully from behind with his face completely turned away and not visible, riding out from a tall gate of light across a wide open plain toward the dawn, carrying a slender banner of soft white light, correct anatomy, one rider only, ahead of him a broad road of morning light descending from parted clouds onto the plain like justice poured from heaven, wind in the horse's mane and in the robe, hopeful and victorious without any violence, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 8 — 1:43–1:56 (plik: `1m43s-1m56s`) — detal

Frazy (wpis 8): „Twe szaty pachną mirrą drogocenną / Jak ogród pełen kwiatów porą wiosenną"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, ivory white, gentle rose and light spring green, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of the flowing folds of a luminous ivory and white royal robe drifting gently in the air of a blossoming spring garden, the fabric embroidered with fine threads of gold, small glowing amber drops of precious myrrh resin resting in the folds and releasing their fragrance as soft golden mist curling upward, all around flowering branches heavy with white and rose blossom, petals floating through the warm light, no figure visible, only the robe and the garden, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 9 — 1:56–2:10 (plik: `1m56s-2m10s`) — plan szeroki — nić przewodnia (pióro #3)

Frazy (wpis 9): „W pałacach z kości słoniowej struny grają / I pieśnią wesołą ciebie tam witają"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of ivory white, pale gold, gentle rose and light sky blue, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast luminous palace hall of ivory and pearl, slender carved ivory columns rising into soft golden haze, long golden harp strings stretched between the arches shimmering and trembling as they play by themselves, bright sparks of light rising from the strings like notes of a joyful song of welcome, garlands of white flowers wound around the columns, a single small golden feather drifting through the hall among the floating notes of light, festive and glorious, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 10 — 2:10–2:23 (plik: `2m10s-2m23s`) — plan średni

Frazy (wpis 10, tekst faktycznie śpiewany): „Łaska i pokój z twych słów cicho spływa / W nich Boża miłość na wieki spoczywa"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, ivory white, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A perfectly still mountain lake at golden hour, from one bright glowing cloud a gentle rain of golden drops of light falls softly onto the water, each drop opening into a quiet ring of light, and in every ring a small enduring star of light remains resting on the surface, a white dove gliding low and calm across the water between the falling light, love come down to rest and stay, deep serenity, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 11 — 2:23–2:37 (plik: `2m23s-2m37s`) — plan szeroki — **PATTERN BREAK** (wet-on-wet)

Frazy (wpis 11): „Tyś najpiękniejszy królu uwielbiony / Tron twój o Boże na wieki niewzruszony"

```
Breathtaking wet-on-wet watercolor painting, rich flowing textures, colors bleeding freely into each other in dramatic blooms, regal gold, deep rose and ivory pigment flowering across the entire frame like beauty itself made of paint, intricate veins of shimmering gold spreading through the washes, and out of the heart of the blooms a faint radiant suggestion of a crown of rays slowly emerging, almost abstract, majestic and luminous, no figures, full bleed with paint covering the entire canvas edge to edge, no white paper borders, radiant and uplifting. 16:9 cinematic composition.
```

## Kadr 12 — 2:37–2:52 (plik: `2m37s-2m52s`) — detal

Frazy (wpis 12): „Umiłowałeś drogę sprawiedliwości / Więc Bóg cię namaścił olejkiem radości"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, warm amber, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Close-up of an ancient golden anointing horn tilted by two gentle hands formed of pure soft light, pouring a stream of luminous golden oil over a royal crown resting on a simple stone altar, the shining oil running down the crown in glowing ribbons of joy, and wherever a drop falls on the stone small blossoms of light spring open, solemn and joyful at once, warm radiance filling the whole frame, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 13 — 2:52–3:05 (plik: `2m52s-3m05s`) — plan średni — nić przewodnia (pióro #4)

Frazy (wpis 13): „Posłuchaj córko spójrz i nakłoń ucha / Niech serce twoje głosu tego słucha"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, ivory white, gentle rose and light sky blue, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A young woman in a long flowing white bridal veil seen entirely from behind, her face completely hidden and turned away from the viewer, her head gently inclined to one side as she listens, before her a great soft radiance speaking from parted golden clouds, warm rays of light reaching down and touching her veil like a gentle voice, a single small golden feather floating in the air beside her, drawn slowly toward the light, stillness of deep attention, correct anatomy, one figure only, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 14 — 3:05–3:19 (plik: `3m05s-3m19s`) — plan szeroki

Frazy (wpis 14): „Zapomnij domu ojca i narodu / I serca nie oddaj już nikomu"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, ivory white, gentle rose and soft sky blue, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A wide road of pale gold leading away from a small distant homestead on the far left of the frame, the old house and its village softly dissolving into tender morning mist as if lovingly left behind, the road running forward toward a wide open radiant horizon filled with warm rising light, above the road a single small glowing heart of ivory light traveling forward toward the brightness, kept whole and given to no one along the way, farewell without sadness, bright hope ahead, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 15 — 3:19–3:32 (plik: `3m19s-3m32s`) — plan średni

Frazy (wpis 15): „Bo król zapragnął twojej piękności / On panem twoim pokłoń się mu w miłości"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of pale gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. The young woman in her long white bridal veil seen fully from behind, her face completely hidden, kneeling in a graceful low bow before a towering gate of golden light, above the gate a crown of pure rays shining like a gentle sun, the light of the gate flowing forward and wrapping around her like an embrace, her veil spread softly on the ground behind her, devotion and love without fear, correct anatomy, one figure only, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 16 — 3:32–3:45 (plik: `3m32s-3m45s`) — **PSALMISTKA** — zbliżenie (w tym filmie NIE jest bazą miniatury — patrz nagłówek)

Frazy (wpis 16): „Piękno królewskiej córki mieszka w sercu / Gdy staje przed królem na ślubnym kobiercu"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm pastel palette of ivory white, pale gold, warm golden light and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. On the right side of the frame, a large close-up of the face of a young woman, the psalmist, her whole figure kept entirely within the right half of the composition, a woman of about 20 to 22 years old, clearly a grown adult woman and not a teenager, with fully adult facial proportions - a longer oval face, defined cheekbones, a slender defined jawline and eyes of normal adult proportion to the face, a plain modest devout young woman, wholesome and innocent, no makeup at all, her lips calmly and completely closed, her expression calm serene and composed, positioned clearly in the right side of the frame with her whole head and shoulders contained within the right half of the composition, her face filling the right half while the entire left half of the frame opens into flowing washes of soft light and pale sky with no figure in it, her head turned in a gentle three-quarter angle so both the front and the side of her face are visible, her long soft light golden blonde hair, fair wheat blonde and clearly lighter and paler than the golden halo behind her, simple and untouched, drifting sideways as if caught by a soft wind, a soft radiant halo of pure golden light glowing behind her head like a ring of pale fire, no wings anywhere on her body, wearing a simple modest plain dress with a high closed neckline covering her shoulders, her eyes wide open and clearly visible, looking straight into the camera in direct eye contact with the viewer despite the angled pose, a calm composed prayerful gaze, her serene adult face softly painted in luminous watercolor, the quiet beauty of the King's daughter dwelling within her heart as she stands before her King on her wedding day, entirely innocent and prayerful, nothing sensual or glamorous, main subject composed in the upper half of the frame, the lower left third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details there (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

**Negative prompt TYLKO dla tego kadru (kompletny blok — nie doklejać stałego negative promptu!):**

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, wings attached to chest, wings growing from front of body, closed eyes, eyes shut, half-closed eyes, downcast eyes, looking away, gaze averted, blindfold, sexy, sensual, seductive, sultry, alluring, glamour, fashion model, beauty photography, makeup, lipstick, glossy lips, parted lips, open mouth, pouting, bare shoulders, cleavage, low neckline, tight clothing, provocative pose, child, little girl, kid, teenager, adolescent, schoolgirl, childlike face, round baby face, chubby cheeks, puffy cheeks, freckles, small childlike features, oversized doe eyes, mature woman, middle-aged, elderly, dark hair, black hair, brown hair, brunette, auburn hair, red hair, ginger hair, grey hair, dyed hair
```

## Kadr 17 — 3:45–3:59 (plik: `3m45s-3m59s`) — detal — **PATTERN BREAK** (niemal abstrakcyjny)

Frazy (wpis 17): „Jej szata złotem utkana się mieni / Lecz dusza jej droższa od skarbów tej ziemi"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of deep glowing gold, warm amber, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. The entire frame filled with the flowing folds of a gold-woven bridal gown painted almost abstractly, shimmering threads of real gold running through the fabric and catching the light in rippling waves, intricate woven patterns dissolving into pure luminous washes, and deep within the folds one small pearl of pure white light glowing quietly, shining clearly brighter and more precious than all the gold around it, the soul dearer than every treasure, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 18 — 3:59–4:12 (plik: `3m59s-4m12s`) — plan szeroki

Frazy (wpis 18): „Tyś najpiękniejszy królu uwielbiony / Tron twój o Boże na wieki niewzruszony"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of radiant gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast panorama of a throne of blazing white-gold light set on the summit of a great mountain rising above an endless sea of golden clouds, a monumental staircase of light ascending the mountainside toward the throne, above it a crown of rays burning gently like a noon sun, rivers of golden light flowing down the slopes into the clouds, everything immense, glorious and utterly unshakable, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 19 — 4:12–4:26 (plik: `4m12s-4m26s`) — plan średni

Frazy (wpis 19): „Umiłowałeś drogę sprawiedliwości / Więc Bóg cię namaścił olejkiem radości"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, warm palette of radiant gold, warm golden light, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A perfectly straight radiant path running through soft rolling hills toward the light, along its whole length warm golden light raining gently down from an open sky, and everywhere the light touches the ground flowers burst open in waves of white, rose and gold on both sides of the path, the path itself glowing like polished gold, overflowing joy poured out on the way of righteousness, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 20 — 4:26–4:40 (plik: `4m26s-4m40s`) — plan szeroki

Frazy (wpis 20): „Prowadzą mnie dzisiaj wśród wielkiej radości / Wchodzę do pałacu króla mej miłości"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of white-gold, luminous white, warm gold and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. First-person view from the very center of a petal-strewn path as the great gates of a palace of white-gold light swing wide open directly ahead, brilliant welcoming light pouring out through the gates toward the viewer, ribbons of light and drifting white petals arching overhead like a joyful wedding procession, columns of ivory and gold rising on both sides into radiant haze, the sensation of being led forward into the light with great joy, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 21 — 4:40–4:52 (plik: `4m40s-4m52s`) — detal — nić przewodnia (pióro #5) — minimalny

Frazy (wpis 21): „Będę wspominała imię twe / Mój panie przez pokolenia pieśń ta nie ustanie"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of white-gold, warm gold, ivory white and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. Minimal serene scene of the golden quill feather writing across a vast glowing evening-gold sky one single long unbroken flowing ribbon of luminous melody, purely abstract shining line with no letters and no readable writing, the radiant ribbon stretching away over the horizon without end, and all along its length small warm flames of light kindling one from another into the far distance like generations passing on the same song, quiet and eternal, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 22 — 4:52–5:06 (plik: `4m52s-5m06s`) — plan szeroki

Frazy (wpisy 22–23): „Wszystkie ludy będą sławić cię na wieki / Bo ty jesteś dobry i nie jesteś daleki"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of white-gold, luminous white, warm gold and soft rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. The wide curve of the whole earth seen from high above soft clouds at daybreak, from every land and every horizon countless slender columns of golden light rising upward like songs of praise from all the peoples of the world, the columns converging high above toward a great opening of white-gold radiance in the sky, and from that opening warm light reaching back down toward the earth, near and kind, not distant, the whole scene one great meeting of praise rising and goodness descending, no figure anywhere in the scene, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 23 — 5:06–5:19 (plik: `5m06s-5m19s`) — plan średni — nić przewodnia (finał pióra)

Frazy (wpis 24): „Tyś najpiękniejszy królu uwielbiony"

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, radiant palette of luminous white-gold and almost pure glowing white with the faintest rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. High in a heaven of pure white-gold radiance the royal crown appears transfigured, no longer solid gold but woven entirely of brilliant white light, blazing gently like a soft sun with immense calm glory, and rising toward it on a current of light the small golden feather, its long written ribbon of luminous melody trailing behind it and merging seamlessly into the rays of the crown, the song becoming part of the King's eternal glory, overwhelming beauty and peace, dreamy soft focus. 16:9 cinematic composition.
```

## Kadr 24 — 5:19–5:33 (plik: `5m19s-5m33s`) — plan szeroki — kadr finałowy pod ekran końcowy

Frazy: instrumentalne wybrzmienie po ostatnim refrenie (do końca audio 5:33)

```
Breathtaking watercolor painting, rich watercolor textures, soft flowing washes, serene composition, radiant palette of luminous white-gold, ivory white and the palest rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. A vast calm expanse of luminous white-gold sky filled with the softest slow drifting ivory clouds, almost uniform gentle light across the whole frame, only near the left edge of the frame a faint tender glow like the last quiet trace of a crown of light dissolving into the brightness, the center and right side of the frame completely calm, simple and free of any details, pure restful light and peace, dreamy soft focus. 16:9 cinematic composition.
```
