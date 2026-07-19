# Etap 2 — Napisy

> Część `styl-teledysku.md` — wczytywać przy pracy nad Etapem 2 (synchronizacja napisów). Wykonywany zaraz po Etapie 1 (lyrics), przed Etapem 3 (prompty do obrazków) — jego wynik zasila rozpisanie kadrów w Etapie 3.

**Model: Sonnet, tryb Thinking WYŁĄCZONY, effort medium.** Synchronizację robi skrypt `whisper_napisy.py` (transkrypcja OpenAI Whisper z word-level timestamps + dopasowanie do `lirycs.txt`) — to zadanie deterministyczne, nie wymaga już swobodnego osądu co do granic sekcji ani liczenia segmentów ręcznie, więc Opus nie jest potrzebny. Rola modelu: uruchomić skrypt, sprawdzić ostrzeżenia o rozjazdach, w razie potrzeby poprosić użytkownika o potwierdzenie niejednoznacznego miejsca.

**Cel etapu:** wygenerowanie pliku `napisy.srt` w podfolderze `txt/` — tekst parafrazy z `txt/lirycs.txt` rozłożony na znaczniki czasowe, zsynchronizowany z audio. Napisy CC są indeksowane przez wyszukiwarkę YouTube i poprawiają dostępność. Wynik tego etapu (dokładne znaczniki czasowe per-linijka) jest potem podstawą rozpisania kadrów w Etapie 3 — patrz `etap3-prompty-stylu.md`.

## Źródło audio — plik z izolowanym wokalem

Synchronizację robimy na pliku zawierającym **wyłącznie wokal** (bez instrumentów), np. `audio/audio (Vocals).wav` — użytkownik dostarcza go osobno, wyizolowanego przez zewnętrzne narzędzie (stem separation). Jeśli taki plik istnieje w `audio/`, używamy go zamiast pełnego miksu `audio.wav` — Whisper rozpoznaje słowa dokładniej na czystym wokalu niż na pełnym miksie z instrumentami. Jeśli pliku z izolowanym wokalem nie ma, poproś użytkownika o dostarczenie go.

## Metoda synchronizacji — transkrypcja Whisper + dopasowanie do tekstu (WAŻNE — nie „na oko")

Skrypt: `instrukcje/skrypty/whisper_napisy.py`. Wymaga klucza API OpenAI w zmiennej środowiskowej `OPENAI_API_KEY` (klucza NIE wpisywać nigdzie w repo/czacie — jeśli już tam trafił, unieważnić na https://platform.openai.com/api-keys i wygenerować nowy).

```
export OPENAI_API_KEY="..."
python3 "instrukcje/skrypty/whisper_napisy.py" "audio/audio (Vocals).wav" "txt/lirycs.txt" "txt/napisy.srt"
```

1. **Transkrypcja z word-level timestamps.** Skrypt wysyła plik audio do OpenAI Whisper (`whisper-1`, `response_format=verbose_json`, `timestamp_granularities=["word"]`, `language=pl`) i dostaje listę rozpoznanych słów z czasem startu każdego z nich. Wynik cache'uje w `txt/napisy.srt.whisper.json` — kolejne uruchomienia (np. po poprawce parowania linijek) nie płacą ponownie za tę samą minutę audio.
2. **Treść napisów bazuje na `lirycs.txt`, ALE transkrypcja Whisper jest nadrzędna, gdy się różnią.** Dopasowanie rozpoznanych słów do słów z `lirycs.txt` robi `difflib.SequenceMatcher` na znormalizowanych tokenach (bez interpunkcji, lowercase); dla pojedynczych błędnie rozpoznanych słów (literówka, inna końcówka) `lirycs.txt` pozostaje źródłem prawdy, a ich czas jest interpolowany liniowo między sąsiednimi trafieniami. **Jeśli jednak Whisper konsekwentnie wykrywa słowa/frazy, których w `lirycs.txt` w ogóle nie ma** (nie pojedyncza pomyłka rozpoznania, tylko realny, powtarzalny nadmiar tekstu) — traktować to jako sygnał, że Suno podczas generowania utworu dośpiewało coś od siebie, czego nie było w tekście wysłanym do Suno. W takim wypadku napisy dla tego fragmentu mają iść za tym, co faktycznie słychać (wg Whispera), a nie za `lirycs.txt` — inaczej napisy rozjeżdżają się z audio od tego miejsca do końca utworu. Przy wątpliwości, czy to pomyłka rozpoznania czy realny dodatek Suno, potwierdzić z użytkownikiem zamiast zgadywać.
3. **Start linijki = czas pierwszego dopasowanego/zinterpolowanego słowa tej linijki.** Sekcje ([Verse], [Chorus] itd.) są tylko separatorami parowania (patrz niżej) — nie trzeba już ręcznie liczyć segmentów RMS per sekcja.
4. **Dokładność zależy od jakości rozpoznania Whisper na danym nagraniu** — zwykle wysoka na czystym wokalu solo. Po wygenerowaniu obejrzeć ostrzeżenia w output skryptu (patrz "Kotwice" niżej) i w razie wątpliwości sprawdzić fragment w YouTube Studio (edytor napisów pokazuje ścieżkę dźwiękową).

## Kotwice czasowe od użytkownika w `lirycs.txt` (opcjonalne — teraz tylko do weryfikacji, nie do napędzania mapowania)

Format `[M:SS]` tuż przed tekstem linijki (np. `[1:17]Jednego pragnę, o to wciąż wołam,`) nadal jest wspierany, ale odkąd czas pochodzi z Whisper zamiast z ręcznego liczenia segmentów RMS, kotwice nie są już potrzebne do samego mapowania — skrypt je wykorzystuje wyłącznie jako **kontrolę spójności**: jeśli obliczony (z Whisper) start linijki różni się od podanej kotwicy o więcej niż ~1,5 s, skrypt wypisuje ostrzeżenie na stdout. Warto je zostawiać w trudniejszych utworach (szybkie tempo, niewyraźna dykcja) jako tani sposób złapania błędu dopasowania bez ręcznego przesłuchiwania całości.

## Format wyświetlania — dwie linijki naraz, start dokładnie na wokalu (bez wyprzedzenia)

- **Napisy grupujemy parami** — każdy wpis SRT pokazuje jednocześnie 2 kolejne linijki tekstu (linijka 1+2 razem, 3+4 razem, itd.), oddzielone twardym podziałem wiersza w tym samym wpisie. Parowanie idzie sekwencyjnie przez cały utwór (nie per-sekcja) — jeśli sekcja ma nieparzystą liczbę linijek, ostatnia linijka tej sekcji zostaje bez pary (wyświetlana samodzielnie) zamiast łączyć się z linijką z następnej sekcji.
- **Start wpisu = dokładny, wykryty start wokalu pierwszej linijki w parze — BEZ żadnego wyprzedzenia.** Wcześniej testowany wariant z 1-sekundowym wyprzedzeniem („efekt karaoke") został odrzucony przez użytkownika jako rozjeżdżający się z dźwiękiem — napisy mają się pojawiać dokładnie w momencie, gdy dany wers faktycznie zaczyna brzmieć, nie wcześniej.
- **Koniec wpisu = start następnego wpisu** — bez przerwy między wpisami, tekst na ekranie zmienia się w momencie startu kolejnej pary. Ostatni wpis w utworze kończy się na końcu ostatniej zaśpiewanej frazy (+ mały bufor na doczytanie, do końca pliku audio).

Zależności: `ffmpeg`/`ffprobe` (do pomiaru długości audio) + biblioteka Python `requests` w środowisku roboczym; klucz `OPENAI_API_KEY`; struktura sekcji i tekst z `lirycs.txt`; opcjonalne kotwice czasowe od użytkownika w `lirycs.txt` (do weryfikacji).
