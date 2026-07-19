# Etap 1 — Lyrics (wsad do Suno AI)

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 1 (lyrics).

Obowiązuje dla każdego utworu w projekcie. Wsad składa się z dwóch pól: **Lyrics** (tekst) i **Style of Music** (styl).

**Model: zawsze Fable.** Etap 1 (pisanie/parafrazowanie tekstu) wykonujemy modelem Fable, niezależnie od modelu/ustawień używanych w reszcie sesji. W praktyce: jeśli bieżąca sesja nie działa na tym modelu, deleguj to zadanie do subagenta z `model: "fable"`.

**Rodzaj gramatyczny „ja" — zawsze żeński.** Wokal śpiewa kobieta, więc wszystkie formy odnoszące się do osoby psalmisty/„ja" (czasowniki w czasie przeszłym i trybie warunkowym, imiesłowy, przymiotniki) mają być w rodzaju żeńskim, np. „skryję się sama", „Choćbym rzekła", „Choćbym wstąpiła" — nie męskim. Dotyczy to każdego nowego `lirycs.txt` od tej pory, a przy okazji poprawek warto sprawdzić też starsze teksty pod tym kątem. Formy odnoszące się do Boga („Ty") zostają bez zmian (zwyczajowo męskie).

**Start bez zwłoki.** Utwór ma zaczynać się śpiewem niemal natychmiast po starcie — bez sekcji `[Intro]`/`(Instrumental)`.

**Psalm 27 jako górny limit długości (obowiązuje od 2026-07-07).** Psalm 27 (30 unikalnych wersów) wyznacza **maksymalną** długość tekstu dla kolejnych utworów — żaden nowy `lirycs.txt` nie powinien wychodzić dłuższy niż Psalm 27. Tekst może być krótszy — dopuszczalny dolny próg to ok. **80% długości Psalmu 27, czyli ok. 24 unikalne wersy**. Zakres obowiązujący dla nowych tekstów: **ok. 24–30 unikalnych wersów**. Dotyczy każdego nowego `lirycs.txt` od tej pory — nie dotyczy retroaktywnie utworów już ukończonych ani tych, gdzie audio zostało już wygenerowane w Suno (zmiana tekstu unieważniłaby dopasowanie audio i dalszych etapów).

## Zasady przygotowania tekstu (pole Lyrics)

1. **Zawsze parafraza — nigdy tekst przekładu.** Nie wklejamy tekstu żadnego chronionego przekładu (Biblia Tysiąclecia itp.) — zawsze piszemy **własną parafrazę** psalmu. Powód: brak problemów z prawami autorskimi przy generowaniu i przy publikacji. Przekład (weryfikowany ze źródłem, nie z pamięci) służy wyłącznie jako podstawa znaczeniowa.
2. **Parafraza wierna psalmowi.** Zachowujemy wszystkie obrazy, pojęcia i ich kolejność (pasterz, zielone łąki, ciemna dolina, kij i laska, stół, kielich, dom Pana...). Niczego nie pomijamy; drobne poetyckie dopowiedzenia w duchu psalmu są dozwolone, jeśli służą rymowi i melodii.
3. **Ma się ładnie rymować.** Piszemy tak, żeby wyszła ładna piosenka: rymy parami (AABB) lub przeplatane (ABAB), dopuszczalne rymy niedokładne/asonanse, jeśli brzmią naturalnie. Unikamy rymów częstochowskich na siłę — lepszy dobry asonans niż wymuszony rym.
4. **Równy rytm fraz.** Wersy o zbliżonej liczbie sylab (ok. 10–14), krótkie frazy-oddechy (jedna fraza = jeden oddech). Długie, nierówne linijki powodują, że Suno „rozciąga" tekst i robi 2–3-sekundowe pauzy w środku wersu.
5. **Prosta interpunkcja.** Tylko przecinki i kropki — bez średników, dwukropków, myślników i cudzysłowów (generują pauzy). Bez numerów wersetów.
6. **Powtórzenia są mile widziane.** Refren wraca w całości; można też powtórzyć pojedynczą kluczową frazę (np. ostatnią linijkę Outro) dla domknięcia utworu.
7. **Znaczniki sekcji w nawiasach kwadratowych**, po angielsku: `[Verse 1]`, `[Pre-Chorus]`, `[Chorus]`, `[Verse 2]`, `[Bridge]`, `[Outro]`, `[End]`. Suno ich nie śpiewa — traktuje jako strukturę utworu. **Bez `[Intro]`/`(Instrumental)`** — tekst zaczyna się od razu od `[Verse 1]`, na samym końcu tekstu stawiamy `[End]`.
8. **Klasyczna struktura piosenki z powtórzonym refrenem, bez wstępu instrumentalnego.** Psalm dzielimy jak piosenkę, zaczynając od razu śpiewem: `[Verse 1]` (5–6 linijek) → `[Pre-Chorus]` (wydzielona 1–2-linijkowa zapowiedź) → `[Chorus]` → `[Verse 2]` (5–6 linijek) → `[Chorus]` (powtórka, identyczna słowo w słowo) → `[Bridge]` (3–4 linijki, standardowy element, nie opcjonalny) → `[Outro]` (6–8 linijek, pełne domknięcie psalmu). Do `[Chorus]` wybieramy emocjonalne serce psalmu (np. w Psalmie 23 — „ciemną dolinę"). Refren powtarzamy zwykle raz (po Verse 2); przy psalmach bogatszych w treść można dodać drugą powtórkę refrenu albo dodatkowy `[Verse 3]` przed `[Bridge]`.
9. **Bez `[Fade to silence]`** i podobnych didaskaliów na końcu — potrafią wywołać dziwne wyciszenia. Zakończenie oznaczamy znacznikiem `[End]`.
10. Jeśli utwór wychodzi za krótki — najpierw powtórka refrenu (pkt 8), potem ewentualnie funkcja **Extend** w Suno.

## Prawa autorskie

Standard projektu: **wyłącznie autorska parafraza** (pkt 1) — dzięki temu nie ma problemu ani z filtrem copyright w Suno, ani z prawami przy publikacji na YouTube. Tekstów chronionych przekładów (Biblia Tysiąclecia i inne współczesne) nie wklejamy do Suno w ogóle. Gdyby kiedyś zależało nam na dosłownym tekście przekładu, alternatywy to: przekład z domeny publicznej (Biblia Gdańska, Wujek) albo zgoda wydawcy (dla Tysiąclatki: Pallottinum).

## Pole Style of Music

**Standardowy wsad projektu** — używany domyślnie przy każdym psalmie, dla spójności brzmienia kanału:

```
intimate acoustic worship, soft emotional female vocals, delicate piano, atmospheric, reflective, slow tempo, ambient, smooth continuous vocal phrasing, flowing melodic lines without long pauses, vocals begin immediately with no instrumental intro, track ends shortly after the vocals finish with no extended instrumental outro, intimate and spiritual, Polish lyrics
```

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

## Praktyka generowania

- Generacja to trochę loteria: jeśli utwór ma dziury/pauzy w wokale, zwykle wystarczą 2–3 próby z tym samym promptem.
- Wybierać wersję z najrówniejszą frazą wokalną i najczystszą polską wymową; drobne artefakty wymowy dyskwalifikują ujęcie, bo tekst psalmu musi być zrozumiały.
- **Każdy wygenerowany wsad lyrics zapisujemy od razu do podfolderu `txt/` jako `lirycs.txt`** (dokładnie ta wersja, która idzie do Suno) — to źródło dla teledysku, napisów i opisu filmu.
- **Finalne pole Style of Music (dokładnie to, co poszło do Suno, z uwzględnieniem ewentualnej zaakceptowanej modyfikacji) zapisujemy od razu do podfolderu `txt/` jako `style.txt`** — obok `lirycs.txt`, żeby wiadomo było, jakim stylem dany utwór wygenerowano. **Plik `style.txt` zakładamy zawsze, bez wyjątku** — również wtedy, gdy użytkownik nie przyjął żadnej modyfikacji i finalny styl jest identyczny ze standardowym wsadem projektu; nie pomijamy pliku tylko dlatego, że treść pokrywa się z domyślną.
- Po wybraniu wersji utworu: pobrać `audio.wav`/`mp3` do podfolderu `audio/`.
- **Zaraz po zapisaniu `lirycs.txt` i audio: założyć pełną strukturę katalogów** (`images/`, `audio/`, `prompts/`, `txt/`, `render/`, `wideo/`) w folderze utworu — patrz `styl-teledysku.md` → „Struktura katalogów w folderze utworu". Zakładać ją od razu, nawet jeśli część podfolderów na razie zostaje pusta.

## Szablon struktury

```
[Verse 1]
...5–6 linijek...

[Pre-Chorus]
...1–2 linijki zapowiedzi refrenu...

[Chorus]
...emocjonalne serce psalmu...

[Verse 2]
...5–6 linijek...

[Chorus]
...powtórka refrenu, identyczna słowo w słowo...

[Bridge]            (standardowy element, nie opcjonalny — 3–4 linijki)
...

[Outro]
...6–8 linijek, pełne domknięcie psalmu...
[End]
```

Utwór zaczyna się od razu od `[Verse 1]` — bez sekcji `[Intro]`/`(Instrumental)`. Przy psalmach bogatszych w treść, między `[Bridge]` a `[Outro]` (albo przed `[Bridge]`) można dodać `[Verse 3]`.

**Backing vocals w refrenie:** w `[Chorus]` mogą, ale nie muszą wystąpić backing vocals (np. dopisane w nawiasie pod główną linijką) — decyzja zależy od tego, czy dany psalm się do tego nadaje; nie jest to element obowiązkowy w szablonie.

**Modyfikacja szablonu:** jeśli struktura konkretnego psalmu wyraźnie lepiej pasuje do innego układu sekcji (np. brak naturalnego `[Pre-Chorus]`, potrzeba dodatkowego `[Verse 3]`, inny układ powtórzeń refrenu), szablon można zmodyfikować. Nie może się to jednak dziać za każdym razem od nowa — trzymamy się tego szablonu jako domyślnego układu w większości utworów, żeby seria brzmiała spójnie; odstępstwo powinno być uzasadnione charakterem danego psalmu, nie stosowane rutynowo.
