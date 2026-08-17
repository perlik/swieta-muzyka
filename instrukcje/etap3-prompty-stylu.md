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

W teledysku nie występują zwykłe postacie ludzkie **ani aniołowie — postaci anioła nie używamy w ogóle, w żadnym kadrze** (decyzja użytkownika z 2026-07 przy Psalmie 19; wcześniejsza zasada „anioł bez skrzydeł, z aureolą" jest wycofana razem z aniołami). Około **70% kadrów** zawiera motyw duchowy: symbolikę Bożą — wielkie skrzydła nad krajobrazem (jako oddzielny, bezosobowy motyw krajobrazowy, nie atrybut żadnej postaci), snop światła z nieba, dłoń światła, gołębica, baranek, korona z promieni, otwarta brama światła — oraz ewentualnie postać Jezusa (w prostej jasnej szacie, malowaną miękko i z szacunkiem). Pozostałe **~30%** to czyste pejzaże: łąki, doliny, świt, sad, droga wśród wzgórz — oddech, głównie w partiach instrumentalnych.

Opieka, która w tekście dotyczy człowieka, wyrażana jest przez symbole (namiot pod kopułą światła, ptak pod skrzydłem, droga wyścielona światłem). Jeśli w kadrze pojawia się postać Jezusa, zasady anatomii obowiązują: wyraźne rozdzielenie sylwetek przy kilku postaciach i jawny zapis poprawnej anatomii w promptcie.

**Limit baranków i owieczek: maksymalnie 25% kadrów danego filmu.** Baranek/owca może grać duszę chronioną, ale nie w co drugim kadrze — w pozostałych scenach rolę „ja" psalmu pełnią zamiennie: biały gołąb lub inny ptak, sam symbol chroniony (namiot, dom, lampa, serce, korona), albo perspektywa pierwszoosobowa (widz patrzy „oczami" psalmisty — np. dłonie światła wyciągnięte KU kamerze, droga rozpościerająca się przed widzem). Przy rozpisywaniu kadrów policzyć: liczba kadrów z barankiem/owcami ≤ 25% wszystkich kadrów filmu.

**Wyjątek:** jeśli sam tekst psalmu jest mocno pasterski — dosłownie mówi o pasterzu, owcach, stadzie, pastwiskach (np. Psalm 23, Psalm 100) — limit nie obowiązuje sztywno i baranków/owiec może być więcej niż 25%, bo wymaga tego zasada wierności tekstowi. W pozostałych psalmach limit stosujemy bez wyjątków.

**Psalmistka — wyjątek od zakazu widocznych twarzy (decyzja użytkownika, 2026-07, Psalm 46):** obok Jezusa (twarz zawsze ukryta) dopuszczalna jest kobieca postać psalmistki (śpiewaczki) — jedyna postać w serii, której twarz **może być widoczna, włącznie z kontaktem wzrokowym wprost w kamerę**. Nie jest to „zwykła postać ludzka/tłum" objęta ogólnym zakazem — to symboliczna reprezentacja głosu/„ja" psalmu.

**Obowiązkowy kadr psalmistki w każdym filmie (decyzja użytkownika, 2026-07, Psalm 46; doprecyzowanie 2026-08-04, Psalm 22):** w każdym filmie umieszczać **dokładnie jeden kadr** z psalmistką, malowany miękko w tej samej akwarelowej, świetlistej stylistyce co reszta kadrów. Reszta kadrów filmu nadal trzyma się zakazu twarzy i zakazu aniołów bez wyjątku.

**Kadr psalmistki jest ZAWSZE kadrem 1 — otwierającym, od 0:00 (decyzja użytkownika 2026-08-04).** Nie szukamy już dla niego „najlepiej pasującego wersu w pierwszej osobie" — pozycja jest stała i nie podlega ocenie przy rozpisywaniu kadrów. Wcześniejsza praktyka (Psalm 46: kadr 14, Psalm 22: kadr 21) jest wycofana; starych plików `prompty.md` nie poprawiamy wstecz. **Kadr 1 jest tym samym zawsze bazą miniatury** — patrz „Miniatura — wybór kadru" niżej.

### Wygląd psalmistki — obowiązkowa specyfikacja

Kompozycja i poza:

- duże zbliżenie na twarz, ale **twarz po PRAWEJ stronie kadru** (wypełnia prawą połowę kompozycji), lewa strona otwarta na płynące plamy ciepłego światła i bladego nieba. Prawa strona jest wymuszona przez miniaturę: skrypt `generuj_miniature.py` kładzie panel z napisem **na dole po lewej**, więc twarz po prawej i spokojny lewy dół to jedyny układ, w którym napis nie zasłania twarzy;
- **prawą stronę zapisywać dwustronnie** (poprawka 2026-08-09, Psalm 119): powiedzieć nie tylko, gdzie postać jest, ale też że po lewej **nikogo nie ma** — `with her whole head and shoulders contained within the right half of the composition` + `the entire left half of the frame opens into ... with no figure in it`. Samo `her face filling the right half` zostawia generatorowi furtkę: twarz idzie w prawo, a korpus i tak wjeżdża na środek. Wykluczenie postaci z lewej połowy działa na te modele mocniej niż samo wskazanie prawej;
- **pozycję podawać też NA POCZĄTKU opisu sceny** (poprawka 2026-08-14, Psalm 131): opis sceny otwierać od `On the right side of the frame, a large close-up...` z dopiskiem `her whole figure kept entirely within the right half of the composition`, zanim padną jakiekolwiek detale twarzy — generator waży początek promptu mocniej niż środek, więc umiejscowienie wymienione dopiero w połowie bloku bywa ignorowane i psalmistka ląduje na środku lub po lewej. Frazy dwustronne z punktu wyżej zostają dodatkowo w środku bloku. Kanoniczny prompt niżej ma to już wpisane;
- głowa w łagodnym obrocie 3/4 (widać przód i bok twarzy);
- **oczy szeroko otwarte i wyraźnie widoczne, wzrok wprost w kamerę** (bezpośredni kontakt wzrokowy z widzem) mimo obróconej głowy — to najczęstszy błąd generatora, który przy „dreamy soft focus" domyka powieki, dlatego zapisujemy to jawnie i wzmacniamy negative promptem;
- **długie jasne blond włosy** (decyzja użytkownika 2026-08-09, Psalm 119), powiewające jakby na wietrze, naturalne i nieukładane. Kolor zapisywać **w odniesieniu do aureoli**: `fair wheat blonde and clearly lighter and paler than the golden halo behind her`. Bez tego zastrzeżenia blond i złota aureola zlewają się w jedną świecącą plamę i włosy przestają być czytelne. W negative prompcie blokować pozostałe kolory (`dark hair, black hair, brown hair, brunette, auburn hair, red hair, ginger hair, grey hair, dyed hair`);
- miękka aureola z czystego złotego światła za głową, **bez skrzydeł**.

**Czego NIE wpisywać w negative prompt: negatywów przestrzennych** (`subject on the left`, `centered subject` itp.). Na Phoenixie działają nieprzewidywalnie — model łapie samo słowo „left" i zaczyna unikać lewej strony w ogóle, czyli czyści także spokojny lewy dół zarezerwowany pod panel miniatury. Kompozycję trzyma wyłącznie prompt pozytywny.

Charakter postaci — **młoda, niewinna kobieta „z oazy", nie modelka** (decyzja użytkownika 2026-08-04, Psalm 22; wcześniejsze prompty wychodziły zbyt zmysłowo, a próba korekty przez „teenage girl" dała z kolei dziecko):

- **kobieta w wieku około 20 lat** — dorosła, ale młoda; **nie dziecko, nie nastolatka** i nie dojrzała kobieta;
- **sama liczba lat w promptcie nie wystarcza** (sprawdzone przy Psalmie 22: `about 20 years old` dało twarz ok. 15-letnią). Wiek niosą **proporcje twarzy**, więc opisywać je wprost: pociągła owalna twarz, zarysowane kości policzkowe, wyraźna smukła linia żuchwy, oczy w normalnej dorosłej proporcji do twarzy, szyja dorosłej kobiety. W negative prompcie wykluczać to, co czyta się jako dziecko: okrągła buzia, pucołowate policzki, piegi, wielkie „sarnie" oczy, drobne rysy;
- wyraz **spokojny i pogodny** — bardziej opanowany niż nieśmiały. „Shy", „childlike", „trusting" ciągną generator w stronę nastolatki, więc w promptcie lepiej pracuje `calm serene composed`;
- **bez makijażu**, bez wyretuszowanej urody, bez stylizacji;
- **usta spokojnie i całkowicie zamknięte**, ewentualnie nieśmiały delikatny uśmiech — **nigdy lekko rozchylone wargi**, bo to natychmiast przestawia generator na estetykę beauty/glamour;
- skromny strój z **wysokim, zabudowanym dekoltem** zakrywającym ramiona;
- zero zmysłowości, zero glamouru, zero pozy.

Negative prompt w tym jednym kadrze różni się od stałego: **pomijamy** pozycje `face, facing camera, front view, detailed face, eye contact` oraz `angel, angelic figure, choir of angels`, a dopisujemy wykluczenia lecące w obie strony naraz — i przeciw glamourowi, i przeciw zdziecinnieniu, plus blokadę koloru włosów.

**W `prompty.md` zapisywać ten negative prompt zawsze jako jeden gotowy do skopiowania blok** (poprawka 2026-08-09, Psalm 119), nigdy jako instrukcję „weź stały, usuń pięć pozycji, dopisz resztę". Powód jest praktyczny: przy generowaniu w Etapie 4 składanie tego z dwóch kawałków kończy się wklejeniem pełnego stałego negative promptu razem z dopiskami, a wtedy wracają usunięte `face, facing camera, front view, detailed face, eye contact` i kasują dokładnie to, na czym w tym kadrze zależy — twarz i kontakt wzrokowy. Nad blokiem umieszczać ostrzeżenie, żeby go **nie łączyć** ze stałym negative promptem.

Gotowy blok (kompletny — to jest całość, którą się wkleja):

```
ordinary people, crowd, modern clothing, dark, gloomy, black, deep navy, heavy shadows, ominous mood, white paper border, unpainted edges, photorealistic, 3D render, text, watermark, three arms, extra limbs, deformed hands, fused bodies, merged figures, distorted face, wings attached to chest, wings growing from front of body, closed eyes, eyes shut, half-closed eyes, downcast eyes, looking away, gaze averted, blindfold, sexy, sensual, seductive, sultry, alluring, glamour, fashion model, beauty photography, makeup, lipstick, glossy lips, parted lips, open mouth, pouting, bare shoulders, cleavage, low neckline, tight clothing, provocative pose, child, little girl, kid, teenager, adolescent, schoolgirl, childlike face, round baby face, chubby cheeks, puffy cheeks, freckles, small childlike features, oversized doe eyes, mature woman, middle-aged, elderly, dark hair, black hair, brown hair, brunette, auburn hair, red hair, ginger hair, grey hair, dyed hair
```

Jeśli stały negative prompt kiedykolwiek się zmieni, ten blok trzeba przeliczyć ręcznie — jest kopią, nie odwołaniem.

### Kanoniczny prompt psalmistki (kadr 1) — punkt wyjścia dla każdego filmu

Skopiować i podmienić wyłącznie **[FRAZA Z PSALMU]** na jednozdaniowy sens otwierającego wersu danego psalmu oraz paletę na początkową (chłodniejszą) zgodnie z łukiem kolorystycznym:

```
Breathtaking watercolor painting, rich watercolor textures, intricate flowing details, dramatic composition, airy pastel palette of ivory white, pale gold, light sky blue and gentle rose, radiant heavenly light, full bleed with paint covering the entire canvas edge to edge, no white paper borders. On the right side of the frame, a large close-up of the face of a young woman, the psalmist, her whole figure kept entirely within the right half of the composition, a woman of about 20 to 22 years old, clearly a grown adult woman and not a teenager, with fully adult facial proportions - a longer oval face, defined cheekbones, a slender defined jawline and eyes of normal adult proportion to the face, a plain modest devout young woman, wholesome and innocent, no makeup at all, her lips calmly and completely closed, her expression calm serene and composed, positioned clearly in the right side of the frame with her whole head and shoulders contained within the right half of the composition, her face filling the right half while the entire left half of the frame opens into flowing washes of soft light and pale sky with no figure in it, her head turned in a gentle three-quarter angle so both the front and the side of her face are visible, her long soft light golden blonde hair, fair wheat blonde and clearly lighter and paler than the golden halo behind her, simple and untouched, drifting sideways as if caught by a soft wind, a soft radiant halo of pure golden light glowing behind her head like a ring of pale fire, no wings anywhere on her body, wearing a simple modest plain dress with a high closed neckline covering her shoulders, her eyes wide open and clearly visible, looking straight into the camera in direct eye contact with the viewer despite the angled pose, a calm composed prayerful gaze, her serene adult face softly painted in luminous watercolor, [FRAZA Z PSALMU], entirely innocent and prayerful, nothing sensual or glamorous, main subject composed in the upper half of the frame, the lower left third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details there (space reserved for a text overlay), dreamy soft focus. 16:9 cinematic composition.
```

Regulacja, gdy wynik ucieka w bok — **wiek zmieniamy tylko przez liczbę, nie przez rzeczowniki** („girl", „teenage" zawsze zjeżdżają w dziecko, „woman" bez liczby zjeżdża w dojrzałą kobietę):

- **za dorośle / za zmysłowo:** wzmocnić blok antyglamourowy (`no makeup`, `lips completely closed`, `nothing sensual or glamorous`) i zejść ze skali z „large close-up" na plan popiersia — twarz w mniejszej skali słabiej ciągnie model w stronę portretu beauty; wieku nie obniżać poniżej 20;
- **za dziecinnie (najczęstszy problem):** liczby lat nie podbijać w nieskończoność — zamiast tego dołożyć opis **proporcji dorosłej twarzy** (`longer oval face, defined cheekbones, slender defined jawline, eyes of normal adult proportion to the face, adult woman's neck`), zamienić `shy / childlike / trusting` na `calm serene composed`, i sprawdzić, czy w negative prompcie są `child, teenager, adolescent, schoolgirl, round baby face, chubby cheeks, freckles, oversized doe eyes, small childlike features`. Dopiero gdy to nie wystarczy, podnieść wiek do `about 25 years old` — model zwykle rysuje o kilka lat mniej, niż się napisze.

**Twarze — zasada kluczowa (dla wszystkich pozostałych postaci):** AI często generuje zniekształcone, dziwnie wyglądające twarze. Dlatego **twarze postaci (np. Jezusa) nie powinny być widoczne**. Postacie pokazujemy **od tyłu, z boku, z opuszczoną/odwróconą głową, z twarzą skrytą w świetle lub poza kadrem** (np. kadr obcięty poniżej ramion, sylwetka pod światło / kontra). W promptcie zapisywać to jawnie, np.: `seen from behind`, `face turned away`, `head bowed`, `face hidden in light`, `back view`, `profile silhouette`, `figure cropped below the shoulders`. Wyjątek dopuszczalny tylko wtedy, gdy twarz jest daleko i bardzo mała lub całkowicie rozświetlona/rozmyta. Do negative promptu dodawać: `face, facing camera, front view, detailed face, eye contact`.

**Aniołowie — całkowity zakaz (aktualizacja 2026-07):** postaci aniołów **nie generujemy w ogóle** — w promptach nie używamy fraz typu `angel`, `angelic figure`, `choir of angels`. Wcześniejsza zasada „anioł bez skrzydeł, z aureolą" jest wycofana razem z samymi aniołami. Wielkie skrzydła jako samodzielny motyw krajobrazowy (np. „ogromne skrzydła światła nad doliną") pozostają dopuszczalne, o ile nie są narysowane jako część żadnej postaci. Wykluczenia `wings, feathered wings, angel wings` oraz `wings attached to chest, wings growing from front of body` zostają w stałym negative prompcie.

## Spektakularność: każdy kadr

**Wszystkie kadry teledysku są spektakularne** — bogata faktura akwareli, płynące misterne detale, dramatyczna kompozycja, rozmach i wyższy poziom abstrakcji (ogromne skrzydła nad doliną, eksplozje rozkwitającej farby, bramy światła w chmurach). Nie ma podziału na kadry „proste" i „otwierające" — poziom wizualny kadru 1 obowiązuje od pierwszej do ostatniej sekundy. Żeby przy tym bogactwie obraz pozostał czytelny: **jeden wyraźny motyw główny na kadr** — detale budują scenę wokół motywu, ale z nim nie konkurują.

Pierwsze 5 sekund to nadal być albo nie być: kadry 1–2 powinny być najmocniejsze z całej (spektakularnej) serii — to one zatrzymują widza. Kadr 1 jest z definicji kadrem psalmistki (patrz wyżej), więc „najmocniejszy" znaczy tu: najlepiej namalowany portret, z pełnym rozmachem światła i faktury akwareli wokół twarzy — a nie inny motyw. Ciężar spektakularnego pejzażu/symbolu przejmuje kadr 2.

**Kompozycja ostatniego kadru (finałowego) pod ekran końcowy:** na ostatnich ~20 sekundach filmu leżą elementy ekranu końcowego (karta z następnym filmem, przycisk subskrypcji). Dlatego ostatni kadr to **w miarę jednolity, spokojny krajobraz lub przestrzeń światła — bez wyrazistego detalu w centrum ekranu**, który odciągałby wzrok od karty do kliknięcia. Główny akcent (jeśli jest) trzymać przy krawędzi kadru, środek i prawa część możliwie czyste.

**Kompozycja kadru-bazy miniatury:** bazą miniatury jest **zawsze kadr 1, czyli kadr psalmistki** (patrz „Postacie" wyżej i „Miniatura — wybór kadru" niżej) — nie ma tu już wyboru między kadrami. Ten kadr komponujemy tak, że **twarz psalmistki znajduje się po prawej stronie i w górnej połowie kadru**, a **dolna lewa część kadru jest celowo spokojna** — tylko miękkie plamy mgły, chmur i światła, bez kluczowych detali (bo tam skrypt Etapu 7 kładzie panel z napisem „Psalm X śpiewany"). W promptcie zapisywać to jawnie, np.: `main subject composed in the upper half of the frame, the lower left third of the frame intentionally calm and simple - only soft washes of mist, clouds and light, no important details there (space reserved for a text overlay)`.

## Wierność tekstowi (zasada nadrzędna dla treści kadru)

Każdy kadr ma **dosłownie oddawać to, co mówi dana linijka psalmu** — konkretne przedmioty, istoty i czynności w niej nazwane — a nie luźny symbol zastępczy. Punktem wyjścia dla treści kadru jest zawsze aktualnie śpiewany wers.

- Jeśli wers nazywa konkretną rzecz, ta rzecz **ma być w kadrze**: pióra i skrzydła okrywające (w. 4), tarcza i puklerz (w. 4), strzała lecąca za dnia (w. 5), aniołowie niosący **na rękach** (w. 11–12), stopa i kamień (w. 12), stąpanie po **wężu, żmii, lwie i smoku** (w. 13), twierdza/ucieczka (w. 2, 9).
- Liczby i obrazy z tekstu oddajemy wprost: „tysiąc padnie u boku, dziesięć tysięcy po prawicy" (w. 7) → realnie widoczne mnóstwo padających wokół jednej ocalonej postaci, a nie sama mgła.
- Dopiero gdy wers jest czysto abstrakcyjny („mój Boże, któremu ufam", „ukażę mu moje zbawienie"), sięgamy po obraz symboliczny.

Ta zasada ma **pierwszeństwo przed doborem ładnego motywu** — najpierw sprawdzamy „co dokładnie mówi ten wers", potem budujemy kadr wokół tego. Pozostałe reguły stylu obowiązują nadal i nadają temu formę: jasna świetlista paleta, brak zwykłych ludzi i aniołów (rolę „człowieka" z psalmu pełni osłaniany symbol albo perspektywa pierwszoosobowa), ukryte twarze, zagrożenia pokonane/rozpływające się w świetle (groźny element może być pokazany dosłownie — wąż, smok, strzała — ale zawsze jako pokonany, nieszkodliwy, ustępujący światłu, nie jako dominanta grozy).

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

**Kadr psalmistki ma własny, osobny negative prompt** — nie ten. Gotowy do skopiowania blok stoi w § „Wygląd psalmistki". Tamten jest kompletny sam w sobie; sklejenie go z powyższym psuje kadr.

Zmiana czegokolwiek w bloku powyżej wymaga ręcznego przeliczenia bloku psalmistki — to kopia z pominięciami, nie odwołanie.

## Produkcja obrazów

Ten plik dostarcza tylko treść promptów (styl, blok kanoniczny, negative prompt). Samo generowanie plików obrazków z tych promptów przez Leonardo AI (API, tryb, rozdzielczość, koszt) to osobny etap: patrz Etap 4 w `styl-teledysku.md` (`etap4-generowanie-obrazkow.md`).

## Miniatura — wybór kadru (decyzja podejmowana na tym etapie)

**Bazą miniatury jest zawsze kadr 1, czyli kadr psalmistki** (decyzja użytkownika 2026-08-04). Nie ma tu wyboru ani oceny „który kadr jest najmocniejszy" — twarz psalmistki jest stałym elementem miniatur całej serii, co daje kanałowi rozpoznawalny, powtarzalny wygląd w browse. Kadr 1 komponujemy pod miniaturę wg zasady wyżej („Kompozycja kadru-bazy miniatury"): twarz po prawej i w górnej połowie, dolna lewa część spokojna.

Mimo że wybór jest stały, zapisać go **jawnie w `prompty.md`** (Etap 7 czyta tylko ten plik): w nagłówku kadru 1 dopisać adnotację „**baza miniatury**" (obok adnotacji skali/nici przewodniej) oraz dodać na końcu pliku (albo w podsumowaniu łuku na górze) osobną linię „**Kadr na miniaturę: Kadr 1 (psalmistka)**". Etap 7 nie pyta użytkownika i nie czeka na rekomendację z Etapu 6. Pełne zasady miniatury (napisy, panel, czcionka, nazewnictwo plików): patrz Etap 7 w `styl-teledysku.md`.

**Wyjątek dla starszych filmów:** `prompty.md` powstałe przed 2026-08-04 mają psalmistkę w innym kadrze i bazę miniatury wskazaną gdzie indziej — tych plików nie poprawiamy wstecz, Etap 7 wykonuje dla nich to, co jest w ich `prompty.md`.
