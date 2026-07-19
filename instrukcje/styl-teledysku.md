# Psalmy: Muzyka i Słowo — wytyczne stylu i produkcji teledysków (v17)

> Obowiązuje dla każdego teledysku w projekcie. Przykłady odnoszą się do Psalmu 91 (utwór 5:20), ale zasady stosuje się do wszystkich utworów.

## Zasady współpracy

**Rób tylko to, o co poproszono.** Jeśli przy okazji zadania zauważysz coś, co Twoim zdaniem warto by też zmienić albo zaktualizować (np. inny plik, inny utwór, starszy wpis) — nie rób tego samodzielnie. Zapytaj użytkownika i poczekaj na zgodę, zanim ruszysz zakres poza to, o co wyraźnie poprosił.

**Skrypty zawsze zapisuj do repo, nie tylko do scratchpada.** Jeśli w ramach zadania piszesz skrypt (Python, shell itp.), który automatyzuje jakiś krok produkcji (np. generowanie miniatury, wyciąganie klatki, analiza dźwięku) — zapisz go w `instrukcje/skrypty/` zamiast zostawiać tylko w katalogu tymczasowym. Proces sześciu etapów powtarza się dla każdego psalmu, więc taki skrypt się jeszcze przyda — nie pisz go od zera za każdym razem, tylko wczytaj i uruchom istniejący (aktualizując go, jeśli zasady się zmieniły).

> **Struktura instrukcji:** ten plik jest spisem wszystkich 7 etapów ze streszczeniem i zasadami wspólnymi (rozdzielczość). Szczegóły każdego etapu są wydzielone do osobnych plików, żeby sesja pracująca nad jednym etapem nie musiała wczytywać całości:
> - Etap 1 (lyrics): `instrukcje/etap1-lyrics.md`
> - Etap 2 (napisy): `instrukcje/etap2-napisy.md`
> - Etap 3 (prompty do obrazków, cały styl wizualny): `instrukcje/etap3-prompty-stylu.md`
> - Etap 4 (generowanie obrazków przez Leonardo AI): `instrukcje/etap4-generowanie-obrazkow.md`
> - Etap 5 (obrabianie obrazków): `instrukcje/etap5-obrobka-obrazkow.md`
> - Etap 6 (opis filmu, tagi, tytuły): `instrukcje/etap6-opis.md`
> - Etap 7 (miniatura): `instrukcje/etap7-miniatura.md`
> - Etap 8 (oś czasu do DaVinci Resolve): `instrukcje/etap8-timeline-davinci.md`

## Rozdzielczość docelowa (jedno miejsce, obowiązuje wszędzie)

**2560×1440 (2K), format 16:9.** Dotyczy: promptów pod docelową rozdzielczość (Etap 3), generowania/upscalowania obrazków (Etap 4) oraz kadrowania i konwersji plików (Etap 5). Szczegóły generowania/upscalowania: patrz `instrukcje/etap4-generowanie-obrazkow.md`; szczegóły przycinania do 16:9: patrz `instrukcje/etap5-obrobka-obrazkow.md`.

## Struktura katalogów w folderze utworu (jedno miejsce, obowiązuje wszędzie)

Każdy folder `psalm N/` ma stały układ podfolderów wg **typu pliku** — zakładany od razu po Etapie 1, zaraz po zapisaniu `lirycs.txt` (i pobraniu audio), jeszcze zanim powstaną pliki kolejnych etapów:

- **`images/`** — wszystkie pliki graficzne: surowe wygenerowane kadry (Etap 4), kadry po przycięciu/konwersji (Etap 5), miniatura (Etap 7). Odrzucone wersje obrazków trafiają do `images/_do_usuniecia/`.
- **`audio/`** — pliki audio (`audio.mp3`, `audio.wav`).
- **`prompts/`** — pliki z promptami do obrazków (`prompty.md` i warianty, np. `prompty-opus.md`).
- **`txt/`** — pozostałe pliki tekstowe utworu: `lirycs.txt`, `style.txt` (pole Style of Music użyte w Suno), `napisy.srt`, `opis.txt`.
- **`render/`** — pliki projektu montażowego: `movavi.mepj` oraz oś czasu do DaVinci Resolve wygenerowana w Etapie 8 (`timeline_edytowalny.fcpxml`, `timeline_edytowalny_fcp7.xml`).
- **`wideo/`** — finalny wyeksportowany plik wideo (`.mp4`).

Zakładać wszystkie sześć podfolderów od razu (nawet jeśli część na razie zostaje pusta, bo dany etap jeszcze nie był realizowany) — struktura ma być identyczna w każdym kolejnym folderze psalmu (podfoldery odpowiadają typom plików, nie liczbie etapów, więc zostaje ich sześć mimo że etapów jest teraz osiem).

## Nazwa folderu jako status produkcji

Nazwa folderu `psalm N/` sama niesie status: `psalm N - in progress - <cyfra>` w trakcie produkcji, `psalm N - done` po publikacji filmu. `<cyfra>` to numer ostatnio **ukończonego** etapu, zapisany cyfrą, bez słowa „etap" (1, 2, 3, 4, 5, 6, 7 lub 8) — np. `psalm 121 - in progress - 3` — Etap 1, 2 i 3 gotowe, Etap 4 jeszcze nie.

**Po zakończeniu każdego etapu zmieniać nazwę folderu**, tak żeby zawsze zawierała cyfrę właśnie ukończonego etapu (nadpisując poprzednią cyfrę, jeśli folder już ją miał).

## Etapy pracy nad każdym filmem

Praca nad każdym utworem przebiega w **ośmiu etapach**, wykonywanych w kolejności numeracji. Użytkownik mówi tylko, do którego etapu przejść — reszta wynika z instrukcji.

1. **Etap 1 — Lyrics.** Autorska rymowana parafraza psalmu + struktura pod Suno. Wynik: `lirycs.txt` w podfolderze `txt/`. Zaraz po tym etapie zakładać strukturę katalogów opisaną wyżej. Wykonywać zawsze modelem **Fable** (jeśli bieżąca sesja nie działa na tym modelu, delegować do subagenta z `model: "fable"`). Pełne zasady, w tym reguła o żeńskim rodzaju gramatycznym „ja": `instrukcje/etap1-lyrics.md`.

2. **Etap 2 — Napisy.** Wygenerowanie `napisy.srt` (tekst zsynchronizowany z audio) w podfolderze `txt/`. Wykonywany celowo **przed** Etapem 3 (prompty) — jego dokładne znaczniki czasowe per-linijka napędzają rozpisanie kadrów w Etapie 3, zamiast żeby Etap 3 szacował strukturę audio samodzielnie. Wykonywać zawsze modelem **Sonnet**, z trybem **Thinking wyłączonym** i effortem **medium** (jeśli bieżąca sesja nie działa na tych parametrach, delegować do subagenta z `model: "sonnet"`, effort medium). Pełna metoda synchronizacji: `instrukcje/etap2-napisy.md`.

3. **Etap 3 — Prompty do obrazków.** Rozpisanie 16–26 kadrów (dosłowność, 10–20 s/kadr, lead ~1 s, łuk kolorystyczny, nić przewodnia) na bazie dokładnych znaczników czasowych z `txt/napisy.srt` (Etap 2). Ten etap decyduje też, który kadr będzie bazą miniatury (Etap 7) — decyzja zapisana jawnie w `prompty.md`. Wynik: `prompty.md` w podfolderze `prompts/`. **Warunek wstępny: musi już istnieć plik audio w podfolderze `audio/` ORAZ gotowy `txt/napisy.srt`** — jeśli któregoś z nich brakuje, nie rozpoczynać tego etapu, tylko zatrzymać się i zgłosić użytkownikowi brak. Wykonywać zawsze modelem **Fable** (jeśli bieżąca sesja nie działa na tym modelu, delegować do subagenta z `model: "fable"`). Pełne zasady stylu wizualnego, kanoniczny blok promptu, negative prompt i tempo montażu: `instrukcje/etap3-prompty-stylu.md`.

4. **Etap 4 — Generowanie obrazków przez Leonardo AI.** Z promptów przygotowanych w Etapie 3 wygenerować faktyczne pliki obrazków, kadr po kadrze, bezpośrednio przez API Leonardo z Claude Code (bez przeglądarki). Domyślnie: tryb standard (bez Ultra), Full HD 1920×1080, jeden obraz na kadr; koszt każdej generacji zgłaszać użytkownikowi w złotówkach. **Model Claude: Haiku, effort low** (obrazy generuje Leonardo, nie Claude). Pełne zasady i sposób wywołania skryptu: `instrukcje/etap4-generowanie-obrazkow.md`.

5. **Etap 5 — Obrabianie obrazków.** Po wgraniu wygenerowanych plików (w podfolderze `images/`): zmiana nazw na znaczniki czasowe, kadrowanie do 16:9, konwersja wg zasad jakości. Wyłącznie techniczne przetworzenie plików — bez oceny treści. **Model Claude: Haiku, effort low.** Pełne zasady: `instrukcje/etap5-obrobka-obrazkow.md`.

6. **Etap 6 — Opis filmu.** Wygenerowanie `opis.txt` (tytuł, opis, tagi, hashtagi) w podfolderze `txt/`. Wykonywać zawsze modelem **Fable** (jeśli bieżąca sesja nie działa na tym modelu, delegować do subagenta z `model: "fable"`). Pełny format opisu, źródło fraz kluczowych, zasady tagów i dwóch tytułów: `instrukcje/etap6-opis.md`.

7. **Etap 7 — Miniatura.** Wygenerowanie miniatury 1280×720 na bazie kadru wskazanego w Etapie 3 (nie pierwszego pliku domyślnie, nie pytamy użytkownika o wybór), z napisem „Psalm X" + „śpiewany" na ciemnym panelu z równym paddingiem. **Model Claude: Haiku, effort low** (wygląd realizuje skrypt Pillow). Pełne zasady i nazewnictwo plików publikacyjnych: `instrukcje/etap7-miniatura.md`.

8. **Etap 8 — Oś czasu do DaVinci Resolve.** Wygenerowanie edytowalnej osi czasu (`timeline_edytowalny_fcp7.xml`, XMEML v5) w podfolderze `render/`, na bazie plików z `images/` nazwanych znacznikami czasu w Etapie 5 — klipy rozmieszczone automatycznie wg nazw plików, w pełni trimowalne i gotowe na przejścia po zaimportowaniu do darmowej wersji DaVinci Resolve, w rozdzielczości sekwencji 2560×1440. **Model Claude: Haiku, effort low.** Pełne zasady i sposób wywołania skryptu: `instrukcje/etap8-timeline-davinci.md`.

