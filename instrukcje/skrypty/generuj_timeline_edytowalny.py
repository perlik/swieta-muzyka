"""
Generator W PEŁNI EDYTOWALNEJ osi czasu z obrazków (Etap 5 → montaż) dla
darmowej wersji DaVinci Resolve — następca `generuj_fcpxml_timeline.py`.

Wcześniej skrypt generował dwa warianty (FCPXML 1.8 i FCP7 XML). Wariant
FCPXML okazał się niepotrzebny w praktyce — generujemy więc tylko
`timeline_edytowalny_fcp7.xml`: legacy Final Cut Pro 7 XML (XMEML v5), gdzie
każdy still ma zadeklarowany masterclip dłuższy niż użyty fragment (zapas
HANDLE_SEC z każdej strony), więc trim/przejścia mają z czego brać.

Rozdzielczość sekwencji jest sztywno ustawiona na TARGET_WIDTH x TARGET_HEIGHT
(2560x1440, docelowa rozdzielczość projektu — patrz styl-teledysku.md), a NIE
odczytywana z rzeczywistych wymiarów plików w images/ — te bywają większe
(np. 2944x1656) i podstawienie ich wprost dawałoby złą rozdzielczość sekwencji
przy imporcie do Resolve.

Użycie:
    1. Ustaw niżej FOLDER_PATH (folder images/ danego psalmu, po Etapie 5 —
       pliki nazwane PEŁNYM zakresem czasu, np. 0m00s-0m15s.jpg) i FPS.
    2. Uruchom zwykłym: python3 generuj_timeline_edytowalny.py
    3. W DaVinci Resolve: File -> Import -> Timeline... -> wskaż
       `timeline_edytowalny_fcp7.xml`. Resolve utworzy nową oś czasu
       z obrazkami rozmieszczonymi wg nazw plików, z klipami, które można
       normalnie trimować i łączyć przejściami.
    4. Jeśli klipy nadal byłyby zablokowane: zaimportuj najpierw same JPG-i
       przez File -> Import Media do Media Pool, potem importuj XML
       z ODZNACZONĄ opcją "Automatically import source clips into media pool"
       — wtedy timeline linkuje do stilli już znanych Resolve.
"""

import os
import re
from urllib.parse import quote

# ==========================================
# TUTAJ WPISZ ŚCIEŻKĘ DO FOLDERU Z PLIKAMI (images/ po Etapie 5):
FOLDER_PATH = r"/Volumes/ADATA SE880/_Święta Muzyka/psalm 42 - in progress - 7/images"
# Gdzie zapisać plik wynikowy.
# Uwaga: mimo że skrypt czyta obrazki z images/, wynikowy plik timeline
# to plik projektu montażowego, więc ląduje w render/, nie w images/.
OUTPUT_XMEML = r"/Volumes/ADATA SE880/_Święta Muzyka/psalm 42 - in progress - 7/render/timeline_edytowalny_fcp7.xml"
# Klatkaż timeline'u (np. 25, 24, 30):
FPS = 25
# Nazwa projektu/sekwencji widoczna w Resolve:
PROJECT_NAME = "Auto Timeline"
# Zapas (handle) z każdej strony klipu, w sekundach — tyle maksymalnie da się
# wyciągnąć krawędź klipu / tyle miejsca mają przejścia:
HANDLE_SEC = 10
# Docelowa rozdzielczość sekwencji (2560x1440 — patrz styl-teledysku.md).
# Ustawiona sztywno, NIE odczytywana z plików w images/ (te bywają większe).
TARGET_WIDTH = 2560
TARGET_HEIGHT = 1440
# ==========================================


def time_to_frames(m, s, fps):
    total_seconds = (int(m) * 60) + int(s)
    return int(round(total_seconds * fps))


def to_file_url(path):
    # FCP7/FCPX używają formy file://localhost/... — Resolve akceptuje ją
    # w obu formatach; znaki spoza ASCII i spacje muszą być procentowane.
    return "file://localhost" + quote(path, safe="/")


def collect_clips():
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
    clips.sort(key=lambda x: x[0])
    return clips


def build_xmeml(clips, width, height):
    """Wariant 2 (zapasowy): FCP7 XML (XMEML v5) — masterclip każdego stilla
    dłuższy o HANDLE_SEC z każdej strony niż fragment użyty na osi czasu."""
    handle = HANDLE_SEC * FPS
    total = clips[-1][1] if clips else 0

    rate_block = (
        "<rate>\n"
        f"                                <timebase>{FPS}</timebase>\n"
        "                                <ntsc>FALSE</ntsc>\n"
        "                            </rate>"
    )

    clipitems = []
    for i, (start_frame, end_frame, filename) in enumerate(clips):
        length = end_frame - start_frame
        master_duration = length + 2 * handle
        pathurl = to_file_url(os.path.join(FOLDER_PATH, filename))
        clipitems.append(f"""                        <clipitem id="clipitem-{i + 1}">
                            <name>{filename}</name>
                            <enabled>TRUE</enabled>
                            <duration>{master_duration}</duration>
                            {rate_block}
                            <start>{start_frame}</start>
                            <end>{end_frame}</end>
                            <in>{handle}</in>
                            <out>{handle + length}</out>
                            <file id="file-{i + 1}">
                                <name>{filename}</name>
                                <pathurl>{pathurl}</pathurl>
                                <duration>{master_duration}</duration>
                                {rate_block}
                                <media>
                                    <video>
                                        <samplecharacteristics>
                                            <width>{width}</width>
                                            <height>{height}</height>
                                        </samplecharacteristics>
                                    </video>
                                </media>
                            </file>
                        </clipitem>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xmeml>
<xmeml version="5">
    <sequence id="sequence-1">
        <name>{PROJECT_NAME}</name>
        <duration>{total}</duration>
        {rate_block}
        <media>
            <video>
                <format>
                    <samplecharacteristics>
                        <width>{width}</width>
                        <height>{height}</height>
                        {rate_block}
                    </samplecharacteristics>
                </format>
                <track>
{chr(10).join(clipitems)}
                    <enabled>TRUE</enabled>
                    <locked>FALSE</locked>
                </track>
            </video>
        </media>
    </sequence>
</xmeml>
"""


def main():
    if not os.path.isdir(FOLDER_PATH):
        print(f"Błąd: Podany folder '{FOLDER_PATH}' nie istnieje.")
        return

    clips = collect_clips()
    if not clips:
        print("Nie znaleziono żadnych plików pasujących do wzorca (np. 0m17s-0m32s.jpg).")
        return

    content = build_xmeml(clips, TARGET_WIDTH, TARGET_HEIGHT)
    os.makedirs(os.path.dirname(OUTPUT_XMEML), exist_ok=True)
    with open(OUTPUT_XMEML, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Zapisano oś czasu z {len(clips)} kadrami do: {OUTPUT_XMEML}")

    print()
    print("W Resolve: File -> Import -> Timeline... -> wskaż timeline_edytowalny_fcp7.xml.")


if __name__ == "__main__":
    main()
