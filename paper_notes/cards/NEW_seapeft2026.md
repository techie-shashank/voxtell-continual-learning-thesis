# SEA-PEFT (self-auditing PEFT for few-shot 3D segmentation) — fact card (tier B)
| | |
|---|---|
| Paper | S. T. Ly, H. V. Nguyen, "Self-Auditing Parameter-Efficient Fine-Tuning for Few-Shot 3D Medical Image Segmentation", arXiv:2603.05822v1 (6 Mar 2026); 8 pages main text + references (LNCS format) |
| Bib key / Local PDF | NEW_seapeft2026 (no bib entry yet) / papers/t2_few_shot/NEW_seapeft2026.pdf |
| Version read | arXiv v1; no peer-reviewed venue stated in the PDF |
| Written | 2026-10-23, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: adapting a pretrained 3D segmentation foundation model to a new site with few labelled scans, choosing the PEFT configuration (adapter type, placement, rank) automatically during training instead of by hand or by offline search (Abstract; Sec. 1, pp. 1–2).
- Method (two sentences): a library of candidate adapters on a frozen backbone is trained in a search–audit–allocate loop; each adapter's utility is its validation-Dice change when toggled off, divided by its parameter cost, smoothed by EMA and an IQR penalty, and a greedy knapsack picks the active set under a parameter budget, with a finite-state controller requiring 2–3 consistent votes before switching (Sec. 3.2, Eq. 5–6, 9). The final configuration is re-initialised and fine-tuned from scratch (p. 5).
- Audit space (Sec. 4, pp. 5–6): LoRA r ∈ {2, 4, 8, 16} on self-attention and feed-forward layers, AdaptFormer bottleneck ∈ {4, 8, 16, 32} on feed-forward layers, each as serial, parallel or serial+parallel; Affine-LN on normalisation layers.
- Setting: few-shot = "1-, 5-, and 10-shot regimes" (p. 6); the paper does not define a shot explicitly (by context, labelled 3D scans per target), and does not state how the support scans were sampled or the size of the validation set used for auditing. Single-task adaptation; no continual learning, no task sequence, no forgetting measurement. No text or spatial prompts.
- Data and backbones (p. 6): nine abdominal organs (spleen, left kidney, gallbladder, oesophagus, liver, pancreas, stomach, duodenum, aorta); binary segmentation on TotalSegmentator, multi-class on FLARE'22; pretrained FSEFT and SuPreM weights on a frozen Swin-UNETR. Training: 96³ patches, batch 1, AdamW, lr 1e-3, 200 epochs with early stopping, one V100 32 GB; mean over 3 random seeds, metric Dice (no std reported).
- Results, TotalSegmentator with FSEFT (Table 1, p. 7), mean Dice 1/5/10-shot: SEA-PEFT 78.33 / 79.90 / 80.29; full fine-tuning 75.90 / 77.15 / 76.93; LoRA 74.34 / 76.30 / 77.79; AdaptFormer 74.55 / 76.29 / 75.12; Affine-LN 73.29 / 76.58 / 77.33; BitFit 73.24 / 72.70 / 76.69. The abstract's "2.4–2.8 points over the strongest fixed-topology PEFT baselines" matches the margins over the best baseline including full fine-tuning (+2.43, +2.75, +2.50).
- FLARE'22 (Table 1): SEA-PEFT 75.77 (1-shot), 76.33 (5-shot), 77.03 (10-shot); at 10-shot Affine-LN is best (77.52), so the claim "across all shot regimes and both datasets" (p. 6) does not hold for FLARE 10-shot. No full fine-tuning row on FLARE.
- SuPreM (Table 2, p. 8, 5 organs): SEA-PEFT 77.89 (5-shot), 79.93 (10-shot) vs Spatial Adapter 77.01 / 75.95 and LoRA 58.65 / 69.35.
- Cost (Table 3, p. 8): 2.5 / 4.5 / 6.5 h end to end for 1/5/10-shot (6000 / 8000 / 12000 steps), 0.2 % trainable parameters.
- Observation relevant to few-shot: in TotalSegmentator, full fine-tuning does not improve from 5 to 10 shots (77.15 → 76.93), whereas LoRA rises from 74.34 to 77.79 over 1 → 10 shots (Table 1).
- Limitations stated by the authors: none stated explicitly; direct comparison with NOAH/AutoPEFT called infeasible (p. 6).

## Where it fits in Ch. 2 (suggestion)
Section on few-shot / parameter-efficient adaptation of 3D medical foundation models: recent evidence that PEFT (incl. LoRA) is competitive with or better than full fine-tuning at 1–10 labelled scans, and that the best PEFT configuration depends on organ and number of shots.

## Relevance (NOT from the paper)
Supports the thesis's motivation for comparing LoRA rank and full fine-tuning under few shots, but it is single-task, non-promptable and measures no forgetting, so it does not touch the gap claim.
