#!/usr/bin/env python3
"""
Etap 2 — generowanie napisy.srt WYŁĄCZNIE z odpowiedzi OpenAI Whisper.

Napisy budowane są 1:1 z segmentów zwróconych przez Whisper (verbose_json,
granulacja "segment"): jeden segment = jeden wpis SRT, start wpisu = start
segmentu, koniec wpisu = start następnego segmentu (ostatni: koniec swojego
segmentu). NIE ma tu dopasowania do lirycs.txt, parowania linijek ani
wyprzedzenia (lead) — czasy i podział pochodzą wprost z Whispera.

Po wygenerowaniu poprawia się RĘCZNIE tylko TEKST przesłyszeń (wg lirycs.txt),
NIGDY nie ruszając znaczników czasowych. lirycs.txt nie jest wejściem tego
skryptu — służy dopiero do ręcznej korekty tekstu na końcu.

Wejście audio: pełny miks audio.wav. Jeśli plik przekracza limit API OpenAI
(25 MB), najpierw skompresować do mp3, np.:
    ffmpeg -i audio.wav -codec:a libmp3lame -qscale:a 4 audio.mp3

Surowa odpowiedź Whisper jest cache'owana obok wyjścia (<out>.whisper.json)
i wczytywana przy kolejnym uruchomieniu zamiast ponownego (płatnego) wywołania.

Wymaga OPENAI_API_KEY w zmiennej środowiskowej (klucza NIE wpisywać w repo/czat).

Użycie:
    export OPENAI_API_KEY="..."
    python3 whisper_napisy_raw.py <audio.wav/mp3> <napisy_v2.srt>
"""
import json
import os
import subprocess
import sys

import requests

API_URL = "https://api.openai.com/v1/audio/transcriptions"
COST_PER_MINUTE_USD = 0.006


def get_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        stdout=subprocess.PIPE, check=True).stdout.decode().strip()
    return float(out)


def transcribe(audio_path):
    duration = get_duration(audio_path)
    print(f"Długość audio: {duration:.1f} s — szacowany koszt: ${duration/60*COST_PER_MINUTE_USD:.4f}")
    with open(audio_path, "rb") as f:
        resp = requests.post(
            API_URL,
            headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"},
            data={
                "model": "whisper-1",
                "response_format": "verbose_json",
                "timestamp_granularities[]": "segment",
                "language": "pl",
            },
            files={"file": (os.path.basename(audio_path), f)},
        )
    resp.raise_for_status()
    return resp.json()


def ts(sec):
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    audio_path, out_path = sys.argv[1], sys.argv[2]
    cache_path = out_path + ".whisper.json"

    if os.path.exists(cache_path):
        data = json.load(open(cache_path, encoding="utf-8"))
        print("Wczytano cache:", cache_path)
    else:
        data = transcribe(audio_path)
        json.dump(data, open(cache_path, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("Zapisano cache:", cache_path)

    segs = [s for s in data.get("segments", []) if s["text"].strip()]
    entries = []
    for i, s in enumerate(segs):
        start = s["start"]
        end = segs[i + 1]["start"] if i + 1 < len(segs) else s["end"]
        entries.append(f"{i+1}\n{ts(start)} --> {ts(end)}\n{s['text'].strip()}\n")

    open(out_path, "w", encoding="utf-8").write("\n".join(entries) + "\n")
    print(f"Zapisano {len(entries)} wpisów SRT do {out_path}")
    print("PAMIĘTAJ: popraw ręcznie tylko tekst przesłyszeń wg lirycs.txt, "
          "nie ruszając znaczników czasowych.")


if __name__ == "__main__":
    main()
