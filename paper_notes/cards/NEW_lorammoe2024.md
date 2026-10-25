# Low-Rank MoE for continual medical segmentation — fact card (tier B)
| | |
|---|---|
| Paper | Q. Chen, L. Zhu, H. He, X. Zhang, S. Zeng, Q. Ren, Y. Lu, "Low-Rank Mixture-of-Experts for Continual Medical Image Segmentation", arXiv:2406.13583v1 (19 Jun 2024); 11 pages in LNCS format (main text pp. 1–9) |
| Bib key / Local PDF | NEW_lorammoe2024 (no bib entry yet) / papers/t5_cl_medseg_networks/NEW_lorammoe2024.pdf |
| Version read | arXiv v1; no venue stated in the PDF (LNCS layout, running head "Authors Suppressed Due to Excessive Length", i.e. a conference submission format). The appendix referred to in Sec. 3 is not in the downloaded file |
| Written | 2026-10-23, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: continual medical image segmentation without access to earlier data or labels, at task level (new datasets, cross-modal) and at class level (new organ classes); the authors argue that pseudo-label methods corrupt learned features and that architecture expansion is memory-costly (Abstract; Sec. 1).
- Data (Sec. 3.1): task level: ACDC (70/10/20 train/val/test), ISIC skin lesions (2,270/162/162 images), COVID-19 CT segmentation (100 axial CT images; split not stated). Class level: BTCV (30 labelled CT scans, 24 train / 6 test, MONAI split), then LiTS (131 contrast-enhanced CT; split following Zhang et al. [28]).
- Method (two sentences): a Transformer whose FFN and attention projections receive one LoRA expert (r = 8) per dataset; when a new dataset arrives, a new expert is added and trained while W0 and all earlier experts stay frozen, and the new expert's output is summed on top of the earlier frozen low-rank updates, which the authors also describe as using earlier LoRA weights as initial values (Sec. 2.1–2.2, Eq. 2–6; Sec. 3.3). Routing: at task level a "matching-based offline classifier" on CLIP image features (8 support images per dataset; reported accuracy 99.7 %) selects the expert by task number at test time; at class level a language-guided gate uses a CLIP text embedding of a dataset description listing its label names, with top-1 hard routing per token at test time (Sec. 2.2, Fig. 2–3).
- Setting: task-incremental with inferred task identity (task level, SETR backbone, 2D data) and class-incremental with two steps (class level, 3D Swin-UNETR "improved" in MONAI). The text is a fixed per-dataset description, not a free-text prompt per target (Sec. 2.2, p. 5). Pretraining source of W0 not stated in the main text. No few-shot setting.
- Evaluation: DSC (Sec. 3.2). Task level: DSC per dataset after each order; class level: mean DSC over 13 BTCV classes after step 1 and after step 2, plus DSC of the new liver-tumour class (val/test) (Sec. 3.2, following [28]). No explicit forgetting or transfer metric; no variance or number of runs reported. Baselines: single-task models, sequential training without low-rank/MoE, LwF, ILT, PLOP, CLAMTS (Zhang et al. 2023) (Tables 1–2).
- Best result, task level (Table 1, p. 8): with Low-Rank MoE (3.4M trainable parameters), ACDC stays at 92.08 in all four orders, e.g. ACDC→ISIC→COVID gives 92.08 / 90.77 / 74.17 vs single-task 92.08 / 90.61 / 73.27. Without low-rank MoE (88.1M), ACDC drops to 3.03 after ACDC→ISIC→COVID and to 39.08 after ACDC→COVID→ISIC. Text speaks of "eight distinct scenarios", but Table 1 lists four orders.
- Best result, class level (Table 2, p. 8): step 2 BTCV DSC 80.6 and LiTS tumour 53.5/46.7 (val/test) with 2.3M trainable parameters, vs CLAMTS 78.5 and 50.9/45.4, PLOP 78.0 and 41.2/36.6, LwF 76.2 and 49.9/43.1 (37.5M parameters each); step-1 BTCV 82.6 (single-task Swin-UNETR† 82.7).
- Limitations stated by the authors: none stated (the conclusion, Sec. 4, only summarises).
- Not stated: number of seeds, the separate effect of the routing error, results without task identity at task level.

## Where it fits in Ch. 2 (suggestion)
- Sec. "Segmentation Networks" (related_work.tex l. 83–85), in the architectural-isolation paragraph next to González et al. and Continual Segment, or as a medical counterpart of MoE-Adapters in the "Mixture-of-experts routing" paragraph (l. 64): it supports the claim that dedicated components are reached via task identity or a routing decision (l. 94).

## Relevance (NOT from the paper)
Closest medical analogue to task-specific LoRA in this thesis (one rank-8 LoRA per task, earlier ones frozen), but it relies on an image-based task classifier or a text gate over dataset descriptions, not free-text prompts, and is not few-shot. Its near-zero forgetting is by construction, as for task-specific LoRA here. Single-run results without variance; treat the comparisons as indicative.
