# Etap 2 — Napisy

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 2 (synchronizacja napisów). Wykonywany zaraz po Etapie 1 (lyrics), przed Etapem 3 (prompty do obrazków) — jego wynik zasila rozpisanie kadrów w Etapie 3.

**Model: Sonnet, tryb Thinking WYŁĄCZONY, effort medium.** Transkrypcję i budowę pliku robi skrypt `whisper_napisy_raw.py` (OpenAI Whisper) — to zadanie mechaniczne. Rola modelu: skompresować audio w razie potrzeby, uruchomić skrypt, a na końcu ręcznie poprawić tekst przesłyszeń (patrz niżej).

**Cel etapu:** wygenerowanie pliku `napisy.srt` w podfolderze `txt/` — napisy CC zsynchronizowane z audio, indeksowane przez wyszukiwarkę YouTube i poprawiające dostępność. (Jeśli w folderze istnieje już starszy `napisy.srt`, którego nie chcemy nadpisywać, nowy plik zapisujemy z sufiksem, np. `napisy_v2.srt` — tak jak przy Psalmie 19.) Wynik tego etapu (dokładne znaczniki czasowe per-linijka) jest potem podstawą rozpisania kadrów w Etapie 3 — patrz `etap3-prompty-stylu.md`.

## Źródło audio — pełny miks `audio.wav`

Synchronizację robimy na **pełnym miksie `audio/audio.wav`** (nie na izolowanym wokalu). Jeśli plik przekracza limit API OpenAI (**25 MB**), najpierw skompresować go do mp3 — to jedyny cel kompresji, jakość mp3 w zupełności wystarcza Whisperowi:

```
ffmpeg -i "audio/audio.wav" -codec:a libmp3lame -qscale:a 4 /ścieżka/tymczasowa/audio.mp3
```

Plik tymczasowy mp3 kasujemy po wygenerowaniu napisów.

## Metoda — napisy budowane WYŁĄCZNIE z odpowiedzi Whisper (bez dopasowania do `lirycs.txt`)

Skrypt: `instrukcje/skrypty/whisper_napisy_raw.py`. Wymaga klucza API OpenAI w zmiennej środowiskowej `OPENAI_API_KEY` (klucza NIE wpisywać nigdzie w repo/czacie — jeśli już tam trafił, unieważnić na https://platform.openai.com/api-keys i wygenerować nowy).

```
export OPENAI_API_KEY="..."
python3 "instrukcje/skrypty/whisper_napisy_raw.py" "/ścieżka/tymczasowa/audio.mp3" "txt/napisy.srt"
```

1. **Transkrypcja z segmentami.** Skrypt wysyła audio do OpenAI Whisper (`whisper-1`, `response_format=verbose_json`, `timestamp_granularities=["segment"]`, `language=pl`) i dostaje listę **segmentów** z czasem startu i końca każdego. Surową odpowiedź cache'uje w `txt/napisy.srt.whisper.json` — kolejne uruchomienia nie płacą ponownie za tę samą minutę audio.
2. **SRT powstaje 1:1 z segmentów Whisper.** Jeden segment = jeden wpis SRT. Start wpisu = start segmentu wg Whispera; koniec wpisu = start następnego segmentu (ostatni wpis: koniec swojego segmentu). **Nie ma tu dopasowania treści do `lirycs.txt`, parowania linijek w pary, wyprzedzenia (lead) ani ręcznego liczenia segmentów** — czasy i podział na wpisy pochodzą wprost z odpowiedzi API.
3. **`lirycs.txt` NIE jest wejściem tego etapu.** Nie modyfikujemy go i nie używamy do napędzania treści napisów — służy dopiero do ręcznej korekty tekstu w ostatnim kroku.

## Ręczna korekta tekstu (tylko tekst, nigdy znaczniki czasowe)

Po wygenerowaniu SRT przejść wpisy i poprawić **wyłącznie tekst** tam, gdzie Whisper przesłyszał słowo (np. „prawdą śnią" → „prawdą lśnią", „czekają korona" → „czeka ją korona", „Pan Młody" → „pan młody"), zgadzając treść ze śpiewanymi słowami wg `lirycs.txt`. **Znaczników czasowych nie ruszamy w ogóle** — pochodzą z Whispera i są źródłem prawdy dla synchronizacji. Poprawiamy tylko oczywiste przesłyszenia; reszta transkrypcji zostaje bez zmian.

## Wyprzedzenie napisów (lead) — drobna korekta na słuch, po wygenerowaniu

**Aktualizacja 2026-08-01.** Czasy z Whispera bywają odbierane jako minimalnie spóźnione względem wokalu, dlatego dopuszczalne jest przesunięcie całego pliku o **0,2-0,3 s wcześniej**. To zmiana rzędu ćwierć sekundy, wprowadzana **po** wygenerowaniu surowego SRT i **na wyraźną prośbę użytkownika po odsłuchu** — nie automatycznie i nie „na wszelki wypadek".

Nie unieważnia to zasady wyżej: surowy plik z Whispera zostaje nietknięty jako punkt odniesienia, a przesunięta wersja idzie do **osobnego pliku z kolejnym numerem** (`napisy_v3.srt`, `napisy_v4.srt`...). Wcześniejszy zakaz leadu dotyczył wariantu **1-sekundowego** („efekt karaoke"), który użytkownik odrzucił jako rozjeżdżający się z dźwiękiem — 0,25 s to inna skala i inny cel.

Trzy rzeczy, które łatwo zepsuć:

1. **Start pierwszego wpisu zostaje na `00:00:00,000`** — wcześniej nie da się go przesunąć. Jego **koniec** przesuwamy razem z resztą, bo inaczej wpis 1 nachodziłby na wpis 2 o wartość leadu, a nachodzące się napisy YouTube renderuje nieprzewidywalnie.
2. **Każdą kolejną wersję wyprowadzamy z pliku o czasach Whispera**, nigdy z poprzedniej przesuniętej — inaczej przesunięcia się kumulują (v4 z v3 dałoby -0,55 s zamiast -0,25 s).
3. **Ciągłość musi zostać:** koniec każdego wpisu = start następnego. Po przesunięciu sprawdzić to programowo, razem z warunkiem „start przed końcem" w każdym wpisie.

Przesunięcie napisów **nie wpływa na obrazki ani na oś czasu** — kadry są zsynchronizowane z audio, nie z napisami, a audio się nie zmienia. Nie ma nic do przeliczania w Etapach 3, 5 i 8.

Stan Psalmu 121 jako wzorzec: `napisy_v2.srt` (czasy Whispera, nietknięte), `napisy_v3.srt` (-0,3 s), `napisy_v4.srt` (-0,25 s, wersja wybrana).

Zależności: `ffmpeg`/`ffprobe`, biblioteka Python `requests`, klucz `OPENAI_API_KEY`.
