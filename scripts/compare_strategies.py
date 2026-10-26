"""Paired bootstrap intervals for the difference of every metric between two experiments.

Input:  results/experiment_index.csv, each experiment's eval_matrix.csv and
        thesis/tables/per_volume_dice.csv (scripts/extract_per_volume.py).
Output: thesis/tables/cl_differences.csv (one row per pair of experiments and metric).

Why. cl_metrics.csv gives an interval for each experiment on its own. Two such
intervals can overlap although one experiment is better on almost every
resample, because both are evaluated on the same test volumes and their errors
are correlated. The question "does A forget less than B?" needs an interval of
the difference A - B computed on the same resamples.

Method. The test volumes are resampled once (B = 2000 draws, fixed seed): the
SKM-TEA test scans with replacement, the same draw for every task, checkpoint
and experiment, and the control-task volumes separately. Every metric of every
experiment is recomputed on each draw with the functions of
compute_cl_metrics.py, so the difference of two experiments on one draw is a
paired difference. Columns: diff (on the full test set), diff_std (bootstrap
standard deviation), diff_ci_low/_ci_high (2.5 and 97.5 percentiles) and
share_a_greater (fraction of draws with A > B).

Pairs. All pairs of experiments that have a role in the index and the same
evaluated tasks, plus the 'Pretrained model' reference row of each task order.
Tagged evaluations (best_validation, weight_ensemble) enter as entries of their own, with id
"<experiment_id>:<tag>", so that, e.g., the best-validation checkpoints of two runs or the
weight ensemble and the student of one run can be compared on the same draws. Pairs are formed between task orders
too: the metrics are defined per run, and all runs share the same test volumes.
Joint fine-tuning (one training stage, evaluated on the six structures) is paired
with the sequential runs on the metrics both have: Final Performance and the
control-task drop.

Interpretation. The interval reflects the choice of test volumes only, not
training randomness (one seed per configuration) or the choice of support set.
It is not a significance test: the intervals are unadjusted for the number of
comparisons, so only comparisons fixed in advance should be read from it, and
the word "significant" should not be used for them. For final_forgetting and
control_drop lower is better; for all other metrics higher is better.

Usage (from the repository root):
    python scripts/compare_strategies.py
"""
from __future__ import annotations

import csv
from itertools import combinations

import numpy as np

from _common import INDEX_FILE, REPO, evaluations
from compute_cl_metrics import (BOOTSTRAP_SEED, METRICS, N_BOOTSTRAP, all_metrics,
                                load_volumes, split_matrix, volume_tensor)

OUT_FILE = REPO / "thesis" / "tables" / "cl_differences.csv"


def cases_of(cells, row_task: str) -> list[str]:
    return sorted(cells[(row_task, 0)])


def metric_samples(tv: np.ndarray, cv: np.ndarray, idx_t: np.ndarray, idx_c: np.ndarray,
                   joint: bool = False) -> dict:
    """metric -> array [B] of the metric on each bootstrap draw (NaN where undefined)."""
    out = {k: np.full(len(idx_t), np.nan) for k in METRICS}
    for b in range(len(idx_t)):
        a = tv[:, :, idx_t[b]].mean(axis=2)
        c = cv[:, :, idx_c[b]].mean(axis=2)
        for k, v in all_metrics(a, c, joint).items():
            if v != "":
                out[k][b] = v
    return out


def main():
    with open(INDEX_FILE, newline="", encoding="utf-8") as f:
        index = [r for r in csv.DictReader(f)
                 if r["status"] == "completed" and r["has_eval_matrix"] == "yes" and r["role"].strip()]
    volumes = load_volumes()

    entries = []        # dicts with label, n_tasks, point metrics, tensors
    task_cases = control_cases = None
    for r in index:
        tasks = r["tasks"].split(";")
        eval_tasks = (r["eval_tasks"] or r["tasks"]).split(";")
        joint = r["strategy"] == "joint_fine_tuning"
        controls = [t for t in r["control_tasks"].split(";") if t]
        for name, eval_dir, _ in evaluations(REPO / r["path"]):
            cells = volumes[(r["experiment_id"], name)]
            a, c = split_matrix(eval_dir, tasks, controls, eval_tasks)
            tv = volume_tensor(cells, eval_tasks, len(tasks) + 1, a)
            cv = volume_tensor(cells, controls, len(tasks) + 1, c)
            # Paired resampling needs the same test volumes in every experiment.
            tc, cc = cases_of(cells, eval_tasks[0]), cases_of(cells, controls[0])
            if task_cases is None:
                task_cases, control_cases = tc, cc
            if tc != task_cases or cc != control_cases:
                raise ValueError(f"{r['experiment_id']}: test volumes differ from the other experiments")
            main = name == "main"
            entries.append({"id": r["experiment_id"] if main else f"{r['experiment_id']}:{name}",
                            "label": r["label"] if main else f"{r['label']} [{name}]", "order": r["task_order"],
                            "n_tasks": len(tasks), "rows": frozenset(eval_tasks), "joint": joint, "main": main,
                            "point": all_metrics(a, c, joint), "tv": tv, "cv": cv})

    # Pretrained-model reference per task order: every checkpoint equals the pretrained column.
    for order in sorted({e["order"] for e in entries if e["n_tasks"] > 1 and not e["joint"]}):
        first = next(e for e in entries if e["order"] == order and e["n_tasks"] > 1 and e["main"])
        rows_ref = first["rows"]
        T = first["n_tasks"]
        tv = np.repeat(first["tv"][:, :1], T + 1, axis=1)
        cv = np.repeat(first["cv"][:, :1], T + 1, axis=1)
        entries.append({"id": f"pretrained_{order}", "label": f"Pretrained model (Task Order={order.capitalize()})",
                        "order": order, "n_tasks": T, "rows": rows_ref, "joint": False, "main": True,
                        "point": all_metrics(tv.mean(axis=2), cv.mean(axis=2)), "tv": tv, "cv": cv})

    rng = np.random.default_rng(BOOTSTRAP_SEED)
    n, m = len(task_cases), len(control_cases)
    idx_t = rng.integers(0, n, (N_BOOTSTRAP, n))
    idx_c = rng.integers(0, m, (N_BOOTSTRAP, m))
    for e in entries:
        e["samples"] = metric_samples(e["tv"], e["cv"], idx_t, idx_c, e["joint"])

    rows = []
    for ea, eb in combinations(entries, 2):
        if ea["rows"] != eb["rows"]:
            continue
        for k in METRICS:
            pa, pb = ea["point"][k], eb["point"][k]
            if pa == "" or pb == "":
                continue
            d = ea["samples"][k] - eb["samples"][k]
            rows.append({
                "metric": k,
                "a_id": ea["id"], "a_label": ea["label"],
                "b_id": eb["id"], "b_label": eb["label"],
                "a": pa, "b": pb, "diff": pa - pb,
                "diff_std": float(d.std(ddof=1)),
                "diff_ci_low": float(np.percentile(d, 2.5)),
                "diff_ci_high": float(np.percentile(d, 97.5)),
                "share_a_greater": float((d > 0).mean()),
            })

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} paired differences ({len(entries)} experiments incl. references) "
          f"to {OUT_FILE.relative_to(REPO)}")


if __name__ == "__main__":
    main()
