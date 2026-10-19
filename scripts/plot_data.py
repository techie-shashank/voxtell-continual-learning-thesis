"""Figures and tables for the Data Description chapter (Ch. 4).

Input:  results/data_stats/ (output of scripts/hpc/data_stats.py, run on the HPC)
        results/data_stats/skm_tea_annotations/v1.0.0/{train,val,test}.json
            (official SKM-TEA annotation files: voxel spacing, orientation, official split,
             pathology bounding boxes)
        thesis/tables/per_volume_dice.csv (to cross-check the test split)
Output: thesis/tables/ch4_datasets.tex   dataset summary (bare tabular)
        thesis/tables/ch4_structures.tex per-task text prompt, label value, structure volume
        thesis/tables/ch4_splits.tex     this thesis's split vs the official SKM-TEA split
        thesis/figures/ch4_examples.pdf  example slices with label overlays
        thesis/figures/ch4_structure_sizes.pdf  distribution of structure volumes

Facts that come from the dataset papers (not from the data) are listed in
PAPER_FACTS with their source; everything else is computed from the data.

Usage (from the repository root):
    python scripts/plot_data.py [--data-dir DIR] [--png DIR]
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from _common import REPO
from _results import FIGURES, TABLES, TEXT_WIDTH_IN, setup_style, y_grid

SKM_TASKS = ["skm_tea_lateral_tibial", "skm_tea_medial_tibial", "skm_tea_femoral",
             "skm_tea_patellar", "skm_tea_medial_meniscus", "skm_tea_lateral_meniscus"]
TASK_NAME = {
    "skm_tea_lateral_tibial": "Lateral tibial cartilage",
    "skm_tea_medial_tibial": "Medial tibial cartilage",
    "skm_tea_femoral": "Femoral cartilage",
    "skm_tea_patellar": "Patellar cartilage",
    "skm_tea_medial_meniscus": "Medial meniscus",
    "skm_tea_lateral_meniscus": "Lateral meniscus",
}
TASK_SHORT = {"skm_tea_lateral_tibial": "LT", "skm_tea_medial_tibial": "MT", "skm_tea_femoral": "Fe",
              "skm_tea_patellar": "Pa", "skm_tea_medial_meniscus": "MM", "skm_tea_lateral_meniscus": "LM"}
# Overlay colours: one per structure (structures do not touch each other much; each is also
# labelled directly in the figure, so identity never relies on colour alone).
TASK_COLOUR = {"skm_tea_lateral_tibial": "#2a78d6", "skm_tea_medial_tibial": "#eb6834",
               "skm_tea_femoral": "#1baf7a", "skm_tea_patellar": "#eda100",
               "skm_tea_medial_meniscus": "#e87ba4", "skm_tea_lateral_meniscus": "#6250d6"}
LUNG_COLOUR = "#2a78d6"

# From the dataset papers (cite them in the caption). Key: (dataset, field) -> (value, source).
PAPER_FACTS = {
    ("skm", "source"): ("Stanford Healthcare", "desai2021skmtea, Sec. 3"),
    ("skm", "modality"): ("MRI, 3D qDESS, echo 1", "desai2021skmtea, Sec. 3; echo 1 per code/scripts/h5_to_nifti.py"),
    ("skm", "scanner"): ("3T GE MR750", "desai2021skmtea, Sec. 3"),
    ("skm", "patients"): ("155", "desai2021skmtea, abstract"),
    ("skm", "labels"): ("manual, 6 tissues", "desai2021skmtea, Sec. 3 and App. A.4"),
    ("skm", "access"): ("github.com/StanfordMIMI/skm-tea", "desai2021skmtea, abstract"),
    ("aero", "source"): ("St. Olavs hospital", "stÃ¸verud2023aeropathairwaysegmentationbenchmark"),
    ("aero", "modality"): ("CT angiography", "stÃ¸verud2023aeropathairwaysegmentationbenchmark"),
    ("aero", "patients"): ("27", "stÃ¸verud2023aeropathairwaysegmentationbenchmark"),
    ("aero", "access"): ("github.com/raidionics/AeroPath", "stÃ¸verud2023aeropathairwaysegmentationbenchmark"),
}

PNG_DIR: Path | None = None


def save(fig, name):
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / f"{name}.pdf")
    if PNG_DIR:
        fig.savefig(PNG_DIR / f"{name}.png", dpi=200)
    plt.close(fig)
    print(f"Wrote thesis/figures/{name}.pdf")


def read_csv(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def check_test_split(skm_rows, aero_rows):
    """The recomputed test split must equal the test volumes in the evaluation logs."""
    per_volume = REPO / "thesis" / "tables" / "per_volume_dice.csv"
    logged = defaultdict(set)
    for r in read_csv(per_volume):
        logged["aeropath" if r["row_task"] == "aeropath" else "skm"].add(r["case_id"])
    skm_test = {r["case_id"] for r in skm_rows if r["split"] == "test"}
    aero_test = {r["case_id"] for r in aero_rows if r["split"] == "test"}
    for name, recomputed in [("skm", skm_test), ("aeropath", aero_test)]:
        if recomputed != logged[name]:
            raise ValueError(f"{name}: recomputed test split {sorted(recomputed)} differs from the "
                             f"evaluation logs {sorted(logged[name])}")
    print("Test splits match the evaluation logs.")


def load_annotations(folder: Path) -> dict:
    """scan_id -> metadata from the official SKM-TEA annotation files."""
    scans = {}
    for official in ("train", "val", "test"):
        d = json.loads((folder / f"{official}.json").read_text())
        names = {c["id"]: c["supercategory"] for c in d["categories"]}
        by_image = defaultdict(set)
        for a in d["annotations"]:
            by_image[a["image_id"]].add(names[a["category_id"]])
        for im in d["images"]:
            scans[im["scan_id"]] = {
                "official_split": official, "subject_id": im["subject_id"], "timepoint": im["timepoint"],
                "voxel_spacing": tuple(im["voxel_spacing"]), "matrix_shape": tuple(im["matrix_shape"]),
                "orientation": tuple(im["orientation"]), "pathologies": sorted(by_image[im["id"]]),
                "version": d["info"]["version"],
            }
    return scans


def iqr(values):
    q1, med, q3 = np.percentile(values, [25, 50, 75])
    return med, q1, q3


def fmt_int(v):
    return f"{int(round(v)):,}".replace(",", "\\,")


def voxel_cm3(spacing) -> float:
    return float(np.prod(spacing)) / 1000.0


def structure_cm3(skm_rows, ann, task):
    return [int(r["structure_voxels"]) * voxel_cm3(ann[r["case_id"]]["voxel_spacing"])
            for r in skm_rows if r["task"] == task]


def tables(skm_rows, aero_rows, meta, ann):
    skm_cases = sorted({r["case_id"] for r in skm_rows})
    skm_split = {s: len({r["case_id"] for r in skm_rows if r["split"] == s}) for s in ("train", "val", "test")}
    aero_split = {s: sum(r["split"] == s for r in aero_rows) for s in ("train", "val", "test")}
    shapes = sorted({r["shape"] for r in skm_rows})
    aero_vox = sorted({r["voxel_size_mm"] for r in aero_rows})

    def rng(values):
        lo, hi = min(values), max(values)
        return f"{lo}" if lo == hi else f"{lo}--{hi}"

    skm_dims = np.array([[int(x) for x in s.split("x")] for s in {r["shape"] for r in skm_rows}])
    aero_dims = np.array([[int(x) for x in r["shape"].split("x")] for r in aero_rows])
    aero_zooms = np.array([[float(x) for x in r["voxel_size_mm"].split("x")] for r in aero_rows])
    skm_spacing = sorted({ann[c]["voxel_spacing"] for c in skm_cases})
    if len(skm_spacing) != 1:
        raise ValueError(f"SKM-TEA voxel spacing is not uniform: {skm_spacing}")
    skm_spacing_txt = " $\\times$ ".join(f"{z:g}" for z in skm_spacing[0])
    with_pathology = sum(bool(ann[c]["pathologies"]) for c in skm_cases)
    subjects = len({ann[c]["subject_id"] for c in skm_cases})
    lines = [
        "% Generated by scripts/plot_data.py from results/data_stats and the dataset papers. Do not edit.",
        r"\small\setlength{\tabcolsep}{4pt}",
        # Wrapping columns (needs the array package, loaded by tabularx in the thesis preamble).
        r"\begin{tabular}{@{}l>{\raggedright\arraybackslash}p{0.34\linewidth}"
        r">{\raggedright\arraybackslash}p{0.34\linewidth}@{}}", r"\toprule",
        r" & SKM-TEA & AeroPath \\", r"\midrule",
        rf"Role in this thesis & six continual-learning tasks & control task \\",
        rf"Imaging & {PAPER_FACTS[('skm', 'modality')][0]} & {PAPER_FACTS[('aero', 'modality')][0]} \\",
        rf"Source & {PAPER_FACTS[('skm', 'source')][0]} & {PAPER_FACTS[('aero', 'source')][0]} \\",
        rf"Volumes used (patients) & {len(skm_cases)} ({subjects}) & {len(aero_rows)} ({PAPER_FACTS[('aero', 'patients')][0]}) \\",
        rf"With pathology label$^{{a}}$ & {with_pathology} of {len(skm_cases)} & -- \\",
        rf"Split (train/val/test) & {skm_split['train']}/{skm_split['val']}/{skm_split['test']} & "
        rf"{aero_split['train']}/{aero_split['val']}/{aero_split['test']} \\",
        "Volume size (voxels) & "
        + " $\\times$ ".join(rng(skm_dims[:, a]) for a in range(3)) + " & "
        + " $\\times$ ".join(rng(aero_dims[:, a]) for a in range(3)) + r" \\",
        f"Voxel size (mm) & {skm_spacing_txt}$^{{b}}$ & "
        + " $\\times$ ".join(rng([f"{z:.2f}" for z in aero_zooms[:, a]]) for a in range(3))
        + r" \\",
        rf"Structures used & 6 (Table~\ref{{tab:ch4_structures}}) & lung \\",
        rf"Access & \url{{{PAPER_FACTS[('skm', 'access')][0]}}} & \url{{{PAPER_FACTS[('aero', 'access')][0]}}} \\",
        r"\bottomrule", r"\end{tabular}",
        # Footnotes as wrapping text below the table (they would widen the tabular otherwise).
        r"\par\smallskip{\footnotesize\raggedright"
        r" $^{a}$ At least one pathology bounding box in the official SKM-TEA annotation files"
        r" (cartilage lesion, effusion, meniscal tear, ligament tear).\par"
        r" $^{b}$ From the official annotation files; the NIfTI files used in this thesis store an"
        r" identity affine (1\,mm).\par}", ""]
    (TABLES / "ch4_datasets.tex").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote thesis/tables/ch4_datasets.tex")

    lines = ["% Generated by scripts/plot_data.py from results/data_stats. Do not edit.",
             r"\small\setlength{\tabcolsep}{4pt}",
             r"\begin{tabular}{lllr}", r"\toprule",
             r"Task & Text prompt & Label & Volume (cm$^3$), median [IQR] \\", r"\midrule"]
    for t in SKM_TASKS:
        rows = [r for r in skm_rows if r["task"] == t]
        labels = sorted({r["label_value"] for r in rows})
        med, q1, q3 = iqr(structure_cm3(skm_rows, ann, t))
        lines.append(rf"{TASK_NAME[t]} & ``{rows[0]['prompt']}'' & {', '.join(labels)} & "
                     rf"{med:.2f} [{q1:.2f}, {q3:.2f}] \\")
    med, q1, q3 = iqr([float(r["lung_volume_ml"]) for r in aero_rows])
    lines += [r"\midrule",
              rf"Control task (AeroPath) & ``lung'' & -- & {fmt_int(med)} [{fmt_int(q1)}, {fmt_int(q3)}] \\",
              r"\bottomrule", r"\end{tabular}", ""]
    (TABLES / "ch4_structures.tex").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote thesis/tables/ch4_structures.tex")

    # This thesis's split (rows) against the official SKM-TEA split (columns).
    ours = {r["case_id"]: r["split"] for r in skm_rows}
    official_names = {"train": "Train", "val": "Val.", "test": "Test$^{a}$"}
    lines = ["% Generated by scripts/plot_data.py from results/data_stats. Do not edit.",
             r"\small\setlength{\tabcolsep}{6pt}",
             r"\begin{tabular}{lrrrr}", r"\toprule",
             r" & \multicolumn{3}{c}{Official SKM-TEA split} & \\", r"\cmidrule(lr){2-4}",
             r"This thesis & " + " & ".join(official_names.values()) + r" & Total \\", r"\midrule"]
    for s, name in [("train", "Training"), ("val", "Validation"), ("test", "Test")]:
        counts = [sum(1 for c, v in ours.items() if v == s and ann[c]["official_split"] == o)
                  for o in ("train", "val", "test")]
        lines.append(rf"{name} & " + " & ".join(map(str, counts)) + rf" & {sum(counts)} \\")
    totals = [sum(1 for c in ours if ann[c]["official_split"] == o) for o in ("train", "val", "test")]
    lines += [r"\midrule", "Total & " + " & ".join(map(str, totals)) + rf" & {len(ours)} \\",
              r"\bottomrule", r"\end{tabular}",
              r"\par\smallskip{\footnotesize $^{a}$ Patients with additional arthroscopic surgery.\par}", ""]
    (TABLES / "ch4_splits.tex").write_text("\n".join(lines), encoding="utf-8")
    print("Wrote thesis/tables/ch4_splits.tex")


def example_figure(ex, aero_spacing, extra=None, skm_spacing=None):
    """(a) SKM-TEA sagittal slice with the most labelled voxels, [(b) SKM-TEA coronal slice
    through the tibial plateau, if examples_extra.npz exists,] and an AeroPath coronal slice.

    SKM-TEA arrays are stored (SI, AP, LR) (official annotation files, field 'orientation'):
    row 0 = superior, so slices are shown without transposing, superior up (anterior left in
    the sagittal view). The coronal SKM-TEA slice has rows SI (skm_spacing[0] mm) and columns
    LR (skm_spacing[2] mm); its pixel aspect is corrected. AeroPath slices come from the
    RAS-canonical volume and are shown in radiological convention (patient's right on the
    viewer's left); the pixel aspect is set from aero_spacing = (x, y, z) mm.
    """
    from matplotlib.patches import Patch

    n = 3 if extra is not None else 2
    fig, axes = plt.subplots(1, n, figsize=(TEXT_WIDTH_IN, 3.1), layout="constrained",
                             gridspec_kw={"width_ratios": [1.0, 0.75, 0.8] if n == 3 else [1, 1]})
    label_of = json.loads(str(ex["skm_label_map"]))

    def knee(ax, img, lab, aspect, title):
        lo, hi = np.percentile(img, [1, 99])
        ax.imshow(img, cmap="gray", vmin=lo, vmax=hi, aspect=aspect)
        overlay = np.zeros((*lab.shape, 4))
        for task in SKM_TASKS:
            overlay[lab == label_of[task]] = matplotlib_rgba(TASK_COLOUR[task], 0.75)
        ax.imshow(overlay, aspect=aspect)
        ax.set_title(title, fontsize=9)

    # Sagittal (fixed LR index): rows SI, columns AP, both in-plane -> square pixels.
    knee(axes[0], ex["skm_img_ax2"], ex["skm_lab_ax2"], 1.0, "(a) SKM-TEA, sagittal")
    if extra is not None:
        if str(extra["skm_case"]) != str(ex["skm_case"]):
            raise ValueError("examples_extra.npz is from a different volume than examples.npz")
        knee(axes[1], extra["skm_img_coronal"], extra["skm_lab_coronal"],
             skm_spacing[0] / skm_spacing[2], "(b) SKM-TEA, coronal")
    letter = "c" if n == 3 else "b"
    img, lab = ex["aero_img_ax1"], ex["aero_lab_ax1"]
    aspect = aero_spacing[2] / aero_spacing[0]          # rows = z, columns = x
    axes[-1].imshow(img.T, cmap="gray", vmin=-1000, vmax=400, origin="lower", aspect=aspect)
    overlay = np.zeros((*lab.T.shape, 4))
    overlay[lab.T > 0] = matplotlib_rgba(LUNG_COLOUR, 0.35)
    axes[-1].imshow(overlay, origin="lower", aspect=aspect)
    axes[-1].invert_xaxis()
    axes[-1].set_title(f"({letter}) AeroPath, coronal", fontsize=9)
    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_visible(False)
    handles = [Patch(facecolor=TASK_COLOUR[t], label=TASK_NAME[t]) for t in SKM_TASKS]
    handles.append(Patch(facecolor=LUNG_COLOUR, alpha=0.5, label="Lung (control task)"))
    fig.legend(handles=handles, loc="outside lower center", ncol=4, frameon=False, fontsize=8)
    # Case IDs contain '_', which the Computer Modern font cannot render; name them in the caption.
    print(f"Example volumes: SKM-TEA {ex['skm_case']} (slices {ex['skm_index'].tolist()}), "
          f"AeroPath {ex['aero_case']} (slices {ex['aero_index'].tolist()})")
    save(fig, "ch4_examples")


def matplotlib_rgba(hex_colour, alpha):
    h = hex_colour.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)] + [alpha]


def size_figure(skm_rows, ann):
    fig, ax = plt.subplots(figsize=(TEXT_WIDTH_IN, 2.6))
    rng = np.random.default_rng(0)
    for k, t in enumerate(SKM_TASKS):
        vals = np.array(structure_cm3(skm_rows, ann, t))
        ax.boxplot(vals, positions=[k], widths=0.5, showfliers=False,
                   medianprops={"color": "#0b0b0b"}, boxprops={"color": "#52514e"},
                   whiskerprops={"color": "#52514e"}, capprops={"color": "#52514e"})
        ax.scatter(k + rng.uniform(-0.18, 0.18, len(vals)), vals, s=6, color=TASK_COLOUR[t],
                   alpha=0.7, linewidths=0, zorder=3)
    ax.set_yscale("log")
    ax.set_xticks(range(len(SKM_TASKS)), [TASK_NAME[t].replace(" ", "\n", 1) for t in SKM_TASKS])
    ax.set_ylabel("Structure volume (cm$^3$)")
    y_grid(ax)
    fig.tight_layout(pad=0.3)
    save(fig, "ch4_structure_sizes")


def main():
    global PNG_DIR
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default=str(REPO / "results" / "data_stats"))
    parser.add_argument("--png")
    args = parser.parse_args()
    PNG_DIR = Path(args.png) if args.png else None
    data = Path(args.data_dir)

    setup_style()
    skm_rows = read_csv(data / "skm_tea_volumes.csv")
    aero_rows = read_csv(data / "aeropath_volumes.csv")
    meta = json.loads((data / "meta.json").read_text())
    check_test_split(skm_rows, aero_rows)
    ann = load_annotations(data / "skm_tea_annotations" / "v1.0.0")
    if set(ann) != {r["case_id"] for r in skm_rows}:
        raise ValueError("SKM-TEA scan IDs differ between the data and the official annotation files")

    ex = dict(np.load(data / "examples.npz", allow_pickle=False))
    label_map = {t: int(next(r["label_value"] for r in skm_rows if r["task"] == t)) for t in SKM_TASKS
                 if next(r["label_value"] for r in skm_rows if r["task"] == t) not in ("", "None")}
    ex["skm_label_map"] = json.dumps(label_map)

    tables(skm_rows, aero_rows, meta, ann)
    aero_row = next(r for r in aero_rows if r["case_id"] == str(ex["aero_case"]))
    extra_file = data / "examples_extra.npz"
    extra = dict(np.load(extra_file)) if extra_file.exists() else None
    if extra is None:
        print("examples_extra.npz not found: example figure without the coronal knee slice "
              "(run scripts/hpc/data_stats.py --examples-only on the HPC)")
    example_figure(ex, [float(z) for z in aero_row["voxel_size_mm"].split("x")], extra,
                   ann[str(ex["skm_case"])]["voxel_spacing"])
    size_figure(skm_rows, ann)


if __name__ == "__main__":
    main()
