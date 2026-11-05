"""Draw the result figures into thesis/figures/ (PDF at the printed text width).

Input:  thesis/tables/cl_metrics.csv, results/experiment_index.csv and the
        experiments' eval_matrix.csv files.
Output (include with width=\\linewidth so they are not scaled):
  ch6_main_metrics.pdf       all metrics, main comparison, 95% bootstrap intervals
  ch6_main_matrices.pdf      evaluation matrices of the main comparison
  ch6_rank.pdf               shared-LoRA metrics over the LoRA rank
  ch6_task_order.pdf         original vs reverse task order
  ch6_few_shot.pdf           metrics over the number of training volumes per task
  appA_shared_lora_loss.pdf  training loss of the first two tasks of shared LoRA (appendix)

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
    # Shared LoRA + replay follows shared LoRA (one strategy order everywhere, thesis_notes.md 2026-11-01).
    return (STRATEGY_ORDER.index(run["strategy"]), int(run["lora_rank"] or 0), bool(run["replay_fraction"]))


def is_replay(run):
    return bool(run["replay_fraction"])


def run_label(run):
    """Strategy name; the replay run shares the strategy code of shared LoRA but is its own strategy."""
    name = strategy_name(run)
    return name.replace("Shared LoRA", "Shared LoRA + replay") if is_replay(run) else name


def legend_right(ax, **kw):
    ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), frameon=False, **kw)


def training_loss_per_epoch(run) -> dict[int, float]:
    """Mean training loss per epoch from the run.log of a single-task run (a resumed epoch overwrites itself)."""
    import re
    pattern = re.compile(r"Epoch (\d+)/(\d+) completed \| Training Loss=([0-9.]+)")
    logs = sorted((REPO / run["path"] / "tasks").glob("task_[0-9][0-9]_*/logs/run.log"))
    if len(logs) != 1:
        raise SystemExit(f"{run['label']}: expected one task log, found {len(logs)}")
    loss = {}
    for line in logs[0].read_text(encoding="utf-8", errors="replace").splitlines():
        m = pattern.search(line)
        if m:
            loss[int(m.group(1))] = float(m.group(3))
    return loss


def patellar_curves(diag):
    """Training loss per epoch of the single-task patellar runs; one setting changed per run."""
    base = {"lora_rank": "4", "lr": "0.0001", "train_seed": "42", "epochs": "10"}
    name = {"lora_rank": lambda r: f"rank $r={r['lora_rank']}$", "lr": lambda r: r"$\eta_0 = 3\cdot 10^{-4}$",
            "train_seed": lambda r: f"seed {r['train_seed']}", "epochs": lambda r: f"{r['epochs']} epochs"}
    colours = ["#52514e", "#2a78d6", "#eda100", "#1baf7a", "#eb6834"]
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, 2.5))
    order = [None, "lora_rank", "lr", "train_seed", "epochs"]

    def changed(r):
        d = [k for k in base if r[k] != base[k]]
        return d[0] if d else None

    for colour, r in zip(colours, sorted(diag, key=lambda r: order.index(changed(r)))):
        loss = training_loss_per_epoch(r)
        k = changed(r)
        label = "settings of the sequence" if k is None else name[k](r)
        ax.plot(list(loss), list(loss.values()), color=colour, linewidth=1.4, marker="o", markersize=2.5,
                label=label, zorder=3)
    ax.axvline(10, color=REFERENCE_COLOUR, linestyle="--", linewidth=1.0)
    ax.set_xlim(0.5, 50.5)
    ax.set_ylim(0, 1.3)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Training loss")
    y_grid(ax)
    legend_right(ax)
    fig.tight_layout(pad=0.3)
    save(fig, "ch6_patellar_loss")


def task_loss_per_epoch(run, task_index: int) -> dict[int, float]:
    """Mean training loss per epoch of one task (1-based position in the sequence) of a sequence run."""
    import re
    pattern = re.compile(r"Epoch (\d+)/(\d+) completed \| Training Loss=([0-9.]+)")
    logs = sorted((REPO / run["path"] / "tasks").glob(f"task_{task_index:02d}_*/logs/run.log"))
    if len(logs) != 1:
        raise SystemExit(f"{run['label']}: expected one log for task {task_index}, found {len(logs)}")
    loss = {}
    for line in logs[0].read_text(encoding="utf-8", errors="replace").splitlines():
        m = pattern.search(line)
        if m:
            loss[int(m.group(1))] = float(m.group(3))   # a resumed epoch overwrites itself
    return loss


def shared_lora_first_tasks_loss(curves):
    """Training loss per epoch of the first two tasks of shared LoRA (App. A; quoted in the task-order section).

    curves: list of (run, label, colour). Epochs 1-10 are the first task, 11-20 the second; the line is
    broken at the task boundary because the training data change there (the adapter carries over).
    """
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, 2.5))
    for run, label, colour in curves:
        for t in (1, 2):
            loss = task_loss_per_epoch(run, t)
            xs = [e + 10 * (t - 1) for e in sorted(loss)]
            ax.plot(xs, [loss[e] for e in sorted(loss)], color=colour, linewidth=1.4, marker="o",
                    markersize=2.5, label=label if t == 1 else None, zorder=3)
    ax.axvline(10.5, color=REFERENCE_COLOUR, linestyle="--", linewidth=1.0)
    ax.set_xlim(0.5, 20.5)
    ax.set_xticks([1, 5, 10, 11, 15, 20], ["1", "5", "10", "1", "5", "10"])
    ax.set_ylim(0, 1.2)
    ax.set_xlabel("Epoch of the first task (left) and of the second task (right)")
    ax.set_ylabel("Training loss")
    y_grid(ax)
    legend_right(ax)
    fig.tight_layout(pad=0.3)
    save(fig, "appA_shared_lora_loss")


# --------------------------------------------------------------------------

def control_task_curve(main_runs):
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, 3.2))
    tasks = main_runs[0]["tasks"].split(";")
    x = np.arange(len(tasks) + 1)
    for r in main_runs:
        labels, _, values = load_eval_matrix(REPO / r["path"])
        row = [i for i, lab in enumerate(labels) if lab.endswith("(Retention)")]
        _, colour, marker = STRATEGY[r["strategy"]]
        # White marker edge keeps coinciding points (e.g. values near 0) apart. Shared LoRA + replay:
        # colour of shared LoRA, dashed line and hollow marker (variant of shared LoRA, no extra palette slot).
        variant = {"linestyle": "--", "markerfacecolor": "white", "markeredgecolor": colour} if is_replay(r) \
            else {"markeredgecolor": "white"}
        ax.plot(x, values[row[0]], color=colour, marker=marker, markersize=5.5,
                markeredgewidth=0.8 if not is_replay(r) else 1.2, linewidth=1.5, label=run_label(r),
                clip_on=False, zorder=3, **variant)
    names = {"skm_tea_lateral_tibial": "Lateral\ntibial", "skm_tea_medial_tibial": "Medial\ntibial",
             "skm_tea_femoral": "Femoral", "skm_tea_patellar": "Patellar",
             "skm_tea_medial_meniscus": "Medial\nmeniscus", "skm_tea_lateral_meniscus": "Lateral\nmeniscus"}
    ax.set_xticks(x, ["Pre-\ntrained"] + [names[t] for t in tasks])
    ax.set_xlim(-0.2, len(tasks) + 0.2)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Checkpoint (after training on task)")
    ax.set_ylabel("Control-task DSC")
    y_grid(ax)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3, frameon=False,
              columnspacing=1.0, handlelength=2.2, handletextpad=0.5)
    fig.tight_layout(pad=0.3)
    save(fig, "ch6_control_task_main")


def metric_bars(runs, ref, name, height=2.9, joint=None):
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, height))
    n = len(runs)
    width = 0.8 / n
    x = np.arange(len(METRICS))
    for k, r in enumerate(runs):
        _, colour, _ = STRATEGY[r["strategy"]]
        vals = [value(r, m) or 0.0 for m in METRICS]
        err = np.array([ci(r, m) for m in METRICS]).T
        hatch = {"hatch": "////", "edgecolor": "white", "linewidth": 0} if is_replay(r) else {}
        ax.bar(x - 0.4 + width * (k + 0.5), vals, width * 0.92, color=colour, label=run_label(r), **hatch,
               yerr=err, error_kw={"elinewidth": 0.8, "capsize": 1.5, "ecolor": "#2b2a28"}, zorder=2)
    for j, m in enumerate(METRICS):
        ax.hlines(value(ref, m), j - 0.42, j + 0.42, colors=REFERENCE_COLOUR, linestyles="--",
                  linewidth=1.0, zorder=3, label="Pretrained model" if j == 0 else None)
    # Joint fine-tuning (upper reference): only Final Performance and the control-task drop are defined.
    if joint is not None:
        first = True
        for j, m in enumerate(METRICS):
            if value(joint, m) is None:
                continue
            ax.hlines(value(joint, m), j - 0.42, j + 0.42, colors=STRATEGY["joint_fine_tuning"][1],
                      linestyles="-.", linewidth=1.4, zorder=3,
                      label="Joint fine-tuning" if first else None)
            first = False
    ax.set_xticks(x, [METRIC_LABEL[m].replace(" ", "\n", 1) for m in METRICS])
    ax.set_xlim(-0.5, len(METRICS) - 0.5)
    ax.set_ylim(0, 1)
    ax.set_ylabel("DSC")
    y_grid(ax)
    # Strategies first, then the reference lines.
    handles, labels = ax.get_legend_handles_labels()
    refs_first = [i for i, l in enumerate(labels) if l in ("Pretrained model", "Joint fine-tuning")]
    order = [i for i in range(len(labels)) if i not in refs_first] + refs_first
    ax.legend([handles[i] for i in order], [labels[i] for i in order],
              loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=3, frameon=False,
              columnspacing=1.0, handlelength=1.6, handletextpad=0.5)
    fig.tight_layout(pad=0.3)
    save(fig, name)


def matrices(main_runs):
    n = len(main_runs)
    cols = 3
    rows = int(np.ceil(n / cols))
    fig, axes = plt.subplots(rows, cols, figsize=(TEXT_WIDTH_IN, 2.9 * rows), layout="constrained")
    axes = axes.ravel()
    for ax, r in zip(axes, main_runs):
        labels, _, values = load_eval_matrix(REPO / r["path"])
        tasks = [lab.split(" (")[0] for lab in labels]
        im = ax.imshow(values, cmap="Blues", vmin=0, vmax=1, aspect="auto")
        for i in range(values.shape[0]):
            for j in range(values.shape[1]):
                v = values[i, j]
                ax.text(j, i, f"{v:.2f}"[1:] if v < 1 else "1.0", ha="center", va="center", fontsize=10,
                        color="white" if v > 0.55 else "#0b0b0b")
        ax.set_xticks(range(values.shape[1]), ["Pre"] + [TASK_SHORT[t] for t in tasks[:values.shape[1] - 1]],
                      fontsize=10, rotation=90)
        ax.set_yticks(range(values.shape[0]), [TASK_SHORT[t] for t in tasks], fontsize=10)
        ax.axhline(values.shape[0] - 1.5, color="white", linewidth=1.5)
        ax.tick_params(length=0)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(run_label(r), fontsize=10)
    for ax in axes[n:]:
        ax.axis("off")
    fig.colorbar(im, ax=axes.tolist(), label="DSC", shrink=0.5, aspect=25, pad=0.02)
    fig.supxlabel("Checkpoint (after training on task)", fontsize=10)
    fig.supylabel("Evaluated task", fontsize=10)
    save(fig, "ch6_main_matrices")


def rank_sweep(rank_runs, ref):
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, 2.7))
    ranks = [int(r["lora_rank"]) for r in rank_runs]
    shown = ["adaptation", "final_forgetting", "control_drop", "final_performance"]
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
    ax.set_ylabel("DSC")
    y_grid(ax)
    legend_right(ax)
    fig.tight_layout(pad=0.3)
    save(fig, "ch6_rank")


def task_order(pairs, refs):
    shown = ["adaptation", "final_forgetting", "control_drop", "final_performance"]
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
    axes[0].set_ylabel("DSC")
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


def few_shot(groups, ref, equal=(), joint=()):
    shown = ["adaptation", "final_forgetting", "control_drop", "final_performance"]
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
                    markeredgewidth=0.7, linewidth=1.4, label=strategy_name(runs[0]), zorder=3,
                    clip_on=False)   # markers at 0 would otherwise be cut in half by the axis
        # Equal-updates runs: k = 5 with the 1,080 updates per task of the full split, hollow marker
        # in the colour of the strategy.
        # Small horizontal offsets (log axis) keep the three markers at k = 5 apart.
        offset = {"naive_sequential_finetuning": 1.1, "lora": 0.9, "shared_lora": 1.21}
        for r in equal:
            _, colour, marker = STRATEGY[r["strategy"]]
            v = value(r, m)
            err = [[v - float(r[f"{m}_ci_low"])], [float(r[f"{m}_ci_high"]) - v]]
            ax.errorbar([train_volumes(r) * offset.get(r["strategy"], 1.0)], [v], yerr=err, fmt=marker, markersize=6, markerfacecolor="white",
                        markeredgecolor=colour, markeredgewidth=1.3, ecolor=colour, elinewidth=0.9,
                        capsize=1.5, zorder=4, clip_on=False)
        # Joint fine-tuning: defined for Final Performance and the control-task drop only.
        js = sorted([r for r in joint if value(r, m) is not None], key=train_volumes)
        if js:
            _, colour, marker = STRATEGY["joint_fine_tuning"]
            ax.plot([train_volumes(r) for r in js], [value(r, m) for r in js], color=colour, marker=marker,
                    markersize=5, markeredgecolor="white", markeredgewidth=0.6, linewidth=1.4, linestyle="-.",
                    label="Joint fine-tuning", zorder=3, clip_on=False)
        ax.axhline(value(ref, m), color=REFERENCE_COLOUR, linestyle="--", linewidth=1.0,
                   label="Pretrained model")
        ax.set_xscale("log")
        ticks = sorted({train_volumes(r) for g in groups for r in g})
        ax.set_xticks(ticks, [str(t) for t in ticks])
        ax.minorticks_off()
        ax.set_title(METRIC_LABEL[m])
        ax.set_ylim(0, 1)
        y_grid(ax)
    axes[0].set_ylabel("DSC")
    fig.supxlabel("Training volumes per task", fontsize=10)
    # Legend: strategies and references from the panel with all entries, plus one neutral hollow marker
    # for the equal-updates runs (their colour follows the strategy).
    full = axes[shown.index("final_performance")]
    handles, labels = full.get_legend_handles_labels()
    if equal:
        from matplotlib.lines import Line2D
        handles.append(Line2D([], [], linestyle="none", marker="o", markersize=6, markerfacecolor="white",
                              markeredgecolor=REFERENCE_COLOUR, markeredgewidth=1.3))
        labels.append("5 volumes, 1,080 updates")
    fig.legend(handles, labels, loc="upper center", ncol=3, frameon=False, bbox_to_anchor=(0.5, 1.0))
    fig.tight_layout(pad=0.3, rect=(0.015, 0, 1, 0.78))
    save(fig, "ch6_few_shot")


def main():
    global PNG_DIR
    parser = argparse.ArgumentParser()
    parser.add_argument("--png", help="also write PNG previews into this directory")
    args = parser.parse_args()
    PNG_DIR = Path(args.png) if args.png else None

    setup_style()
    runs, refs = load()

    # Shared LoRA + replay (role "Replay Ablation") is one of the six strategies of the comparison.
    main_runs = sorted([r for r in runs if "Main" in roles(r) or "Replay Ablation" in roles(r)], key=by_strategy)
    # control_task_curve(main_runs)  # figure removed from the thesis 2026-11-04 (same data as the Ctrl rows of ch6_main_matrices)
    joint = [r for r in runs if "Joint Reference" in roles(r)]
    joint_full = [r for r in joint if not r["train_max_cases"]]
    metric_bars(main_runs, refs["original"], "ch6_main_metrics", joint=joint_full[0] if joint_full else None)
    matrices(main_runs)

    # The sweep plot shows shared LoRA only; the two task-specific ranks are in the table.
    rank_runs = sorted([r for r in runs if "Rank Ablation" in roles(r) and r["strategy"] == "shared_lora"],
                       key=lambda r: int(r["lora_rank"]))
    rank_sweep(rank_runs, refs["original"])

    patellar_curves([r for r in runs if "Convergence Diagnosis" in roles(r)])

    reverse = sorted([r for r in runs if "Task Order Ablation" in roles(r)], key=by_strategy)
    task_order([(counterpart(r, runs), r) for r in reverse], refs)

    # Training loss of the first two tasks of shared LoRA (appendix figure, added 2026-11-05).
    shared = [r for r in runs if r["strategy"] == "shared_lora" and not r["replay_fraction"]
              and not r["train_max_cases"] and r["epochs"] == "10"]
    def pick(rank, order):
        hits = [r for r in shared if r["lora_rank"] == rank and r["task_order"] == order]
        if len(hits) != 1:
            raise SystemExit(f"expected one shared-LoRA run with r = {rank}, {order} order, found {len(hits)}")
        return hits[0]
    shared_lora_first_tasks_loss([
        (pick("1024", "original"), r"$r = 1024$, original order", STRATEGY["shared_lora"][1]),
        (pick("1024", "reverse"), r"$r = 1024$, reverse order", "#2a78d6"),
        (pick("4", "original"), r"$r = 4$, original order", "#eda100"),
    ])

    few = [r for r in runs if "Few-shot" in roles(r)]
    keys = sorted({(r["strategy"], r["lora_rank"]) for r in few}, key=lambda k: STRATEGY_ORDER.index(k[0]))
    groups = []
    for key in keys:
        g = [r for r in few if (r["strategy"], r["lora_rank"]) == key]
        groups.append(g + [counterpart(g[0], runs)])
    equal = [r for r in runs if "Equal Updates" in roles(r)]
    few_shot(groups, refs["original"], equal=equal, joint=joint)


if __name__ == "__main__":
    main()
