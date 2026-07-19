---
name: etap
description: This skill should be used when the user asks to "przejdź do etapu N", "zrób etap N dla Psalmu X", "wykonaj etap N", or otherwise names a production-stage number (1-7) for a specific psalm song in the Święta Muzyka pipeline.
argument-hint: "<numer etapu 1-7> <numer psalmu>"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Agent
  - AskUserQuestion
---

# Etap produkcji Święta Muzyka

Wykonać jeden z siedmiu etapów produkcji teledysku dla wskazanego psalmu, zgodnie z `CLAUDE.md` i `instrukcje/`.

## 1. Wyciągnąć parametry

Z `$ARGUMENTS` wyciągnąć numer etapu (1-7) i numer psalmu — akceptować zarówno skrótową formę ("2 91"), jak i naturalny język ("etap 2 dla Psalmu 91", "przejdź do etapu 5 Psalmu 27"). Jeśli którykolwiek z nich jest niejednoznaczny lub brakuje go, zapytać użytkownika (`AskUserQuestion`) zamiast zgadywać.

## 2. Zmapować numer etapu na plik instrukcji

| Etap | Plik |
|---|---|
| 1 | `instrukcje/etap1-lyrics.md` |
| 2 | `instrukcje/etap2-napisy.md` |
| 3 | `instrukcje/etap3-prompty-stylu.md` |
| 4 | `instrukcje/etap4-generowanie-obrazkow.md` |
| 5 | `instrukcje/etap5-obrobka-obrazkow.md` |
| 6 | `instrukcje/etap6-opis.md` |
| 7 | `instrukcje/etap7-miniatura.md` |

Wczytać wskazany plik. Reguły wspólne (docelowa rozdzielczość 2560×1440 16:9, struktura katalogów, zasady współpracy) są już w `CLAUDE.md` — w razie wątpliwości sprawdzić `instrukcje/styl-teledysku.md`.

## 3. Znaleźć folder psalmu

Folder nie nazywa się dokładnie `psalm N` — ma zmienny suffiks statusu: `psalm N - in progress - <cyfra>` albo `psalm N - done`. Dopasować przez `ls` / glob `psalm N*` w katalogu głównym repo.

Wyjątek: dla **Etapu 1** folder może jeszcze nie istnieć — to oczekiwane, bo folder i sześć podfolderów (`images/`, `audio/`, `prompts/`, `txt/`, `render/`, `wideo/`) zakłada się **dopiero zaraz po** Etapie 1, po zapisaniu `lirycs.txt`.

Jeśli dla etapu 2-7 folder nie istnieje, zatrzymać się i zgłosić to użytkownikowi zamiast go tworzyć samodzielnie.

## 4. Warunki wstępne konkretnych etapów

- **Etap 2** (napisy) wymaga, żeby w `audio/` był już plik audio. Jeśli go nie ma — zatrzymać się i zgłosić brak, nie zaczynać etapu.
- **Etap 3** (prompty) wymaga, żeby w `audio/` był już plik audio ORAZ żeby `txt/napisy.srt` (Etap 2) był już gotowy — jego dokładne znaczniki czasowe napędzają rozpisanie kadrów. Jeśli któregoś z nich brakuje — zatrzymać się i zgłosić brak, nie zaczynać etapu. Jeśli użytkownik poprosi o Etap 3, a Etap 2 jeszcze nie został wykonany, zapytać, czy najpierw wykonać Etap 2.
- **Etap 7** buduje miniaturę na bazie pierwszej klatki filmu w `wideo/` — jeśli tam nic nie ma, zgłosić brak zamiast kontynuować.

## 5. Reguła modelu (Etapy 1, 2, 3)

Te trzy etapy muszą być wykonane modelem **Opus**, w trybie **Thinking**, z effortem **high**. Jeśli bieżąca sesja już na tych parametrach działa — wykonać etap bezpośrednio. Jeśli nie — delegować wykonanie do subagenta (`Agent`, `model: "opus"`) przekazując mu: numer psalmu, ścieżkę do folderu, pełną treść wczytanego pliku `instrukcje/etapN-*.md`, oraz (dla etapu 2 i 3) treść pliku audio / `napisy.srt` i informację o jego długości i strukturze.

## 6. Wykonać etap

Zgodnie z wczytanym plikiem `instrukcje/etapN-*.md`, zapisać wynik w odpowiednim podfolderze wg typu pliku (nie etapu) — patrz `styl-teledysku.md` § "Struktura katalogów w folderze utworu":

- Etap 1 → `txt/lirycs.txt` (plus stworzenie sześciu podfolderów, patrz punkt 3)
- Etap 2 → `txt/napisy.srt`
- Etap 3 → `prompts/prompty.md`
- Etap 4 → `images/` (surowe pliki numerowane)
- Etap 5 → `images/` (te same pliki, po przycięciu/konwersji/zmianie nazwy)
- Etap 6 → `txt/opis.txt`
- Etap 7 → `images/` (miniatura) + `wideo/` (nazwa pliku eksportu musi zgadzać się z miniaturą)

## 7. Po zakończeniu etapu

Zmienić nazwę folderu na `psalm N - in progress - <cyfra>`, gdzie `<cyfra>` to numer właśnie ukończonego etapu (nadpisując poprzednią cyfrę, jeśli była). Nie zmieniać statusu na `- done` automatycznie nawet po Etapie 7 — to wymaga osobnego potwierdzenia użytkownika i aktualizacji `instrukcje/lista-psalmow.md`.

## 8. Zasady współpracy

Jeśli przy okazji etapu widać coś spoza zakresu, co warto poprawić (inny plik, inny psalm, starszy wpis) — nie ruszać tego samodzielnie. Zapytać użytkownika (`AskUserQuestion`) i poczekać na zgodę.
