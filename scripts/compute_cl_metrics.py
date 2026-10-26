"""Compute the continual-learning metrics of every completed experiment.

Input:  results/experiment_index.csv and each experiment's eval_matrix.csv, plus the
        tagged evaluations in evaluations/<tag>/eval_matrix.csv (reruns of October 2026,
        e.g. best_validation, weight_ensemble).
Output: thesis/tables/cl_metrics.csv (one row per experiment and evaluation; column
        `evaluation` is 'main' for the evaluation in the experiment root, else the tag).

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

Joint training. A joint run has one training stage on all six structures and is
evaluated on each of them (index column eval_tasks), so its task block is 6 x 2.
Adaptation, Final Forgetting and Transfer need a task sequence and are left empty;
Final Performance (mean over the six structures after training) and the
control-task drop are computed as above.

Reference rows. For each task order, one extra row 'Pretrained model' applies
the same metrics to a model that is never updated: every checkpoint equals the
pretrained column. Its forgetting and control-task drop are 0 by construction.
The pretrained column is taken from the experiments with that task order; the
script checks that they agree.

Variability. Each configuration was trained once (one seed), so the only
variability available is over the test volumes. For every metric the script
reports a paired bootstrap over test volumes (B = 2000, seed fixed per row by rng_for): the
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
import zlib
from collections import defaultdict

import numpy as np

from _common import INDEX_FILE, REPO, evaluations, load_eval_matrix

OUT_FILE = REPO / "thesis" / "tables" / "cl_metrics.csv"
PER_VOLUME_FILE = REPO / "thesis" / "tables" / "per_volume_dice.csv"
METRICS = ["adaptation", "average_performance", "final_performance",
           "final_forgetting", "transfer", "control_drop"]
N_BOOTSTRAP = 2000
BOOTSTRAP_SEED = 0


def rng_for(key: str):
    """Bootstrap generator of one row, seeded from BOOTSTRAP_SEED and the row's key, so a row's
    intervals do not change when other experiments or evaluations are added."""
    return np.random.default_rng([BOOTSTRAP_SEED, zlib.crc32(key.encode("utf-8"))])


def split_matrix(exp_dir, tasks: list[str], control_tasks: list[str], eval_tasks: list[str] | None = None):
    """Return (a, c): the evaluated-task block (rows x (stages + 1)) and the control rows.

    Checks that the rows and columns of eval_matrix.csv are in the configured
    task order, so that the diagonal is 'just trained'. `exp_dir` may also be an
    evaluations/<tag>/ folder. `eval_tasks` are the evaluated rows when they differ
    from the trained tasks (joint training).
    """
    eval_tasks = eval_tasks or tasks
    labels, cols, values = load_eval_matrix(exp_dir)
    expected_rows = [f"{t} (CL)" for t in eval_tasks] + [f"{t} (Retention)" for t in control_tasks]
    expected_cols = ["Pretrained"] + [f"After {t}" for t in tasks]
    if labels != expected_rows or cols != expected_cols:
        raise ValueError(f"{exp_dir}: eval_matrix.csv rows/columns do not match the config task order")
    if np.isnan(values).any():
        raise ValueError(f"{exp_dir}: eval_matrix.csv has missing entries")
    n = len(eval_tasks)
    return values[:n], values[n:]


def cl_metrics(a: np.ndarray, joint: bool = False) -> dict:
    """a: T x (T+1) matrix, column 0 = pretrained. Joint training: rows x 2 matrix."""
    if joint:
        return {"adaptation": "", "average_performance": "", "final_performance": float(a[:, -1].mean()),
                "final_forgetting": "", "transfer": ""}
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
    """(experiment_id, evaluation) -> {(row_task, stage): {case_id: dice}}"""
    vols = defaultdict(lambda: defaultdict(dict))
    with open(PER_VOLUME_FILE, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            vols[(r["experiment_id"], r["evaluation"])][(r["row_task"], int(r["stage"]))][r["case_id"]] = float(r["dice"])
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


def all_metrics(a: np.ndarray, c: np.ndarray, joint: bool = False) -> dict:
    """a: task block (T x (T+1); joint: rows x 2), c: control row(s) with the same columns."""
    return {**cl_metrics(a, joint), "control_drop": float(c[0, 0] - c[0, -1])}


def bootstrap(task_vols: np.ndarray, control_vols: np.ndarray, rng, joint: bool = False) -> dict:
    n, m = task_vols.shape[2], control_vols.shape[2]
    samples = defaultdict(list)
    for _ in range(N_BOOTSTRAP):
        a = task_vols[:, :, rng.integers(0, n, n)].mean(axis=2)
        c = control_vols[:, :, rng.integers(0, m, m)].mean(axis=2)
        for k, v in all_metrics(a, c, joint).items():
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

    rows = []
    pretrained = {}     # (task order, tasks, control task) -> list of (column, volume slices)
    for r in index:
        tasks = r["tasks"].split(";")
        eval_tasks = (r["eval_tasks"] or r["tasks"]).split(";")
        joint = r["strategy"] == "joint_fine_tuning"
        controls = [t for t in r["control_tasks"].split(";") if t]
        if len(controls) != 1:
            raise ValueError(f"{r['experiment_id']}: expected one control task, got {controls}")
        for name, eval_dir, _ in evaluations(REPO / r["path"]):
            a, c = split_matrix(eval_dir, tasks, controls, eval_tasks)
            cells = volumes[(r["experiment_id"], name)]
            tv = volume_tensor(cells, eval_tasks, len(tasks) + 1, a)
            cv = volume_tensor(cells, controls, len(tasks) + 1, c)
            rows.append({
                "experiment_id": r["experiment_id"],
                "evaluation": name,
                "label": r["label"],
                "role": r["role"],
                "task_order": r["task_order"],
                "n_tasks": len(tasks),
                **all_metrics(a, c, joint),
                "control_task": controls[0],
                "control_pretrained": float(c[0, 0]),
                "control_final": float(c[0, -1]),
                **bootstrap(tv, cv, rng_for(f"{r['experiment_id']}|{name}"), joint),
            })
        # Reference rows: from the main evaluation of runs with a task sequence.
        a, c = split_matrix(REPO / r["path"], tasks, controls, eval_tasks)
        cells = volumes[(r["experiment_id"], "main")]
        tv = volume_tensor(cells, eval_tasks, len(tasks) + 1, a)
        cv = volume_tensor(cells, controls, len(tasks) + 1, c)
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
            "evaluation": "main",
            "label": f"Pretrained model (Task Order={order.capitalize()})",
            "role": "Reference",
            "task_order": order,
            "n_tasks": T,
            **all_metrics(frozen, frozen_c),
            "control_task": control,
            "control_pretrained": float(col[T]),
            "control_final": float(col[T]),
            **bootstrap(tv, cv, rng_for(f"reference|{order}")),
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
