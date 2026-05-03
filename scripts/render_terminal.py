#!/usr/bin/env python3
"""ANSI-aware terminal-to-PNG renderer.

Same approach as the sibling red-team toolkit: rasterise ANSI text
directly via PIL using a locally-installed monospace font. Avoids the
broken-CDN-webfont gotcha you hit with Rich's SVG export when running
offline.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


_ANSI16 = {
    30: (40, 42, 46),     31: (224, 92, 84),    32: (140, 188, 80),
    33: (236, 188, 80),   34: (96, 160, 224),   35: (192, 124, 200),
    36: (104, 188, 184),  37: (200, 200, 200),
    90: (104, 104, 104),  91: (240, 124, 116),  92: (160, 208, 120),
    93: (240, 220, 120),  94: (124, 184, 240),  95: (220, 156, 224),
    96: (140, 220, 220),  97: (240, 240, 240),
}
_BG_DEFAULT = (24, 24, 28)
_FG_DEFAULT = (220, 220, 220)
_ANSI_RE = re.compile(r"\x1b\[([0-9;]*)m")


def _parse_ansi(text: str):
    fg, bg, bold = _FG_DEFAULT, _BG_DEFAULT, False
    pos = 0
    for m in _ANSI_RE.finditer(text):
        if m.start() > pos:
            yield text[pos:m.start()], fg, bg, bold
        codes = [int(x) if x else 0 for x in m.group(1).split(";")] or [0]
        i = 0
        while i < len(codes):
            c = codes[i]
            if c == 0:
                fg, bg, bold = _FG_DEFAULT, _BG_DEFAULT, False
            elif c == 1:
                bold = True
            elif c == 22:
                bold = False
            elif c == 39:
                fg = _FG_DEFAULT
            elif c == 49:
                bg = _BG_DEFAULT
            elif c in _ANSI16:
                fg = _ANSI16[c]
            elif c in {n + 10 for n in _ANSI16}:
                bg = _ANSI16[c - 10]
            elif c == 38 and i + 4 < len(codes) and codes[i + 1] == 2:
                fg = (codes[i + 2], codes[i + 3], codes[i + 4]); i += 4
            elif c == 48 and i + 4 < len(codes) and codes[i + 1] == 2:
                bg = (codes[i + 2], codes[i + 3], codes[i + 4]); i += 4
            elif c == 38 and i + 2 < len(codes) and codes[i + 1] == 5:
                idx = codes[i + 2]; i += 2
                fg = _ANSI16.get(30 + (idx % 8), _FG_DEFAULT)
            i += 1
        pos = m.end()
    if pos < len(text):
        yield text[pos:], fg, bg, bold


def render(text: str, out_path: Path, *, font_size: int = 16,
           padding: int = 16) -> Path:
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
    bold_path = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
    font = ImageFont.truetype(font_path, font_size)
    bold = ImageFont.truetype(bold_path, font_size)

    tmp = Image.new("RGB", (1, 1))
    d = ImageDraw.Draw(tmp)
    bbox = d.textbbox((0, 0), "M", font=font)
    cell_w = bbox[2] - bbox[0]
    cell_h = int((bbox[3] - bbox[1]) * 1.55)

    lines = text.splitlines() or [""]
    max_cols = max((len(_ANSI_RE.sub("", ln)) for ln in lines), default=1)
    img_w = max_cols * cell_w + 2 * padding
    img_h = len(lines) * cell_h + 2 * padding

    img = Image.new("RGB", (img_w, img_h), _BG_DEFAULT)
    d = ImageDraw.Draw(img)
    for row, line in enumerate(lines):
        x = padding
        y = padding + row * cell_h
        for chunk, fg, bg, is_bold in _parse_ansi(line):
            if not chunk:
                continue
            chunk_w = len(chunk) * cell_w
            if bg != _BG_DEFAULT:
                d.rectangle([x, y, x + chunk_w, y + cell_h], fill=bg)
            d.text((x, y), chunk, font=(bold if is_bold else font), fill=fg)
            x += chunk_w

    img.save(out_path, "PNG")
    return out_path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--in", dest="in_path", required=False)
    p.add_argument("--out", dest="out_path", required=True)
    p.add_argument("--font-size", type=int, default=16)
    args = p.parse_args(argv)
    text = Path(args.in_path).read_text(encoding="utf-8") if args.in_path else sys.stdin.read()
    out = Path(args.out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    render(text, out, font_size=args.font_size)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
