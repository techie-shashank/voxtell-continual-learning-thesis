"""Compile the standalone TikZ figures and check their width.

Every thesis/figures/tikz/ch*.tex (standalone class, shared preamble.tex) is compiled with
pdfLaTeX in that folder and copied to thesis/figures/<name>.pdf, which the thesis includes.
Optionally renders 400 dpi PNGs and a 3 x 2 grid of crops for the visual check
(CLAUDE.md, TikZ diagram rules) into a given folder.

Usage (from the repository root):
    python scripts/build_tikz.py                    # build all
    python scripts/build_tikz.py --render DIR       # build and render full images + crops
"""
import argparse
import shutil
import subprocess
from pathlib import Path

from _common import REPO

TIKZ = REPO / "thesis" / "figures" / "tikz"
FIGURES = REPO / "thesis" / "figures"
TEXT_WIDTH_PT = 460.93457            # \textwidth from thesis_main.log
PT_PER_BP = 72.27 / 72


def build(tex: Path) -> Path:
    run = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                         cwd=TIKZ, capture_output=True, text=True)
    if run.returncode != 0:
        print(run.stdout[-3000:])
        raise SystemExit(f"pdflatex failed for {tex.name}")
    pdf = TIKZ / f"{tex.stem}.pdf"
    out = FIGURES / pdf.name
    shutil.copyfile(pdf, out)
    for ext in (".aux", ".log", ".pdf"):        # keep only the sources in figures/tikz
        (TIKZ / f"{tex.stem}{ext}").unlink(missing_ok=True)
    return out


def width_pt(pdf: Path) -> float:
    import fitz  # PyMuPDF
    with fitz.open(pdf) as d:
        return d[0].rect.width * PT_PER_BP


def render(pdf: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    full = out_dir / pdf.stem
    subprocess.run(["pdftoppm", "-png", "-r", "400", "-singlefile", str(pdf), str(full)], check=True)
    from PIL import Image
    img = Image.open(f"{full}.png")
    w, h = img.size
    cols, rows = 3, 2
    for r in range(rows):
        for c in range(cols):
            box = (c * w // cols, r * h // rows, (c + 1) * w // cols, (r + 1) * h // rows)
            img.crop(box).save(out_dir / f"{pdf.stem}_crop_r{r}c{c}.png")
    print(f"  rendered {full}.png and {rows * cols} crops")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--render", type=Path, default=None)
    args = ap.parse_args()
    for tex in sorted(TIKZ.glob("ch*.tex")):
        pdf = build(tex)
        w = width_pt(pdf)
        status = "ok" if w <= TEXT_WIDTH_PT else "TOO WIDE"
        print(f"Wrote thesis/figures/{pdf.name}: width {w:.1f} pt of {TEXT_WIDTH_PT:.1f} pt ({status})")
        if args.render:
            render(pdf, args.render)


if __name__ == "__main__":
    main()
