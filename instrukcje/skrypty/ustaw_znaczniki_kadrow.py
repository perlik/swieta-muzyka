import os
import re

def time_to_frames(m, s, fps):
    """Konwertuje minuty i sekundy na klatki na podstawie klatkażu projektu."""
    total_seconds = (int(m) * 60) + int(s)
    return int(round(total_seconds * fps))

def main():
    # Połączenie z API DaVinci Resolve (działa bezpośrednio w konsoli programu)
    resolve = bmd.scriptapp("Resolve")
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    timeline = project.GetCurrentTimeline()

    if not timeline:
        print("Błąd: Brak aktywnej osi czasu (timeline). Utwórz ją najpierw.")
        return

    # Pobieranie klatkażu projektu (np. 24, 25, 30, 60)
    fps_setting = project.GetSetting("timelineFrameRate")
    try:
        fps = float(fps_setting)
    except ValueError:
        fps = 25.0  # Domyślna wartość w razie błędu
        print(f"Nie udało się odczytać klatkażu. Używam domyślnie {fps} fps.")

    # ==========================================
    # TUTAJ WPISZ ŚCIEŻKĘ DO FOLDERU Z PLIKAMI:
    folder_path = r"/Volumes/ADATA SE880/_Święta Muzyka/_claude/psalm 27 - in progress - 6/images"
    # ==========================================

    # Kolor znaczników (jedna z wartości Resolve):
    # Blue, Cyan, Green, Yellow, Red, Pink, Purple, Fuchsia, Rose, Lavender, Sky, Mint, Lemon, Sand, Cocoa, Cream
    marker_color = "Blue"

    if not os.path.isdir(folder_path):
        print(f"Błąd: Podany folder '{folder_path}' nie istnieje.")
        return

    frames = []  # (start_frame, etykieta_pliku)
    for filename in os.listdir(folder_path):
        match = re.search(r"(\d+)m(\d+)s-(\d+)m(\d+)s", filename)
        if match:
            start_m, start_s, _end_m, _end_s = match.groups()
            start_frame = time_to_frames(start_m, start_s, fps)
            frames.append((start_frame, filename))

    if not frames:
        print("\nNie znaleziono żadnych plików pasujących do wzorca (np. 0m17s-0m32s.jpg).")
        return

    frames.sort(key=lambda x: x[0])

    existing = timeline.GetMarkers() or {}

    added = 0
    for i, (start_frame, filename) in enumerate(frames, start=1):
        if start_frame in existing:
            print(f"Pominięto: klatka {start_frame} ({filename}) — znacznik już tam istnieje.")
            continue
        ok = timeline.AddMarker(start_frame, marker_color, f"Kadr {i}", filename, 1)
        if ok:
            added += 1
            print(f"Znacznik: klatka {start_frame} — Kadr {i} ({filename})")
        else:
            print(f"Błąd przy dodawaniu znacznika na klatce {start_frame} ({filename}).")

    print(f"\nSukces! Dodano {added} znaczników na osi czasu (spośród {len(frames)} kadrów).")

if __name__ == "__main__":
    main()
