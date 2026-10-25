# CLIP-LoRA — fact card (tier B)
| | |
|---|---|
| Paper | M. Zanella, I. Ben Ayed, "Low-Rank Few-Shot Adaptation of Vision-Language Models", arXiv:2405.18541v2 (1 Jun 2024); main text pp. 1–8, appendix tables after the references |
| Bib key / Local PDF | zanella2024lowrankfewshotadaptationvisionlanguage / papers/t2_few_shot/zanella2024lowrankfewshotadaptationvisionlanguage.pdf |
| Version read | arXiv v2; no peer-reviewed venue stated in the PDF |
| Written | 2026-10-23, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: few-shot adaptation of CLIP for image classification; the authors argue that prompt-tuning and adapter methods are costly to train or need per-dataset hyperparameter searches, and propose LoRA as a simple baseline (Abstract; Sec. 1, p. 1–2).
- Data (Sec. 5, p. 5): 11 2D natural-image classification datasets (ImageNet, SUN397, FGVC Aircraft, EuroSAT, Stanford Cars, Food101, Oxford Pets, Flowers102, Caltech101, DTD, UCF101), following the CoOp protocol; 1, 2, 4, 8, 16 shots per class (Table 2; Appendix). Number of images, classes and test splits are not restated in the paper (taken from the CoOp setting). Not medical, not segmentation.
- Method (two sentences): LoRA modules (rank r = 2, dropout 0.25 on the module input) are added to the query, key and value matrices of every layer of both the vision and the text encoder of CLIP and trained with cross-entropy on the support set (Sec. 4, Eq. 6, p. 5). Same hyperparameters for all datasets and shot numbers: learning rate 2 × 10⁻⁴, cosine schedule, batch size 32, 500 × (shots per class) iterations, fixed text template "a photo of a [class]" (Sec. 4, p. 5).
- Setting: text conditioning by a fixed class-name template (closed set of class names per dataset); no continual learning (each dataset adapted separately from the same pretrained CLIP); few-shot with k = 1, 2, 4, 8, 16 shots per class; results averaged over 3 random seeds (Table 2 caption).
- Evaluation: top-1 accuracy averaged over 3 seeds (Table 2). Baselines: zero-shot CLIP; prompt-based CoOp (4 and 16 tokens), CoCoOp, PLOT++, KgCoOp, MaPLe, ProGrad; adapter-based Tip-Adapter-F, CLIP-Adapter, TaskRes (Sec. 5). Backbones ViT-B/16 (main), ViT-B/32, ViT-L/14 (Fig. 2; Appendix Tables). Training time on 16-shot ImageNet, single A100 80 GB: CLIP-LoRA 50 min vs CoOp (16) 2 h, ProGrad 3 h 20, PLOT++ 15 h 30 (Table 1, p. 4).
- Best result (Table 2, p. 6, ViT-B/16, mean over 11 datasets): 1 shot 72.5 % vs best competitor Tip-Adapter-F 70.9 % (zero-shot CLIP 65.1 %); 4 shots 77.4 % vs PLOT++ 76.9 %; 16 shots 83.0 % vs PLOT++ 82.1 %. Worse than several baselines on Food101 and Oxford Pets (Sec. 5, p. 6). No standard deviations or significance tests reported. Ablation (Fig. 3, 4 shots, ImageNet / Stanford Cars / EuroSAT): adapting both encoders best on average (EuroSAT slight exception, vision only); W_v or W_o the best single matrices; more matrices or higher rank can reduce accuracy (ImageNet, Cars); LoRA in all layers preferred over upper or lower half (Sec. 6, p. 7).
- Limitations stated by the authors: underperforms on Food101 and Oxford Pets, possibly due to no regularisation beyond cross-entropy (Sec. 5, p. 6); choosing the adapted matrices and rank is "not trivial" (Sec. 7); results do not dismiss prompt-learning or adapter research (Abstract; Sec. 1).

## Check of the author's notes
- related_work.tex:60 "CLIP-LoRA inserts such modules into both encoders of CLIP" → correct (Sec. 4, p. 5: q, k, v of every layer in both encoders).
- related_work.tex:60 "and performed competitively across eleven few-shot image-classification datasets" → correct but understated: the paper reports the best average accuracy at every shot level in Table 2 (e.g. 72.5 vs 70.9 % at 1 shot), with losses on Food101 and Oxford Pets.
- related_work.tex:60 "with a single configuration for all datasets and shot levels" → correct (Sec. 4, p. 5; Sec. 5).
- related_work.tex:60 "indicating that the mechanism does not require per-dataset tuning to be effective" → partly correct: no per-dataset tuning was done, but the shared configuration (rank, matrices, placement) was chosen from ablations on ImageNet, Stanford Cars and EuroSAT (Sec. 6, Fig. 3), and the authors state that choosing matrices and rank is "not trivial" (Sec. 7). The inference is the author's, and it holds for classification with CLIP only.
- related_work.tex:60 "the updates are merged into the frozen weights after training and add no cost at inference" → correct (Sec. 2, p. 2; Fig. 1b; Sec. 5, p. 6).
- related_work.tex:178 (table) "Eleven datasets, 1--16 shots | Rank-2 LoRA in both encoders; not continual | $72.5\,\%$ (1-shot), $83.0\,\%$ (16-shot)" → correct (Table 2, ViT-B/16, average top-1 accuracy); the metric (top-1 accuracy) and backbone are not named in the cell.
- introduction.tex: not cited → not found.
- Additionally checked: method.tex:273 "LoRA has been applied to attention projections of vision--language models before, for instance in CLIP-LoRA" → correct (Sec. 4).

## Relevance (NOT from the paper)
Main evidence that low-rank adaptation of attention projections works with few labelled samples in a vision–language model; it supports the choice of LoRA strategies but says nothing about forgetting, segmentation or medical 3D data.
