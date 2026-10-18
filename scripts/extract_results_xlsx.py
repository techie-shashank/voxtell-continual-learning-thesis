"""Extract every table of results/few_shot_cl_results_fixed.xlsx into CSV files.

Values are copied verbatim as stored in the xlsx XML (no float parsing, rounding
or recomputation). Formulas are copied verbatim as well (shared formulas are
expanded by shifting row references, which is how Excel defines them).

Usage:
    python scripts/extract_results_xlsx.py [path/to/workbook.xlsx] [out_dir]

Only the Python standard library is used.
"""
import csv
import hashlib
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {
    "m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}
M = "{%s}" % NS["m"]

# Explicit file names for every block, keyed by (sheet name, title cell).
# Any block not listed here makes the script fail, so new tables are never
# silently skipped.
BLOCK_FILES = {
    ("ZSCL", "A1"): "zscl__original.csv",
    ("TIL-LoRA (isolated)", "A1"): "til_lora_isolated__rank8_original.csv",
    ("TIL-LoRA (isolated)", "A11"): "til_lora_isolated__rank16_original.csv",
    ("TIL-LoRA (isolated)", "A21"): "til_lora_isolated__rank32_original.csv",
    ("TIL-LoRA (isolated)", "A31"): "til_lora_isolated__rank64_original.csv",
    ("TIL-LoRA (isolated)", "A41"): "til_lora_isolated__rank128_original.csv",
    ("TIL-LoRA (isolated)", "A51"): "til_lora_isolated__rank8_reversed.csv",
    ("CIL-LoRA", "A1"): "cil_lora__rank128_original.csv",
    ("CIL-LoRA", "A12"): "cil_lora__rank256_original.csv",
    ("CIL-LoRA", "A23"): "cil_lora__rank256_reverse.csv",
    ("CIL-LoRA", "A34"): "cil_lora__rank128_original_replay0.1.csv",
    ("CIL-LoRA", "A45"): "cil_lora__rank4_original.csv",
    ("CIL-LoRA", "A56"): "cil_lora__rank512_original.csv",
    ("CIL-LoRA", "A67"): "cil_lora__rank32_original.csv",
    ("CIL-LoRA", "A78"): "cil_lora__rank1024_original.csv",
    ("CIL-LoRA", "A89"): "cil_lora__rank2048_original.csv",
    ("CIL-LoRA", "A100"): "cil_lora__rank1024_original_5shot.csv",
    ("CIL-LoRA", "A111"): "cil_lora__rank1024_original_10shot.csv",
    ("CIL-LoRA", "A122"): "cil_lora__rank1024_original_20shot.csv",
    ("CIL-LoRA", "A133"): "cil_lora__rank1024_reverse.csv",
    ("CIL-LoRA", "A144"): "cil_lora__rank1024_original_replay0.1.csv",
    ("TIL-LoRA", "A1"): "til_lora__rank4_original.csv",
    ("TIL-LoRA", "A12"): "til_lora__rank4_reverse.csv",
    ("TIL-LoRA", "A23"): "til_lora__rank8_original.csv",
    ("TIL-LoRA", "A34"): "til_lora__rank4_only_patellar.csv",
    ("TIL-LoRA", "A40"): "til_lora__rank8_original__duplicate_A40.csv",
    ("TIL-LoRA", "A51"): "til_lora__rank4_original_10shot.csv",
    ("TIL-LoRA", "A62"): "til_lora__rank4_original_5shot.csv",
    ("TIL-LoRA", "A73"): "til_lora__rank4_original_20shot.csv",
    ("CPE-CLIP", "A1"): "cpe_clip__original.csv",
    ("Fine-tuning", "A1"): "fine_tuning__original.csv",
    ("Fine-tuning", "A12"): "fine_tuning__original_20shot.csv",
    ("Fine-tuning", "A23"): "fine_tuning__original_5shot.csv",
    ("Fine-tuning", "A34"): "fine_tuning__original_10shot.csv",
    ("Fine-tuning", "A45"): "fine_tuning__reverse.csv",
}


def col2n(c):
    n = 0
    for ch in c:
        n = n * 26 + ord(ch) - 64
    return n


def n2col(n):
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def shift_rows(formula, dr):
    return re.sub(r"([A-Z]+)(\d+)", lambda m: m.group(1) + str(int(m.group(2)) + dr), formula)


def load(path):
    z = zipfile.ZipFile(path)
    shared_strings = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).findall("m:si", NS):
            shared_strings.append("".join(t.text or "" for t in si.iter(M + "t")))
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = {r.get("Id"): r.get("Target") for r in ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
    sheets = []
    for s in wb.findall("m:sheets/m:sheet", NS):
        root = ET.fromstring(z.read("xl/" + rels[s.get("{%s}id" % NS["r"])]))
        cells, masters, pending = {}, {}, []
        for c in root.iter(M + "c"):
            ref = c.get("r")
            ctype = c.get("t", "n")
            v = c.find("m:v", NS)
            f = c.find("m:f", NS)
            value = v.text if v is not None else None
            if ctype == "s" and value is not None:
                value = shared_strings[int(value)]
            elif ctype == "inlineStr":
                value = "".join(t.text or "" for t in c.iter(M + "t"))
            formula = None
            if f is not None:
                formula = f.text
                if f.get("t") == "shared":
                    if formula:
                        masters[f.get("si")] = (ref, formula)
                    else:
                        pending.append((ref, f.get("si")))
            if value is None and formula is None:
                continue
            m = re.match(r"([A-Z]+)(\d+)", ref)
            cells[(int(m.group(2)), col2n(m.group(1)))] = {
                "ref": ref, "type": ctype, "value": value, "formula": formula}
        for ref, si in pending:
            mref, mformula = masters[si]
            r = int(re.match(r"[A-Z]+(\d+)", ref).group(1))
            mr = int(re.match(r"[A-Z]+(\d+)", mref).group(1))
            m = re.match(r"([A-Z]+)(\d+)", ref)
            cells[(r, col2n(m.group(1)))]["formula"] = shift_rows(mformula, r - mr)
        merged = [mc.get("ref") for mc in root.findall("m:mergeCells/m:mergeCell", NS)]
        sheets.append({"name": s.get("name"), "state": s.get("state", "visible"),
                       "cells": cells, "merged": merged})
    return sheets


def block_titles(sheet):
    """Title rows are the rows directly above a header row with 'Pretrained' in column B."""
    return sorted(r - 1 for (r, c), d in sheet["cells"].items() if c == 2 and d["value"] == "Pretrained")


def write_block(sheet, top, bottom, path):
    cells = sheet["cells"]
    cols = sorted({c for (r, c) in cells if top <= r <= bottom})
    rows = []
    for r in range(top, bottom + 1):
        row = [cells[(r, c)]["value"] if (r, c) in cells else "" for c in cols]
        rows.append(row)
    while rows and not any(rows[-1]):
        rows.pop()
    header = rows[0]
    header[0] = header[0] or "row_label"
    with open(path, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(rows)
    last_row = top + len(rows) - 1
    return "%s%d:%s%d" % (n2col(cols[0]), top, n2col(cols[-1]), last_row)


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "results/few_shot_cl_results_fixed.xlsx"
    out = sys.argv[2] if len(sys.argv) > 2 else "results/extracted"
    os.makedirs(out, exist_ok=True)
    with open(src, "rb") as fh:
        print("source sha256:", hashlib.sha256(fh.read()).hexdigest())
    sheets = load(src)
    index = []
    all_cells = []
    seen = set()
    for sh in sheets:
        for (r, c), d in sorted(sh["cells"].items()):
            all_cells.append([sh["name"], d["ref"], d["type"], d["value"] if d["value"] is not None else "",
                              d["formula"] or ""])
        if sh["name"] == "Dashboard":
            rng = write_block(sh, 1, max(r for r, _ in sh["cells"]), os.path.join(out, "dashboard.csv"))
            index.append(("dashboard.csv", sh["name"], sh["state"], rng, ""))
            continue
        titles = block_titles(sh)
        max_row = max(r for r, _ in sh["cells"])
        for i, t in enumerate(titles):
            key = (sh["name"], "A%d" % t)
            if key not in BLOCK_FILES:
                raise SystemExit("Unmapped table: %s %s" % key)
            seen.add(key)
            bottom = (titles[i + 1] - 1) if i + 1 < len(titles) else max_row
            name = BLOCK_FILES[key]
            rng = write_block(sh, t + 1, bottom, os.path.join(out, name))
            index.append((name, sh["name"], sh["state"], rng, sh["cells"][(t, 1)]["value"]))
    missing = set(BLOCK_FILES) - seen
    if missing:
        raise SystemExit("Mapped tables not found: %s" % sorted(missing))
    with open(os.path.join(out, "all_cells.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["sheet", "cell", "xlsx_type", "stored_value", "formula"])
        w.writerows(all_cells)
    with open(os.path.join(out, "index.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["file", "sheet", "sheet_state", "cell_range", "table_title"])
        w.writerows(index)
    print("wrote %d tables + all_cells.csv + index.csv to %s" % (len(index), out))


if __name__ == "__main__":
    main()
