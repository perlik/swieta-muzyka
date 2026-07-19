# Etap 3 — Prompty do obrazków (styl wizualny)

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 3 (prompty do obrazków). Zawiera cały styl wizualny, kanoniczny blok promptu i negative prompt. Same generowanie obrazków z tych promptów: patrz Etap 4 (`etap4-generowanie-obrazkow.md`). Rozdzielczość docelowa: patrz `## Rozdzielczość docelowa` niżej — to jedno miejsce, obowiązuje też przy Etapie 4, Etapie 5 i Etapie 7.

**Cel etapu:** rozpisanie kadrów wg poniższych zasad (dosłowność, 10–20 s, lead ~1 s, łuk kolorystyczny, nić przewodnia), oparte na dokładnych znacznikach czasowych per-linijka z `txt/napisy.srt` (wygenerowanego w Etapie 2, który wykonujemy celowo przed tym etapem — patrz `styl-teledysku.md` § „Etapy pracy nad każdym filmem"). Wynik: `prompty.md` w podfolderze `prompts/`.

**Warunek wstępny: plik audio musi istnieć w `audio/` ORAZ musi być już gotowy `txt/napisy.srt`.** Jeśli któregoś z nich brakuje, **nie rozpoczynać Etapu 3** — zatrzymać się i nic nie robić, tylko poinformować użytkownika o braku (audio albo Etapu 2). Dokładne znaczniki czasowe z `napisy.srt` są podstawą rozpisania kadrów i nie da się ich zastąpić samodzielną analizą surowego audio.

**Model: zawsze Fable.** Etap 3 (prompty do obrazków) wykonujemy modelem Fable, niezależnie od modelu/ustawień używanych w reszcie sesji. W praktyce: jeśli bieżąca sesja nie działa na tym modelu, deleguj to zadanie do subagenta z `model: "fable"`.

## Rozdzielczość docelowa

**2560×1440 (2K), format 16:9** — to docelowa rozdzielczość robocza projektu. Obowiązuje przy: generowaniu/upscalowaniu obrazków w Leonardo (Etap 4), kompozycji kadru (ten dokument) oraz eksporcie finalnego wideo z Movavi (patrz Etap 7 w `styl-teledysku.md`). Nie powtarzać pełnego sformułowania poza tym miejscem — odsyłać tutaj.

## Styl: Akwarela / rozmyty pastel — wersja świetlista

Miękkie, rozlewające się plamy koloru na mokrym papierze w jasnej, anielskiej tonacji: kość słoniowa, blade złoto, pastelowy błękit nieba i delikatny róż, z promienistym ciepłym światłem wypełniającym kadr. Granaty i mrok wycofane — nawet sceny nocne malowane łagodnym lawendowym błękitem rozświetlonym złotem, zawsze z perspektywy bezpieczeństwa. Nastrój każdego kadru pozytywny i pełen nadziei; zagrożenia z psalmu (strzała, sieć, zaraza) wyłącznie jako rozpraszające się, rozpływające w świetle.

## Postacie

W teledysku nie występują zwykłe postacie ludzkie. Około **70% kadrów** zawiera postacie duchowe: aniołów (pojedynczych lub w grupach, **bez skrzydeł — zamiast tego z aureolą/nimbem białozłotego światła nad głową**), ewentualnie postać Jezusa (w prostej jasnej szacie, malowaną miękko i z szacunkiem) oraz symbolikę Bożą — wielkie skrzydła nad krajobrazem (jako oddzielny, bezosobowy motyw krajobrazowy, nie atrybut postaci anioła), snop światła z nieba, dłoń światła, gołębica, baranek, korona z promieni, otwarta brama światła. Pozostałe **~30%** to czyste pejzaże: łąki, doliny, świt, sad, droga wśród wzgórz — oddech, głównie w partiach instrumentalnych.

Opieka, która w tekście dotyczy człowieka, wyrażana jest przez symbole (namiot pod kopułą światła, ptak pod skrzydłem, droga wyścielona światłem). Aniołowie i Jezus są humanoidalni, więc zasady anatomii obowiązują: wyraźne rozdzielenie sylwetek przy kilku postaciach i jawny zapis poprawnej anatomii w promptcie.

**Limit baranków i owieczek: maksymalnie 25% kadrów danego filmu.** Baranek/owca może grać duszę chronioną, ale nie w co drugim kadrze — w pozostałych scenach rolę „ja" psalmu pełnią zamiennie: biały gołąb lub inny ptak, sam symbol chroniony (namiot, dom, lampa, serce, korona), postać anioła widziana od tyłu, albo perspektywa pierwszoosobowa (widz patrzy „oczami" psalmisty — np. dłonie światła wyciągnięte KU kamerze, droga rozpościerająca się przed widzem). Przy rozpisywaniu kadrów policzyć: liczba kadrów z barankiem/owcami ≤ 25% wszystkich kadrów filmu.

**Wyjątek:** jeśli sam tekst psalmu jest mocno pasterski — dosłownie mówi o pasterzu, owcach, stadzie, pastwiskach (np. Psalm 23, Psalm 100) — limit nie obowiązuje sztywno i baranków/owiec może być więcej niż 25%, bo wymaga tego zasada wierności tekstowi. W pozostałych psalmach limit stosujemy bez wyjątków.

**Twarze — zasada kluczowa:** AI często generuje zniekształcone, dziwnie wyglądające twarze. Dlatego **twarze postaci (aniołów, Jezusa) nie powinny być widoczne**. Postacie pokazujemy **od tyłu, z boku, z opuszczoną/odwróconą głową, z twarzą skrytą w świetle lub poza kadrem** (np. kadr obcięty poniżej ramion, sylwetka pod światło / kontra). W promptcie zapisywać to jawnie, np.: `seen from behind`, `face turned away`, `head bowed`, `face hidden in light`, `back view`, `profile silhouette`, `figure cropped below the shoulders`. Wyjątek dopuszczalny tylko wtedy, gdy twarz jest daleko i bardzo mała lub całkowicie rozświetlona/rozmyta. Do negative promptu dodawać: `face, facing camera, front view, detailed face, eye contact`.

**Aniołowie — bez skrzydeł:** postacie aniołów **nie mają skrzydeł** — generator regularnie umieszcza je błędnie z przodu ciała (jak peleryna/aureola na klatce piersiowej), a samo doprecyzowanie anatomii w promptcie tego nie naprawia. Zamiast skrzydeł, atrybutem anioła jest **aureola/nimb** białozłotego światła nad głową lub wokół sylwetki. W promptcie zapisywać to jawnie, np.: `no wings`, `a halo of soft white-gold light above the head` / `radiant nimbus of light around the figure`. Do negative promptu dodawać: `wings, feathered wings, angel wings`. Wielkie skrzydła jako samodzielny motyw krajobrazowy (np. „ogromne skrzydła nad doliną") są nadal dopuszczalne, o ile nie są narysowane jako część konkretnej postaci anioła.

## Spektakularność: każdy kadr

**Wszystkie kadry teledysku są spektakularne** — bogata faktura akwareli, płynące misterne detale, dramatyczna kompozycja, rozmach i wyższy poziom abstrakcji (ogromne skrzydła nad doliną, eksplozje rozkwitającej farby, bramy światła w chmurach). Nie ma podziału na kadry „proste" i „otwierające" — poziom wizualny kadru 1 obowiązuje od pierwszej do ostatniej sekundy. Żeby przy tym bogactwie obraz pozostał czytelny: **jeden wyraźny motyw główny na kadr** — detale budują scenę wokół motywu, ale z nim nie konkurują.

Pierwsze 5 sekund to nadal być albo nie być: kadry 1–2 powinny być najmocniejsze z całej (spektakularnej) serii — to one zatrzymują widza.

**Kompozycja ostatniego kadru (finałowego) pod ekran końcowy:** na ostatnich ~20 sekundach filmu leżą elementy ekranu końcowego (karta z następnym filmem, przycisk subskrypcji). Dlatego ostatni kadr to **w miarę jednolity, spokojny krajobraz lub przestrzeń światła — bez wyrazistego detalu w centrum ekranu**, który odciągałby wzrok od karty do kliknięcia. Główny akcent (jeśli jest) trzymać przy krawędzi kadru, środek i prawa część możliwie czyste.

**Kompozycja kadru-bazy miniatury:** ten etap (Etap 3) decyduje, który kadr będzie bazą miniatury — patrz „Miniatura — wybór kadru" niżej. Ten kadr komponujemy tak, że **główny, najatrakcyjniejszy element wizualny (anioł, aureola, postać, twierdza) znajduje się w górnej połowie kadru**, a **dolna 1/3 kadru jest celowo spokojna** — tylko miękkie plamy mgły, chmur, łąki czy światła, bez kluczowych detali (bo tam leży napis „Psalm X śpiewany" w Etapie 7). W promptcie zapisywać to jawnie, np.: `main subject composed in the upper half of the frame, the lower third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details in the lower part (space reserved for a text overlay)`. Domyślnie to kadr 1 (otwierający), ale jeśli inny kadr niesie mocniejszy/bardziej rozpoznawalny motyw psalmu, skomponować pod miniaturę ten kadr zamiast kadru 1.

## Wierność tekstowi (zasada nadrzędna dla treści kadru)

Każdy kadr ma **dosłownie oddawać to, co mówi dana linijka psalmu** — konkretne przedmioty, istoty i czynności w niej nazwane — a nie luźny symbol zastępczy. Punktem wyjścia dla treści kadru jest zawsze aktualnie śpiewany wers.

- Jeśli wers nazywa konkretną rzecz, ta rzecz **ma być w kadrze**: pióra i skrzydła okrywające (w. 4), tarcza i puklerz (w. 4), strzała lecąca za dnia (w. 5), aniołowie niosący **na rękach** (w. 11–12), stopa i kamień (w. 12), stąpanie po **wężu, żmii, lwie i smoku** (w. 13), twierdza/ucieczka (w. 2, 9).
- Liczby i obrazy z tekstu oddajemy wprost: „tysiąc padnie u boku, dziesięć tysięcy po prawicy" (w. 7) → realnie widoczne mnóstwo padających wokół jednej ocalonej postaci, a nie sama mgła.
- Dopiero gdy wers jest czysto abstrakcyjny („mój Boże, któremu ufam", „ukażę mu moje zbawienie"), sięgamy po obraz symboliczny.

Ta zasada ma **pierwszeństwo przed doborem ładnego motywu** — najpierw sprawdzamy „co dokładnie mówi ten wers", potem budujemy kadr wokół tego. Pozostałe reguły stylu obowiązują nadal i nadają temu formę: jasna anielska paleta, brak zwykłych ludzi (rolę „człowieka" z psalmu pełni anioł lub osłaniany symbol), ukryte twarze, zagrożenia pokonane/rozpływające się w świetle (groźny element może być pokazany dosłownie — wąż, smok, strzała — ale zawsze jako pokonany, nieszkodliwy, ustępujący światłu, nie jako dominanta grozy).

## Rytm skali ujęć

Same szerokie pejzaże nużą. Przeplatać: **szeroki plan** (dolina) → **detal** (piórko, dłoń światła) → **plan średni** (anioł) → znowu szeroko. Zbliżenia po serii planów ogólnych działają jak akcent i resetują uwagę widza. W praktyce: nie więcej niż dwa kadry tej samej skali pod rząd.

## Łuk kolorystyczny

Subtelna podróż temperatury barw przez cały film: **chłodniejszy pastelowy świt na początku → coraz cieplejsze złoto w środku → niemal czysta świetlista biel w finale** („ukażę mu moje zbawienie"). Widz tego nie nazwie, ale poczuje narastanie. W promptach: początek z przewagą light sky blue i ivory, środek z pale gold i warm golden light, finał z radiant white-gold, luminous white.

## Nić przewodnia

Jeden powracający motyw ewoluujący przez cały teledysk — małe złote piórko: pojawia się w intro, przewija przez kolejne sceny (spada, unosi się, prowadzi wzrok), w finale okazuje się częścią wielkich skrzydeł. Widz podświadomie śledzi ten element.

## Tempo montażu (dramaturgia)

Granice kadrów wyznaczamy na bazie dokładnych znaczników czasowych linijek z `txt/napisy.srt` (Etap 2) — nie trzeba już samodzielnie szacować wejść wokalu z surowego audio.

Każdy kadr trwa **od 10 do 20 sekund** — również na początku utworu (zmiany co ~5 s to za dużo; obrazy migają, zamiast wybrzmieć). W praktyce: na początku i w refrenach bliżej dolnej granicy (~10–12 s), w partiach spokojnych i w finale bliżej górnej (~15–20 s), ale **nigdy krócej niż 10 s i nigdy dłużej niż 20 s**.

**Kadry pokrywają CAŁY czas trwania audio — od 0:00 do ostatniej sekundy pliku, bez wyjątków.** Ostatni kadr kończy się dokładnie na końcu audio. Nie stosujemy końcówek „wypełnianych" samym przenikaniem do bieli bez obrazka. Jeśli po ostatniej śpiewanej frazie zostaje długie instrumentalne wyciszenie, planujemy na nie **dodatkowy kadr finałowy** (a przy ogonie dłuższym niż 20 s — kolejne kadry, każdy ≤20 s), tak żeby znaczniki czasowe w nazwach plików obejmowały film od początku do końca. Tempo podąża za wokalem — zmiana kadru na granicy frazy; jeden kadr obejmuje zwykle 2–3 śpiewane linijki, więc jego treść ilustruje najważniejszy obraz z tego fragmentu tekstu. Raz na ~60–90 s jeden „pattern break" — kadr inny niż wszystkie (np. niemal abstrakcyjny wet-on-wet), który budzi uwagę. Orientacyjnie: utwór 3:30 → ~13–17 kadrów, utwór 5:20 → ~20–26 kadrów.

**Wyprzedzenie obrazu względem słów (lead ~1 s):** kadr ma pojawiać się **chwilę przed** momentem w piosence, którego dotyczy — najpierw wchodzi obraz, a dopiero za ~1 sekundę pada śpiewana fraza, którą on ilustruje. Widz zdąży „wejść" w obraz, zanim usłyszy odpowiadające mu słowa. W praktyce znacznik **początku** kadru w nazwie pliku ustawiamy o **około 1 sekundę wcześniej** (0,5–1,5 s, zależnie od tempa) niż dokładny start ilustrowanej frazy wokalu odczytany z `txt/napisy.srt`; kolejny kadr również startuje ~1 s przed swoją frazą. Wyjątek: pierwszy kadr zawsze zaczyna się o 0:00.

## Kompozycja i format

Jeden wyraźny motyw główny na kadr, wokół niego bogata, spektakularna faktura akwareli i płynące detale. Farba wypełnia całe płótno od krawędzi do krawędzi — żadnych białych marginesów papieru (fraza „lots of white space" zakazana; pusta przestrzeń to jednolita malowana plama). Format 16:9 — rozdzielczość: patrz `## Rozdzielczość docelowa` wyżej.

## Kanoniczny blok stylu (początek każdego promptu)

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. [OPIS SCENY] dreamy soft focus. 16:9 cinematic composition.
```

Paletę w bloku modyfikować zgodnie z łukiem kolorystycznym (początek: więcej light sky blue i ivory; środek: pale gold, warm golden light; finał: radiant white-gold, luminous white).

## Stały negative prompt

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, face, facing camera, front view, detailed face, eye contact, wings attached to chest, wings growing from front of body
```

## Produkcja obrazów

Ten plik dostarcza tylko treść promptów (styl, blok kanoniczny, negative prompt). Samo generowanie plików obrazków z tych promptów przez Leonardo AI (API, tryb, rozdzielczość, koszt) to osobny etap: patrz Etap 4 w `styl-teledysku.md` (`etap4-generowanie-obrazkow.md`).

## Miniatura — wybór kadru (decyzja podejmowana na tym etapie)

**Wybór kadru na miniaturę jest decyzją Etapu 3, nie Etapu 6 ani 7.** Podczas rozpisywania kadrów (Fable) wybrać jeden — najmocniejszy wizualnie, najlepiej z aniołem/aureolą lub innym rozpoznawalnym motywem psalmu, czytelny w małym rozmiarze — i skomponować go pod miniaturę wg zasady wyżej („Kompozycja kadru-bazy miniatury"). Domyślny kandydat to kadr 1 (otwierający), ale wybrać inny, jeśli lepiej oddaje główny motyw/tytułowy hak psalmu.

Decyzję zapisać **jawnie i jednoznacznie w `prompty.md`**: w nagłówku wybranego kadru dopisać adnotację „**baza miniatury**" (obok istniejących adnotacji skali/nici przewodniej) oraz dodać na końcu pliku (albo w podsumowaniu łuku na górze) osobną linię, np. „**Kadr na miniaturę: Kadr N** — [jednozdaniowe uzasadnienie]". To jedyne miejsce, z którego Etap 7 czerpie informację, który kadr użyć — Etap 7 nie pyta użytkownika i nie czeka na rekomendację z Etapu 6. Pełne zasady miniatury (napisy, panel, czcionka, nazewnictwo plików): patrz Etap 7 w `styl-teledysku.md`.
