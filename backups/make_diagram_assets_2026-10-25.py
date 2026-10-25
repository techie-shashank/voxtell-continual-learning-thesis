"""Image assets for the TikZ diagrams (Ch. 1, Ch. 3 and Ch. 5).

Crops a square region around the femoral cartilage from the sagittal SKM-TEA example slice
that Ch. 4 already shows (MTR_005, results/data_stats/examples.npz, test split) and writes
  thesis/figures/tikz/knee_patch.png       image only (input of the diagram)
  thesis/figures/tikz/knee_patch_mask.png  image with the femoral-cartilage label overlaid
The overlay is the reference label, used in the diagram to illustrate the output mask.

For the Ch. 1 setting figure, it also writes (same example volumes as Fig. ch4_examples)
  thesis/figures/tikz/ch1_task_<task>.png  coronal SKM-TEA slice (results/data_stats/
      examples_extra.npz), one square crop around the tibiofemoral joint (same field of view
      for every task), with only that task's reference label overlaid in its Ch. 4 colour
  thesis/figures/tikz/ch1_lung.png         coronal AeroPath slice with the lung label
Pixel aspects are corrected from the voxel spacing (SKM-TEA annotation files, AeroPath csv).

Usage (from the repository root):
    python scripts/make_diagram_assets.py
"""
import csv

import matplotlib.pyplot as plt
import numpy as np

from _common import REPO
from plot_data import LUNG_COLOUR, TASK_COLOUR, load_annotations, matplotlib_rgba

OUT = REPO / "thesis" / "figures" / "tikz"
TASK = "skm_tea_femoral"
JOINT = ["skm_tea_medial_tibial", "skm_tea_lateral_tibial", "skm_tea_medial_meniscus",
         "skm_tea_lateral_meniscus"]                   # field of view of the Ch. 1 crops
CH1_TASKS = ["skm_tea_lateral_tibial", "skm_tea_medial_tibial", "skm_tea_lateral_meniscus"]
SIZE_PX = 256  # output resolution; the diagram shows the patch at about 2.5 cm


def main():
    ex = dict(np.load(REPO / "results" / "data_stats" / "examples.npz", allow_pickle=False))
    img, lab = ex["skm_img_ax2"], ex["skm_lab_ax2"]          # sagittal, rows SI, columns AP
    with open(REPO / "results" / "data_stats" / "skm_tea_volumes.csv", newline="", encoding="utf-8") as f:
        label = int(next(r["label_value"] for r in csv.DictReader(f) if r["task"] == TASK))
    rows, cols = np.nonzero(lab == label)
    half = int(0.6 * max(np.ptp(rows), np.ptp(cols)))             # square around the cartilage
    r0, c0 = int(rows.mean()), int(cols.mean())
    r0 = min(max(r0, half), img.shape[0] - half)
    c0 = min(max(c0, half), img.shape[1] - half)
    sl = (slice(r0 - half, r0 + half), slice(c0 - half, c0 + half))
    crop, mask = img[sl], lab[sl] == label

    lo, hi = np.percentile(crop, [1, 99])
    grey = np.clip((crop - lo) / (hi - lo), 0, 1)
    rgb = np.repeat(grey[..., None], 3, axis=2)
    colour = np.array(matplotlib_rgba(TASK_COLOUR[TASK], 1.0)[:3])
    overlay = rgb.copy()
    overlay[mask] = 0.25 * rgb[mask] + 0.75 * colour

    OUT.mkdir(parents=True, exist_ok=True)
    for name, arr in [("knee_patch", rgb), ("knee_patch_mask", overlay)]:
        plt.imsave(OUT / f"{name}.png", resize(arr, SIZE_PX))
        print(f"Wrote thesis/figures/tikz/{name}.png ({ex['skm_case']}, crop {2 * half} px)")
    ch1_assets(ex)


def label_value(task):
    with open(REPO / "results" / "data_stats" / "skm_tea_volumes.csv", newline="", encoding="utf-8") as f:
        return int(next(r["label_value"] for r in csv.DictReader(f) if r["task"] == task))


def stretch(arr, factor, axis):
    """Nearest-neighbour stretch of one axis by a (non-integer) factor: square physical pixels."""
    n = int(round(arr.shape[axis] * factor))
    idx = np.minimum((np.arange(n) / factor).astype(int), arr.shape[axis] - 1)
    return np.take(arr, idx, axis=axis)


def square_crop(mask, pad):
    """Square slice pair around the foreground of mask, padded by pad x its larger extent."""
    rows, cols = np.nonzero(mask)
    half = int((0.5 + pad) * max(np.ptp(rows), np.ptp(cols)))
    r0, c0 = int(rows.min() + rows.max()) // 2, int(cols.min() + cols.max()) // 2
    r0 = min(max(r0, half), mask.shape[0] - half)
    c0 = min(max(c0, half), mask.shape[1] - half)
    return slice(r0 - half, r0 + half), slice(c0 - half, c0 + half)


def grey(img, lo, hi):
    g = np.clip((img - lo) / (hi - lo), 0, 1)
    return np.repeat(g[..., None], 3, axis=2)


def ch1_assets(ex):
    extra = dict(np.load(REPO / "results" / "data_stats" / "examples_extra.npz", allow_pickle=False))
    if str(extra["skm_case"]) != str(ex["skm_case"]):
        raise ValueError("examples_extra.npz is from a different volume than examples.npz")
    spacing = load_annotations(REPO / "results" / "data_stats" / "skm_tea_annotations" / "v1.0.0")[
        str(extra["skm_case"])]["voxel_spacing"]
    factor = spacing[2] / spacing[0]                          # rows SI, columns LR (as Ch. 4)
    img = stretch(extra["skm_img_coronal"], factor, 1)
    lab = stretch(extra["skm_lab_coronal"], factor, 1)
    joint = np.isin(lab, [label_value(t) for t in JOINT])
    sl = square_crop(joint, 0.15)
    crop, labc = img[sl], lab[sl]
    lo, hi = np.percentile(crop, [1, 99])
    rgb = grey(crop, lo, hi)
    for task in CH1_TASKS:
        mask = labc == label_value(task)
        colour = np.array(matplotlib_rgba(TASK_COLOUR[task], 1.0)[:3])
        out = rgb.copy()
        out[mask] = 0.25 * rgb[mask] + 0.75 * colour
        plt.imsave(OUT / f"ch1_task_{task.removeprefix('skm_tea_')}.png", resize(out, SIZE_PX))
    print(f"Wrote ch1_task_*.png ({extra['skm_case']}, coronal slice {int(extra['coronal_index'])})")

    with open(REPO / "results" / "data_stats" / "aeropath_volumes.csv", newline="", encoding="utf-8") as f:
        row = next(r for r in csv.DictReader(f) if r["case_id"] == str(ex["aero_case"]))
    sx, _, sz = (float(v) for v in row["voxel_size_mm"].split("x"))
    img = ex["aero_img_ax1"].T[::-1, ::-1]                    # rows z (superior up), radiological
    lab = ex["aero_lab_ax1"].T[::-1, ::-1] > 0
    img, lab = stretch(img, sz / sx, 0), stretch(lab, sz / sx, 0)
    sl = square_crop(lab, 0.08)
    rgb = grey(img[sl], -1000, 400)                            # window as Fig. ch4_examples
    mask = lab[sl]
    colour = np.array(matplotlib_rgba(LUNG_COLOUR, 1.0)[:3])
    rgb[mask] = 0.65 * rgb[mask] + 0.35 * colour               # lung alpha as Fig. ch4_examples
    plt.imsave(OUT / "ch1_lung.png", resize(rgb, SIZE_PX))
    print(f"Wrote ch1_lung.png (AeroPath {ex['aero_case']})")


def resize(arr, size):
    """Nearest-neighbour resize to size x size (keeps the label edges sharp)."""
    idx = (np.arange(size) * arr.shape[0] / size).astype(int)
    return arr[idx][:, idx]


if __name__ == "__main__":
    main()
