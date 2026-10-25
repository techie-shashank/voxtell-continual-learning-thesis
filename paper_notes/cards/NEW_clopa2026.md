# CLoPA (continual low-parameter adaptation of nnInteractive) — fact card (tier B)
| | |
|---|---|
| Paper | P. Esmaeili, C. Tangwiriyasakul, E. Gibson, S. Ourselin, M. J. Cardoso, "CLoPA: Continual Low-Parameter Adaptation of Interactive Segmentation for Medical Image Annotation", arXiv:2603.06426v1 (6 Mar 2026); 8 pages main text + references (LNCS format) |
| Bib key / Local PDF | NEW_clopa2026 (no bib entry yet) / papers/t6_cl_medseg_foundation/NEW_clopa2026.pdf |
| Version read | arXiv v1; no peer-reviewed venue stated in the PDF |
| Written | 2026-10-23, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: online adaptation of a zero-shot 3D interactive segmentation model during an annotation campaign, using the growing cache of annotated volumes of one task, to reach expert (nnU-Net) level with click prompts (Abstract; Sec. 1, pp. 1–2).
- Model and prompts: nnInteractive (3D, CNN U-Net) with click prompts only: one foreground and one background point per interaction step, sampled from false-negative regions; evaluation = interactive initialisation plus 100 editing steps (Sec. 2.1, p. 4; Sec. 3 "Prompting", p. 4). No text prompts.
- Setting: "continual" means repeated training episodes on one fixed binary task as annotations accumulate, with full memory replay of the cache (Sec. 2, p. 3). Episodes are triggered when the cache holds at least 25 % of the dataset (k_D = 0.25) and at least 5 unassigned samples (k_M = 0.2) (p. 3). There is no sequence of different tasks: each of the 8 tasks is adapted separately from the base model.
- Adapted parameters (Sec. 2.1, p. 3): all pretrained weights frozen except (1) CLoPA-I.N: instance-normalisation affine scale and bias (< 0.01 % of the model); (2) CLoPA-C.N: all instance-normalisation parameters plus the convolution kernels of the first encoder stage and last decoder stage. No new parameters, inference pipeline unchanged.
- Training (p. 4): 192³ patches, Dice + cross-entropy averaged over N = 5 simulated interaction steps (Eq. 1), batch size 2, Adam, lr 1e-3, 10 epochs × 50 updates per episode.
- Data and evaluation (Sec. 3, Table 1, pp. 4–5): 8 binary MSD tasks (hippocampus N = 130, brain tumour core 240, pancreas 140, liver 65, prostate 16, lung lesion 31, hepatic vessels 151, colon cancer 63; post-split sizes), 50/50 train/holdout split. Metrics: Dice and NSD at initialisation and iteration 100, nAUC, nNoI (interactions to expert level), NoF (% samples failing), and trajectory AUCs over dataset size; Wilcoxon / McNemar tests at α = 0.05; 3 training-stream permutations × 3 inference runs (p. 5).
- Forgetting: not measured. No evaluation on other tasks or on the pretrained model's zero-shot ability after adaptation; the low parameter count is argued to make forgetting risk "minimal" (p. 3), without an experiment.
- Results (Table 2, p. 6, final episode, iteration-100 Dice): hepatic vessels nnInteractive 0.165 → CLoPA-I.N 0.698 / C.N 0.692; hippocampus 0.805 → 0.903 / 0.911; brain tumour 0.753 → 0.815 / 0.811; liver initialisation Dice 0.373 → 0.912 (I.N). Most gain comes after the first training episode, then plateaus (Sec. 4, pp. 7–8; Fig. 2). I.N generally better than C.N on the tasks where the base model already converges (p. 6).
- Limitations stated by the authors (pp. 7–8): instance-normalisation and shallow-kernel tuning saturate on complex geometries (hepatic vessels NoF 11.8 %); deeper representation tuning likely needed; short training interaction window (N = 5) may limit the signal.

## Where it fits in Ch. 2 (suggestion)
Section on adapting promptable 3D foundation models with few parameters: shows parameter-efficient, few-sample task adaptation of a spatially promptable 3D model, but per task in isolation, without a task sequence or forgetting measurement.

## Relevance (NOT from the paper)
Does not contradict the gap claim: spatial (click) prompts, not free-text; single-task adaptation, not a multi-task sequence; no forgetting or control-task measure. Its "continual" is data-incremental within one task.
