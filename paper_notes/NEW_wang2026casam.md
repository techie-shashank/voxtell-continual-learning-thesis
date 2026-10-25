# CA-SAM (Continual Alignment for SAM) — paper notes

Read as prior work for Ch. 2 (State of the Art): exemplar-free continual segmentation with a frozen 2D SAM, one small alignment module per dataset and a VAE-based task router with fallback to frozen SAM for unseen domains.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Wang, Dai, Wang, Yang, Bi, Sun (Xi'an Jiaotong University). *Continual Alignment for SAM: Rethinking Foundation Models for Medical Image Segmentation in Continual Learning.* arXiv:2511.17201v1 [cs.CV], 21 Nov 2025 (p. 1, margin). 17 PDF pages: p. 1–8 main paper, p. 9–10 references, p. 11–17 "Supplementary Material" (Appendix A–F, Tables 7–11, Algorithms 1–7) |
| Local PDF | `papers/t6_cl_medseg_foundation/NEW_wang2026casam.pdf` |
| Bib key | none yet (author's notes use the literal label `[Wan+26]`; planned key `NEW_wang2026casam`). Note: the arXiv version is dated **2025**, so "2026" in the key/label is not supported by this PDF |
| Version read | **arXiv preprint v1 (21 Nov 2025).** The PDF does **not** state a peer-reviewed venue (no conference/journal header or acceptance note) |
| Code | "code, models and datasets will be released on https://github.com/azzzzyo/Continual-Alignment-for-SAM" (abstract, p. 1) |
| Notes written | 2026-10-23, by Claude, from the arXiv preprint v1. Page numbers = PDF pages (the paper has no printed page numbers) |

## 1. Problem and idea (abstract, Sec. 1, Sec. 3.1; p. 1–3)
- Privacy rules between institutions often prevent joint training on pooled data, which motivates continual segmentation from data streams without revisiting earlier samples (abstract; Sec. 1, p. 1).
- Three limitations of SAM-based continual methods claimed (p. 2): (1) poor balance of computation and performance due to large backbone updates; (2) reliance on stored exemplars/rehearsal, conflicting with exemplar-free constraints; (3) fine-tuning erodes SAM's generalisation, giving poor out-of-distribution (OOD) performance.
- Preliminary study (Sec. 3.1, Fig. 2, p. 3): on three datasets, full fine-tuning of SAM beats CNNs (U-Net, UNet++) but is costly; PEFT reduces cost but only matches CNN IoU (gains in Boundary IoU).
- Proposal: an **Alignment Layer** between frozen SAM encoder and decoder, and **CA-SAM**, one Alignment Layer per task plus an exemplar-free **VAE router** with OOD fallback to frozen SAM (Sec. 1, p. 2; contributions p. 2).

## 2. Setting (Sec. 3.3, p. 3–4; Sec. 4.1.2, p. 5)
- Scenario in the authors' terms: "continual image segmentation", "exemplar-free continual learning", "cross-dataset continual segmentation" (p. 1–2, Fig. 1). They do **not** use task-/class-/domain-incremental labels.
- **A task = one dataset** D_t with its own train/test split (Eq. 4, p. 3); nine tasks, each with a different organ/structure and/or modality (Sec. 4.1.1, p. 5).
- At stage t only D_t^tr is accessible; evaluation on the accumulated test sets of all seen tasks (p. 3–4).
- **Task identity at inference: not given.** The VAE router picks the alignment layer "without explicit task labels" (p. 4). Inputs judged OOD use an identity alignment layer, i.e. frozen SAM (p. 4).
- **Prompts are spatial:** random points or boxes during training, **box prompts only at test** (Sec. 4.1.2, p. 5). No text prompts.
- Not few-shot: official train/test splits, hundreds to ~1,700 training images per dataset (Sec. 4.1.1, p. 5; App. A, p. 11).
- **Task order (main):** ACDC → EBHI-SEG → 56Nx → DN → Polyp → MSD_Prostate → MSD_Spleen → Promise12 → STS-2D (p. 5). Three further orders in Table 8 (p. 15): DN → 56Nx → EBHI-SEG → STS-2D → promise12 → MSD_Spleen → MSD_Prostate → Polyp → ACDC; EBHI-SEG → Polyp → ACDC → MSD_Prostate → 56Nx → MSD_Spleen → DN → promise12 → STS-2D; MSD_Prostate → 56Nx → STS-2D → Polyp → DN → MSD_Spleen → ACDC → EBHI-SEG → promise12.

## 3. Method (Sec. 3.2–3.3, p. 3–4; Fig. 3; Alg. 7, p. 14)
- **Frozen:** SAM image encoder E and mask decoder D (Eq. 1–3, p. 3; p. 5). The prompt encoder is not discussed separately.
- **Trained per task:** Alignment Layer A_t, acting on the encoder feature map, Z̃ = A_t(E(I)), Y = D(Z̃) (Eq. 2–3, p. 3). A_t = stacked **CAResBlocks**: two 3×3 conv + ReLU, adaptive global average pooling, 1D conv for channel attention, LayerNorm2d (Sec. 4.1.2, p. 5). Number of blocks in the final model: not stated explicitly; Fig. 6 (p. 8) ablates 2–5 layers.
- **Task router:** a global feature f is obtained from Z by parameter-free attention pooling (softmax over L2 norms with temperature T, Eq. 5, p. 4); one **VAE V_t** per task models p_t(f), trained with reconstruction + β-weighted KL (ELBO) loss (Eq. 6, p. 4).
- **Inference:** score s_t(f) for each VAE, t* = argmin s_t (Eq. 7, p. 4). If s_t* is below a per-task threshold τ_t*, A_t* is loaded; otherwise **identity alignment layer** (frozen SAM, zero-shot) (p. 4; Alg. 7).
- τ_t calibrated by K-fold cross-validation on the training set, as the **p97** percentile of the held-out ELBO distribution (p. 4–5; Table 6, p. 8; Table 9, p. 15).
- **No memory of earlier samples** (exemplar-free, Table 1 "EF" ✓). Old alignment layers and VAEs are kept and never modified (Alg. 7).

## 4. Data (Sec. 4.1.1, p. 5; App. A, p. 11)
All images are 2D, resized to 1024×1024 (p. 5). Counts are images (train/test), from App. A; official splits (p. 5).
- **ACDC** — MR, heart (LV, myocardium, RV) — 1632/177.
- **EBHI-SEG** — histopathology, colon cancer — 1701/487.
- **56Nx** — histopathology, glomerulus — 558/463.
- **DN** — histopathology, glomerulus — 724/391.
- **Polyp** (Kvasir-SEG, ref. [15]) — "RGB imaging" — 804/196. **Inconsistency:** App. A gives the target as "the spleen" (p. 11); the cited dataset is a polyp dataset.
- **MSD Prostate** — MR T2, peripheral and transition zone — 419/53.
- **MSD Spleen** — CT, spleen — 876/146.
- **Promise12** — MR, prostate — 712/66.
- **STS-2D** — X-ray, teeth — 1700/70.
- How 2D images were derived from originally volumetric collections (ACDC, MSD, Promise12): **not stated**; ACDC, MSD and Promise12 are cited via ref. [8], an interactive medical segmentation benchmark (p. 5, p. 9).
- Sec. 4.1.1 lists modalities as MR, CT and histopathology (p. 5); App. A additionally has RGB (Polyp) and X-ray (STS-2D) (p. 11): minor inconsistency.
- **Unseen (OOD) datasets** for zero-shot tests: DDTI, BUSI benign, BUSI malignant, Brain Tumor, CAMO (Table 2, p. 6). Sizes, modalities and sources: **not stated**.
- No patient numbers given.

## 5. Implementation (Sec. 4.1.2, p. 5; App. D, F)
- Single **NVIDIA RTX A5000 (24 GB)**; inputs 1024×1024; Adam, lr 1e-4, batch size 6, **24 epochs per task** (p. 5).
- SAM variant: the text does not name it; Fig. 2 (p. 3) labels a point "SAM Vit-B".
- VAE: two-layer MLP encoder/decoder, latent dimension 64, β = 16.5, 10 epochs, lr 5e-4; K = 5 folds; p97 threshold (p. 5); temperature T = 1 (App. F.1, p. 15–16).
- Trainable parameters 3.54M, 514.3 GFLOPs per training pass on a 3×1024×1024 image (Table 3, p. 6; Fig. 2 caption, p. 3). Training time and memory: not stated.
- Baselines re-implemented on the alignment-layer framework (App. D.1, p. 12; Alg. 1–6): naive sequential fine-tuning of the alignment layer (lower bound), LwF, EWC, EMR (merging), ER, DER, L2P, MoDA, MoDA + HQ-SAM decoder; joint training (upper bound). ER, DER and MoDA store exemplars (Table 1, EF ✗).
- Number of runs/seeds, variance: **not stated**; no ± values.

## 6. Evaluation protocol and metrics (Sec. 3.3, p. 3–4; App. B, p. 12)
- Metrics: **IoU** and **Boundary IoU (BIoU)**, reported in %.
- IoU_t = test-set-size-weighted mean IoU over tasks 1…t after training t tasks (Eq. 8). **Last-IoU** = IoU_N (Eq. 9); **Avg-IoU** = mean of IoU_t over the N steps (Eq. 10).
- Forgetting f_{k,t} = max_{j<t}(IoU_{k,j} − IoU_{k,t}) (Eq. 11); **FF-IoU** = mean over k = 1…N−1 of f_{k,N} (Eq. 12). Same for BIoU. (Chaudhry-style maximum-drop forgetting; the paper does not cite Chaudhry for it.)
- Zero-shot/OOD: after all nine tasks, IoU/BIoU on five unseen datasets, plus router **OOD discrimination accuracy** (Sec. 4.4, p. 6; Table 2).
- Single-dataset versatility: alignment layer trained and tested on each dataset alone (Sec. 4.2, Table 3, p. 5–6; Table 7, p. 13).

## 7. Results
- **Continual learning, Table 1 (p. 6), main order**; Last-IoU / Avg-IoU / FF-IoU | Last-BIoU / Avg-BIoU / FF-BIoU:
  - Joint training 78.43 / — / — | 61.26 / — / —
  - SAM (zero-shot) 53.81 / — / — | 36.52 / — / —
  - SAM + AL (naive) 14.38 / 37.93 / 65.79 % | 13.50 / 29.91 / 49.69 %
  - LwF 27.84 / 30.77 / 3.03 % | 22.82 / 28.45 / 3.05 %
  - EWC 17.78 / 38.51 / 57.32 % | 12.58 / 30.42 / 42.16 %
  - EMR 43.09 / 53.96 / 10.95 % | 26.05 / 33.77 / 8.53 %
  - ER 59.19 / 69.59 / 21.68 % | 39.93 / 51.37 / 24.25 %
  - DER 59.99 / 63.14 / 6.55 % | 40.69 / 42.20 / 6.69 %
  - L2P 57.34 / 53.84 / 1.55 % | 37.86 / 35.70 / 1.79 %
  - MoDA + HQ-SAM 69.30 / 70.86 / 2.00 % | 55.52 / 55.88 / 1.64 %
  - MoDA 70.64 / 72.44 / **0.66 %** | 52.12 / 54.45 / 0.65 %
  - **CA-SAM 76.12 / 76.90 / 1.43 %** | **59.95 / 59.45 / 0.24 %**
- Text (p. 5): CA-SAM improves Last-IoU and Last-BIoU over the second-best by 5.48 % and 4.43 % (own check: 76.12 − 70.64; 59.95 − 55.52). It also says CA-SAM reduces forgetting "to nearly zero" (p. 5); **note:** MoDA has lower FF-IoU (0.66 % vs 1.43 %; MoDA is highlighted as best in Table 1). CA-SAM's Last-IoU is 2.31 points below joint training (own calc).
- **Zero-shot on unseen data, Table 2 (p. 6), IoU / BIoU:** SAM: DDTI 78.08 / 45.98, BUSI benign 75.73 / 53.30, BUSI malignant 69.90 / 33.70, Brain Tumor 52.85 / 60.89, CAMO 67.60 / 43.05. CA-SAM: 77.62 / 45.73, 72.99 / 51.67, 65.86 / 31.66, 52.85 / 60.89, 62.37 / 39.60. MoDA: 29.66 / 20.18, 10.06 / 11.45, 6.24 / 6.50, 24.47 / 30.59, 21.51 / 13.85. LwF: 61.34 / 21.22, 59.16 / 37.64, 30.38 / 13.07, 34.20 / 27.46, 21.14 / 12.79.
- Router OOD discrimination accuracy, weighted average **99.42 %** over the five unseen datasets (DDTI 99.37 %, BUSI benign 96.34 %, BUSI malignant 92.38 %, Brain Tumor 100.00 %, CAMO 92.00 %) (Sec. 4.4, p. 6). MoDA's hard routing misassigns OOD samples (p. 6).
- **Single-dataset, Table 3 (p. 6), params / GFLOPs / Avg-IoU / Avg-BIoU:** SAM — / — / 55.08 / 37.67; Tuning Decoder 4.06M / 669.8 / 70.40 / 53.86; HQ-SAM 5.14M / 678.9 / 72.91 / 58.41; SAM-Med2D 13.31M / 728.2 / 75.17 / 58.97; **CA-SAM 3.54M / 514.3 / 80.15 / 66.52**. Best on 5 of 9 datasets (ACDC, EBHI-SEG, 56Nx, DN, STS-2D); worse than all three fine-tuned SAM variants on Polyp (65.02 vs ≥ 78.46), MSD Prostate, MSD Spleen and Promise12 (Table 7, p. 13).
- Possible inconsistency: weighting the per-dataset IoUs of Table 7 by the App. A test-set sizes gives 78.58 for CA-SAM, not 80.15 (own calc); the weights used are not specified. SAM zero-shot is 55.08 in Table 3 but 53.81 in Table 1 (different protocols, not explained).
- **Task-order robustness, Table 8 (p. 15)**, CA-SAM Last-IoU / FF-IoU: 75.61 / 1.71 %, 75.78 / 1.31 %, 76.19 / 1.66 %. MoDA FF-IoU 2.20 %, 1.44 %, **0.96 %**; FF-BIoU of MoDA lower than CA-SAM in all three orders (1.12 vs 1.84; 1.06 vs 1.64; 0.90 vs 1.70). **Inconsistency:** App. D.2 says CA-SAM has "the lowest forgetting across all orders" (p. 13–14), which Table 8 contradicts for the third order (IoU) and all orders (BIoU). Naive, LwF, EWC vary strongly with order; routing-based methods "largely invariant to task order" (p. 13–14).
- **Ablations:** parameter-free attention pooling best among six pooling variants, Last-IoU 76.41 (Table 5, p. 8); threshold p97 chosen for the trade-off (IoU (Med) 76.02, Acc 99.42; p99 76.04 / 98.76) (Table 6, p. 8); temperature T robust in [1, 16] (Table 10); β < 6 unstable, stable for β ∈ [7, 18] (Table 11, p. 16). More alignment blocks improve fitting (Fig. 6, p. 8). Note: Table 6 p97 IoU (Med) 76.02 vs Table 1 Last-IoU 76.12 for the same configuration (unexplained).
- Explainability: TV and JS distances to features of an Adapter-fine-tuned SAM shrink slightly after the alignment layer (56Nx: TV 0.2830 → 0.2742; DN: 0.2840 → 0.2832) (Table 4, p. 7).

## 8. Limitations stated by the authors
- No limitations section. The conclusion (p. 8–9) names no limitation or future work beyond calling CA-SAM "a promising direction".
- Implicit: full-parameter fine-tuning of SAM still gives the "pronounced improvements" that PEFT does not reach (Sec. 3.1, p. 3).

## 9. Check of the author's notes
`thesis/introduction.tex` contains no sentence about CA-SAM (searched "CA-SAM", "Wan+26", "Continual Alignment"). CA-SAM has no row in the positioning table (`related_work.tex:225–240`).

| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:92` | "CA-SAM adapts the two-dimensional SAM" | **Correct** (Eq. 1–3, p. 3; 2D images, p. 5). |
| `thesis/related_work.tex:92` | "processing volumetric datasets slice by slice" | **Not supported.** The paper never mentions volumes or slicing; it works on 2D images resized to 1024×1024 (p. 5), and five of nine datasets are natively 2D (histopathology, endoscopy RGB, X-ray; App. A, p. 11). Rephrase as "on 2D images, including 2D images from MR and CT collections". |
| `thesis/related_work.tex:92` | "inserts lightweight alignment blocks between the frozen image encoder and the decoder" | **Correct**; the decoder is frozen as well (p. 3, p. 5). |
| `thesis/related_work.tex:92` | "trains a separate set of these blocks per dataset" | **Correct** (Sec. 3.2, p. 3; p. 5; Alg. 7). |
| `thesis/related_work.tex:92` | "selects among them through a task router based on variational autoencoders, which reverts to the original representation for unfamiliar inputs" | **Correct** (Eq. 7, identity alignment layer, p. 4). |
| `thesis/related_work.tex:92` | "across nine heterogeneous datasets it reported a forgetting measure of 1.43 % and an out-of-distribution discrimination accuracy of 99.42 %" | **Correct numbers** (FF-IoU, Table 1, p. 6; Sec. 4.4, p. 6). Missing context: 99.42 % is over **five unseen** datasets, not the nine; MoDA has lower FF-IoU (0.66 %), so 1.43 % is not the lowest forgetting in that table. |
| `thesis/related_work.tex:94` | capability "held in a dedicated component, which is reached … through … an explicit routing decision" | **Correct** for CA-SAM (per-task alignment layer chosen by the VAE router, p. 4). |
| `thesis/related_work.tex:101` (% SUMMARY TABLE) | "2D SAM ViT-B, slices resized to 1024x1024; average IoU 76.90 % over nine datasets" | **Partly correct.** ViT-B appears only as a label in Fig. 2 (p. 3), not in the text. "Slices": not stated (images, p. 5). 76.90 % is **Avg-IoU** (mean over the nine training steps of the cumulative IoU, Eq. 10), not the final IoU; final Last-IoU is 76.12 %; the single-dataset average IoU is 80.15 % (Table 3). Label the metric explicitly. |
| `thesis/related_work.tex:212` (summary table) | Data "Nine datasets (2D slices)"; approach "Per-dataset alignment blocks, VAE router"; result "Forgetting 1.43 %" | **Mostly correct.** Replace "2D slices" by "2D images" (see above). Result correct (Table 1), name it FF-IoU. |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
1. **Relation to this thesis:** both protect a pretrained segmentation foundation model during a sequence of tasks and test retention outside the sequence (CA-SAM's zero-shot test on unseen datasets resembles this thesis's control task). But CA-SAM is **2D**, uses **spatial (box/point) prompts**, keeps **one module per dataset selected by a router** (a routing decision, no single shared parameter set), uses full training sets (not few-shot), and a task is a whole dataset with a different modality/structure.
2. **Gap claim** ("no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model"): **not weakened.** SAM here takes box prompts only at test (p. 5), no text input; all data are 2D images (p. 5).
3. Facts usable for the gap/positioning: (a) box prompts only at test, points/boxes in training (p. 5); (b) 2D, 1024×1024 images, no volumes (p. 5); (c) not few-shot: official splits with 419–1,701 training images per dataset (App. A); (d) one task order in the main table, three more in the appendix; no seeds.
4. Possible support for this thesis's design: their observation that routing-based isolation is order-robust while LwF/EWC/naive vary strongly with order (Table 8) relates to the original/reverse orders; their Chaudhry-style max-drop forgetting (Eq. 11–12) matches the type of forgetting measure used here (check that the thesis's Final Forgetting definition is the same before claiming this).
5. The author's argument at `related_work.tex:94` (dedicated components need routing or task identity, which a free-text promptable model lacks) is consistent with CA-SAM; CA-SAM's OOD fallback is a counter-example to "routing always fails", so the reference to the mixture-of-experts routing failure mode should not be generalised to VAE routing without care (CA-SAM reports 99.42 % OOD accuracy, though MoDA's routing fails, p. 6).
6. Bib: arXiv only, dated 2025; check for a published version before adding the entry and before using "2026" in the key/label.
