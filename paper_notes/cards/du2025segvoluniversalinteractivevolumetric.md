# SegVol — fact card (tier B)
| | |
|---|---|
| Paper | Y. Du, F. Bai, T. Huang, B. Zhao, "SegVol: Universal and Interactive Volumetric Medical Image Segmentation", arXiv:2311.13385v5 (12 Feb 2025); 38 pages (main text pp. 1–10, appendix after references) |
| Bib key / Local PDF | du2025segvoluniversalinteractivevolumetric / papers/t1_text_promptable/du2025segvoluniversalinteractivevolumetric.pdf |
| Version read | arXiv v5; p. 1 footer: 38th Conference on Neural Information Processing Systems (NeurIPS 2024). Bib entry is the arXiv @misc although a peer-reviewed version is stated |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: a 3D foundation model for universal and interactive volumetric CT segmentation of many anatomical categories with easy prompting and efficient full-volume inference (Abstract; Sec. 1).
- Data (Abstract; Sec. 2.1, 3.1): self-supervised pre-training on 96K CT volumes (abstract: 90K unlabelled + 6K labelled); supervised fine-tuning on 25 public CT segmentation datasets (about 6K CTs, 150K masks, over 200 categories), with FH-algorithm pseudo-masks for unlabelled structures; 20 % of each dataset held out. External test sets: AMOS22 validation (120 cases, 15 organs), ULS23 (DeepLesion3D, Radboudumc Bone 744, Pancreas 124 lesion cases), SegTHOR (40 cases, 4 organs); 1,778 test cases in total (Sec. 3.2, p. 6–7). CT only, 3D.
- Method (two sentences): SAM-like design with a 3D ViT image encoder (12 layers, SimMIM pre-trained), a frozen CLIP text encoder fed with the template "A computerized tomography of a [text prompt]", a point/box prompt encoder and a mask decoder with an extra text branch (Sec. 2.2). Inference uses a zoom-out-zoom-in scheme: coarse prediction on the resized volume, then sliding-window refinement inside the region of interest (Sec. 2.4, Table 3).
- Setting: text conditioning by category names (word or phrase, e.g. "liver", "cervical spine C2") in a fixed template, plus point and box prompts and their combinations; no continual learning; no few-shot (Sec. 2.2–2.3).
- Evaluation: median Dice per category; baselines SAM (points, box), SAM-Med2D, SAM-Med3D, MedSAM (Table 2); task-specific nnU-Net, SwinUNETR, 3DUX-NET only in the appendix (Sec. 3.2). Hardware: 8 × A100-40GB; pre-training about 20 × 8 GPU hours, fine-tuning about 300 × 8 GPU hours (Sec. 3.1).
- Best result (Table 2, p. 6): average Dice (bbox + text) AMOS22 0.8593 vs 0.6668 SAM-Med2D; SegTHOR 0.8155 vs 0.7727 SAM-Med3D; ULS23 0.7046, equal to MedSAM 0.7046. Best in 19 of 22 tasks, up to 37.24 % over the runner-up (Abstract). Zoom-out-zoom-in Dice 0.7298 at 190 ms vs sliding window 0.6529 at 3331 ms (Table 3). Bbox+text +5.85 % over text alone; point+text +4.62 % over point alone (Sec. 3.3).
- Limitations stated by the authors: gap to referring (sentence-level) volumetric segmentation remains; CT-only training (MRI generalisation shown only in the appendix) (Sec. 4).

## Check of the author's notes
- introduction.tex:13 "Early approaches to promptable universal segmentation models relied primarily on visual interaction mechanisms, requiring users to provide spatial prompts, such as points or bounding boxes" (cites Ma_2024, du2025segvol..., cheng2023sammed2d) → partly wrong for SegVol: it supports text prompts (category names via CLIP) as well as points and boxes, and its headline results use bbox + text (Sec. 2.2; Table 2). It is not a spatial-prompt-only model.
- related_work.tex: not cited (no row in the summary table).

## Relevance (NOT from the paper)
A 3D CT model that already combines short text prompts (category names) with spatial prompts; in a review it sits between interactive SAM-style models and text-promptable universal models, and shows that text alone is weaker than text plus a box.
