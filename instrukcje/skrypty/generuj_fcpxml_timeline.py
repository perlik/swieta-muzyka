"""
Generator gotowej osi czasu (FCPXML) z obrazkow po Etapie 5 — pelna automatyzacja
rozmieszczenia i dlugosci kadrow, bez recznego przeciagania w Resolve.

Do czego to jest: `ustaw_znaczniki_kadrow.py` i `rozmieszczenie_obrazkow.py` wymagaja
API skryptowego Resolve (Studio-only, patrz `generuj_znaczniki_edl.py`). Ten skrypt
tego nie potrzebuje — dziala calkowicie lokalnie i generuje plik .fcpxml, ktory
Resolve (rowniez wersja darmowa) importuje przez zwykle menu jako gotowa oś czasu:
kazdy obrazek juz na wlasciwym miejscu, z wlasciwa dlugoscia wynikajaca z zakresu
czasu w nazwie pliku — zero recznego dopasowywania.

Wzorowany na recznie zrobionym `Psalm27_Timeline.fcpxml` z tego samego folderu.

Użycie:
    1. Ustaw nizej FOLDER_PATH (folder images/ danego psalmu, po Etapie 5 —
       pliki nazwane PELNYM zakresem czasu, np. 0m00s-0m15s.jpg) i FPS.
    2. Uruchom zwyklym: python3 generuj_fcpxml_timeline.py
    3. W DaVinci Resolve: File -> Import -> Timeline... -> wskaz wygenerowany
       plik .fcpxml. Resolve utworzy nowa oś czasu z obrazkami juz rozmieszczonymi
       poprawnie w czasie. Mozna ja potem przeciagnac/skopiowac do wlasciwego
       projektu, albo dolaczyc audio recznie na osobnej sciezce.
"""

import os
import re
from urllib.parse import quote

try:
    from PIL import Image
except ImportError:
    Image = None

# ==========================================
# TUTAJ WPISZ ŚCIEŻKĘ DO FOLDERU Z PLIKAMI (images/ po Etapie 5):
FOLDER_PATH = r"/Volumes/ADATA SE880/_Święta Muzyka/_claude/psalm 118 - in progress - 7/images"
# Gdzie zapisać wynikowy plik .fcpxml:
OUTPUT_PATH = r"/Volumes/ADATA SE880/_Święta Muzyka/_claude/psalm 118 - in progress - 7/images/timeline.fcpxml"
# Klatkaż timeline'u (np. 25, 24, 30):
FPS = 25
# Nazwa projektu/sekwencji widoczna w Resolve:
PROJECT_NAME = "Auto Timeline"
# ==========================================


def time_to_frames(m, s, fps):
    total_seconds = (int(m) * 60) + int(s)
    return int(round(total_seconds * fps))


def to_file_url(path):
    return "file://" + quote(path, safe="/")


def main():
    if not os.path.isdir(FOLDER_PATH):
        print(f"Błąd: Podany folder '{FOLDER_PATH}' nie istnieje.")
        return

    clips = []  # (start_frame, end_frame, filename)
    for filename in sorted(os.listdir(FOLDER_PATH)):
        if filename.startswith("."):
            continue  # pomiń ukryte pliki (np. AppleDouble "._nazwa.jpg" na exFAT)
        match = re.search(r"(\d+)m(\d+)s-(\d+)m(\d+)s", filename)
        if match:
            start_m, start_s, end_m, end_s = match.groups()
            start_frame = time_to_frames(start_m, start_s, FPS)
            end_frame = time_to_frames(end_m, end_s, FPS)
            if end_frame > start_frame:
                clips.append((start_frame, end_frame, filename))
            else:
                print(f"Pominięto {filename}: czas końcowy nie jest po początkowym.")

    if not clips:
        print("Nie znaleziono żadnych plików pasujących do wzorca (np. 0m17s-0m32s.jpg).")
        return

    clips.sort(key=lambda x: x[0])

    width, height = 2560, 1440
    if Image is not None:
        try:
            with Image.open(os.path.join(FOLDER_PATH, clips[0][2])) as im:
                width, height = im.size
        except Exception:
            pass

    assets_xml = []
    spine_xml = []
    for i, (start_frame, end_frame, filename) in enumerate(clips):
        duration = end_frame - start_frame
        src = to_file_url(os.path.join(FOLDER_PATH, filename))
        assets_xml.append(
            f'        <asset id="r{i}" name="{filename}" src="{src}" start="0s" '
            f'duration="0s" hasVideo="1" format="f1" />'
        )
        spine_xml.append(
            f'                    <asset-clip ref="r{i}" offset="{start_frame}/{FPS}s" '
            f'name="{filename}" start="0s" duration="{duration}/{FPS}s" />'
        )

    fcpxml = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.5">
    <resources>
        <format id="f1" name="Custom Format" width="{width}" height="{height}" frameDuration="1/{FPS}s" />
{chr(10).join(assets_xml)}
    </resources>
    <library>
        <event name="Auto_Import">
            <project name="{PROJECT_NAME}">
                <sequence format="f1">
                    <spine>
{chr(10).join(spine_xml)}
                    </spine>
                </sequence>
            </project>
        </event>
    </library>
</fcpxml>
"""

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(fcpxml)

    print(f"Zapisano oś czasu z {len(clips)} kadrami do: {OUTPUT_PATH}")
    print("W Resolve: File -> Import -> Timeline... -> wskaż ten plik.")


if __name__ == "__main__":
    main()
