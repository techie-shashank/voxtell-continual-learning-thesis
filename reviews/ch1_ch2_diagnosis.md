# Diagnosis: Chapter 1 (Introduction) and Chapter 2 (State of the Art)

Date: 2026-10-18. Diagnosis only, no edits made.

Files reviewed: `thesis/introduction.tex` (79 lines, pp. 1–6) and `thesis/related_work.tex` (244 lines, pp. 7–~22).
Both were checked against `guidelines/supervisor_guidelines.md`, `guidelines/chair_guidelines.md`, `CLAUDE.md`, `thesis_notes.md`, `results/experiment_index.csv`, `thesis/tables/cl_metrics.csv`, `thesis/literature.bib`, the last build log (`thesis/thesis_main.log`) and the strategy code in `code/src/continual/strategies/`.

Severity: **M** = must fix, **S** = should fix, **m** = minor.
Line numbers refer to the source lines. Both files have one paragraph per line, so a line number usually means a whole paragraph.

---

## 0. Most important findings

1. **The main comparison is not few-shot.** Every run with role `Main` in `results/experiment_index.csv` has an empty `train_max_cases`, so it trains on the full training split (108 SKM-TEA volumes per task, `thesis_notes.md` §2). Only sequential fine-tuning, TIL-LoRA (r = 4) and CIL-LoRA (r = 1024) have 5/10/20-volume runs. ZSCL and CPE-CLIP have none. Even so, the research question (intro L36), L5, L24, chapter 2 L40/L122 and the positioning table (L238, "Few-shot: yes") present the whole comparison as few-shot. This is the biggest gap an examiner could attack.
2. **The motivation describes a different setting from the one tested.** Chapter 1 motivates adaptation with new imaging conditions, modalities, pathologies and acquisition settings (L3, L15). The six tasks are six knee structures in the same SKM-TEA MRI scans (`tasks` column of `experiment_index.csv`). The pretrained model's low Dice on these tasks (mean diagonal 0.114, `cl_metrics.csv`, "Pretrained model" row) would be a stronger, direct motivation, but it is not used.
3. **Preserving the pretrained model's own abilities (the control task) is not mentioned in either chapter.** It is one of the six metrics (`thesis_notes.md` §1), and chapter 2 L46 argues that it matters. The research question, objectives and the chapter 2 summary (author TODO at L123) do not name it.
4. **Chapter 2 is incomplete for the supervisor's per-paper requirement.** About half the reviewed works have no dataset size, no labels, or no quantitative best result (see table C-2.1). Several works are cited in chapter 1 as closest prior work but never reviewed in chapter 2 (`Zhang_2025`, `chen2025forgingdynamicmemoryretrievalguided`).
5. **Citation problems break the build.** There are 5 literal placeholder labels, 2 missing bib keys (`wu2024gift`, `moe4cl2024`), the undefined reference `subsec:zscl`, a duplicate BiomedParse entry, and about 40 entries cited as arXiv/`@misc`, many of which have peer-reviewed versions.
6. **Contributions are stated as final** (intro L55–66). CLAUDE.md marks them as provisional.

---

## 1. Issues

### 1.1 Structure

| ID | File:line | Sev. | Issue | Suggestion |
|---|---|---|---|---|
| S-1.1 | introduction.tex:80 | M | No thesis outline. The commented-out outline is outdated: it describes 6 chapters, with Experiments as chapter 5 and Summary as chapter 6, while the thesis has 8. Required by CLAUDE.md and expected by the chair. | Write a new outline paragraph with `\autoref{chap:…}`. The chapters currently have no `\label`s. |
| S-1.2 | introduction.tex:55–66 | M | The Contributions section reads as final, but CLAUDE.md says the contributions are provisional. | Add a `\todo{provisional: finalise after results}` until the results analysis is done. |
| S-1.3 | introduction.tex:7–29 | S | Two background sections (1.1, 1.2: about 2.5 pp.) come before a short Problem Statement and Motivation (1.3: two paragraphs). The motivation is spread across 1.1–1.2, and 1.3 says little that is new. The chair asks for motivation and problem as the core of the introduction. | Consider merging 1.1–1.2 into one shorter background section and expanding 1.3 with the concrete problem: a pretrained model that is poor on new structures, few labels, and the need to keep both earlier tasks and pretrained ability. |
| S-1.4 | introduction.tex:3–5 | S | The connection to prior work is thin. L29 cites three works as "recent studies" without saying what they did or why they are not enough. | Say in one sentence each what the closest works do and do not cover, and point to `\autoref{sec:sota-summary}`. |
| S-1.5 | introduction.tex:41–52, 55–66 | S | Objectives and contributions don't map onto each other. Objective 1 (protocol) has no matching contribution. Contributions 2–3 bring in terms (transfer, retention, task ordering) that the objectives don't use. | Decide on the mapping later, together with the final contributions. A two-column mapping in your notes would help. |
| S-1.6 | introduction.tex:68–77 | m | Scope and Delimitations partly repeats itself: L71, L73 and L77 all say "limited to the model, datasets, task sequences…". | Merge L71 and L77. |
| S-1.7 | introduction.tex:36, 41–64 | m | Heavy bold in the research question, objectives and contributions. CLAUDE.md asks for no excessive bold. | Keep bold for the research question at most. |
| S-2.1 | related_work.tex (whole) | S | Page budget: chapter 2 runs from p. 7 to about p. 22 (`thesis_main.toc`), about 15 pages, i.e. 25–30 % of a 50–60-page main text. | Shorten the descriptions of works far from the setting (e.g. 2.1.1 Language as Auxiliary Supervision, multimodal replay) and keep the detail for the closest works. |
| S-2.2 | related_work.tex:15 | S | Few-shot is named as a constraint of the setting, but no section reviews few-shot adaptation of segmentation models. This includes in-context few-shot models such as UniverSeg (`universeg` is in the bib but not cited) and the review `theekshana26fewshot`, which is cited only in chapter 1. | Add a short subsection or paragraph on few-shot adaptation of segmentation foundation models. It should also make clear that "few-shot" in this thesis means fine-tuning on k labelled volumes. |
| S-2.3 | related_work.tex (whole) | S | Objective 1 is an evaluation protocol, but the chapter reviews no existing CL evaluation protocols or metrics: Chaudhry et al. forgetting/intransigence, ZSCL's Transfer/Last, SPU's control set (`Zhang_2024_CVPR`, in the bib, uncited), and task-order sensitivity. The metric decisions in `thesis_notes.md` §1 depend on these. | Add a short section (or a paragraph in 2.2) on how CL for pretrained models is evaluated. Alternatively, move this to Background and say so. |
| S-2.4 | related_work.tex:94, 122–128 | S | Design decisions sit inside the State of the Art: why TIL-LoRA is evaluated with task identity, which strategies are chosen, and how ZSCL is adapted. They belong in Method; the State of the Art should only end with the gap. | Keep one sentence each and move the justification to Method with a forward `\autoref`. |
| S-2.5 | related_work.tex:5–11, 100–106, 118–127, 242–245 | m | Working comments (TODOs, "SUMMARY TABLE" blocks) are fine for now, but list them so they are cleared before submission. | — |
| S-2.6 | related_work.tex:110 | m | `\newcolumntype` is defined inside the chapter. | Move it to the preamble (the comment already suggests this). |
| S-2.7 | related_work.tex:60, 62, 64 | m | `\paragraph{…:}` headings end in a colon and show up in the ToC (`thesis_main.toc` l.17–19). The chair asks for ToC depth 3. | Drop the colons. Check `tocdepth` (out of scope here; flag only). |
| S-2.8 | related_work.tex:217 | M | The build log shows "ignored error: Infinite glue shrinkage found in box" three times at the longtable (`thesis_main.log` l.1904–1908). The lab requires a clean compile. | Probably caused by `\newline` in `p{}` cells inside longtable. Fix when the table is revised. |

### 1.2 Content and argument

**Chapter 1**

| ID | File:line | Sev. | Issue | Suggestion / question for you |
|---|---|---|---|---|
| C-1.1 | introduction.tex:5, 24, 36; related_work.tex:40, 122, 238 | M | **Few-shot framing vs. the experiments.** The main comparison of all five strategies uses the full training split (108 volumes). Few-shot runs (5/10/20 volumes) exist only for fine-tuning, TIL-LoRA r = 4 and CIL-LoRA r = 1024 (`experiment_index.csv`, role `Main` / `Few-shot`). The research question says "under few-shot conditions". 20 volumes is also a lot to call few-shot for 3D segmentation, and that needs a justification. | `\todo{defense}`. Options for you to choose from: (a) reframe the research question as "across amounts of labelled data, down to few-shot"; (b) add few-shot runs for ZSCL and CPE-CLIP; (c) keep the wording and justify it explicitly. Define "shot" = one labelled volume. |
| C-1.2 | introduction.tex:3, 15 | M | **The motivation doesn't match the tasks.** The text motivates new imaging conditions, modalities, pathologies and acquisition settings. The experiments add six new anatomical structures in one MRI dataset. All tasks share the same scans and split (`thesis_notes.md` §2: one seeded split for SKM-TEA; please confirm). | Motivate with new target structures in a domain the model handles poorly. Your own result supports this: pretrained mean Dice 0.114 over the six tasks (`thesis/tables/cl_metrics.csv`, "Pretrained model" rows, column `adaptation`). Is SKM-TEA in VoxTell's training data? Ask/verify and state it. |
| C-1.3 | introduction.tex:5, 36, 75 | M | **The pretrained model's abilities are missing from the problem statement.** L5 says "preserving its performance on previously learned tasks". The control-task drop (AeroPath, prompt "lung") measures something different, the loss of pretrained ability. It is one of the six metrics but is not motivated anywhere in chapter 1. | Question for you: should the research question or objectives name this explicitly? Chapter 2 L46 already gives the argument (ZSCL). |
| C-1.4 | introduction.tex:22 | S | TIL/CIL/DIL are named but not defined, and the text doesn't say which setting(s) this thesis uses or why. The thesis uses both: TIL for task-specific LoRA, CIL for the others. | One sentence: which setting applies and what "task identity at inference" means for a free-text promptable model. See also C-2.8. |
| C-1.5 | introduction.tex:13 | S | "Text-promptable segmentation \cite{carion2026sam3…} offers clinicians a more intuitive alternative." SAM 3 is a natural-image concept-segmentation model, so it is a weak source for medical text prompting. The claim about clinicians has no source. | Cite medical text-promptable works (SAT, VoxTell, BiomedParse) for the concept. Remove the clinician claim or add `\todo{cite: user study / clinical usability of text prompts}`. |
| C-1.6 | introduction.tex:3, 5, 13 | S | "Text-promptable" (L3, L13) and "free-text promptable" (L5) are both used, and the difference is never explained. Chapter 2 L38 explains it (fixed vocabulary vs. free-form). The title depends on this distinction. | Define "free-text promptable" in chapter 1 in one sentence. |
| C-1.7 | introduction.tex:13 | S | "Early approaches… relied primarily on visual interaction mechanisms" is a doubtful chronology. The text-conditioned CLIP-Driven Universal Model (ICCV 2023) appeared at about the same time as MedSAM/SAM-Med2D. | Present visual and text prompting as two lines of work, not as a sequence. |
| C-1.8 | introduction.tex:20 | S | "Different modalities exhibiting different rates of forgetting" uses "modality" for image vs. text. L9 uses it for CT/MRI/PET. Is the claim relevant to VoxTell at all? Its text encoder (Qwen3-Embedding-4B) is frozen. Please confirm which parts each strategy updates. | Either explain how this applies to VoxTell or drop it. Fix the term (see §2). |
| C-1.9 | introduction.tex:22 | S | The method families listed (regularisation, rehearsal, dynamic architecture) don't match chapter 2's taxonomy (replay, regularisation, parameter-efficient) or the scope at L73 (parameter-efficient, prompt-based, regularisation, + replay). | Use one taxonomy across chapters 1, 2 and Method. |
| C-1.10 | introduction.tex:22, 27 | S | "Additional challenges due to their large scale and architectural complexity" (L22) and "introduce additional considerations" (L27) are vague. An examiner will ask "which?". | Name the concrete differences: frozen text encoder, cross-modal fusion, shared parameters for all prompts, no closed output head (chapter 2 L94 already argues the last one). |
| C-1.11 | introduction.tex:24 | S | "Few-shot learning refers to the adaptation of a model using only a small number of labelled examples" is ambiguous. In the segmentation literature, few-shot often means in-context support sets at inference without training. | Define the few-shot setting used here: fine-tuning on the first k volumes of a seeded split, one sample per k, nested sets (`thesis_notes.md` §2). Say which other meaning you are not using. |
| C-1.12 | introduction.tex:29; related_work.tex:117 | M | The gap is stated with different strength: chapter 1 says it "remains limited", chapter 2 says "no prior work". Chapter 1 also cites `Zhang_2025` (contrastive regularisation over LoRA for multimodal biomedical incremental learning) and `chen2025forgingdynamicmemoryretrievalguided` (CL for generalist medical foundation models) as related, but chapter 2 never reviews them. They may weaken the "no prior work" claim. | Review both in chapter 2 and then decide on one version of the gap claim. The author TODO at L118 (search method) is still open. |
| C-1.13 | introduction.tex:29 | S | "This question is especially relevant under few-shot conditions": the text names no question and gives no reason. | State why few-shot makes the trade-off harder or different (overfitting, fewer gradient steps, a support set that is too small to replay). |
| C-1.14 | introduction.tex:52 | S | Objective 4 ("experimental factors… ablation studies") is unspecific. | Name the factors once the experiments are fixed: LoRA rank, replay, task order, amount of data(?). |
| C-1.15 | introduction.tex:71, 73 | S | Scope: datasets are cited but not named. AeroPath's role (control task only, never trained, except in replay runs) is not stated. The strategy list leaves out the sequential fine-tuning baseline and the TIL/CIL split. "Prompt-based" is also parameter-efficient (chapter 2 L62). | Name SKM-TEA (six tasks) and AeroPath (control task). List the strategies with their settings. |
| C-1.16 | introduction.tex:75 | m | "Computational cost… outside the scope", but the chair requires runtime and memory for each algorithm, and `thesis/tables/compute.csv` exists. | Rephrase as "cost in clinical deployment is out of scope; training cost is reported in \autoref{…}". |
| C-1.17 | introduction.tex:73 | m | "Does not aim to develop a new continual-learning algorithm" is fine. Note that the ZSCL- and CPE-CLIP-based strategies are your adaptations (C-2.5, C-2.6). That needs to be stated as your contribution, not as prior work. | — |

**Chapter 2**

| ID | File:line | Sev. | Issue | Suggestion / question for you |
|---|---|---|---|---|
| C-2.1 | related_work.tex (all reviewed works) | M | **Supervisor requirement: main findings, dataset (n samples, groups/labels), methods, best results for each paper.** Coverage is incomplete; see the table below. | Fill the missing fields from the PDFs. Put numbers in the prose for the closest works and in the table for all of them. |
| C-2.2 | related_work.tex:134–217 | M | The summary table's "Reported result" column mixes metrics without naming them (accuracy, DSC, Transfer, "last", "Final", AP, F1, forgetting, IoU). Several cells are not results at all: "Gains over baselines", "Better than regularisation", "Ranking depends on setting", "ViT retains more", "$<0.3\,\%$ of parameters trained", "--". The "Data" column has no sample counts for most rows. AP, LLM, VAE and "last" are not defined in the caption. | Add a "Metric" column (or a metric name in every cell), n samples / labels in "Data", and possibly columns for modality/dimension, CL setting, text conditioning and few-shot. The positioning table partly does this. The author TODO L244 says to verify every value against the PDFs; CoLeCLIP's metric label is still uncertain. |
| C-2.3 | related_work.tex:242 | S | Works cited for a mechanism only are left out of the table: Ozdemir, ILT, MiB, Liu 2022/2023, O-LoRA. The supervisor asks for "a table to summarize the works reviewed". | Fine if the caption states the inclusion rule. Otherwise add them. |
| C-2.4 | related_work.tex:34 | S | "Its slice-wise formulation… limiting its performance on complete volumetric scans" is a claim with no source. | Cite the comparison that shows this (e.g. in the SAT or VoxTell paper, if they report it) or soften it. |
| C-2.5 | related_work.tex:54, 125 | M | "A regularisation strategy derived from ZSCL". The implementation drops the reference dataset (`thesis_notes.md` §2; `code/src/continual/strategies/zscl/strategy.py`), and L54 itself calls the reference set ZSCL's key element ("principal stated limitation"). An examiner will ask whether the variant still protects zero-shot ability. | `\todo{defense}`: state the deviation and its reason in Method, and name it here in one clause. |
| C-2.6 | related_work.tex:62, 125 | M | **The CPE-CLIP description vs. the code, and a claim that is not quite correct.** L62 describes CPE-CLIP as prompts in both the language and vision branches. The implementation adds learned prompt tokens only to VoxTell's transformer decoder, freezes the rest, and scales gradients per task (α = α_base/(t+1), floor 0.25; `code/src/continual/strategies/cpe_clip/model.py:46-100`, `strategy.py:33-55`). L62 also says "degradation of the original representation is excluded by construction". The weights stay fixed, but the learned prompts change the function for every input, including the control task. | Change it to "pretrained weights are unchanged", not "degradation excluded". Name the deviations in Method. Please check whether the CPE-CLIP prompts are active when the control task is evaluated. |
| C-2.7 | related_work.tex:60 | M | LoRA is introduced without a citation to Hu et al. The key `hu2022lora` is used elsewhere in the thesis, but biblatex reports it missing from `literature.bib` (`thesis_main.log`). | Add LoRA to Zotero, then cite it here. |
| C-2.8 | related_work.tex:94, 125, 238 | S | **The TIL/CIL distinction needs a precise definition for a promptable model.** In "CIL" the free-text prompt still names the target structure, so the model gets a form of task information there too. The distinction in this thesis is really "the adapter is selected by task ID" vs. "one set of parameters for all tasks". | `\todo{defense}`: define both settings precisely (in Background or Method) and use that definition here. |
| C-2.9 | related_work.tex:72 | S | The partial-annotation / background-conflict problem is described generally. It applies directly to your setup: six structures in the same knee scans, each task labelling only one. VoxTell predicts one binary mask per prompt, which may avoid the conflict. | Question for you: how are the other structures handled in each task's training masks? Connect this to the setup in one sentence. |
| C-2.10 | related_work.tex:46 | S | "The sequential adaptation of VoxTell is a problem of continual learning for vision–language models" is an analogy that needs a reason. The VLM-CL methods reviewed target contrastive CLIP classifiers. VoxTell is a segmentation model with a frozen text encoder and fusion in the decoder. | Say what transfers (protecting a shared cross-modal representation) and what doesn't (no similarity-based classifier). L125 already partly does this. |
| C-2.11 | related_work.tex:66 | S | The capacity argument ("too small to accommodate a task that differs substantially… limit tightens as tasks accumulate") has no citation. It is a hypothesis that your rank ablation tests (see §3). | Mark it as an expectation, or cite a source. |
| C-2.12 | related_work.tex:115 | m | The summary says VLM-CL methods were "developed almost exclusively for two-dimensional classification", but LiLoRA (reviewed at L60) is instruction tuning. | "mostly for image classification". |
| C-2.13 | related_work.tex:115–128, 238 | S | The summary and the positioning table leave out the replay ablation, the LoRA rank ablation, the control task, and the missing joint-training upper bound (a limitation, `thesis_notes.md` §3). The table also claims "Few-shot: yes" for all strategies (C-1.1). | Revise after the results are fixed (see §3). |
| C-2.14 | related_work.tex:98 | m | Chen et al.: "the closest of the reviewed works to the task-incremental configuration" is fine. Make sure the 32-shot setting is compared to your shot counts (5/10/20 volumes) in one sentence, since it is the only other few-shot 3D CL work. | — |

*Coverage of the supervisor's per-paper requirement (prose + table), checked against the text only, not the PDFs:*

| Work (line) | Dataset & n | Labels/groups | Method | Best result (number) |
|---|---|---|---|---|
| LViT (25) | no ("X-ray and CT") | no | yes | no |
| TextMatch (25) | QaTa-COV19, n missing | no | yes | yes |
| R-Super (25) | 6,718 pairs | tumour types missing | yes | partly ("F1 up to +16.0 %": relative or pp.? which task?) |
| CLIP-Driven Universal (32) | yes | yes | yes | no (qualitative) |
| BiomedParse (34) | modalities only | no | yes | no in prose; table "Above MedSAM" not in prose |
| MedSAM-3 (34) | no in prose | no | yes | table only |
| SAT (34) | yes | yes | yes | qualitative ("matched") |
| VoxTell (38) | yes | yes | yes | yes |
| CGIL, GIFT, RAPF (50, 54) | no in prose | no | yes | table only (GIFT key missing) |
| ZSCL (54) | MTIL | — | yes | yes |
| CLIP-LoRA, LiLoRA (60) | partly | no | yes | table only |
| S-Prompts, CoLeCLIP (62) | no in prose | no | yes | table only (CoLeCLIP label unverified) |
| CPE-CLIP (62) | table only | no | yes | **no performance result** |
| MoE-Adapters (64) | no in prose | no | yes | table only (two keys) |
| Baweja (77) | UK Biobank, n missing | structures missing | yes | qualitative |
| Bera (79) | benchmark not named | no | yes | yes |
| SegGAN (79) | BTCV, n missing | no | yes | qualitative |
| Lifelong nnU-Net (81) | yes, n missing | yes | yes | qualitative |
| Ranem (81) | hippocampus, n missing | — | yes | qualitative |
| González 2023 (83) | yes, n missing | yes | yes | **none** ("--") |
| Continual Segment (83) | yes | yes | yes | yes |
| CL-Net (83) | yes | yes | yes | table only, no comparison |
| Zhang et al. (85) | table only | no | yes | table only |
| SAM-Med3D-MoE (92) | **none** | **none** | yes | **none** |
| CA-SAM (92) | nine datasets, n missing | no | yes | yes |
| MedSeqFT (96) | five CT tasks | yes (comment block) | yes | yes |
| Chen et al. (98) | yes | yes | yes | yes |

### 1.3 Citations

| ID | File:line | Sev. | Issue |
|---|---|---|---|
| Ci-1 | related_work.tex:92, 210 (`[Wan+24]`), 92, 212 (`[Wan+26]`), 96, 115, 214, 234 (`[MedSeqFT]`), 98, 115, 125, 216, 236 (`[Che+26]`), 125 (`[DAl+23]`) | M | Literal placeholder labels instead of `\cite`. `[Che+26]` probably = `chen2026fewshotcontinuallearning3d` (cited in chapter 1; title "Few-Shot Continual Learning for 3D Brain MRI with Frozen Foundation Models"; please confirm). `[DAl+23]` = `D_Alessandro_2023`, which already exists and is cited at L62. SAM-Med3D-MoE, CA-SAM and MedSeqFT have **no bib entry**; add them to Zotero. |
| Ci-2 | related_work.tex:50, 172 | M | `wu2024gift` (GIFT) is not in `literature.bib` (undefined citation in the build log). |
| Ci-3 | related_work.tex:188 vs 64 | M | `moe4cl2024` is not in the bib. The same paper is cited as `yu2024boostingcontinuallearningvisionlanguage` in the prose. Use one key. |
| Ci-4 | introduction.tex:3 vs related_work.tex:34, 160 | S | BiomedParse appears twice in the bib: `Zhao_2024` (Nature Methods, 2024) and `zhao2025foundation-9de` (Nature Methods, 2025, pp. 166–176). Chapter 1 uses the first, chapter 2 the second. Remove the duplicate in Zotero. |
| Ci-5 | related_work.tex:54, 125 | M | `\ref{subsec:zscl}` is undefined (Method not written yet). Author TODO L126: no reference yet to the CPE-CLIP section. |
| Ci-6 | related_work.tex:118 | S | "To the best of our knowledge, no prior work…": the search method (databases, terms, date) is still missing (author TODO). |
| Ci-7 | related_work.tex:25–98, 152–216 | M | All numbers attributed to papers must be checked against the PDFs (author TODO L244). Under CLAUDE.md I cannot confirm any of them. Values that only appear in the table (GIFT, CGIL, RAPF, CLIP-LoRA, LiLoRA, S-Prompts, CoLeCLIP, MoE-Adapters, CL-Net, Zhang et al., CA-SAM IoU) need checking first. |
| Ci-8 | introduction.tex:13 | S | `carion2026sam3segmentconcepts` is a weak source for medical text prompting (C-1.5). The clinician-intuitiveness claim needs `\todo{cite: …}`. |
| Ci-9 | introduction.tex:29 | S | `Zhang_2025` and `chen2025forgingdynamicmemoryretrievalguided` are cited for "recent studies" but not reviewed in chapter 2 (C-1.12). |
| Ci-10 | related_work.tex (relevant bib entries not cited) | S | These are in the bib and relevant but uncited: `Zhang_2024_CVPR` (SPU, the source of your control-set design, `thesis_notes.md` §1), `universeg` (in-context few-shot segmentation), `ilharco2022patchingopenvocabularymodelsinterpolating` (weight interpolation, related to ZSCL's weight ensembling), the surveys `wang2024comprehensivesurveycontinuallearning`, `delange2022`, `PARISI201954`, and `luo2025empiricalstudycatastrophicforgetting`. These are suggestions; you decide. |
| Ci-11 | `literature.bib` | S | **Fields missing** (report for Zotero): `qazi2026clmedicalimaging` (no pages); `Ma_2024` (no pages/article number); proceedings without editor/location: `D_Alessandro_2023`, `Liu_2023`, `Zhang_2025`, `Degerli_2022`, `newgenerativereplayapproach`, `3d_unet`, `memory_replay_cropping`, `text3dsam`. |
| Ci-12 | `literature.bib` | S | **About 40 cited entries are `@misc`/arXiv.** Peer-reviewed versions I believe exist (please verify each in Zotero, I may be wrong on venues): `isensee2018nnunet…` (Nature Methods 2021), `kemker2017…` (AAAI 2018), `li2017learningforgetting` (TPAMI 2018 / ECCV 2016), `cermelli2020…` MiB (CVPR 2020), `douillard2021…` PLOP (CVPR 2021), `zheng2023…` ZSCL (ICCV 2023), `yu2024boosting…` MoE-Adapters (CVPR 2024), `wang2023sprompts…` (NeurIPS 2022), `zanella2024…` CLIP-LoRA (CVPR Workshops 2024), `huang2024…` RAPF (ECCV 2024), `li2023lvit…` (IEEE TMI), `wang2023orthogonal…` O-LoRA (Findings of EMNLP 2023), `zou2023segment` SEEM (NeurIPS 2023), `du2025segvol…` (NeurIPS 2024), `ji2023continualsegment…` (ICCV 2023), `zhang2023continuallearningabdominal…` (MICCAI 2023), `ranem2022…` (CVPR Workshops 2022), `karani2018…` (MICCAI 2018), `li2018hdenseunet…` (IEEE TMI 2018), `wang2020nonlocalunet…` (AAAI 2020), `støverud2023aeropath…` (PLOS ONE 2024), `liu2022learningincrementally…` (MICCAI 2022?). **Check** whether these have been published: `rokuss2025voxtell…`, `zhao2025sat`, `carion2026sam3…`, `frascaroli2024…`, `li2024coleclip…`, `guo2025…` CL-Net, `che2026lora…`, `liu2026medsam3…`, `chen2026fewshot…`, `memmel2021…`, `gonzalez2023wrong…`, `liu2023incremental…`, `bassi2025…`, `baharoon2025…`, `yu2026recentadvances…`. |
| Ci-13 | `literature.bib` | m | The key `støverud2023…` contains a non-ASCII character. It works with biber, but is fragile. Consider changing the citekey in Better BibTeX. |

### 1.4 Language

| ID | File:line | Sev. | Issue |
|---|---|---|---|
| L-1 | both files, all paragraphs | S | One paragraph per source line. CLAUDE.md requires one sentence per line. Fix when the text is revised. |
| L-2 | both files | S | Acronyms are written out by hand instead of with `\gls`: CT, MRI, PET, CNN, CL, DSC, LoRA, VAE, MoE, EWC, MiB, LwF, ILT, ViT, LLM, MLP, TIL/CIL/DIL, FFT, MTIL, HD95, IoU, AP. `abbreviations.tex` is empty (glossaries warning "No entries defined"). |
| L-3 | introduction.tex:5, 9, 24; related_work.tex:92 vs others | m | "three-dimensional (3D)" is defined at L5 and then written out again at L9 and L24. Chapter 2 mixes "two-dimensional" and "2D". Pick one form after first definition. |
| L-4 | introduction.tex:13 | m | `'segment the left ventricle'` uses straight quotes (should be ``` ``…'' ```) and needs a comma after it. |
| L-5 | introduction.tex:5 | m | "The following sections establish the background and problem formulation for this study" is empty signposting. |
| L-6 | introduction.tex:22 | S | One paragraph with four ideas (CL definition, stability–plasticity, method families, VLM challenges, CL settings). Split it. |
| L-7 | introduction.tex:24, 29 | S | Vague sentences: "Few-shot conditions are used to evaluate how…" (passive, no actor); "…remains limited. In particular, the behaviour… remains insufficiently understood. This question is especially relevant…" ("remains" twice, and "this question" refers to nothing). |
| L-8 | introduction.tex:11 | m | "Deep learning-based" → "Deep-learning-based". |
| L-9 | introduction.tex:71–73 | m | Forward references without `\autoref` ("specified in the experimental design", "the defined experimental protocol"). Non-parallel phrase: "for adaptation and mitigating catastrophic forgetting". |
| L-10 | related_work.tex:15, 34, 38, 54, 62, 94, 115 | S | Very long sentences (50+ words), dense with nominalisations. Example L15: "The first section describes the kind of model adapted in this thesis, the second the methods developed for continually adapting models of the same kind, and the third the methods developed for the same kind of prediction…". L46 "In the type of model it adapts" and L72 "those reviewed in this section produce the same kind of prediction" are hard to parse. |
| L-11 | related_work.tex:27, 50, 66, 79, 81, 83, 85 | S | Most paragraphs end with a summarising/moral sentence ("In both cases the burden moves from storage to modelling…", "Both variants substitute…"). CLAUDE.md lists this as a pattern to avoid. Keep only the ones that carry the argument towards the gap. |
| L-12 | related_work.tex:50, 54, 94 | m | Colon reveals ("…to modelling: what is preserved…", "…fixed label set: a preservation term…", "…for the present study: the capability…"). |
| L-13 | related_work.tex:64 | m | Missing full stop at the end of the paragraph ("…stored in the correct one"). |
| L-14 | related_work.tex (5×) vs (12×) | m | "the present study" and "this thesis" are used interchangeably. Pick one ("this thesis"). |
| L-15 | related_work.tex:38, 40 | m | "strong zero-shot performance", "robustness to linguistic variations", "promising direction": vague or on the banned list. The second "robustness" is used technically; keep it only if you specify what was measured. |
| L-16 | related_work.tex numbers | S | Number formats are inconsistent: DSC is given in % with 1, 2 or no decimals (62 %, 68.1 %, 83.56 %). Thousands use commas ("22,186") with no `siunitx`. Your own results are Dice in [0, 1] with three decimals (`thesis_notes.md`: 0.979). Decide on one scale for the whole thesis. |
| L-17 | related_work.tex:77 | — | "Modeling the Background" is the method's own name, so American spelling is correct there. No other American spellings found in either file. |

---

## 2. Terms and symbols

**Symbols:** neither chapter defines or uses any mathematical symbol; only numbers, `$\rightarrow$` and `%` appear. The first symbols will appear in Background/Method, e.g. the evaluation-matrix entry a_{i,j}, number of tasks, shot count k, LoRA rank r, CPE-CLIP α. No notation conflicts yet. Suggestion: reserve **k** for the number of labelled volumes (shots), **r** for the LoRA rank, **T** for the number of tasks, **a_{i,j}** for the evaluation matrix. Note that `thesis_notes.md` §1 already writes a_{i,i} and Chaudhry's a_{k,k}. If k = shots, Chaudhry's index must be renamed (e.g. a_{t,t}).

**Terms:** inventory with variants found and a proposed CLAUDE.md entry. "Keep" means it is already in CLAUDE.md and used consistently.

| Concept | Variants found (file:line) | Problem | Proposed CLAUDE.md entry |
|---|---|---|---|
| free-text promptable | "text-promptable" (intro 3×2, 13; ch2 heading L18, L21, L115), "free-text promptable" (intro 5, 27, 29; ch2 L94, L117), "language-guided" (ch2 L21), "text conditioning"/"concept-level text conditioning" (ch2 L29–34), "free-form descriptions" (ch2 L38), "natural language descriptions" (intro 13) | Chapter 1 uses "text-promptable" for the model of this thesis. | **free-text promptable**: accepts arbitrary free-form text (VoxTell). **text-promptable**: umbrella term for any text-conditioned model, including fixed-vocabulary ones (SAT, CLIP-Driven). Use "free-text promptable" whenever VoxTell or this thesis is meant. |
| universal segmentation model | "universal models", "text-promptable universal models", "promptable universal segmentation models" (intro 3, 13), "segmentation foundation model" (ch2 L87–90), "medical foundation models" (intro 29), "3D foundation model", "3D FM" (ch2 L98, L224), "multimodal foundation models" (intro 22) | Universal vs. foundation model are mixed. CLAUDE.md marks this [CONFIRM DEFINITION]. | **universal segmentation model**: one model that segments many structures across imaging modalities, with the target chosen by a prompt. **foundation model**: a model pretrained on large, diverse data and then adapted. VoxTell is both. Use "universal" when the prompt-selected target matters, "pretrained model" when the pretrained state matters. |
| 3D | "3D", "three-dimensional", "volumetric" | Variants mixed (L-3). | **3D**: defined once in chapter 1, then "3D" only; "volumetric" allowed as an adjective for data. |
| task | "newly introduced task", "target task", "previously unseen tasks" (intro), "step"/"learning steps" (intro 22), "domain" (ch2 L62), "session" (code) | The CLAUDE.md definition ("one training stage on **one dataset**") is **wrong for this thesis**: the six tasks are six structures of one dataset (SKM-TEA). | **task**: one training stage on one target structure (one text prompt) of SKM-TEA. The model is trained on task 1, then task 2, and so on. In this thesis a task ≠ a dataset. |
| task order / task sequence | "task sequences" (intro 73, 77; ch2 L81), "task ordering" (intro 64) | "ordering" breaks the CLAUDE.md rule. | Keep the CLAUDE.md entry. Add the two orders used: **original** and **reverse** (from `experiment_index.csv`). The `custom` order runs are single-task; drop them or name them. |
| continual learning | "continual learning (CL)", "continual adaptation", "sequential adaptation", "continual-learning perspective" | Fine. "continual adaptation" and "sequential adaptation" mean the same thing. | Keep. Allow **continual adaptation** for the process applied to a pretrained model; drop "sequential adaptation". |
| catastrophic forgetting | "forgetting", "backward degradation" (ch2 L98), "degradation" (ch2 L62), "interference" (ch2 L58–62), "overwrite" (ch2 L60) | "interference" is the mechanism, "forgetting" the effect; "backward degradation" is a third term. | Keep. Add: **interference** = the mechanism (updates for one task changing performance on another); not a synonym for forgetting. Drop "backward degradation". |
| stability / plasticity | intro 22 | Defined. Fine. | **stability / plasticity**: properties, never metric names (consistent with the "adaptation" entry). |
| CL scenarios | "task-incremental, class-incremental, domain-incremental learning" (intro 22), TIL/CIL/DIL (ch2 tables), "task-incremental setting"/"class-incremental setting" (ch2 L94, L125) | Not defined for a promptable model (C-2.8). | **TIL (task-incremental)**: the task identity selects task-specific parameters at inference. **CIL (class-incremental)**: one parameter set for all tasks; only the text prompt names the structure. **DIL**: only in related work. |
| strategy names | "task-specific LoRA adapters", "a separate low-rank adapter for each task" (ch2 L60, L125, L238); "a single LoRA adapter shared across tasks", "shared LoRA" (ch2 L60, L125, L238); code `lora` / `shared_lora`; notes "TIL-LoRA" / "CIL-LoRA" | Three naming schemes. | **TIL-LoRA** (one LoRA adapter per task, chosen by task identity) and **CIL-LoRA** (one LoRA adapter shared across tasks). Always give the rank r. |
| fine-tuning baseline | "sequential fine-tuning" (intro 20; ch2 L46, L98, L125), "sequential full fine-tuning" (ch2 L98), "full fine-tuning", "FFT" (ch2 L96, L214, L234, L238), "unconstrained fine-tuning" (ch2 L77); code `naive_sequential_finetuning` | Four variants. "Full fine-tuning" in the positioning table could mean non-sequential. | **sequential fine-tuning**: all parameters trained on each task in turn, with no CL mechanism; the lower reference. In a related work, use that paper's own term (e.g. FFT) only inside its description. |
| ZSCL-based / CPE-CLIP-based | "derived from ZSCL", "ZSCL-based" (ch2 L54, L125, L238), "ZSCL-style" (notes); "derived from CPE-CLIP", "CPE-CLIP-based" | The implementations differ from the originals (C-2.5, C-2.6). | **ZSCL-based** and **CPE-CLIP-based**: always with "-based" for the thesis's variants. Plain "ZSCL"/"CPE-CLIP" only for the original papers. |
| replay | "replay", "rehearsal" (intro 22; ch2 L81, L230), "memory replay", "generative replay" | Two terms for one family. | **replay**: storing earlier training samples and mixing them into later tasks. "rehearsal" only when quoting a paper's own term. |
| method families | intro 22: regularisation / rehearsal / dynamic architecture; ch2: replay / regularisation / parameter-efficient (+ prompt, LoRA, MoE); scope: parameter-efficient / prompt-based / regularisation / replay | No common taxonomy (C-1.9). | One taxonomy, e.g. **replay**, **regularisation**, **parameter-efficient adaptation** (sub-types: LoRA, learned prompt tokens, mixture of experts), **architectural isolation**. Your choice. |
| prompt (overloaded) | the text prompt of VoxTell; "prompts" as learned vectors in S-Prompts, CoLeCLIP, CPE-CLIP (ch2 L62); "prompt learning", "prompt tuning"; "concept prompts", "spatial prompts" (intro 13) | **Ambiguous in a thesis about prompting.** | **text prompt**: the free-text input naming the target structure (e.g. "femoral cartilage"). **learned prompt tokens**: the trainable vectors of CPE-CLIP-based strategies. Never write a bare "prompt" where both meanings are possible. |
| modality | imaging modality (intro 9; ch2 L34, L38); image vs. text (intro 20 "different modalities", "multimodal"; ch2 "cross-modal", "multimodal replay") | Two meanings (C-1.8). | **imaging modality**: CT, MRI, PET. **input modality**: image or text. "Multimodal" only for image + text. |
| zero-shot | "zero-shot performance/generalisation" (ch2 L34, L38, L40), "zero-shot transfer" (ch2 L46), "zero-shot model" (ch2 L54), "zero-shot inference" (ch2 L64) | Fine for related work. The control task is not zero-shot (CLAUDE.md). | Keep the CLAUDE.md rule. Add: **pretrained model** (not "zero-shot model" or "original model") for the never-updated VoxTell checkpoint. |
| transfer | "zero-shot transfer", "Transfer 68.1 %" (ZSCL metric), "cross-modality transfer", "downstream transferability", "transferred better to unseen tasks" (ch2 L32–96); intro contribution 2 | CLAUDE.md [CONFIRM]. `thesis_notes.md` says Transfer is as in ZSCL. | **Transfer** (metric): as in ZSCL. Give the exact formula in Method once you confirm it: forward transfer to tasks not yet trained? In prose use "transfer" only in this sense. |
| retention | intro 62 (contribution); ch2 L83, L96, L122 | CLAUDE.md [CONFIRM METRIC]. There is **no retention metric** in the decided metric set (`thesis_notes.md` §1). | Either (a) "retention" = the property, measured by Final Forgetting and control-task drop, with no separate metric; or (b) drop the word from contribution 2. Your choice. |
| adaptation | "adaptation performance" (RQ), "adaptation strategy", "continual adaptation", "adaptation configuration" (intro 64), "adaptation methods" (intro 77) | The process and the metric are mixed. | Keep the CLAUDE.md metric entry. Add: capitalised **Adaptation** = the metric; lowercase "adaptation" = the process; "adaptation configuration" → name the factor (e.g. LoRA rank). |
| few-shot / shot | "few-shot conditions", "few-shot settings" (title), "limited supervision", "small number of labelled volumes/examples", "32-shot" | "Shot" is never defined; the main runs are not few-shot (C-1.1). | **shot**: one labelled training volume of a task. **k-shot**: training on the first k volumes of the seeded split (k ∈ {5, 10, 20}); "full data" = all 108 volumes. Always state k. |
| data unit | "volumes", "scans", "images", "examples", "samples", code "cases" | Mixed. | **volume** for this thesis's data. "scan" only when quoting related work. |
| Dice | "Dice similarity coefficient (DSC)" (ch2 L25), "DSC" (ch2), "Dice" (notes, results) | Abbreviation and scale (% vs. [0, 1]) not fixed (L-16). | **Dice** (Dice similarity coefficient, DSC via `\gls`), reported in [0, 1] with three decimals. Convert related-work values or mark them as %. |
| task identity | "task identity" (ch2 L60, L94, L98, L115, L125), "task identification" (ch2 L98), "domain identification" (ch2 L62), "routing decision" | Fine. | **task identity**: the index of the task a test input belongs to, given to the model at inference (TIL only). |
| control task | not used in chapters 1–2 (C-1.3); ch2 L123 TODO "zero-shot performance on concepts outside the sequence" | Missing. | Keep the CLAUDE.md entry. Use it in chapter 1 and the chapter 2 summary. |
| gap wording | "this thesis" / "the present study" (L-14) | Both used. | **this thesis** for the work; **we** for actions (CLAUDE.md). |

---

## 3. Statements that depend on results or on contributions that aren't final

Revisit each one after the results analysis.

| File:line | Statement | Depends on |
|---|---|---|
| introduction.tex:36 | Research question "…under few-shot conditions" | Which strategies have few-shot runs (only 3 of 5 now; C-1.1). |
| introduction.tex:41–43 | Objective 1: "Develop a few-shot CL evaluation protocol" | The final protocol and whether it is claimed as a contribution (it is not in the contributions list). |
| introduction.tex:48–50 | Objective 3: amount of labelled data for "the evaluated strategies" | Few-shot runs exist for 3 strategies only. |
| introduction.tex:52 | Objective 4: "experimental factors… ablation studies" | Which ablations are reported: rank (CIL-LoRA 4–2048; TIL-LoRA only r = 4/8, see `thesis_notes.md` §3), replay, task order, convergence diagnosis. |
| introduction.tex:55–66 | All three contributions (as final) | Provisional under CLAUDE.md. Contribution 1: "systematic" (one seed, one support set per k). Contribution 2: "transfer and retention" (retention metric undecided). Contribution 3: "task ordering" (reverse order only for FT, TIL-LoRA r = 4, CIL-LoRA r = 256/1024), "adaptation configuration". |
| introduction.tex:73 | Strategies "including parameter-efficient adaptation, prompt-based adaptation, and regularisation… in addition… with replay" | Final strategy list. There are two replay runs marked in_progress/excluded in `experiment_index.csv`. |
| introduction.tex:75 | "measures that quantify adaptation… and forgetting of existing capabilities" | Final metric set (control task included?). |
| introduction.tex:3 | VoxTell "can still exhibit reduced performance on previously unseen tasks" | Can be backed by your own result (pretrained mean diagonal Dice 0.114 in `cl_metrics.csv`). Decide whether to cite it here. |
| introduction.tex:29; related_work.tex:117 | Gap: "remains limited" / "no prior work" | The literature search (TODO L118) and the review of `Zhang_2025`, `chen2025forging…`. |
| related_work.tex:40 | "This motivates the present study… under few-shot conditions" | C-1.1. |
| related_work.tex:46 | Continual adaptation "has to preserve more than the performance on previous tasks" | Whether the control task stays a headline metric. |
| related_work.tex:54, 125 | "A regularisation strategy derived from ZSCL is evaluated… specified in Section subsec:zscl" | The Method chapter, and stating that the reference set is dropped. |
| related_work.tex:60 | "The configurations compared in this thesis lie at the two ends of this range" | The final strategy list. |
| related_work.tex:62 | "Prompt tuning is among the class-incremental strategies compared" | Whether CPE-CLIP-based results are reported (main order only, no few-shot). |
| related_work.tex:66 | Capacity argument (small adapters may be too small; limit tightens as tasks accumulate) | Reads as a finding before results exist. The rank ablation will support or contradict it. Mark it as an expectation or move it to Discussion. |
| related_work.tex:94 | "This thesis accordingly evaluates task-specific adapters only with task identity supplied… restricts the class-incremental comparison to…" | A design decision; belongs in Method. |
| related_work.tex:96, 98 | MedSeqFT / Chen et al. are "the closest" to your CIL/TIL configurations | The final configuration descriptions. |
| related_work.tex:122–125 | "examines how they trade off adaptation… against retention… under few-shot supervision"; strategy list without replay; "sequential fine-tuning… serves as the baseline" | Final experiments, the retention term, the control task (TODO L123), and the missing upper bound (no joint training; `thesis_notes.md` §3). |
| related_work.tex:238 | Positioning row "This thesis": Few-shot "yes"; strategies list | C-1.1; leaves out replay and the rank ablation. |

---

## 4. Side findings (not part of chapters 1–2)

- CLAUDE.md names `guidelines/Thesis_Outline.pdf` and `guidelines/drichtl_en.pdf`, but `guidelines/` contains `supervisor_guidelines.md` and `chair_guidelines.md`. CLAUDE.md also says `references.bib` in two places; the file is `thesis/literature.bib`.
- The CLAUDE.md terminology entry for **task** ("one dataset") contradicts the experiments (see §2).
- The build log also reports missing bib keys used in other chapters (e.g. `hu2022lora`, `chaudhry2018riemannian`, `dalessandro_multimodal_2023`, `desai_skm-tea_2022`, `isensee_nnu-net_2018`). Some of these look like alternative keys for entries that already exist (`D_Alessandro_2023`, `desai2021skmtea`, `Chaudhry_2018`).
- Chair guideline 1.7 spells "shoudl"; irrelevant, just don't copy from it.
