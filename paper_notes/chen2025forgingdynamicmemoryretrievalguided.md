# PRIMED (Chen et al. 2025) — paper notes

Read as prior work for Ch. 2 (State of the Art): continual learning of a medical CLIP-style foundation model with retrieval-built reference data (ZSCL-style distillation extended), including protection of zero-shot ability.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Zizhi Chen, Yizhen Gao, Minghao Han, Yizhou Liu, Zhaoyu Chen, Dingkang Yang, Lihua Zhang. *Forging a Dynamic Memory: Retrieval-Guided Continual Learning for Generalist Medical Foundation Models.* arXiv:2512.13072v1 [cs.CV], 15 Dec 2025 (document date 16 Dec 2025). 26 PDF pages (main p. 1–10, references p. 11–15, appendix A–G p. 16–26) |
| Local PDF | `papers/t6_cl_medseg_foundation/chen2025forgingdynamicmemoryretrievalguided.pdf` |
| Bib key | `chen2025forgingdynamicmemoryretrievalguided` (`@misc`, arXiv) |
| Version read | arXiv v1. **No peer-reviewed venue stated** in the PDF |
| Code | "provided in the supplementary materials" (abstract); project page github.com/CZZZZZZZZZZZZZZZZZ/PRIMED (p. 1) |
| Notes written | 2026-10-22, by Claude, from arXiv v1. Page numbers = PDF pages |

## 1. Problem and idea (abstract, Sec. 1, p. 1–3)
- Medical continual learning must keep **fine-grained intra-modality** features and bridge **large inter-modality** gaps; medical images are similar within a domain but very different across domains (p. 1–2, Fig. 1).
- For continually fine-tuned VLMs, forgetting covers both earlier downstream tasks and **pretrained knowledge / zero-shot ability** (p. 2).
- Pretraining data cannot be replayed; ImageNet-label-based reference sets (as in ZSCL-type methods) do not fit caption-supervised medical VLMs (p. 2).
- **PRIMED** (Precision Retrieval-Infused model for MEDical): build reference data by **retrieval** (RAG) from an 18M image–caption database from PubMed, queried with a ~3,000-entry medical question pool; distil with contrastive knowledge transfer, keep image–text alignment, and regularise weights with a dynamic Fisher importance (p. 2–3, Fig. 2).
- Also proposes the **MGTIL** benchmark (Medical Generalist Task Incremental Learning) with HieraMedTransfer and MedXtreme (p. 2–3).

## 2. Setting (Sec. 3.1, p. 4)
- Authors' terms: **task-incremental and domain-incremental** learning; the domain shift comes from the task order.
- **Task identity is given at inference**; the model only distinguishes classes within the task (p. 4).
- A **task** = one classification dataset with its own class names, classified CLIP-style by image–text similarity with "a photo of {c}" prompts (p. 4).
- Not a few-shot setting in the k-shot sense; MedXtreme is described as containing many few-shot (rare) classes (App. D.2, p. 18).

## 3. Method (Sec. 3.1–3.3, p. 4–6)
- **Retrieval database:** following BIOMEDICA, PubMed images and captions, cleaned and multi-panel figures split (DAB-DETR-based capture model, App. D.1, p. 17); embedded with **Qwen3-Embedding-8B**; 18M entries (p. 4).
- **Question pool:** ~3,000 label-like queries from literature, datasets, QA reformulation, Wikipedia; previous task labels added before each task (Eq. 1, p. 5).
- **Dynamic multi-stage retrieval** (Sec. 3.2, p. 5): dense cosine retrieval with a dynamic threshold at the K-th largest unique score (Eq. 2–6); rerank with the BiomedCLIP encoder, keep top images per caption, BM25 lexical gate (Eq. 7); **Dynamic Siphon** splits queries into task-, domain- and general-level subsets sampled with different sizes (Eq. 8–12).
- **Contrastive Knowledge Transfer (CKT)** (Eq. 13–17, p. 6): B×B image–text similarity matrices of student and teacher on retrieved pairs; KL divergence of row-wise (image→text) and column-wise (text→image) softmax distributions, teacher = **model after task t−1**.
- **Cross-Modality Consistency (CMC)** (Eq. 18, p. 6): contrastive loss of the student's similarity matrix against the identity, because the t−1 teacher itself has forgotten.
- Training loss: L_train = L_CE + α L_CKT + β L_CMC (Eq. 19). Defaults α = 1, β = 0.25 (Table 4c–d, p. 9).
- **Dynamic Fisher Weight Guard (DFG)** (Eq. 20–22, p. 6): EWC-style weighted L2 to the previous task's parameters, with per-step importance = squared gradient of (L_train − L_CE), i.e. of the distillation/alignment terms.
- Trained parameters: the paper argues for backbone fine-tuning rather than prompt tuning/adapters for complex tasks (Sec. 2, p. 3); which parameters are frozen is **not stated explicitly**.
- Extra memory: retrieval database and retrieved reference data; no stored task samples (p. 9).

## 4. Data (Sec. 3.4 p. 6–7; Sec. 4.1 p. 8; App. D.2 Tables 5–6 p. 18–19)
- All **2D image classification**.
- **HieraMedTransfer** (Table 5, p. 18; images, classes): RANZCR (X-ray, blood vessel) 33,665, 11; CheXchoNet (X-ray, chest) 71,589, 4; PD (X-ray, lung) 4,575, 3; BreakHis (pathology, breast) 7,909, 2; Chaoyang (pathology, colonic) 6,160, 4; NuCLS (pathology, gastric) 33,284, 2; EyePACS (fundus, diabetes) 35,126, 5; AIROGS (fundus, glaucoma) 101,442, 2; FARFUM-RoP (fundus, ROP) 1,533, 3.
- **MedXtreme** (Table 6, p. 19): AOD (fundus) 10,000, 8; BMC (cell, bone marrow) 171,375, 21; ISIC2024 (skin) 81,722, 33; NCT100K (pathology, colorectal) 100,000, 9; NIH-Chest-Xray 112,120, 15; PITVIS (endoscopy, pituitary) 120,024, 15.
- Train/test splits: **not stated**.
- Orders: HieraMedTransfer Order I by domain (X-ray → pathology → fundus, column order of Table 7, p. 20); Order II described as "randomized alphabetical" (p. 7) and as "alphabetical" (p. 8); Table 8 columns are alphabetical (p. 21). MedXtreme Order I alphabetical, Order II random (p. 7–8).

## 5. Implementation (Sec. 4.1 p. 7; App. E.1 p. 22; App. F p. 23–25)
- Backbone **BiomedCLIP** (ViT-B/16, following ZSCL's choice); chosen for data provenance, zero-shot behaviour and architecture maturity (App. F.1, p. 24).
- 1,000 iterations per task, batch size 64 (per GPU, App. E.1), learning rate 1 × 10⁻⁵, label smoothing 0.2; small datasets cycled (p. 7; p. 22).
- 4× NVIDIA A6000. Seed 42 for all experiments (p. 9); no variance over seeds reported.
- Baselines' reference sets: for ZSCL and SND an equally sized reference set built by proportional retrieval with 30 medical keywords; GIFT generates images from the question pool (p. 8). LoRA/prompt methods use their papers' hyperparameters (p. 22).
- Other backbones (MMKD-CLIP, UniMed-CLIP, CLIP) in Table 13 (p. 24).

## 6. Evaluation protocol and metrics (Sec. 3.4, p. 7; Fig. 3a)
- HieraMedTransfer: ZSCL metrics on the task × training-step accuracy matrix — **Transfer** (upper-right triangle, tasks not yet trained, i.e. zero-shot ability), **Avg.** (all tasks and timestamps), **Last** (after the final task); each task averaged first (p. 7).
- MedXtreme: zero-shot too weak, so **ACC, AUC, BWT** (Díaz-Rodríguez) and Forgetting (Chaudhry); only BWT reported because it mirrors Forgetting (p. 7, p. 9).
- References (p. 8): **Zero-shot** = upper bound for Transfer; **Continual FT** = lower bound for Avg./Last; **l2 baseline** (weight-magnitude regularisation) = reference for Δ columns. **Fine-tune** on each target dataset alone = upper bound in App. Tables 7–8 (average 85.15, p. 20–21).
- Compared methods: LwF, iCaRL, WiSE-FT, ZSCL, MoE-CL, SND, DIKI, GIFT (Tables 1–2).

## 7. Results
- **HieraMedTransfer, Table 1 (p. 7)**, Transfer / Avg. / Last (%), Order I | Order II:
  - Zero-shot 57.5 / 52.9 / 53.0 | 57.5 / 52.9 / 53.0
  - Continual FT 51.4 / 67.6 / 70.8 | 47.7 / 61.9 / 58.6
  - l2 baseline 53.6 / 68.5 / 74.1 | 45.8 / 63.9 / 66.8
  - ZSCL 57.7 / 70.5 / 77.6 | 45.2 / 65.0 / 76.9
  - MoE-CL 56.8 / 70.7 / 76.1 | 47.6 / 66.1 / 74.2
  - PRIMED_uni (ZSCL-style uniform reference data) 57.1 / 72.7 / 81.7 | 48.0 / 67.7 / 77.0
  - **PRIMED_dyn 58.3 / 73.1 / 82.1 | 48.5 / 68.0 / 81.2** (best)
- **MedXtreme, Table 2 (p. 8)**, ACC / AUC / BWT (%), Order I | Order II:
  - Zero-shot 9.9 / 61.2 / – | 9.9 / 61.2 / –
  - Continual FT 61.0 / 86.7 / −15.1 | 60.0 / 84.1 / −16.0
  - l2 baseline 61.1 / 82.9 / −10.0 | 57.3 / 81.2 / −14.5
  - ZSCL 53.7 / 79.9 / −6.5 | 48.3 / 78.6 / −13.7
  - iCaRL (replay) 65.9 / 84.8 / −3.1 | 64.2 / 84.3 / −5.1
  - GIFT 66.0 / 86.6 / −3.7 | 65.7 / 85.2 / −4.1
  - **PRIMED_dyn 68.6 / 87.4 / −2.7 | 68.1 / 86.3 / −3.4**
- ZSCL with a reference set is strong on the regular Order I but weaker on random Order II and on MedXtreme (p. 8; Tables 1–2).
- **Ablations (HieraMedTransfer Order I; Tables 3–4, p. 9):** full model 58.3 / 73.1 / 82.1; without CKT clearly worse (e.g. CMC only 54.3 / 68.9 / 78.9); teacher **Last CLIP** 58.3 / 73.1 / 82.1 > initial CLIP 57.9 / 70.7 / 78.2 > WiSE(0.5) 58.1 / 71.4 / 79.1; DFG better than l2 (57.2 / 72.9 / 81.8) and EWC; hierarchical retrieval better than BM25 (55.1 / 72.2 / 81.8) or embedding only (56.1 / 72.5 / 81.5). The Last-CLIP teacher advantage also holds on MedXtreme (Table 10, p. 23). Full ablations on all four sequences in Tables 9–10 (p. 22–23).
- Retrieval ratio and volume analyses (Tables 11–12, Fig. 8, p. 23–24); other backbones (Table 13, p. 24): authors report consistent superiority (App. F.2, p. 25).
- Inconsistency found: EWC in the regularisation ablation has Last 80.6 in Table 4e (p. 9) but 82.1 in Table 10 (p. 23).

## 8. Limitations and future work (authors; App. A–C, p. 16–17)
- Storage and compute overhead of building, maintaining and querying the retrieval corpus; suggest pre-computing retrieval for the static question pool.
- PubMed as the only source avoids leakage/copyright issues, but fairness cannot be enforced at retrieval level; possible unseen demographic biases.
- Future work: release the database after an ethics audit, a retrieval cloud service, data streaming; enrich rare-disease content.

## 9. Check of the author's notes
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/introduction.tex:29` | "recent studies have begun to investigate continual learning for medical foundation models" (cited with Chen 2026 and Zhang 2025) | **Correct.** Continual learning of BiomedCLIP, which the paper calls a generalist medical foundation model (title; p. 4). Note: 2D classification, not segmentation. |
| `thesis/related_work.tex` | — | **Not discussed** (no cite, no mention of PRIMED). If added to Ch. 2, it fits the "continual learning for VLMs" section next to ZSCL. |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
1. **Relation:** medical counterpart of ZSCL — protects the pretrained (zero-shot) ability of a medical VLM during continual fine-tuning, which corresponds to the thesis's concern with loss of pretrained ability (control-task drop) and to its distillation-based strategy adapted from ZSCL.
2. **Directly relevant evidence:** (a) ZSCL adapted to medical data with a retrieved reference set beats continual FT on HieraMedTransfer but falls below it on MedXtreme ACC (53.7 vs 61.0, Table 2), so ZSCL's benefit is not universal in medical settings; (b) the teacher ablation favours the **previous-task model** over the **initial model** for medical VLMs (Table 4a), the opposite of ZSCL's Table 1d; the thesis's strategy uses the pretrained model as teacher, so this is a design decision an examiner could question.
3. **Gap claim:** does **not** weaken "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model": 2D, classification by image–text similarity with class-name templates (not free-text prompts for dense prediction), not 3D, not few-shot, task identity given.
4. Single seed (42), no variance; arXiv only. Cite for the setting and qualitative findings rather than exact margins.
