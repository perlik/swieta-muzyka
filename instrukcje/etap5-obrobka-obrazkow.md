# Etap 5 — Obrabianie obrazków

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 5 (obrabianie wygenerowanych obrazków). Rozdzielczość docelowa: patrz `styl-teledysku.md` → „Rozdzielczość docelowa" — to jedno miejsce, obowiązuje też przy Etapie 3, Etapie 4 i Etapie 7.

**Cel etapu:** po wgraniu wygenerowanych plików do podfolderu `images/` — zmiana nazw na znaczniki czasowe, kadrowanie do 16:9 (przycięcie do proporcji, **bez zmniejszania rozdzielczości** — zachowujemy natywną rozdzielczość źródła) i konwersja wg zasad jakości (q100, 4:4:4, bez upscalingu poniżej 2K). Pliki nadpisywane w `images/`; zbędne wersje do podfolderu `images/_do_usuniecia`.

**Model Claude: Haiku, effort low.** Czysto mechaniczne rename/crop/convert — nie wymaga mocnego modelu.

## Format nazwy pliku (zakres czasowy, nie pojedynczy znacznik)

Każdy plik nazywamy zakresem **początek-koniec kadru**, wzorem `0m00s-0m18s.jpg` (minuty i sekundy dwucyfrowe, litera `m`/`s` jako separator, myślnik między początkiem a końcem) — zgodnie z konwencją już użytą w opublikowanych filmach (`kanal/done/psalm N - done/images/`) i wymaganą przez szablon FCPXML (`instrukcje/skrypty/Psalm27_Timeline.fcpxml`). **Nie** nazywać pliku samym znacznikiem startu (błąd popełniony przy Psalmie 121 pierwszy raz — poprawiony).

## Bez oceny treści

Etap 4 to wyłącznie techniczne przetworzenie plików tak, jak opisano poniżej (nazwy, kadrowanie, konwersja) — **nie analizujemy**, czy obrazki są poprawnie wygenerowane, czy stylistycznie zgodne z instrukcją, ani czy odpowiadają treści danej linijki psalmu z `prompty.md`/`lirycs.txt`. Taka ocena nie jest częścią tego etapu i nie wykonujemy jej, chyba że użytkownik wyraźnie o nią poprosi.

## Zasada kadrowania (zawsze)

Każdy kadr konwertujemy do proporcji **16:9** przycięciem centralnym (docinamy tylko nadmiar z boków lub góry/dołu) — **nigdy nie skalujemy w dół**.

- Jeśli źródło ≥ 2560×1440 → tylko przycinamy, zachowując natywną rozdzielczość.
- Jeśli źródło < 2560×1440 → nie skalujemy w górę (zostawiamy natywną rozdzielczość, przycinając do 16:9; warto wcześniej podbić w Leonardo Upscale).

Zapis JPEG quality 100, bez podpróbkowania chromy (4:4:4), tryb progresywny, konwersja ze świeżego oryginału.
