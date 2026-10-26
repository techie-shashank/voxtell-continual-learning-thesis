"""Which epoch was evaluated for each task of each run (checkpoint selection, F3/F4).

The main evaluation of a run uses the checkpoint in the index column eval_checkpoint:
best_model.pt (lowest validation loss; sequential fine-tuning, distillation-based and
prompt-tuning runs before the reruns), last_model.pt (all reruns of October 2026) or
lora_adapter.pt (LoRA runs, adapter after the last epoch). Every strategy continues to
the next task from the state after the last epoch.
This script reads each task's run.log and reports the selected epoch, so the
thesis can state in how many tasks the evaluated model is the one carried
forward (selected epoch = last epoch).

Input:  results/experiment_index.csv, tasks/<task>/logs/run.log of each run.
Output: thesis/tables/selected_epochs.csv (one row per run and task).

Usage (from the repository root):
    python scripts/selected_epochs.py
"""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "results" / "experiment_index.csv"
OUT = ROOT / "thesis" / "tables" / "selected_epochs.csv"

EPOCH_RE = re.compile(r"Epoch (\d+)/(\d+) completed .*Validation Loss=([0-9.]+)")
BEST_RE = re.compile(r"New best model saved \(val_loss=([0-9.]+)\) at epoch=(\d+)")


def parse_run_log(path: Path, epochs: int) -> dict:
    """Last epoch, its validation loss, and the epoch of the last 'best' save (1-based).

    The last epoch is the configured number of epochs (no early stopping in any run). It is
    not read from the log: with validation_interval > 1, and after a resume directly after the
    last batch of an epoch, not every epoch has a 'Validation Loss' line (e.g. joint_ft epoch 10).
    """
    val_loss = {}
    best_epoch = best_loss = None
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        m = EPOCH_RE.search(line)
        if m:
            val_loss[int(m.group(1))] = float(m.group(3))  # a resumed epoch overwrites itself
            continue
        m = BEST_RE.search(line)
        if m:
            best_loss, best_epoch = float(m.group(1)), int(m.group(2)) + 1
    last_epoch = epochs
    return {
        "epochs_completed": last_epoch,
        "selected_epoch": best_epoch,
        "val_loss_selected": best_loss,
        "val_loss_last": val_loss.get(last_epoch),
    }


def main():
    rows = []
    with open(INDEX, newline="", encoding="utf-8") as f:
        runs = [r for r in csv.DictReader(f) if r["role"] and r["has_eval_matrix"] == "yes"]
    for run in runs:
        strategy = run["strategy"]
        task_dirs = sorted((ROOT / run["path"] / "tasks").glob("task_[0-9][0-9]_*"))
        for task_dir in task_dirs:
            log = task_dir / "logs" / "run.log"
            if not log.exists():
                raise FileNotFoundError(log)
            info = parse_run_log(log, int(run["epochs"]))
            selection = "best_validation" if run["eval_checkpoint"] == "best_model.pt" else "last_epoch"
            evaluated = info["selected_epoch"] if selection == "best_validation" else info["epochs_completed"]
            rows.append({
                "experiment_id": run["experiment_id"],
                "label": run["label"],
                "role": run["role"],
                "strategy": strategy,
                "task_index": int(task_dir.name[5:7]),
                "task": task_dir.name[8:],
                "selection_rule": selection,
                "epochs_completed": info["epochs_completed"],
                "best_validation_epoch": info["selected_epoch"],
                "evaluated_epoch": evaluated,
                "evaluated_is_last": evaluated == info["epochs_completed"],
                "val_loss_best": info["val_loss_selected"],
                "val_loss_last": info["val_loss_last"],
            })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"{'run':<70} rule             evaluated epoch per task      last?")
    for exp in dict.fromkeys(r["experiment_id"] for r in rows):
        rs = [r for r in rows if r["experiment_id"] == exp]
        epochs = " ".join(f"{r['evaluated_epoch']:>2}" for r in rs)
        n_last = sum(r["evaluated_is_last"] for r in rs)
        print(f"{rs[0]['label'][:70]:<70} {rs[0]['selection_rule']:<16} {epochs:<29} {n_last}/{len(rs)}")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
