#!/usr/bin/env python3
"""Compose entry.png for make.fun news-image-20261121.

Front-page layout, 1024x1024: a dated masthead over a 2x2 grid of
editorial illustrations, each with a kicker, a headline and one
supporting line. All four stories were reported on, or developed on,
Saturday 21 November 2026 (see the story list in README.md).

Run:  python3 build_image.py   (writes entry.png next to this file)
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
PANELS_DIR = os.path.join(HERE, "panels")
OUT_PATH = os.path.join(HERE, "entry.png")

CANVAS = (1024, 1024)
NAVY = (15, 42, 74)
NAVY_LIGHT = (24, 62, 102)
PAPER = (248, 246, 240)
INK = (18, 18, 18)
GREY = (90, 90, 90)
RULE = (196, 52, 40)          # brick-red rule / kicker colour
WHITE = (255, 255, 255)

HEADER_H = 148
MARGIN = 12
GUTTER = 12
CELL_W = (CANVAS[0] - 2 * MARGIN - GUTTER) // 2        # 494
CELL_H = (CANVAS[1] - HEADER_H - 2 * MARGIN - GUTTER) // 2  # 420
IMG_H = 280
STRIP_H = CELL_H - IMG_H                               # 140

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_MASTHEAD = font("DejaVuSans-Bold.ttf", 30)
F_DATE = font("DejaVuSans-Bold.ttf", 52)
F_SUB = font("DejaVuSans.ttf", 22)
F_KICKER = font("DejaVuSans-Bold.ttf", 20)
F_HEAD = font("DejaVuSans-Bold.ttf", 26)
F_LINE = font("DejaVuSans.ttf", 20)

# (panel file, kicker, headline lines, supporting lines)
STORIES = [
    ("panel_cop31.png", "CLIMATE  •  ANTALYA",
     ["COP31 runs into", "overtime"],
     ["No deal as talks spill into Saturday;", "fossil fuels still unmentioned."]),
    ("panel_akvan.png", "WEATHER  •  INDIA",
     ["Akvan's rain soaks", "Bengal"],
     ["300,000 evacuated; storm weakens", "inland, no major damage reported."]),
    ("panel_poland.png", "SECURITY  •  POLAND",
     ["NATO chief heads", "to Warsaw"],
     ["After Russian missiles crashed in", "Poland, Warsaw calls it provocation."]),
    ("panel_rahul.png", "SPORT  •  WELLINGTON",
     ["Rahul completes", "the SENA set"],
     ["Century in Wellington: first Indian", "opener with tons in all four lands."]),
]


def centre_crop(img, target_w, target_h):
    """Crop to the target aspect ratio, centred, then resize."""
    w, h = img.size
    target_ratio = target_w / target_h
    ratio = w / h
    if ratio > target_ratio:  # too wide: trim sides
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:  # too tall: trim top/bottom
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    return img.resize((target_w, target_h), Image.LANCZOS)


def build():
    canvas = Image.new("RGB", CANVAS, PAPER)
    draw = ImageDraw.Draw(canvas)

    # ---- Masthead -----------------------------------------------------
    draw.rectangle([0, 0, CANVAS[0], HEADER_H], fill=NAVY)
    draw.rectangle([0, HEADER_H - 6, CANVAS[0], HEADER_H], fill=RULE)
    masthead = "THE WORLD IN ONE IMAGE"
    draw.text((MARGIN + 4, 12), masthead, font=F_MASTHEAD, fill=WHITE)
    date = "SATURDAY 21 NOVEMBER 2026"
    draw.text((MARGIN + 4, 48), date, font=F_DATE, fill=WHITE)
    sub = "Four stories from today  •  make.fun news-image-20261121"
    draw.text((MARGIN + 4, 112), sub, font=F_SUB, fill=(205, 216, 228))

    # ---- Four panels --------------------------------------------------
    for idx, (fname, kicker, head_lines, sub_lines) in enumerate(STORIES):
        row, col = divmod(idx, 2)
        x = MARGIN + col * (CELL_W + GUTTER)
        y = HEADER_H + MARGIN + row * (CELL_H + GUTTER)

        path = os.path.join(PANELS_DIR, fname)
        img = Image.open(path).convert("RGB")
        img = centre_crop(img, CELL_W, IMG_H)
        canvas.paste(img, (x, y))

        strip_y = y + IMG_H
        draw.rectangle([x, strip_y, x + CELL_W, strip_y + STRIP_H],
                       fill=WHITE, outline=(200, 200, 200))
        tx = x + 12
        ty = strip_y + 8
        draw.text((tx, ty), kicker, font=F_KICKER, fill=RULE)
        ty += 26
        for line in head_lines:
            draw.text((tx, ty), line, font=F_HEAD, fill=INK)
            ty += 30
        for line in sub_lines:
            draw.text((tx, ty), line, font=F_LINE, fill=GREY)
            ty += 22

    canvas.save(OUT_PATH, "PNG", optimize=True)
    print(f"wrote {OUT_PATH} {canvas.size}")


if __name__ == "__main__":
    build()
