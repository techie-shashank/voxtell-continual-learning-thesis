# MedCRP-CL — paper notes

Read as prior work for Ch. 2 (State of the Art): the closest work found so far to this thesis, a continual-learning method for a pretrained **text-promptable vision–language segmentation model (CLIPSeg)** on medical images. It is checked here mainly against the gap claim in `thesis/related_work.tex:117`.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Ziyuan Gao (single author, University College London). *MedCRP-CL: Continual Medical Image Segmentation via Bayesian Nonparametric Semantic Modality Discovery.* arXiv:2605.20297v2 [cs.CV], 4 Aug 2026. 19 pages (main text p. 1–9, references p. 10–12, appendix A–H p. 13–19) |
| Venue | The first-page footnote states *Proceedings of the 43rd International Conference on Machine Learning*, Seoul, South Korea, PMLR 306, 2026 (p. 1). Not checked against the PMLR site; if a PMLR page exists, cite that instead of arXiv |
| Local PDF | `papers/t6_cl_medseg_foundation/NEW_medcrpcl2026.pdf` (text: `papers/text/NEW_medcrpcl2026.txt`, legacy encoding, tables garbled) |
| Bib key | **none yet** (not in `thesis/literature.bib`) |
| Version read | **arXiv v2 (4 Aug 2026)**, ICML camera-ready template. No supplement besides the appendix in the same PDF |
| Code | github.com/zygao930/MedCRP-CL (abstract, p. 1); not inspected |
| Notes written | 2026-10-23 by Claude from the arXiv v2 PDF. Locators are PDF page numbers plus section, table, figure or equation. Tables 1–3, 5, 8, 9, 11, 12, 14–16 were checked on the PDF page images (p. 5–9, 16–18) because the text extraction is garbled |

## 1. Problem and idea (abstract and introduction; p. 1–2)
- Setting as the author frames it: segmentation data arrive sequentially from heterogeneous clinical sources (e.g. chest X-ray, ultrasound, endoscopy), and the model must learn new tasks without losing earlier ones (p. 1). Vision–language segmentation models guided by natural-language prompts are named as promising, with their use in continual learning described as "largely unexplored" (p. 1, citing CLIPSeg and Zhao et al. 2025).
- Tension identified: uniform constraints (EWC) cause forgetting when tasks conflict; mixture-of-experts needs a predefined expert count; physical modality labels (e.g. "ultrasound") are too coarse, since cardiac and breast ultrasound differ in anatomy and pathology (p. 1–2).
- Idea: group tasks online into **"semantic modalities"** by clustering the CLIP text embeddings of the tasks' clinical text prompts with a **Chinese Restaurant Process (CRP)** prior and an adaptive likelihood; one LoRA adapter per semantic modality, regularised by EWC only within the modality (p. 2, Fig. 1–2).
- Replay-free; only aggregate statistics (centroids, Fisher values, Gaussian similarity statistics) are stored (abstract; p. 2).
- Stated contributions (p. 2): (1) Bayesian nonparametric semantic-modality discovery from clinical text prompts; (2) modality-specific LoRA + intra-modality EWC; (3) results on 16 tasks across four imaging types: 73.3 % Dice, 4.1 % forgetting, +8.0 over the best baseline, 6× fewer parameters than MoE-Adapters.

## 2. Setting (Sec. 3 "Problem Formulation", p. 3; Sec. 4.1, p. 5–6; App. D, p. 16)
- **Task** = one dataset or one dataset subset with one target (e.g. Kvasir polyps, CAMUS left ventricle, BUSI-Benign, one CheXlocalize pathology), 16 tasks in total (Table 1 p. 5; App. B p. 14). Each task's data are triples (image, mask, clinical text prompt) (p. 3).
- **Scenario name:** not given in the paper (no TIL/CIL/DIL label).
- **Task identity at inference: not stated.** The paper describes how a task is assigned to a semantic modality during training (Eq. 6–8, Algorithm 1, p. 4–5) but never says which LoRA adapter is applied when a test image is segmented. Since assignment is computed per task from the set of the task's prompts (Eq. 3) and stored as z(t), the evaluation most likely applies the adapter z(t) of the known task, i.e. task-aware selection, but this is an inference, not stated. The text calls the mechanism routing ("route tasks to appropriate experts", p. 6 and p. 8). Test-time assignment of a single unseen prompt is not described.
- Sequential, no replay, no data of earlier tasks stored (p. 2–3).
- **Not few-shot.** All training images of each task are used (Table 1 p. 5; train splits 25–960 images); the words "few-shot" or "shot" do not appear. The smallest training sets are small (Edema 25, Cardiomegaly 35, Pleural Effusion 39 images), but this is not framed as a few-shot protocol.
- **Four task orders** (Table 11, p. 16): grouped (by semantic modality), reversed (reverse of grouped), interleaved (alternating modalities), mixed (randomised). Main per-task table uses the interleaved order (Table 3, p. 7).

## 3. Method (Sec. 3, p. 3–5; Algorithm 1 p. 5)
- **Backbone: CLIPSeg** (Lüddecke & Ecker 2022), a 2D text-and-image-promptable segmentation model built on CLIP, kept frozen (p. 4 "Dynamic Semantic Modality-Specific LoRA"; p. 6 "Implementation Details"). Whether the CLIPSeg weights are the original general-domain release or a medically fine-tuned checkpoint (e.g. from MedVLSM) is **not stated**.
- **Trainable parameters:** LoRA (rank 8, α = 16) on query, key, value and output projections in **both vision and text encoders**; backbone fixed (p. 6). Whether the CLIPSeg decoder is trained is **not stated**. Trainable parameters 8.6 M in total (Table 2, p. 6).
- **Modality discovery** (Sec. 3.1, p. 3–4):
  - Task embedding e_t = mean of the L2-normalised CLIP text embeddings of the task's unique prompts (Eq. 3). Embeddings come from the frozen CLIP text encoder before any LoRA (p. 6).
  - CRP prior P(z_t = k) ∝ n_k (existing modality) or α (new modality), normalised by t − 1 + α (Eq. 2); α = 5.0 (p. 6).
  - Similarity s_{t,k} = ⟨e_t, μ_k⟩ with running centroid μ_k (Eq. 4, not renormalised, p. 3).
  - Likelihood: log-likelihood ratio of two Gaussians for same-modality vs different-modality similarity, statistics updated online with Welford's algorithm, σ_min = 0.05 (Eq. 5, p. 4). Cold start: logit of the similarity (p. 4; App. E.1 p. 17).
  - MAP assignment over existing modalities and "new" (Eq. 6–8, p. 4). Proposition A.1 gives a consistency guarantee under a separation condition (App. A, p. 13).
- **Modality-specific LoRA:** W_k = W_0 + B_k A_k per semantic modality; a new (A_k, B_k) pair is allocated for a new modality (Eq. 9, p. 4). Parameters are isolated across modalities and shared within one.
- **Intra-modality EWC:** Fisher per task (Eq. 10), consolidated per modality by a running average (Eq. 11), quadratic penalty to the anchor parameters of that modality only (Eq. 12, p. 5); λ = 5000, 200 samples for the Fisher estimate (p. 6). Proposition A.2 bounds forgetting by within-modality tasks only (App. A, p. 13).
- **Loss:** L = L_CE + L_Dice + Ω_{z(t)}, with Ω = 0 for the first task of a modality (Eq. 13, p. 5).
- Pseudocode: Algorithm 1 (p. 5). No complexity analysis.

## 4. Data (Sec. 4.1 "Datasets", p. 5; Table 1 p. 5; App. B p. 14; App. C p. 15)
- **All 2D images**; all resized to 352 × 352 (p. 6). Four imaging types, five anatomical regions (p. 5). No 3D data; 3D is named only as a promising direction in related work (p. 2).
- **Table 1 (p. 5), train/val/test images per task:**
  - Endoscopy, colon: Kvasir 800/100/100; ClinicDB 490/61/61; ETIS 137/39/20; CVC-300 64/21/23; ColonDB 266/76/38
  - Dermoscopy, skin: ISIC 810/90/379
  - Ultrasound, heart: CAMUS 960/120/120; breast: BUSI-Benign 349/44/44, BUSI-Malignant 168/21/21
  - X-ray, chest (CheXlocalize subsets): Airspace Opacity 75/17/33; Atelectasis 48/9/23; Cardiomegaly 35/14/19; Edema 25/9/11; Pleural Effusion 39/10/18; Enlarged Cardiomediastinum 57/18/34; Support Devices 59/17/31
  - Total over the 16 tasks: **6,023 images** (own calculation from Table 1).
- **Text prompts** (p. 5; App. C Table 10 p. 15): "adopted from MedVLSM (Poudel et al., 2024)", i.e. written by a third party (MedVLSM), not by the author or a clinician. Two versions per dataset:
  - *Concise*: class-name-like phrases, e.g. "round polyp", "circle skin melanoma", "Edema in a chest Xray.", "Benign tumor in the breast ultrasound image." (Table 10).
  - *Detailed*: sentence-like descriptions with per-image attributes such as count, size, colour, shape, position in the image, view, cardiac phase, patient age and sex, image quality, and co-present findings (e.g. CAMUS: "Left ventricular cavity of oval shape in four-chamber view in the cardiac ultrasound at end of the diastole cycle of a 18-year-old male with good image quality.", Table 10 p. 15).
  - Prompts are per image (p_i^t in each triple, p. 3), and CLIPSeg is text-conditioned, so a prompt is input at both training and inference; **which of the two prompt versions was used for segmentation training and evaluation in the main results is not stated.** Fig. 1–2 show detailed prompts. Prompt robustness is evaluated only for the clustering (number of discovered modalities K), not for segmentation Dice (Sec. 4.4, p. 9; Table 9; App. G p. 19).
- **Inconsistencies in the data description** (own comparison of Table 1 with App. B):
  - (a) CheXlocalize is described as having "bounding box annotations" (App. B, p. 14), yet is used for segmentation with masks; how masks were obtained is not stated. The cited reference is the CheXpert paper (Irvin et al., 2019).
  - (b) CVC300 is described as 60 cases (App. B), Table 1 sums to 108 images.
  - (c) CAMUS is described as 6,000 images (App. B), Table 1 uses 1,200; the subset selection is not stated.
  - (d) BUSI is 780 images (App. B), Table 1 uses 437 + 210 = 647 (normal images presumably excluded; not stated).
  - (e) CheXlocalize is 2,177 radiographs (App. B), the seven subsets sum to 601; selection not stated.
  - (f) The split procedure (how train/val/test were drawn) is not described.

## 5. Implementation (Sec. 4.1 "Implementation Details", p. 6)
- AdamW, learning rate 1 × 10⁻³, weight decay 8 × 10⁻⁵; up to 60 epochs per task, early stopping with patience 8 and minimum 15 epochs; batch size 16; one NVIDIA RTX 4090 (p. 6).
- Table 2 (p. 6) reports trainable parameters, peak GPU memory and time relative to MedCRP-CL (see Sec. 7).
- Number of seeds/runs: **not stated**. Table 2 reports mean ± std; Fig. 3's caption says shaded regions are std "across orderings" (p. 6), so the ± in Table 2 is probably over the four task orders, but this is not stated for Table 2.
- Hyperparameter selection procedure: not stated.

## 6. Evaluation protocol and metrics (Sec. 4.1 "Metrics", p. 5–6)
- **Average Dice** over the T tasks (Eq. 14), evaluated after the whole sequence (Table 2/3 captions).
- **Average Forgetting Rate** FR = mean over the first T − 1 tasks of (Dice_peak − Dice_final), where Dice_peak is "the best validation performance on task i observed immediately after training on that task" (Eq. 15, p. 5–6). Negative values = backward transfer (Fig. 3 caption, p. 6). (Own note: this is close to Chaudhry's final forgetting, but with the peak defined as the value right after training the task, not the maximum over all earlier steps; the peak is taken on validation data while Dice_final is presumably test; not stated.)
- **Reference points:** "Individual" models trained separately per task, called the upper bound (p. 6); "Sequential" fine-tuning without forgetting mitigation (p. 6). No joint-training reference.
- **Loss of pretrained ability: not measured.** No zero-shot evaluation of the frozen CLIPSeg, no held-out control task or unseen prompts after the sequence, and no forward-transfer metric. The "w/o LoRA" ablation (frozen backbone, 45.39 % Dice, Table 4 p. 8) is the closest to a pretrained-model reference row.
- Efficiency: trainable parameters (M), peak GPU memory (GB) and relative time (Table 2).

## 7. Results
- **Table 2 (p. 6), mean over task orders (presumably), Dice % / Forgetting % / Params M / GPU GB / Time:**
  - Individual 77.9 / – / 19.8 / 12.4 / –
  - Sequential 48.0 ± 7.1 / 28.3 ± 7.7 / 1.2 / 5.8 / 0.7×
  - EWC 56.8 ± 3.7 / 11.3 ± 3.5 / 1.2 / 5.8 / 0.9×
  - RAPF 58.4 ± 1.7 / 7.2 ± 2.6 / 0.9 / 5.6 / 0.8×
  - CL-LoRA 60.7 ± 2.0 / 9.7 ± 1.4 / 0.05 / 5.7 / 1.5×
  - MoE-Adapters 65.3 ± 3.4 / 7.1 ± 3.2 / 51.9 / 13.3 / 1.2×
  - MedCRP-CL 73.3 ± 1.0 / 4.1 ± 0.8 / 8.6 / 12.4 / 1.0×
- The "+8.0 %" (abstract, p. 6) is 73.3 − 65.3 percentage points; "6×" is 51.9 / 8.6 ≈ 6.0 (own calculation). The text calls the improvement "significantly outperforming" (p. 6) without a statistical test.
- **Baselines** (p. 6): EWC (λ = 5000), RAPF, CL-LoRA, MoE-Adapters (K = 16 experts, activate-freeze), Sequential fine-tuning, Individual. How each baseline was adapted from CLIP classification to CLIPSeg segmentation and which parameters each trains is not described (Sequential and EWC have 1.2 M trainable parameters, so they do not train the full model; what they train is not stated). No replay baseline (argued impractical for privacy, p. 2), no distillation baseline besides CL-LoRA's knowledge distillation (p. 6), no prompt-tuning baseline, no task-specific (per-task) LoRA baseline except the "Individual" models.
- **Table 3 (p. 7), interleaved order, average over 16 tasks:** Dice — Individual 77.9, Sequential 52.2, EWC 55.5, RAPF 60.4, CL-LoRA 62.4, MoE-Adapters 67.7, MedCRP-CL 72.2. Forgetting — Sequential 23.9, EWC 14.1, RAPF 8.8, CL-LoRA 8.4, MoE-Adapters 6.6, MedCRP-CL 4.2. MedCRP-CL is below the best baseline on several chest X-ray and breast tasks (e.g. BUSI Ben. 51.7 vs MoE 72.2; Airspace Op. 62.2 vs MoE 70.2).
- **Per-order results for MedCRP-CL (App. F, Tables 14–16, p. 18):** grouped 74.2 / 3.4; mixed 72.7 / 5.1; reversed 73.6 / 3.9; interleaved (Table 3) 72.2 / 4.2 (Dice / FR %). Text: Dice 0.72–0.74, forgetting 0.04–0.06 for MedCRP-CL; MoE-Adapters 0.62–0.70 Dice, 0.11–0.16 forgetting (p. 6, Fig. 5 p. 7). Only MedCRP-CL and MoE-Adapters are shown per order.
- **Ablations (Table 4, p. 8):** full 73.33 / 4.09; w/o EWC 71.92 / 5.41; w/o CRP (one shared LoRA + EWC) 57.59 / 15.55; "Single LoRA" (no CRP, no EWC) 46.94 / 27.34; w/o LoRA 45.39 / 0.03 (Dice / Forgetting %).
- **Loss ablation (Table 5, p. 8):** L_Seg 70.27 / 4.97 / K 4–6; L_Seg + L_EWC 71.87 / 3.66 / 5; L_Seg + L_Dice 72.41 / 5.25 / 5–6; all three 73.33 / 4.09 / 5.
- **Physical vs discovered grouping (Table 6, p. 8):** physical imaging type (K = 4) 65.75 / 9.23; CRP (K = 5) 73.33 / 4.09. CRP separates cardiac (CAMUS) from breast (BUSI) ultrasound (p. 8). Fisher-weighted merging of any two of the five adapters degrades performance for all 10 pairs, by −0.016 to −0.395 (Table 18, p. 19).
- **Text vs visual clustering (Table 7, p. 9):** text embeddings intra 0.95+, inter 0.45, gap ~0.50, K = 5; visual embeddings intra 0.95+, inter 0.73, gap ~0.22, K = 1–4.
- **Encoder choice (Table 8, p. 9):** CLIP and 9 other contrastive text encoders give K = 5 at α = 5 except as noted below; SigLIP and S-PubMedBERT give K = 1 at all α (p. 9).
- **Prompt perturbations (Table 9, p. 9; App. G p. 19):** abbreviations, 10–20 % typos, 20–30 % keyword drop and word shuffle keep K = 5; 30 % typos give K = 3; 50 % keyword drop and a generic prompt ("segment the region.") give K = 1. Effect on Dice not reported.
- **Inconsistencies in the results:**
  - (a) Table 2 Dice of MedCRP-CL (73.3) is not the mean of the four per-order values (74.2, 72.7, 73.6, 72.2 → 73.2; own calculation); forgetting fits (4.15). The ± of 1.0 does not match the std of these four values either (0.78 population, 0.90 sample; own calculation). Table 2 may come from different runs; not stated.
  - (b) The section heading says "Interleaved Task Order" while the body says Table 3 shows the "mixed" sequence (p. 7); the Table 3 order matches "interleaved" in Table 11.
  - (c) The reversed order in Table 16 (Pleural Eff. second-to-last) differs from Table 11 (CheX-Pleural fourth). Table 12 (p. 17) lists as "Task 1" what is the second task of each order in Table 11; e.g. reversed "Task 1" BUSI-B. "JOIN-M0", which is only possible if a task came before.
  - (d) Table 8 caption says all 10 encoders give K = 5 at α = 5, but BiomedCLIP gives K = 2 at α = 5 (Table 8, p. 9). The claim that the default CLIP keeps K = 5 over the widest α range ties with PubMedCLIP (5 at all four α).
  - (e) "w/o EWC" in Table 4 (71.92 / 5.41) and L_Seg + L_Dice in Table 5 (72.41 / 5.25) describe the same configuration with different numbers. Eq. 13 names L_CE, Table 5 names L_Seg.
  - (f) Fig. 5 text gives MedCRP-CL forgetting 0.04–0.06 across orders, but the grouped order has 3.4 % (Table 14).
  - (g) App. A uses μ_inter ≈ 0.51, App. E.2 reports final inter means 0.429–0.473, Table 7 0.45.
  - (h) "w/o LoRA" with a frozen backbone gives forgetting 0.03, not 0; what is trained in this configuration is not stated.

## 8. Limitations and future work (authors)
- No limitations section. The Impact Statement says clinical deployment would need prospective validation and regulatory approval (p. 9–10).
- 3D volumetric settings are mentioned only as a promising direction for continual segmentation in related work (p. 2).
- The method needs text encoders trained with contrastive objectives (p. 9).
- Not stated by the authors (own observation): single-image 2D data only, tasks are mostly separate datasets (shift in both appearance and target), no measure of pretrained ability, no seeds, baselines' adaptation to segmentation undocumented.

## 9. Check of the author's notes (the paper is not cited yet; sentences it contradicts or that need rewording)
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:117` | "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model" | **Still literally true, but only because of "3D"** (and arguably "free-text"). MedCRP-CL continually adapts a pretrained text-promptable vision–language segmentation model (CLIPSeg) on medical images with sentence-like clinical prompts, but on 2D images, full data, without few-shot. An examiner who knows this paper will see the claim as hinging on "3D"; reword (see Sec. 10). |
| `thesis/related_work.tex:117` | "consequently no work has examined how established continual-learning strategies trade off in this setting" | **Needs narrowing.** MedCRP-CL compares EWC, RAPF, CL-LoRA, MoE-Adapters, sequential fine-tuning and individual models on a text-promptable segmentation model (Table 2–3), i.e. established strategies on a promptable model, though 2D, full-data, and as baselines for a new method rather than as a systematic comparison. |
| `thesis/related_work.tex:115` | CL for vision–language models was "developed almost exclusively for two-dimensional classification" | **Still defensible ("almost")**, but MedCRP-CL is a counterexample (VLM continual learning for 2D segmentation) and should be named here or in Sec. 2.2/2.3. |
| `thesis/related_work.tex:115` | "The works closest to the present study each cover only part of its setting: Zhang et al. ..., MedSeqFT ..., Chen et al. ..." | **Incomplete.** MedCRP-CL is closer than Zhang et al. in the language dimension (sentence-like prompts with a frozen pretrained text-promptable model vs fixed class embeddings) and should be added to this list: it covers the promptable pretrained model, but not 3D, not few-shot, and not loss of pretrained ability. |
| `thesis/related_work.tex:94` | "A free-text promptable model has no inherent selection step ... Dedicated components can therefore be added to such a model only if task identity is supplied at inference or a routing decision is introduced" | **Consistent, and MedCRP-CL is an example** of the routing option (assignment of tasks to modality adapters from prompt embeddings). Its test-time selection is not described in the paper, so do not claim it uses task identity or per-input routing. |
| `thesis/related_work.tex:64` and tables (MoE-Adapters, RAPF) | — | No conflict. Note that MedCRP-CL reports MoE-Adapters, RAPF and CL-LoRA on medical segmentation (Table 2), the only such numbers found so far; usable as evidence that these VLM-CL methods were transferred to segmentation. |
| `thesis/related_work.tex:224–238` (positioning table) | Closest prior work: Lifelong nnU-Net, Zhang et al., MedSeqFT, Chen et al. | **Missing row.** Suggested row (own wording): MedCRP-CL — Language: clinical text prompts (MedVLSM; concise and detailed); 3D FM: no (2D CLIPSeg, frozen); Few-shot: no; Setting: not named (task-wise modality adapters; test-time selection not stated); Strategies: proposed method, sequential fine-tuning, EWC, RAPF, CL-LoRA, MoE-Adapters, individual models. The table caption's "3D FM" column would then make the distinction visible; consider adding a "Pretrained promptable" or "Data dim." column. |
| `thesis/related_work.tex:134–216` (summary table) | — | **Missing row.** Suggested: MedCRP-CL — 16 2D tasks (endoscopy, dermoscopy, ultrasound, chest X-ray), 6,023 images — CRP grouping of tasks by prompt embedding, modality-specific LoRA + intra-modality EWC on frozen CLIPSeg — Dice 73.3 %, forgetting 4.1 % (MoE-Adapters 65.3 %). |
| `thesis/introduction.tex` (not checked line by line) | Any sentence repeating the gap claim | Check for the same wording; apply the same rewording. |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
1. **Relation to this thesis.** This thesis studies VoxTell, a pretrained free-text promptable 3D universal segmentation model, adapted sequentially to six tasks (target structures of SKM-TEA knee MRI, one text prompt each) in two task orders (original, reverse), with k-shot support sets, and compares sequential fine-tuning, task-specific LoRA (task-aware inference), shared LoRA, shared LoRA + replay, the distillation-based strategy (adapted from ZSCL) and the prompt-tuning strategy (adapted from CPE-CLIP), measuring Adaptation, Final Forgetting and the drop on a held-out control task (AeroPath, "lung"). MedCRP-CL shares the core element "continual adaptation of a pretrained text-promptable segmentation model on medical images", but differs on every other axis:
   - (a) **Prompts:** clinical text prompts from MedVLSM, per image, in a concise (class-name-like phrase) and a detailed (sentence with per-image attributes) version; written by a third party, not by clinicians or the author; used at inference by CLIPSeg; which version was used for segmentation is not stated. So "free-text" applies at most to the detailed version, and these are template-generated descriptions rather than open free text. Prompt-wording sensitivity is tested only for the clustering.
   - (b) **Data:** 2D only (endoscopy, dermoscopy, ultrasound, chest X-ray), 352 × 352, 6,023 images over 16 tasks; no volumes.
   - (c) **Backbone:** CLIPSeg, a general 2D vision–language segmentation model (medical pretraining not stated), frozen; LoRA in both encoders trained (one adapter per discovered modality). Not a 3D universal medical model.
   - (d) **Scenario:** tasks are datasets or dataset subsets with mostly different targets and appearance; scenario unnamed; test-time adapter selection not described (probably by the task's stored modality assignment, i.e. effectively task-aware; unverified).
   - (e) **Full data**, not few-shot.
   - (f) Forgetting via peak-minus-final Dice (Chaudhry-like); **no measure of loss of pretrained ability** (no control task, no zero-shot evaluation after adaptation, no forward transfer).
   - (g) Baselines: sequential fine-tuning, EWC, RAPF, CL-LoRA, MoE-Adapters, individual models; no replay, no ZSCL-style distillation, no prompt tuning, no shared vs task-specific LoRA comparison as such (the ablations "Single LoRA" and "w/o CRP" are close to shared LoRA; "Individual" is not a per-task LoRA).
2. **Verdict on the gap claim.** The claim at `related_work.tex:117` is **not falsified** but is **weakened**: it now rests on "3D" (and, less firmly, on "free-text"), not on "promptable model + continual learning", which MedCRP-CL already covers for 2D. The second half ("no work has examined how established strategies trade off in this setting") is defensible only if "this setting" is defined as 3D, few-shot and including retention of pretrained ability. The gap that remains clearly true combines four elements none of which MedCRP-CL covers: volumetric (3D) universal model, few-shot tasks, tasks as new structures within one dataset, and measurement of loss of pretrained ability on a held-out control task. The thesis must cite MedCRP-CL and state these differences explicitly; leaving it out would be an attackable omission. Also note that the thesis's footnote on the literature search (TODO at `related_work.tex:118`) should list the date after which MedCRP-CL (arXiv May 2026, v2 August 2026) was found.
3. **Suggested gap wording (SUGGESTION for the author, not settled):** "Continual adaptation of text-promptable segmentation models has so far been studied for 2D images with full training data, where MedCRP-CL [key] routes tasks to modality-specific adapters of a frozen CLIPSeg. To the best of our knowledge, no prior work has studied the continual adaptation of a free-text promptable 3D universal medical segmentation model under few-shot conditions, nor measured how much of the pretrained model's ability on structures outside the task sequence is retained; consequently, how established continual-learning strategies trade off adaptation and forgetting in this setting is unknown." Shorter alternative: "... no prior work has studied the few-shot continual adaptation of a free-text promptable 3D medical segmentation model."
4. **Useful for design decisions / discussion:**
   - Precedent for testing several task orders (four here; this thesis two) and for reporting std across orders.
   - Precedent for a per-group adapter between the two ends compared in this thesis (task-specific vs shared LoRA): MedCRP-CL's "w/o CRP" (one shared LoRA + EWC, 15.55 % forgetting) vs modality-specific LoRA (4.09 %) suggests that sharing one adapter across dissimilar tasks forgets much more, in 2D with full data; whether this holds for six structures of one MRI dataset is what this thesis's shared vs task-specific LoRA comparison tests. Do not transfer the numbers.
   - Its text-embedding clustering argues that text embeddings separate tasks better than image embeddings for 2D CLIP (Table 7). In this thesis all tasks share one dataset/modality, so a modality-based grouping would collapse to one group; this could be a sentence in the Discussion on why routing was not used (author's decision).
   - It does not measure retention of pretrained ability, which is one of this thesis's primary metrics (control-task drop); this is a concrete, citable difference.
5. **Possible further related work cited by this paper (not read):** MedPEFT-CL (Gao & Morel, WACV 2026, pp. 7699–7708, doi 10.1109/WACV61042.2026.00743), parameter-efficient continual learning for medical segmentation with a medical semantic adapter and replay (as described on p. 2); and Low-Rank MoE for continual medical image segmentation (Chen et al., MICCAI 2024, LNCS 15008, pp. 382–392). Neither is in `literature.bib`; the author should check whether MedPEFT-CL also uses a text-promptable model, since it may be equally close.
6. **Bib:** no entry yet. If added, prefer the PMLR (ICML 2026, vol. 306) version if it is published; fields to take from the PMLR page, not from this PDF footnote alone. Paper reliability: numerous internal inconsistencies (Sec. 4 and 7), no seeds, undocumented baseline adaptation, so cite it for its setting and mechanism, and quote numbers only with care.
