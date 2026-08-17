#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Etap 1A — master audio: EQ + de-esser + normalizacja do -14 LUFS.

Bierze surowy plik z Suno (audio/audio.wav) i produkuje audio/audio_eq_v2.wav —
plik, który idzie na oś czasu w DaVinci Resolve.

Użycie:
    python3 master_audio.py "psalm 8 - in progress - 8"
    python3 master_audio.py "psalm 8 - in progress - 8" --wyjscie audio_master.wav
    python3 master_audio.py "psalm 8 - in progress - 8" --deess mocniej

Wymaga: ffmpeg + ffprobe w PATH (brew install ffmpeg).

Łańcuch przetwarzania i uzasadnienie każdej wartości: instrukcje/etap1a-audio-master.md
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

# --- Poziom odniesienia -------------------------------------------------------
# Próg de-essera (acompressor) jest BEZWZGLĘDNY, więc materiał wchodzący głośniej
# byłby de-essowany mocniej, a cichszy prawie wcale. Dlatego przed EQ sprowadzamy
# wejście zawsze do tego samego poziomu. -16.5 LUFS to poziom, na którym wylądował
# Psalm 8 (-13.5 LUFS z Suno, minus 3 dB zapasu) i na którym ustawienia zatwierdzono.
LUFS_ODNIESIENIA = -16.5

# --- Cel końcowy --------------------------------------------------------------
# YouTube normalizuje wszystko do -14 LUFS, więc wypuszczanie głośniejszego
# materiału nic nie daje poza utratą dynamiki. TP -1.0 dBFS zostawia zapas na
# zniekształcenia przy kodowaniu do AAC.
LUFS_CEL = -14.0
TP_CEL = -1.0
LRA_CEL = 11.0

# --- Profile brzmieniowe ------------------------------------------------------
# v3 — DOMYŚLNY od 2026-08-09, zatwierdzony odsłuchowo na Psalmie 119.
# v2 — stary, zatwierdzony na Psalmie 8. Zostaje wyłącznie po to, żeby dało się
#      odtworzyć brzmienie filmów zrobionych przed tą zmianą (Psalmy 1, 8, ...).
#      Do nowych psalmów NIE używać.
# v3 — poprawka po pomiarach na Psalmie 1 (film brzmiał krzykliwie). Dwa zarzuty,
#      oba zmierzone: (1) bell +2.5 dB na 3 kHz siedzi na maksimum polskiego "sz",
#      a jednocześnie dół był ścinany, przez co master wychodził ~3 dB bardziej
#      "do przodu" niż plik z Suno; (2) próg de-essera -22 dBFS leżał POWYŻEJ
#      szczytu RMS pasma sybilantów (-22.9 dBFS), więc kompresor praktycznie
#      nie ruszał. Szczegóły: etap1a-audio-master.md § "Profil v3".
EQ = {
    "v2": ",".join([
        "highpass=f=65:poles=2",                             # rumot, 12 dB/okt
        "bass=g=-4:f=41:width_type=q:width=0.7",             # dół bez odchudzania miksu
        "equalizer=f=300:width_type=q:width=1.2:g=-2.5",     # ubytek mułu — odsłania wokal
        "equalizer=f=3000:width_type=q:width=1.0:g=2.5",     # obecność, zrozumiałość spółgłosek
        "treble=g=2.5:f=11500:width_type=q:width=0.7",       # powietrze
        "lowpass=f=19000:poles=2",
    ]),
    "v3": ",".join([
        "highpass=f=55:poles=2",                             # niżej — 65 Hz zabierało ciało fortepianu
        "bass=g=-2:f=41:width_type=q:width=0.7",             # łagodniej, HPF i tak zdjął sam dół
        "equalizer=f=300:width_type=q:width=1.2:g=-1.5",     # łagodniejszy ubytek mułu
        "equalizer=f=2000:width_type=q:width=1.2:g=1.5",     # obecność POD maksimum "sz", słabsza
        "treble=g=1.5:f=11500:width_type=q:width=0.7",       # powietrze bez ostrości
        "lowpass=f=19000:poles=2",
    ]),
}

# --- De-esser (split-band: kompresja tylko pasma sybilantów) ------------------
# Polskie "sz"/"cz"/"ż" mają maksimum w 3-5 kHz, "ś"/"s" wyżej, 4-9 kHz.
#
# v2: crossover 3.5 kHz, kompresja całej góry. Progi dobrane "na oko" — na
#     materiale z Psalma 1 okazały się za wysokie, żeby cokolwiek zrobić.
# v3: trzy pasma, kompresja WYŁĄCZNIE środkowego (3-9 kHz). Dolna krawędź "sz"
#     przy 3 kHz jest wreszcie objęta, a powietrze powyżej 9 kHz zostaje nietknięte
#     (przy v2 de-esser zjadał shelf 11.5 kHz, który EQ chwilę wcześniej dodał).
#     Progi zjechały o ~8 dB, bo szczyt RMS pasma 3-9 kHz leży ok. -22 dBFS,
#     a jego RMS ogólny ok. -37 dBFS — próg musi siedzieć między nimi.
DEESS = {
    "v2": {
        #            próg (liniowo)   dB     ratio
        "delikatnie": (0.100, 3),   # -20 dB
        "standard":   (0.079, 4),   # -22 dB  <- zatwierdzone na Psalmie 8
        "mocniej":    (0.063, 5),   # -24 dB
    },
    "v3": {
        "delikatnie": (0.045, 3),   # -27 dB
        "standard":   (0.032, 4),   # -30 dB  <- zmierzone na Psalmie 1
        "mocniej":    (0.022, 5),   # -33 dB
    },
}
DEESS_SPLIT = {"v2": "3500", "v3": "3000|9000"}


def uruchom(cmd):
    w = subprocess.run(cmd, capture_output=True, text=True)
    if w.returncode != 0:
        sys.exit(f"BŁĄD ffmpeg:\n{w.stderr[-2000:]}")
    return w.stderr


def zmierz_lufs(plik):
    """Zintegrowana głośność i true peak przez ebur128.

    Uwaga: ebur128 sypie w trakcie przelotowymi liniami 'I: ... LUFS' dla każdej
    ramki. Interesuje nas wyłącznie blok podsumowania na końcu, więc regexy są
    zakotwiczone w jego nagłówkach — inaczej złapiemy wartość z pierwszej ramki
    (-70 LUFS) i całe wyrównanie poziomu wyjdzie kompletnie nie tak.
    """
    wy = uruchom(["ffmpeg", "-hide_banner", "-nostats", "-i", str(plik),
                  "-af", "ebur128=peak=true", "-f", "null", "-"])
    i = re.search(r"Integrated loudness:\s*\n\s*I:\s+(-?[\d.]+)\s*LUFS", wy)
    p = re.search(r"True peak:\s*\n\s*Peak:\s+(-?[\d.]+)\s*dBFS", wy)
    if not i:
        sys.exit("Nie udało się odczytać zintegrowanej głośności z ebur128.")
    return float(i.group(1)), (float(p.group(1)) if p else None)


def zmierz_loudnorm(plik):
    """Pierwszy przebieg loudnorm — zwraca pomiary do przebiegu drugiego."""
    wy = uruchom(["ffmpeg", "-hide_banner", "-nostats", "-i", str(plik),
                  "-af", f"loudnorm=I={LUFS_CEL}:TP={TP_CEL}:LRA={LRA_CEL}:print_format=json",
                  "-f", "null", "-"])
    blok = re.search(r"\{[^{}]*\}", wy, re.S)
    if not blok:
        sys.exit("Nie udało się odczytać pomiaru loudnorm.")
    return json.loads(blok.group(0))


def main():
    ap = argparse.ArgumentParser(description="Etap 1A — master audio dla psalmu")
    ap.add_argument("folder", help="folder utworu, np. 'psalm 8 - in progress - 8'")
    ap.add_argument("--wejscie", default="audio.wav", help="plik źródłowy w audio/ (domyślnie audio.wav)")
    ap.add_argument("--wyjscie", default="audio_eq_v2.wav", help="nazwa pliku wynikowego w audio/")
    ap.add_argument("--deess", default="standard", choices=["delikatnie", "standard", "mocniej"],
                    help="siła de-essera (domyślnie standard)")
    ap.add_argument("--profil", default="v3", choices=list(EQ),
                    help="profil brzmieniowy: v3 (domyślny, zatwierdzony na Psalmie 119) "
                         "albo v2 (stary, zatwierdzony na Psalmie 8 — tylko do odtworzenia "
                         "brzmienia wcześniejszych filmów)")
    a = ap.parse_args()

    folder = Path(a.folder)
    if not folder.is_absolute():
        folder = Path.cwd() / folder
    zrodlo = folder / "audio" / a.wejscie
    cel = folder / "audio" / a.wyjscie

    if not zrodlo.exists():
        sys.exit(f"Brak pliku źródłowego: {zrodlo}")
    if cel.exists():
        sys.exit(f"Plik wynikowy już istnieje, nie nadpisuję: {cel}\n"
                 f"Usuń go ręcznie albo podaj inną nazwę przez --wyjscie.")

    print(f"Źródło: {zrodlo}")
    lufs_we, tp_we = zmierz_lufs(zrodlo)
    print(f"  wejście:  {lufs_we} LUFS, true peak {tp_we} dBFS")

    # Wzmocnienie wyrównujące do poziomu odniesienia — żeby próg de-essera
    # zachowywał się tak samo niezależnie od tego, jak głośno przyszło z Suno.
    pre_gain = round(LUFS_ODNIESIENIA - lufs_we, 2)
    prog, ratio = DEESS[a.profil][a.deess]
    split = DEESS_SPLIT[a.profil]
    print(f"  profil: {a.profil}")
    print(f"  wyrównanie przed EQ: {pre_gain:+.2f} dB  (do {LUFS_ODNIESIENIA} LUFS)")
    print(f"  de-esser: {a.deess} — próg {prog}, ratio {ratio}:1, crossover {split} Hz")

    tmp = folder / "audio" / ".master_tmp.wav"

    # Przebieg 1: wyrównanie + EQ + de-esser.
    # v2 kompresuje całą górę (2 pasma), v3 tylko środkowe pasmo sybilantów (3 pasma).
    if a.profil == "v3":
        deess = (
            f"[pre]acrossover=split={split}:order=4th[lo][mid][hi];"
            f"[mid]acompressor=threshold={prog}:ratio={ratio}:attack=1:release=45:"
            f"knee=4:detection=peak[midd];"
            f"[lo][midd][hi]amix=inputs=3:duration=longest:normalize=0[out]"
        )
    else:
        deess = (
            f"[pre]acrossover=split={split}:order=4th[lo][hi];"
            f"[hi]acompressor=threshold={prog}:ratio={ratio}:attack=1:release=40:"
            f"knee=4:detection=peak:makeup=1[hid];"
            f"[lo][hid]amix=inputs=2:duration=longest:normalize=0[out]"
        )
    graf = f"[0:a]volume={pre_gain}dB,{EQ[a.profil]}[pre];" + deess
    print("  [1/3] EQ + de-esser…")
    uruchom(["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostats", "-y",
             "-i", str(zrodlo), "-filter_complex", graf, "-map", "[out]",
             "-c:a", "pcm_s24le", str(tmp)])

    # Przebieg 2+3: dwuprzebiegowy loudnorm (jednoprzebiegowy trafia w cel niedokładnie)
    print("  [2/3] pomiar głośności…")
    m = zmierz_loudnorm(tmp)
    print("  [3/3] normalizacja do celu…")
    uruchom(["ffmpeg", "-hide_banner", "-loglevel", "error", "-nostats", "-y",
             "-i", str(tmp), "-af",
             f"loudnorm=I={LUFS_CEL}:TP={TP_CEL}:LRA={LRA_CEL}:"
             f"measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
             f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
             f"offset={m['target_offset']}:linear=true,aresample=48000",
             "-c:a", "pcm_s24le", "-ar", "48000", str(cel)])
    tmp.unlink(missing_ok=True)

    lufs_wy, tp_wy = zmierz_lufs(cel)
    print(f"\nGotowe: {cel}")
    print(f"  wyjście:  {lufs_wy} LUFS, true peak {tp_wy} dBFS")
    print("\nPo podmianie ścieżki w Resolve WYŁĄCZ Equalizer na Audio 1 —")
    print("EQ jest już wpieczony w plik, inaczej zadziała podwójnie.")


if __name__ == "__main__":
    main()
