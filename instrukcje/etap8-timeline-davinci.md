# Etap 8 — Oś czasu do DaVinci Resolve

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 8 (przygotowanie edytowalnej osi czasu do montażu w darmowej wersji DaVinci Resolve). Wykonywany po Etapie 5 (obrabianie obrazków) — wymaga gotowych, przyciętych i nazwanych wg znaczników czasu plików w `images/`.

**Cel etapu:** wygenerować plik osi czasu, który DaVinci Resolve zaimportuje jako **w pełni edytowalną** sekwencję — z klipami rozmieszczonymi na osi dokładnie wg nazw plików z Etapu 5, możliwymi do trimowania i łączenia przejściami (nie zablokowanymi), w rozdzielczości sekwencji 2560×1440, **z gotowym ruchem kadru typu Ken Burns wypieczonym w klatki kluczowe**. Wynik: `timeline_edytowalny_fcp7.xml` w podfolderze `render/`.

**Model Claude: Sonnet lub mocniejszy** (zmiana z 2026-08-01). Samo generowanie XML jest mechaniczne, ale etap obejmuje też **obejrzenie wszystkich kadrów i ustalenie stron ruchu** (patrz „Plik kierunków ruchu" niżej) — to ocena kompozycji, której Haiku nie wykona rzetelnie. Wcześniejsza adnotacja „Haiku, effort low" była prawdziwa dopiero dla wersji bez ruchu kadru.

## Warunek wstępny

Etap 5 musi być ukończony: pliki nazwane pełnym zakresem czasu, np. `0m17s-0m32s.jpg` (wzorzec `\d+m\d+s-\d+m\d+s`). Skrypt czyta obrazki z podanego katalogu, ale to jedyne, czego stamtąd potrzebuje — same pliki obrazków tam zostają, tylko wynikowy plik timeline ląduje w `render/` (bo to plik projektu montażowego, nie grafika). Pliki bez znacznika czasu w nazwie (miniatura, `thumb.png`) są pomijane i wypisywane na `stderr`.

## Problem, który ten etap rozwiązuje

Naiwne wygenerowanie FCPXML z elementami `<asset-clip>` importuje się do Resolve poprawnie, ale klipy wychodzą **zablokowane** — nie da się trimować krawędzi ani nakładać przejść, bo `<asset-clip>` przypina klip do sztywnej długości assetu (obrazek statyczny nie ma żadnego zapasu/handles). Dlatego generujemy legacy Final Cut Pro 7 XML (XMEML v5), gdzie każdy still ma masterclip dłuższy o `--handle` sekund z każdej strony, a na oś wchodzi tylko środkowy wycinek przez `<in>`/`<out>`.

## Ruch kadru (Ken Burns)

**Dynamic Zoom nie przechodzi przez XML.** To funkcja wyłącznie Resolve'a — nie ma dla niej miejsca ani w FCP7 XMEML, ani w FCPXML, więc żaden import nie zapali przełącznika DZ ani nie ustawi zielonej/czerwonej ramki. Nie ma sensu tego szukać.

Przechodzi za to **ten sam ruch** zapisany jako klatki kluczowe filtra `Basic Motion` (`effectid: basic`, kategoria `motion`). Resolve wczytuje je jako **Transform → Zoom / Position** z keyframe'ami i na ekranie wychodzi dokładnie to, co dawał DZ. Dla montażysty różnica jest taka, że ruch siedzi w sekcji Transform, przełącznik Dynamic Zoom zostaje wyłączony, a poprawia się go tak samo — przesuwając klatki kluczowe albo zmieniając wartość Zoom.

Metoda przeniesiona z projektu „Holy Creator" (`/Volumes/ADATA SE880/Holy Creator/docs/timeline-davinci-fcp7-xml.md`), gdzie jest sprawdzona na kilkudziesięciu filmach. Cztery rzeczy, które w niej naprawdę mają znaczenie:

1. **Wygładzenie wypieczone w klatki.** Nie licz na to, że importer uszanuje flagi interpolacji — krzywa `smoothstep` (3t² - 2t³) jest próbkowana do `--zoom-klatek` (domyślnie 25) klatek kluczowych, więc „Ease In and Out" przeżywa import niezależnie od wersji Resolve'a. Im większy zakres ruchu, tym gęściej trzeba próbkować: Resolve interpoluje między keyframe'ami liniowo, więc przy zoomie 25% i 9 klatkach widać skokową zmianę prędkości.
2. **Kierunek zmienia się co kadr** (najazd / odjazd na przemian). Gdyby wszystkie kadry jechały w tę samą stronę, po kilku minutach widz widzi mechanikę.
3. **Wielkość najazdu skaluje się długością kadru** (`--zoom-ref`, domyślnie 12 s). Stała wartość daje ruch o tempie odwrotnie proporcjonalnym do długości ujęcia: te same 25% to 2,1%/s na kadrze 12-sekundowym (spokojnie) i 6,3%/s na 4-sekundowym (szarpnięcie). Zoom liczony jest jako `zoom × długość / ref`, przycięty z góry do `--zoom` i z dołu do `--zoom-min`.
4. **Panorama sprzężona z zoomem, nie niezależna.** Przesunięcie w bok w każdej klatce to stały ułamek zapasu, jaki daje **aktualne** powiększenie, więc przy skali 100% wynosi dokładnie zero i **czarny pas przy krawędzi nie może wejść w kadr w żadnym momencie ruchu**. Znak jest odwrotny do intuicji: `center` przesuwa obraz, a nie okno kadru, więc motyw po lewej → `horiz` rośnie dodatnio.

**W tym projekcie ruch dostają wszystkie kadry.** W „Holy Creator" generator pomija karty tekstowe (najazd na kartę miękczy litery), ale u nas kart nie ma — napisy wchodzą jako SRT z Etapu 2, nie jako kadry.

### Plik kierunków ruchu (`kierunki-ruchu.tsv`) — OBOWIĄZKOWY

**Plik kierunków zakładamy przy każdym utworze, zawsze, przed wygenerowaniem osi czasu** (decyzja użytkownika 2026-08-01). Nie pytamy, czy go tworzyć, i nie zostawiamy wszystkich kadrów na „auto" — trzeba **obejrzeć każdy kadr** i wpisać stronę. Bez tego panorama jedzie na przemian niezależnie od kompozycji, czyli w połowie kadrów odjeżdża od motywu zamiast na niego najeżdżać.

**Strony nie da się wykryć automatycznie.** Na akwareli detal tła (rozświetlone niebo, aureola, brama światła przy krawędzi) bywa mocniejszy niż motyw główny, więc środek ciężkości kontrastu myli się o jakieś 40% kadrów. Plik `kierunki-ruchu.tsv` leży **obok obrazków** (w tym samym katalogu, który podajemy skryptowi). Format: `nazwa-pliku<TAB>lewo|prawo|auto`, `#` zaczyna komentarz:

```
0m00s-0m16s.jpg	prawo	# psalmistka przy prawej krawędzi kadru
2m18s-2m32s.jpg	lewo	# ścieżka wchodzi w kadr od lewej
3m27s-3m38s.jpg	auto	# abstrakcja symetryczna, nie ma na co jechać
```

`auto` używamy **świadomie**, nie z lenistwa: dla kompozycji symetrycznych i motywów dokładnie w centrum, gdzie nie ma na co jechać (snop światła na osi, symetryczne skrzydła, radialna abstrakcja). Takie kadry dostają strony na przemian. Wpisy `auto` warto opatrzyć komentarzem, dlaczego kadr jest symetryczny — inaczej po miesiącu nie widać, czy to decyzja, czy przeoczenie.

Orientacyjny rozkład z Psalmu 121 (29 kadrów): 7 `prawo`, 6 `lewo`, 16 `auto`. Jeśli w jakimś utworze wychodzi prawie samo `auto`, to znak, że kadry nie zostały obejrzane uważnie.

Jak wybierać stronę:

- **Motyw wyraźnie przy krawędzi** (lampa po prawej, dom po lewej, psalmistka przy prawej krawędzi) → ta strona.
- **Droga/ścieżka wchodząca w kadr z jednej strony albo zakręcająca** → strona, do której prowadzi.
- **Kadr finałowy** → strona, po której leży akcent wizualny; ruch w tę stronę zostawia środek i prawą część kadru czyste pod ekran końcowy YouTube.
- **Motyw w centrum albo kompozycja symetryczna** → `auto`.

To jedyny krok tego etapu wymagający oceny treści kadru — i jedyny, którego nie da się zautomatyzować.

**Po każdej zmianie audio** (nazwy plików niosą czas, więc się przeliczają) plik trzeba zaktualizować. Generator wypisuje ostrzeżenie o wpisach wskazujących nieistniejące kadry — to najczęstszy sygnał, że kierunki rozjechały się po zmianie długości nagrania.

## Skrypt i sposób użycia

Skrypt: `instrukcje/skrypty/generuj_timeline_edytowalny.py`. Ścieżki i parametry idą **argumentami z linii komend** — nie edytujemy już stałych w pliku.

Kolejność jest stała:

1. **Obejrzeć wszystkie kadry** i zapisać `kierunki-ruchu.tsv` obok obrazków (patrz wyżej — krok obowiązkowy).
2. Uruchomić skrypt:

```
python3 "instrukcje/skrypty/generuj_timeline_edytowalny.py" "psalm N/images" --name "Psalm N"
```

3. Sprawdzić w wypisie, że skrypt policzył wpisy z TSV (`pan: X w lewo, Y w prawo, Z na przemian (wg kierunki-ruchu.tsv)`). Komunikat `brak kierunki-ruchu.tsv obok kadrów` znaczy, że krok 1 wypadł albo plik leży w złym katalogu.

Plik wynikowy trafia domyślnie do `render/timeline_edytowalny_fcp7.xml` w folderze utworu — skrypt szuka istniejącego katalogu `render/` w katalogach nadrzędnych względem podanego `images/`, więc działa też, gdy kadry leżą w podfolderze (np. `images/v2/` przy drugiej wersji utworu).

| Parametr | Domyślnie | Znaczenie |
|---|---|---|
| `images` (pozycyjny) | — | katalog z kadrami po Etapie 5 |
| `--out` | `render/timeline_edytowalny_fcp7.xml` | plik wynikowy |
| `--fps` | 60 | timebase osi; **musi zgadzać się z projektem w Resolve** |
| `--name` | `Auto Timeline` | nazwa sekwencji widoczna w Resolve |
| `--handle` | 10 s | zapas materiału z każdej strony na trim i przejścia |
| `--width` / `--height` | 2560 / 1440 | rozdzielczość wpisywana do XML (nie czytana z plików) |
| `--zoom` | 25 (%) | maksymalny najazd, 100% → 125%; **`0` wyłącza cały ruch** |
| `--zoom-ref` | 12 s | długość kadru, przy której `--zoom` wchodzi w całości; `0` wyłącza skalowanie |
| `--zoom-min` | 6 (%) | podłoga najazdu dla krótkich kadrów |
| `--zoom-klatek` | 25 | ile klatek kluczowych próbkuje krzywą wygładzenia |
| `--pan` | 6 (%) | przesunięcie w bok w skrajnym punkcie, w % szerokości kadru; `0` zostawia sam zoom |
| `--przejscia` | 2.5 s | Cross Dissolve na każdym cięciu; `0` wyłącza |
| `--kierunki` | `<images>/kierunki-ruchu.tsv` | plik ze stronami ruchu |

Wartości 25% zoomu i 6% panu są przeniesione z „Holy Creator", gdzie ustalono je po odsłuchu gotowej osi — wcześniejsze 5-8% zoomu było na gotowym filmie praktycznie niewidoczne. `--pan` powyżej `zoom/4` daje ostrzeżenie, powyżej `zoom/2` skrypt przerywa (przesunięcie nie zmieściłoby się w zapasie i w kadrze pokazałby się czarny pas).

## Przejścia: Cross Dissolve 2,5 s na każdym cięciu

**Domyślnie skrypt wstawia przejścia — nie trzeba ich klikać w Resolve** (decyzja użytkownika 2026-08-01, długość 2,5 s). W XMEML idą jako `<transitionitem>` z `effectid: Cross Dissolve`, wstawiony w torze **między** dwoma `<clipitem>`, w kolejności czasowej. Przy 29 kadrach powstaje 28 przejść — pierwszy kadr nie ma czego przenikać na wejściu, ostatni na wyjściu.

**`alignment=center`, czyli przejście straddluje cięcie:** pierwsza połowa (1,25 s) bierze materiał z zapasu klipu wychodzącego, druga z zapasu wchodzącego. Dwa skutki, które warto znać:

- **Długość osi czasu się nie zmienia.** Przejścia nie wydłużają sekwencji, tylko nakładają kadry na siebie w okolicy cięcia — znaczniki czasowe z nazw plików zostają w mocy, a oś dalej kończy się dokładnie na końcu audio.
- **Potrzebny jest zapas.** `--handle` (domyślnie 10 s) musi być większy niż połowa przejścia. Przy 2,5 s margines jest ogromny, ale skrypt to sprawdza i przerywa, gdyby ktoś zszedł z zapasem.

`<start>`/`<end>` przejścia liczymy w klatkach **osi czasu** — inaczej niż `when` w klatkach kluczowych filtra ruchu, które idą w czasie **mediów** (bo klip ma uchwyty). Pomylenie tych dwóch układów to najłatwiejszy błąd w tym pliku.

**Limit długości przejścia:** kadr krótszy niż całe przejście zostałby przykryty z obu stron naraz, więc skrypt przerywa z listą takich kadrów. Przy naszych kadrach 10-20 s przejście 2,5 s zjada 1,25 s z każdego końca, czyli najkrótszy kadr (10 s) zostaje z 7,5 s czystego obrazu — bezpiecznie. Gdyby kiedyś pojawiła się potrzeba dłuższych przenikań, trzeba najpierw sprawdzić najkrótszy kadr w filmie.

Ruch kadru i przejścia współistnieją bez konfliktu: `<filter>` siedzi w `<clipitem>`, `<transitionitem>` jest osobnym elementem toru.

## Kontrola jakości — skrypt wypisuje, nie milczy

1. **Ciągłość osi** — kadry powinny kafelkować oś bez dziur i bez zakładek; oba przypadki lądują na `stderr` z czasami i nazwami plików. To wyłapuje błędy w nazwach z Etapu 5, nie w XML.
2. **Pominięte pliki** — obrazek bez znacznika czasu w nazwie albo z końcem przed początkiem, z podaniem powodu.
3. **Osierocone kierunki** — wpisy w TSV wskazujące na nieistniejące kadry.
4. **Statystyka ruchu** — zakres i mediana najazdu, ile kadrów siedzi przy suficie, ile przy podłodze, oraz tempo w %/s (min, max, mediana) zestawione z tempem odniesienia. Mediana wyraźnie odbiegająca od odniesienia znaczy, że rozkład długości kadrów w tym filmie nie pasuje do ustawionego `--zoom-ref`.
5. **Przejścia** — długość, liczba cięć i ile bierze z zapasu każdego sąsiada; przerwanie z listą kadrów krótszych niż przejście.
6. **Podsumowanie** — liczba kadrów, długość osi, rozdzielczość, fps, zapas, zoom, pan, przejścia.

## Import w Resolve

1. **File → Import → Timeline...** → wskazać `timeline_edytowalny_fcp7.xml`.
2. Jeśli klipy byłyby zablokowane: zaimportować najpierw same JPG-i przez **File → Import Media** do Media Pool, potem zaimportować XML z **odznaczoną** opcją „Automatically import source clips into media pool" — wtedy timeline linkuje do stilli już znanych Resolve.
3. **Jeśli klipy wchodzą jako Media Offline:** to zwykle ścieżka w `pathurl`, nie sam plik — patrz „Pułapki" na końcu (normalizacja NFC). Przed ponownym importem **usunąć z Media Pool starą, czerwoną wersję kadrów i starą oś czasu**, inaczej w projekcie zostaną duplikaty wskazujące na nierozwiązywalną ścieżkę. Ostatecznie zawsze działa **Relink Media**: prawy przycisk na offline'owym klipie → *Relink Selected Clips* → wskazać katalog z kadrami.
3. Po imporcie sprawdzić na 3-4 kadrach: czy Transform ma keyframe'y, czy w skrajnym punkcie ruchu nie wchodzi czarny pas przy krawędzi, czy panorama nie jest dwa razy mocniejsza niż zamawiana. Jednostki `center` w FCP7 to „1.0 = połowa szerokości kadru" i nie da się tego zweryfikować bez importu — gdyby dana wersja Resolve'a czytała to jako pełną szerokość, ruch wyjdzie dwa razy mocniejszy (nadal w zapasie kadru). Korygować wtedy parametrem `--pan`, nie przerabianiem skryptu.

Rozmieszczenie klipów na osi (offsety, długości) wynika wprost z nazw plików nadanych w Etapie 5 — ten etap nie podejmuje żadnych decyzji montażowych poza jedną: stronami panoramy w `kierunki-ruchu.tsv`, które wymagają obejrzenia kadrów.

## Pułapki, na które już wpadliśmy

- **FCPXML z `<asset-clip>`** — klipy zablokowane, brak trimu i przejść. Stąd FCP7 XMEML.
- **Szukanie Dynamic Zoom w XML** — tego tam nie ma i nie będzie. Basic Motion, keyframe'y.
- **Zdanie się na flagi interpolacji importera** — wypiec smoothstep w klatki.
- **Za rzadkie próbkowanie przy dużym zoomie** — liniowa interpolacja między keyframe'ami daje widoczne skoki prędkości.
- **Stały zoom niezależny od długości kadru** — krótkie ujęcia szarpią.
- **Pan liczony niezależnie od zoomu** — czarny pas przy krawędzi w początkowej fazie ruchu.
- **Automatyczne wykrywanie strony motywu** — myli się o ok. 40% kadrów.
- **Nieprocentowane ścieżki** ze spacjami i znakami spoza ASCII w `pathurl`.
- **Ścieżka w NFD zamiast NFC** — najbardziej podstępna z całej listy (Psalm 121, 2026-08-01). macOS zwraca nazwy plików w formie rozłożonej (`Ś` jako `S` + U+0301), więc bez normalizacji do NFC w `pathurl` ląduje `_S%CC%81wie%CC%A8ta%20Muzyka` zamiast `_%C5%9Awi%C4%99ta%20Muzyka`. Python otwiera oba warianty, więc sprawdzenie „czy plik istnieje" **przechodzi**, ale importer Resolve dopasowuje ścieżkę dosłownie i wszystkie klipy wchodzą jako **Media Offline**. Objaw rozpoznawczy: w Media Pool każdy kadr widnieje dwa razy — raz z podglądem (z `Import Media`) i raz na czerwono (z XML). Skrypt normalizuje teraz do NFC i przerywa, gdy forma NFC się nie otwiera.
- **Niezgodny `--fps`** — Resolve utworzy oś z podanym klatkażem, więc rozjazd z projektem montażowym rozsypie synchronizację z audio.
