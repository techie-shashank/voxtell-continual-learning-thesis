# Continual Learning for Abdominal Multi-Organ and Tumor Segmentation (Zhang et al.) — paper notes

Read as prior work for Ch. 2 (State of the Art): the closest work that combines continual learning for 3D medical segmentation with a language signal (fixed CLIP class embeddings conditioning class-specific heads), class-incremental, full data.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Zhang, Li, Chen, Yuille, Liu, Zhou (Johns Hopkins University). *Continual Learning for Abdominal Multi-Organ and Tumor Segmentation.* arXiv:2306.00988v2 [eess.IV], 21 Jul 2023 (PDF p. 1). 13 PDF pages: p. 1–9 paper, p. 10–11 references, p. 12–13 appendix (Tables 4–7) |
| Local PDF | `papers/t5_cl_medseg_networks/zhang2023continuallearningabdominalmultiorgan.pdf` |
| Bib key | `zhang2023continuallearningabdominalmultiorgan` (`@misc`, arXiv 2306.00988, 2023 in the bib) |
| Version read | **arXiv v2 (21 Jul 2023)**. The PDF does **not** state a peer-reviewed venue (LNCS-style layout, but no conference named). Whether a peer-reviewed version exists was not checked here; check before finalising the bib entry (CLAUDE.md: prefer the publisher version) |
| Code | github.com/MrGiovanni/ContinualLearning (p. 1) |
| Notes written | 2026-10-23, by Claude, from arXiv v2. Page numbers = PDF pages (here identical to the printed page numbers) |

## 1. Problem and idea (abstract, Sec. 1; p. 1–3)
- Extending a multi-organ/tumour segmentation model to new classes suffers from catastrophic forgetting; storing earlier data and annotations may be blocked by privacy rules (p. 1 abstract; p. 2).
- Two questions posed (p. 2): Q1 mitigate forgetting **without earlier data and annotations**; Q2 an architecture that **shares more parameters** across continual-learning steps (contrast with Ji et al., who freeze encoder/decoder and add decoders per step, p. 2, p. 6).
- Idea, part 1: **pseudo-labels** for old classes on the new data, produced by the model of the previous step (p. 2; Sec. 2.1, p. 4). The authors call this simple strategy sufficient for "reasonable performance" on old classes (p. 2).
- Idea, part 2: replace the softmax output layer by **lightweight class-specific ("image-aware organ-specific") heads** on a shared encoder–decoder; head parameters generated from the pooled image feature and a **CLIP text embedding** of the class name (Sec. 2.2, p. 4–5; Fig. 1 p. 3).
- Motivation of CLIP: embeddings carry semantics and help train new classes "with the class names known in advance" (p. 2); the authors claim the fixed-length embedding allows adaptation to open-vocabulary segmentation and novel classes (p. 5) — a claim **not tested** in the paper.

## 2. Setting (Sec. 2, p. 3–4; Sec. 3, p. 6)
- Scenario in the paper's own terms: "continual organ segmentation" over a sequence of **partially annotated datasets** D1…Dn with class sets C1…Cn; earlier datasets unavailable when training on D_t; the model must predict the **accumulated** labels of all seen steps (p. 3–4, Eq. 1–2). The introduction frames this as the class-incremental problem of Rebuffi et al. (p. 2); the paper does not explicitly label its own experiments "class-incremental".
- A **task ("learning step") = a group of new classes**, optionally from a new dataset (JHH: three class groups of one dataset; public: BTCV organs then LiTS tumour) (p. 6).
- Task identity at inference: **not needed**; one model predicts all seen classes, one head per class with sigmoid outputs (multi-label) (p. 4–5, Eq. 5).
- Not few-shot: full datasets used; number of training scans per step **not stated**.
- No earlier data stored; no replay (p. 2, Sec. 2.1).

## 3. Method (Sec. 2, p. 3–6)
- **Backbone:** Swin UNETR (Swin Transformer encoder, deconvolution decoder) (p. 4). Whether pretrained (e.g. self-supervised) weights were used is **not stated**; the paper only cites Swin UNETR's strong self-supervised pre-training as the reason for choosing it (p. 4).
- **Pseudo-labels (Eq. 3, p. 4):** for class c at step t, ground truth if c is new, the previous-step prediction Ŷ^{t−1} if c is old. The intro calls these "soft pseudo annotations" (p. 2), while Eq. 1 defines Ŷ as an **argmax** (hard) mask (p. 4) — **internal inconsistency** about soft vs hard. The proposed model is trained with pseudo-labelling only, "without any other distillation or regularization" (p. 4; repeated p. 7).
- **Class-specific heads (Eq. 4–5, p. 5):** GAP of the last encoder features → per-class MLP_k → parameters θ_k of a short convolutional head applied to decoder features → sigmoid; binary cross-entropy per class.
- **Text-driven parameter generation (Eq. 6, p. 5):** θ_k = MLP_k([GAP(E(X)), ω_k]), ω_k = CLIP text embedding of a medical prompt template, e.g. "a computerized tomography of a [CLS]" (p. 5). CLIP text encoder pre-trained and used only to produce embeddings (p. 5; Fig. 1 caption "calculated using the pre-trained CLIP model"); whether it is fine-tuned is not stated, but the embeddings are described as fixed-length (p. 5).
- **Difference from the CLIP-Driven Universal Model (Liu et al.):** one independent MLP per class instead of one shared MLP, to reduce interference between classes (p. 5).
- Trained vs frozen during continual steps: **not explicitly stated**. The design is described as a "single backbone" with shared encoder and decoder (p. 2) and contrasted with frozen-encoder approaches (p. 2, p. 6); new heads are added per new class (p. 6).
- **Complexity (Sec. 2.3, p. 6):** 661.6 GFLOPs vs Swin UNETR 659.4 GFLOPs; each new head 0.12 GFLOPs; Swin UNETR decoder alone 466.08 GFLOPs, which the Ji et al. design would add per step. ILT and PLOP "double the FLOPs" by running the old model (p. 6). (Note: the paper glosses FLOPs as "floating-point operations per second", p. 6.)

## 4. Data (Sec. 3, p. 2 and p. 6)
- **JHH (in-house, Johns Hopkins Hospital), abdominal CT, 3D:** 200 scans with per-voxel labels for 13 organs, three gastrointestinal tracts and four cardiovascular structures (footnote 1, p. 2). Not public. Splits **not stated**.
  - Step 1: 7 abdominal organs — spleen, right kidney, left kidney, gall bladder, liver, postcava, pancreas.
  - Step 2: 3 gastrointestinal classes — stomach, colon, intestine.
  - Step 3: 4 "other organs" — aorta, portal vein and splenic vein, celiac trunk ("celiac truck" in the paper), superior mesenteric artery (p. 6). Grouping follows TotalSegmentator (p. 6). Tables label this group "JHH_cardiac" (Tables 1, 3, 6).
  - **Inconsistency:** the introduction says step 1 on the private dataset segments **13 organs** (p. 3), Sec. 3 says **seven** classes (p. 6), and the tables say JHH_organ (7).
- **BTCV, abdominal CT, 3D:** 47 CT images with 13 organs (p. 6). Step 1: spleen, right kidney, left kidney, gall bladder, oesophagus, liver, stomach, aorta, inferior vena cava, portal vein and splenic vein, pancreas, right adrenal gland, left adrenal gland (p. 6).
- **LiTS, contrast-enhanced abdominal CT, 3D:** 130 scans for liver and liver tumour; only **liver tumour** is learned in step 2 (p. 6).
- Task orders: JHH organs → gastro → cardiovascular; BTCV → LiTS. A single order per setting; other orders **not tested**.
- Train/validation/test splits, preprocessing, and the number of test scans: **not stated**.

## 5. Implementation (Sec. 3, p. 7–8)
- Heads: three convolution layers, 8, 8 and 1 kernels (p. 7).
- All models: AdamW, **100 epochs**, cosine learning-rate schedule, batch size 2, patch 96 × 96 × 96, initial learning rate 1e-4, weight decay 1e-5 (p. 7). Whether 100 epochs is per step is not stated.
- MONAI 1.1.0; NVIDIA TITAN RTX and Quadro RTX 8000 GPUs (p. 8). Runtime and memory: not reported.
- All compared methods use the same Swin UNETR backbone (p. 6). Hyperparameters of LwF, ILT, PLOP: not stated.
- Number of runs/seeds, variability: **not stated**; single numbers only.

## 6. Evaluation protocol and metrics (Sec. 3, p. 6–7)
- Metric: Dice (DSC), reported as fractions in [0, 1] (p. 7, Tables 1–7).
- At each step, the mean DSC of the current-step classes and of each earlier group is reported separately (p. 7): old-class DSC = retention, current-class DSC = learning of new classes.
- No forgetting/BWT/FWT metric, no joint-training upper bound, no sequential fine-tuning row in the tables. The step-1 row of Table 4/7 labelled "Swin UNETR" is the plain backbone before continual learning. A preliminary experiment states plain fine-tuning "will totally forget the old classes" (p. 4), without numbers.
- Baselines: LwF (prediction distillation, here equated with pseudo-labelling, p. 8), ILT (feature distillation), PLOP (multi-scale pooled feature distillation) (p. 3, p. 7).
- Ablation (Table 3): LwF baseline, heads with one-hot class embeddings ("Ours_1-hot"), full method ("Ours_CLIP") (p. 8).

## 7. Results (Tables 1–3, p. 8–9; appendix Tables 4–7, p. 12–13; DSC in [0, 1])
- **Table 1 (JHH, p. 8):** columns JHH_organ (7) step 1 / 2 / 3 | JHH_gastro (3) step 2 / 3 | JHH_cardiac (4) step 3:
  - LwF 0.891 / 0.777 / 0.767 | 0.530 / 0.486 | 0.360
  - ILT 0.891 / 0.775 / 0.776 | 0.653 / 0.480 | 0.484
  - PLOP 0.891 / 0.780 / 0.777 | 0.427 / 0.464 | 0.318
  - Ours 0.887 / 0.783 / 0.787 | 0.695 / 0.692 | 0.636
  - Ours is lower than the baselines in step 1 (0.887 vs 0.891), best everywhere else.
- **Table 2 (public, p. 8):** BTCV (13) step 1 / step 2 | LiTS (1) step 2:
  - LwF 0.828 / 0.770 | 0.456; ILT 0.828 / 0.786 | 0.335; PLOP 0.828 / 0.799 | 0.362; Ours 0.860 / 0.817 | 0.466.
- **Text claims (p. 8):** pseudo-labelling alone (LwF) keeps old classes reasonably (0.777 step 2, 0.767 step 3 on JHH organs; 0.770 BTCV step 2); the proposed method is best "in most learning steps", with the least forgetting and better adaptation to new classes.
- **Ablation, Table 3 (p. 9):** LwF 0.891 / 0.777 / 0.767 | 0.530 / 0.486 | 0.360; Ours_1-hot 0.882 / 0.767 / 0.777 | 0.674 / 0.665 | 0.452; Ours_CLIP 0.887 / 0.783 / 0.787 | 0.695 / 0.692 | 0.636.
  - Text: heads improve gastro by 0.144 (step 2) and 0.179 (step 3); CLIP adds 0.019 (step 2) and 0.027 (step 3) (p. 8).
  - **Inconsistency (own calculation):** from Table 3, CLIP − 1-hot for gastro step 2 = 0.695 − 0.674 = **0.021**, not 0.019. The other three differences match (0.144, 0.179, 0.027).
  - Own observation: on JHH organs in step 2 the 1-hot heads (0.767) are below LwF (0.777); the gain of the heads is concentrated on the newer groups.
- **Class-wise (appendix):** gall bladder drops from 0.806 (step 1, Ours_clip) to 0.453 (step 2) and pancreas from 0.843 to 0.555 (Table 4, p. 12); intestine is 0 for PLOP (step 2) and for LwF, ILT, PLOP (step 3) (Table 5, p. 12); celiac trunk 0 for LwF, PLOP, Ours_1-hot and SMA 0 for PLOP (Table 6, p. 12). Table 7 (p. 13) lists BTCV classes only; the LiTS tumour value is only in Table 2.
- **Qualitative (Fig. 2, p. 7; text p. 9):** the proposed method segments the correct organs where ILT (called the best baseline) fails.

## 8. Limitations stated by the authors
- **None stated.** The paper has no limitations or future-work section (Conclusion, p. 9).

## 9. Check of the author's notes
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:85` | "combine partial isolation with language in a **class-incremental** Swin UNETR model" | **Partly correct.** Swin UNETR backbone (p. 4) and class-specific heads (p. 5) correct. "Class-incremental": the intro frames the problem with Rebuffi's class-incremental definition (p. 2), and the setting (new classes per step, predict all seen classes, Eq. 1–2) matches it, but the paper does not explicitly name its scenario. |
| `thesis/related_work.tex:85` | "whose shared backbone **continues to be fine-tuned**" | **Partly correct / not explicitly stated.** The paper says single backbone, shared encoder and decoder (p. 2) and contrasts with frozen-encoder designs (p. 2, p. 6), which implies training, but never states which parameters are updated in later steps. Soften or mark as inferred. |
| `thesis/related_work.tex:85` | "MLP layers map the globally pooled encoder features, concatenated with a fixed CLIP embedding of the class, to class-specific convolution kernels, which are applied to the decoder features to produce the mask of that class" | **Correct** (Eq. 4–6, p. 5; Fig. 1 p. 3). Add that there is **one independent MLP per class**, the stated difference from the Universal Model (p. 5). |
| `thesis/related_work.tex:85` | "As in the CLIP-Driven Universal Model" | **Correct** (inspired by Liu et al., p. 2, p. 5), with the per-class-MLP difference (p. 5). |
| `thesis/related_work.tex:85` | "**Soft** pseudo-labels from the model of the preceding task supervise the earlier classes, so no earlier scans are stored" | **Partly correct.** Previous-step predictions as labels for old classes, no stored data: correct (Eq. 3, p. 4; p. 2). "Soft" is the paper's wording on p. 2, but Eq. 1 defines Ŷ as an argmax mask (p. 4); the paper is inconsistent. Safer: "pseudo-labels". |
| `thesis/related_work.tex:85` | "on two abdominal CT sequences the method reported higher DSC than LwF, ILT, and PLOP for both earlier and new classes" | **Mostly correct.** True for all continual steps (Tables 1–2), but not for JHH step 1 (0.887 vs 0.891, Table 1); the paper itself says "in most learning steps" (p. 8). Also note: the paper has **three** datasets / two settings (JHH in-house; BTCV → LiTS). |
| `thesis/related_work.tex:85` | "the class embeddings are fixed and the class names must be known in advance … remains bound to a closed output set" | **Partly correct; interpretation.** "Class names known in advance" (p. 2) and per-class MLPs (p. 5) are in the paper. "Closed output set" is the author's interpretation; the paper **claims the opposite** (fixed-length CLIP embedding "allows us to adapt … to open-vocabulary segmentation", p. 5), though it does not test it. State that the claim is untested and each new class needs its own trained head. |
| `thesis/related_work.tex:115` | "Zhang et al. condition continual segmentation on fixed class embeddings rather than free text" | **Correct** (CLIP embedding of a template prompt with the class name, p. 5). |
| `thesis/related_work.tex:208` (summary table) | Data "200 in-house CT scans; BTCV → LiTS" | **Correct but incomplete** (200 JHH scans, footnote p. 2; BTCV 47, LiTS 130, p. 6). Could add the sizes. |
| `thesis/related_work.tex:208` | Approach "CIL; CLIP-conditioned kernels, soft pseudo-labels" | **Partly correct** (see "class-incremental" and "soft" above). |
| `thesis/related_work.tex:208` | Result "DSC 81.7 % (old), 46.6 % (tumour)" | **Numbers correct, form differs.** Table 2 (p. 8): BTCV step 2 0.817, LiTS 0.466 — the paper uses [0, 1], not %. CLAUDE.md: values quoted from a paper keep the paper's form, so write 0.817 / 0.466. Also state these are the BTCV → LiTS setting. |
| `thesis/related_work.tex:232` (positioning table) | Language "fixed CLIP class embeddings"; 3D FM "no"; few-shot "no"; CIL; "Proposed method, LwF, ILT, PLOP" | **Mostly correct.** Few-shot no (full data); baselines correct (p. 7). 3D FM: Swin UNETR is not a foundation model, but whether pretrained weights were used is **not stated** (p. 4). CIL: see above. |
| `thesis/introduction.tex` | — | **Not found** (no citation of this paper in the introduction). |
| `% SUMMARY TABLE` comment (`related_work.tex:100–106`) | — | **Not found** (no entry for this paper). |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
Thesis setting (from `gonzalez2023lifelong.md` §10 and CLAUDE.md): continual adaptation of the pretrained free-text promptable universal 3D model VoxTell to six tasks (structures, one text prompt each) of one MRI dataset (SKM-TEA), few-shot, original and reverse task orders, with a held-out control task.
1. **Relation to this thesis:** closest prior work combining continual 3D segmentation with language. Differences: language enters only as a **fixed CLIP embedding of a class-name template**, not as free text processed by the segmentation model; one head and MLP per class is added (partial parameter isolation); the model is not a pretrained universal model whose pretrained ability is protected; full data, CT only, one order per setting; no forgetting metric, no joint/sequential reference, no seeds.
2. **Gap claim:** does **not** weaken "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model", provided the thesis states the distinction precisely: the prompt is a fixed class-name template and each class has its own head, so the model is class-conditioned, not free-text promptable. An examiner could argue it is "text-conditioned continual 3D segmentation"; the defence is (a) no free text, (b) no pretrained promptable model, (c) not few-shot.
3. Their claim of open-vocabulary extensibility (p. 5) is untested; the thesis should not repeat it as a finding.
4. Supporting point for the thesis: pseudo-labelling of old classes needs old classes annotated in the new data's output space; in the thesis each task is a single structure with its own prompt, so the class-wise heads idea has no direct analogue, but the "no stored data" constraint motivates the replay-free strategies.
5. Bib: entry is the arXiv version; check whether a peer-reviewed version (e.g. a MICCAI 2023 workshop/conference paper) exists before submission — not verified here.
6. The ablation-text inconsistency (0.019 vs 0.021) and the 13-vs-7 class inconsistency should not be quoted from the text; use the tables.
