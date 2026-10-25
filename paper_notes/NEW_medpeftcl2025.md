# MedPEFT-CL — paper notes

Read as prior work for Ch. 2 (State of the Art): a parameter-efficient continual-learning framework (LoRA adapters + replay + EWC) for a text-prompted (CLIPSeg-based) medical segmentation model, i.e. close to the thesis in model type and in the strategy families compared.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Ziyuan Gao (University College London). *MedPEFT-CL: Dual-Phase Parameter-Efficient Continual Learning with Medical Semantic Adapter and Bidirectional Memory Consolidation.* arXiv:2511.17668v1 [cs.CV], 21 Nov 2025. 8 pages of content + references, two-column CVF-style layout |
| Local PDF | `papers/t6_cl_medseg_foundation/NEW_medpeftcl2025.pdf` (text: `papers/text/NEW_medpeftcl2025.txt`, not valid UTF-8; two-column text interleaved, tables garbled) |
| Venue | **Not stated in the PDF** (no conference footer). Web check 2026-10-23 (not from the paper): a UCL Discovery record (discovery.ucl.ac.uk/id/eprint/10227521) lists it in *Proceedings of the 2026 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV 2026)*, pp. 7699–7708, and a WACV 2026 poster page exists (wacv.thecvf.com/virtual/2026/poster/355). That record names **two authors (Ziyuan Gao, P. Morel)**, the arXiv PDF only one. Take bibliographic fields from the CVF Open Access page, not from these notes |
| Bib key | none yet (working key `NEW_medpeftcl2025`) |
| Version read | arXiv **v1** (21 Nov 2025). The WACV camera-ready version was **not read**; numbers may differ |
| Code | **Not stated** (no repository link) |
| Notes written | 2026-10-23 by Claude from the PDF. Locators are PDF page numbers plus section, table, figure or equation (no line numbers). Tables 1–8 and Figs. 1–3 were checked on the page images (p. 1–8) because the text extraction is garbled |

## 1. Problem and idea (abstract and introduction; p. 1–2)
- Medical vision-language segmentation models forget when adapted sequentially to "new anatomical structures"; the alternative, retraining from scratch, limits deployment (abstract p. 1; p. 1).
- CL specifically for medical vision-language tasks is described as underexplored; earlier work is either single-modality medical or general-domain VLM CL (p. 1–2). The authors also state that combining PEFT with CL "remains unexplored, especially for medical applications" (Related Work, p. 2).
- Proposal: **MedPEFT-CL**, a "dual-phase" framework on CLIPSeg: an adaptive learning phase (prompt-similarity-based adapter allocation + LoRA in both encoders) and a knowledge consolidation phase (difficulty-based replay memory + EWC, coupled by a "bidirectional Fisher–memory" feedback) (p. 1–3, Figs. 1–2).
- Stated contributions (p. 2): semantic-driven adapter allocation; bi-modal LoRA "0.24-0.39M vs 150M" trainable parameters; bidirectional Fisher–memory coordination; evaluation with forgetting "1.91% vs 6.21% for best baseline" (see inconsistency 3 in Sec. 7).

## 2. Setting (Sec. 3 p. 2–3; Sec. 4 p. 5–7)
- Sequence of segmentation tasks T(1)…T(N); each task is a dataset D(t) = {(x_i, y_i, p(t))} of images, masks and "the medical prompt" (Sec. 3, p. 2). Objective Eq. 1 (p. 2): sum of expected segmentation losses over all tasks seen so far.
- **A task = one dataset.** Three sequence types (Sec. 4.2, p. 5–7):
  - **Mixed** (10 tasks): Kvasir → CheX → Colon → BUSI → Clinic → ISIC → ETIS → Camus → CVC300 → DFU (Table 2, p. 6).
  - **Heterogeneous** (6 tasks): Kvasir → ISIC → CheX → BUSI → Camus → DFU (Table 3, p. 7).
  - **Homogeneous** (5 tasks): Clinic → ETIS → CVC → Colon → Kvasir — five polyp datasets, i.e. the **same structure in new datasets** (Table 4, p. 7).
  - So the tasks are partly new modalities/structures (mixed, heterogeneous) and partly new domains of one structure (homogeneous). The authors do not name a CL scenario (TIL/CIL/DIL).
- **Task identity at inference: not stated.** Training creates or reuses a task adapter depending on prompt similarity to earlier tasks (Sec. 3.2.2, p. 3–4); the paper does not say how the adapter is chosen at test time (by known task identity, by the same prompt-similarity rule, or otherwise). Fig. 2 (p. 3) draws a "Similarity > Thres" decision in front of the adapter pool, without stating whether it is applied at inference.
- **Not few-shot:** full training splits (Table 1, p. 5).
- **2D only** (images resized to 352×352, p. 5).
- One fixed order per sequence type; no repeated orders of the same task set.

## 3. Method (Sec. 3.1–3.3, p. 3–5; Fig. 2 p. 3)
- **Text prompts (Sec. 3.2.1, p. 3):** "clinically-informed prompts adapted from [29]" (Poudel et al., 2024, *Exploring transfer learning in medical image segmentation using vision-language models*). They include pathology explanations, patient demographics (age, gender), imaging parameters (quality, cardiac phase), shape/size, object count, spatial position and co-occurring conditions (p. 3). Examples quoted: "Left ventricular cavity in two-chamber view of the heart at end of the diastole cycle of a 56-year-old female with good image quality" and "One small white round polyp which is a projecting growth of tissue located in right of the image" (p. 3).
  - These are **descriptive sentences per image** (they contain image-specific attributes such as age and position), i.e. closer to free text than class names, but generated from a fixed attribute scheme by [29], not written by users. The thesis should not call them "free text" without qualification.
  - Prompts are given to the model with each image during training and evaluation (Eq. 1 uses f_θ(x, p(k)), p. 2). A single "representative prompt" p_k per task is used for adapter similarity (p. 4); how it is chosen: **not stated**.
  - No experiment varies prompt wording.
- **Task-similarity adapter allocation (Eq. 2, p. 3–4):** cosine similarity of CLIPSeg text-encoder embeddings between the new task's prompt and earlier tasks' representative prompts; if the maximum exceeds τ = 0.75, the adapter of the most similar task is reused, otherwise a new adapter is created (p. 4).
- **Bi-modal LoRA (Eq. 3, p. 4):** LoRA on CLIPSeg's transformer layers in both the visual and the text encoder, pretrained weights frozen; r = 8, α = 16. "0.24-0.39M trainable parameters per task compared to CLIPSeg's 150M parameters" (p. 4).
  - **Which parameters are trained:** the LoRA/adapter parameters. Whether the CLIPSeg decoder is trained is **not stated**; Fig. 2 (p. 3) marks "LoRA" and "New Adapter" as trainable and the CLIP encoders as frozen, and shows both a "LoRA" block and separate "Similarity-Aware Adapters" — the text does not clarify whether these are one module or two.
- **Memory buffer (Eqs. 4–5, p. 4):** per task, the ⌊|D(t)| · r_memory⌋ training samples with the highest cross-entropy loss are stored, r_memory = 0.15; the buffer also stores difficulty scores and Fisher-based sampling weights. (Own calculation: e.g. 720 of 4800 CAMUS training images, 120 of 800 Kvasir images — a large replay memory.)
- **Fisher → memory (Eqs. 6–7, p. 4):** per-task replay weight = temporal decay w_base = 1/(T_current − t) times (1 + α · mean Fisher), α = 0.5 (note: α also names the LoRA scaling factor, p. 4).
- **Memory → Fisher (Eq. 8, p. 4):** Fisher computed only on the stored hard samples, weighted by w_diff = 1 + L_diff / max(L_diff).
- **Replay training (Sec. 3.3.3, p. 4–5):** mixed batches with fraction r_replay = 0.4 from memory; loss L_seg + L_dice + λ_ewc · L_EWC (Eq. 9), EWC over all earlier tasks (Eq. 10), λ_ewc = 500 (p. 5). Over which parameters the EWC penalty acts (LoRA only or all): **not stated**.

## 4. Data (Sec. 4.1, Table 1, p. 5)
All 2D; train/val/test (unit not stated, assumed images):
- Endoscopy, colon (polyp): **Kvasir-SEG** 800/100/100; **ClinicDB** 490/61/61; **ETIS** 157/20/19; **ColonDB** 304/38/38; **CVC300** 48/6/6.
- Photography: skin **ISIC 2016** 810/90/379; foot **DFU 2022** 1600/200/200.
- Ultrasound: heart **CAMUS** 4800/600/600; breast **BUSI** 624/78/78.
- X-ray, chest: **CheXlocalize** 1279/446/452, cited as [14], which is the CheXpert paper (Irvin et al., AAAI 2019; p. 8) rather than CheXlocalize itself.
- Which CAMUS structure(s), which CheXlocalize pathologies: **not stated** (Fig. 3 p. 6 shows a single foreground mask per image).
- Note: the ISIC split 810/90/379 is called ISIC 2016 here and ISIC 2018 in PA-EWC (same author, `NEW_paewc2025.md`).

## 5. Implementation (Sec. 4.1 "Implementation Details", p. 5)
- Backbone **CLIPSeg-RD64**; 2×A100 GPUs; 352×352 input; AdamW, lr 8×10⁻⁴, weight decay 8×10⁻⁵; batch size 16; at most 100 epochs per task with early stopping; τ = 0.75; LoRA r = 8, α = 16; r_memory = 0.15; r_replay = 0.4; λ = 500 (p. 5).
- These hyperparameters are "validated as the optimal configuration through comprehensive analysis in Table 7" (p. 5); which split the selection used: **not stated** (risk of selection on test results).
- "All results are averaged over three runs with random seed 43" (p. 5) — **inconsistent** (three runs, one seed). No standard deviations are reported in any table.
- Compute (Table 5, p. 7): Ours 22,358 MiB GPU memory, 1.58 s/it; sequential CLIPSeg 32,172 MiB, 1.50 s/it.
- Baseline hyperparameters (EWC λ, DER buffer, MoE-Adapter experts, etc.): **not stated**.

## 6. Evaluation protocol and metrics (Sec. 4.1, p. 5)
- **Average Dice** over all T tasks after training the sequence (Eq. 11).
- **Average Forgetting Rate** (Eq. 12): FR = 1/(T−1) Σ_{i=1}^{T−1} (Dice_i^peak − Dice_i^final)/Dice_i^peak × 100 % — **relative** to the peak Dice reached on task i during training. The authors present the peak reference as their own choice and "more rigorous" than Lopez-Paz and Ranzato's (GEM) definition (p. 5). The last task has no FR ("-" in Tables 2–4), consistent with the definition.
- Reference points: "CLIPSeg Individual" (one model per task) as "upper bound"; "CLIPSeg Sequential" as naive sequential training (Table 2 caption, p. 6).
- **Loss of pretrained / zero-shot ability: not measured.** No held-out dataset, no evaluation of the pretrained CLIPSeg, no forward-transfer metric.
- Efficiency: trainable parameters, GPU memory, s/it (Table 5).

## 7. Results
- **Table 2 (p. 6), mixed sequence, avg Dice (%)** (Kvasir / CheX / Colon / BUSI / Clinic / ISIC / ETIS / Camus / CVC300 / DFU / Avg):
  - CLIPSeg Individual 91.39 / 62.57 / 78.07 / 69.31 / 85.69 / 91.94 / 75.93 / 86.09 / 92.90 / 76.31 / 81.02
  - CLIPSeg Sequential 67.44 / 42.47 / 59.12 / 55.64 / 68.60 / 90.54 / 62.39 / 74.66 / 90.92 / 72.28 / 68.41
  - EWC 76.50 / 48.47 / 71.01 / 56.64 / 77.36 / 85.01 / 68.07 / 74.51 / 93.50 / 72.88 / 72.40
  - DER 78.95 / 51.23 / 66.44 / 61.87 / 72.15 / 89.92 / 69.81 / 78.94 / 92.18 / 71.92 / 73.34
  - VR-LwF 75.67 / 48.91 / 69.55 / 60.18 / 76.83 / 89.15 / 67.22 / 77.63 / 92.01 / 74.18 / 73.13
  - Low-Rank MoE 73.82 / 46.15 / 67.89 / 58.92 / 74.28 / 88.76 / 65.43 / 76.88 / 91.67 / 73.55 / 71.74
  - MoE-Adapter 79.28 / 53.17 / 68.29 / 65.48 / 72.96 / 90.82 / 68.89 / 78.11 / 91.30 / 73.17 / 74.15
  - Ours 85.85 / 68.72 / 75.27 / 70.67 / 81.46 / 91.77 / 64.04 / 80.18 / 91.61 / 72.28 / 78.19
  - **Avg FR (%)** (first nine tasks / Avg): Sequential 17.43 / 24.87 / 14.55 / 23.84 / 13.00 / 1.81 / 6.08 / 3.54 / 2.00 / 11.90; EWC … 9.38; DER … 7.97; VR-LwF … 8.83; Low-Rank MoE … 9.86; MoE-Adapter 6.90 / 8.79 / 9.03 / 8.62 / 11.41 / 2.31 / 3.76 / 2.76 / 3.00 / 6.21; Ours 0.77 / 0.90 / 0.26 / 4.53 / 1.34 / 1.16 / 7.29 / 1.42 / 0.90 / 2.23.
  - Text (p. 7): 78.19 vs 74.15 (MoE-Adapter), +4.04 points; FR 2.23 vs 6.21, "a 64% reduction" (own check: (6.21 − 2.23)/6.21 = 64.1 %).
  - Ours exceeds the "upper bound" on CheX (68.72 vs 62.57) and BUSI (70.67 vs 69.31) and gives Dice identical to Sequential on DFU (72.28) — the last task.
- **Table 3 (p. 7), heterogeneous, avg Dice** (Kvasir / ISIC / CheX / BUSI / Camus / DFU): Individual 91.39 / 91.94 / 62.57 / 69.31 / 91.09 / 76.13; Sequential 58.34 / 84.26 / 25.25 / 62.37 / 79.80 / 72.12; EWC 63.02 / 86.39 / 38.36 / 63.07 / 84.12 / 73.04; DER 73.22 / 88.45 / 53.91 / 66.18 / 85.78 / 74.12; VR-LwF 67.89 / 86.78 / 45.33 / 63.95 / 83.44 / 73.45; Low-Rank MoE 65.45 / 87.12 / 42.18 / 64.23 / 82.95 / 73.67; MoE-Adapter 71.38 / 84.87 / 50.05 / 69.16 / 79.39 / 73.02; Ours 81.78 / 92.15 / 69.63 / 70.69 / 81.66 / 72.28. **FR** (first five): Sequential 27.22 / 8.30 / 41.69 / 15.68 / 4.51; MoE-Adapter 15.11 / 7.01 / 11.49 / 8.93 / 3.12; Ours 3.78 / 0.57 / 0.66 / 7.82 / 0.21. No "Avg" column in this table.
- **Table 4 (p. 7), homogeneous (polyp), avg Dice** (Clinic / ETIS / CVC / Colon / Kvasir): Individual 91.69 / 75.93 / 88.90 / 78.07 / 91.39; Sequential 80.80 / 61.38 / 83.24 / 71.57 / 85.98; EWC 82.05 / 74.13 / 85.44 / 69.86 / 88.40; DER 82.35 / 74.85 / 85.80 / 70.45 / 88.75; VR-LwF 81.90 / 73.65 / 85.20 / 70.80 / 88.25; Low-Rank MoE 81.45 / 72.80 / 84.90 / 70.25 / 87.85; MoE-Adapter 79.71 / 66.91 / 88.38 / 71.68 / 87.14; Ours 82.21 / 69.99 / 90.90 / 77.67 / 87.08. **FR** (first four): Sequential 5.00 / 11.58 / 8.60 / 8.61; EWC 4.06 / 0.94 / 9.08 / 10.04; DER 4.05 / 1.85 / 5.45 / 8.85; MoE-Adapter 4.14 / 5.29 / 8.25 / 6.69; Ours 1.73 / 4.34 / 1.96 / 1.19. Here DER has the best Dice on three of five tasks and EWC/DER forget less than Ours on ETIS.
- **Table 5 (p. 7), averages "across all evaluated task sequences"** (Avg Dice / Avg FR / trainable params M / GPU MiB / s/it): Individual 81.02 / – / 150 / – / –; Sequential 67.71 / 15.36 / 150 / 32172 / 1.50; EWC 71.37 / 10.73 / 150 / 32180 / 1.52; LwF 70.86 / 11.48 / 149.6 / 32172 / 1.54; PackNet 74.21 / 8.32 / 75 / 16086 / 0.95; Progressive NN 73.12 / 7.89 / 375 / 80430 / 3.75; DER 74.59 / 6.58 / 155 / 33276 / 1.68; VR-LwF 73.69 / 8.18 / 149.6 / 32236 / 1.51; Low-Rank MoE 72.86 / 10.48 / 2.3 / 15,247 / 1.07; MoE-Adapters 75.81 / 5.13 / 59.8 / 19898 / 1.37; Ours 78.84 / 1.91 / 0.24–0.39 / 22358 / 1.58. Note: the full-fine-tuning baselines (EWC, LwF, DER, VR-LwF) train ~150 M parameters, Ours only LoRA — the comparison mixes trainable-parameter budgets.
- **Table 6 (p. 8), similarity threshold τ** (new/reused adapters; Dice; FR): 0.3: 30 %/70 %, 73.00, 5.72; 0.5: 45 %/55 %, 76.52, 3.28; **0.75: 60 %/40 %, 78.84, 1.91**; 0.9: 65 %/35 %, 74.52, 4.22.
- **Table 7 (p. 8), nine configurations** (r, α, r_memory, r_replay, λ → train params, Dice, FR, s/it); e.g. #4 r = 16, α = 32, 0.20, 0.5, λ = 2000 → 265,604, 80.11, 1.38, 2.5; #6 (default) r = 8, α = 16, 0.15, 0.4, λ = 500 → 245,636, 78.84, 1.91, 1.6; #5 r = 64 → 385,412, 75.38, 7.06; #3 r_memory = 0.05 → 69.37, 11.28. Authors keep #6 for speed although #4 is better (p. 8).
- **Table 8 (p. 8), module ablation** (Dice / FR): PEFT baseline 61.31 / 20.32; + EWC 67.22 / 14.01; + replay memory 73.27 / 6.56; + Fisher guidance 76.24 / 3.38; + bidirectional feedback 78.84 / 1.91. Replay gives the largest single gain (+6.05 Dice, −7.45 FR over the EWC row; own calculation).
  - Notable: the PEFT-only baseline (61.31 / 20.32) is **worse than CLIPSeg Sequential full fine-tuning** in Table 5 (67.71 / 15.36). Whether this PEFT baseline uses adapter allocation (task-specific/reused adapters) or one shared LoRA is **not stated**.

### Inconsistencies (own checks; arithmetic marked as own)
1. **"Individual" upper bound differs between tables for the same dataset:** Camus 86.09 (Table 2) vs 91.09 (Table 3); Clinic 85.69 (Table 2) vs 91.69 (Table 4); CVC300 92.90 (Table 2) vs 88.90 (Table 4); DFU 76.31 (Table 2) vs 76.13 (Table 3). Independent models should not depend on the sequence.
2. **Table 5 averages cannot be reproduced from Tables 2–4** (own calculations). Ours: per-sequence mean Dice 78.19 (mixed), 78.03 (heterogeneous, mean of six), 81.57 (homogeneous, mean of five); mean of the three = 79.26, task-weighted mean = 78.95; Table 5 gives 78.84. Ours FR: 2.23, 2.61, 2.31 → mean 2.38; Table 5 gives 1.91. Sequential Dice: 68.41, 63.69, 76.59 → mean 69.56 (Table 5: 67.71); Sequential FR: 11.90, 19.48, 8.45 → mean 13.28 (Table 5: 15.36). Table 5 "CLIPSeg Ind." 81.02 equals the mixed-sequence value only.
3. **Headline "1.91% vs 6.21% for best baseline"** (p. 2) combines Ours from Table 5 (1.91) with MoE-Adapter from Table 2 (6.21); in Table 5 MoE-Adapters has 5.13.
4. Trainable parameters: "0.24–0.39M" (p. 2, 4; Table 5) vs 235,652–385,412 in Table 7 and "0.16–0.26% (235K–385K) of the ~151M total" (p. 8), while the CLIPSeg total is given as 150M elsewhere.
5. "Three runs with random seed 43", no variances; "significantly" used without tests (p. 1–2).
6. Author list: one author on arXiv, two (Gao, P. Morel) in the UCL Discovery record of the WACV version.
7. α denotes both the LoRA scaling (16) and the Fisher weight in Eq. 6 (0.5).
8. Coincidence across the two papers by the same first author (observation, not an accusation): the PA-EWC headline average Dice 75.34 (`NEW_paewc2025.md`, Table 3) equals MedPEFT-CL Table 7 configuration #1 (75.34).

## 8. Limitations and future work (authors)
- **None stated.** The conclusion (p. 8) restates the claims; no limitations or future-work section.

## 9. Check of the author's notes (not cited yet; sentences of `thesis/related_work.tex` affected, checked 2026-10-23)
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:115` | CL for VLMs "developed almost exclusively for two-dimensional classification, in which the prediction is a global image--text similarity over a finite label space" | **Needs rewording.** MedPEFT-CL (with PA-EWC) is CL of a text-prompted 2D segmentation VLM and compares VLM-CL methods (VR-LwF, MoE-Adapters) on dense output. Name these as the (2D) exception. |
| `thesis/related_work.tex:115` | "The works closest to the present study each cover only part of its setting: …" | **Incomplete.** MedPEFT-CL is arguably the closest work on the model and strategy axes (text-prompted segmenter, LoRA in both encoders, replay, EWC); it should be added with its missing parts: 2D, not a 3D foundation model, full data, descriptive attribute-based prompts, no measurement of pretrained ability. |
| `thesis/related_work.tex:117` | "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model, and consequently no work has examined how established continual-learning strategies trade off in this setting" | **True as worded only because of "3D"** (and arguably "free-text"). A weaker version ("text-promptable medical segmentation") would be false. The sentence should keep "3D" and should acknowledge the 2D CLIPSeg work explicitly. |
| `thesis/related_work.tex:120` | "results obtained for task-specific networks or for CLIP-based classifiers cannot be assumed to carry over to a pretrained free-text promptable model" | **Needs extension** to CLIP-based 2D segmenters; argue why they do not carry over (volumetric model, structures within one dataset, few-shot, VoxTell's architecture). |
| `thesis/related_work.tex:60` (LoRA paragraph) | "The configurations compared in this thesis lie at the two ends of this range: a separate low-rank adapter for each task … and a single low-rank adapter shared across all tasks" | **Consistent, and MedPEFT-CL is a medical intermediate point**: adapters reused across tasks whose prompts are similar (τ = 0.75), new adapters otherwise (p. 3–4). Could be cited here. |
| `thesis/related_work.tex:94` / `:115` | the capability added in each task is held in a dedicated component "reached through task identity or routing" | **Consistent:** MedPEFT-CL keeps task adapters allocated by text-prompt similarity (a routing decision), but inference-time selection is not stated — do not claim it routes by prompt at test time. |
| `thesis/related_work.tex:125` | task-specific LoRA is "the parameter-isolation design used by Chen et al." | **Could be broadened:** MedPEFT-CL also uses per-task (partly shared) LoRA adapters, in a text-prompted model. |
| `thesis/related_work.tex:219–241` (positioning table) | rows Lifelong nnU-Net, Zhang et al., MedSeqFT, Chen et al. | **Missing row:** Language "descriptive attribute-based text prompts (from [29])"; 3D FM "no (2D CLIPSeg)"; Few-shot "no"; Setting "sequential datasets (3 sequences); task identity at inference not stated"; Strategies "proposed method, seq. FT, individual, EWC, LwF, PackNet, PNN, DER, VR-LwF, Low-Rank MoE, MoE-Adapters". |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
Thesis setting (from `gonzalez2023lifelong.md`, Sec. 10): tasks are **different structures from one dataset** (SKM-TEA), a pretrained free-text promptable 3D model (VoxTell), few-shot supervision, loss of pretrained ability measured on a control task.
1. **Relation to this thesis:** the closest prior work found so far on the model and strategy axes. Shared: a pretrained text-prompted segmentation VLM adapted continually; LoRA in the backbone; replay and regularisation; sequential fine-tuning as baseline; forgetting measured from per-task Dice. Different: 2D images and a 2D CLIPSeg backbone (not a 3D universal model); tasks are whole datasets (mostly different modalities), only the homogeneous sequence keeps one structure; full training sets (48–4800 training images per task) and a 15 % replay buffer; attribute-generated descriptive prompts; FR relative to peak Dice (the thesis uses absolute Chaudhry-style Final Forgetting); no zero-shot/control-task measurement; no task-order variation within a task set; task identity at inference not stated.
2. **Verdict on the gap claim:** "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model" is **not contradicted**, because the model and data are 2D. But it narrows the gap to the "3D" and "few-shot" (and control-task/pretrained-ability) dimensions: continual adaptation of a text-prompted medical segmentation model, with a comparison of established CL strategies, **has** been studied in 2D (MedPEFT-CL, PA-EWC). The thesis text must say so explicitly; otherwise an examiner can point to these two papers.
3. **Evidential weight:** peer-reviewed (WACV 2026, per external record) but internally inconsistent (Sec. 7, items 1–4), no variances, no code, hyperparameters possibly selected on test results. Cite for setting and design; quote numbers sparingly and from the version cited (check the WACV camera-ready first).
4. Useful for design arguments: (a) precedent for LoRA in a text-prompted segmenter and for comparing PEFT, replay and EWC; (b) Table 8: PEFT alone (61.31 / 20.32) forgets more than full sequential fine-tuning (67.71 / 15.36, Table 5) — relevant when interpreting shared LoRA vs sequential fine-tuning in this thesis, but the PEFT-baseline configuration is not specified; (c) replay gives the largest gain (Table 8), relevant for shared LoRA + replay; (d) prompt-similarity-based adapter reuse is an alternative to task-aware inference that the thesis does not evaluate (possible examiner question: why not route adapters by text prompt?).
5. Bib: use the WACV 2026 proceedings entry (CVF Open Access) once verified; author list must be checked (arXiv: one author; UCL record: two).
