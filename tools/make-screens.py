"""Bakes a clean status bar (9:41, signal, wifi, full battery) into the real screenshots.
Original PNGs are never modified.

Usage (from anywhere):
    python3 tools/make-screens.py <dir with 01.png … 04.png>

Writes assets/{scan,pantry,recipe,goal}.{jpg,webp} at the repo root.
"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = sys.argv[1] if len(sys.argv) > 1 else "/workspace/optimat-real-screens"
BG = (248, 249, 250)
INK = (11, 13, 16)
S = 3
FONT = "/usr/share/fonts/truetype/sand-box/google/Noto Sans/NotoSans-VariableFont_wdth,wght.ttf"


def statusbar(im):
    W, H = im.size
    h = 170
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, h], fill=BG)
    # supersampled overlay
    L = Image.new("RGBA", (W * S // 1, h * S), (0, 0, 0, 0))
    g = ImageDraw.Draw(L)
    f = ImageFont.truetype(FONT, 60 * S)
    f.set_variation_by_axes([700, 100])
    g.text((205 * S, 88 * S), "9:41", font=f, fill=INK, anchor="mm")
    # island
    g.rounded_rectangle([402 * S, 34 * S, 776 * S, 143 * S], radius=55 * S, fill=(0, 0, 0))
    # signal
    x0 = 872
    for i in range(4):
        bh = 14 + i * 8
        g.rounded_rectangle([(x0 + i * 14) * S, (100 - bh) * S, (x0 + i * 14 + 9) * S, 100 * S], radius=2 * S, fill=INK)
    # wifi
    cx, cy = 975, 102
    for r in (30, 20, 10):
        g.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], 225, 315, fill=INK, width=int(5.5 * S))
    g.ellipse([(cx - 5) * S, (cy - 6) * S, (cx + 5) * S, (cy + 4) * S], fill=INK)
    # battery
    bx, by, bw, bh = 1030, 68, 70, 34
    g.rounded_rectangle([bx * S, by * S, (bx + bw) * S, (by + bh) * S], radius=10 * S, outline=(11, 13, 16, 110), width=3 * S)
    g.rounded_rectangle([(bx + 5) * S, (by + 5) * S, (bx + bw - 5) * S, (by + bh - 5) * S], radius=6 * S, fill=INK)
    g.rounded_rectangle([(bx + bw + 4) * S, (by + 11) * S, (bx + bw + 9) * S, (by + bh - 11) * S], radius=2 * S, fill=(11, 13, 16, 110))
    L = L.resize((W, h), Image.LANCZOS)
    im.paste(L, (0, 0), L)
    return im


def build(n):
    im = Image.open(f"{SRC}/0{n}.png").convert("RGB")
    if n == 4:  # drop the "Gör så här / Inga instruktioner ännu" block; show Mål directly after the ingredients
        a = im.crop((0, 0, im.width, 1170))
        b = im.crop((0, 1470, im.width, im.height))
        out = Image.new("RGB", im.size, BG)
        out.paste(a, (0, 0))
        out.paste(b, (0, 1170))
        im = out
    return statusbar(im)


names = {1: "scan", 2: "pantry", 3: "recipe", 4: "goal"}
assets = ROOT / "assets"
for n, o in names.items():
    im = build(n)
    im = im.resize((720, int(720 * im.height / im.width)), Image.LANCZOS)
    im.save(assets / f"{o}.jpg", quality=85, optimize=True, progressive=True)
    im.save(assets / f"{o}.webp", quality=85)
