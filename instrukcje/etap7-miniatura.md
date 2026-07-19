# Etap 7 — Miniatura

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 7 (miniatura).

**Cel etapu:** wygenerowanie pliku miniatury (1280×720) w podfolderze `images/`, na bazie kadru wskazanego w Etapie 3, z napisem „Psalm X" + „śpiewany". **Etap dotyczy wyłącznie tworzenia pliku miniatury** — nie obejmuje zmiany nazwy pliku wideo w `wideo/` ani żadnej innej operacji na pliku wideo (to osobna czynność, wykonywana przy eksporcie/publikacji, nie w ramach tego etapu).

**Model Claude: Haiku, effort low.** Cały wygląd realizuje skrypt (patrz niżej) — rola modelu to tylko uruchomienie go z właściwymi argumentami.

## Zasady

- **Kadr na miniaturę jest już ustalony w Etapie 3** — sprawdzić `prompts/prompty.md`, sekcję „Miniatura — wybór kadru" / adnotację „baza miniatury" przy jednym z nagłówków kadrów, i użyć dokładnie tego kadru. **Nie pytać użytkownika o wybór kadru** — decyzja zapadła w Etapie 3, ten etap ją tylko wykonuje. Jeśli z jakiegoś powodu Etap 3 nie wskazał żadnego kadru (np. `prompty.md` starszy niż ta reguła), wybrać samodzielnie najmocniejszy wizualnie kadr z serii — również bez pytania użytkownika — i kontynuować.
- **Mapowanie numeru kadru na plik:** po Etapie 5 pliki w `images/` są nazwane zakresami czasu (nie `N.jpg`), posortowane chronologicznie — kadr N z `prompty.md` odpowiada N-temu plikowi w kolejności czasowej (np. kadr 1 = najwcześniejszy zakres czasu, kadr 5 = piąty plik od początku).
- **Generowanie:** użyj gotowego skryptu `instrukcje/skrypty/generuj_miniature.py` (Pillow) zamiast pisać go od nowa za każdym razem — uruchom go bezpośrednio z plikiem wskazanym jako baza miniatury (patrz wyżej), numerem psalmu i ścieżką wyjściową (patrz docstring w pliku). Skrypt sam realizuje całą specyfikację wyglądu — napis „Psalm X" + „śpiewany" czytelny na mobile, ciemny półprzezroczysty panel w kolorze dopasowanym do dominującego odcienia kadru, blok po lewej stronie u dołu, czcionka Lora — nic z tego nie trzeba ręcznie liczyć ani pilnować; zapisuje od razu w 1280×720. Zmieniać stałe w skrypcie tylko wtedy, gdy użytkownik poprosi o inny wygląd.
- **Nazewnictwo pliku miniatury:** plik miniatury (`images/`) nazywa się **dokładnie tak jak tytuł główny filmu**, np. `Gdy strach nie daje zasnąć (Psalm 91).jpg` — przy uploadzie od razu wiadomo, który plik jest który, a YouTube podpowiada tytuł z nazwy pliku. **Ten etap nie zmienia nazwy pliku wideo w `wideo/`** — dopasowanie nazwy pliku wideo do tytułu (jeśli potrzebne) to osobna czynność przy eksporcie/publikacji, poza zakresem Etapu 7.
