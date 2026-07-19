# Etap 4 — Generowanie obrazków przez Leonardo AI

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 4 (generowanie plików obrazków z promptów przygotowanych w Etapie 3). Rozdzielczość docelowa: patrz `styl-teledysku.md` → „Rozdzielczość docelowa" — to jedno miejsce, obowiązuje też przy Etapie 3, Etapie 5 i Etapie 7.

**Cel etapu:** z promptów przygotowanych w Etapie 3 (`prompts/prompty.md` lub `prompty-opus.md`) wygenerować faktyczne pliki obrazków, kadr po kadrze, i zapisać je w podfolderze `images/` pod prostymi nazwami numerycznymi (np. `7.jpg`) — dopiero Etap 5 zmienia te nazwy na znaczniki czasowe i kadruje do 16:9.

**Model Claude: Haiku, effort low.** Same obrazki generuje Leonardo AI (model Phoenix 1.0, patrz niżej) — rola modelu Claude to tylko uruchomienie skryptu i odczytanie kosztu, więc nie potrzeba mocnego modelu.

## Narzędzie: Leonardo AI REST API bezpośrednio z Claude Code

Generowanie odbywa się przez API Leonardo, **bez wchodzenia w przeglądarkę** — skrypt `instrukcje/skrypty/generuj_obrazki_phoenix.py`. Model: **Phoenix 1.0**.

Wymagany klucz API w zmiennej środowiskowej `LEONARDO_API_KEY` — użytkownik podaje go na początku sesji; **nigdy nie zapisywać go w żadnym pliku repo**. Rozliczenie API jest osobne od planu web (Essential, $12/mies.) — płatność PAYG, koszt rzędu pojedynczych groszy za kadr.

**Po każdej generacji (i każdym upscale) podawać użytkownikowi koszt przeliczony na złote** — skrypt sam wypisuje `koszt: $X (~Y zł)` (stała `USD_TO_PLN` w skrypcie, aktualizować w razie wyraźnego dryfu kursu).

## Ustalony tryb domyślny: standard, Full HD, 15 kroków

Poniższe ustawienia to **potwierdzony wybór użytkownika** po porównaniu wariantów, nie tylko doraźna oszczędność — trzymać się ich jako domyślnych, chyba że użytkownik poprosi inaczej:

- Tryb **`--standard`** (bez Ultra). Ultra generuje w wyższej rozdzielczości (auto-podbicie 2×, np. 1920×1080 → 3840×2160), ale różnica jakości okazała się nie być warta dodatkowego kosztu/wagi pliku po przetestowaniu obu wariantów.
- Rozdzielczość **1920×1080 (Full HD)** — API Leonardo odrzuca żądania szersze niż 1920 px, więc to naturalny sufit trybu standard.
- **15 kroków dyfuzji (wartość domyślna skryptu, nie podawać `--steps`)** — testowano też 10 kroków (flaga `--steps 10`), ale cena wyszła identyczna, więc przy tej samej cenie zostajemy przy jakości domyślnych 15 kroków.
- **Jeden obraz na kadr** — bez generowania kilku wariantów do selekcji (zmiana wprowadzona celowo, żeby ograniczyć koszt).

## Jak wywołać (jeden kadr na raz)

```
export LEONARDO_API_KEY="..."
python3 instrukcje/skrypty/generuj_obrazki_phoenix.py --standard --raw "<pełny prompt kadru z prompty.md/prompty-opus.md>" "psalm N/images" <numer_kadru>
```

- `--raw` + pełny, gotowy tekst promptu wprost z pliku promptów danego psalmu — każdy kadr ma własny wariant palety wg łuku kolorystycznego, więc nie przepuszczać przez generyczny prefiks stylu wbudowany w skrypt (ten prefiks jest tylko dla szybkich, doraźnych opisów scen bez `--raw`).
- Nazwa pliku wyjściowego = sam numer kadru (np. `7.jpg`).
- Generować **kadr po kadrze**, nie całą serię naraz — po każdym sprawdzić wynik (podgląd obrazu) pod kątem zgodności ze stylem i treścią (twarze niewidoczne, brak zwykłych ludzi, liczba postaci/skrzydeł zgodna z promptem — np. jeśli postać ma mieć skrzydła, to dwa, nie jedno) i dopiero potem przejść do kolejnego kadru.

## Jeśli dany kadr musi trzymać min. 2K

Tryb standard daje 1920×1080, poniżej progu 2K (2560×1440). Gdy konkretny kadr **musi** trzymać 2K, dogrywamy go osobnym, tanim upscale zamiast przełączać generację całego kadru na Ultra:

```
python3 instrukcje/skrypty/generuj_obrazki_phoenix.py --upscale <generatedImageId> <plik_wyjsciowy.jpg> 1.34
```

`generatedImageId` skrypt wypisuje po każdej generacji. Mnożnik 1,34 to minimalne powiększenie z 1920×1080 do ~2560×1440 (najtańsza opcja spełniająca próg) — inne mnożniki też działają (np. 2 → 3840×2160, jak przy Ultra), ale zostawiamy minimalny, żeby nie płacić za rozdzielczość, która nie jest potrzebna.

## Selekcja i poprawki

Jeśli wynik nie pasuje do promptu (dodatkowa postać, zła liczba skrzydeł, widoczna twarz, brakujący element wymieniony w promptcie) — **nie akceptować automatycznie**: opisać różnicę użytkownikowi i zapytać, czy generować ponownie z doprecyzowanym promptem, czy zostawić jak jest. Nie jest to jeszcze etap „bez oceny treści" (to dopiero Etap 5) — tutaj ocena zgodności z promptem jak najbardziej należy do procesu.
