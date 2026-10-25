# MSLoRA-CR (Zhang et al. 2025) — paper notes

Read as prior work for Ch. 2 (State of the Art): continual (incremental) learning of a medical large vision-language model with modality-specific LoRA branches.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Haojie Zhang, Yixiong Liang, Hulin Kuang, Lihui Cen, Zhe Qu, Yigang Cen, Min Zeng, Shichao Kan. *Contrastive Regularization over LoRA for Multimodal Biomedical Image Incremental Learning.* arXiv:2508.11673v1 [cs.LG], 8 Aug 2025. 10 PDF pages (8 main incl. conclusion, references p. 8–10) |
| Local PDF | `papers/t6_cl_medseg_foundation/Zhang_2025.pdf` |
| Bib key | `Zhang_2025` (`@inproceedings`, Proc. 33rd ACM International Conference on Multimedia (MM '25), pp. 7500–7509, DOI 10.1145/3746027.3754917 in the bib) |
| Version read | arXiv v1. **The PDF does not state the venue** (no ACM reference-format block); the ACM MM fields in the bib were not checked against the publisher page here. The bib entry lacks editors and conference location (chair requires place for proceedings) |
| Code | github.com/VentusAislant/MSLoRA_CR (abstract, p. 1) |
| Notes written | 2026-10-22, by Claude, from arXiv v1. Page numbers = PDF pages. The supplementary material referred to in the text is not in the PDF |

## 1. Problem and idea (abstract, Sec. 1, p. 1–2)
- Introduces **Multimodal Biomedical Image Incremental Learning (MBIIL)**: train one unified model incrementally over biomedical image **modalities and tasks**, to avoid one model per modality/task (p. 1).
- Two challenges: keep earlier knowledge, and reuse knowledge from earlier modalities for new ones (p. 1).
- Existing PEFT-based CL (e.g. InfLoRA, MoE adapters) targets task-incremental learning on natural images and ignores modality-incremental complexity (p. 2).
- **MSLoRA-CR:** a frozen large vision-language model (LVLM) with a new **modality-specific LoRA** branch per task, plus a **contrastive regularisation** on LoRA parameters (pull together same-modality branches, push apart different-modality ones) and an **orthogonality** constraint (p. 1–2, Fig. 1).
- Headline: 1.88 % improvement in overall performance over unconstrained incremental LoRA fine-tuning (abstract; p. 2).

## 2. Setting (Sec. 1 p. 2; Sec. 3 p. 3)
- Authors' term: they apply **task-incremental learning** across modalities; task identities are available at inference (p. 2).
- Task set A (VQA, classification, report generation) × modality set B (pathology, radiology, dermatology) → a **modality-specific task sequence** T; each element (task, modality) has its own dataset (Sec. 3, p. 3).
- A **task** = one (task type, modality) pair, in practice one dataset (Table 1, p. 5).
- Inference: a mask selecting LoRA branches is specified manually per task (p. 3).
- Not few-shot (full datasets; sizes not stated in main text).

## 3. Method (Sec. 3.1–3.5, p. 3–5; Fig. 2 p. 4; Alg. 1 p. 5)
- Base: LLaVA-like LVLM = visual encoder (CLIP ViT) + mapping layer + LLM; visual tokens concatenated with text-instruction tokens and fed to the LLM (Sec. 3.1, p. 3).
- **Frozen:** whole LVLM (visual encoder, projector, LLM). **Trained:** LoRA branches inserted in the LLM (Sec. 3.2, p. 3).
- LoRA described as ΔW = AB with A ∈ R^{d_o×r}, B ∈ R^{r×d_i}; the text states A is initialised with zeros and B normally (p. 3).
- **MSLoRA** (Eq. 1, p. 3): for task t a new branch is added; forward pass e = Wh + Σ_{i=1}^{t} m_i A_i B_i h, with mask m whose first t entries are 1, i.e. **branches 1…t are summed**; earlier branches frozen, only branch t trained (p. 3, p. 5).
- Proposition 1 (p. 4, Eq. 2–4): the gradient for the new branch equals that for the pretrained weight W and does not depend on earlier branches; the authors use this to argue a stability–plasticity balance.
- **CR loss** (Sec. 3.4, p. 4–5): sim(P, Q) = exp(−Manhattan distance) (Eq. 5); L_converge = Σ (1 − sim) over earlier **same-modality** tasks (Eq. 6); L_diverge = Σ sim over earlier **different-modality** tasks (Eq. 7); L_cr = L_converge + L_diverge (Eq. 8).
- **Orthogonal loss** (Eq. 9, p. 5): ‖AᵀA − I‖²_F + ‖BBᵀ − I‖²_F.
- Total loss (Eq. 10, p. 5): L = L_ce + α L_cr + β L_ortho; chosen α = 0.1, β = 0.01 (p. 6, Table 4).
- Memory: one LoRA branch per task, grows linearly with the number of tasks; no replay buffer.

## 4. Data (Sec. 4.1, Table 1, p. 5)
- Nine datasets, three modalities, three task types, all **2D images**:
  - VQA: PathVQA (pathology), Slake and VQA-Rad (radiology; **merged into one dataset**), Fitzpatrick (dermatology; converted from classification to VQA).
  - Classification: CXP (radiology), PCam (pathology), HAM (dermatology, seven classes) — reformulated as instruction-based open-ended QA.
  - Report generation: WSI-DX (pathology), IU-X-Ray (radiology).
- Dataset sizes and splits: **not stated** in the main text ("supplementary materials", p. 5). Only aggregate: pathology modality 48,332 QA pairs, radiology 14,597 pairs (p. 7, in the order ablation).
- Main-experiment task order: **not stated** in the main text. Ablation (6 datasets) default order = PathVQA, Slake-VQARad, PCam, CXP, WSI-DX, IU-X-Ray (A1, B1, A2, B2, A3, B3, shaded row of Table 6, p. 7).

## 5. Implementation (Sec. 4.1, p. 6)
- Foundation model **LLaVA-Med-v1.5**.
- 8× A6000 (48 GB); AdamW without weight decay; cosine schedule; warm-up ratio 0.03; ~20 GPU hours per experiment, ~500 GPU hours total.
- LoRA **rank = alpha = 64** by default.
- Learning rate, epochs and batch size: not stated in the main text. Number of seeds/runs: not stated; no variance reported.

## 6. Evaluation protocol and metrics (Sec. 4.1, p. 5–6)
- VQA: accuracy on closed-ended, recall on open-ended questions. Classification: F1 and AUC (HAM: accuracy only). Report generation: F1 and BLEU.
- Overall: **SUM** of all task-specific metrics (p. 6).
- No forgetting/BWT or forward-transfer metric is defined; when the reported scores are measured (after the full sequence or after each task) is not stated explicitly.
- Comparisons (Table 2, p. 6): PathAsst (numbers copied from its paper), Quilt-LLaVA, BiomedGPT-B, **LLaVA-Med-v1.5 (marked baseline, zero-shot)**, **Data-Specific FT** (marked SOTA; text calls it "LoRA-Each": a separate LoRA per modality, p. 6), MSLoRA (no regularisation), MSLoRA-CR, MSLoRA-CR-ORTHO. No sequential full fine-tuning and no joint-training baseline.

## 7. Results
- **Table 2 (p. 6), SUM (%)**: Quilt-LLaVA 404.38; BiomedGPT-B 345.88; LLaVA-Med-v1.5 524.81; Data-Specific FT 970.29; MSLoRA 976.89; MSLoRA-CR 990.25; **MSLoRA-CR-ORTHO 995.21** (best).
- Selected per-dataset (MSLoRA / MSLoRA-CR-ORTHO / Data-Specific FT): PCam F1 92.74 / 93.21 / 91.83; CXP F1 88.05 / 91.05 / 90.89; IU-X-Ray BLEU 4.67 / 14.12 / 3.89; Fitzpatrick open 54.73 / 50.96 / 56.98 (Table 2).
- Authors: MSLoRA alone beats separate fine-tuning, attributed to an MoE-like effect of merging adapters; CR adds "approximately 16 points" (p. 6). (Table 2 difference MSLoRA-CR − MSLoRA is 13.36; my computation, not the paper's.)
- The abstract's 1.88 % matches 995.21 vs 976.89 (my computation).
- **Rank, Table 3 (p. 7), SUM on 6 datasets:** r = 8: 753.24; 16: 763.61; **32: 773.54**; 64: 760.83; 128: 678.94. Performance rises then falls with rank.
- **α, β, Table 4 (p. 7):** chosen α = 0.1, β = 0.01 (SUM 760.83); trainable α/β not better.
- **Placement, Table 5 (p. 7):** all layers 760.83; deepest 8 layers 730.08; shallowest 8 layers 752.70.
- **Task order, Table 6 (p. 7), SUM:** A1,B1,A2,B2,A3,B3 760.83 (default, best); A1,A2,A3,B1,B2,B3 748.52; B1,B2,B3,A1,A2,A3 682.25; A2,B2,A1,B1,A3,B3 642.30; A3,B3,A2,B2,A1,B1 610.40. Pathology-first beats radiology-first (attributed to the larger pathology data); report generation first is worst, VQA first best (p. 7).
- t-SNE (Fig. 3, p. 8): CR improves clustering of visual embeddings per dataset.

## 8. Limitations and future work (authors)
- Performance bounded by the foundation model; still below specifically trained models on some tasks (p. 6).
- Future work: integrate **data-incremental** learning; extend to **detection and segmentation**; natural-scene domain differences (p. 8).

## 9. Check of the author's notes
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/introduction.tex:29` | "recent studies have begun to investigate continual learning for medical foundation models" (cited with Chen 2026 and Chen 2025) | **Correct.** Continual learning on LLaVA-Med-v1.5, which the paper calls its foundation model (p. 6). Note it is a 2D LVLM for VQA/classification/report generation, not segmentation. |
| `thesis/related_work.tex` | — | **Not discussed** (no `\cite{Zhang_2025}`, no mention by name or method). If cited in Ch. 2, add it with its task-incremental, 2D, non-segmentation setting. |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
1. **Relation:** continual adaptation of a pretrained, text-conditioned medical model with per-task LoRA and task identity at inference — mechanically close to the thesis's task-specific LoRA (frozen base, one adapter per task), but branches are **summed** (1…t) rather than selected one at a time, and a parameter-space regulariser couples them.
2. **Gap claim:** does **not** weaken "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model": 2D images, no segmentation (named as future work, p. 8), not 3D, not few-shot. The text input is a free-form instruction/question, so it is evidence that continual learning of **free-text-conditioned medical models** exists in 2D generative settings; the gap should be phrased around 3D segmentation.
3. Their order ablation (Table 6) is further evidence that task order changes results strongly in medical CL; can support the thesis's two task orders.
4. No forgetting metric and no sequential fine-tuning baseline, so it cannot serve as a reference for forgetting magnitudes.
5. Bib: confirm the ACM MM '25 fields on the publisher page and add missing proceedings fields (editor, location) before final submission.
