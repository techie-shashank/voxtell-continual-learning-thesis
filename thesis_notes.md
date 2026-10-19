# Thesis notes: decisions, verified facts, limitations

Working record for writing the thesis. Every fact has a source (file or log). Not thesis text.
Update this file when a decision is made or a fact is verified; delete entries that turn out wrong.

## 0. Status and next steps (update at the end of every session)

As of 2026-10-19 (submission 2026-11-15):
- **Done:** results pipeline (`scripts/run_all.py`, `scripts/plot_data.py`; tables in `thesis/tables/`, figures in `thesis/figures/`); Ch. 4 Data Description fully drafted (`% CLAUDE-DRAFT`); VoxTell paper notes (`paper_notes/voxtell.md`); bib duplicates removed.
- **Author, now:** rewrite Ch. 4 in own words (content, not polish), then ask for the section review.
- **Claude, next:** Ch. 5 Method — fact sheet from `code/` (fine-tuning setup, each strategy incl. LoRA target modules, replay, ZSCL-based, CPE-CLIP-based; loss, optimiser, patch sampling, checkpoint selection, sliding-window inference, metric formulas), complexity + measured runtime/memory (`thesis/tables/compute.csv`), preamble setup (`algorithm`/`algorithmic`, bold `\vec`/`\mat`), notation proposal, outline + interview questions. No prose before the outline is approved.
- **Workflow (confirmed by the author 2026-10-19):** one-chapter lag — Claude prepares/drafts chapter N+1 while the author rewrites chapter N; section review right after each rewrite; chapter review when a chapter is complete; line-by-line language polish only in the final review. One new Claude session per chapter.
- **Open with the supervisor:** separate Method chapter? AI-use statement?

## 1. Decisions (made by the author)

| Date | Decision | Reason / source |
|---|---|---|
| 2026-10-18 | Metrics: Adaptation, Average Performance, Final Performance, Final Forgetting, Transfer, control-task drop | Discussion in session; implemented in `scripts/compute_cl_metrics.py` |
| 2026-10-18 | Final Forgetting = Chaudhry et al. 2018, Eq. 3, unchanged (max over all earlier stages) | Same form in `yu2026recentadvancesmultimodalcontinual`; restricting the max changes only TIL-LoRA, by at most 0.0016 |
| 2026-10-18 | Adaptation = mean of the diagonal a_{i,i}; described as the a_{k,k} term of Chaudhry's intransigence measure, without the joint-training reference | No joint-training run exists; "learning accuracy" label not confirmed in the literature |
| 2026-10-18 | Average Performance, Final Performance, Transfer as in ZSCL (Avg., Last, Transfer) | `zheng2023preventingzeroshottransferdegradation` |
| 2026-10-18 | Control task (AeroPath, prompt "lung"), control-task drop = absolute Dice drop pretrained → final checkpoint; follows SPU's control set | `Zhang_2024_CVPR`; chosen because the pretrained model performs well on it (0.979 Dice) and it is public |
| 2026-10-18 | Results tables get a "Pretrained model" reference row per task order | Shows whether a run moved away from the pretrained model at all |
| 2026-10-18 | `results/hpc/experiments/` is the single source of truth; `results/experiment_index.csv` maps runs; the xlsx is not a source | Session decision |
| 2026-10-18 | Strategy names: sequential fine-tuning (baseline), task-specific LoRA, shared LoRA, shared LoRA with replay, ZSCL-based, CPE-CLIP-based; "task-aware inference" for task-specific LoRA; TIL/CIL only for related work (full list in CLAUDE.md terminology) | "CIL" means the model must infer the class/task itself, but the text prompt names the target in every strategy here; names describe the mechanism instead. "-based" marks this thesis's variants (C-2.5, C-2.6, C-2.8 in `reviews/ch1_ch2_diagnosis.md`). Sequential fine-tuning is not a "lower bound": it has the highest Adaptation |
| 2026-10-18 | Not reported: shared LoRA r = 256 reverse, shared LoRA r = 128 + replay, task-specific LoRA r = 8 (no role in the index) | Author decision |
| 2026-10-19 | No Zotero: `thesis/literature.bib` is maintained by hand; Claude edits it only on request (rules in CLAUDE.md). Removed 5 exact duplicate entries; Colab tutorial entry is now `skmtea_tutorial` (@online, author Stanford MIMI Lab, title from the SKM-TEA README; no year given anywhere) | Author request |
| 2026-10-19 | Figures stay vector PDF (charts sharp in print, real text in the thesis font, small files); image slices are embedded as raster inside the PDF. `\includegraphics` needs the `.pdf` extension (lmedoc.cls limits default extensions) | Author agreed to the recommendation |
| 2026-10-18 | Heatmap labels use abbreviations LT, MT, Fe, Pa, MM, LM, Ctrl (to be defined in the caption) | Author decision |
| 2026-10-18 | Variability = paired bootstrap over test volumes (B = 2000, seed 0; 24 SKM-TEA scans resampled jointly for all tasks and checkpoints, 4 AeroPath volumes separately); tables show point estimates, figures show 95% intervals, std and intervals in `cl_metrics.csv` | Only one seed per configuration; reflects test-volume sampling only, not training randomness |

## 2. Verified facts about the experiments

**Data and splits**
- SKM-TEA split 108/23/24 (train/val/test), seeded shuffle (seed 42), identical test set in every run. Source: "Train/Val/Test Split" lines in SLURM logs; test image paths in `eval.log`.
- AeroPath split 19/4/4; the control task is evaluated on the 4 test volumes only (AeroPath 1, 3, 6, 12). Source: `code/src/evaluation/test.py:69`, `eval.log`.
- VoxTell does not train on AeroPath: AeroPath is a held-out test set in the VoxTell paper, category "Healthy (Known Concept)", VoxTell lung Dice 96.99 on all 27 volumes (VoxTell Table 7, S-p. 7). Lung is heavily represented in VoxTell's training data (Table 10: lung 3427, left/right lung 4404 images). Source: `paper_notes/voxtell.md` §4, §7.
- Few-shot: `train_max_cases` = first k volumes of the seeded training split; one sample per k; the 5-volume set is contained in the 10- and 20-volume sets. 5-shot: MTR_038, 074, 097, 201, 225. Source: `code/src/data/adapters/base.py:71-72`, `[DATA]` lines in `run.log`.
- Prompts: one fixed prompt per structure, identical in training and evaluation (e.g. "femoral cartilage", "lung"); wording never varied. Source: `run.log`, `eval.log`, `per_prompt/prompts.json`.

**Datasets (from the dataset papers in `datasets/`)**
- SKM-TEA (`desai2021skmtea`): 155 patients, Stanford Healthcare, knee MRI with the 3D qDESS sequence on two 3T GE MR750 scanners; patient consent and Stanford IRB approval (Sec. 3). Acquisition: matrix 416×512, in-plane resolution 0.38×0.31 mm², TE 5.7/30.1 ms (echo 1/2), TR 17.9 ms, flip angle 20°, 80–88 slices (Table 5, App. A.1). Slice thickness is not stated in the paper.
- SKM-TEA labels: manual segmentation of patellar, femoral, lateral/medial tibial cartilage and lateral/medial meniscus on all DICOM images (Sec. 3); two researchers (3–4 years of knee MRI experience) supervised by two musculoskeletal radiologists; one annotator per scan; sagittal slice-by-slice in ITK-SNAP (App. A.4).
- SKM-TEA official split: 86/33/36 (train/val/test); the 36 test patients had additional arthroscopic surgery (Sec. 3). **This thesis does not use it**: it re-splits all 155 scans randomly 108/23/24 (`code/src/data/datamodule.py:53-66`).
- SKM-TEA licence: Stanford University School of Medicine terms plus the LERA dataset terms (App. A.5). Access: github.com/StanfordMIMI/skm-tea; the data was downloaded from Redivis (`aimi` / `skm_tea:5r8z:v1_0`, table `image_files`; `code/scripts/redvis_data_download.py`).
- AeroPath (`støverud2023aeropathairwaysegmentationbenchmark`): 27 contrast CT (CTA) scans, Thorax Lung protocol, St. Olavs hospital, Trondheim; patients 52–84 years (median 70), nine women, all undergoing diagnostic tests for lung cancer, pathologies incl. malignant tumours, sarcoidosis, emphysema; size [487–512]×[441–512]×[241–829] voxels, in-plane 0.68–0.76 mm, slice thickness 0.5–1.25 mm; ethics approval REK Sør-Øst A 2010/3385a, written consent; openly available at github.com/raidionics/AeroPath. The paper describes how the **airway** labels were made; it does not describe the **lung** labels that this thesis uses. Neither do the GitHub README nor the Zenodo record (checked 2026-10-19).
- AeroPath data licence: Creative Commons Attribution 4.0 International; Zenodo record 10069289, DOI 10.5281/zenodo.10069289, v1, published 2023-11-03 (zenodo.org/records/10069289, read 2026-10-19). The repository code is MIT-licensed (README).

**From the data (`results/data_stats/`, HPC run 2026-10-19, code commit 50a654b, dirty; official annotation files v1.0.0)** — tables/figures by `scripts/plot_data.py`
- Splits recomputed with the code's adapters: SKM-TEA 108/23/24 for all six tasks, AeroPath 19/4/4; test split identical to the evaluation logs.
- SKM-TEA: 155 scans = 155 patients (`subject_id`), one timepoint each, so no patient appears in two splits. Voxel spacing 0.3125 × 0.3125 × 0.8 mm for all scans; matrix 512 × 512 × 160 (151 scans), 144/152/156/168 slices (one each). Orientation stored as (SI, AP, LR) for 137 scans and (SI, AP, RL) for 18; the identity affine drops this, so the 18 reach the model mirrored along the left–right array axis. Two echoes per scan.
- SKM-TEA pathology (official bounding boxes): 130 of 155 scans have ≥ 1 label — cartilage lesion 99, effusion 88, meniscal tear 68, ligament tear 36 scans.
- This thesis's split vs the official split: training 63/22/23 (official train/val/test), validation 10/7/6, test 13/4/7. So 7 of the 24 test scans come from the official (arthroscopy) test set.
- Structure volumes, median [IQR] cm³: lateral tibial 2.32 [1.82, 2.96], medial tibial 2.13 [1.75, 2.56], femoral 10.99 [8.73, 13.50], patellar 3.14 [2.35, 3.77], medial meniscus 2.20 [1.81, 2.69], lateral meniscus 1.90 [1.50, 2.37]; AeroPath lung 4,858 [3,732, 6,231] cm³.
- AeroPath in the data: in-plane 0.56–0.82 mm, slice 0.50–1.25 mm, up to 843 slices. This is wider than the paper's stated ranges (0.68–0.76 mm, 241–829 slices). Report the data values.

**Author's answers on the data (2026-10-19)**
- Why SKM-TEA: the VoxTell paper reports poor VoxTell performance on SKM-TEA; knee MRI is a rare region not covered by VoxTell's training. **Verified in the paper** (`paper_notes/voxtell.md` §7–8): Table 9 (S-p. 10), VoxTell zero-shot mean Dice 10.72% on SKM-TEA (femoral cartilage 46.45, medial tibial 14.78, lateral tibial 2.97, others ≤ 0.07); Limitations p. 8 name the knee as sparsely represented and suggest "few-shot adaptation with minimal labeled examples" as future work. **Caveat**: VoxTell's training data does contain knee cartilage labels (SKI10, Lower Extremity Muscles; Table 10: femoral, patellar, medial/lateral tibial cartilage) but no meniscus, so write "rarely seen", not "never seen".
- Identity affine: the author checked alignment of labels and images visually in ITK-SNAP.
- Why the random split (author, corrected 2026-10-19): a deliberate choice. (1) Every strategy, task and run uses the same split, so the strategy comparison is fair; the thesis never compares numbers with SKM-TEA benchmarks, which is what the official split is for. (2) The official test set contains only the 36 patients with arthroscopic surgery, a selected subgroup; a random split keeps training and test volumes from the same distribution, so adaptation and forgetting are not mixed with a train–test shift. Limitation to state: results are not comparable with SKM-TEA benchmark numbers. Do not write that the random split was "easier" or that the official split was found later.
- Echo 1 only: follows the segmentation part of the SKM-TEA authors' Colab tutorial (colab.research.google.com/drive/1PluqK77pobD5dXE7zzBLEAeBgaaeGKXa).
- Identity affine: deliberate, intended to keep labels and images aligned. True slice thickness unknown to the author.
- Licences: the author signed the Stanford AIMI research-use agreement for SKM-TEA.
- No scans were excluded (all 155 SKM-TEA, all 27 AeroPath).

**Data pipeline (from `code/`)**
- SKM-TEA conversion (`code/scripts/h5_to_nifti.py`): image = HDF5 key `echo1` (echo 1 only), labels = argmax of the one-hot `seg` + 1, background 0; saved with an **identity affine**, so the NIfTI files carry no voxel size (treated as 1 mm isotropic) and no orientation.
- SKM-TEA adapter (`code/src/data/adapters/skm_tea.py`, pulled from the HPC 2026-10-19): label map 1 patellar, 2 femoral, 3 medial tibial, 4 lateral tibial cartilage, 5 medial, 6 lateral meniscus; each task adapter keeps one label. This matches the channel order of `seg` in the official SKM-TEA DATASET.md (1 Patellar Cartilage, 2 Femoral Cartilage, 3 Tibial Cartilage – Medial, 4 – Lateral, 5 Meniscus – Medial, 6 – Lateral) together with `argmax + 1` in `h5_to_nifti.py`, so every text prompt names the right structure. Source: github.com/StanfordMIMI/skm-tea DATASET.md (read 2026-10-19).
- SKM-TEA files used: `image_files/` = "Data related to the DICOM track in HDF5 format" (DATASET.md), i.e. scanner DICOM images and DICOM segmentations, not SENSE reconstructions. Keys `echo1`, `echo2`, `seg` (one-hot, 6 classes).
- SKM-TEA voxel spacing and orientation are stored per scan in the annotation JSON files (`annotations/<version>/{train,val,test}.json`, fields `voxel_spacing`, `orientation`; example in DATASET.md: [0.3125, 0.3125, 0.8] mm). These files were not downloaded and the spacing is not used anywhere in the pipeline.
- Preprocessing (`code/src/data/preprocess.py`, `dataset.py`): reading with nnU-Net's `NibabelIOWithReorient`, crop to the non-zero bounding box, per-volume z-score normalisation (nnU-Net `ZScoreNormalization`), **no resampling**. Training uses 192³ patches, 85% centred on foreground (`dataset.py`).
- Evaluation (`code/src/inference/`): sliding window with 192³ patches, 50% overlap, Gaussian weighting; sigmoid, threshold 0.5.

**Training and evaluation**
- All runs: seed 42, one run per configuration; no repeated seeds.
- Checkpoint evaluated = lowest validation loss (`best_model.pt`). Source: `code/src/continual/evaluator.py:72`, `run.log`.
- Pretrained model: `models/voxtell_v1.1`, `fold_0/checkpoint_final.pth`; text encoder Qwen/Qwen3-Embedding-4B (code default, not overridden). Source: `code/src/model/builder.py:67`, `code/src/engine/model_engine.py:21`.
- Evaluation matrix entry = mean Dice over the test volumes of one task at one checkpoint. Source: `evaluator.py`, `eval_*.json`.
- Per-volume Dice recovered for all 1343 cells; every cell's mean reproduces `eval_matrix.csv` to 1e-5; every SKM-TEA cell has the same 24 scans, every AeroPath cell the same 4. Source: `scripts/extract_per_volume.py`, `thesis/tables/per_volume_dice.csv`.
- Bootstrap std of the main-comparison metrics is about 0.01 Dice or less. Source: `thesis/tables/cl_metrics.csv`.
- Few-shot epochs are short (about 3-6 min) because validation on 23 volumes dominates; epoch time includes validation. Source: `thesis/tables/compute.csv`.
- Fine-tuning job wall-clock (27.0 h) includes a first job that hit the 24 h limit and a re-evaluation job. Source: SLURM logs `voxtell_1779284.out`, `voxtell_1784581.out`.

**Strategies (behaviour fixed by the code)**
- TIL-LoRA evaluates each earlier task with that task's own adapter, so its forgetting is ~0 by design, and evaluates the control task with the plain pretrained model (no adapter), so its control-task drop is 0 by design. Source: `code/src/continual/strategies/lora/task_specific/strategy.py:49-56`; confirmed in `eval.log` model-load lines.
- TIL-LoRA (r = 4, original order) never learned Patellar: Dice 0.0000 right after training on it. Source: `eval_matrix.csv` of `exp_20260816_155157_668e608d`.
- ZSCL here is ZSCL-style: distillation on the current task's own batches plus weight ensembling; no separate reference dataset (the original uses one). Source: `code/src/continual/strategies/zscl/strategy.py`.
- Replay memory is initialised with about 10% of the AeroPath training split (2 volumes), plus 10% of each finished task, so in replay runs the control task is trained on; replayed AeroPath volumes (11, 25; 5, 7 after a job resume) are disjoint from its test volumes. Source: `code/src/continual/strategies/base.py:136-165`, `run.log`.
- Replay sampling is unseeded across job resumes: the replayed AeroPath volumes changed after the resume of `exp_20261014_120720_abe47a15`. Source: `run.log`.

**Compute (sources for the Method/Experiments chapter)**
- Hardware: NVIDIA A100-SXM4-40GB, cluster "tinygpu", partition a100. Source: SLURM logs.
- Per-job elapsed time, peak GPU memory: SLURM log footer. Per-epoch and per-task time: `run.log` timestamps. Inference time: `eval.log` timestamps.
- Trainable parameters: "Model parameters" lines in SLURM logs (full model 440,029,541; CIL-LoRA r = 1024: 50,331,648; TIL-LoRA r = 4: 196,608; CPE-CLIP: 12,599,296).

**Code version**
- No git commit was logged per run, and runs used uncommitted code (e.g. replay code committed 2026-08-22, replay run started 2026-08-16). Behaviour can be checked from the logs (model-load lines, `[DATA]` lines). Source: `git -C code log`.

## 3. Limitations and threats to validity (to discuss)

- One seed per configuration; variability can only be reported across the 24 test volumes, not across runs.
- One support set per few-shot setting; no variability across support-set samples.
- No joint-training upper bound; no intransigence measure.
- ZSCL and CPE-CLIP: no reverse-order or few-shot runs. TIL-LoRA rank ablation only r = 4 and r = 8 on 6 tasks.
- Control task: one dataset, one large high-contrast structure, 4 test volumes.
- TIL-LoRA needs the task identity at inference; its 0 forgetting and 0 control-task drop follow from that.
- Replay runs train on the control task, so their control-task drop is not comparable with the other strategies.
- ZSCL implementation differs from the original (no reference dataset).
- Code version per run not recorded.
- SKM-TEA: own random split instead of the official 86/33/36 split (the official test patients are mixed into all three splits); results are not comparable with SKM-TEA benchmark numbers.
- SKM-TEA NIfTI files have an identity affine: anisotropic voxels are treated as 1 mm isotropic, and no resampling is done. AeroPath keeps its real voxel size. The two datasets therefore reach the model at different physical scales.
- Echo 1 only; the second qDESS echo (used by the annotators) is not given to the model.
- Each SKM-TEA scan was labelled by one annotator; no inter-rater information.
- Lung labels of AeroPath: origin not documented in the paper (manual or automatic?).

## 4. Open questions

- Supervisor: separate Method chapter? "Use of AI tools" statement in the front matter?
- Ch. 4 outline approved 2026-10-19 (overview; SKM-TEA; AeroPath; splits and few-shot subsets; preprocessing; data quality and limitations).
- Ch. 4 still open: VoxTell's target spacing / resampling (not stated in the paper; check the official VoxTell code if needed); SKM-TEA annotation JSONs (spacing, orientation, official split; author will add them); lung-label origin (ask the AeroPath authors or state as unknown); Colab tutorial as an `@online` bib entry; which split argument(s) to use (options given 2026-10-19).
- Contributions are provisional until the results analysis.
- The 6 older 5-task tables (hidden xlsx sheet) have no experiment folder: drop them from the thesis?
