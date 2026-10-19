"""Collect the dataset statistics for the Data Description chapter. RUN ON THE HPC.

The volumes are only on the HPC, so this script runs there, inside the VoxTell
code directory, with the same Python environment as the experiments. It uses
the code's own dataset adapters (src/data/adapters, including skm_tea.py, which
is only on the HPC) and repeats the split logic of src/data/datamodule.py
(_build_splits: adapter.cases(), random.Random(seed).shuffle, round(n * fraction)),
so the cases, label values and splits are exactly those of the experiments.

Usage (on the HPC, from the VoxTell code directory, so that `src` can be imported):
    cd /home/hpc/iwi5/iwi5326h/projects/VoxTell
    python -u scripts/data_stats.py --out ./data_stats
It prints a timestamped line at start and progress every 10 volumes; reading all
155 + 27 volumes takes several minutes. On a login node, prefer a compute node
(e.g. inside a SLURM job). Then copy the output folder to results/data_stats/ in
the thesis repository.

Output (in --out):
  skm_tea_volumes.csv     one row per SKM-TEA volume and task: case_id, task,
                          split, label value, voxel count of the structure,
                          image shape, header voxel size, intensity percentiles
  aeropath_volumes.csv    one row per AeroPath volume: case_id, split, shape,
                          voxel size, lung voxel count and volume (ml), HU range
  examples.npz            orthogonal slices of one SKM-TEA and one AeroPath test
                          volume (image + labels) for the example figure
  meta.json               date, host, code commit, arguments, split sizes

Only numpy and nibabel are needed besides the code itself.
"""
from __future__ import annotations

import argparse
import csv
import json
import platform
import random
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import nibabel as nib
import numpy as np

SKM_TASKS = ["skm_tea_lateral_tibial", "skm_tea_medial_tibial", "skm_tea_femoral",
             "skm_tea_patellar", "skm_tea_medial_meniscus", "skm_tea_lateral_meniscus"]
PROMPT = {  # the text prompt of each task, as in the training logs
    "skm_tea_lateral_tibial": "lateral tibial cartilage",
    "skm_tea_medial_tibial": "medial tibial cartilage",
    "skm_tea_femoral": "femoral cartilage",
    "skm_tea_patellar": "patellar cartilage",
    "skm_tea_medial_meniscus": "medial meniscus",
    "skm_tea_lateral_meniscus": "lateral meniscus",
}


def log(message: str) -> None:
    print(f"[{datetime.now():%H:%M:%S}] {message}", flush=True)


def splits(cases, seed: int, train_fraction: float, val_fraction: float) -> dict:
    """Mirror of src/data/datamodule.py _build_splits."""
    cases = list(cases)
    random.Random(seed).shuffle(cases)
    n = len(cases)
    n_train, n_val = round(n * train_fraction), round(n * val_fraction)
    out = {}
    for i, c in enumerate(cases):
        out[str(c.image_path)] = "train" if i < n_train else ("val" if i < n_train + n_val else "test")
    return out


def case_id(path: Path) -> str:
    name = path.name.removesuffix(".nii.gz")
    return name.removesuffix("_CT_HR")


def target(case, prompt: str):
    """(mask path, label value) of a case for one prompt."""
    paths = case.target_paths or {}
    labels = case.target_labels or {}
    if prompt in paths:
        return paths[prompt], labels.get(prompt)
    if len(paths) == 1:                       # adapters that key by something else
        key = next(iter(paths))
        return paths[key], labels.get(key)
    raise KeyError(f"no target for prompt {prompt!r} in {paths}")


def image_info(img) -> dict:
    data = np.asarray(img.dataobj, dtype=np.float32)
    p1, p50, p99 = np.percentile(data, [1, 50, 99])
    return {"shape": "x".join(map(str, data.shape)),
            "voxel_size_mm": "x".join(f"{z:.4f}" for z in img.header.get_zooms()[:3]),
            "affine_is_identity": bool(np.allclose(img.affine, np.eye(4))),
            "intensity_min": float(data.min()), "intensity_p1": float(p1), "intensity_p50": float(p50),
            "intensity_p99": float(p99), "intensity_max": float(data.max())}, data


def best_slices(mask: np.ndarray) -> list[int]:
    """Index along each axis with the most foreground voxels."""
    return [int(np.argmax(mask.sum(axis=tuple(a for a in range(3) if a != ax)))) for ax in range(3)]


def extra_examples(args) -> None:
    """examples_extra.npz: a coronal slice through the tibial plateau of the same SKM-TEA
    example volume as examples.npz (first test case), so that the example figure can show
    all six structures (the sagittal slice shows only one compartment)."""
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    log(f"examples-only run, output folder: {out.resolve()}")
    sys.path.insert(0, str(Path.cwd()))
    from src.data.adapters import get_dataset_adapter
    adapter = get_dataset_adapter("skm_tea", args.skm_root)       # all six labels
    cases = adapter.cases()
    split_of = splits(cases, args.seed, args.train_fraction, args.val_fraction)
    case = next(c for c in cases if split_of[str(c.image_path)] == "test")
    mask_path = next(iter((case.target_paths or {}).values()))
    labels = adapter.LABEL_MAP
    img = np.asarray(nib.load(str(case.image_path)).dataobj, dtype=np.float32)
    lab = np.asarray(nib.load(str(mask_path)).dataobj).astype(np.int16)
    plateau = np.isin(lab, [labels["medial tibial cartilage"], labels["lateral tibial cartilage"],
                            labels["medial meniscus"], labels["lateral meniscus"]])
    ap = int(np.argmax(plateau.sum(axis=(0, 2))))               # arrays are (SI, AP, LR)
    np.savez_compressed(out / "examples_extra.npz", skm_case=case_id(Path(case.image_path)),
                        coronal_index=np.array(ap), skm_img_coronal=img[:, ap, :],
                        skm_lab_coronal=lab[:, ap, :])
    log(f"Done. {case_id(Path(case.image_path))}: coronal slice at AP index {ap} -> examples_extra.npz")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skm-root", default="/home/vault/iwi5/iwi5326h/projects/VoxTell/data/skm_tea/")
    parser.add_argument("--aeropath-root", default="/home/vault/iwi5/iwi5326h/projects/VoxTell/data/AeroPath/")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--train-fraction", type=float, default=0.7)
    parser.add_argument("--val-fraction", type=float, default=0.15)
    parser.add_argument("--out", required=True)
    parser.add_argument("--examples-only", action="store_true",
                        help="only write examples_extra.npz (extra slices for the example figure)")
    args = parser.parse_args()
    if args.examples_only:
        extra_examples(args)
        return

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    log(f"data_stats.py started, output folder: {out.resolve()}")

    sys.path.insert(0, str(Path.cwd()))
    from src.data.adapters import get_dataset_adapter   # the code's own adapters
    log("Imported the code's dataset adapters")
    meta = {"date": datetime.now().isoformat(timespec="seconds"), "host": platform.node(),
            "cwd": str(Path.cwd()), "args": vars(args), "split_sizes": {}}
    try:
        meta["code_commit"] = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                                             text=True, check=True).stdout.strip()
        meta["code_dirty"] = bool(subprocess.run(["git", "status", "--porcelain"], capture_output=True,
                                                 text=True).stdout.strip())
    except Exception as exc:                               # noqa: BLE001
        meta["code_commit"] = f"unavailable: {exc}"

    # ---------------- SKM-TEA ----------------
    # First collect (mask, label, split) of every task for every image, then read each
    # image and each mask file only once.
    per_image = {}                               # image path -> {task: (mask path, label, split)}
    for task in SKM_TASKS:
        adapter = get_dataset_adapter(task, args.skm_root)
        cases = adapter.cases()
        split_of = splits(cases, args.seed, args.train_fraction, args.val_fraction)
        meta["split_sizes"][task] = {s: sum(v == s for v in split_of.values()) for s in ("train", "val", "test")}
        for case in cases:
            mask_path, label = target(case, PROMPT[task])
            per_image.setdefault(Path(case.image_path), {})[task] = (Path(mask_path), label,
                                                                     split_of[str(case.image_path)])
        log(f"{task}: {len(cases)} cases, splits {meta['split_sizes'][task]}")

    rows, examples, example_case = [], {}, None
    for n, (img_path, tasks) in enumerate(sorted(per_image.items()), start=1):
        info, _ = image_info(nib.load(str(img_path)))
        masks = {}
        for task, (mask_path, label, split) in tasks.items():
            if mask_path not in masks:
                masks[mask_path] = np.asarray(nib.load(str(mask_path)).dataobj)
            mask = masks[mask_path]
            voxels = int((mask == label).sum()) if label is not None else int((mask > 0).sum())
            rows.append({"case_id": case_id(img_path), "task": task, "prompt": PROMPT[task],
                         "split": split, "label_value": label, "mask_file": mask_path.name,
                         "structure_voxels": voxels,
                         "all_label_values": " ".join(map(str, np.unique(mask).astype(int))), **info})
            if example_case is None and split == "test":
                example_case = (img_path, mask_path)
        if n % 10 == 0 or n == len(per_image):
            log(f"SKM-TEA volumes read: {n}/{len(per_image)}")
    with open(out / "skm_tea_volumes.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    img = np.asarray(nib.load(str(example_case[0])).dataobj, dtype=np.float32)
    lab = np.asarray(nib.load(str(example_case[1])).dataobj).astype(np.int16)
    idx = best_slices(lab > 0)
    examples["skm_case"] = case_id(example_case[0])
    examples["skm_index"] = np.array(idx)
    for ax in range(3):
        examples[f"skm_img_ax{ax}"] = np.take(img, idx[ax], axis=ax)
        examples[f"skm_lab_ax{ax}"] = np.take(lab, idx[ax], axis=ax)

    # ---------------- AeroPath ----------------
    adapter = get_dataset_adapter("aeropath", args.aeropath_root)
    cases = adapter.cases()
    split_of = splits(cases, args.seed, args.train_fraction, args.val_fraction)
    meta["split_sizes"]["aeropath"] = {s: sum(v == s for v in split_of.values()) for s in ("train", "val", "test")}
    log(f"aeropath: {len(cases)} cases, splits {meta['split_sizes']['aeropath']}")
    rows, aero_example = [], None
    for n, case in enumerate(cases, start=1):
        img = nib.as_closest_canonical(nib.load(str(case.image_path)))
        info, data = image_info(img)
        mask_path, label = target(case, "lung")
        raw = np.asarray(nib.as_closest_canonical(nib.load(str(mask_path))).dataobj)
        lung = raw > 0
        voxel_ml = float(np.prod(img.header.get_zooms()[:3])) / 1000.0
        rows.append({"case_id": case_id(Path(case.image_path)), "split": split_of[str(case.image_path)],
                     "lung_voxels": int(lung.sum()), "lung_volume_ml": float(lung.sum()) * voxel_ml,
                     "lung_label_values": " ".join(map(str, np.unique(raw).astype(int))), **info})
        if aero_example is None and split_of[str(case.image_path)] == "test":
            aero_example = (case_id(Path(case.image_path)), data, lung)
        if n % 5 == 0 or n == len(cases):
            log(f"AeroPath volumes read: {n}/{len(cases)}")
    with open(out / "aeropath_volumes.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    cid, data, lung = aero_example
    idx = best_slices(lung)
    examples["aero_case"] = cid
    examples["aero_index"] = np.array(idx)
    for ax in range(3):
        examples[f"aero_img_ax{ax}"] = np.take(data, idx[ax], axis=ax)
        examples[f"aero_lab_ax{ax}"] = np.take(lung, idx[ax], axis=ax).astype(np.int16)

    np.savez_compressed(out / "examples.npz", **examples)
    (out / "meta.json").write_text(json.dumps(meta, indent=2))
    log(f"Done. Wrote {sorted(p.name for p in out.iterdir())} to {out.resolve()}")


if __name__ == "__main__":
    main()
