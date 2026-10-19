"""Shared helpers for the result scripts: paths, config parsing, matrix loading.

Only the Python standard library and numpy are used. The experiment configs are
parsed with a small YAML-subset reader (block mappings, block lists, scalars),
because PyYAML is not installed in the analysis environment. It raises on any
construct it does not understand instead of guessing.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[1]
RESULTS = REPO / "results"
EXPERIMENTS = RESULTS / "hpc" / "experiments" / "continual"
SLURM_LOGS = RESULTS / "hpc" / "logs"
INDEX_FILE = RESULTS / "experiment_index.csv"

# Task order as configured in code/configs/continual/lora.yaml.
ORIGINAL_ORDER = [
    "skm_tea_lateral_tibial",
    "skm_tea_medial_tibial",
    "skm_tea_femoral",
    "skm_tea_patellar",
    "skm_tea_medial_meniscus",
    "skm_tea_lateral_meniscus",
]


# --------------------------------------------------------------------------
# YAML subset
# --------------------------------------------------------------------------

def _scalar(text: str):
    text = text.strip()
    if text in ("", "null", "~"):
        return None
    if text in ("true", "false"):
        return text == "true"
    for cast in (int, float):
        try:
            return cast(text)
        except ValueError:
            pass
    if len(text) >= 2 and text[0] == text[-1] and text[0] in "'\"":
        return text[1:-1]
    return text


def _lines(path: Path):
    out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if "\t" in raw[: len(raw) - len(raw.lstrip())]:
            raise ValueError(f"{path}: tab indentation is not supported")
        out.append((len(raw) - len(raw.lstrip(" ")), raw.strip()))
    return out


def _parse_block(lines, i, indent):
    """Parse the block starting at lines[i] with the given indentation."""
    if lines[i][1].startswith("- "):
        result = []
        while i < len(lines) and lines[i][0] == indent and lines[i][1].startswith("- "):
            item = lines[i][1][2:]
            if ":" in item and not item.endswith(":") and ": " not in item:
                raise ValueError(f"unsupported list item: {item!r}")
            if ":" in item:
                # list item that is a mapping: re-indent its first key
                lines[i] = (indent + 2, item)
                value, i = _parse_block(lines, i, indent + 2)
            else:
                value, i = _scalar(item), i + 1
            result.append(value)
        return result, i
    result = {}
    while i < len(lines) and lines[i][0] == indent:
        text = lines[i][1]
        if text.startswith("- "):
            break
        key, sep, rest = text.partition(":")
        if not sep:
            raise ValueError(f"cannot parse line: {text!r}")
        rest = rest.strip()
        i += 1
        if rest:
            result[key.strip()] = _scalar(rest)
        elif i < len(lines) and (lines[i][0] > indent or
                                 (lines[i][0] == indent and lines[i][1].startswith("- "))):
            value, i = _parse_block(lines, i, lines[i][0])
            result[key.strip()] = value
        else:
            result[key.strip()] = None
    return result, i


def read_config(path: Path) -> dict:
    lines = _lines(path)
    data, end = _parse_block(lines, 0, lines[0][0])
    if end != len(lines):
        raise ValueError(f"{path}: unparsed content from line {end + 1}")
    return data


# --------------------------------------------------------------------------
# Experiments
# --------------------------------------------------------------------------

def experiment_dirs() -> list[Path]:
    """Every experiment directory (one that holds an eval_matrix.csv)."""
    return sorted(p.parent for p in EXPERIMENTS.rglob("eval_matrix.csv")
                  if p.parent.name.startswith("exp_"))


def load_eval_matrix(exp_dir: Path):
    """Return (row labels, column labels, values) of an experiment's eval_matrix.csv.

    Rows: the trained tasks in task order, then the control task(s).
    Columns: 'Pretrained', then one checkpoint after each training task.
    Entry [i, s]: mean Dice on row i, evaluated with checkpoint s.
    """
    with open(exp_dir / "eval_matrix.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    cols = rows[0][1:]
    labels = [r[0] for r in rows[1:]]
    values = np.array([[float(v) if v != "" else np.nan for v in r[1:]]
                       for r in rows[1:]], dtype=float)
    return labels, cols, values


def read_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
