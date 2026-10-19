"""Draw the result figures into thesis/figures/ (PDF at the printed text width).

Input:  thesis/tables/cl_metrics.csv, results/experiment_index.csv and the
        experiments' eval_matrix.csv files.
Output (include with width=\\linewidth so they are not scaled):
  ch6_control_task_main.pdf  control-task Dice per checkpoint, main comparison
  ch6_main_metrics.pdf       all metrics, main comparison, 95% bootstrap intervals
  ch6_main_matrices.pdf      evaluation matrices of the main comparison
  ch6_rank.pdf               shared-LoRA metrics over the LoRA rank
  ch6_task_order.pdf         original vs reverse task order
  ch6_few_shot.pdf           metrics over the number of training volumes per task

Error bars and bands are 95% paired-bootstrap intervals over the test volumes
(see compute_cl_metrics.py); they do not include training randomness (one seed).

Usage (from the repository root):
    python scripts/plot_results.py [--png DIR]   # optional PNG previews
"""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _common import REPO, load_eval_matrix
from _results import (FIGURES, METRIC_LABEL, METRICS, REFERENCE_COLOUR, STRATEGY, STRATEGY_ORDER,
                      TASK_SHORT, TEXT_WIDTH_IN, ci, counterpart, load, roles, setup_style,
                      strategy_name, train_volumes, value, y_grid)

PNG_DIR: Path | None = None


def save(fig, name):
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / f"{name}.pdf")
    if PNG_DIR:
        fig.savefig(PNG_DIR / f"{name}.png", dpi=200)
    plt.close(fig)
    print(f"Wrote thesis/figures/{name}.pdf")


def by_strategy(run):
    return (STRATEGY_ORDER.index(run["strategy"]), int(run["lora_rank"] or 0))


def legend_right(ax, **kw):
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), frameon=False, **kw)


# --------------------------------------------------------------------------

def control_task_curve(main_runs):
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, 2.7))
    tasks = main_runs[0]["tasks"].split(";")
    x = np.arange(len(tasks) + 1)
    for r in main_runs:
        labels, _, values = load_eval_matrix(REPO / r["path"])
        row = [i for i, lab in enumerate(labels) if lab.endswith("(Retention)")]
        _, colour, marker = STRATEGY[r["strategy"]]
        # White marker edge keeps coinciding points (e.g. values near 0) apart.
        ax.plot(x, values[row[0]], color=colour, marker=marker, markersize=5.5, markeredgecolor="white",
                markeredgewidth=0.8, linewidth=1.5, label=strategy_name(r), clip_on=False, zorder=3)
    names = {"skm_tea_lateral_tibial": "Lateral\ntibial", "skm_tea_medial_tibial": "Medial\ntibial",
             "skm_tea_femoral": "Femoral", "skm_tea_patellar": "Patellar",
             "skm_tea_medial_meniscus": "Medial\nmeniscus", "skm_tea_lateral_meniscus": "Lateral\nmeniscus"}
    ax.set_xticks(x, ["Pre-\ntrained"] + [names[t] for t in tasks])
    ax.set_xlim(-0.2, len(tasks) + 0.2)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Checkpoint (after training on task)")
    ax.set_ylabel("Control-task Dice")
    y_grid(ax)
    legend_right(ax)
    fig.tight_layout(pad=0.3)
    save(fig, "ch6_control_task_main")


def metric_bars(runs, ref, name, height=2.9):
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, height))
    n = len(runs)
    width = 0.8 / n
    x = np.arange(len(METRICS))
    for k, r in enumerate(runs):
        _, colour, _ = STRATEGY[r["strategy"]]
        vals = [value(r, m) or 0.0 for m in METRICS]
        err = np.array([ci(r, m) for m in METRICS]).T
        ax.bar(x - 0.4 + width * (k + 0.5), vals, width * 0.92, color=colour, label=strategy_name(r),
               yerr=err, error_kw={"elinewidth": 0.8, "capsize": 1.5, "ecolor": "#2b2a28"}, zorder=2)
    for j, m in enumerate(METRICS):
        ax.hlines(value(ref, m), j - 0.42, j + 0.42, colors=REFERENCE_COLOUR, linestyles="--",
                  linewidth=1.0, zorder=3, label="Pretrained model" if j == 0 else None)
    ax.set_xticks(x, [METRIC_LABEL[m].replace(" ", "\n", 1) for m in METRICS])
    ax.set_xlim(-0.5, len(METRICS) - 0.5)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Dice")
    y_grid(ax)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3, frameon=False)
    fig.tight_layout(pad=0.3)
    save(fig, name)


def matrices(main_runs):
    n = len(main_runs)
    cols = 3
    rows = int(np.ceil(n / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(TEXT_WIDTH_IN, 2.25 * rows), layout="constrained")
    axes = axes.ravel()
    for ax, r in zip(axes, main_runs):
        labels, _, values = load_eval_matrix(REPO / r["path"])
        tasks = [lab.split(" (")[0] for lab in labels]
        im = ax.imshow(values, cmap="Blues", vmin=0, vmax=1, aspect="auto")
        for i in range(values.shape[0]):
            for j in range(values.shape[1]):
                v = values[i, j]
                ax.text(j, i, f"{v:.2f}"[1:] if v < 1 else "1.0", ha="center", va="center", fontsize=6,
                        color="white" if v > 0.55 else "#0b0b0b")
        ax.set_xticks(range(values.shape[1]), ["Pre"] + [TASK_SHORT[t] for t in tasks[:values.shape[1] - 1]],
                      fontsize=7)
        ax.set_yticks(range(values.shape[0]), [TASK_SHORT[t] for t in tasks], fontsize=7)
        ax.axhline(values.shape[0] - 1.5, color="white", linewidth=1.5)
        ax.tick_params(length=0)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(strategy_name(r), fontsize=9)
    for ax in axes[n:]:
        ax.axis("off")
    fig.colorbar(im, ax=axes.tolist(), label="Dice", shrink=0.5, aspect=25, pad=0.02)
    fig.supxlabel("Checkpoint (after training on task)", fontsize=9)
    fig.supylabel("Evaluated task", fontsize=9)
    save(fig, "ch6_main_matrices")


def rank_sweep(rank_runs, ref):
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, 2.7))
    ranks = [int(r["lora_rank"]) for r in rank_runs]
    shown = ["adaptation", "final_performance", "final_forgetting", "control_drop"]
    styles = {"adaptation": ("#2a78d6", "o"), "final_performance": ("#eb6834", "s"),
              "final_forgetting": ("#1baf7a", "^"), "control_drop": ("#eda100", "D")}
    for m in shown:
        colour, marker = styles[m]
        vals = np.array([value(r, m) for r in rank_runs])
        lo = np.array([float(r[f"{m}_ci_low"]) for r in rank_runs])
        hi = np.array([float(r[f"{m}_ci_high"]) for r in rank_runs])
        ax.fill_between(ranks, lo, hi, color=colour, alpha=0.15, linewidth=0)
        ax.plot(ranks, vals, color=colour, marker=marker, markersize=5, markeredgecolor="white",
                markeredgewidth=0.8, linewidth=1.5, label=METRIC_LABEL[m], zorder=3)
    ax.set_xscale("log", base=2)
    ax.set_xticks(ranks, [str(k) for k in ranks])
    ax.minorticks_off()
    ax.set_ylim(0, 1)
    ax.set_xlabel("LoRA rank $r$ (shared LoRA)")
    ax.set_ylabel("Dice")
    y_grid(ax)
    legend_right(ax)
    fig.tight_layout(pad=0.3)
    save(fig, "ch6_rank")


def task_order(pairs, refs):
    shown = ["adaptation", "final_performance", "final_forgetting", "control_drop"]
    fig, axes = plt.subplots(1, len(shown), figsize=(TEXT_WIDTH_IN, 2.5), sharey=True)
    x = np.arange(len(pairs))
    for ax, m in zip(axes, shown):
        for k, (order, hatch) in enumerate([("original", None), ("reverse", "////")]):
            runs = [p[k] for p in pairs]
            vals = [value(r, m) or 0.0 for r in runs]
            err = np.array([ci(r, m) for r in runs]).T
            colours = [STRATEGY[r["strategy"]][1] for r in runs]
            ax.bar(x - 0.2 + 0.4 * k, vals, 0.38, color=colours, hatch=hatch, edgecolor="white",
                   linewidth=0.0, yerr=err, error_kw={"elinewidth": 0.8, "capsize": 1.5}, zorder=2)
        ax.axhline(value(refs["original"], m), color=REFERENCE_COLOUR, linestyle="--", linewidth=1.0)
        # Strategy identity is carried by colour and named in the legend (long names do not fit as ticks).
        ax.set_xticks(x, [])
        ax.tick_params(axis="x", length=0)
        ax.set_title(METRIC_LABEL[m].replace(" ", "\n", 1) if len(METRIC_LABEL[m]) > 14 else METRIC_LABEL[m])
        ax.set_ylim(0, 1)
        y_grid(ax)
    axes[0].set_ylabel("Dice")
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    top = [Patch(facecolor=STRATEGY[p[0]["strategy"]][1], label=strategy_name(p[0])) for p in pairs]
    bottom = [Patch(facecolor="#9b9a96", label="Original order"),
              Patch(facecolor="#9b9a96", hatch="////", edgecolor="white", label="Reverse order"),
              Line2D([], [], color=REFERENCE_COLOUR, linestyle="--", label="Pretrained model")]
    # The legend fills column by column; interleave so row 1 = strategies, row 2 = order and reference.
    handles = [h for pair in zip(top, bottom) for h in pair]
    fig.legend(handles=handles, loc="upper center", ncol=len(top), frameon=False, bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(pad=0.3, rect=(0, 0, 1, 0.8))
    save(fig, "ch6_task_order")


def few_shot(groups, ref):
    shown = ["adaptation", "final_performance", "final_forgetting", "control_drop"]
    fig, axes = plt.subplots(1, len(shown), figsize=(TEXT_WIDTH_IN, 2.5), sharey=True)
    for ax, m in zip(axes, shown):
        for runs in groups:
            runs = sorted(runs, key=train_volumes)
            _, colour, marker = STRATEGY[runs[0]["strategy"]]
            xs = [train_volumes(r) for r in runs]
            vals = np.array([value(r, m) for r in runs])
            lo = np.array([float(r[f"{m}_ci_low"]) for r in runs])
            hi = np.array([float(r[f"{m}_ci_high"]) for r in runs])
            ax.fill_between(xs, lo, hi, color=colour, alpha=0.15, linewidth=0)
            ax.plot(xs, vals, color=colour, marker=marker, markersize=4.5, markeredgecolor="white",
                    markeredgewidth=0.7, linewidth=1.4, label=strategy_name(runs[0]), zorder=3)
        ax.axhline(value(ref, m), color=REFERENCE_COLOUR, linestyle="--", linewidth=1.0,
                   label="Pretrained model")
        ax.set_xscale("log")
        ticks = sorted({train_volumes(r) for g in groups for r in g})
        ax.set_xticks(ticks, [str(t) for t in ticks])
        ax.minorticks_off()
        ax.set_title(METRIC_LABEL[m])
        ax.set_ylim(0, 1)
        y_grid(ax)
    axes[0].set_ylabel("Dice")
    fig.supxlabel("Training volumes per task", fontsize=10)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(pad=0.3, rect=(0, 0, 1, 0.8))
    save(fig, "ch6_few_shot")


def main():
    global PNG_DIR
    parser = argparse.ArgumentParser()
    parser.add_argument("--png", help="also write PNG previews into this directory")
    args = parser.parse_args()
    PNG_DIR = Path(args.png) if args.png else None

    setup_style()
    runs, refs = load()

    main_runs = sorted([r for r in runs if "Main" in roles(r)], key=by_strategy)
    control_task_curve(main_runs)
    metric_bars(main_runs, refs["original"], "ch6_main_metrics")
    matrices(main_runs)

    rank_runs = sorted([r for r in runs if "Rank Ablation" in roles(r)], key=lambda r: int(r["lora_rank"]))
    rank_sweep(rank_runs, refs["original"])

    reverse = sorted([r for r in runs if "Task Order Ablation" in roles(r)], key=by_strategy)
    task_order([(counterpart(r, runs), r) for r in reverse], refs)

    few = [r for r in runs if "Few-shot" in roles(r)]
    keys = sorted({(r["strategy"], r["lora_rank"]) for r in few}, key=lambda k: STRATEGY_ORDER.index(k[0]))
    groups = []
    for key in keys:
        g = [r for r in few if (r["strategy"], r["lora_rank"]) == key]
        groups.append(g + [counterpart(g[0], runs)])
    few_shot(groups, refs["original"])


if __name__ == "__main__":
    main()
