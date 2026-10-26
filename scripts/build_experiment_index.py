"""Build results/experiment_index.csv: one row per experiment in results/hpc/experiments.

The experiment folders are the single source of truth. This script only reads
them. All columns except `label`, `role` and `notes` are derived from each
experiment's config.yaml, continual_state.json, run_info.json (reruns from
October 2026 on) and the SLURM logs in results/hpc/logs, so rerunning the
script never changes them by hand.
`label`, `role` and `notes` are maintained by the author; their values are kept
when the script is rerun (matched by experiment_id).

Usage (from the repository root):
    python scripts/build_experiment_index.py
"""
from __future__ import annotations

import csv
import json
import re

from _common import (EXPERIMENTS, INDEX_FILE, ORIGINAL_ORDER, REPO, SLURM_LOGS,
                     read_config, read_json)

MANUAL_COLUMNS = ["label", "role", "notes"]
COLUMNS = [
    "experiment_id", "path", "status", "has_eval_matrix",
    "strategy", "lora_rank", "lora_alpha", "lora_dropout",
    "task_order", "n_tasks", "tasks", "control_tasks",
    "train_max_cases", "replay_fraction", "replay_max_size",
    "epochs", "lr", "train_seed", "split_seed", "strategy_params",
    "eval_tasks", "eval_checkpoint", "extra_evaluations", "validation_interval",
    "replay_control_volumes", "code_commits",
    "slurm_logs",
] + MANUAL_COLUMNS

EXP_ID = re.compile(r"exp_\d{8}_\d{6}_[0-9a-f]{8}")


def slurm_logs_by_experiment() -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for log in sorted(SLURM_LOGS.glob("*.out")):
        ids = set(EXP_ID.findall(log.read_text(encoding="utf-8", errors="replace")))
        for exp_id in ids:
            found.setdefault(exp_id, []).append(log.name)
    return found


def task_order(tasks: list[str], joint: bool = False) -> str:
    if joint:
        return "joint"
    if tasks == ORIGINAL_ORDER:
        return "original"
    if tasks == ORIGINAL_ORDER[::-1]:
        return "reverse"
    return "custom"


def row_for(exp_dir, logs) -> dict:
    cfg = read_config(exp_dir / "config.yaml")
    cont = cfg["continual"]
    lora = cont.get("lora") or {}
    replay = cont.get("replay_memory") or {}
    data = cfg.get("dataset") or {}
    train = cfg["training"]
    tasks = [t["name"] for t in cont["tasks"]]
    # Joint training (reruns 2026-10): one training task whose dataset concatenates several task
    # datasets (dataset.joint_names); it is evaluated on the structures in continual.evaluation.tasks.
    joint = any((t.get("dataset") or {}).get("joint_names") for t in cont["tasks"])
    evaluation = cont.get("evaluation") or {}
    eval_tasks = [t["name"] for t in evaluation.get("tasks") or []] or tasks
    # Same default as code/src/continual/task_manager.py
    strategy = cont.get("strategy", cont.get("baseline", "naive_sequential_finetuning"))
    if joint:
        strategy = "joint_fine_tuning"
    # Evaluated parameters of the main evaluation. LoRA strategies always load the adapter saved
    # after the last epoch (lora/*/strategy.py, build_evaluation_spec); the others load
    # continual.evaluation.checkpoint, which defaulted to best_model.pt before the reruns.
    if strategy in ("lora", "shared_lora"):
        eval_checkpoint = "lora_adapter.pt"
    else:
        eval_checkpoint = evaluation.get("checkpoint") or "best_model.pt"
    extra = ";".join(f"{e['tag']}:{e['checkpoint']}" for e in evaluation.get("extra") or [])
    run_info = exp_dir / "run_info.json"
    commits = list(dict.fromkeys(f"{x['git_commit'][:7]}{'-dirty' if x['git_dirty'] else ''}"
                                 for x in read_json(run_info))) if run_info.exists() else []
    params = {k: cont[k] for k in ("zscl", "cpe_clip") if k in cont}
    state_file = exp_dir / "continual_state.json"
    return {
        "experiment_id": exp_dir.name,
        "path": exp_dir.relative_to(REPO).as_posix(),
        "status": read_json(state_file).get("status", "") if state_file.exists() else "",
        "has_eval_matrix": "yes" if (exp_dir / "eval_matrix.csv").exists() else "no",
        "strategy": strategy,
        "lora_rank": lora.get("rank", ""),
        "lora_alpha": lora.get("alpha", ""),
        "lora_dropout": lora.get("dropout", ""),
        "task_order": task_order(tasks, joint),
        "n_tasks": len(tasks),
        "tasks": ";".join(tasks),
        "control_tasks": ";".join(t["name"] for t in cont.get("retention_tasks") or []),
        # Empty = no cap, i.e. the full training split.
        "train_max_cases": data.get("train_max_cases", "") or "",
        "replay_fraction": replay.get("fraction", "") if replay.get("enabled") else "",
        "replay_max_size": replay.get("max_size", "") if replay.get("enabled") else "",
        "epochs": train["epochs"],
        "lr": train["optimizer"]["lr"],
        "train_seed": train.get("seed", ""),
        "split_seed": data.get("seed", ""),
        "strategy_params": json.dumps(params, sort_keys=True) if params else "",
        "eval_tasks": ";".join(eval_tasks),
        "eval_checkpoint": eval_checkpoint,
        "extra_evaluations": extra,
        "validation_interval": train.get("validation_interval", 1),
        # Default of replay_memory.include_retention_tasks in code/src/continual/strategies/base.py: true.
        "replay_control_volumes": ("yes" if replay.get("include_retention_tasks", True) else "no")
                                  if replay.get("enabled") else "",
        "code_commits": ";".join(commits),
        "slurm_logs": ";".join(logs.get(exp_dir.name, [])),
    }


def main():
    old = {}
    if INDEX_FILE.exists():
        with open(INDEX_FILE, newline="", encoding="utf-8") as f:
            old = {r["experiment_id"]: r for r in csv.DictReader(f)}

    logs = slurm_logs_by_experiment()
    exp_dirs = sorted(p.parent for p in EXPERIMENTS.rglob("config.yaml")
                      if p.parent.name.startswith("exp_"))
    rows = []
    for exp_dir in exp_dirs:
        row = row_for(exp_dir, logs)
        for col in MANUAL_COLUMNS:
            row[col] = old.get(exp_dir.name, {}).get(col, "")
        rows.append(row)

    missing = sorted(set(old) - {r["experiment_id"] for r in rows})
    if missing:
        raise SystemExit(f"Experiments in the index but no longer on disk: {missing}")
    orphan_logs = sorted(set(logs) - {r["experiment_id"] for r in rows})
    if orphan_logs:
        print(f"Warning: SLURM logs mention experiments without a folder: {orphan_logs}")

    rows.sort(key=lambda r: r["experiment_id"])
    with open(INDEX_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} experiments to {INDEX_FILE.relative_to(REPO)}")


if __name__ == "__main__":
    main()
