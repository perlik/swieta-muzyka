#!/usr/bin/env python3
"""
Etap 6 — generowanie napisy.srt przez transkrypcję OpenAI Whisper (word-level
timestamps) + dopasowanie do zatwierdzonego tekstu z lirycs.txt.

Whisper dostarcza znaczniki czasowe (poprzez rozpoznane słowa), a treść napisów to
domyślnie oryginalny tekst z lirycs.txt (śpiewana parafraza bywa błędnie rozpoznawana
słowo w słowo — pojedyncze pomyłki Whispera nie psują wyniku). Dopasowanie tekstu do
rozpoznanych słów robi difflib.SequenceMatcher; luki między dopasowanymi słowami są
interpolowane liniowo.

WYJĄTEK — Whisper jest NADRZĘDNY, gdy wykryje spójny blok słów, którego w lirycs.txt
w ogóle nie ma (>= MIN_EXTRA_WORDS kolejnych nierozpoznanych słów pod rząd). To sygnał,
że Suno przy generowaniu utworu dośpiewało coś od siebie, czego nie było w tekście
wysłanym do Suno — bez takiego bloku napisy rozjeżdżałyby się z audio od tego miejsca
do końca utworu. Taki blok jest wstawiany do napisów jako dodatkowa linijka (tekstem
wprost z transkrypcji Whisper, nie z lirycs.txt), a skrypt wypisuje ostrzeżenie na
stdout, żeby operator mógł zweryfikować, czy to faktyczny dodatek Suno, czy zbieg
pomyłek rozpoznania.

Wymaga klucza API OpenAI w zmiennej środowiskowej OPENAI_API_KEY. Klucza NIE wpisywać
nigdzie w repo — jeśli klucz kiedykolwiek trafił do czatu/logów, unieważnić go na
https://platform.openai.com/api-keys i wygenerować nowy.

Użycie:
    export OPENAI_API_KEY="..."
    python3 whisper_napisy.py <audio_wokal.wav/mp3> <lirycs.txt> <napisy.srt> [--cache whisper_cache.json]

Wejście audio: plik z izolowanym wokalem (patrz etap2-napisy.md) — dokładniejsze
rozpoznanie niż pełny miks z instrumentami. Cache JSON z surową odpowiedzią Whisper
jest zapisywany obok wyjścia (domyślnie <napisy.srt>.whisper.json) i wczytywany przy
kolejnym uruchomieniu zamiast ponownego wywołania API (płatnego za minutę audio).

Koszt: whisper-1 ok. $0.006/minutę audio (sprawdzić aktualny cennik na
https://openai.com/api/pricing/) — skrypt wypisuje szacowany koszt przed wywołaniem.
"""

import difflib
import json
import os
import re
import subprocess
import sys

import requests

API_URL = "https://api.openai.com/v1/audio/transcriptions"
COST_PER_MINUTE_USD = 0.006

# Minimalna liczba kolejnych słów rozpoznanych przez Whisper, a nieobecnych w
# lirycs.txt, żeby uznać to za realny dodatkowy fragment (np. refren dołożony
# przez Suno), a nie pojedyncze złe rozpoznanie/oddech. Poniżej tego progu blok
# jest po staremu ignorowany.
MIN_EXTRA_WORDS = 3


def get_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        stdout=subprocess.PIPE, check=True).stdout.decode().strip()
    return float(out)


def transcribe(audio_path, api_key):
    duration = get_duration(audio_path)
    est_cost = duration / 60 * COST_PER_MINUTE_USD
    print(f"Długość audio: {duration:.1f} s — szacowany koszt Whisper: ${est_cost:.4f}")
    with open(audio_path, "rb") as f:
        resp = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {api_key}"},
            data={
                "model": "whisper-1",
                "response_format": "verbose_json",
                "timestamp_granularities[]": "word",
                "language": "pl",
            },
            files={"file": (os.path.basename(audio_path), f)},
        )
    resp.raise_for_status()
    return resp.json()


SECTION_TAG_RE = re.compile(r"^\[([^:\]]+)\]$")
ANCHOR_RE = re.compile(r"^\[(\d{1,2}):(\d{2})\](.*)$")


def parse_lyrics(path):
    """Zwraca listę linijek: {section, text, anchor_s (opcjonalny)}. Pomija tagi sekcji i puste linie."""
    lines = []
    for raw in open(path, encoding="utf-8"):
        line = raw.strip()
        if not line:
            continue
        m = SECTION_TAG_RE.match(line)
        if m:
            if m.group(1).strip().lower() == "end":
                continue
            lines.append({"section_tag": m.group(1).strip()})
            continue
        anchor_s = None
        m = ANCHOR_RE.match(line)
        if m:
            anchor_s = int(m.group(1)) * 60 + int(m.group(2))
            line = m.group(3).strip()
        lines.append({"text": line, "anchor_s": anchor_s})
    return lines


def normalize(word):
    return re.sub(r"[^\w]", "", word, flags=re.UNICODE).lower()


def align(whisper_words, lyric_lines):
    """whisper_words: [{word,start,end}]; lyric_lines: wynik parse_lyrics (tylko wpisy z 'text').
    Zwraca listę czasów startu (float) dla każdej linijki tekstu."""
    w_norm = [normalize(w["word"]) for w in whisper_words]

    true_words_flat = []
    true_word_line_idx = []
    text_lines = [l for l in lyric_lines if "text" in l]
    for li, line in enumerate(text_lines):
        for w in line["text"].split():
            true_words_flat.append(normalize(w))
            true_word_line_idx.append(li)

    sm = difflib.SequenceMatcher(a=w_norm, b=true_words_flat, autojunk=False)
    opcodes = sm.get_opcodes()
    true_word_time = [None] * len(true_words_flat)
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "equal":
            for k in range(i2 - i1):
                true_word_time[j1 + k] = whisper_words[i1 + k]["start"]

    # Bloki słów rozpoznanych przez Whisper, których nie ma w ogóle w lirycs.txt
    # (tag == "delete": obecne tylko w a=whisper, brak odpowiednika w b=lyrics).
    # Krótkie takie bloki to zwykle szum/pomyłka rozpoznania — ignorujemy je.
    # Od progu MIN_EXTRA_WORDS traktujemy to jako realny dodatek Suno i wstawiamy
    # do napisów wprost z transkrypcji Whisper (patrz nagłówek pliku).
    extra_blocks = []
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "delete" and (i2 - i1) >= MIN_EXTRA_WORDS:
            insert_after_line_idx = true_word_line_idx[j1 - 1] if j1 > 0 else -1
            text = " ".join(whisper_words[i]["word"].strip() for i in range(i1, i2)).strip()
            extra_blocks.append({
                "insert_after_line_idx": insert_after_line_idx,
                "text": text,
                "start": whisper_words[i1]["start"],
            })

    # interpolacja luk między dopasowanymi słowami
    n = len(true_word_time)
    i = 0
    while i < n:
        if true_word_time[i] is not None:
            i += 1
            continue
        j = i
        while j < n and true_word_time[j] is None:
            j += 1
        prev_t = true_word_time[i - 1] if i > 0 else None
        next_t = true_word_time[j] if j < n else None
        gap = j - i
        if prev_t is not None and next_t is not None:
            for k in range(gap):
                true_word_time[i + k] = prev_t + (next_t - prev_t) * (k + 1) / (gap + 1)
        elif next_t is not None:
            avg_gap = 0.4
            for k in range(gap):
                true_word_time[i + k] = max(0.0, next_t - avg_gap * (gap - k))
        elif prev_t is not None:
            avg_gap = 0.4
            for k in range(gap):
                true_word_time[i + k] = prev_t + avg_gap * (k + 1)
        else:
            for k in range(gap):
                true_word_time[i + k] = 0.0
        i = j

    line_start = [None] * len(text_lines)
    for word_idx, line_idx in enumerate(true_word_line_idx):
        if line_start[line_idx] is None:
            line_start[line_idx] = true_word_time[word_idx]

    last_word_time = true_word_time[-1] if true_word_time else 0.0

    for li, line in enumerate(text_lines):
        if line.get("anchor_s") is not None:
            diff = abs(line_start[li] - line["anchor_s"])
            if diff > 1.5:
                print(f"UWAGA: linijka '{line['text'][:40]}...' — obliczony start "
                      f"{line_start[li]:.2f}s różni się od kotwicy {line['anchor_s']}s o {diff:.2f}s")

    return text_lines, line_start, last_word_time, extra_blocks


def insert_extra_lines(lyric_lines, line_start, extra_blocks):
    """Wstawia do lyric_lines/line_start bloki wykryte przez Whisper, a nieobecne
    w lirycs.txt (patrz align()/MIN_EXTRA_WORDS). Zwraca nowe (lyric_lines, line_start)."""
    if not extra_blocks:
        return lyric_lines, line_start

    lyric_lines = list(lyric_lines)
    line_start = list(line_start)

    def find_insert_position(text_line_index):
        """Indeks w lyric_lines tuż za text_line_index-tą ORYGINALNĄ (nie-extra)
        linijką tekstu; -1 oznacza wstawienie na samym początku."""
        if text_line_index == -1:
            return 0
        count = -1
        for idx, entry in enumerate(lyric_lines):
            if "text" in entry and not entry.get("extra"):
                count += 1
                if count == text_line_index:
                    return idx + 1
        return len(lyric_lines)

    # W obrębie tego samego miejsca wstawienia: od najpóźniejszego czasu do
    # najwcześniejszego, żeby po kolejnych wstawieniach w tej samej pozycji
    # wynikowa kolejność była chronologiczna (rosnąco).
    ordered = sorted(extra_blocks, key=lambda b: (b["insert_after_line_idx"], -b["start"]))

    for block in ordered:
        pos = find_insert_position(block["insert_after_line_idx"])
        text_entries_before = sum(1 for e in lyric_lines[:pos] if "text" in e)
        lyric_lines.insert(pos, {"text": block["text"], "anchor_s": None, "extra": True})
        line_start.insert(text_entries_before, block["start"])
        print(f"UWAGA: wykryto blok tekstu z Whispera nieobecny w lirycs.txt "
              f"(prawdopodobny dodatek Suno) w ok. {block['start']:.2f}s — "
              f"wstawiono do napisów: \"{block['text']}\"")

    return lyric_lines, line_start


def build_pairs(lyric_lines, line_start):
    """Paruje linijki 2-po-2, resetując parzystość na każdej granicy sekcji."""
    pairs = []
    current_section_lines = []

    def flush():
        i = 0
        while i < len(current_section_lines):
            if i + 1 < len(current_section_lines):
                pairs.append(current_section_lines[i:i + 2])
            else:
                pairs.append(current_section_lines[i:i + 1])
            i += 2
        current_section_lines.clear()

    text_idx = 0
    for entry in lyric_lines:
        if "section_tag" in entry:
            flush()
        else:
            current_section_lines.append((entry["text"], line_start[text_idx]))
            text_idx += 1
    flush()
    return pairs


def format_srt_time(seconds):
    seconds = max(0.0, seconds)
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int(round((seconds - int(seconds)) * 1000))
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt(pairs, last_word_time, duration, out_path):
    end_buffer = 1.0
    last_entry_end = min(last_word_time + end_buffer, duration)
    with open(out_path, "w", encoding="utf-8") as f:
        for idx, pair in enumerate(pairs):
            start = pair[0][1]
            if idx + 1 < len(pairs):
                end = pairs[idx + 1][0][1]
            else:
                end = last_entry_end
            text = "\n".join(line for line, _ in pair)
            f.write(f"{idx + 1}\n")
            f.write(f"{format_srt_time(start)} --> {format_srt_time(end)}\n")
            f.write(f"{text}\n\n")


def main():
    args = sys.argv[1:]
    cache_path = None
    if "--cache" in args:
        i = args.index("--cache")
        cache_path = args[i + 1]
        del args[i:i + 2]
    if len(args) != 3:
        sys.exit("Użycie: whisper_napisy.py <audio> <lirycs.txt> <napisy.srt> [--cache plik.json]")
    audio_path, lyrics_path, out_path = args
    if cache_path is None:
        cache_path = out_path + ".whisper.json"

    if os.path.exists(cache_path):
        print(f"Wczytuję z cache: {cache_path} (bez ponownego wywołania API)")
        whisper_json = json.load(open(cache_path, encoding="utf-8"))
    else:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            sys.exit("Brak OPENAI_API_KEY w zmiennych środowiskowych.")
        whisper_json = transcribe(audio_path, api_key)
        json.dump(whisper_json, open(cache_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"Zapisano surową odpowiedź Whisper do {cache_path}")

    words = whisper_json.get("words")
    if not words:
        sys.exit("Brak word-level timestamps w odpowiedzi Whisper (sprawdź response_format/timestamp_granularities).")

    lyric_lines = parse_lyrics(lyrics_path)
    text_lines, line_start, last_word_time, extra_blocks = align(words, lyric_lines)
    lyric_lines, line_start = insert_extra_lines(lyric_lines, line_start, extra_blocks)
    pairs = build_pairs(lyric_lines, line_start)
    duration = get_duration(audio_path)
    write_srt(pairs, last_word_time, duration, out_path)
    print(f"Zapisano {len(pairs)} wpisów SRT do {out_path}")


if __name__ == "__main__":
    main()
