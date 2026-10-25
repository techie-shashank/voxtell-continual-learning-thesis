"""Image assets for the TikZ diagrams (Ch. 1, Ch. 3 and Ch. 5).

Crops a square region around the femoral cartilage from the sagittal SKM-TEA example slice
that Ch. 4 already shows (MTR_005, results/data_stats/examples.npz, test split) and writes
  thesis/figures/tikz/knee_patch.png       image only (input of the diagram)
  thesis/figures/tikz/knee_patch_mask.png  image with the femoral-cartilage label overlaid
The overlay is the reference label, used in the diagram to illustrate the output mask.

For the Ch. 1 setting figure, it also writes (same example volumes as Fig. ch4_examples)
  thesis/figures/tikz/ch1_task_<task>.png  coronal SKM-TEA slice (results/data_stats/
      examples_extra.npz), the full slice without cropping, with only that task's reference
      label overlaid in its Ch. 4 colour
  thesis/figures/tikz/ch1_lung.png         full coronal AeroPath slice with the lung label, padded
      with air above and below to the aspect of the knee slice
The Ch. 1 images are resampled to square physical pixels (voxel spacing from the SKM-TEA
annotation files and the AeroPath csv) at CH1_WIDTH_PX, about 535 dpi at their printed width:
the image bicubically, the label linearly and thresholded at 0.5 (smooth edges).

Usage (from the repository root):
    python scripts/make_diagram_assets.py
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import zoom

from _common import REPO
from plot_data import LUNG_COLOUR, TASK_COLOUR, load_annotations, matplotlib_rgba

OUT = REPO / "thesis" / "figures" / "tikz"
TASK = "skm_tea_femoral"
CH1_TASKS = ["skm_tea_lateral_tibial", "skm_tea_medial_tibial", "skm_tea_lateral_meniscus"]
SIZE_PX = 256  # output resolution; the diagram shows the patch at about 2.5 cm
CH1_WIDTH_PX = 600  # Ch. 1 images are printed 28.5 mm wide: about 535 dpi


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


def resample(arr, height_mm, width_mm, order, h=None):
    """Resample a 2D slice to square physical pixels, CH1_WIDTH_PX wide (scipy spline order).

    h fixes the height in pixels (equal image heights in the figure despite rounding)."""
    h = h or int(round(CH1_WIDTH_PX * height_mm / width_mm))
    return zoom(arr.astype(float), (h / arr.shape[0], CH1_WIDTH_PX / arr.shape[1]), order=order,
                grid_mode=True, mode="nearest")


def grey(img, lo, hi):
    g = np.clip((img - lo) / (hi - lo), 0, 1)
    return np.repeat(g[..., None], 3, axis=2)


def ch1_assets(ex):
    extra = dict(np.load(REPO / "results" / "data_stats" / "examples_extra.npz", allow_pickle=False))
    if str(extra["skm_case"]) != str(ex["skm_case"]):
        raise ValueError("examples_extra.npz is from a different volume than examples.npz")
    spacing = load_annotations(REPO / "results" / "data_stats" / "skm_tea_annotations" / "v1.0.0")[
        str(extra["skm_case"])]["voxel_spacing"]
    img, lab = extra["skm_img_coronal"], extra["skm_lab_coronal"]   # rows SI, columns LR (as Ch. 4)
    size_mm = (img.shape[0] * spacing[0], img.shape[1] * spacing[2])
    lo, hi = np.percentile(img, [1, 99])
    rgb = grey(resample(img, *size_mm, order=3), lo, hi)
    for task in CH1_TASKS:
        mask = resample(lab == label_value(task), *size_mm, order=1) > 0.5
        colour = np.array(matplotlib_rgba(TASK_COLOUR[task], 1.0)[:3])
        out = rgb.copy()
        out[mask] = 0.25 * rgb[mask] + 0.75 * colour
        plt.imsave(OUT / f"ch1_task_{task.removeprefix('skm_tea_')}.png", out)
    print(f"Wrote ch1_task_*.png ({extra['skm_case']}, coronal slice {int(extra['coronal_index'])}, "
          f"{rgb.shape[1]} x {rgb.shape[0]} px)")

    with open(REPO / "results" / "data_stats" / "aeropath_volumes.csv", newline="", encoding="utf-8") as f:
        row = next(r for r in csv.DictReader(f) if r["case_id"] == str(ex["aero_case"]))
    sx, _, sz = (float(v) for v in row["voxel_size_mm"].split("x"))
    img = ex["aero_img_ax1"].T[::-1, ::-1]                    # rows z (superior up), radiological
    lab = ex["aero_lab_ax1"].T[::-1, ::-1] > 0
    width_mm = img.shape[1] * sx
    pad = int(round((width_mm * size_mm[0] / size_mm[1] - img.shape[0] * sz) / sz / 2))
    img = np.pad(img, ((pad, pad), (0, 0)), constant_values=-1000)   # air: same aspect as the knee
    lab = np.pad(lab, ((pad, pad), (0, 0)))
    height_mm = img.shape[0] * sz
    h = int(round(CH1_WIDTH_PX * size_mm[0] / size_mm[1]))
    rgb = grey(resample(img, height_mm, width_mm, order=3, h=h), -1000, 400)   # window as Fig. ch4_examples
    mask = resample(lab, height_mm, width_mm, order=1, h=h) > 0.5
    colour = np.array(matplotlib_rgba(LUNG_COLOUR, 1.0)[:3])
    rgb[mask] = 0.65 * rgb[mask] + 0.35 * colour               # lung alpha as Fig. ch4_examples
    plt.imsave(OUT / "ch1_lung.png", rgb)
    print(f"Wrote ch1_lung.png (AeroPath {ex['aero_case']}, {rgb.shape[1]} x {rgb.shape[0]} px)")


def resize(arr, size):
    """Nearest-neighbour resize to size x size (keeps the label edges sharp)."""
    idx = (np.arange(size) * arr.shape[0] / size).astype(int)
    return arr[idx][:, idx]


if __name__ == "__main__":
    main()
