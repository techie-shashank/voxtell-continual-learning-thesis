"""Collect compute figures per experiment from the logs.

Input:  results/experiment_index.csv, the SLURM logs (results/hpc/logs) and the
        experiments' run.log / eval.log files.
Output: thesis/tables/compute.csv (every completed experiment) and
        thesis/tables/ch6_compute.tex (main comparison, bare tabular: trainable
        parameters, epoch time, total job wall-clock time, evaluation time per
        volume, peak GPU memory). With 6 tasks x 10 epochs, train_hours equals
        epoch_minutes numerically, so the table shows job_hours instead.

Columns and where they come from:
  gpu                    GPU name in the SLURM 'GPU utilization' footer
  slurm_jobs             number of SLURM jobs of the run (restarts and re-evaluations included)
  total_params, trainable_params
                         last 'Model parameters' line before the first 'Training started'
                         in the run's first SLURM log
  epoch_minutes          mean wall-clock time of one training epoch (run.log timestamps,
                         '[EPOCH k/N]' to 'Epoch k+1/N completed'; includes validation)
  train_hours            sum of all epoch times over all tasks
  eval_seconds_per_volume
                         median over the run's evaluations of (last batch - start) / volumes
                         (includes data loading and text encoding)
  peak_gpu_mib           max 'max_memory_usage' over the run's SLURM jobs (training and evaluation)
  job_hours              sum of 'Elapsed runtime' over the run's SLURM jobs

Usage (from the repository root):
    python scripts/make_compute_table.py
"""
from __future__ import annotations

import csv
import re
from datetime import datetime

import numpy as np

from _common import INDEX_FILE, REPO, SLURM_LOGS
from _results import STRATEGY_ORDER, TABLES, roles, strategy_name

TS = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3})")
PARAMS = re.compile(r"Model parameters - Total: (\d+) \| Trainable: (\d+)")
EPOCH_START = re.compile(r"\[EPOCH (\d+)/(\d+)\]")
EPOCH_DONE = re.compile(r"Epoch (\d+)/(\d+) completed")
ELAPSED = re.compile(r"Elapsed runtime\s*:\s*(?:(\d+)-)?(\d+):(\d+):(\d+)")
GPU_LINE = re.compile(r"^(NVIDIA [^,]+), [0-9A-F:.]+, \d+, [^,]+, [^,]+, (\d+) MiB")
EVAL_START = re.compile(r"Evaluation started \| dataset=\S+ \| .*batches=(\d+)")
BATCH = re.compile(r"Batch (\d+) \| Loss")


def ts(line):
    m = TS.match(line)
    return datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S,%f") if m else None


def slurm_info(log_names: list[str]) -> dict:
    gpus, mem, hours, params = set(), [], 0.0, None
    for i, name in enumerate(log_names):
        with open(SLURM_LOGS / name, encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        if i == 0:
            for line in lines:
                if "Training started" in line:
                    break
                m = PARAMS.search(line)
                if m:
                    params = (int(m.group(1)), int(m.group(2)))
        for line in lines:
            m = GPU_LINE.match(line.strip())
            if m:
                gpus.add(m.group(1))
                mem.append(int(m.group(2)))
            m = ELAPSED.search(line)
            if m:
                d, h, mi, s = (int(x or 0) for x in m.groups())
                hours += d * 24 + h + mi / 60 + s / 3600
    return {"gpu": ";".join(sorted(gpus)), "slurm_jobs": len(log_names),
            "total_params": params[0] if params else "", "trainable_params": params[1] if params else "",
            "peak_gpu_mib": max(mem) if mem else "", "job_hours": round(hours, 3)}


def epoch_minutes(exp_dir) -> list[float]:
    durations = []
    for log in sorted(exp_dir.glob("tasks/task_*/logs/run.log")):
        per_epoch, start = {}, None
        with open(log, encoding="utf-8", errors="replace") as f:
            for line in f:
                m = EPOCH_START.search(line)
                if m:
                    start = (int(m.group(1)), ts(line))
                    continue
                m = EPOCH_DONE.search(line)
                if m and start and int(m.group(1)) == start[0] + 1:
                    per_epoch[start[0]] = (ts(line) - start[1]).total_seconds() / 60   # last run of an epoch wins
                    start = None
        durations += per_epoch.values()
    return durations


def eval_seconds_per_volume(exp_dir) -> float | None:
    per_volume = []
    for log in exp_dir.glob("tasks/*/*/test/logs/eval.log"):
        with open(log, encoding="utf-8", errors="replace") as f:
            start, n, last = None, None, None
            for line in f:
                m = EVAL_START.search(line)
                if m:
                    if start and last and n:
                        per_volume.append((last - start).total_seconds() / n)
                    start, n, last = ts(line), int(m.group(1)), None
                elif BATCH.search(line):
                    last = ts(line)
            if start and last and n:
                per_volume.append((last - start).total_seconds() / n)
    return float(np.median(per_volume)) if per_volume else None


def main():
    with open(INDEX_FILE, newline="", encoding="utf-8") as f:
        index = [r for r in csv.DictReader(f)
                 if r["status"] == "completed" and r["has_eval_matrix"] == "yes"]
    rows = []
    for r in index:
        exp_dir = REPO / r["path"]
        epochs = epoch_minutes(exp_dir)
        evals = eval_seconds_per_volume(exp_dir)
        rows.append({
            "experiment_id": r["experiment_id"], "label": r["label"], "role": r["role"],
            **slurm_info([x for x in r["slurm_logs"].split(";") if x]),
            "epoch_minutes": round(float(np.mean(epochs)), 2) if epochs else "",
            "train_hours": round(sum(epochs) / 60, 2) if epochs else "",
            "eval_seconds_per_volume": round(evals, 2) if evals else "",
        })
    with open(TABLES / "compute.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote compute figures for {len(rows)} experiments to thesis/tables/compute.csv")

    by_id = {r["experiment_id"]: r for r in index}
    main_rows = sorted([c for c in rows if "Main" in roles(c)],
                       key=lambda c: (STRATEGY_ORDER.index(by_id[c["experiment_id"]]["strategy"])))
    lines = ["% Generated by scripts/make_compute_table.py from the experiment logs. Do not edit.",
             r"\small\setlength{\tabcolsep}{4pt}",
             r"\begin{tabular}{lrrrrr}", r"\toprule",
             r"Strategy & Trainable & Epoch & Wall-clock & Evaluation & Peak GPU \\",
             r" & param.\ (M) & (min) & (h) & (s/volume) & mem.\ (GiB) \\",
             r"\midrule"]
    for c in main_rows:
        run = by_id[c["experiment_id"]]
        lines.append(" & ".join([
            strategy_name(run),
            f"{c['trainable_params'] / 1e6:.2f}",
            f"{c['epoch_minutes']:.1f}",
            f"{c['job_hours']:.1f}",
            f"{c['eval_seconds_per_volume']:.1f}",
            f"{c['peak_gpu_mib'] / 1024:.1f}",
        ]) + r" \\")
    lines += [r"\bottomrule", r"\end{tabular}", ""]
    (TABLES / "ch6_compute.tex").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote thesis/tables/ch6_compute.tex")


if __name__ == "__main__":
    main()
