"""Compute the continual-learning metrics of every completed experiment.

Input:  results/experiment_index.csv and each experiment's eval_matrix.csv.
Output: thesis/tables/cl_metrics.csv (one row per experiment).

This script is the reference implementation of the metrics used in the thesis.
code/src/continual/metrics.py computes some of them differently (its average
performance reads the matrix along the wrong axis, and its retention drop is
averaged over checkpoints); its metrics.json files are not used.

Notation. T training tasks, trained in the order 1..T. a[i, s] is the mean Dice
on task i evaluated with checkpoint s, where s = 0 is the pretrained model and
s = t is the model after training on task t. Task i is trained at stage i.

  Adaptation           mean of a[i, i] over i = 1..T: performance on each task
                       right after training on it. This is the a_{k,k} term of
                       the intransigence measure of Chaudhry et al. (ECCV 2018),
                       without its joint-training reference (none was trained).
  Average performance  mean of a[i, s] over i = 1..T, s = 1..T
                       ("Avg." of ZSCL, Zheng et al., ICCV 2023)
  Final performance    mean of a[i, T] over i = 1..T             ("Last" of ZSCL)
  Final forgetting     mean over i = 1..T-1 of
                       max_{s = 1..T-1} a[i, s] - a[i, T]
                       (Chaudhry et al., ECCV 2018, Eq. 3, unchanged: the max
                       runs over all earlier stages)
  Transfer             mean over i = 2..T of mean_{s = 1..i-1} a[i, s]
                       ("Transfer" of ZSCL: performance on a task before it is
                       trained)
  Control-task drop    c[0] - c[T], where c[s] is the Dice on the control task
                       (never trained on) at checkpoint s. Absolute, final
                       checkpoint; positive means the pretrained ability was
                       lost. Follows the control-set evaluation of SPU
                       (Zhang et al., CVPR 2024).

Reference rows. For each task order, one extra row 'Pretrained model' applies
the same metrics to a model that is never updated: every checkpoint equals the
pretrained column. Its forgetting and control-task drop are 0 by construction.
The pretrained column is taken from the experiments with that task order; the
script checks that they agree.

Variability. Each configuration was trained once (one seed), so the only
variability available is over the test volumes. For every metric the script
reports a paired bootstrap over test volumes (B = 2000, fixed seed): the
24 SKM-TEA test scans are resampled with replacement, with the same draw for
every task and checkpoint (all tasks share the same scans), the 4 control-task
volumes are resampled separately, and the metric is recomputed from the
resampled means. Columns <metric>_std (bootstrap standard deviation) and
<metric>_ci_low/_ci_high (2.5 and 97.5 percentiles). This reflects the choice of
test volumes only, not training randomness. Needs thesis/tables/per_volume_dice.csv
(scripts/extract_per_volume.py).

Usage (from the repository root):
    python scripts/compute_cl_metrics.py
"""
from __future__ import annotations

import csv
from collections import defaultdict

import numpy as np

from _common import INDEX_FILE, REPO, load_eval_matrix

OUT_FILE = REPO / "thesis" / "tables" / "cl_metrics.csv"
PER_VOLUME_FILE = REPO / "thesis" / "tables" / "per_volume_dice.csv"
METRICS = ["adaptation", "average_performance", "final_performance",
           "final_forgetting", "transfer", "control_drop"]
N_BOOTSTRAP = 2000
BOOTSTRAP_SEED = 0


def split_matrix(exp_dir, tasks: list[str], control_tasks: list[str]):
    """Return (a, c): the T x (T+1) task block and the control rows.

    Checks that the rows and columns of eval_matrix.csv are in the configured
    task order, so that the diagonal is 'just trained'.
    """
    labels, cols, values = load_eval_matrix(exp_dir)
    expected_rows = [f"{t} (CL)" for t in tasks] + [f"{t} (Retention)" for t in control_tasks]
    expected_cols = ["Pretrained"] + [f"After {t}" for t in tasks]
    if labels != expected_rows or cols != expected_cols:
        raise ValueError(f"{exp_dir}: eval_matrix.csv rows/columns do not match the config task order")
    if np.isnan(values).any():
        raise ValueError(f"{exp_dir}: eval_matrix.csv has missing entries")
    T = len(tasks)
    return values[:T], values[T:]


def cl_metrics(a: np.ndarray) -> dict:
    """a: T x (T+1) matrix, column 0 = pretrained."""
    T = a.shape[0]
    stages = a[:, 1:]                       # stages[i, s-1] = a[i, s]
    out = {
        "adaptation": float(np.diag(stages).mean()),
        "average_performance": float(stages.mean()),
        "final_performance": float(stages[:, -1].mean()),
        "final_forgetting": "",
        "transfer": "",
    }
    if T > 1:
        out["final_forgetting"] = float(np.mean(
            [stages[i, :T - 1].max() - stages[i, T - 1] for i in range(T - 1)]))
        out["transfer"] = float(np.mean(
            [stages[i, :i].mean() for i in range(1, T)]))
    return out


def load_volumes():
    """experiment_id -> {(row_task, stage): {case_id: dice}}"""
    vols = defaultdict(lambda: defaultdict(dict))
    with open(PER_VOLUME_FILE, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            vols[r["experiment_id"]][(r["row_task"], int(r["stage"]))][r["case_id"]] = float(r["dice"])
    return vols


def volume_tensor(cells, row_tasks: list[str], n_stages: int, check: np.ndarray) -> np.ndarray:
    """Array [rows, stages, volumes] with the volumes in one fixed order."""
    cases = sorted(cells[(row_tasks[0], 0)])
    out = np.empty((len(row_tasks), n_stages, len(cases)))
    for i, task in enumerate(row_tasks):
        for s in range(n_stages):
            cell = cells[(task, s)]
            if sorted(cell) != cases:
                raise ValueError(f"cell ({task}, {s}) has different test volumes")
            out[i, s] = [cell[c] for c in cases]
    if np.abs(out.mean(axis=2) - check).max() > 1e-5:
        raise ValueError("per-volume means do not reproduce eval_matrix.csv")
    return out


def all_metrics(a: np.ndarray, c: np.ndarray) -> dict:
    """a: T x (T+1) task block, c: control row(s) T x (T+1)."""
    return {**cl_metrics(a), "control_drop": float(c[0, 0] - c[0, -1])}


def bootstrap(task_vols: np.ndarray, control_vols: np.ndarray, rng) -> dict:
    n, m = task_vols.shape[2], control_vols.shape[2]
    samples = defaultdict(list)
    for _ in range(N_BOOTSTRAP):
        a = task_vols[:, :, rng.integers(0, n, n)].mean(axis=2)
        c = control_vols[:, :, rng.integers(0, m, m)].mean(axis=2)
        for k, v in all_metrics(a, c).items():
            if v != "":
                samples[k].append(v)
    out = {}
    for k in METRICS:
        v = np.array(samples.get(k, []))
        out[f"{k}_std"] = float(v.std(ddof=1)) if len(v) else ""
        out[f"{k}_ci_low"] = float(np.percentile(v, 2.5)) if len(v) else ""
        out[f"{k}_ci_high"] = float(np.percentile(v, 97.5)) if len(v) else ""
    return out


def main():
    with open(INDEX_FILE, newline="", encoding="utf-8") as f:
        index = [r for r in csv.DictReader(f)
                 if r["status"] == "completed" and r["has_eval_matrix"] == "yes"]
    volumes = load_volumes()
    rng = np.random.default_rng(BOOTSTRAP_SEED)

    rows = []
    pretrained = {}     # (task order, tasks, control task) -> list of (column, volume slices)
    for r in index:
        tasks = r["tasks"].split(";")
        controls = [t for t in r["control_tasks"].split(";") if t]
        if len(controls) != 1:
            raise ValueError(f"{r['experiment_id']}: expected one control task, got {controls}")
        a, c = split_matrix(REPO / r["path"], tasks, controls)
        tv = volume_tensor(volumes[r["experiment_id"]], tasks, len(tasks) + 1, a)
        cv = volume_tensor(volumes[r["experiment_id"]], controls, len(tasks) + 1, c)
        rows.append({
            "experiment_id": r["experiment_id"],
            "label": r["label"],
            "role": r["role"],
            "task_order": r["task_order"],
            "n_tasks": len(tasks),
            **all_metrics(a, c),
            "control_task": controls[0],
            "control_pretrained": float(c[0, 0]),
            "control_final": float(c[0, -1]),
            **bootstrap(tv, cv, rng),
        })
        if len(tasks) > 1:
            key = (r["task_order"], ";".join(tasks), controls[0])
            pretrained.setdefault(key, []).append(
                (np.concatenate([a[:, 0], c[:, 0]]), tv[:, :1], cv[:, :1]))

    for (order, tasks, control), entries in sorted(pretrained.items()):
        columns = np.array([e[0] for e in entries])
        spread = float(np.ptp(columns, axis=0).max())
        if spread > 1e-5:
            raise ValueError(f"pretrained columns disagree for task order {order} (max spread {spread:.2e})")
        col = columns.mean(axis=0)
        T = len(tasks.split(";"))
        frozen = np.repeat(col[:T, None], T + 1, axis=1)
        frozen_c = np.repeat(col[T:, None], T + 1, axis=1)
        # Volumes of the pretrained model, taken from the first experiment with this order.
        tv = np.repeat(entries[0][1], T + 1, axis=1)
        cv = np.repeat(entries[0][2], T + 1, axis=1)
        rows.append({
            "experiment_id": "",
            "label": f"Pretrained model (Task Order={order.capitalize()})",
            "role": "Reference",
            "task_order": order,
            "n_tasks": T,
            **all_metrics(frozen, frozen_c),
            "control_task": control,
            "control_pretrained": float(col[T]),
            "control_final": float(col[T]),
            **bootstrap(tv, cv, rng),
        })
        print(f"Reference '{order}': pretrained column from {len(columns)} experiments, "
              f"max spread {spread:.1e}")

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote metrics for {len(rows)} experiments to {OUT_FILE.relative_to(REPO)}")


if __name__ == "__main__":
    main()
