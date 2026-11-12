# Pass 3 — Citations, restricted scope (2026-11-12)

Report-only subagent pass (fresh agent, restarted in a new session). No files edited by the agent. Saved by the main session.

**Scope.** Ch. 1–7 and the appendix (`thesis/*.tex`), plus `tables/ch2_sota.tex` and `tables/ch2_positioning.tex`. Individual citations were not re-checked against the papers (done in the per-chapter citation reports); bibliography fields not checked (B4).

## 1. Every \cite key exists in literature.bib
- **No missing keys.** 79 distinct keys in the chapter files (incl. the multi-citation at `experiment_results.tex:630`); the 25 keys in the generated tables resolve. No `\nocite{*}`.
- **Unused bib entries (minor, information only).** About 50 entries never cited (e.g. `Litjens_2017`, `french1999catastrophic`, `icarl2017`, `kemker2017measuringcatastrophicforgettingneural`, `yushkevich2006itksnap`, `milletari2016vnet`). Harmless; check whether any should be cited, e.g. `french1999catastrophic` for the definition of catastrophic forgetting.
- **Dead file.** `thesis/fig1.tex` is not included anywhere.

## 2. Non-obvious claims without a citation

| # | Location | Claim | Source needed | Severity |
|---|---|---|---|---|
| 2.1 | `method.tex:204` | "VoxTell was pretrained with batches of 128 patches" | VoxTell paper, Sec. 5 p. 5 / Suppl. A.1 (`paper_notes/voxtell.md` l. 63). No citation in the sentence. | must fix |
| 2.2 | `method.tex:122` | "version 1.1 of the released VoxTell checkpoint~\cite{rokuss2025…}" | The paper describes v1.0 only (`voxtell.md` l. 13). v1.1 needs `rokuss2026voxtellmodelcard` (in the bib, used at Ch. 6 l. 630), possibly with `rokuss2026voxtellissue15`. | should fix |
| 2.3 | `background.tex:290` | "four metrics from the literature and the control task with a fifth" | Adaptation is not from the literature as a metric (l. 300–301: only the a_{i,i} term of Chaudhry's intransigence). Reword, e.g. three from the literature, one derived from Chaudhry's intransigence, a fifth for the control task. | should fix |
| 2.4 | `related_work.tex:266` | "…show that **their** zero-shot generalisation does not extend to the knee structures" | Only VoxTell's SKM-TEA result is cited (l. 47); nothing shows SAT on knee MRI. Narrow to VoxTell or cite a SAT result. | should fix |
| 2.5 | `method.tex:141`, `146` | Released implementation takes keys/values from stage 4; self-attention never executed | Claim about third-party code; source is code inspection (comment l. 150), reader gets no reference. Footnote with VoxTell repository/commit, as for ZSCL at l. 391. | should fix |
| 2.6 | `introduction.tex:53` | Retraining from scratch "would be expected to preserve most of what it could segment before" | `delange2022` Sec. 6.2.1 (soft upper bound, used at `background.tex:333`) would support it. | minor |
| 2.7 | `introduction.tex:20` | Manual outlining is laborious because every slice has to be outlined | Common knowledge; `desai2021skmtea` Sec. 1 available. | minor |
| 2.8 | `related_work.tex:158` | "the image encoder of VoxTell is convolutional" | Ch. 2 precedes Ch. 3 where it is cited; add `\cite[Sec.~3]{rokuss2025…}`. | minor |
| 2.9 | `background.tex:47` | Whole volumes don't fit in GPU memory, so training on patches | Standard knowledge, or cite nnU-Net (next paragraph). | minor |
| 2.10 | `background.tex:262` | DSC not inflated by background voxels | Follows from the equation; optional citation. | minor |
| 2.11 | `data_description.tex:137` (footnote) | Contents of `plans.json` in the Hugging Face repository | No bib reference; `rokuss2026voxtellmodelcard` points to the same repository. | minor |
| 2.12 | `method.tex:257` | Kaiming-uniform "instead of the Gaussian of the original LoRA" | Add Hu et al. Sec. 4.1 locator. Check: loralib (from which CLIP-LoRA's layers derive, l. 265) itself initialises A with Kaiming-uniform; if so, it is inherited, not our deviation (see 5.4). | minor (check) |

**Missing locators on cited claims (minor):**
- `introduction.tex:41`: VoxTell authors' attribution of the low knee value — p. 8 / Sec. 6; citation only in the next sentence.
- `introduction.tex:54`: six days on 64 A100s — Sec. 5, p. 5.
- `experiment_results.tex:256`: Lifelong nnU-Net, "the replay method forgot the least".
- `related_work.tex:34`: quoted template — `Liu_2023` Sec. 3.2.

## 3. Close paraphrase and direct quotes
- **All four direct quotes correctly marked** (quotation marks + citation): `introduction.tex:73` (De Lange Sec. 1, matches `paper_notes/delange2022.md` l. 14); `experiment_results.tex:575` (Hu Sec. 4.1); `related_work.tex:34` (locator missing, above); `background.tex:229` ("a photo of a", short example, no locator; add `[Sec.~3]` if wanted).
- **No uncited close paraphrase** found (compared with `paper_notes/voxtell.md`, `zscl.md`, `spu.md`, `lora_hu.md`, `delange2022.md` and the cards for Beyond Forgetting, Liu_2023, SegVol, Silva-Rodríguez).
- **Close but cited, acceptable:** `introduction.tex:42` ("adapting the model with a few labelled examples" vs "few-shot adaptation with minimal labeled examples"); `background.tex:212` ("unlabelled public images and arbitrary texts").

## 4. Figures and tables not created by the author
- `background.tex:96` (`ch3_voxtell`) and `method.tex:130` (`ch5_voxtell_strategies`): "adapted from~\cite[Fig.~2]{rokuss2025…}". OK.
- Own figures: `ch1_setting`, `ch3_metrics`, `ch4_examples`, all `ch6_*`, `appA_shared_lora_loss`.
- `tab:ch4_datasets` credits the dataset papers and tutorial; `tables/ch2_sota.tex` and `ch2_positioning.tex` cite every row (caption: "as reported by the authors"). Nothing missing.

## 5. Own contribution vs prior work

| # | Location | Issue | Severity |
|---|---|---|---|
| 5.1 | `introduction.tex:193–194`, `summary.tex:28` | "Our work consists of … the evaluation protocol" / "Our own work is the evaluation protocol". Its parts are prior work: evaluation matrix and Transfer/Last (ZSCL), Final Forgetting (Chaudhry), held-out control set (SPU; similar in CA-SAM, SAM-Med3D-MoE), joint-training upper reference (De Lange). Individual sentences cite them and l. 105 says "builds on this idea", but the explicit statement of what is ours names the protocol without qualification, and the list of existing methods at l. 193 names only the strategies. An examiner can read Contribution 1 as claiming the control-set idea. One clause would fix it (combination and pretrained-model reference row are ours). | should fix |
| 5.2 | `method.tex:46–48` | "Evaluate all tasks at every stage, including untrained ones" justified as own choice, no pointer to ZSCL (whose Transfer depends on these entries; credited at `background.tex:266`). Back-reference or `\cite[Fig.~4b]{zheng2023…}`. | minor |
| 5.3 | `method.tex:105` | "As an upper reference, we use joint fine-tuning" uncited in Ch. 5; De Lange attribution only in Ch. 3 (l. 333). Back-reference. | minor |
| 5.4 | `method.tex:255–258` | Kaiming-uniform init and input-only dropout read as own design choices; l. 265 says LoRA layers adapted from CLIP-LoRA's code. If inherited, say so (see 2.12). | minor |
| 5.5 | `background.tex:274` | "We measure this loss of pretrained ability with a control task" before the SPU attribution at l. 316; acceptable (Ch. 1 l. 105 already says "builds on this idea"); "(following SPU, see below)" would remove doubt. | minor |

**Handled well:** `introduction.tex:150` (meta-net "our addition, inspired by CoCoOp"); `method.tex:343` (only tokens and scaling from CPE-CLIP); `method.tex:342` (0.25 bound "not part of CPE-CLIP"); `method.tex:382–394` (differences from ZSCL incl. public code); `experiment_results.tex:604` (results "do not describe the original methods"); `appendix.tex:120–122`.

## Priorities
- **Must fix:** 2.1.
- **Should fix:** 2.2, 2.3, 2.4, 2.5, 5.1.
- **Minor:** 2.6–2.12, missing locators, 5.2–5.5.
- **Keys:** all exist; ~50 bib entries unused.
