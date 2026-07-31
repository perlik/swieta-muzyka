# Etap 6 — Opis filmu

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 6 (opis filmu, tagi, tytuły).

**Cel etapu:** wygenerowanie pliku `opis.txt` w podfolderze `txt/`, zawierającego: tytuł filmu, opis, tagi i hashtagi.

**Model: zawsze Fable.** Etap 6 (opis filmu) wykonujemy modelem Fable, niezależnie od modelu/ustawień używanych w reszcie sesji. W praktyce: jeśli bieżąca sesja nie działa na tym modelu, deleguj to zadanie do subagenta z `model: "fable"`.

## Źródło fraz kluczowych

Plik **`kanal/ranking_fraz_seo.csv`** — analiza SEO (wolumen wyszukań/mies., poziom konkurencji niska/średnia/wysoka, wynik ogólny) dla puli fraz kluczowych kanału. To jest teraz **jedyne** źródło fraz przy pisaniu opisu (zastępuje starszy `kanal/top-10-fraz-kluczowych.pdf`) — zawsze wczytać ten plik na nowo przy każdym Etapie 6, bo może być aktualizowany.

**Trzy stałe frazy otwierające (najwyższy wolumen przy niskiej konkurencji, zawsze w tej roli, niezależnie od aktualizacji pliku, chyba że użytkownik jawnie każe je zmienić):** „muzyka chrześcijańska", „piosenki religijne", „muzyka katolicka".

**Dalsze frazy do reszty opisu:** dobierać z pliku CSV frazy o **niskiej konkurencji i możliwie wysokim wolumenie** (kolumna KONKURENCJA = „niska"), tematycznie pasujące do treści danego psalmu — np. muzyka religijna polska, muzyka chrześcijańska z tekstem, polskie pieśni religijne, muzyka do modlitwy, muzyka religijna, muzyka chrześcijańska polska, najlepsza muzyka chrześcijańska, piosenka religijna, muzyka chrześcijańska uwielbienie (dokładna lista i wolumeny — zawsze z aktualnego CSV, nie z pamięci).

**Proporcja konkurencji w całym opisie (opis + tagi łącznie):** ok. **80% użytych fraz z pulą niskiej konkurencji**, ok. **20% ze średniej/wysokiej konkurencji** (np. psalmy śpiewane, modlitwa śpiewana, pieśni chrześcijańskie, psalm — świadomie, bo mimo wyższej konkurencji są tożsamościowe dla kanału lub mają bardzo wysoki wolumen).

## Format opisu (w tej kolejności)

0. **Pierwsze zdanie zawsze wprost mówi, jakiego psalmu dotyczy film** (np. „Psalm X śpiewany po polsku…") — zanim jeszcze wejdą frazy SEO, widz/algorytm ma jasność, o który psalm chodzi.
1. **Akapit SEO (pierwsze ~150 znaków to najważniejsza część opisu):** zdanie o psalmie (patrz pkt 0) + w **pierwszych dwóch zdaniach** obowiązkowo wszystkie **trzy stałe frazy otwierające** („muzyka chrześcijańska", „piosenki religijne", „muzyka katolicka"), wplecione naturalnie — bez wyliczanki.
2. **Akapit 2:** krótki opis aranżacji i teledysku, z kolejnymi frazami niskiej konkurencji z `ranking_fraz_seo.csv` (dopasowanymi tematycznie do psalmu) wplecionymi naturalnie.
3. **Akapit 3 — kontekst/treść psalmu (decyzja użytkownika, 2026-07, wzorzec: Psalm 19, Psalm 46):** dłuższy akapit przybliżający treść i przesłanie samego psalmu — skąd/z jakich okoliczności pochodzi (jeśli to coś wnosi), jego główny obraz/wezwanie (najlepiej z bezpośrednim cytatem z tekstu pieśni), do kogo psalm jest kierowany (jaki stan/sytuacja życiowa) i kiedy/w jakich okolicznościach warto go słuchać (modlitwa poranna, przed trudną decyzją, wieczorem, w kryzysie itd.). To akapit „dla czytającego do końca", pogłębiający, nie tylko SEO.
4. **🔔 Krótkie CTA subskrypcji + 🎧 link do playlisty „Psalmy śpiewane"** (dwie linijki, jedna pod drugą, nad tekstem pieśni — łapią czytających tylko górę opisu). Link subskrypcji: `https://www.youtube.com/@swieta-muzyka?sub_confirmation=1` (otwiera okno subskrypcji). Playlista wydłuża sesję widza w obrębie kanału — silny sygnał dla browse. Kanał projektu: https://www.youtube.com/@swieta-muzyka | Playlista „Psalmy śpiewane": https://www.youtube.com/playlist?list=PLx3JbKsW_a05aXyvEW1BSj1Ek3tMBE0UA
5. **🎵 TEKST PIEŚNI** — pełny tekst parafrazy (każda linijka staje się frazą wyszukiwalną).
6. **▶ POSŁUCHAJ TAKŻE** — linki do pozostałych psalmów kanału. Źródło linków: plik `instrukcje/baza-linków.md` — za każdym razem przy tworzeniu opisu wstawiać stamtąd 3 linki do już opublikowanych filmów (jeśli opublikowanych filmów jest więcej niż 3, wybrać najbardziej pasujące tematycznie lub najnowsze). Jeśli film, do którego linkujemy, jeszcze nie jest opublikowany, wstawić „[LINK - uzupełnij po publikacji]". Po publikacji nowego filmu: dopisać jego link do `baza-linków.md` oraz zaktualizować „[LINK - uzupełnij po publikacji]" na realny link we wszystkich starszych opisach, które go referencjonują.
7. **Blurb kanału** + cytat „Śpiewajcie Panu pieśń nową" (Ps 96,1).
8. **3–5 hashtagów.** Nigdy nie używać `#modlitwa`.

**Uwaga (2026-07, decyzja użytkownika): nie dodawać już informacji o napisach/CC do opisu** — usunięto z formatu (dawny punkt 5).

## Przypięty komentarz

W `opis.txt` zawsze dwie propozycje angażującego przypiętego komentarza (pytanie o doświadczenie widza, prośba o proste słowo-odpowiedź typu „Amen", zachęta do podzielenia się filmem) — po publikacji wybrać jeden i przypiąć.

## Tagi — podział na domyślne i indywidualne

W YouTube Studio (Ustawienia → Ustawienia domyślne przesyłania → Tagi) ustawiony jest na stałe zestaw domyślny, który wgrywa się automatycznie przy każdym uploadzie:

```
modlitwa śpiewana, muzyka chrześcijańska, muzyka chrześcijańska polska, muzyka chrześcijańska uwielbienie, muzyka chrześcijańska z tekstem, muzyka do modlitwy, muzyka katolicka, muzyka religijna, muzyka religijna polska, najlepsza muzyka chrześcijańska, pieśni chrześcijańskie, pieśni katolickie, pieśni religijne, pieśni uwielbienia, piosenka religijna, piosenki religijne, polskie pieśni religijne, psalm, psalm śpiewany, psalmy śpiewane
```

**Ten zestaw pokrywa już niemal wszystkie ogólne frazy z `kanal/ranking_fraz_seo.csv`** (niskiej, średniej i wysokiej konkurencji) — więc żadnej z powyższych 20 fraz **nie powielamy** w tagach indywidualnych `opis.txt`. Sekcja tagów w `opis.txt` zawiera więc **tylko tagi indywidualne filmu**, czyli te, których nie ma na powyższej liście: numer psalmu (np. „psalm 90"), „psalm X śpiewany", incipit/cytat z pieśni, motyw przewodni/tematyczny danego psalmu — z adnotacją, że dopisuje się je przy uploadzie do już wgranych domyślnych. Suma domyślne+indywidualne ≤ 500 znaków (domyślne zajmują ~280, zapas ~220). W upload defaults warto mieć też domyślny opis (blurb kanału + cytat Ps 96), kategorię Muzyka i język polski — wtedy przy publikacji dokleja się nad nim tylko akapit SEO i tekst pieśni.

**Tagi indywidualne — skład (5-8 sztuk):** ponieważ ogólne frazy z `ranking_fraz_seo.csv` są już pokryte przez zestaw domyślny powyżej, tagi indywidualne budujemy **wyłącznie z rzeczy specyficznych dla aktualnego psalmu** — numer psalmu, „psalm X śpiewany", incipit/cytat, motyw przewodni. Proporcja 80% niska / 20% średnia-wysoka konkurencja (patrz „Źródło fraz kluczowych" wyżej) dotyczy fraz ogólnych **w treści opisu** (akapity SEO), nie tagów indywidualnych — tam nie ma już miejsca na ogólne frazy, bo się dublowałyby z domyślnymi.

## Tytuł i miniatura — podział ról (optymalizacja pod browse)

W browse widz zawsze widzi miniaturę i tytuł razem, więc nie powtarzają one tej samej informacji:

- **Miniatura**: duży napis „PSALM X śpiewany" — identyfikacja i marka serii.
- **Tytuł, wzorzec obowiązujący od 2026-07-30** (ustalony na danych kanału po 3 tygodniach; zastępuje wcześniejszy „[hak] (Psalm X)" z numerem w nawiasie na końcu):

  ```
  Psalm X - [hak sytuacyjny] | Psalm X śpiewany
  ```

  np. `Psalm 91 - Gdy boisz się o tych, których kochasz | Psalm 91 śpiewany`.
- **Opis, pierwsza linia**: frazy pod wyszukiwarkę (np. „Psalm 91 śpiewany po polsku - muzyka chrześcijańska") — pracują dla algorytmu, widz czyta je dopiero po kliknięciu.

### Reguły wzorca

1. **Fraza szukalna NIE idzie na początek tytułu.** Ruch kanału przychodzi z browse, a nie z wyszukiwarki, więc tytuł pracuje jako podpis obok miniatury, nie jako ciąg do dopasowania. Miniatura i tak niesie „Psalm X śpiewany" wielkimi literami - powtarzanie tego w widocznej części tytułu zjadałoby znaki na drugą kopię tej samej informacji.
2. **Widoczne okno to część przed pionową kreską: 40-52 znaki.** Na telefonie tytuł urywa się koło pięćdziesiątki, więc hak musi się zmieścić w całości. Cała długość z ogonem: do ~75 znaków.
3. **Ogon zawsze z numerem** - `| Psalm 91 śpiewany`, nie `| Psalm śpiewany`. Dokładnie tę frazę ludzie wpisują, a numer tuż przy słowie „śpiewany" daje dopasowanie całego wyrażenia. Na telefonie ogon i tak się nie wyświetla, więc nic nie kosztuje. **Tekst z miniatury NIE liczy się do indeksowania** - fraza musi być w tytule albo w opisie; samo umieszczenie jej na obrazku nie daje w wyszukiwarce nic.
4. **Hak nazywa sytuację widza, nie cytuje incipitu.** W kohorcie z 2. tygodnia kanału tytuły sytuacyjne biły incipitowe: „Gdzie schronić serce, gdy czas ucieka?" - 134 wyświetlenia, „Oto dzień, który Pan uczynił" - 52. Przesłanka słabsza niż hipoteza o długości utworu (pięć filmów, splątane z długością), ale kierunek zgodny z profilem odbiorcy.
5. **Rotować konstrukcje haka.** Na stronie kanału widać kilkanaście tytułów naraz i seria zbudowana w całości z „Gdy…" czyta się jak generator, a nie jak seria. Proporcja z przebudowy katalogu 2026-07-30: 7 × „Gdy", 2 × „Kiedy", 4 zdania oznajmujące, 1 pytanie.
6. **Bez wersalików i bez wyliczanki keywordów** w widocznej części.

Zasada żelazna: numer psalmu stoi teraz i na początku tytułu, i w ogonie, więc identyfikacja jest spełniona niezależnie od miniatury.

**Kiedy ten wzorzec zrewidować:** co jakiś czas sprawdzić Studio → Źródła ruchu. Jeśli udział „YouTube search" zacznie wyraźnie rosnąć (materiał evergreen z czasem to robi), warto przetestować frazę szukalną z przodu. Zmiana tytułu opublikowanego filmu niczym nie grozi.

**Czego nie ruszać:** haków filmów o wyraźnie najlepszych wynikach. Przy przebudowie katalogu 2026-07-30 haki Psalmu 100 („W dobre ręce Pasterza", 277 wyświetleń) i Psalmu 90 („Gdzie schronić serce, gdy czas ucieka?", 134) zostały nietknięte - zmienił się w nich tylko ogon.

## Zawsze wymyślić przynajmniej DZIESIĘĆ propozycji tytułów i ułożyć je w ranking

Zanim wybierzemy finalne tytuły, wygenerować **min. 10 propozycji** (różne haki: cytat z pieśni, moment życia, obietnica doświadczenia, motyw przewodni psalmu itd.), a następnie **ułożyć całą pulę w ranking malejący wg przewidywanego CTR** — miejsce 1. to tytuł-pretendent do najwyższego CTR, kolejne miejsca (2., 3. ... 10.) to propozycje o coraz mniejszym przewidywanym potencjale.

Z tego rankingu:

1. **Tytuł główny** — pozycja 1. rankingu (z nim publikujemy).
2. **Tytuł zapasowy** — pozycja 2. rankingu, w innym stylu haka, do podmiany po ~2 tygodniach, jeśli CTR tytułu głównego jest niski (poniżej ~3–4% w Studio → podmieniamy; powyżej ~6% → nie ruszamy).

Cały ranking (wszystkie 10 pozycji, w kolejności malejącej) zapisywany w `opis.txt` w sekcji „Ranking propozycji tytułów" — tytuł główny i zapasowy oznaczone jawnie, a pozostałe pozycje 3.–10. zostają pod ręką: gdyby oba wybrane tytuły trzeba było kiedyś zamienić na inny hak, bierzemy kolejny z rankingu (wg malejącego potencjału), a nie losowy z puli.

## Dopasowanie tytułu do kadru miniatury (kierunek odwrotny niż mogłoby się wydawać)

**Kadr na miniaturę jest już ustalony wcześniej, w Etapie 3** (sekcja „Miniatura — wybór kadru" w `prompty.md`) — Etap 6 go nie wybiera ani nie rekomenduje. Przy generowaniu propozycji tytułów sprawdzić, który kadr Etap 3 wskazał jako bazę miniatury (adnotacja „baza miniatury" w `prompty.md`), i przy doborze haka do tytułu głównego brać pod uwagę motyw tego kadru — silniejsza konotacja tytuł-obraz działa lepiej w browse. Nie jest to jednak twardy wymóg: jeśli najlepszy hak tytułowy nie pasuje tematycznie do ustalonego kadru miniatury, tytuł i tak wygrywa (kadr miniatury i tytuł nie muszą się dosłownie pokrywać, wystarczy że nie kłócą się ze sobą).

## Neutralność płciowa w tytułach

Tytuły (główny i pretendent) muszą pasować zarówno do widza, jak i widzki — unikać form osobowych nacechowanych rodzajem (przymiotniki/imiesłowy typu „samotny", „niezrozumiany", czasowniki w czasie przeszłym typu „czułeś/czułaś"). Zamiast przymiotnika/imiesłowu użyć rzeczownika lub przeformułować zdanie w stronę bezosobową/rzeczownikową.

Przykład: zamiast „Gdy czujesz się samotny i niezrozumiany (Psalm 139)" → „Gdy czujesz samotność i brak zrozumienia (Psalm 139)".

**Najczęstsza wpadka: słowo „sam".** Wchodzi do zdania niepostrzeżenie, bo brzmi jak wzmocnienie, a nie jak forma rodzajowa - i przeszło przez pierwszą wersję dwóch tytułów z przebudowy 2026-07-30:

- „Nawet w ciemnej dolinie nie jesteś sam" → „Nawet w ciemnej dolinie ktoś idzie obok"
- „Kiedy sam sobie nie umiesz wybaczyć" → „Kiedy nie umiesz wybaczyć sobie"

Przy każdym haku przeczytaj go na końcu tak, jakby czytała go kobieta. To wyłapuje „sam", „gotowy", „zmęczony", „czułeś" szybciej niż szukanie ich z listy.

## Interpunkcja

W tytułach i opisach **nie używać znaku „—" (długiej pauzy)** — zamiast niego zawsze zwykły łącznik „-".
