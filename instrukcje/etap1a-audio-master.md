# Etap 1A — Master audio (EQ + de-esser + normalizacja)

Surowy plik z Suno brzmi mulisto w dole, ma wystrzelone sybilanty i zerowy zapas
na szczytach. Ten etap przerabia go na plik, który idzie na oś czasu w DaVinci
Resolve. EQ jest **wpieczony w plik**, a nie ustawiony w Resolve — dzięki temu
brzmienie jest powtarzalne między psalmami i nie zależy od tego, co akurat
zostało wyklikane w projekcie.

**Kiedy:** zaraz po tym, jak audio z Suno trafi do `audio/`, czyli między Etapem 1
(lyrics) a Etapem 2 (napisy).

**Model Claude: Haiku, effort low** — całą robotę wykonuje skrypt. Jedyna decyzja
należy do użytkownika i jest odsłuchowa: czy sybilanty są już dość ściszone.

**Wejście:** `audio/audio.wav` (pełny miks z Suno)
**Wyjście:** `audio/audio_eq_v3.wav` (48 kHz / 24 bit, −14 LUFS, true peak −1.0 dBFS)

## Jak uruchomić — to wystarczy

```bash
python3 instrukcje/skrypty/master_audio.py "psalm N - in progress - X" --wyjscie audio_eq_v3.wav
```

**Profil `v3` jest domyślny od 2026-08-09** (zatwierdzony odsłuchowo na Psalmie 119),
więc nie trzeba go podawać. Jedyne, co dopisujemy, to nazwa pliku wyjściowego —
skrypt domyślnie zapisuje do `audio_eq_v2.wav`, a nowe psalmy mają lądować w
`audio_eq_v3.wav`, żeby po nazwie było widać, którym łańcuchem plik powstał.

Nic nie trzeba dostrajać ręcznie. Skrypt sam mierzy głośność wejścia i wyrównuje
ją do wewnętrznego poziomu odniesienia, więc te same ustawienia dają ten sam
efekt niezależnie od tego, jak głośno przyszło z Suno.

**Kontrola po wykonaniu — trzy liczby, które skrypt wypisuje na końcu:**

1. głośność wyjścia ma być **−14.0 LUFS** (±0.1),
2. true peak ma być **około −1.0 dBFS** (dopuszczalne −1.0 do −1.5),
3. długość pliku ma być identyczna z `audio.wav` — sprawdzić, jeśli napisy
   już istnieją:
   ```bash
   ffprobe -v error -select_streams a:0 -show_entries stream=duration_ts \
     -of csv=p=0 "psalm N - .../audio/audio.wav"
   ```
   ta sama liczba próbek dla obu plików oznacza, że `napisy.srt` i oś czasu
   z Etapu 8 pasują bez przesuwania czegokolwiek.

Potem zostaje **odsłuch** — to jedyna decyzja, której skrypt nie podejmie:
czy sybilanty („ś", „sz", „cz") są dość ściszone. Najlepiej na telefonie, bo tam
publiczność kanału ogląda i tam ta różnica jest największa. Jeśli syczy za mocno,
powtórzyć z `--deess mocniej`; jeśli wokal stracił artykulację — `--deess delikatnie`.

Opcje:

| Flaga | Do czego |
|---|---|
| `--wyjscie NAZWA` | nazwa pliku wynikowego — **dla nowych psalmów zawsze `audio_eq_v3.wav`** |
| `--deess delikatnie` | sybilanty ledwo przeszkadzają (ratio 3:1) |
| `--deess standard` | **domyślne** (ratio 4:1) |
| `--deess mocniej` | wokalistka mocno sepleni na „ś"/„sz" (ratio 5:1) |
| `--profil v3` | **domyślne** — nie trzeba podawać |
| `--profil v2` | stary łańcuch z Psalma 8; **do nowych psalmów nie używać**, zostaje tylko po to, żeby dało się odtworzyć brzmienie filmów zrobionych przed 2026-08-09 |

Progi de-essera zależą od profilu — v2 pracuje na −20/−22/−24 dB, v3 na
−27/−30/−33 dB. To nie jest „mocniejszy de-esser", tylko inny punkt odniesienia:
v3 kompresuje wyłącznie pasmo 3–9 kHz, którego poziom jest z natury niższy niż
całej góry razem wziętej.

Skrypt **nie nadpisuje** istniejącego pliku wynikowego — przy powtórce trzeba
skasować poprzedni albo podać inną nazwę przez `--wyjscie`.

**Po podmianie w Resolve wyłączyć Equalizer na ścieżce Audio 1** — EQ jest już
wpieczony w plik, zostawiony włączony zadziała drugi raz.

## Profil v3 — co i dlaczego zmienione

Psalm 1 po uploadzie brzmiał nieprzyjemnie „do przodu" — wokal aż za wyraźny.
Pomiary pokazały, że winna jest nie głośność (−13.9 LUFS, czyli dokładnie tam,
gdzie YouTube i tak wszystko sprowadza), tylko **barwa masteru**.

**Zarzut 1: łańcuch dokładał krzykliwości.** Wszystko poniżej 2 kHz było ścinane,
a pasmo obecności podbijane. Netto master wychodził ~3 dB bardziej „do przodu"
niż plik, który przyszedł z Suno:

| Balans względem pasma obecności 2–6 kHz | dół 60–300 Hz | środek 300 Hz–2 kHz | góra 6–16 kHz |
|---|---|---|---|
| surowy z Suno (Psalm 1) | +10.8 | +9.7 | −4.0 |
| master v2 | +8.2 | +7.9 | −5.5 |
| master v3 | +11.2 | +10.6 | −3.8 |

**Zarzut 2: de-esser praktycznie nie działał.** Próg 0.079 to −22.0 dBFS, a szczyt
RMS pasma >3.5 kHz w tym materiale wynosi **−22.9 dBFS** — próg leżał *powyżej*
najgłośniejszego momentu pasma, więc kompresor łapał tylko pojedyncze szczyty
próbkowe. Zmierzony efekt: 1.5 dB redukcji, przy czym bell +2.5 dB na 3 kHz
dokładał z powrotem 1.9 dB. **Sybilanty w masterze v2 były głośniejsze
bezwzględnie niż w surowym pliku** (szczyt p99 w 3–5 kHz: 44.9 → 45.1).

### Co się zmieniło w v3

| Element | v2 | v3 | Po co |
|---|---|---|---|
| HPF | 65 Hz | **55 Hz** | 65 Hz zabierało ciało fortepianu |
| Low shelf 41 Hz | −4 dB | **−2 dB** | HPF i tak zdejmuje sam dół, razem robiły −7 dB |
| Bell 300 Hz | −2.5 dB | **−1.5 dB** | mniej odchudzania środka |
| Obecność | 3 kHz +2.5 dB, Q 1.0 | **2 kHz +1.5 dB, Q 1.2** | 3 kHz to maksimum polskiego „sz" — boost tam sam produkował problem, który gasił de-esser |
| High shelf 11.5 kHz | +2.5 dB | **+1.5 dB** | powietrze bez ostrości |
| De-esser | 2 pasma, split 3.5 kHz | **3 pasma, split 3000\|9000** | kompresja tylko pasma sybilantów; góra >9 kHz nietknięta (v2 zjadał shelf, który EQ chwilę wcześniej dodał) |
| Próg (standard) | 0.079 (−22 dB) | **0.032 (−30 dB)** | próg musi leżeć między RMS pasma (≈−37 dBFS) a jego szczytem (≈−22 dBFS) |
| Makeup | 1 | brak | nie ma czego nadrabiać, gdy kompresja jest łagodna |

Głośność wyjściowa się nie zmienia — v3 trafia w te same −14 LUFS / −1 dBFS TP.
Zmienia się wyłącznie barwa.

### Wynik na Psalmie 119

| | surowy | v2 | v3 |
|---|---|---|---|
| Głośność | −13.5 LUFS | −14.0 LUFS | −14.0 LUFS |
| True peak | −1.2 dBFS | −1.1 dBFS | −1.3 dBFS |
| LRA | 6.2 LU | 7.4 LU | 6.9 LU |
| Dół do obecności | +7.2 dB | +4.1 dB | **+7.1 dB** |
| Środek do obecności | +7.6 dB | +5.9 dB | **+8.5 dB** |
| Sybilanty 3–5 kHz (szczyt p99) | 42.5 | 43.6 | **39.6** |
| Sybilanty 5–9 kHz (szczyt p99) | 41.6 | 39.4 | **38.0** |

Długość w próbkach identyczna (19 358 640 @ 48 kHz), więc `napisy.srt` i oś czasu
z Etapu 8 pasują bez ruszania czegokolwiek.

## Co robi łańcuch i dlaczego

### 1. Wyrównanie poziomu wejścia do −16.5 LUFS

Próg de-essera jest **bezwzględny**, więc materiał wchodzący głośniej byłby
de-essowany mocniej, a cichszy prawie wcale. Bez tego kroku to samo ustawienie
dałoby inny efekt na każdym psalmie. −16.5 LUFS to poziom, na którym wylądował
Psalm 8 (−13.5 LUFS z Suno minus 3 dB zapasu) i na którym ustawienia zatwierdzono.

### 2. EQ

| Pasmo | Ustawienie | Po co |
|---|---|---|
| HPF | 65 Hz, 12 dB/okt | rumot i podmuchy, bez zabierania ciała fortepianu |
| Low shelf | 41 Hz, **−4 dB** | porządkuje sam dół; mocniej (np. −20 dB) odchudza cały miks |
| Bell | 300 Hz, **−2.5 dB**, Q 1.2 | ubytek mułu — to on odsłania wokal, nie żaden boost |
| Bell | 3 kHz, **+2.5 dB**, Q 1.0 | obecność, zrozumiałość spółgłosek |
| High shelf | 11.5 kHz, **+2.5 dB** | powietrze (nie 15 kHz — tam w materiale z Suno są głównie artefakty kodeka) |
| LPF | 19 kHz | odcięcie śmieci nad pasmem słyszalnym |

### 3. De-esser

Polskie sybilanty rozkładają się szeroko: „sz"/„cz"/„ż" mają maksimum w **3–5 kHz**,
„ś"/„s" wyżej, w **4–9 kHz**. Statyczny ubytek w jednym miejscu nie załatwia obu,
a przy okazji przygłusza wokal na stałe. Dlatego działa tu kompresja pasmowa:
crossover 3.5 kHz (`acrossover`), kompresor tylko na górnym paśmie (ratio 4:1,
atak 1 ms, release 40 ms), potem oba pasma z powrotem razem. Kompresor rusza
wyłącznie na wystrzale sybilanta — reszta materiału przechodzi nietknięta.

Pasmo >3.5 kHz ma szczyty ok. 25–28 dB nad swoim RMS, i to właśnie te szczyty
łapie próg.

### 4. Normalizacja

Dwuprzebiegowy `loudnorm` na **−14 LUFS / true peak −1.0 dBFS**. −14 LUFS to
próg, do którego YouTube i tak wszystko sprowadza, więc wypuszczanie głośniejszego
materiału nie daje nic poza utratą dynamiki. Jednoprzebiegowy loudnorm trafia
w cel niedokładnie, stąd dwa przebiegi.

## Wynik na Psalmie 8 (punkt odniesienia)

| | oryginał | po masteringu |
|---|---|---|
| Głośność | −13.5 LUFS | −14.0 LUFS |
| True peak | 0.0 dBFS (zero zapasu) | −1.0 dBFS |
| 3–5 kHz („sz") RMS | −37.4 dB | −36.0 dB |
| 5–9 kHz („ś") RMS | −37.5 dB | −37.7 dB |

Długość pliku jest identyczna co do próbki, więc `napisy.srt` i oś czasu z Etapu 8
pasują bez przesuwania czegokolwiek.

## Po podmianie w Resolve

**Wyłączyć Equalizer na ścieżce Audio 1.** EQ jest już w pliku — zostawiony
włączony zadziała drugi raz.

Etap 2 (napisy) dalej pracuje na `audio.wav`, nie na pliku po masteringu.
Znaczniki czasu są identyczne, więc kolejność tych dwóch etapów nie ma znaczenia.

---

## Co można zrobić lepiej — do sprawdzenia przy kolejnym psalmie

Poniższe nie zostało zastosowane na Psalmie 8. Warto przetestować i, jeśli wyjdzie
lepiej, przenieść do domyślnych ustawień wyżej.

**Punkty 1 i 2 są już zrobione — weszły do profilu `v3`** (patrz sekcja „Profil v3"
wyżej). Zostają tu jako zapis uzasadnienia. Do sprawdzenia zostają punkty 3–5.

### 1. Ograniczyć de-esser do pasma 3–9 kHz zamiast całej góry  ✅ w v3

Obecnie crossover na 3.5 kHz oddaje kompresorowi **wszystko** powyżej — łącznie
z shelfem powietrza z 11.5 kHz. Przy mocniejszym de-essingu to się mści: w testach
na Psalmie 8 pasmo 5–9 kHz spadło wtedy ~6 dB **pod** poziom oryginału, czyli
de-esser zjadł powietrze, które EQ chwilę wcześniej dodało.

Lepsza konstrukcja to trzy pasma i kompresja wyłącznie środkowego:

```
acrossover=split=3000|9000:order=4th[lo][mid][hi];
[mid]acompressor=threshold=0.079:ratio=4:attack=1:release=45:knee=4:detection=peak[midd];
[lo][midd][hi]amix=inputs=3:duration=longest:normalize=0
```

Crossover przesunięty na 3000 Hz łapie też dolną krawędź „sz", która przy 3.5 kHz
zostawała bez ochrony, a góra powyżej 9 kHz zostaje nietknięta.

### 2. Przenieść obecność z 3 kHz na ok. 2 kHz  ✅ w v3

Bell +2.5 dB na 3 kHz siedzi **dokładnie** na maksimum polskiego „sz" — to on
w pierwszej kolejności wyprodukował problem, który potem gasi de-esser. Boost
+2 dB na 2.0–2.2 kHz z Q 1.2 daje artykulację i zrozumiałość spółgłosek, ale nie
dokłada energii do sybilantów. Wtedy de-esser może pracować dużo delikatniej.

### 3. Wykorzystać stem wokalu z Suno

Suno oddaje osobny `audio (Vocals).wav`, zgrany z miksem **próbkowo** (sprawdzone
testem na odjęcie: po odjęciu stemu od miksu wokal znika, −14.3 LUFS zamiast
−11.8, które wyszłoby przy braku zgrania). Dołożenie tego stemu do miksu na
poziomie −11 dB daje **+3 dB podbicia samego wokalu**, bez ruszania fortepianu
i smyczków:

```
[1:a]highpass=f=90:poles=2,equalizer=f=300:width_type=q:width=1.2:g=-2,volume=-11dB[v];
[m][v]amix=inputs=2:duration=longest:normalize=0
```

Przelicznik: dodanie stemu na poziomie −8 dB to +3 dB wokalu, −11.7 dB to +2 dB.
Największa zaleta jest pośrednia — skoro wokal wychodzi do przodu sam z siebie,
można zejść z boostu 3 kHz na całym miksie, czyli usunąć źródło sybilantów
zamiast je gasić.

Przy Psalmie 8 odrzucone (użytkownik nie chciał plików opartych o sam wokal),
ale wersja „miks + podbity stem" to nadal jeden zwykły plik pełnego miksu.

### 4. Dynamiczny EQ zamiast statycznego boostu obecności

Bell na 3 kHz podbija obecność również tam, gdzie wokalu nie ma — w przegrywkach
podbija smyczki i talerze. EQ dynamiczny (boost tylko gdy wokal faktycznie gra,
wysterowany ze stemu wokalu jako sidechain) załatwiłby to precyzyjniej.

### 5. Odsłuch kontrolny na telefonie

Główna publiczność kanału ogląda na telefonie, gdzie nie ma dołu, a cała ocena
brzmienia rozgrywa się w paśmie 300 Hz – 8 kHz — czyli dokładnie tam, gdzie
działa ten łańcuch. To, co na monitorach brzmi „powietrznie", na głośniku
telefonu potrafi brzmieć po prostu ostro.
