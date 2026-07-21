# Etap 1 — Lyrics (wsad do Suno AI)

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 1 (lyrics).

Obowiązuje dla każdego utworu w projekcie. Wsad składa się z dwóch pól: **Lyrics** (tekst) i **Style of Music** (styl).

**Model: zawsze Fable.** Etap 1 (pisanie/parafrazowanie tekstu) wykonujemy modelem Fable, niezależnie od modelu/ustawień używanych w reszcie sesji. W praktyce: jeśli bieżąca sesja nie działa na tym modelu, deleguj to zadanie do subagenta z `model: "fable"`.

**Rodzaj gramatyczny „ja" — zawsze żeński.** Wokal śpiewa kobieta, więc wszystkie formy odnoszące się do osoby psalmisty/„ja" (czasowniki w czasie przeszłym i trybie warunkowym, imiesłowy, przymiotniki) mają być w rodzaju żeńskim, np. „skryję się sama", „Choćbym rzekła", „Choćbym wstąpiła" — nie męskim. Dotyczy to każdego nowego `lirycs.txt` od tej pory, a przy okazji poprawek warto sprawdzić też starsze teksty pod tym kątem. Formy odnoszące się do Boga („Ty") zostają bez zmian (zwyczajowo męskie).

**Start bez zwłoki.** Utwór ma zaczynać się śpiewem niemal natychmiast po starcie — bez sekcji `[Intro]`/`(Instrumental)`.

**Psalm 27 jako górny limit długości (obowiązuje od 2026-07-07).** Psalm 27 (30 unikalnych wersów) wyznacza **maksymalną** długość tekstu dla kolejnych utworów — żaden nowy `lirycs.txt` nie powinien wychodzić dłuższy niż Psalm 27. Tekst może być krótszy — dopuszczalny dolny próg to ok. **80% długości Psalmu 27, czyli ok. 24 unikalne wersy**. Zakres obowiązujący dla nowych tekstów: **ok. 24–30 unikalnych wersów**. Dotyczy każdego nowego `lirycs.txt` od tej pory — nie dotyczy retroaktywnie utworów już ukończonych ani tych, gdzie audio zostało już wygenerowane w Suno (zmiana tekstu unieważniłaby dopasowanie audio i dalszych etapów).

## Zasady przygotowania tekstu (pole Lyrics)

0. **Pole Lyrics jest dosłowne.** Wszystko, co nie jest tagiem w nawiasie kwadratowym, zostanie zaśpiewane — żadnych instrukcji technicznych, opisów stylu ani uwag w tekście (Suno by je zaśpiewało). Instrukcje brzmieniowe idą wyłącznie do pola Style of Music i do opisów w tagach. Limit pola: 3000 znaków (nasze teksty 24–30 wersów mieszczą się z dużym zapasem).

1. **Zawsze parafraza — nigdy tekst przekładu.** Nie wklejamy tekstu żadnego chronionego przekładu (Biblia Tysiąclecia itp.) — zawsze piszemy **własną parafrazę** psalmu. Powód: brak problemów z prawami autorskimi przy generowaniu i przy publikacji. Przekład (weryfikowany ze źródłem, nie z pamięci) służy wyłącznie jako podstawa znaczeniowa.
2. **Parafraza wierna psalmowi.** Zachowujemy wszystkie obrazy, pojęcia i ich kolejność (pasterz, zielone łąki, ciemna dolina, kij i laska, stół, kielich, dom Pana...). Niczego nie pomijamy; drobne poetyckie dopowiedzenia w duchu psalmu są dozwolone, jeśli służą rymowi i melodii.
3. **Ma się ładnie rymować.** Piszemy tak, żeby wyszła ładna piosenka: rymy parami (AABB) lub przeplatane (ABAB), dopuszczalne rymy niedokładne/asonanse, jeśli brzmią naturalnie. Unikamy rymów częstochowskich na siłę — lepszy dobry asonans niż wymuszony rym.
4. **Równy rytm fraz.** Wersy o zbliżonej liczbie sylab (ok. 10–14), krótkie frazy-oddechy (jedna fraza = jeden oddech). Długie, nierówne linijki powodują, że Suno „rozciąga" tekst i robi 2–3-sekundowe pauzy w środku wersu.
5. **Prosta interpunkcja.** Tylko przecinki i kropki — bez średników, dwukropków, myślników i cudzysłowów (generują pauzy). Bez numerów wersetów.
6. **Powtórzenia są mile widziane.** Refren wraca w całości; można też powtórzyć pojedynczą kluczową frazę (np. ostatnią linijkę Outro) dla domknięcia utworu.
7. **Znaczniki sekcji w nawiasach kwadratowych**, po angielsku: `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2]`, `[Bridge]`, `[Outro]`, `[End]`. Suno ich nie śpiewa — traktuje jako strukturę utworu. **Bez `[Intro]`/`(Instrumental)`** — tekst zaczyna się od razu od `[Verse 1]`, na samym końcu tekstu stawiamy `[End]`.
   - **Opisy w tagach (opcjonalne, po dwukropku):** tag może dostać 2–4 krótkie opisy po angielsku sterujące charakterem danej sekcji, wzorem `[Verse 1: Soft, Intimate, Piano Only]`, `[Chorus: Fuller Arrangement, Soaring]`, `[Bridge: Minimal, Emotional]`. To najskuteczniejszy sposób nadania utworowi łuku dynamiki (delikatne zwrotki → pełniejszy refren → wyciszony bridge → domykające outro) bez zmiany pola Style of Music. Więcej niż 4–5 opisów na tag gubi Suno — nie przekraczać. Opisy mają zostać w ramach brzmienia kanału (soft/intimate/piano/strings itp.), nie wprowadzać obcego instrumentarium ani agresywnej dynamiki (bez `Drop`, `Heavy`, `Aggressive`).
8. **Klasyczna struktura piosenki z powtórzonym refrenem, bez wstępu instrumentalnego.** Psalm dzielimy jak piosenkę, zaczynając od razu śpiewem: `[Verse 1]` (5–6 linijek) → `[Pre-Chorus]` (wydzielona 1–2-linijkowa zapowiedź) → `[Chorus]` → `[Verse 2]` (5–6 linijek) → `[Chorus]` (powtórka, identyczna słowo w słowo) → `[Bridge]` (3–4 linijki, standardowy element, nie opcjonalny) → `[Outro]` (6–8 linijek, pełne domknięcie psalmu). Do `[Chorus]` wybieramy emocjonalne serce psalmu (np. w Psalmie 23 — „ciemną dolinę"). Refren powtarzamy zwykle raz (po Verse 2); przy psalmach bogatszych w treść można dodać drugą powtórkę refrenu albo dodatkowy `[Verse 3]` przed `[Bridge]`.
9. **Bez `[Fade to silence]`, `[Fade Out]`** i podobnych didaskaliów na końcu — potrafią wywołać dziwne wyciszenia. Zakończenie oznaczamy znacznikiem `[End]`. (Poradniki Suno często polecają `[Outro: Fade Out]` — u nas ta technika się nie sprawdziła i pozostaje zakazana; doświadczenie projektu ma pierwszeństwo przed ogólnymi poradnikami.)
10. Jeśli utwór wychodzi za krótki — najpierw powtórka refrenu (pkt 8), potem ewentualnie funkcja **Extend** w Suno.

## Prawa autorskie

Standard projektu: **wyłącznie autorska parafraza** (pkt 1) — dzięki temu nie ma problemu ani z filtrem copyright w Suno, ani z prawami przy publikacji na YouTube. Tekstów chronionych przekładów (Biblia Tysiąclecia i inne współczesne) nie wklejamy do Suno w ogóle. Gdyby kiedyś zależało nam na dosłownym tekście przekładu, alternatywy to: przekład z domeny publicznej (Biblia Gdańska, Wujek) albo zgoda wydawcy (dla Tysiąclatki: Pallottinum).

## Pole Style of Music

**Standardowy wsad projektu** — używany domyślnie przy każdym psalmie, dla spójności brzmienia kanału:

```
intimate acoustic worship, soft emotional female vocals, delicate piano, atmospheric, reflective, slow tempo, ambient, smooth continuous vocal phrasing, flowing melodic lines without long pauses, vocals begin immediately with no instrumental intro, track ends shortly after the vocals finish with no extended instrumental outro, intimate and spiritual, Polish lyrics
```

**Jak Suno czyta to pole (anatomia prompta):** Suno nie rozumie muzyki — dopasowuje wzorce do słów, dlatego liczy się kolejność i dyscyplina. **Gatunek zawsze na początku** (u nas: `intimate acoustic worship` — to on definiuje „osobowość" utworu i musi zostać pierwszy), dalej wokal, instrumentarium, nastrój, tempo, frazy funkcjonalne. Optimum Suno to 5–10 elementów — nasz standardowy wsad już jest na górnej granicy (frazy funkcjonalne są długie, ale sprawdzone), więc modyfikacje robimy **przez podmianę, nie dokładanie**: nowa fraza wchodzi w miejsce jednej z istniejących (spoza listy nienaruszalnych poniżej), nie na koniec coraz dłuższej listy. Nie wprowadzać elementów sprzecznych z resztą prompta (np. `upbeat`/`fast` obok `slow tempo`, `powerful` obok `soft` — Suno dostaje wtedy chaos zamiast stylu); psalmom radosnym tempo podnosimy podmianą `slow tempo` → `mid-tempo`, nie dopisaniem drugiego określenia tempa. Całe pole zawsze po angielsku (polskie słowa w prompcie działają nieprzewidywalnie — polszczyznę wymusza wyłącznie fraza `Polish lyrics`). Przymiotnik przy instrumencie daje lepszą kontrolę niż sama nazwa (dlatego `delicate piano`, nie `piano` — analogicznie przy ewentualnych korektach: `soft strings`, nie `strings`). Konkretne wartości BPM w prompcie są zawodne — trzymamy się określeń opisowych (`slow tempo`, `mid-tempo`).

**Zasada modyfikacji:** jeśli charakter psalmu wyraźnie tego wymaga, dopuszczalna jest **drobna zmiana** stylu (1–3 frazy dodane lub podmienione), ale **nigdy istotna przebudowa** — brzmienie kanału ma pozostać spójne. Każdą proponowaną zmianę sugerujemy użytkownikowi przy etapie 1 (lyrics), z uzasadnieniem; decyzja należy do niego. Przykłady drobnych, dopuszczalnych korekt:

- psalmy pokutne (51, 130): + `melancholic, penitential mood`;
- psalmy radosne / hymny (100, 118, 150): + `gently uplifting, joyful undertone` (ew. odrobinę żywsze tempo — bez zmiany instrumentarium);
- psalmy nocne / o ochronie (4, 91, 121): + `calm nocturnal atmosphere`.

Kluczowe frazy, których **nigdy nie usuwamy ani nie zmieniamy**:

- `smooth continuous vocal phrasing, flowing melodic lines without long pauses` — pilnuje, żeby Suno nie robiło długich pauz między wyrazami;
- `vocals begin immediately with no instrumental intro` — utwór ma zaczynać się śpiewem od razu po starcie, bez wstępu instrumentalnego;
- `track ends shortly after the vocals finish with no extended instrumental outro` — utwór ma się kończyć krótko po ostatniej zaśpiewanej linijce, bez rozbudowanego outro instrumentalnego;
- `Polish lyrics` — wymusza polską wymowę;
- `intimate acoustic worship, soft emotional female vocals` — rdzeń tożsamości brzmieniowej kanału.

## Ustawienia Custom Mode (Exclude, suwaki, Persona)

Generujemy zawsze w **Custom Mode** (własny tekst + własny styl). Poza polami Lyrics i Style of Music są tam trzy narzędzia, które wprost wspierają spójność serii:

**Exclude (prompty negatywne, w Advanced Options).** Standardowy wsad projektu:

```
male vocals, heavy drums
```

Jedno–dwa celne wykluczenia działają lepiej niż długa lista (za dużo wykluczeń miesza modelowi tak samo jak za długi prompt) — te dwa pilnują dwóch najczęstszych odchyleń od brzmienia kanału: męskiego/dublowanego męskiego wokalu i zbyt ciężkiej perkusji. Nie rozbudowywać rutynowo; trzecie wykluczenie dodać tylko, gdy w kolejnych generacjach powtarza się konkretny niechciany element.

**Creative Sliders (Weirdness / Style Influence).** Nasz przypadek to „wiem dokładnie, czego chcę, seria ma brzmieć spójnie", więc domyślnie:

- **Weirdness: ~40–45%** (lekko poniżej normy — przewidywalnie, bez eksperymentów; chwytliwość i powtarzalność ważniejsze niż zaskoczenie);
- **Style Influence: ~70–80%** (mocne trzymanie się naszego opisu stylu — po to mamy dopracowany wsad).

Nie podkręcać Weirdness powyżej ~55% ani nie luzować Style Influence poniżej ~60% bez wyraźnego powodu; przy iterowaniu zmieniać **jeden suwak na raz**, żeby było wiadomo, co wpłynęło na wynik.

**Persona (spójny głos serii).** Suno pozwala zapisać głos/klimat udanego utworu jako Personę i używać jej we wszystkich kolejnych generacjach — dla kanału opartego na jednym żeńskim wokalu to najskuteczniejsze narzędzie spójności brzmienia (słuchacze kojarzą „ten głos" z kanałem). Rekomendowany krok: wybrać spośród opublikowanych psalmów utwór z najlepszym, najbardziej reprezentatywnym wokalem, utworzyć z niego Personę (… → Create → Make Persona, ustawić jako **prywatną**) i od tej pory generować wszystkie nowe psalmy z tą Personą (Persona wypełnia pole Style — sprawdzić, czy nasze frazy nienaruszalne pozostały w mocy). **Wybór utworu-źródła należy do użytkownika** — przy najbliższym Etapie 1 zapytać, czy chce Personę założyć i z którego psalmu.

## Praktyka generowania

- Generacja to trochę loteria: jeśli utwór ma dziury/pauzy w wokale, zwykle wystarczą 2–3 próby z tym samym promptem.
- Przy iterowaniu zmieniać **jedną zmienną na raz** (najpierw zablokować tekst, potem testować warianty stylu, na końcu ewentualnie suwaki) — zmiana kilku rzeczy naraz nie mówi, co poprawiło albo zepsuło wynik. Frazy, które dały dobry rezultat, trafiają do instrukcji (ten plik pełni rolę „prompt logu" projektu).
- W bibliotece Suno nadawać utworom tytuły (np. „Psalm 42") i oznaczać udane wersje lajkiem — przy kilkudziesięciu generacjach bez tego robi się chaos i trudno odnaleźć wybrane ujęcie.
- Wybierać wersję z najrówniejszą frazą wokalną i najczystszą polską wymową; drobne artefakty wymowy dyskwalifikują ujęcie, bo tekst psalmu musi być zrozumiały.
- **Każdy wygenerowany wsad lyrics zapisujemy od razu do podfolderu `txt/` jako `lirycs.txt`** (dokładnie ta wersja, która idzie do Suno) — to źródło dla teledysku, napisów i opisu filmu.
- **Finalne pole Style of Music (dokładnie to, co poszło do Suno, z uwzględnieniem ewentualnej zaakceptowanej modyfikacji) zapisujemy od razu do podfolderu `txt/` jako `style.txt`** — obok `lirycs.txt`, żeby wiadomo było, jakim stylem dany utwór wygenerowano. **Plik `style.txt` zakładamy zawsze, bez wyjątku** — również wtedy, gdy użytkownik nie przyjął żadnej modyfikacji i finalny styl jest identyczny ze standardowym wsadem projektu; nie pomijamy pliku tylko dlatego, że treść pokrywa się z domyślną.
- Po wybraniu wersji utworu: pobrać `audio.wav`/`mp3` do podfolderu `audio/`.
- **Zaraz po zapisaniu `lirycs.txt` i audio: założyć pełną strukturę katalogów** (`images/`, `audio/`, `prompts/`, `txt/`, `render/`, `wideo/`) w folderze utworu — patrz `styl-teledysku.md` → „Struktura katalogów w folderze utworu". Zakładać ją od razu, nawet jeśli część podfolderów na razie zostaje pusta.

## Szablon struktury

```
[Verse 1: Soft, Intimate, Piano Only]
...5–6 linijek...

[Pre-Chorus: Building Gently]
...1–2 linijki zapowiedzi refrenu...

[Chorus: Fuller Arrangement, Emotional]
...emocjonalne serce psalmu...

[Verse 2: Soft, More Layers]
...5–6 linijek...

[Chorus: Fuller Arrangement, Emotional]
...powtórka refrenu, identyczna słowo w słowo...

[Bridge: Minimal, Quiet, Emotional]            (standardowy element, nie opcjonalny — 3–4 linijki)
...

[Outro: Gentle, Peaceful Ending]
...6–8 linijek, pełne domknięcie psalmu...
[End]
```

Opisy w tagach powyżej to **domyślny łuk dynamiki** serii (cicho → pełniej → wyciszenie → domknięcie): delikatna pierwsza zwrotka, pełniejszy refren, minimalny bridge jako emocjonalny oddech przed finałem. Można je dostosować do charakteru psalmu (albo pominąć przy psalmach, gdzie jednolita dynamika brzmi lepiej) — w granicach z pkt 7 „Opisy w tagach". Przy powtórce refrenu opisy zostawiamy identyczne jak za pierwszym razem, żeby Suno nie przearanżowało powtórki.

Utwór zaczyna się od razu od `[Verse 1]` — bez sekcji `[Intro]`/`(Instrumental)`. Przy psalmach bogatszych w treść, między `[Bridge]` a `[Outro]` (albo przed `[Bridge]`) można dodać `[Verse 3]`.

**Backing vocals w refrenie:** w `[Chorus]` mogą, ale nie muszą wystąpić backing vocals (np. dopisane w nawiasie pod główną linijką) — decyzja zależy od tego, czy dany psalm się do tego nadaje; nie jest to element obowiązkowy w szablonie. Mechanika Suno: tekst w nawiasach okrągłych `( )` na końcu linijki jest wykonywany jako **ad-lib** — ciszej, w tle, za głównym wokalem — dokładnie tego chcemy od backing vocals; nie umieszczać w nawiasach okrągłych niczego, co ma wybrzmieć jako pełnoprawna linijka.

**Modyfikacja szablonu:** jeśli struktura konkretnego psalmu wyraźnie lepiej pasuje do innego układu sekcji (np. brak naturalnego `[Pre-Chorus]`, potrzeba dodatkowego `[Verse 3]`, inny układ powtórzeń refrenu), szablon można zmodyfikować. Nie może się to jednak dziać za każdym razem od nowa — trzymamy się tego szablonu jako domyślnego układu w większości utworów, żeby seria brzmiała spójnie; odstępstwo powinno być uzasadnione charakterem danego psalmu, nie stosowane rutynowo.
