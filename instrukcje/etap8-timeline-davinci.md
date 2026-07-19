# Etap 8 — Oś czasu do DaVinci Resolve

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 8 (przygotowanie edytowalnej osi czasu do montażu w darmowej wersji DaVinci Resolve). Wykonywany po Etapie 5 (obrabianie obrazków) — wymaga gotowych, przyciętych i nazwanych wg znaczników czasu plików w `images/`.

**Cel etapu:** wygenerować plik osi czasu, który DaVinci Resolve zaimportuje jako **w pełni edytowalną** sekwencję — z klipami rozmieszczonymi na osi dokładnie wg nazw plików z Etapu 5, ale możliwymi do trimowania i łączenia przejściami (nie zablokowanymi), w rozdzielczości sekwencji 2560×1440. Wynik: `timeline_edytowalny_fcp7.xml` w podfolderze `render/`.

**Model Claude: Haiku, effort low.** Skrypt wykonuje całą pracę mechanicznie — rola modelu to tylko ustawienie ścieżek/FPS w skrypcie i jego uruchomienie.

## Warunek wstępny

Etap 5 musi być ukończony: pliki w `images/` nazwane pełnym zakresem czasu, np. `0m17s-0m32s.jpg` (wzorzec `\d+m\d+s-\d+m\d+s`). Skrypt czyta obrazki z `images/`, ale to jedyne, czego stamtąd potrzebuje — same pliki obrazków tam zostają, tylko wynikowe pliki timeline lądują w `render/` (bo to pliki projektu montażowego, nie grafika).

## Problem, który ten etap rozwiązuje

Naiwne wygenerowanie FCPXML z elementami `<asset-clip>` importuje się do Resolve poprawnie, ale klipy wychodzą **zablokowane** — nie da się trimować krawędzi ani nakładać przejść, bo `<asset-clip>` przypina klip do sztywnej długości assetu (obrazek statyczny nie ma żadnego zapasu/handles).

## Skrypt i sposób użycia

Skrypt: `instrukcje/skrypty/generuj_timeline_edytowalny.py`.

1. Ustawić w skrypcie `FOLDER_PATH` (folder `images/` danego psalmu) i `FPS` (klatkaż audio/wideo utworu).
2. Uruchomić: `python3 "instrukcje/skrypty/generuj_timeline_edytowalny.py"`.
3. Skrypt generuje jeden plik wynikowy w `render/`: `timeline_edytowalny_fcp7.xml` — legacy Final Cut Pro 7 XML (XMEML v5), gdzie każdy still ma masterclip dłuższy niż użyty fragment (zapas `HANDLE_SEC`, domyślnie 10 s, z każdej strony), więc trim/przejścia mają z czego brać. Rozdzielczość sekwencji jest sztywno ustawiona na `TARGET_WIDTH`×`TARGET_HEIGHT` (2560×1440) w skrypcie, niezależnie od rzeczywistych wymiarów plików w `images/`.
4. W Resolve: **File → Import → Timeline...** → wskazać `timeline_edytowalny_fcp7.xml`.
5. Jeśli klipy nadal byłyby zablokowane: zaimportować najpierw same JPG-i przez **File → Import Media** do Media Pool, potem zaimportować XML z odznaczoną opcją „Automatically import source clips into media pool" — wtedy timeline linkuje do stilli już znanych Resolve.

Rozmieszczenie klipów na osi (offsety, długości) wynika wprost z nazw plików (znaczników czasu) nadanych w Etapie 5 — ten etap nie podejmuje żadnych decyzji montażowych, tylko mechanicznie przekłada strukturę plików na format osi czasu.
