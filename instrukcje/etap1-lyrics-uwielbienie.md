# Etap 1 — Lyrics uwielbienie (pieśni pisane od zera, wsad do Suno AI)

> Wariant Etapu 1 dla **autorskich pieśni uwielbienia** — utworów chrześcijańskich pisanych od zera dla polskiego słuchacza, nie będących parafrazą konkretnego psalmu. Stosuje się **zamiast** `etap1-lyrics.md`, gdy utwór jest pieśnią uwielbienia; przy pracy nad tym etapem **wczytać także `etap1-lyrics.md`** — wspólna mechanika Suno (pole Style of Music, Custom Mode, Persona, praktyka generowania, szablon struktury) obowiązuje stamtąd bez zmian i nie jest tu powielana, żeby nie rozjechały się dwa źródła prawdy.

**Model: zawsze Fable.** Jak w Etapie 1 dla psalmów — jeśli bieżąca sesja nie działa na tym modelu, delegować do subagenta z `model: "fable"`.

**Najważniejsza różnica względem psalmów:** nie ma tekstu źródłowego. Przy psalmie temat, obrazy, kolejność i łuk narracyjny wyznacza sam psalm — tutaj wszystkie trzy rzeczy projektujemy sami. Dlatego ten etap ma trzy obowiązki, których wariant psalmowy nie ma: **wybór tematu**, **praca hook-first z dużą pulą wariantów refrenu** i **zaprojektowanie łuku narracyjnego zwrotek (storytelling)**.

## Co obowiązuje bez zmian z `etap1-lyrics.md`

Wszystkie poniższe zasady stosują się wprost (szczegóły w tamtym pliku, tu tylko wyliczenie):

- **Rodzaj gramatyczny „ja" — zawsze żeński** (wokal śpiewa kobieta); formy odnoszące się do Boga („Ty") zwyczajowo męskie.
- **Start bez zwłoki** — bez `[Intro]`/`(Instrumental)`, śpiew od razu od `[Verse 1]`, na końcu `[End]`.
- **Docelowa długość: 5:00–6:00 audio** → ok. 30–40 unikalnych wersów / 46–54 linijki śpiewane; długość weryfikuje się na gotowym audio (2–3 podejścia), ratunkowo: dodatkowa powtórka refrenu, potem Extend.
- **Pole Lyrics jest dosłowne** (limit 3000 znaków) — żadnych instrukcji technicznych w tekście.
- **Rymowanie** (AABB lub ABAB, dopuszczalne asonanse, rytm ważniejszy niż idealny rym), **równy rytm fraz** (10–14 sylab, fraza = oddech, czytać na głos pod kątem zbitek spółgłosek), **prosty zrozumiały język** (z wyjątkiem utrwalonego słownictwa biblijno-liturgicznego), **poprawność gramatyczna form** (imiesłowy, rekcja, zgodność rodzaju — sprawdzić linijka po linijce przed oddaniem).
- **Znaczniki sekcji po angielsku** z opcjonalnymi opisami w tagach (2–4 opisy, w ramach brzmienia kanału), **szablon struktury** i domyślny łuk dynamiki, **powtórki refrenu identyczne słowo w słowo i tag w tag**, **backing vocals w nawiasach okrągłych jako ad-lib** (opcjonalnie), **zakaz `[Fade Out]`** i podobnych didaskaliów.
- **Pole Style of Music: standardowy wsad projektu** z frazami nienaruszalnymi, modyfikacje tylko drobne i tylko za zgodą użytkownika (szczegóły niżej — sekcja „Style of Music dla uwielbienia").
- **Custom Mode:** Exclude `male vocals, heavy drums`, suwaki Weirdness ~40–45% / Style Influence ~70–80%, **Persona z Psalmu 34** (jeden głos kanału obowiązuje też w pieśniach uwielbienia — słuchacz ma poznawać kanał po głosie, nie po gatunku tekstu).
- **Praktyka generowania:** jedna zmienna na raz, tytuły i lajki w bibliotece Suno, wybór wersji z najrówniejszą frazą i najczystszą polską wymową.
- **Zapis wyników:** finalny tekst → `txt/lirycs.txt`, finalne pole Style of Music → `txt/style.txt` (zawsze, bez wyjątku), audio → `audio/`, zaraz potem pełna struktura sześciu podfolderów.

## Temat pieśni (zastępuje psalm jako źródło)

1. **Jedna pieśń = jeden temat uwielbienia.** Temat wybieramy **przed** napisaniem pierwszej linijki — to on robi robotę, którą przy parafrazie robił psalm. Jeśli użytkownik podał temat, pracujemy na nim; jeśli nie — zaproponować **3–4 tematy** z krótkim uzasadnieniem (jaka emocja, jaki obraz przewodni) i poczekać na wybór.

2. **Bank tematów uwielbienia** (punkt startowy, nie zamknięta lista):
   - wielkość i majestat Boga (stworzenie, niebo, ziemia);
   - wdzięczność za dobroć i wierność Boga;
   - Boża obecność w codzienności (blisko, nie tylko w kościele);
   - zaufanie i oddanie (powierzenie Bogu tego, czego nie udźwignę);
   - Boże miłosierdzie i przebaczenie;
   - Jezus — imię, krzyż, zbawienie;
   - tęsknota za Bogiem i pragnienie Jego bliskości;
   - pokój w Bogu (cisza, odpocznienie, światło w ciemności).

3. **Tematy, których unikamy:** polityka, kontrowersje społeczne, polemiki międzywyznaniowe, abstrakcyjne koncepty teologiczne wymagające wykładu. Pieśń ma być śpiewalna dla każdego polskiego chrześcijanina — tak jak psalmy są wspólne dla wszystkich wyznań, pieśni pisane od zera też mają łączyć, nie dzielić.

4. **Fundament biblijny.** Tekst powstaje od zera, ale obrazowanie ma być zakorzenione w Biblii: światło, skała, źródło, pasterz, dom, droga, winnica, żniwo — obrazy, które polski słuchacz rozpozna sercem, zanim je przemyśli. Zawsze własnymi słowami, nigdy cytatem z chronionego przekładu. Sens teologiczny weryfikować: nic sprzecznego z Pismem, w razie wątpliwości uprościć — lepsza prosta prawda niż efektowna dwuznaczność.

5. **Konkret nad abstrakcją.** Zamiast pojęć — obrazy i sytuacje: nie „doświadczam Twojej łaski", tylko „Ty podnosisz mnie, gdy braknie sił". Słuchacz ma zobaczyć scenę, nie przeczytać definicję. To zasada z warsztatu songwriterskiego, która dla tekstów pisanych od zera jest jeszcze ważniejsza niż przy psalmach (psalm konkret przynosi sam).

6. **Polszczyzna od zera, nie kalki z angielskiego worship.** Nie tłumaczyć fraz z anglojęzycznych pieśni („to jest nasz Bóg", „jesteś dobry cały czas" — brzmi obco); szukać naturalnej polskiej frazy, którą można powiedzieć w rozmowie i zaśpiewać bez zgrzytu.

## Proces pracy: hook-first, potem storytelling

### Krok 1 — Refren (hook) przed wszystkim

Refren decyduje, czy pieśń zostaje w głowie — przy utworze pisanym od zera **wybór refrenu jest wyborem całej pieśni**, bo nie ma psalmu, który by ją zakotwiczał. Dlatego pula wariantów jest tu większa niż przy psalmach:

- Wygenerować **10–15 wariantów refrenu** na wybrany temat (przy psalmach wystarczy 3–5, bo serce psalmu zawęża pole — tu nie ma tego zawężenia).
- **Różnicować warianty** na czterech osiach: emocjonalnej (radość, cisza, tęsknota, pewność), obrazowej (różne obrazy przewodnie z banku biblijnego), rytmicznej (frazy krótsze/dłuższe) i językowej (anafora, pytanie retoryczne, powtórzenie frazy kluczowej).
- **Kryteria oceny każdego wariantu** (odrzucać, co nie spełnia wszystkich):
  - fraza kluczowa powtórzona **minimum 2 razy** w refrenie;
  - zapada w pamięć po jednym przeczytaniu na głos;
  - śpiewa się naturalnie (przeczytać na głos — co się źle mówi, będzie się źle śpiewać);
  - brzmi autentycznie, nie jak spis pobożnych słów;
  - mieści się w brzmieniu kanału (intymnie, nie stadionowo);
  - fraza kluczowa **nadaje się na tytuł roboczy** utworu i jest **neutralna płciowo** (zasada tytułów z `etap6-opis.md` — refren często staje się tytułem, więc pilnujemy tego już tutaj).
- **Refren wybiera Claude samodzielnie** (decyzja użytkownika z 2026-08-14 — wcześniej wybór należał do użytkownika): ocenić warianty po powyższych kryteriach, wybrać najlepszy i pracować dalej bez pytania. W podsumowaniu etapu pokazać 2–3 najmocniejsze odrzucone warianty z jednozdaniowym uzasadnieniem wyboru — użytkownik może po fakcie poprosić o zamianę.
- Wariantów nie zapisujemy do `lirycs.txt` — tam trafia tylko wersja finalna.

### Krok 2 — Storytelling zwrotek

Łuk narracyjny, który przy psalmie był dany, tu trzeba zaprojektować. Zwrotki mają opowiadać drogę, która prowadzi do refrenu i emocjonalnie go uzasadnia:

- `[Verse 1]` — **wprowadzenie sytuacji lub emocji**: zaczynać od konkretu, najlepiej z codzienności (poranek, droga, zmęczenie, cisza wieczoru), nie od tezy;
- `[Verse 2]` — **rozwój i pogłębienie**: ta sama nić, szerszy obraz lub głębsza warstwa (od „ja widzę" do „ja rozumiem");
- `[Bridge]` — **kulminacja lub zmiana perspektywy**: np. z „ja" na „my", z prośby na pewność, z ziemi na niebo — najbardziej emocjonalny moment utworu, minimalny aranż;
- `[Outro]` — **domknięcie** z powrotem frazy kluczowej refrenu (zdublowana ostatnia linijka domyka utwór).

Każda zwrotka musi **prowadzić do refrenu** — jeśli po zwrotce refren „nie wynika", zwrotka jest o czymś innym i trzeba ją przepisać, nie dopisywać przejścia.

**Open loop na początku (obowiązkowe od 2026-08-14).** Pieśń otwieramy niedopowiedzeniem albo pytaniem bohaterki, którego celowo **nie rozwiązujemy od razu** — pętla ma trzymać uwagę słuchacza (retencja YT) i zostać **spłacona po czasie**, najlepiej kaskadowo: częściowa odpowiedź w okolicy końca `[Verse 2]`, pełna w `[Bridge]` lub `[Outro]`. Po spłacie pierwszej pętli można otworzyć kolejną, mniejszą (np. motyw rzucony w `[Verse 2]` i domknięty w `[Verse 3]`). Zasady:
- pętlę otwierać w **pierwszych 1–2 linijkach** utworu (to one decydują, czy słuchacz zostanie);
- pętla ma być **organiczna** — prawdziwe pytanie bohaterki (np. „ile jestem warta?"), nie clickbaitowy teaser; pytanie retoryczne z dozwolonym „?" to naturalna forma;
- najlepiej, gdy słowa pętli tworzą **pole leksykalne ciągnące się przez cały utwór** (pytanie → echa w kolejnych sekcjach → odpowiedź), a nie pojedynczy wtręt;
- **spłacić w całości przed końcem utworu** — to pieśń uwielbienia, nie serial: słuchacz nie może zostać z pytaniem bez odpowiedzi;
- pętla nie zwalnia z reszty Kroku 2 — łuk zwrotek (sytuacja → rozwój → kulminacja → przemiana) zostaje bez zmian, open loop jest jego wzmocnieniem, nie zamiennikiem.

### Krok 3 — Spójność

Jeden temat, jeden obraz przewodni przez cały utwór (ta sama nić przewodnia, którą Etap 3 poprowadzi potem wizualnie). Bez nagłych skoków między niezwiązanymi wątkami — pieśń uwielbienia łatwo rozpada się w ciąg luźnych pobożnych zdań i to jest jej najczęstsza wada; test: każdą linijkę da się wskazać jako ogniwo drogi z Kroku 2.

### Krok 4 — Śpiewalność (finalny przegląd)

Cały tekst przeczytać na głos przed zapisaniem: równe sylaby (10–14), fraza = oddech, bez trudnych zbitek spółgłosek, naturalne akcenty. Potem przegląd gramatyczny linijka po linijce (jak w `etap1-lyrics.md` pkt 4b).

## Zasady tekstu — różnice względem wariantu psalmowego

- **Interpunkcja:** przecinki i kropki jak dotąd; **dodatkowo dopuszczony znak zapytania** w pytaniach retorycznych (podnosi intonację frazy, nie generuje pauzy — a pytanie retoryczne to naturalne narzędzie pieśni uwielbienia). Średniki, dwukropki, myślniki, cudzysłowy i **wykrzykniki** pozostają zakazane — wykrzyknik popycha Suno w ekspresję, która kłóci się z intymnym brzmieniem kanału.
- **Ekspresja (oszczędnie, opcjonalnie):** pojedyncze słowo zapisane WIELKIMI LITERAMI Suno śpiewa głośniej i z naciskiem — dopuszczalne najwyżej w jednym miejscu utworu (np. kluczowe słowo finałowego refrenu), po uzgodnieniu z użytkownikiem. Rozciąganie samogłosek („o-o-o") na razie u nas nietestowane — nie stosować bez wyraźnej zgody użytkownika, a wynik testu zapisać tutaj (ten plik pełni rolę prompt logu serii uwielbieniowej).
- **Struktura:** szablon z `etap1-lyrics.md` bez zmian (`[Verse 1]` → `[Pre-Chorus]` → `[Chorus]` → `[Verse 2]` → `[Chorus]` → `[Bridge]` → `[Outro]` → `[End]`), z tym samym domyślnym łukiem dynamiki w opisach tagów.

## Prawa autorskie — tu ostrzej niż przy psalmach

Psalm jest domeną publiczną i chroniony był tylko przekład. **Pieśń uwielbienia pisana od zera porusza się po polu gęstym od cudzych chronionych utworów** — polski repertuar uwielbieniowy (pieśni oazowe, worshipowe, chorusy) to teksty objęte prawem autorskim w całości. Dlatego:

1. Tekst ma być **w 100% autorski** — nie parafrazujemy istniejących pieśni uwielbienia, nie zapożyczamy ich charakterystycznych fraz ani refrenów.
2. **Frazę kluczową wybranego refrenu sprawdzić przed finalizacją**: czy nie pokrywa się z tytułem lub refrenem znanej pieśni religijnej (polskiej lub tłumaczonej). Jeśli brzmi znajomo — przeredagować, nawet kosztem dobrego rymu.
3. Obrazy i sformułowania biblijne (światło, skała, pasterz) są bezpieczne — to wspólne dziedzictwo, nie czyjś tekst; chodzi o gotowe frazy piosenkowe, nie o motywy.

## Style of Music dla uwielbienia

Domyślnie **standardowy wsad projektu bez zmian** (spójność brzmienia kanału jest ważniejsza niż dopasowanie do podgatunku) wraz ze wszystkimi frazami nienaruszalnymi — patrz `etap1-lyrics.md` § „Pole Style of Music". Dopuszczalne drobne modyfikacje (1–3 frazy, przez podmianę, nie dokładanie; propozycja dla użytkownika z uzasadnieniem, decyzja jego):

- pieśni radosnego uwielbienia (wdzięczność, majestat): podmiana `slow tempo` → `mid-tempo`, + `gently uplifting, joyful undertone`;
- pieśni adoracyjne, ciche (obecność, pokój, tęsknota): + `calm reverent atmosphere`;
- pieśni pokutne (miłosierdzie, przebaczenie): + `melancholic, penitential mood`.

## Folder utworu i tytuł roboczy

- Folder utworu: **`uwielbienie - [tytuł roboczy]/`** zamiast `psalm N/` — z tą samą strukturą sześciu podfolderów (`images/`, `audio/`, `prompts/`, `txt/`, `render/`, `wideo/`) i tym samym mechanizmem statusu w nazwie (`uwielbienie - [tytuł] - in progress - <cyfra>`, po publikacji `- done`).
- **Tytuł roboczy = fraza kluczowa refrenu** (2–4 słowa, neutralna płciowo). Nadawać go od razu — tak samo tytułujemy utwór w bibliotece Suno.

## Dalsze etapy pipeline'u

- **Etapy 1A, 2, 3, 4, 5 i 8 przebiegają bez zmian** — działają na plikach, nie na treści psalmu.
- **Etap 6 (opis) i Etap 7 (miniatura):** wzorzec tytułu `Psalm X - [hak] | Psalm X śpiewany` oraz napis miniatury „Psalm X" + „śpiewany" **nie stosują się wprost** do pieśni uwielbienia. Przy pierwszym utworze serii format tytułu, ogona SEO i tekstu miniatury ustalić z użytkownikiem, a wypracowaną regułę dopisać do `etap6-opis.md` i `etap7-miniatura.md` jako wariant dla serii uwielbieniowej. Frazy kluczowe z `kanal/top-10-fraz-kluczowych.pdf` dotyczą psalmów — dla uwielbienia potrzebny będzie osobny research vidIQ (nie blokuje Etapu 1).
