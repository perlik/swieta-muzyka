#!/usr/bin/env python3
"""
Pomocnik Etapu 8 — arkusze podglądowe kadrów do ustalenia `kierunki-ruchu.tsv`.

Etap 8 wymaga OBEJRZENIA każdego kadru i zapisania, po której stronie leży motyw
główny (patrz `instrukcje/etap8-timeline-davinci.md` § „Plik kierunków ruchu").
Czytanie 20-30 pełnowymiarowych JPG-ów jest kosztowne, więc ten skrypt składa je
w kilka arkuszy 2x2 z numerem i nazwą pliku wypisanymi na każdym kadrze oraz
pionową linią środka, która ułatwia ocenę „lewo czy prawo".

Użycie:
    python3 arkusz_kadrow.py "psalm N/images" --out /katalog/na/arkusze
"""
import argparse
import os
import re

from PIL import Image, ImageDraw, ImageFont

ZAKRES = re.compile(r"^\d+m\d+s-\d+m\d+s\.jpg$", re.I)
FONT = "/Applications/HP.app/Contents/Resources/Fonts/Lora-Regular.ttf"


def czas(nazwa):
    m = re.match(r"(\d+)m(\d+)s-", nazwa)
    return int(m.group(1)) * 60 + int(m.group(2))


def font(size):
    for p in (FONT, "/System/Library/Fonts/Supplemental/Arial.ttf"):
        if os.path.isfile(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images")
    ap.add_argument("--out", required=True, help="katalog na arkusze")
    ap.add_argument("--kafelek", type=int, default=640, help="szerokość jednego kadru")
    ap.add_argument("--na-arkusz", type=int, default=4)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    pliki = sorted((f for f in os.listdir(a.images) if ZAKRES.match(f)), key=czas)
    tw = a.kafelek
    th = tw * 9 // 16
    f = font(max(18, tw // 26))

    for i in range(0, len(pliki), a.na_arkusz):
        grupa = pliki[i:i + a.na_arkusz]
        kol = 2
        wier = (len(grupa) + kol - 1) // kol
        ark = Image.new("RGB", (tw * kol, th * wier), (20, 20, 20))
        d = ImageDraw.Draw(ark)
        for j, nazwa in enumerate(grupa):
            with Image.open(os.path.join(a.images, nazwa)) as im:
                im = im.convert("RGB").resize((tw, th), Image.LANCZOS)
            x, y = (j % kol) * tw, (j // kol) * th
            ark.paste(im, (x, y))
            d.line([(x + tw // 2, y), (x + tw // 2, y + th)], fill=(255, 0, 0), width=1)
            etykieta = f"{i + j + 1}. {nazwa}"
            box = d.textbbox((0, 0), etykieta, font=f)
            d.rectangle([x + 6, y + 6, x + 14 + box[2], y + 14 + box[3]], fill=(0, 0, 0))
            d.text((x + 10, y + 10), etykieta, fill=(255, 255, 255), font=f)
        out = os.path.join(a.out, f"arkusz{i // a.na_arkusz + 1}.jpg")
        ark.save(out, "JPEG", quality=88)
        print(out, "->", ", ".join(grupa))


if __name__ == "__main__":
    main()
