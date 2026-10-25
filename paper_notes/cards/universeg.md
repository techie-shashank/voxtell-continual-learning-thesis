# UniverSeg — fact card (tier B)
| | |
|---|---|
| Paper | V. I. Butoi, J. J. Gonzalez Ortiz, T. Ma et al., "UniverSeg: Universal Medical Image Segmentation", arXiv:2304.06131v1 (12 Apr 2023); 35 pages (main paper pp. 1–9, supplement after references) |
| Bib key / Local PDF | universeg / papers/t2_few_shot/universeg.pdf |
| Version read | arXiv v1. The PDF states no venue; the bib entry gives ICCV 2023, pp. 21381–21394 (not checked against the publisher version) |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: segment new, unseen medical segmentation tasks (new anatomies, modalities, labels) without any retraining or fine-tuning, given a query image and a support set of labelled examples (Abstract; Sec. 1; Fig. 2).
- Data: MegaMedical, 53 open-access datasets, over 22,000 scans, 26 medical domains, 16 imaging modalities (Abstract; Sec. 4). All tasks are 2D binary: for 3D data the mid-slice along each major axis is used; multi-label datasets are split into binary tasks; images resized to 128 × 128 (Sec. 4). Plus 1000 synthetic tasks (SynthMorph-style shapes) (Sec. 4). Per-dataset splits 60/20/20 % (support/dev/test) (Sec. 5.1). Held-out test datasets: ACDC, SCD (heart), STARE (retinal vessels), PanDental (mandible), SpineWeb (vertebrae), WBC (white blood cells) (Sec. 5.1).
- Method (two sentences): a UNet-like fully convolutional network whose blocks are CrossBlocks, built on a cross-convolution that combines the query feature map with each support image–label pair and averages the results, so the network is invariant to support order and size (Sec. 3.1, Eq. 1–2, Fig. 3). Trained across many tasks with in-task augmentation, task augmentation and synthetic tasks; at inference predictions from K sampled support sets can be averaged (Sec. 3.2–3.3, Alg. 1).
- Setting: no text conditioning (task defined by visual support set); not continual learning; few-shot / in-context: support size N from 1 to 64, default training support size 64 (Sec. 5.1, 5.3). No weights are updated at test time.
- Evaluation: Dice score (0–100) on test splits of held-out datasets, 5 predictions per subject with random support sets, ensembled; subject bootstrapping (1000 repetitions) for std (Sec. 5.1). Baselines: few-shot methods SE-net, ALPNet, PANet; upper bound: 17 task-specific nnU-Nets (Sec. 5.1, Table 1).
- Best result (Table 1, p. 7): average held-out Dice 71.8 ± 0.9 (UniverSeg, 1.18 M parameters) vs SENet 50.1 ± 1.3, ALPNet 47.8 ± 1.1, PANet 41.8 ± 1.3; supervised nnU-Net upper bound 84.4 ± 1.0. Per-dataset improvement over the best baseline 7.3 to 34.9 Dice (Sec. 5.2). Training support size 1 → 16 raises held-out Dice from 53.7 to 69.9 (max 71 at 64) (Sec. 5.3, Fig. 7). More training tasks/diversity improves held-out Dice (Fig. 6); ablation: all augmentation strategies jointly 71.8 ± 0.9 (Table 2).
- Limitations stated by the authors: only 2D images and single (binary) labels; gap to the supervised upper bounds remains (Sec. 6 "Limitations").

## Check of the author's notes
- Not cited in thesis/related_work.tex or thesis/introduction.tex (no `\cite{universeg}` and no mention of "UniverSeg"); no row in the summary table. Nothing to check.

## Relevance (NOT from the paper)
Reference point for few-shot adaptation without gradient updates (in-context, support-set conditioning) as an alternative to the fine-tuning-based few-shot adaptation studied in this thesis; it is 2D and has no text prompts and no continual-learning component, and its support-size analysis parallels the thesis's study of the number of labelled volumes.
