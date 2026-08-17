#!/usr/bin/env python3
"""
Etap 5 — obrabianie wygenerowanych kadrów.

Bierze surowe, numerowane pliki z Etapu 4 (`1.jpg`, `2.jpg`, ... w `images/`),
zmienia im nazwy na zakresy czasowe odczytane z `prompts/prompty.md`, przycina
centralnie do 16:9 i zapisuje jako JPEG quality 100, bez podpróbkowania chromy
(4:4:4), progresywny.

Zasady (patrz `instrukcje/etap5-obrobka-obrazkow.md`):
  - kadrujemy WYŁĄCZNIE przycięciem centralnym, nigdy nie skalujemy w dół,
  - nie skalujemy też w górę, gdy źródło jest mniejsze niż 2560x1440 —
    zostawiamy natywną rozdzielczość (skrypt to wypisuje jako ostrzeżenie),
  - nazwa pliku to pełny zakres `0m00s-0m14s.jpg`, nie sam znacznik startu,
  - etap jest czysto mechaniczny — nie oceniamy treści obrazków.

Kadr N z `prompty.md` odpowiada plikowi `N.jpg` (kolejność generowania z Etapu 4).

Użycie:
    python3 obrobka_kadrow.py "psalm N/images" [--prompty "psalm N/prompts/prompty.md"]
    python3 obrobka_kadrow.py "psalm N/images" --dry-run
"""
import argparse
import os
import re
import sys

from PIL import Image

MIN_W, MIN_H = 2560, 1440
ZAKRES = re.compile(r"`(\d+m\d+s-\d+m\d+s)`")


def zakresy_z_prompty(path):
    """Zakresy czasowe w kolejności występowania, bez powtórek."""
    out = []
    for m in ZAKRES.finditer(open(path, encoding="utf-8").read()):
        if m.group(1) not in out:
            out.append(m.group(1))
    return out


def kadruj_16_9(im):
    w, h = im.size
    if w * 9 == h * 16:
        return im, (w, h)
    if w * 9 > h * 16:                      # za szeroki -> docinamy boki
        nw, nh = h * 16 // 9, h
    else:                                   # za wysoki -> docinamy górę/dół
        nw, nh = w, w * 9 // 16
    left, top = (w - nw) // 2, (h - nh) // 2
    return im.crop((left, top, left + nw, top + nh)), (nw, nh)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images", help="katalog z surowymi kadrami z Etapu 4")
    ap.add_argument("--prompty", help="ścieżka do prompty.md (domyślnie ../prompts/prompty.md)")
    ap.add_argument("--dry-run", action="store_true", help="tylko wypisz, co by zrobił")
    a = ap.parse_args()

    img_dir = os.path.abspath(a.images)
    prompty = a.prompty or os.path.join(os.path.dirname(img_dir), "prompts", "prompty.md")
    if not os.path.isfile(prompty):
        sys.exit(f"BŁĄD: nie znaleziono prompty.md: {prompty}")

    zakresy = zakresy_z_prompty(prompty)
    numerowane = sorted(
        (f for f in os.listdir(img_dir)
         if re.fullmatch(r"\d+\.(jpg|jpeg|png)", f, re.I) and not f.startswith("._")),
        key=lambda f: int(os.path.splitext(f)[0]))

    if not numerowane:
        sys.exit(f"BŁĄD: brak numerowanych kadrów w {img_dir}")
    if len(numerowane) != len(zakresy):
        sys.exit(f"BŁĄD: {len(numerowane)} kadrów w images/, ale {len(zakresy)} zakresów "
                 f"w prompty.md — sprawdź, czy Etap 4 wygenerował komplet.")

    male = []
    for src, zakres in zip(numerowane, zakresy):
        src_path = os.path.join(img_dir, src)
        dst_path = os.path.join(img_dir, zakres + ".jpg")
        with Image.open(src_path) as im:
            w0, h0 = im.size
            im = im.convert("RGB")
            im, (w1, h1) = kadruj_16_9(im)
            print(f"{src:>8}  {w0}x{h0} -> {w1}x{h1}  {zakres}.jpg")
            if w1 < MIN_W or h1 < MIN_H:
                male.append(f"{zakres}.jpg ({w1}x{h1})")
            if not a.dry_run:
                im.save(dst_path, "JPEG", quality=100, subsampling=0,
                        progressive=True, optimize=True)
        if not a.dry_run and os.path.abspath(src_path) != os.path.abspath(dst_path):
            os.remove(src_path)

    print(f"\nGotowe: {len(numerowane)} kadrów, JPEG q100 4:4:4 progresywny.")
    if male:
        print("UWAGA: poniżej 2560x1440 (nie skalowano w górę, rozważ Upscale w Leonardo):")
        for m in male:
            print("  -", m)


if __name__ == "__main__":
    main()
