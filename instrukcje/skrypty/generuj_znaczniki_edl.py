"""
Generator znaczników kadrów jako plik EDL (Etap 5/render).

Do czego to jest: DaVinci Resolve w wersji darmowej (bez Studio) NIE obsługuje
API skryptowego (bmd.scriptapp("Resolve").GetProjectManager() zawsze zwraca
None) — więc `ustaw_znaczniki_kadrow.py` tam nie zadziała. Ten skrypt omija
ten problem: generuje zwykły plik .edl na dysku (bez potrzeby Resolve w ogóle),
który Resolve umie zaimportować jako znaczniki na timeline przez menu, bez
żadnego skryptowania.

Użycie:
    1. Ustaw niżej FOLDER_PATH (folder images/ danego psalmu, po Etapie 5 —
       pliki nazwane zakresami czasu, np. 0m00s-0m15s.jpg), FPS i START_TIMECODE
       (musi się zgadzać z timecode'em początku Twojej osi czasu w Resolve —
       domyślnie w nowych timeline'ach Resolve to 01:00:00:00).
    2. Uruchom zwykłym: python3 generuj_znaczniki_edl.py
    3. W DaVinci Resolve: menu Timeline -> Import -> Timeline Markers from EDL...
       -> wskaż wygenerowany plik .edl. Upewnij się, że właściwa oś czasu jest
       aktywna/otwarta przed importem.
"""

import os
import re

# ==========================================
# TUTAJ WPISZ ŚCIEŻKĘ DO FOLDERU Z PLIKAMI (images/ po Etapie 5):
FOLDER_PATH = r"/Volumes/ADATA SE880/_Święta Muzyka/_claude/psalm 118 - in progress - 7/images"
# Gdzie zapisać wynikowy plik .edl:
OUTPUT_PATH = r"/Volumes/ADATA SE880/_Święta Muzyka/_claude/psalm 118 - in progress - 7/images/znaczniki_kadrow.edl"
# Klatkaż timeline'u w Resolve (np. 25, 24, 30):
FPS = 25
# Timecode początku osi czasu w Resolve (domyślny dla nowego timeline'u to 01:00:00:00;
# jeśli Twój timeline zaczyna się od 00:00:00:00, zmień na to):
START_TIMECODE = "01:00:00:00"
# ==========================================


def time_to_frames(m, s, fps):
    """Konwertuje minuty i sekundy (z nazwy pliku) na liczbę klatek."""
    total_seconds = (int(m) * 60) + int(s)
    return int(round(total_seconds * fps))


def timecode_to_frames(tc, fps):
    hh, mm, ss, ff = (int(x) for x in tc.split(":"))
    fps_int = int(round(fps))
    return ((hh * 3600 + mm * 60 + ss) * fps_int) + ff


def frames_to_timecode(total_frames, fps):
    fps_int = int(round(fps))
    ff = total_frames % fps_int
    total_seconds = total_frames // fps_int
    ss = total_seconds % 60
    mm = (total_seconds // 60) % 60
    hh = total_seconds // 3600
    return f"{hh:02d}:{mm:02d}:{ss:02d}:{ff:02d}"


def main():
    if not os.path.isdir(FOLDER_PATH):
        print(f"Błąd: Podany folder '{FOLDER_PATH}' nie istnieje.")
        return

    markers = []  # (start_frame_relative, filename)
    for filename in os.listdir(FOLDER_PATH):
        if filename.startswith("."):
            continue  # pomiń ukryte pliki (np. AppleDouble "._nazwa.jpg" na exFAT)
        match = re.search(r"(\d+)m(\d+)s-(\d+)m(\d+)s", filename)
        if match:
            start_m, start_s, _end_m, _end_s = match.groups()
            start_frame = time_to_frames(start_m, start_s, FPS)
            markers.append((start_frame, filename))

    if not markers:
        print("Nie znaleziono żadnych plików pasujących do wzorca (np. 0m17s-0m32s.jpg).")
        return

    markers.sort(key=lambda x: x[0])

    base_frame = timecode_to_frames(START_TIMECODE, FPS)

    lines = ["TITLE: Znaczniki kadrow", "FCM: NON-DROP FRAME", ""]

    for i, (rel_frame, filename) in enumerate(markers, start=1):
        abs_in = base_frame + rel_frame
        abs_out = abs_in + 1
        tc_in = frames_to_timecode(abs_in, FPS)
        tc_out = frames_to_timecode(abs_out, FPS)
        event_num = f"{i:03d}"
        lines.append(f"{event_num}  001      V     C        {tc_in} {tc_out} {tc_in} {tc_out}")
        lines.append(f"Kadr {i} - {filename}")
        lines.append("")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Zapisano {len(markers)} znacznikow do: {OUTPUT_PATH}")
    print("W Resolve: Timeline -> Import -> Timeline Markers from EDL...")


if __name__ == "__main__":
    main()
