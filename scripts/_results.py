"""Shared pieces for the result tables and figures: experiment groups, names, plot style.

The experiment groups follow the 'role' column of results/experiment_index.csv
(the author's grouping). Comparison runs that a group needs (e.g. the
original-order counterpart of a reverse-order run) are found by matching the
configuration, never by hard-coded experiment IDs.
"""
from __future__ import annotations

import csv

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from _common import INDEX_FILE, REPO

METRICS_FILE = REPO / "thesis" / "tables" / "cl_metrics.csv"
TABLES = REPO / "thesis" / "tables"
FIGURES = REPO / "thesis" / "figures"

# Training volumes per task without a cap: "Train/Val/Test Split: 108/23/24" in the SLURM logs.
FULL_TRAIN_VOLUMES = 108

METRICS = ["adaptation", "average_performance", "final_performance",
           "final_forgetting", "transfer", "control_drop"]
METRIC_LABEL = {
    "adaptation": "Adaptation",
    "average_performance": "Average Performance",
    "final_performance": "Final Performance",
    "final_forgetting": "Final Forgetting",
    "transfer": "Transfer",
    "control_drop": "Control-task drop",
}
HIGHER_IS_BETTER = {"adaptation": True, "average_performance": True, "final_performance": True,
                    "final_forgetting": False, "transfer": True, "control_drop": False}

# Fixed name, colour and marker per strategy (validated categorical palette, light mode).
# Names follow the CLAUDE.md terminology (mechanism names; "-based" marks this thesis's variants).
STRATEGY = {
    "naive_sequential_finetuning": ("Seq. fine-tuning", "#2a78d6", "o"),
    "lora": ("Task-specific LoRA", "#eb6834", "s"),
    "shared_lora": ("Shared LoRA", "#1baf7a", "^"),
    "cpe_clip": ("CPE-CLIP-based", "#eda100", "D"),
    "zscl": ("ZSCL-based", "#e87ba4", "v"),
}
STRATEGY_ORDER = list(STRATEGY)
REFERENCE_COLOUR = "#52514e"

TASK_SHORT = {
    "skm_tea_lateral_tibial": "LT",
    "skm_tea_medial_tibial": "MT",
    "skm_tea_femoral": "Fe",
    "skm_tea_patellar": "Pa",
    "skm_tea_medial_meniscus": "MM",
    "skm_tea_lateral_meniscus": "LM",
    "aeropath": "Ctrl",
}

TEXT_WIDTH_IN = 460.93457 / 72.27   # \textwidth from thesis_main.log


def load():
    """Return (index rows with metrics merged in, reference rows by task order)."""
    with open(INDEX_FILE, newline="", encoding="utf-8") as f:
        index = {r["experiment_id"]: r for r in csv.DictReader(f)}
    with open(METRICS_FILE, newline="", encoding="utf-8") as f:
        metrics = list(csv.DictReader(f))
    runs, refs = [], {}
    for m in metrics:
        if m["role"] == "Reference":
            refs[m["task_order"]] = {**m, "strategy": "", "lora_rank": ""}
        else:
            runs.append({**index[m["experiment_id"]], **m})
    return runs, refs


def roles(run) -> list[str]:
    return [x for x in run["role"].split(";") if x]


def train_volumes(run) -> int:
    return int(run["train_max_cases"]) if run["train_max_cases"] else FULL_TRAIN_VOLUMES


def is_default(run) -> bool:
    """Full training data, no replay, 10 epochs, 6 tasks, original order."""
    return (not run["train_max_cases"] and not run["replay_fraction"] and run["epochs"] == "10"
            and run["n_tasks"] == "6" and run["task_order"] == "original")


def counterpart(run, runs):
    """The default-configuration run with the same strategy and LoRA rank."""
    hits = [r for r in runs if is_default(r) and r["strategy"] == run["strategy"]
            and r["lora_rank"] == run["lora_rank"]]
    if len(hits) != 1:
        raise ValueError(f"expected one counterpart for {run['label']}, found {len(hits)}")
    return hits[0]


def strategy_name(run, with_rank: bool = True, math: str = "$") -> str:
    name = STRATEGY[run["strategy"]][0]
    if with_rank and run["lora_rank"]:
        name += f" ({math}r={run['lora_rank']}{math})"
    return name


def value(run, metric):
    return float(run[metric]) if run.get(metric, "") != "" else None


def ci(run, metric):
    v = value(run, metric)
    if v is None or run.get(f"{metric}_ci_low", "") == "":
        return (0.0, 0.0)
    return (max(0.0, v - float(run[f"{metric}_ci_low"])), max(0.0, float(run[f"{metric}_ci_high"]) - v))


def setup_style():
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["cmr10"],          # Computer Modern, matches Latin Modern in the thesis
        "mathtext.fontset": "cm",
        "axes.formatter.use_mathtext": True,
        "axes.unicode_minus": False,
        "font.size": 10,
        "axes.labelsize": 10,
        "axes.titlesize": 10,
        "legend.fontsize": 9,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#52514e",
        "xtick.color": "#52514e",
        "ytick.color": "#52514e",
        "axes.grid": False,
        "pdf.fonttype": 42,
    })


def y_grid(ax):
    ax.grid(axis="y", color="#e4e3df", linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)
