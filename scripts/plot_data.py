"""Figures and tables for the Data Description chapter (Ch. 4).

Input:  results/data_stats/ (output of scripts/hpc/data_stats.py, run on the HPC)
        results/data_stats/skm_tea_annotations/v1.0.0/{train,val,test}.json
            (official SKM-TEA annotation files: voxel spacing, orientation, official split,
             pathology bounding boxes)
        thesis/tables/per_volume_dice.csv (to cross-check the test split)
Output: thesis/tables/ch4_datasets.tex   dataset summary (bare tabular)
        stdout: this thesis's split vs the official SKM-TEA split (not in the text; defense point D3)
        thesis/figures/ch4_examples.pdf  example slices with label overlays
        stdout: median structure volume per task (quoted in Ch. 4.2)

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
from _results import FIGURES, TABLES, TEXT_WIDTH_IN, setup_style

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
# Overlay colours: one per structure, from the categorical palette of the dataviz skill.
TASK_COLOUR = {"skm_tea_lateral_tibial": "#2a78d6", "skm_tea_medial_tibial": "#eb6834",
               "skm_tea_femoral": "#1baf7a", "skm_tea_patellar": "#eda100",
               "skm_tea_medial_meniscus": "#6250d6", "skm_tea_lateral_meniscus": "#b5179e"}
# Chosen with the dataviz palette validator so that structures touching in the knee images
# (femoral with patellar, tibial and menisci; each meniscus with its tibial cartilage) differ by
# normal-vision dE >= 22.9 and CVD dE >= 9.1. The lung (alone in its panel) differs from all knee
# colours by normal dE >= 15.6; under CVD it is close to medial tibial cartilage (dE 3.2).
LUNG_COLOUR = "#008300"

# From the dataset papers (cite them in the caption). Key: (dataset, field) -> (value, source).
PAPER_FACTS = {
    ("skm", "source"): ("Stanford Healthcare", "desai2021skmtea, Sec. 3"),
    ("skm", "modality"): ("MRI, 3D qDESS, echo 1", "desai2021skmtea, Sec. 3; echo 1 per code/scripts/h5_to_nifti.py"),
    ("skm", "scanner"): ("3T GE MR750", "desai2021skmtea, Sec. 3"),
    ("skm", "patients"): ("155", "desai2021skmtea, abstract"),
    ("skm", "labels"): ("manual, 6 tissues", "desai2021skmtea, Sec. 3 and App. A.4"),
    ("skm", "access"): ("github.com/StanfordMIMI/skm-tea", "desai2021skmtea, abstract"),
    ("aero", "source"): ("St. Olavs Hospital", "stÃ¸verud2023aeropathairwaysegmentationbenchmark"),
    ("aero", "modality"): ("CT angiography", "stÃ¸verud2023aeropathairwaysegmentationbenchmark"),
    ("aero", "patients"): ("27", "stÃ¸verud2023aeropathairwaysegmentationbenchmark"),
    ("aero", "access"): ("github.com/raidionics/AeroPath", "stÃ¸verud2023aeropathairwaysegmentationbenchmark"),
}

PNG_DIR: Path | None = None
EXAMPLE_DPI = 600   # print resolution of the image slices in ch4_examples.pdf


def save(fig, name, dpi="figure"):
    """dpi sets the resolution at which images inside the vector PDF are rasterised."""
    FIGURES.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIGURES / f"{name}.pdf", dpi=dpi)
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
        rf"Volumes (patients) & {len(skm_cases)} ({subjects}) & {len(aero_rows)} ({PAPER_FACTS[('aero', 'patients')][0]}) \\",
        rf"With pathology label$^{{a}}$ & {with_pathology} of {len(skm_cases)} & -- \\",
        rf"Split (train/val/test) & {skm_split['train']}/{skm_split['val']}/{skm_split['test']} & "
        rf"{aero_split['train']}/{aero_split['val']}/{aero_split['test']} \\",
        "Volume size (voxels) & "
        + " $\\times$ ".join(rng(skm_dims[:, a]) for a in range(3)) + " & "
        + " $\\times$ ".join(rng(aero_dims[:, a]) for a in range(3)) + r" \\",
        f"Voxel size (mm) & {skm_spacing_txt}$^{{b}}$ & "
        + " $\\times$ ".join(rng([f"{z:.2f}" for z in aero_zooms[:, a]]) for a in range(3))
        + r" \\",
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

    # Structure sizes are quoted in the text of Ch. 4.1 (no table or figure).
    for t in SKM_TASKS:
        prompt = next(r["prompt"] for r in skm_rows if r["task"] == t)
        med, q1, q3 = iqr(structure_cm3(skm_rows, ann, t))
        print(f"{TASK_NAME[t]} ('{prompt}'): median {med:.2f} cm3 [IQR {q1:.2f}, {q3:.2f}]")

    # This thesis's split against the official SKM-TEA split (not in the text; defense point D3).
    ours = {r["case_id"]: r["split"] for r in skm_rows}
    print("This thesis's split vs official SKM-TEA split (train/val/test):")
    for s_ in ("train", "val", "test"):
        counts = [sum(1 for c, v in ours.items() if v == s_ and ann[c]["official_split"] == o)
                  for o in ("train", "val", "test")]
        print(f"  {s_}: {counts[0]}/{counts[1]}/{counts[2]} (total {sum(counts)})")


def example_figure(ex, aero_spacing, extra=None, skm_spacing=None):
    """(a) SKM-TEA sagittal slice with the most labelled voxels, [(b) SKM-TEA coronal slice
    through the tibial plateau, if examples_extra.npz exists,] and an AeroPath coronal slice.

    SKM-TEA arrays are stored (SI, AP, LR) (official annotation files, field 'orientation'):
    row 0 = superior, so slices are shown without transposing, superior up (anterior left in
    the sagittal view). The coronal SKM-TEA slice has rows SI (skm_spacing[0] mm) and columns
    LR (skm_spacing[2] mm); its pixel aspect is corrected. AeroPath slices come from the
    RAS-canonical volume and are shown in radiological convention (patient's right on the
    viewer's left); the pixel aspect is set from aero_spacing = (x, y, z) mm.

    The knee panels are cropped to the labelled region plus a margin, so that the thin
    structures are visible at print size. All labels are opaque, so the legend shows the
    colours as printed.
    Images are rasterised at 600 dpi (EXAMPLE_DPI) inside the vector PDF.
    """
    from matplotlib.patches import Patch

    label_of = json.loads(str(ex["skm_label_map"]))

    def crop(img, lab, margin=0.35):
        rows, cols = np.nonzero(lab)
        r0, r1, c0, c1 = rows.min(), rows.max() + 1, cols.min(), cols.max() + 1
        dr, dc = int(margin * (r1 - r0)), int(margin * (c1 - c0))
        r0, r1 = max(r0 - dr, 0), min(r1 + dr, lab.shape[0])
        c0, c1 = max(c0 - dc, 0), min(c1 + dc, lab.shape[1])
        return img[r0:r1, c0:c1], lab[r0:r1, c0:c1]

    # Panels: (image, labels, pixel aspect, title); width ratios give all panels one height.
    panels = [crop(ex["skm_img_ax2"], ex["skm_lab_ax2"]) + (1.0, "(a) SKM-TEA, sagittal")]
    if extra is not None:
        if str(extra["skm_case"]) != str(ex["skm_case"]):
            raise ValueError("examples_extra.npz is from a different volume than examples.npz")
        panels.append(crop(extra["skm_img_coronal"], extra["skm_lab_coronal"])
                      + (skm_spacing[0] / skm_spacing[2], "(b) SKM-TEA, coronal"))
    letter = "c" if extra is not None else "b"
    aero_img, aero_lab = ex["aero_img_ax1"].T, ex["aero_lab_ax1"].T      # rows = z, columns = x
    aero_aspect = aero_spacing[2] / aero_spacing[0]
    ratios = [img.shape[1] / (img.shape[0] * a) for img, _, a, _ in panels]
    ratios.append(aero_img.shape[1] / (aero_img.shape[0] * aero_aspect))
    panel_h = (TEXT_WIDTH_IN - 0.1 * len(ratios)) / sum(ratios)

    fig, axes = plt.subplots(1, len(ratios), figsize=(TEXT_WIDTH_IN, panel_h + 0.85),
                             layout="constrained", gridspec_kw={"width_ratios": ratios})
    for ax, (img, lab, aspect, title) in zip(axes, panels):
        lo, hi = np.percentile(img, [1, 99])
        ax.imshow(img, cmap="gray", vmin=lo, vmax=hi, aspect=aspect, interpolation="bilinear")
        overlay = np.zeros((*lab.shape, 4))
        for task in SKM_TASKS:
            overlay[lab == label_of[task]] = matplotlib_rgba(TASK_COLOUR[task], 1.0)
        ax.imshow(overlay, aspect=aspect, interpolation="nearest")
        ax.set_title(title, fontsize=10)

    ax = axes[-1]
    ax.imshow(aero_img, cmap="gray", vmin=-1000, vmax=400, origin="lower", aspect=aero_aspect,
              interpolation="bilinear")
    overlay = np.zeros((*aero_lab.shape, 4))
    overlay[aero_lab > 0] = matplotlib_rgba(LUNG_COLOUR, 1.0)
    ax.imshow(overlay, origin="lower", aspect=aero_aspect, interpolation="nearest")
    ax.invert_xaxis()
    ax.set_title(f"({letter}) AeroPath, coronal", fontsize=10)
    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_visible(False)

    # Legend in four columns: cartilages, tibial cartilages, menisci, control task.
    order = ["skm_tea_femoral", "skm_tea_patellar", "skm_tea_lateral_tibial", "skm_tea_medial_tibial",
             "skm_tea_lateral_meniscus", "skm_tea_medial_meniscus"]
    handles = [Patch(facecolor=TASK_COLOUR[t], label=TASK_NAME[t]) for t in order]
    handles.append(Patch(facecolor=LUNG_COLOUR, label="Lung (control task)"))
    fig.legend(handles=handles, loc="outside lower center", ncol=4, frameon=False, fontsize=10,
               columnspacing=0.8, handlelength=1.2, handletextpad=0.5)
    # Case IDs contain '_', which the Computer Modern font cannot render; name them in the caption.
    print(f"Example volumes: SKM-TEA {ex['skm_case']} (slices {ex['skm_index'].tolist()}), "
          f"AeroPath {ex['aero_case']} (slices {ex['aero_index'].tolist()})")
    with plt.rc_context({"image.composite_image": False}):
        save(fig, "ch4_examples", dpi=EXAMPLE_DPI)


def matplotlib_rgba(hex_colour, alpha):
    h = hex_colour.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)] + [alpha]


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


if __name__ == "__main__":
    main()
