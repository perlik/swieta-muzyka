import os
import re

def time_to_frames(m, s, fps):
    """Konwertuje minuty i sekundy na klatki na podstawie klatkażu projektu."""
    total_seconds = (int(m) * 60) + int(s)
    return int(total_seconds * fps)

def main():
    # Połączenie z API DaVinci Resolve (działa bezpośrednio w konsoli programu)
    resolve = bmd.scriptapp("Resolve")
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    mediaPool = project.GetMediaPool()
    timeline = project.GetCurrentTimeline()

    if not timeline:
        print("Błąd: Brak aktywnej osi czasu (timeline). Utwórz ją najpierw.")
        return

    # Pobieranie klatkażu projektu (np. 24, 25, 30, 60)
    fps_setting = project.GetSetting("timelineFrameRate")
    try:
        fps = float(fps_setting)
    except ValueError:
        fps = 25.0 # Domyślna wartość w razie błędu
        print(f"Nie udało się odczytać klatkażu. Używam domyślnie {fps} fps.")

    # ==========================================
    # TUTAJ WPISZ ŚCIEŻKĘ DO FOLDERU Z PLIKAMI:
    folder_path = r"/Volumes/ADATA SE880/_Święta Muzyka/_claude/psalm 103 - in progress - 7/images" 
    # ==========================================

    if not os.path.isdir(folder_path):
        print(f"Błąd: Podany folder '{folder_path}' nie istnieje.")
        return

    print("Importowanie plików do Media Pool...")
    # Importowanie wszystkich plików ze wskazanego folderu
    items = mediaPool.ImportMedia(folder_path)

    if not items:
        print("Nie znaleziono plików lub nie udało się ich zaimportować.")
        return

    clips_to_add = []

    for item in items:
        clip_name = item.GetClipProperty("Clip Name")
        
        # Wyrażenie regularne szukające wzorca: XmYs-AmBs
        match = re.search(r"(\d+)m(\d+)s-(\d+)m(\d+)s", clip_name)
        if match:
            start_m, start_s, end_m, end_s = match.groups()

            # Przeliczanie czasu z nazwy pliku na klatki
            start_frame = time_to_frames(start_m, start_s, fps)
            end_frame = time_to_frames(end_m, end_s, fps)
            
            # Obliczanie długości trwania obrazka
            duration_frames = end_frame - start_frame

            if duration_frames > 0:
                clip_info = {
                    "mediaPoolItem": item,
                    "startFrame": 0,                    # Zaczynamy od początku klipu/obrazka
                    "endFrame": duration_frames,        # Ustawiamy czas trwania na osi czasu
                    "recordFrame": start_frame          # Wrzucamy w konkretne miejsce na osi czasu
                }
                clips_to_add.append(clip_info)
                print(f"Przygotowano: {clip_name} -> start: {start_frame} klatka, długość: {duration_frames} klatek.")
            else:
                print(f"Pominięto {clip_name}: czas końcowy jest mniejszy lub równy początkowemu.")

    if clips_to_add:
        # Sortowanie klipów po czasie startu dla zachowania porządku
        clips_to_add.sort(key=lambda x: x["recordFrame"])
        
        # Automatyczne wrzucenie wszystkiego na timeline
        mediaPool.AppendToTimeline(clips_to_add)
        print(f"\nSukces! Dodano {len(clips_to_add)} plików na oś czasu.")
    else:
        print("\nNie znaleziono żadnych plików pasujących do wzorca (np. 0m17s-0m32s.jpg).")

if __name__ == "__main__":
    main()