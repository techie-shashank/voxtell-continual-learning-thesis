"""Extract the Dice score of every test volume for every cell of every evaluation matrix.

Input:  results/experiment_index.csv and the eval.log of each cell
        (tasks/pretrained/<eval task>/test/logs/eval.log for the pretrained column,
         tasks/<trained task>/<eval task>/test/logs/eval.log for the others).
Output: thesis/tables/per_volume_dice.csv
        columns: experiment_id, row_task, stage (0 = pretrained, t = after task t),
                 case_id, dice

The eval.log files are appended to by later evaluations in the same job, and
some cells were evaluated more than once. A cell's scores are therefore taken
from the block in its log that (1) evaluates the cell's dataset, (2) has as
many volumes as the evaluation reported, and (3) whose mean reproduces the
value in eval_matrix.csv to 1e-5. If no block qualifies, the cell is listed as
missing and left out; nothing is guessed.

Usage (from the repository root):
    python scripts/extract_per_volume.py
"""
from __future__ import annotations

import csv
import re

import numpy as np

from _common import INDEX_FILE, REPO, load_eval_matrix

OUT_FILE = REPO / "thesis" / "tables" / "per_volume_dice.csv"
TOL = 1e-5

START = re.compile(r"Evaluation started \| dataset=(\S+) \| .*batches=(\d+)")
IMG = re.compile(r"Img Path: (\S+)")
BATCH = re.compile(r"Batch (\d+) \| Loss: \S+ \| Dice\(mean\): ([0-9.eE+-]+)")


def case_id(image_path: str) -> str:
    name = image_path.replace("\\", "/").split("/")[-1]
    name = name.removesuffix(".nii.gz")
    return name.removesuffix("_CT_HR")          # AeroPath: '14_CT_HR' -> '14'


def read_blocks(log_path):
    """Yield (dataset, expected volumes, [(case_id, dice), ...]) per evaluation block."""
    block = None
    image = None
    with open(log_path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = START.search(line)
            if m:
                if block:
                    yield block
                block = (m.group(1), int(m.group(2)), [])
                image = None
                continue
            if block is None:
                continue
            m = IMG.search(line)
            if m:
                image = m.group(1)
                continue
            m = BATCH.search(line)
            if m and image is not None:
                block[2].append((case_id(image), float(m.group(2))))
                image = None
    if block:
        yield block


def cell_log(exp_dir, stage_dir: str, eval_task: str):
    matches = sorted((exp_dir / "tasks" / stage_dir).glob(f"task_??_{eval_task}/test/logs/eval.log"))
    if len(matches) != 1:
        return None
    return matches[0]


def main():
    with open(INDEX_FILE, newline="", encoding="utf-8") as f:
        index = [r for r in csv.DictReader(f)
                 if r["status"] == "completed" and r["has_eval_matrix"] == "yes"]

    out_rows, missing, n_cells = [], [], 0
    for r in index:
        exp_dir = REPO / r["path"]
        tasks = r["tasks"].split(";")
        eval_tasks = tasks + [t for t in r["control_tasks"].split(";") if t]
        labels, _, values = load_eval_matrix(exp_dir)
        stage_dirs = ["pretrained"] + [f"task_{i + 1:02d}_{t}" for i, t in enumerate(tasks)]
        for row, eval_task in enumerate(eval_tasks):
            for stage, stage_dir in enumerate(stage_dirs):
                n_cells += 1
                target = values[row, stage]
                log = cell_log(exp_dir, stage_dir, eval_task)
                chosen = None
                if log is not None:
                    for dataset, expected, vols in read_blocks(log):
                        if (dataset == eval_task and len(vols) == expected and vols
                                and abs(np.mean([d for _, d in vols]) - target) <= TOL):
                            chosen = vols          # keep the last qualifying block
                if chosen is None:
                    missing.append((r["experiment_id"], eval_task, stage))
                    continue
                for cid, dice in chosen:
                    out_rows.append({"experiment_id": r["experiment_id"], "row_task": eval_task,
                                     "stage": stage, "case_id": cid, "dice": dice})

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["experiment_id", "row_task", "stage", "case_id", "dice"])
        writer.writeheader()
        writer.writerows(out_rows)
    print(f"{n_cells - len(missing)}/{n_cells} cells extracted, {len(out_rows)} volume scores "
          f"-> {OUT_FILE.relative_to(REPO)}")
    for m in missing:
        print("  missing:", *m)


if __name__ == "__main__":
    main()
