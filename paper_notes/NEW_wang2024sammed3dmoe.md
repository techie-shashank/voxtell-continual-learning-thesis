# SAM-Med3D-MoE (Wang et al., 2024) — paper notes

Read as prior work for Ch. 2 (State of the Art): a 3D medical segmentation foundation model (SAM-Med3D, point/box-promptable) extended to new classes and a new dataset by separately fine-tuned decoder experts behind a learned gate, keeping the original decoder as a fallback to avoid forgetting.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Guoan Wang, Jin Ye, Junlong Cheng, Tianbin Li, Zhaolin Chen, Jianfei Cai, Junjun He, Bohan Zhuang (Shanghai AI Laboratory; East China Normal University; Monash University; Sichuan University). *SAM-Med3D-MoE: Towards a Non-Forgetting Segment Anything Model via Mixture of Experts for 3D Medical Image Segmentation.* arXiv:2407.04938v1 [cs.CV], 6 Jul 2024 (PDF p. 1). 10 PDF pages: p. 1–8 paper, p. 9 Table 2 and references, p. 10 references |
| Local PDF | `papers/t6_cl_medseg_foundation/NEW_wang2024sammed3dmoe.pdf` |
| Bib key | **none yet** (cited in the author's notes as literal `[Wan+24]`) |
| Version read | **arXiv v1 (6 Jul 2024)**. The PDF does **not** state a peer-reviewed venue (LNCS-style layout with a "Disclosure of Interests" section, but no conference named). Whether a peer-reviewed version exists was not checked; check before creating the bib entry |
| Code | Not given: "Codes and datasets will be publicly available" (p. 1) |
| Notes written | 2026-10-23, by Claude, from arXiv v1. Page numbers = PDF pages (identical to the printed page numbers) |

## 1. Problem and idea (abstract, Sec. 1; p. 1–4, Fig. 1)
- Volumetric segmentation foundation models (SAM-Med3D, SegVol) perform well on general organs and tumours but poorly on some categories in clinical downstream tasks, e.g. neuroblastoma in children's MRI (SPPIN2023) (p. 1; p. 3; Fig. 1a).
- Stated reason: public medical data are small and not diverse; SegVol and SAM-Med3D "5.7k images with 149k corresponding masks and another 21k images with 131k corresponding masks", about 0.1 % of SAM's images and 0.01 % of its masks (p. 3). (Which number belongs to which model is given only by order; own reading: SegVol 5.7k/149k, SAM-Med3D 21k/131k.)
- Supervised fine-tuning (SFT) improves the downstream task but degrades the general knowledge (p. 3; Fig. 1b).
- Idea: a **mixture of experts** that merges the original model (**general expert**) with task-specific fine-tuned decoders (**specific experts**) into one model, at the cost of training an extra lightweight **gating network**, plus a **selector** that combines the general output with the top-1 specific expert (p. 3; Fig. 1c, Fig. 2 p. 4).
- Claimed contributions (p. 3–4): first MoE merging foundation-model and task-specific knowledge for volumetric segmentation; lightweight trainable gate and selector; evaluation on SPPIN2023 and 15 weak classes.

## 2. Setting (Sec. 2.1, p. 4; Sec. 3.1, p. 6–7)
- Not framed as a continual-learning sequence. The paper speaks of "Extensions on Downstream Tasks" and "Extensions on Weak Categories" and of mitigating catastrophic forgetting (p. 6). **No CL scenario name** (task-/class-/domain-incremental) is used.
- Experts are fine-tuned **separately** from the same foundation model, one per downstream task or category, and then assembled; there is **no sequential training** of tasks and no task order (p. 4; p. 6–7).
- A "task" = a downstream dataset (SPPIN2023, 1 expert) or one weak anatomical category (15 experts, one per category) (p. 6–7). Whether both experiments use one combined MoE is not stated.
- Task identity at inference: **not given**; the gate chooses the expert from image and prompt embeddings, supervised by cross-entropy on the correct expert during training (p. 5; p. 6).
- Not few-shot; amount of fine-tuning data per expert **not stated**.
- Prompts at inference: **6 points or a bounding box** (Table 1, Table 2 captions). Fig. 2 (p. 4) draws a "Text Prompt: Liver" as an input to the 3D prompt encoder, but Sec. 2 describes the prompt encoder as handling **point and box prompts only** (p. 4), and no experiment uses text. **Internal inconsistency**; text prompting is neither described nor evaluated.

## 3. Method (Sec. 2, p. 4–5; Fig. 2–3)
- **Base model:** SAM-Med3D: ViT-based 3D image encoder; prompt encoder for points and boxes (frozen 3D absolute positional encodings plus learned per-type embeddings); lightweight 3D mask decoder (p. 4).
- **Experts:** the original 3D mask decoder = general expert; task-specific experts = copies of the mask decoder fine-tuned **on the decoder alone**; image and prompt encoders shared and identical for all experts (p. 4).
- **Gating network (Sec. 2.2, p. 5, Fig. 3):** inputs image embedding X_i ∈ R^{(HWD/16³)×C} and prompt embedding X_p ∈ R^C; self-attention on the prompt, cross-attention prompt→image, MLP, cross-attention image→prompt, residuals and normalisation after each block, two fully connected layers and softmax → scores S ∈ R^m for m experts.
- **Mask selector (Sec. 2.3, p. 5):** with top-1 score s_top and threshold τ: M_o = (1 − s_top)·M_g + s_top·M_top if s_top > τ, otherwise M_o = M_g (general decoder only).
- **Trained vs frozen:** image and prompt encoders frozen; "confining updates exclusively to the parameters of the Top-1 expert mask decoder" during MoE training (p. 6). Elsewhere: "by only training the gating network" (p. 6) and "without updating any parameters of them" (abstract p. 1; Conclusion p. 8). **Internal inconsistency** about whether the expert decoders are updated after assembly; the general decoder is not described as updated.
- **Losses (p. 6):** DiceCE loss on the final prediction; cross-entropy on the gate output for selecting the correct expert.
- **Memory:** no replay; earlier knowledge kept in the frozen general decoder and in the stored expert decoders. GPU memory grows with the number of experts (p. 5–6).

## 4. Data (p. 3; p. 6–7; Fig. 4)
- **SAM-Med3D training data:** reused for training, "the same as that used for the initial baseline SAM-Med3D model" (p. 6); SAM-Med3D is described as trained on "over 100k volumetric masks" (p. 2). Composition, modalities and number of scans **not stated in this paper**.
- **SPPIN2023 (MICCAI 2023 challenge):** neuroblastoma segmentation in children's MRI, unseen by SAM-Med3D (p. 3; p. 6). Number of scans, splits, MRI sequences: **not stated**.
- **15 weak categories:** chosen because baseline SAM-Med3D performed poorly (p. 6). Names only on the x-axis of Fig. 4a (p. 8), read from the figure: oesophagus, small bowel, aorta, clavicula left, spinal cord, a thoracic vertebra (label not legible), gallbladder, pancreas, autochthon right, scapula right, lung upper lobe left, clavicula right, scapula left, hip right, vertebrae T1. Source dataset(s) of these classes: not stated.
- **"Other classes":** the remaining categories "within the validation dataset" (p. 7); which validation set and how many classes: not stated (Fig. 4b, p. 8, shows 15 such categories, own count from the axis labels, e.g. vertebrae C2–C7, sacrum, femur left, kidney right, brain, prostate&uterus, lung lower lobe right; whether Table 1 "Other classes" averages exactly these is not stated).
- All 3D. Train/validation/test splits: **not stated**.

## 5. Implementation (Sec. 3, p. 5–6)
- PyTorch; 15-expert variant trained on 8 NVIDIA V100 GPUs with 32 GB each; training speed "nearly on par" with baseline SAM-Med3D (p. 6). No runtime or memory numbers.
- AdamW; learning rate 1 × 10⁻⁴ for fine-tuning experts, 1 × 10⁻⁶ for the gate (p. 6).
- Epochs, iterations, batch size, patch/crop size, τ used in Table 1: **not stated**. Ablation uses τ = 0.5 and 0.7 (p. 7).
- Number of runs/seeds, variability: **not stated**.

## 6. Evaluation protocol and metrics (Sec. 3, p. 6–7)
- Metric: Dice, reported in [0, 1] in the tables (Table 1–2), in % in the abstract and introduction (p. 1, p. 4).
- References: **Baseline** = original SAM-Med3D; **FT-expert / Upper bound** = SAM-Med3D fine-tuned on the task or category (Table 1; Fig. 4; Table 2). No sequential fine-tuning, joint training or other CL baselines; no forgetting metric.
- Forgetting is read from performance on "Ori tasks" (original tasks SAM-Med3D learned) and "Other classes" (p. 6–7).
- Each result for 6-point and box prompts.

## 7. Results (Dice in [0, 1] as in the tables)
- **Table 1 (p. 7)**, Point/Bbox. Downstream: Ori tasks | SPPIN; weak categories: Other classes | finetune 15 classes:
  - Baseline 0.433/0.527 | 0.338/0.323 || 0.424/0.541 | 0.399/0.532
  - FT-expert 0.333/0.438 | 0.503/0.510 || 0.036/0.094 | 0.660/0.637
  - Ours 0.411/0.527 | 0.451/0.489 || 0.353/0.400 | 0.520/0.564
- Abstract figures (p. 1, p. 4): 15 classes 53.2 % → 56.4 % and SPPIN 48.9 % vs 32.3 % correspond to the **Bbox** column of Table 1 (own check); the point-prompt gains are larger (0.399 → 0.520; 0.338 → 0.451).
- Per-class gains of 29.6 % (spinal cord), 8.5 % (oesophagus), 11.2 % (right hip) (p. 1, p. 4): only shown as bars in Fig. 4a, prompt type not stated; not verifiable from numbers.
- FT-expert improves SPPIN by "approximately 17%" (p. 6); own calculation: +0.165 (points), +0.187 (box).
- **Forgetting:** Ori tasks: Ours 0.411 vs Baseline 0.433 (points), equal with box (0.527). Other classes: Ours 0.353/0.400 vs Baseline 0.424/0.541, i.e. −0.071/−0.141 (own calculation), much better than FT-expert (0.036/0.094).
  - **Text–table inconsistency:** the text says integration "did not detrimentally impact performance on the baseline categories" (p. 7) and maintains "stable or slightly decreased performance on the original task" (p. 6); Table 1 shows a drop of 0.141 Dice (box) on Other classes.
- **Ablation, Table 2 (p. 9)**, four categories (aorta, stomach, small bowel, oesophagus), Point/Bbox, weight mean:
  - Baseline 0.447/0.523; Upperbound 0.687/0.660; τ0.5 0.522/0.589; τ0.7 0.508/0.565; Avg 0.480/0.588; Aft_weight 0.040/0.458.
  - Higher τ lowers accuracy (biases toward the general decoder); the s_top-weighted sum is best (p. 7). Avg and Aft_weight use τ = 0.5 (p. 7).
- Table 1 values of "Ours" are printed in red without explanation (p. 7).

## 8. Limitations stated by the authors (Conclusion, p. 8)
- Future work: (1) verify on more medical segmentation foundation models; (2) τ should be adapted dynamically to the scenario.
- Memory usage grows with the number of experts (p. 5–6), stated as a property, not as a limitation.
- No other limitations stated.

## 9. Check of the author's notes
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:92` | "adds task-specific mask-decoder experts to the volumetric segmentation foundation model SAM-Med3D behind a gating mechanism" | **Correct** (p. 4, Fig. 2; Sec. 2.2). |
| `thesis/related_work.tex:92` | "while retaining its general image and prompt encoders" | **Correct** (shared and frozen, p. 4; p. 6). |
| `thesis/related_work.tex:92` | "falls back to the original decoder when no expert is appropriate" | **Correct with a nuance.** Fallback when the top-1 score ≤ τ (Sec. 2.3, p. 5). When an expert is chosen, its mask is **fused** with the general decoder's mask by an s_top-weighted sum, not used alone. "Appropriate" = top score above threshold τ. |
| `thesis/related_work.tex:92` | citation `[Wan+24]` | **No bib entry exists yet**; needs an entry (arXiv 2407.04938v1 unless a peer-reviewed version is found). |
| `thesis/related_work.tex:64` (MoE paragraph) | — | Not cited there; the paper would fit as the medical, 3D example of MoE routing. |
| `thesis/related_work.tex:115` | "most of its methods hold the capability added in each task in dedicated components that are reached through task identity, a routing decision, or a closed set of classes" | **Consistent** with this paper (routing by a learned gate, p. 5); the paper is not named there. |
| `thesis/related_work.tex:210` (summary table) | Data "--"; approach "Gated decoder experts on frozen SAM-Med3D"; result "--" | **Approach correct** (encoders frozen, p. 6; general decoder kept). **Data and result missing:** data = SAM-Med3D training data, SPPIN2023 (paediatric neuroblastoma MRI), 15 weak categories (p. 6–7); result e.g. 15 classes 0.532 → 0.564 and SPPIN 0.323 → 0.489 (Bbox, Table 1, p. 7), with Other classes 0.541 → 0.400. |
| `thesis/related_work.tex` positioning table | — | **Not found** (no row). |
| `thesis/introduction.tex` | — | **Not found.** |
| `% SUMMARY TABLE` comment (`related_work.tex:100–106`) | — | **Not found.** |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
Thesis setting (from `gonzalez2023lifelong.md` §10 and CLAUDE.md): continual adaptation of the pretrained free-text promptable universal 3D model VoxTell to six tasks (structures, one text prompt each) of one MRI dataset (SKM-TEA), few-shot, original and reverse task orders, with a held-out control task.
1. **Relation to this thesis:** shares the core concern (adapt a pretrained 3D segmentation foundation model to new structures without losing pretrained ability) and the measurement of pretrained ability on original classes, comparable in spirit to the thesis's control task. Differences: spatial (point/box) prompts, not free text; experts trained independently, no sequence or task order; full data, not few-shot; one strategy (its own MoE) vs SFT, no CL baselines; no seeds.
2. **Gap claim:** does **not** weaken "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model". Risk: Fig. 2 shows a text prompt ("Liver") entering the prompt encoder; an examiner reading only the figure might call it text-promptable. Defence: Sec. 2 limits the prompt encoder to points and boxes (p. 4) and all experiments use 6 points or a box (Table 1–2). Also it is not sequential continual learning.
3. The result that the foundation model fine-tuned on one dataset collapses on other classes (Other classes 0.424/0.541 → 0.036/0.094, Table 1) is a 3D medical example of the forgetting of pretrained ability that motivates the control task; quote with its prompt type.
4. Like task-specific LoRA in the thesis, it isolates new knowledge in per-task modules; unlike it, selection is by a learned gate instead of the given task identity, and the gate can misroute (the drop on Other classes suggests routing errors; the paper does not analyse this).
5. Do not reuse the abstract's "56.4 %" or "48.9 %" without stating that they are box-prompt values; note the text–table inconsistency on forgetting (p. 7 vs Table 1).
