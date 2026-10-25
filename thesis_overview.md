# Thesis overview

One-page summary of the thesis as of 2026-10-19. Not thesis text. Numbers come from
`thesis/tables/cl_metrics.csv`, `thesis/tables/compute.csv` and `results/data_stats/`
(regenerate with `python scripts/run_all.py`); decisions and facts from `thesis_notes.md`.
Interpretation of the results is still open (author's task, Ch. 6 and 7).

## Thesis
- **Title:** Continual Learning for Promptable Universal 3D Medical Image Segmentation in Few-Shot Settings
- **Type:** Master's thesis in Computer Science, Pattern Recognition Lab (LME), FAU Erlangen-Nürnberg
- **Author:** Shashank Shashank. **Advisors:** Prof. Dr.-Ing. habil. Andreas Maier, Dr.-Ing. Tomás Arias Vergara
- **Period:** 15.04.2026 – 15.11.2026

## Research question
How do different continual-learning strategies trade off adaptation performance and catastrophic forgetting when adapting free-text promptable universal 3D medical image segmentation models under few-shot conditions?

**Objectives:** (1) a few-shot continual-learning evaluation protocol for free-text promptable 3D segmentation; (2) a comparison of continual-learning strategies under this protocol (adaptation and forgetting); (3) the influence of the amount of labelled training data; (4) the influence of further experimental factors through ablations.

**Contributions (provisional, to be finalised after the results analysis):** a systematic empirical evaluation of continual adaptation for free-text promptable 3D segmentation; a comparative analysis of adaptation, forgetting, transfer and retention under limited supervision; an investigation of factors such as the amount of labelled data, task order and adaptation configuration.

## Model
**VoxTell** (Rokuss et al., arXiv 2025; notes in `paper_notes/voxtell.md`): a free-text promptable universal 3D segmentation model. ResEncL UNet image encoder, frozen Qwen3-Embedding-4B text encoder, transformer prompt decoder, text–image fusion at every decoder scale. Trained on 158 public datasets (> 62,000 CT, MRI and PET volumes, 1,087 concepts). Its authors report poor zero-shot performance on knee MRI (SKM-TEA, mean Dice 10.72 %) and name few-shot adaptation as future work. Checkpoint used: `voxtell_v1.1`.

## Data (Ch. 4)
| | SKM-TEA | AeroPath |
|---|---|---|
| Role | six continual-learning tasks | control task (never trained on, except by replay) |
| Imaging | knee MRI, 3D qDESS, echo 1 | chest CT angiography |
| Volumes (patients) | 155 (155) | 27 (27) |
| Structures / text prompts | lateral and medial tibial cartilage, femoral cartilage, patellar cartilage, medial and lateral meniscus | lung |
| Split (train/val/test), seed 42 | 108 / 23 / 24 (own random split, not the official one) | 19 / 4 / 4 |

Few-shot settings: the first k = 5, 10 or 20 training volumes per task (nested, one subset per k); full data = 108.

## Strategies compared
| Strategy | Mechanism |
|---|---|
| Sequential fine-tuning | all parameters trained on each task in turn (baseline) |
| Task-specific LoRA (r = 4) | one LoRA adapter per task, chosen by the task identity at inference |
| Shared LoRA (r = 1024 in the main comparison) | one LoRA adapter for all tasks |
| Distillation-based (adapted from ZSCL) | all parameters trained + feature distillation from the pretrained model on current-task data (weight ensemble implemented but not evaluated) |
| Prompt tuning (adapted from CPE-CLIP) | learned prompt tokens + meta-net in the prompt decoder, pretrained weights frozen (per-task gradient scaling implemented but inactive) |
| Shared LoRA with replay | shared LoRA + replay memory (includes control-task volumes) |

Training: 6 tasks in sequence, 10 epochs per task, SGD, LR 1e-4, poly decay, 192³ patches, checkpoint with the lowest validation loss. One seed (42) per configuration.

## Metrics (Dice-based, computed from the evaluation matrix)
Adaptation (diagonal mean, the a_k,k term of Chaudhry's intransigence); Average Performance (ZSCL "Avg."); Final Performance (ZSCL "Last"); Final Forgetting (Chaudhry et al. 2018, Eq. 3); Transfer (ZSCL); control-task drop (absolute Dice drop on AeroPath from the pretrained model to the final checkpoint; follows SPU's control set). Variability: 95 % paired bootstrap intervals over test volumes (std ≈ 0.01 Dice in the main comparison).

## Results at a glance (Dice, test split)
**Main comparison** (full data, original task order)
| Strategy | Adaptation | Final Perf. | Final Forgetting | Transfer | Control-task drop |
|---|---|---|---|---|---|
| Seq. fine-tuning | 0.717 | 0.130 | 0.704 | 0.001 | 0.979 |
| Task-specific LoRA (r = 4) | 0.485 | 0.485 | 0.000 | 0.129 | 0.000 |
| Shared LoRA (r = 1024) | 0.471 | 0.233 | 0.289 | 0.174 | 0.237 |
| Prompt tuning | 0.608 | 0.135 | 0.568 | 0.043 | 0.979 |
| Distillation-based | 0.744 | 0.134 | 0.732 | 0.002 | 0.979 |
| *Pretrained model (reference)* | 0.114 | 0.114 | 0.000 | 0.137 | 0.000 |

Task-specific LoRA's 0 forgetting and 0 control-task drop follow from its design (task identity at inference; control task evaluated without an adapter).

**Shared-LoRA rank ablation** (Adaptation / Final Perf. / Final Forgetting / Control-task drop): r = 4: 0.607 / 0.152 / 0.546 / 0.978 · r = 32: 0.570 / 0.154 / 0.499 / 0.978 · r = 128: 0.524 / 0.204 / 0.384 / 0.958 · r = 256: 0.503 / 0.222 / 0.337 / 0.832 · r = 512: 0.488 / 0.230 / 0.309 / 0.574 · r = 1024: 0.471 / 0.233 / 0.289 / 0.237 · r = 2048: 0.462 / 0.233 / 0.284 / 0.091.

**Task order** (original → reverse; Adaptation, Final Perf., Final Forgetting): Seq. fine-tuning 0.717 → 0.745, 0.130 → 0.132, 0.704 → 0.736 · Task-specific LoRA 0.485 → 0.478, 0.485 → 0.478, 0.000 → 0.002 · Shared LoRA (r = 1024) 0.471 → 0.439, 0.233 → 0.345, 0.289 → 0.124.

**Few-shot** (Adaptation at k = 5 / 10 / 20 / 108): Seq. fine-tuning 0.530 / 0.612 / 0.598 / 0.717 · Task-specific LoRA 0.114 / 0.115 / 0.116 / 0.485 · Shared LoRA 0.115 / 0.116 / 0.140 / 0.471. The task-specific and shared LoRA runs with 5–20 volumes stay close to the pretrained-model reference (0.114) on every metric.

**Replay** (shared LoRA r = 1024, without → with replay fraction 0.1): Adaptation 0.471 → 0.429, Final Perf. 0.233 → 0.446, Final Forgetting 0.289 → 0.039, control-task drop 0.237 → 0.007 (the control task is part of the replay memory).

**Compute** (A100 40 GB, per run): trainable parameters 0.20 M (task-specific LoRA r = 4) to 440 M (sequential fine-tuning, ZSCL-based); about 18–36 min per epoch with full data (3–6 min with 5–20 volumes, mostly validation); peak GPU memory 20–38 GiB.

## Main limitations (see `thesis_notes.md` §3)
One seed per configuration; one training subset per k; no joint-training upper bound; distillation-based and prompt-tuning strategies only in the main comparison; control task with 4 test volumes; SKM-TEA processed with an identity affine (no physical voxel size, no resampling); own random split (results not comparable with SKM-TEA benchmarks); task-specific LoRA requires the task identity.

## Status of the chapters
| Ch. | Chapter | Status |
|---|---|---|
| 1 | Introduction | early draft, diagnosed (`reviews/ch1_ch2_diagnosis.md`), revision after the results |
| 2 | State of the Art | early draft, diagnosed, revision after the results |
| 3 | Theoretical Background | to do (week 3) |
| 4 | Data Description | full draft, author rewrite in progress |
| 5 | Method | next (new session) |
| 6 | Experiment & Results | tables and figures ready; text in week 2 |
| 7 | Discussion | week 3 |
| 8 | Summary | week 4 |
