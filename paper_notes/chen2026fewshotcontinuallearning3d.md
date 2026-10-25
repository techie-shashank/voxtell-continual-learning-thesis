# Chen et al. 2026 (few-shot CL, 3D brain MRI, frozen FM + LoRA) — paper notes

Read as the closest prior work for Ch. 2 (State of the Art): few-shot continual learning with task-specific LoRA on a frozen 3D medical foundation model.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Chi-Sheng Chen, Xinyu Zhang, Guan-Ying Chen, Qiuzhe Xie, Fan Zhang, En-Jui Kuo. *Few-Shot Continual Learning for 3D Brain MRI with Frozen Foundation Models.* arXiv:2602.23533v1 [eess.IV], 26 Feb 2026. 14 PDF pages (8 main incl. conclusion, references p. 8–9, appendix of figures p. 10–14) |
| Local PDF | `papers/t6_cl_medseg_foundation/chen2026fewshotcontinuallearning3d.pdf` |
| Bib key | `chen2026fewshotcontinuallearning3d` (`@misc`, arXiv) |
| Version read | arXiv v1. **No peer-reviewed venue stated** in the PDF. Affiliations include independent researchers (p. 1) |
| Code | Not given in the PDF |
| Notes written | 2026-10-22, by Claude, from arXiv v1. Page numbers = PDF pages |

## 1. Problem and idea (abstract, Sec. 1, p. 1–2)
- Clinical setting: new analysis tasks are added over time with few labelled cases and without access to earlier task data (p. 1).
- Sequential fine-tuning of shared parameters forgets; EWC/LwF need tuning and may still overwrite representations (p. 1).
- Idea: freeze a pretrained 3D backbone and train **one LoRA adapter plus one head per task**; earlier adapters and the backbone stay frozen, so **BWT = 0 by design** (p. 1–2, Fig. 1).
- Contributions (p. 2): the formulation; validation on BraTS and IXI; ablations of LoRA placement and shot count.

## 2. Setting (Sec. 2.1, 2.3, 5.3; p. 2–3, 7)
- Authors' term: **task-incremental** few-shot continual learning across heterogeneous outputs (Sec. 5.3, p. 7).
- **Task** = a different downstream problem with its own output type: T1 tumour segmentation (BraTS), T2 brain-age regression (IXI) (Sec. 2.1, p. 2; Sec. 3.1, p. 3). Each task has modality-specific inputs (BraTS: T2w, T2-FLAIR, T1c; IXI: T1, T2) (p. 2).
- **Task identity at inference: yes** — backbone + adapter k + head k are loaded for task k (Sec. 2.3, p. 3; Fig. 1).
- **Few-shot:** N_k ∈ {16, 32, 64} labelled samples per task (Sec. 2.1, p. 2); main results with n_shot = 32 (Sec. 4.1, p. 4).
- **No replay** of earlier task data (p. 2).
- Two tasks only; two orders (seg → regression; regression → seg, "Phase 3", Sec. 4.5, p. 6).

## 3. Method (Sec. 2.2–2.4, p. 3)
- LoRA W' = W + B·A, A ∈ R^{r×k}, B ∈ R^{d×r} (Eq. 1); for 3D convolutions realised as **1×1×1 convolutions** (linear in the channel dimension) (p. 3).
- Rank r ∈ {4, 8, 16}, default **r = 8, α = 16**; LoRA in **encoder and decoder** for segmentation, **encoder only** for regression (p. 3).
- Per task: freeze backbone f and all earlier adapters; add LoRA_k and head h_k; train only these on the few-shot samples; save; continue (Sec. 2.3, p. 3). No shared adapter.
- Trainable share: < 0.1 % of the ≈ 50M backbone parameters per task (p. 3). Table 8 (p. 8): 46,872 trainable parameters for T1, 28,177 for T2.
- Heads and losses: T1 full UNet decoder, **Dice + BCE**; T2 "ClsRegHead" with one output, **MSE** (Sec. 2.4, p. 3).

## 4. Data (Sec. 3.1, p. 3)
- Public datasets used "via Plan B" because FOMO downstream data were unavailable (p. 3). T1/T2 correspond to FOMO Task002/Task003.
- **BraTS 2023 Glioma**: 1,251 training cases, 3 channels (T2w, T2-FLAIR, T1c), binary tumour mask from expert annotations; 3D MRI (p. 3).
- **IXI**: 577 subjects with T1 and T2 scans and age labels; target age in years; **missing ages imputed to 50.0 years** (p. 3).
- Preprocessing: per-channel z-score, 64³ patches, few-shot sampling 16/32/64 with fixed seeds, **validation split 20 %** (p. 3). A separate test split is not stated; IXI evaluation is on the validation set (n = 109, seed 42) (p. 5).
- Task order main: T1 (segmentation) → T2 (regression); reverse order in Sec. 4.5 / Table 6.

## 5. Implementation (Sec. 3.2, 3.5; p. 4)
- Backbone: **FOMO `unet_b`**, weights `fomo25_mmunetvae_pretrained.ckpt`; **59/82 keys loaded** for the full UNet (T1), 39/40 encoder keys for encoder-only (T2) (Sec. 3.2, p. 4).
- Seeds 42, 43, 44; 100 epochs per task; batch size 2; learning rate 10⁻³; Adam; LoRA r = 8, α = 16, dropout 0.1; 1× NVIDIA RTX 3090 (24 GB) (Sec. 2.4 p. 3; Sec. 3.5 p. 4).
- Resources (Table 8, p. 8): T1 peak GPU 1,670 MB, time ~4k–26k s; T2 688 MB, ~95–780 s.

## 6. Evaluation protocol and metrics (Sec. 3.3–3.4, p. 4)
- T1: Dice; T2: MAE **in years** (p. 4).
- **BWT** = R_{T,k} − R_{k,k}: for seg → regression, T1 Dice after T2 minus T1 Dice right after T1 (negative = forgetting); for the reverse order, T2 MAE after T1 minus right after T2 (positive = forgetting) (p. 4).
- Baselines (Sec. 3.3, p. 4): Sequential Linear (frozen backbone, heads/decoder trained sequentially, one shared model); Sequential FT (full fine-tuning); EWC; LwF (feature distillation from previous-task model); Replay (stored samples, distillation on replay); proposed LoRA.
- Reference: **Per-task Linear** (separate model per task, patch 32, 50 epochs; called "Oracle (no continual)") in Table 2 (p. 6). No joint-training upper bound.
- Statistics: paired t-tests across 3 seeds; bootstrap CI; Wilcoxon test on IXI residuals (p. 4–5).

## 7. Results
- **Table 1 (p. 5), n_shot = 32, mean ± std over seeds 42–44** (T1 Dice / T2 MAE / T1 after T2 / BWT):
  - LoRA (enc+dec) 0.60 ± 0.08 / 0.012 ± 0.003 / (= T1) / 0.00
  - Sequential Linear 0.79 ± 0.01 / 1.45 ± 0.03 / 0.78 ± 0.01 / −0.01 ± 0.01
  - Sequential FT 0.80 ± 0.02 / 0.005 ± 0.003 / 0.16 ± 0.19 / −0.65 ± 0.17
  - EWC 0.79 ± 0.02 / 0.001 ± 0.001 / 0.15 ± 0.24 / −0.65 ± 0.23
  - LwF 0.80 ± 0.02 / 0.020 ± 0.009 / 0.25 ± 0.22 / −0.56 ± 0.24
  - Replay 0.79 ± 0.01 / 0.021 ± 0.013 / 0.01 ± 0.01 / −0.78 ± 0.02
  - Authors flag Seq FT and EWC T2 MAE as implausibly low, likely overfitting to the few-shot validation set (Table 1 caption; Sec. 5.2, p. 7).
- Table 2 (p. 6): Per-task Linear T1 Dice 0.65, T2 MAE 0.063.
- Statistics (p. 4): LoRA vs Sequential Linear on T2 MAE p = 0.001 (LoRA better); on T1 Dice Sequential Linear higher, 95 % CI of difference [0.08, 0.27], **p = 0.09**.
- Sec. 4.2 (p. 5): Seq FT T1 Dice 0.80 → 0.16 after T2, "Δ ≈ 0.64".
- **Placement ablation, Table 3 (p. 7):** encoder-only T1 Dice 0.19, T2 MAE 0.20; encoder+decoder 0.50, 0.20.
- **Shot ablation, Table 4 (p. 7), LoRA:** 16 shots T1 0.45 ± 0.04, T2 MAE 0.33 ± 0.01 (seeds 42–43); 32 shots 0.62 ± 0.07, 0.16 ± 0.05. No 64-shot LoRA row although Sec. 4.4 heading names 64.
- **Table 5 (p. 8), 64 shots:** EWC T1 0.84 ± 0.02, T2 MAE 0.001, T1 after T2 0.07 ± 0.10, BWT −0.77 ± 0.11; LwF 0.82 ± 0.01, 0.038 ± 0.014, 0.25 ± 0.41, −0.58 ± 0.42.
- **Reverse order, Table 6 (p. 8):** LoRA T1 Dice 0.50 ± 0.08, T2 MAE 0.005 ± 0.002, BWT 0.00; Sequential Linear 0.78 ± 0.01, 0.26 ± 0.003, T2 after T1 0.36 ± 0.05, BWT 0.10 ± 0.05; Sequential FT 0.81 ± 0.01, 0.001, 7.17 ± 1.41, BWT 7.16 ± 1.41.
- **Per seed, Table 7 (p. 8):** T1 Dice 0.523 / 0.598 / 0.680; T2 MAE 0.014 / 0.008 / 0.012.
- Wilcoxon on IXI residuals: significant systematic **underestimation** of age (p < 0.001); the six best IXI samples all have ground truth 50.0 y, i.e. imputed labels (p. 5).
- **Internal inconsistencies in the paper** (reported as found, not interpreted): LoRA 32-shot T1 Dice is 0.60 ± 0.08 (Tables 1–2, Sec. 5.2), 0.62 ± 0.07 (abstract, Sec. 1, Table 4) and 0.50 (Table 3, enc+dec); LoRA T2 MAE is 0.012 ± 0.003 (Table 1) vs 0.16 ± 0.05 (abstract, Table 4) vs 0.20 (Table 3). The conclusion lists task-order and 64-shot experiments as future work (p. 8) although Sec. 4.5 and Table 5 report them. Task labels switch between "T1/T2" and FOMO numbering "T2/T3" (Sec. 4.5, Sec. 6).

## 8. Limitations and future work (authors; Sec. 5.2 p. 7, Sec. 6 p. 8)
- LoRA's segmentation Dice (0.60) is below Sequential Linear (0.79) and Sequential FT (0.80); possibly LoRA capacity or decoder adaptation.
- Systematic brain-age underestimation; IXI age imputation limits interpretability of T2 MAE.
- Infarct detection (ISLES 2022) of the FOMO formulation not evaluated (no negative controls); deferred.
- Implausibly low T2 MAE of Seq FT and EWC suggests overfitting to the few-shot validation set.
- Future work (p. 8): task-order ablation and 64-shot experiments.

## 9. Check of the author's notes
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:98` | "few-shot form of the problem for a frozen 3D foundation model of brain MRI" | **Correct** (abstract; Sec. 3.2, p. 4). Note only 59/82 keys of the full UNet are loaded from the pretrained checkpoint (p. 4). |
| `related_work.tex:98` | "Each task receives a dedicated LoRA module and prediction head" | **Correct** (Sec. 2.3, p. 3; Fig. 1). |
| `related_work.tex:98` | "tumour segmentation on BraTS followed by brain-age estimation on IXI in a 32-shot setting" | **Correct** for the main experiment (Sec. 4.1); 16-shot, 64-shot (baselines only) and reverse order also reported. |
| `related_work.tex:98` | "fewer than 0.1 % of the backbone parameters trained per task" | **Correct** (Sec. 2.2, p. 3; Table 8). |
| `related_work.tex:98` | "backward degradation is excluded by construction" | **Correct** (Sec. 2.3, p. 3). |
| `related_work.tex:98` | "sequential full fine-tuning reduced the DSC of the first task from 80 % to 16 %" | **Partly correct.** Numbers right (0.80 → 0.16, Table 1, Sec. 4.2), but the paper reports Dice in [0, 1] form, so by the thesis convention it should be quoted as 0.80 → 0.16. |
| `related_work.tex:98` | "requires the task to be identified at inference, its two tasks produce different prediction types through dedicated heads, and the model is not addressed through natural-language prompts" | **Correct** (Sec. 2.3; Sec. 2.4; no text input anywhere in the paper). |
| `related_work.tex:105` (comment) | "32-shot DSC 0.62 +/- 0.07 (BraTS)" | **Partly correct.** 0.62 ± 0.07 is in the abstract and Table 4, but the main Table 1 gives **0.60 ± 0.08**, consistent with the per-seed values of Table 7 (mean 0.600, my computation). Paper is internally inconsistent; cite the table you use. |
| `related_work.tex:105–106` (comment) | "brain-age MAE 0.16 +/- 0.05 on a normalised scale (not years)" | **Not found in the paper.** The paper defines MAE "in years" (Sec. 3.4, p. 4); it does not mention a normalised scale. It does flag MAE < 0.01 as implausible/overfitting. 0.16 ± 0.05 is from abstract/Table 4; Table 1 gives 0.012 ± 0.003. |
| `related_work.tex:105–106` (comment) | "LoRA rank 8" | **Correct** (Sec. 2.2, 3.5). |
| `related_work.tex:115` | "address few-shot continual adaptation of a 3D foundation model **only** through task-specific modules selected by task identity" | **Partly correct.** The proposed method is task-specific, but the paper also evaluates shared-parameter strategies on the same backbone (Sequential FT, EWC, LwF, Replay, Sequential Linear; Table 1). "Only" should refer to the proposed method. |
| `related_work.tex:125` | "Task-specific LoRA adapters, the parameter-isolation design used by Chen et al." | **Correct** (Sec. 2.3). |
| `related_work.tex:216` (summary table) | "BraTS → IXI, 32 shots; TIL; per-task LoRA and head, frozen backbone; DSC 62 %; FFT drops task 1 from 80 to 16 %" | **Partly correct.** Setting correct. DSC: Table 1 gives 0.60 ± 0.08 (0.62 only in abstract/Table 4); use the paper's [0, 1] form. |
| `related_work.tex:236` (positioning table) | Language none; 3D FM yes; few-shot yes; TIL; strategies "Proposed method, sequential fine-tuning, EWC" | **Partly correct.** Strategies list is incomplete: also Sequential Linear, LwF, Replay, and the Per-task Linear oracle (Sec. 3.3, Tables 1–2). Other cells correct. |
| `thesis/introduction.tex:29` | cited as a recent study of continual learning for medical foundation models | **Correct** (frozen FOMO-pretrained backbone). |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
1. **Closest setting so far:** 3D, segmentation as one task, pretrained medical backbone, few-shot (16/32 shots), task-specific LoRA with task identity at inference, sequential FT/EWC/LwF/replay compared. This matches the thesis's task-specific LoRA strategy and its sequential fine-tuning baseline.
2. **Differences:** no language interface; a **task is a different output type** (segmentation vs regression) with its own head, not a different structure under one segmentation output; only two tasks; no measurement of loss of pretrained ability (no control task); no shared-adapter or prompt-tuning strategy; evaluation on a 20 % validation split, no separate test split stated; 3 seeds, no variation of the few-shot sample beyond the seeds.
3. **Gap claim:** does **not** weaken "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model", because the model has no text prompt. It does weaken any broader claim such as "no prior work on few-shot continual learning of 3D medical foundation models"; the thesis should not phrase the gap that broadly.
4. Reliability caveats an examiner may raise if the thesis leans on this paper: arXiv only, internal inconsistencies (Dice 0.60 vs 0.62 vs 0.50; MAE 0.012 vs 0.16 vs 0.20), imputed IXI labels, partial loading of pretrained weights. Prefer citing it for the setting, not for exact numbers.
5. Its finding that task-specific LoRA gives BWT = 0 but lower Adaptation than full fine-tuning (0.60 vs 0.80 Dice) is a reference point for the thesis's task-specific LoRA vs sequential fine-tuning comparison; check against the thesis's own results before drawing any parallel.
