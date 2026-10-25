# PA-EWC — paper notes

Read as prior work for Ch. 2 (State of the Art): a continual-learning method for a text-prompted (CLIPSeg-based) medical segmentation model, i.e. close to the thesis in that a language-conditioned segmentation model is trained on a task sequence.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Ziyuan Gao, Philippe Morel (University College London). *Prompt-Aware Adaptive Elastic Weight Consolidation for Continual Learning in Medical Vision-Language Models.* arXiv:2511.20732v2 [cs.MM], 21 Dec 2025. 14 pages (13 pages of content + references), Springer LNCS-like layout |
| Local PDF | `papers/t6_cl_medseg_foundation/NEW_paewc2025.pdf` (text: `papers/text/NEW_paewc2025.txt`, not valid UTF-8; tables garbled) |
| Venue | **Not stated** in the PDF (no conference footer, no acknowledgement of acceptance). Treat as an arXiv preprint until a peer-reviewed version is found |
| Bib key | none yet (working key `NEW_paewc2025`) |
| Version read | arXiv **v2** (21 Dec 2025). v1 not read; differences unknown |
| Code | **Not stated** (no repository link) |
| Notes written | 2026-10-23 by Claude from the PDF. Locators are PDF page numbers (= arXiv page numbers) plus section, table, figure or equation. Tables 1, 3, 4, 5 and Figs. 1–3 were checked on the page images (p. 4–5, 9–12) because the text extraction is garbled |

## 1. Problem and idea (abstract and introduction; p. 1–2)
- Medical vision-language models deployed clinically must learn new imaging protocols and conditions without losing earlier capabilities; sequential training causes catastrophic forgetting (p. 1–2).
- Standard EWC protects all components uniformly, which the authors consider inadequate for medical VLMs (p. 2).
- Proposal: **PA-EWC**, an EWC variant that groups parameters by their "functional role" (visual-descriptive, spatial-guided, medical-semantic) and scales each group's penalty using prompt complexity, gradient stability and task similarity (abstract p. 1; p. 2).
- Four stated contributions (p. 2): prompt-guided parameter classification; adaptive Fisher information with gradient stability; parameter-aligned complexity assessment based on medical terminology density; dynamic multi-group protection.
- Headline claims (abstract p. 1; p. 2): forgetting reduced "by up to 17.58%", improvements of 4.30 % on chest X-ray localisation and 6.06 % on polyp segmentation compared with sequential learning. (These are absolute percentage-point differences from Tables 4 and 5, see Sec. 7; own check.)

## 2. Setting (Sec. 3.1 p. 3–4; Sec. 4 p. 8–11)
- Tasks T1…TN learned sequentially; each task = images, segmentation masks and textual prompts "with varying complexity levels" (Sec. 3.1, p. 3). Objective Eq. 1 (p. 4): minimise the sum of task losses subject to not increasing earlier-task losses.
- **A task = one dataset**, which here also means a new modality, anatomy and target structure (Kvasir-SEG polyp, ISIC 2018 skin lesion, CheXlocalize chest X-ray pathology, BUSI breast tumour, CAMUS cardiac structures; Sec. 4.1 p. 8). The authors do not name a CL scenario (TIL/CIL/DIL).
- **Task identity at inference: not stated.** One shared model (no task-specific modules are mentioned); the text prompt differs per dataset, so the target is specified through the prompt. Whether the evaluation prompt implicitly encodes the task is not discussed.
- **Not few-shot:** full training splits of each dataset (Sec. 4.1, p. 8; sizes in Sec. 4).
- **2D only:** endoscopy, dermoscopy, radiography, ultrasound images processed at 512×512 (Sec. 4.2, p. 8). No volumetric data.

## 3. Method (Sec. 3.2–3.6, p. 4–8; Fig. 1 p. 4; Tables 1–2 p. 5)
- **Text prompts — five-tier hierarchy (Table 1, p. 5):** Basic (class names, e.g. "polyp", "skin lesion", "foot ulcer", "myocardium"); Visual-Descriptive (P_visual, e.g. "pink round polyp"); Spatial-Guided (P_spatial, e.g. "polyp located in center"); Medical-Semantic (P_medical, e.g. "polyp which is a small lump in colon"); Comprehensive (all combined). Basic and Comprehensive are baselines (p. 4).
  - The prompts are **templated descriptive phrases**, not clinical free text written by users. Fig. 1 (p. 4) lists text-input sources "Radiology Report", "Image Metadata", "Mask Description", "VQA Model's answer", "Manual Text Prompt", but the text never explains how prompts are generated per image or per dataset. **Not stated** whether spatial descriptors ("top left") are computed from the mask.
  - Inconsistency: Table 1 uses "foot ulcer" examples, but no foot-ulcer dataset is used (Sec. 4.1).
  - The "Task-Adaptive Prompt (OURS)" evaluated in Sec. 4.6 is not defined in Sec. 3; the examples in Fig. 3 (p. 12) are sentences such as "Left ventricular cavity in four-chamber view of the heart" and "Airspace Opacity in the frontal view of a Chest Xray".
- **Parameter classification (Eq. 2, p. 5; Table 2 p. 5):** each parameter is assigned to the prompt type that gives it the largest gradient norm. Resulting groups: θ_visual ≈ vision processing layers; θ_spatial ≈ cross-attention / conditional modules; θ_medical ≈ text processing layers. Inconsistency: Eq. 2 is written with an arg max over the gradient, while the following sentence refers to an undefined R_k^(t) (p. 5).
- **Prompt complexity (Eq. 3, p. 6):** mean over a task's prompts of weighted word counts, weights λ_visual = 2.0, λ_spatial = 2.5, λ_medical = 3.0 (base words weight 1).
- **Adaptive Fisher (Eqs. 4–6, p. 6):** standard diagonal Fisher per group, multiplied by a gradient-stability factor S (a function of gradient variance; the function symbol is garbled in the text, appears to be a sigmoid/exponential of −Var, not verifiable) and a task-similarity factor A from layer-wise activation mean/std differences between consecutive tasks (Eq. 5). Text claim: A "approaches 1.0 for dissimilar tasks" (p. 6).
- **Adaptive weight (Eq. 7, p. 7):** w_m = F_m · (1 + C^(i)/C_max).
- **Loss (Eqs. 8–10, p. 7–8):** w_seg · L_seg + w_dice · L_dice + w_ewc · Σ_{j<i} L_EWC^(j), with w_seg = 1.0, w_dice = 0.3, w_ewc = 10.0; base Fisher "scaled to 1000" (p. 8). L_seg is not defined (presumably cross-entropy; not stated). Eq. 9 says the weights come "from Equation (8)" though they are defined in Eq. 7 (p. 7).
- **Which parameters are trained:** not stated explicitly. Because the penalty covers vision, cross-attention and text-encoder groups and the "Params (M)" column is 150.0 for sequential CLIPSeg and EWC and 155.0 for PA-EWC (Table 3, p. 9), the whole CLIPSeg model (including the CLIP encoders) appears to be trained. This is an inference; the original CLIPSeg freezes CLIP, and the paper does not say whether it does. The source of the extra 5 M parameters of PA-EWC is **not stated**.

## 4. Data (Sec. 4.1, p. 8)
All 2D; split sizes given as train/val/test (images; unit not stated, assumed images):
- **Kvasir-SEG** (polyp, endoscopy): 800/100/100.
- **ISIC 2018** (skin lesion, dermoscopy): 810/90/379.
- **CheXlocalize** (chest X-ray pathology localisation): 1279/446/452. Citation problem: reference [16] is Selvan et al., "Lung segmentation from chest X-rays using variational data imputation" (p. 14), not the CheXlocalize paper. Which pathologies are segmented and how multiple pathologies per image are handled: **not stated** (Fig. 3 shows "Airspace Opacity", "Atelectasis").
- **BUSI** (breast ultrasound tumour): 624/78/78.
- **CAMUS** (cardiac ultrasound chamber segmentation): 4800/600/600. Which structure(s) are segmented: not stated in Sec. 4.1 (Table 1 mentions "myocardium"; Fig. 3 shows "Left ventricular cavity").
- Binary foreground segmentation (Eq. 10 uses softmax channel 1 as foreground, p. 8).

## 5. Implementation (Sec. 4.2, p. 8–9)
- Backbone **CLIPSeg** [Lüddecke & Ecker, CVPR 2022] with ViT-B/16 vision encoder and transformer text encoder, 512×512 input (p. 8).
- AdamW, learning rate 1e-4, weight decay 1e-2, cosine annealing; **50 epochs per task**, early stopping on validation Dice; batch size 16; 2×A100 GPUs (p. 8–9).
- Runs: "Results are averaged over three runs with random seed 43" (p. 9) — **inconsistent** (three runs but one seed named).
- Training time and parameter counts per method in Table 3 (p. 9): PA-EWC 8.7 h, 155.0 M; sequential 8.1 h, 150.0 M.
- Hyperparameters of the baselines (EWC λ, LoRA rank, replay buffer size of DER++, ZSCL reference data, etc.): **not stated**.

## 6. Evaluation protocol and metrics (Sec. 4.1, p. 8)
- **Dice** per task after training on all tasks, Dice_i^final (Eq. 11). Tables report Dice in %.
- **Forgetting Rate** (Eq. 12): FR = Σ_{i=1}^{T−1} (Dice_i^peak − Dice_i^final), attributed to [9] (Kirkpatrick et al., which does not define this metric — attribution questionable). Eq. 12 is a sum, while Table 3 reports "Average Forgetting (%)"; Table 4 reports per-task values.
- Training time and parameter overhead also reported (p. 8).
- Reference points: "CLIPSeg Individual" (one model per task) as "upper bound" (Table 5, p. 11; text p. 10); "CLIPSeg Sequential" as naive baseline.
- **Loss of pretrained / zero-shot ability: not measured.** No held-out dataset or zero-shot evaluation of the pretrained CLIPSeg is reported, although ZSCL (a zero-shot-preservation method) is a baseline. Forward transfer is not reported.
- Five task orders are evaluated for forgetting (Table 4, p. 10; Fig. 2 p. 11); the main comparison (Tables 3 and 5) uses Kvasir → ISIC → CheXlocalize → BUSI → CAMUS (p. 10).

## 7. Results
- **Table 3 (p. 9), average Dice % / average forgetting % / training time h / params M** (mean ± std, presumably over 3 runs):
  - CLIPSeg Individual 78.5±0.6 / 0.0±0.0 / 12.4 / 150.0
  - CLIPSeg Sequential 62.3±1.9 / 35.7±2.3 / 8.1 / 150.0
  - EWC 65.48±1.7 / 28.34±2.1 / 8.5 / 150.0
  - LwF 67.2±1.5 / 26.8±1.9 / 8.9 / 150.0
  - PackNet 68.92±1.4 / 24.71±1.8 / 9.2 / 150.0
  - Progressive NN 71.23±1.2 / 22.15±1.5 / 15.3 / 375.0
  - DER++ 71.58±1.0 / 22.43±1.3 / 9.8 / 155.0
  - CLIPSeg + LoRA 69.5±1.2 / 24.3±1.6 / 6.8 / 152.5
  - CLIPSeg + CLIP-Adapter 70.1±1.3 / 23.7±1.4 / 6.9 / 151.8
  - ZSCL 73.02±0.9 / 20.87±1.2 / 9.1 / 150.0
  - MoE-Adapters 72.84±1.1 / 21.34±1.4 / 9.4 / 165.3
  - PA-EWC 75.34±0.8 / 18.42±1.0 / 8.7 / 155.0
  - Text (p. 9): PA-EWC exceeds ZSCL by 2.32 (Dice) and 2.45 (forgetting) points.
- **Table 5 (p. 11), Dice % per task, order Kvasir → ISIC → CheX → BUSI → CAMUS** (Kvasir / ISIC / CheX / BUSI / CAMUS):
  - CLIPSeg (Individual) 89.51±0.8 / 92.12±0.5 / 59.56±1.1 / 64.32±0.9 / 88.85±0.6
  - Sequential Baseline 67.36±1.2 / 88.28±0.4 / 52.48±0.6 / 69.06±1.0 / 80.38±1.8
  - General EWC 59.31±2.1 / 83.67±1.3 / 33.85±1.8 / 68.47±2.2 / 82.11±1.2
  - Self-adaptive EWC 70.94±0.9 / 89.15±0.7 / 43.71±1.4 / 69.18±1.6 / 81.63±0.8
  - PA-EWC 73.42±0.6 / 88.93±0.8 / 56.78±0.9 / 71.92±1.3 / 78.64±1.1
  - Abstract gains = Table 5 differences to sequential: 73.42 − 67.36 = 6.06 (Kvasir), 56.78 − 52.48 = 4.30 (CheX) (own check).
- **Table 4 (p. 10), forgetting % per task, sequential vs PA-EWC, five orders** (CAMUS / BUSI / ISIC / Kvasir / CheX):
  - Kvasir→ISIC→CheX→BUSI→CAMUS: seq 21.45 / 25.96 / 12.14 / 33.83 / 46.93; PA-EWC 21.80 / 25.56 / 11.23 / 26.90 / 43.77
  - CheX→CAMUS→BUSI→ISIC→Kvasir: seq 45.89 / 29.78 / 8.02 / 18.34 / 37.92; PA-EWC 40.26 / 27.02 / 8.26 / 15.59 / 22.65
  - CAMUS→Kvasir→CheX→BUSI→ISIC: seq 58.74 / 25.67 / 7.37 / 24.12 / 26.95; PA-EWC 50.30 / 22.00 / 7.46 / 20.90 / 23.02
  - ISIC→CAMUS→Kvasir→CheX→BUSI: seq 47.56 / 20.62 / 12.18 / 23.45 / 49.32; PA-EWC 31.50 / 22.47 / 9.52 / 19.92 / 31.74
  - CheX→Kvasir→CAMUS→ISIC→BUSI: seq 32.69 / 21.97 / 8.37 / 21.08 / 41.42; PA-EWC 32.69 / 19.90 / 8.57 / 19.61 / 31.78
  - "Up to 17.58%" = 49.32 − 31.74 (CheX, fourth order) (own check). Authors: earlier tasks generally forget more; PA-EWC "consistently outperforms" sequential across orders (p. 10).
- **Prompt strategies (Fig. 2, p. 11; text p. 11–12):** average forgetting Task-Adaptive Prompt 10.6 %, Basic Prompt 14.6 %, Comprehensive Prompt 14.0 %, Sequential Baseline 15.2 %. Fig. 2 shows four tasks per order (the last task omitted). The text calls the five orders "five comprehensive evaluation metrics" (p. 11).
- Qualitative masks for each prompt strategy in Fig. 3 (p. 12).

### Inconsistencies (own checks; arithmetic marked as own)
1. **Table 3 vs Table 5.** Own calculation of the unweighted mean over the five tasks in Table 5: Individual 78.87 (Table 3: 78.5); Sequential 71.51 (Table 3: 62.3); General EWC 65.48 (Table 3 EWC: 65.48, matches); Self-adaptive EWC 70.92 (not in Table 3); PA-EWC 73.94 (Table 3: 75.34). The sequential and PA-EWC averages do not match; the paper does not say whether Table 3 uses another order or averages over orders.
2. **Non-zero forgetting of the last task in Table 4.** By Eq. 12 forgetting is defined only for tasks 1…T−1, and the last-trained task has no later tasks; yet Table 4 lists non-zero values for the last task of every order (e.g. CAMUS 21.45/21.80 in the first order, BUSI 20.62/22.47 in the fourth). Fig. 2 omits the last task, but its values differ from Table 4 (e.g. sequential Kvasir in the first order is roughly 22 % in Fig. 2, 33.83 % in Table 4; read off the bar chart).
3. **"Consistently outperforms" vs Table 4:** PA-EWC forgets more than sequential in several cells (CAMUS 21.80 vs 21.45; ISIC 8.26 vs 8.02, 7.46 vs 7.37, 8.57 vs 8.37; BUSI 22.47 vs 20.62) and equals it once (CAMUS 32.69).
4. **Average forgetting magnitudes:** sequential 35.7 % in Table 3, 15.2 % in Fig. 2.
5. **PA-EWC is not best on all tasks in Table 5** (best on three of five, as the text concedes, p. 10), and it is below sequential on CAMUS (78.64 vs 80.38), the last task — a plasticity cost.
6. Individual models are called an "upper bound" yet sequential training beats them on BUSI (69.06 vs 64.32) and PA-EWC on BUSI (71.92) (Table 5).
7. "Three runs with random seed 43" (p. 9); "significantly" used (p. 10, p. 12) without a statistical test.
8. Undefined "Task-Adaptive Prompt"; "foot ulcer" examples without dataset; CheXlocalize citation points to a different paper; Eq. 9 refers to Eq. 8 for weights defined in Eq. 7.

## 8. Limitations and future work (authors)
- **None stated.** The conclusion (p. 12) repeats the claims and mentions potential for clinical deployment; no limitations section.

## 9. Check of the author's notes (not cited yet; sentences of `thesis/related_work.tex` affected, checked 2026-10-23)
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:115` | continual learning for VLMs "developed almost exclusively for two-dimensional classification, in which the prediction is a global image--text similarity over a finite label space" | **Needs rewording.** PA-EWC (and MedPEFT-CL) apply CL to a text-prompted 2D *segmentation* VLM (CLIPSeg) with dense output, and PA-EWC benchmarks ZSCL, MoE-Adapters, LoRA and CLIP-Adapter on it (Table 3). "Almost exclusively" can stand only if these works are named as the exception. |
| `thesis/related_work.tex:115` | "The works closest to the present study each cover only part of its setting: Zhang et al. …, MedSeqFT …, Chen et al. …" | **Incomplete.** PA-EWC is closer than Zhang et al. on the language axis (text prompts with descriptive phrases rather than fixed class embeddings) and should be listed: 2D, not a 3D foundation model, full data, no zero-shot/control evaluation. |
| `thesis/related_work.tex:117` | "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model, and consequently no work has examined how established continual-learning strategies trade off in this setting" | **Still true as worded** (PA-EWC is 2D, CLIPSeg is not a 3D model), but the second half needs care: PA-EWC compares established strategies (EWC, LwF, PackNet, PNN, DER++, LoRA, CLIP-Adapter, ZSCL, MoE-Adapters) on a text-prompted 2D medical segmentation model. The claim must keep "3D" and should not be weakened to "text-promptable medical segmentation". |
| `thesis/related_work.tex:120` | "results obtained for task-specific networks or for CLIP-based classifiers cannot be assumed to carry over to a pretrained free-text promptable model" | **Needs extension.** There are now results for a CLIP-based *segmenter* (2D); the argument should say why 2D CLIPSeg results do not carry over to a volumetric model (e.g. VoxTell's architecture, 3D data, few-shot). |
| `thesis/related_work.tex:94` | the capability added in each task "is held in a dedicated component … reached through task identity or routing" (recurring assumption) | **Counter-example** for regularisation-based CL: PA-EWC uses one shared parameter set with a penalty and no task-specific components. The sentence is about CL for medical segmentation in general; it should not be read as universal. |
| `thesis/related_work.tex:219–241` (positioning table) | rows Lifelong nnU-Net, Zhang et al., MedSeqFT, Chen et al. | **Missing row** if the paper is used: Language "templated descriptive text prompts"; 3D FM "no (2D CLIPSeg)"; Few-shot "no"; Setting "sequential datasets (task identity not stated)"; Strategies "PA-EWC, seq. FT, individual, EWC, LwF, PackNet, PNN, DER++, LoRA, CLIP-Adapter, ZSCL, MoE-Adapters". |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
Thesis setting (from `gonzalez2023lifelong.md`, Sec. 10): tasks are **different structures from one dataset** (SKM-TEA), a pretrained free-text promptable 3D model (VoxTell), few-shot supervision, loss of pretrained ability measured on a control task.
1. **Relation to this thesis:** closest in that a language-conditioned segmentation VLM is trained continually and compared with ZSCL, LoRA and MoE-Adapters. Differences: 2D images, CLIPSeg (CLIP ViT-B/16 with a light decoder, not a 3D universal model), tasks = whole datasets of different modalities (much larger shift than structures within one knee MRI dataset), full training sets (624–4800 training images per task), templated phrases rather than free text, no measure of pretrained/zero-shot ability, task identity at inference not stated.
2. **Verdict on the gap claim:** "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model" is **not contradicted** — the model is 2D and not free-text in the VoxTell sense. It does contradict any weaker form ("text-promptable medical segmentation" or "medical VLM segmentation"), and the claim that VLM-CL methods were studied only for classification (line 115) must be reworded. The thesis should cite PA-EWC (and MedPEFT-CL) as the 2D precedent and state the differences explicitly.
3. **Evidential weight is low:** arXiv preprint without stated venue, no code, internally inconsistent tables (Sec. 7, items 1–4), unclear prompt generation, undefined trained parameters, misattributed citations. Cite for existence and setting, not for numbers; if numbers are quoted, flag the inconsistency or avoid Table 3 averages.
4. Useful for design arguments: (a) EWC-type regularisation on a text-prompted segmenter is a published strategy family the thesis does not evaluate — an examiner may ask why EWC is absent (possible `\todo{defense: ...}`); (b) the paper shows forgetting depends strongly on task order (Table 4), supporting the use of two orders; (c) it shows prompt wording (basic vs comprehensive vs task-adaptive) changes forgetting (Fig. 2), relevant to the thesis's prompt-dependence question; (d) its lack of a zero-shot/control measurement is a point where the thesis's control task goes further.
5. Bib: no peer-reviewed version identified; check later whether it was published (format suggests a Springer conference submission). Do not cite as peer-reviewed.
