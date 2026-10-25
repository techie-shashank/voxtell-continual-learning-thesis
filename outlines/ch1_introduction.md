# Ch. 1 Introduction — outline, revision 2 (PROPOSED 2026-10-23, awaiting approval)

Revision 2 is built from the thesis as it now stands (Ch. 2.5 gap and interview, Ch. 3–6 drafts, `thesis_notes.md`, `cl_metrics.csv`), not from the old `introduction.tex`. Nothing is taken over from the old text; citations are chosen per claim. Revision 1 and the interview record are kept at the end.

## What the chapter must do (and the reader it is for)
- Supervisor: problem statement, motivation, objectives, main contributions. Chair §1.5: motivation and problem in words, understandable for a reader outside the field, connection to prior work with citations.
- Reader: a computer scientist who knows deep learning but not medical segmentation or continual learning. After Ch. 1 they must know: what a free-text promptable 3D model is; why it needs to learn new structures; why doing so one after another with few labels is hard; what exactly this thesis measures and compares; what is new and what is not.
- One story line, told once: **capable general model → fails on a rarely seen anatomy → must learn new structures from few annotated volumes, one after another → learning them can destroy what it knew → which strategy gives which trade-off is unknown for this kind of model → we measure it.**

## Ground rules
- ≈ 5 pp. (guide). No section repeats Ch. 2 in detail; prior work appears only where it carries the argument, with pointers to Ch. 2.
- Concepts informal (decision 2026-10-22): forgetting, stability vs plasticity, few-shot, task. No TIL/CIL/DIL, no method-family taxonomy (Ch. 2.3).
- Terms introduced in the order the reader needs them, each defined once in words: free-text promptable (1.1), task (1.2), few-shot / shot (1.2), control task (1.4); metric names only informally (adaptation, forgetting, loss of pretrained ability).
- Numbers: VoxTell zero-shot mean 10.72 % DSC on SKM-TEA (VoxTell Table 9); our pretrained model 0.114 mean DSC over the six structures, 0.979 on the control task (`cl_metrics.csv`, Pretrained-model rows, `adaptation`, `control_pretrained`). No result of the strategy comparison in Ch. 1 (results are provisional; contributions are stated as what was done, not what was found, until the results analysis).
- Gap claim with the same wording basis and strength as 2.5.
- Rerun-dependent items marked `\todo`.

## 1.1 Motivation (≈ 1.25 pp.) — `sec:intro-motivation`
Paragraph plan (one idea each):
1. **Segmentation and the cost of labels.** What 3D segmentation is and what it is used for, in two sentences; manual voxel-wise annotation of 3D volumes is slow and needs experts (MRI-specific: `desai2021skmtea` Sec. 1; general: `Litjens_2017` only if the source check supports it, else `\todo{cite}`).
2. **From one model per structure to one model for many.** nnU-Net as the strong per-dataset approach (`isensee2018…`); universal models segment many structures with one network, steered by a prompt; spatial prompts (points, boxes) and text prompts as two parallel lines (one sentence, pointer `\cref{sec:text-promptable-seg}`).
3. **Free-text promptable models.** Define: the target is named in free text, not chosen from a fixed list of class names; SAT (fixed vocabulary, `zhao2025sat`) vs VoxTell (free text, `rokuss2025…`). Why this matters for the thesis: one network with one set of weights serves every structure, and the text prompt, not a separate output head, selects the target.
4. **Where such a model fails.** VoxTell's own zero-shot evaluation on knee MRI: 10.72 % mean DSC over six structures; our pretrained model 0.114 (forward pointer `\cref{chap:experiments}`). Rarely seen, not unseen: cartilage is in VoxTell's training vocabulary, menisci are not (`data_description.tex:96` basis).
5. **Why the knee structures matter.** Cartilage and menisci segmentations locate the tissue regions in which quantitative MRI biomarkers of tissue health, e.g. for osteoarthritis, are measured (Desai et al., secondary for the osteoarthritis link → cite Desai for its statement; primary source optional `\todo{cite}`).
6. **The practical situation.** Annotations for such structures arrive a few volumes at a time, and structures are added one after another as annotations become available (2.5 interview). Without naming an actor (author's choice, Q1).

## 1.2 Problem Statement (≈ 1 p.) — `sec:intro-problem`
1. **The task sequence.** A *task* = learning one new target structure, named by one text prompt; tasks arrive in sequence; the model must serve all of them afterwards. (Here: six knee structures; detail in 1.4.)
2. **Three requirements, one trade-off.** (i) learn the new structure (adaptation); (ii) keep the structures learned earlier in the sequence; (iii) keep what the pretrained model could already do (pretrained ability). Updating shared weights for (i) can destroy (ii) and (iii): catastrophic forgetting (`french1999catastrophic`); the tension between learning and keeping as stability vs plasticity (`van_de_Ven_2025`). Forgetting in this thesis covers both (ii) and (iii) (Q3).
3. **Why few labels make it harder.** Few-shot here = fine-tuning on k labelled volumes per task, one shot = one labelled training volume (not in-context segmentation at inference; pointer `\cref{sec:sota-few-shot}`). Fewer volumes mean fewer updates per task for the same number of epochs, so a strategy may adapt less (and forget less); and annotation cost is what keeps k small in practice (author, Q2).
4. **Why existing continual-learning results do not settle it.** Concrete differences, each one sentence: (a) continual-learning methods for pretrained vision–language models were built and evaluated for classification or text output (`liu2026…`, pointer `\cref{sec:cl-vlm}`); (b) continual learning for medical segmentation mostly concerns task-specific networks or adds structures as new output channels, while here all structures share one network and the text prompt selects the target (`\cref{sec:cl-medseg}`); (c) the closest works lack 3D, few-shot or free text, and none measures the pretrained ability kept (2.5). Gap sentence as in 2.5 ("In our search … we found no work that …").

## 1.3 Research Question and Objectives (≈ 0.6 p.) — `sec:intro-rq`
- Research question unchanged (CLAUDE.md), displayed, bold.
- One sentence on how it is read: "forgetting" includes the loss of pretrained ability (Q3); "few-shot conditions" = k = 5, 10, 20 next to the full training data (Q4, exact strategy list in 1.4).
- Objectives as a plain enumerated list, no bold:
  1. a few-shot continual-learning evaluation protocol (as in CLAUDE.md);
  2. compare strategies under it in adaptation and forgetting;
  3. influence of the amount of labelled data, incl. equal-updates ablation (Q5);
  4. influence of task order, LoRA rank and strategy components (replay; after reruns weight ensemble, gradient scaling) (Q5).

## 1.4 Approach and Scope (≈ 0.9 p.) — `sec:intro-approach`
Replaces a separate "Scope" section: the reader learns what is done and where its boundaries are in one place.
1. **Setting.** Pretrained VoxTell; six SKM-TEA structures as six tasks (`desai2021skmtea`), in two task orders (original, reverse); AeroPath lung as *control task*, never trained, used only to measure loss of pretrained ability (`støverud2023…`; replay exception until the rerun, `\todo`).
2. **Strategies.** Sequential fine-tuning as baseline; task-specific LoRA, shared LoRA, shared LoRA with replay, distillation-based strategy (adapted from ZSCL), prompt-tuning strategy (adapted from CPE-CLIP); chosen to cover the three paradigms of `\cref{sec:cl-vlm}`. Full names at first use per CLAUDE.md.
3. **Data amounts.** All strategies with the full training split; sequential fine-tuning, task-specific LoRA and shared LoRA also with k = 5, 10, 20 (same sentence as 2.5; `\todo` after reruns); `\todo{defense}` D46.
4. **Measures.** Adaptation, forgetting within the sequence, loss of pretrained ability on the control task (pointer `\cref{sec:method-protocol}`, `\cref{sec:bg-cl}` / metrics section).
5. **Delimitations** (2–3 sentences): no new method; one model, one dataset, one control task, one fixed text prompt per structure, one draw per k → conclusions limited to this setting (detail Ch. 7); clinical deployment and user studies out of scope; training cost is reported (`\cref{sec:exp-compute}`).

## 1.5 Contributions (≈ 0.5 p.) — `sec:intro-contributions`
`\todo{provisional: finalise after the results analysis}`. Plain enumerated list, each with a pointer to where it is supported:
1. An evaluation protocol for few-shot continual adaptation of a free-text promptable 3D segmentation model that measures adaptation, forgetting and the loss of pretrained ability on a held-out control task, and a systematic evaluation under it (Q6; "protocol", not "benchmark").
2. A comparative analysis of the strategies' adaptation, forgetting, transfer and retention with full and few labelled data (CLAUDE.md contribution 2, wording aligned).
3. An analysis of factors: amount of labelled data, task order, adaptation configuration (rank, components) (CLAUDE.md contribution 3).
Closing sentence separating own from prior work: the strategies are existing methods; their adaptation to VoxTell (distillation-based, prompt-tuning), the protocol and the experiments are this thesis's work.

## 1.6 Thesis Outline (≈ 0.3 p.) — `sec:intro-outline`
One paragraph, one sentence per chapter 2–8 with `\cref{chap:…}`; labels `chap:discussion`, `chap:summary` to add when those chapters exist.

## Figure
None in Ch. 1 (author, Q7). **Correction:** Ch. 5 has no protocol figure (only `fig:ch5_voxtell`; Ch. 3 has `fig:ch3_metrics`). Options for the author: (a) no figure reference in Ch. 1; (b) refer to `fig:ch3_metrics` in 1.4 for the measures; (c) a protocol figure in Ch. 5.1 (task sequence + control task + evaluation matrix), referenced from 1.4 — suggestion only, it would add a page-budget item.

## Differences from the old introduction (for the author's check)
- Opens with the model's failure on a concrete anatomy, not with a general history of segmentation; no background sections on CNNs, modalities or CL families.
- Problem framed as three requirements (learn, keep earlier tasks, keep pretrained ability) instead of "new distributions".
- Explains why existing CL results do not transfer with concrete differences (shared network, text prompt selects the target, classification-only evaluation) instead of "architectural complexity".
- New "Approach and Scope" section: setting, strategies, data amounts and measures stated before the contributions; scope reduced to delimitations.
- Few-shot defined (shot = one labelled volume, fine-tuning) and why it matters (fewer updates, annotation cost).
- No results claimed; contributions provisional.

## Open for the author before drafting
- Approve revision 2 (structure, order, section titles).
- Q1 rest: name an actor in 1.1 ¶6 or not (default: not).
- Figure option (a)/(b)/(c).

---

## Interview round 1 — answers (2026-10-23)
- **Q1** Ch. 4 does not answer it (labels and pathologies only, `data_description.tex:47, 51`); the dataset README neither. The SKM-TEA paper (local arXiv v1; bib cites the NeurIPS 2021 D&B version, so no page locators until checked) gives: dense MRI annotations are cumbersome to curate and vary between readers (Sec. 1); qDESS T2 is sensitive to collagenous tissue degeneration and yields quantitative biomarkers for osteoarthritis, and qMRI analysis needs the regions of interest localised by hand (Sec. 2, "Quantitative MRI"); SKM-TEA provides tissue-wise biomarker maps from the segmentations (Sec. 1, contribution 1). The osteoarthritis and T2 claims are Desai et al.'s statements with their own references (secondary). Who adapts the model: not in any source, open for the author.
- **Q2** Author: fewer updates per task and annotation cost.
- **Q3** Author: RQ unchanged, forgetting defined in 1.2 for earlier tasks and pretrained ability.
- **Q4** Accepted (author, 2026-10-23): keep the RQ; state exactly which strategies have few-shot runs (same sentence as 2.5); `\todo{defense}` D46.
- **Q5** Accepted: objective 3 = amount of labelled data incl. equal-updates ablation; objective 4 = task order, LoRA rank, strategy components; patellar diagnosis not an objective.
- **Q6** Accepted: protocol merged into contribution 1 ("protocol", not "benchmark"), provisional.
- **Q7** Author: no figure in Ch. 1.
