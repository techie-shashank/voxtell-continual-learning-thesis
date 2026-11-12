"""B1: trace every number in the thesis prose to a source (report only, never edits).

Usage: python reviews/tools/check_numbers.py thesis/introduction.tex [more .tex files]

Each number with a decimal point, a percentage, or a thousands separator is looked up in
  1. thesis/tables/* (generated from results/ by scripts/), with rounding to the printed precision,
  2. results/data_stats/* and results/experiment_index.csv,
  3. paper_notes/**/*.md (numbers quoted from papers),
  4. '% source:' / '% values:' comments within 6 lines of the sentence.
Output: one line per number with where it was found; UNTRACED lines need a human check.
Small integers without decimals (k = 5, six tasks, 108 volumes) are not checked; see the
'--ints' flag to include integers >= 10.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NUM = re.compile(r"(?<![\w.{])-?\d+(?:\{,\}\d{3})*(?:\.\d+)?(?:\\,\\%|\\%)?(?![\w}])")


def norm(tok):
    tok = tok.replace("{,}", "").replace("\\,", "").replace("\\%", "")
    return tok.lstrip("-")


def load_numbers(paths):
    """Map file -> set of number strings, plus rounded variants of floats."""
    found = {}
    for p in paths:
        try:
            txt = open(p, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        nums = set()
        for m in re.finditer(r"-?\d[\d,]*(?:\.\d+)?(?:[eE]-?\d+)?", txt):
            s = m.group(0).replace(",", "")
            nums.add(s.lstrip("-"))
            try:
                v = abs(float(s))
            except ValueError:
                continue
            for d in (0, 1, 2, 3):
                nums.add(f"{v:.{d}f}")
                nums.add(f"{v * 100:.{d}f}")  # fractions printed as percentages
        found[p] = nums
    return found


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    ints = "--ints" in sys.argv
    tables = glob.glob(os.path.join(ROOT, "thesis", "tables", "*"))
    stats = glob.glob(os.path.join(ROOT, "results", "data_stats", "**", "*.*"), recursive=True) + [os.path.join(ROOT, "results", "experiment_index.csv")]
    notes = glob.glob(os.path.join(ROOT, "paper_notes", "**", "*.md"), recursive=True)
    srcs = [("tables", load_numbers(tables)), ("results", load_numbers(stats)), ("paper_notes", load_numbers(notes))]
    untraced = 0
    for path in args:
        lines = open(path, encoding="utf-8").read().splitlines()
        for ln, raw in enumerate(lines, 1):
            if raw.lstrip().startswith("%"):
                continue
            text = re.sub(r"(?<!\\)%.*", "", raw)
            text = re.sub(r"\\(cite|cref|Cref|label|ref|url|includegraphics|input)(\[[^\]]*\])*\{[^}]*\}", " ", text)
            for m in NUM.finditer(text):
                tok = m.group(0)
                n = norm(tok)
                is_dec = "." in n
                if not (is_dec or "{,}" in tok or "%" in tok or (ints and n.isdigit() and int(n) >= 10)):
                    continue
                hits = []
                for name, src in srcs:
                    files = [os.path.relpath(f, ROOT) for f, s in src.items() if n in s]
                    if files:
                        hits.append(f"{name}: {', '.join(sorted(files)[:3])}{' …' if len(files) > 3 else ''}")
                window = "\n".join(lines[max(0, ln - 7):ln + 6])
                comments = [c for c in re.findall(r"%\s*(?:source|values|sources)[^\n]*", window) if n in c.replace("{,}", "").replace(",", "")]
                if comments:
                    hits.append("source comment")
                status = "ok" if hits else "UNTRACED"
                if not hits:
                    untraced += 1
                print(f"{os.path.relpath(path, ROOT)}:{ln} {status:8} {tok:>14}  {' | '.join(hits)}")
    print(f"# {untraced} untraced")


if __name__ == "__main__":
    main()
