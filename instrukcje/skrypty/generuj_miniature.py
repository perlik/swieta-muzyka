"""
Generator miniatury (Etap 7) — patrz instrukcje/etap7-miniatura.md.

Użycie:
    python3 generuj_miniature.py <klatka_ze_stage5.jpg> <numer_psalmu> <plik_wyjsciowy.jpg>

Klatka wejściowa to plik już istniejący w images/ (po Etapie 5), wskazany
w prompty.md adnotacją "baza miniatury" — niekoniecznie pierwszy kadr,
nie trzeba nic wyciągać przez ffmpeg.
"""

import sys
import colorsys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_PATH = "/Applications/HP.app/Contents/Frameworks/ImageEditor.framework/Versions/A/Resources/Lora-Regular.ttf"
W, H = 1280, 720

PSALM_SIZE = 130
SPIEWANY_SIZE = 105
PADDING = 26
LEFT_MARGIN = 45
BOTTOM_MARGIN = 35
PANEL_OPACITY = int(round(255 * 0.80))
PANEL_RADIUS = 30
LINE_GAP = 8

IVORY = (255, 255, 240)
WHITE = (255, 255, 255)
SHADOW = (0, 0, 0, 140)


def dominant_hue(img):
    small = img.convert("RGB").resize((160, 90))
    hue_weight = {}
    for r, g, b in small.getdata():
        h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
        if s < 0.15 or v < 0.15 or v > 0.97:
            continue
        bucket = int(h * 36)
        hue_weight[bucket] = hue_weight.get(bucket, 0) + s
    if not hue_weight:
        return 0.5
    best = max(hue_weight, key=hue_weight.get)
    return best / 36


def panel_color(hue):
    r, g, b = colorsys.hls_to_rgb(hue, 0.18, 0.45)
    return (int(r * 255), int(g * 255), int(b * 255), PANEL_OPACITY)


def cover_resize(img, target_w, target_h):
    src_w, src_h = img.size
    src_ratio = src_w / src_h
    target_ratio = target_w / target_h
    if src_ratio > target_ratio:
        new_h = target_h
        new_w = int(new_h * src_ratio)
    else:
        new_w = target_w
        new_h = int(new_w / src_ratio)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))


def make_thumbnail(frame_path, psalm_number, out_path):
    base = Image.open(frame_path)
    base = cover_resize(base, W, H).convert("RGB")

    hue = dominant_hue(base)
    fill = panel_color(hue)

    font_psalm = ImageFont.truetype(FONT_PATH, PSALM_SIZE)
    font_spiewany = ImageFont.truetype(FONT_PATH, SPIEWANY_SIZE)

    tmp_draw = ImageDraw.Draw(base)
    line1 = f"Psalm {psalm_number}"
    line2 = "śpiewany"

    b1 = tmp_draw.textbbox((0, 0), line1, font=font_psalm)
    b2 = tmp_draw.textbbox((0, 0), line2, font=font_spiewany)
    w1, h1 = b1[2] - b1[0], b1[3] - b1[1]
    w2, h2 = b2[2] - b2[0], b2[3] - b2[1]
    block_w = max(w1, w2)
    block_h = h1 + LINE_GAP + h2

    panel_left = LEFT_MARGIN
    panel_top = H - BOTTOM_MARGIN - block_h - 2 * PADDING
    panel_right = panel_left + block_w + 2 * PADDING
    panel_bottom = panel_top + block_h + 2 * PADDING

    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    shadow_offset = 10
    shadow_box = [
        panel_left + shadow_offset,
        panel_top + shadow_offset,
        panel_right + shadow_offset,
        panel_bottom + shadow_offset,
    ]
    odraw.rounded_rectangle(shadow_box, radius=PANEL_RADIUS, fill=SHADOW)
    overlay = overlay.filter(ImageFilter.GaussianBlur(12))
    odraw = ImageDraw.Draw(overlay)

    odraw.rounded_rectangle(
        [panel_left, panel_top, panel_right, panel_bottom],
        radius=PANEL_RADIUS,
        fill=fill,
    )

    text_x1 = panel_left + PADDING + (block_w - w1) / 2
    text_x2 = panel_left + PADDING + (block_w - w2) / 2
    text_y1 = panel_top + PADDING - b1[1]
    text_y2 = text_y1 + h1 + LINE_GAP - (b2[1] - b1[1])

    text_shadow_offset = 3
    odraw.text((text_x1 + text_shadow_offset, text_y1 + text_shadow_offset), line1, font=font_psalm, fill=(0, 0, 0, 120))
    odraw.text((text_x2 + text_shadow_offset, text_y2 + text_shadow_offset), line2, font=font_spiewany, fill=(0, 0, 0, 120))

    odraw.text((text_x1, text_y1), line1, font=font_psalm, fill=IVORY + (255,))
    odraw.text((text_x2, text_y2), line2, font=font_spiewany, fill=WHITE + (255,))

    result = Image.alpha_composite(base.convert("RGBA"), overlay).convert("RGB")
    result.save(out_path, quality=95)
    print(f"saved {out_path} (hue={hue:.2f}, panel_fill_rgb={fill[:3]})")


if __name__ == "__main__":
    frame_path, psalm_number, out_path = sys.argv[1], sys.argv[2], sys.argv[3]
    make_thumbnail(frame_path, psalm_number, out_path)
