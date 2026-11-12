# Pass 4 — Consistency (2026-11-12)

Report-only subagent pass (fresh agent, new session). No files edited by the agent. Saved by the main session.

**Overall:** good. Forbidden-term greps clean outside related-work descriptions (lifelong, incremental learning, text-guided, Dice score, lower bound, ZSCL-based, CPE-CLIP-based, TIL-LoRA, retention drop, ordering, background conflict, zero-shot for the control task, "method" for our strategies, bare "prompt"). Every own-result decimal in Ch. 6, Summary and App. A found in `thesis/tables/*.tex` or the CSVs. No "I", no future tense, every figure and table referenced. Remaining: notation clashes, caption self-containment, minor label/precision drift. **No must fix.**

## 1. Terminology
| # | Location | Problem | Severity |
|---|---|---|---|
| T1 | method.tex:220, 237 | Sec. 5.3 "Continual-Learning Strategies" includes the subsection "Sequential Fine-Tuning"; the term means only the five. | should fix |
| T2 | introduction.tex:152 vs method.tex:225–227 | Intro names Liu et al.'s families "replay, regularisation, and parameter-efficient adaptation" (De Lange's names mixed in); term list and method.tex:227 use "multimodal replay, cross-modal regularisation". | should fix |
| T3 | introduction.tex:31, 202; related_work.tex:16, 20, 33, 51, 239, 244, 266; method.tex:252; tables/ch2_sota.tex:26 | "text-promptable" used as umbrella term (fixed-vocabulary and free-text), not in the term list; experiment_results.tex:255 calls the CLIPSeg-based MedPEFT-CL model "text-prompted", method.tex:252 "text-promptable". Add to list, pick one form. | should fix |
| T4 | method.tex:205–206, 386, 408, 412 vs Ch. 6/summary (42× "updates"), method.tex:203 ("training step") | "iterations", "updates", "training step" for the same thing; notation calls U "iterations per task", Table 6.3 "Vol. (updates)". State once or use one word. | should fix |
| T5 | experiment_results.tex:173 (caption "at each checkpoint (columns)") | Columns are *stages* j (background.tex:267, 282); "checkpoint" also used for best-validation and v1.0/v1.1. | minor |
| T6 | method.tex:112 "Our joint model"; experiment_results.tex:614 "the joint reference"; tables/appA_matrices.tex:124, 143, 162, 181 "Joint" | Prescribed: "joint fine-tuning". | minor |
| T7 | tables/ch5_strategies.tex:12 "Sequential fine-tuning"; ch5_voxtell_strategies.pdf legend "distillation:", "prompt tuning:" | Prescribed labels "Seq. fine-tuning", "Distillation-based", "Prompt tuning"; Table 5.1 omits r for LoRA rows. | minor |
| T8 | ch6_main.tex:14 "Joint fine-tuning (upper reference)" vs ch6_few_shot "Joint fine-tuning"; "Pre" (ch6_main_matrices) vs "Pre." (appA_matrices) | Label variants. | minor |
| T9 | prose, e.g. summary.tex:37, 48, 56, 66 | "Always state the rank r" often not followed in prose; acceptable since experiment_results.tex:74 fixes ranks; rule could be softened. | minor |
| T10 | method.tex:224 "no mechanism to reduce forgetting" | Generic "mechanism"; banned only as a name for strategies. | minor |
| T11 | experiment_results.tex:11 "Experiments and Results" | CLAUDE.md / supervisor outline: "Experiment & Results". Confirm. | minor |
| T12 | tables/ch6_hparams.tex:11 "polynomial, exponent 1" vs "linear decay" (experiment_results.tex:65, method.tex:206); α "Scaling constant" vs "LoRA scaling hyperparameter" (notation.tex:74); M_max "Maximum memory size" vs "capacity of the memory" | Same thing, different words. | minor |

Full names at first use OK (introduction.tex:149, 151).

## 2. Notation
| # | Location | Problem | Severity |
|---|---|---|---|
| N1 | notation.tex:55 vs 85; method.tex:359 | $\vec{q}$ text query (and $\vec{q}_l$) vs $q_{g,v}$ / $\bar q_{g,v}$ distillation distribution; neighbouring Method subsections. | should fix |
| N2 | notation.tex:50 vs 64 | $\mat{U}$ query vectors vs $U$ iterations per task. | should fix |
| N3 | notation.tex:57 vs 64 | $\mat{E}_s$ guidance matrix vs $E$ epochs per task; both in Method. | should fix |
| N4 | background.tex:191 vs 196 (eq:bg-rslora); method.tex:256 | $\gamma_r$ defined as $\alpha/r$ then $\alpha/\sqrt{r}$; only the second in the table. Call the original "the factor $\alpha/r$". | should fix |
| N5 | notation.tex:50, 61 | $\mat{S}$ source vectors vs $\mathcal{S}$ strategy; shows in alg:adapt. | minor |
| N6 | notation.tex:43, 49, 55, 84 | "f" overloaded: $f_\theta$, $f_{\mathrm{text}}$, $\vec{f}_v$ / $\bar{\vec f}$, $\mat{F}_s$. | minor |
| N7 | notation.tex:68, 77 | $\ell$ (validation loss) vs $l$ (layer index). | minor |
| N8 | notation.tex:31, 34 ("Sec." column) | $T$, $\mathcal{D}_t^{\mathrm{tr}}$ first defined in background.tex:163–164, not sec:method-setting-protocol. | minor |
| N9 | background.tex:240 | $\beta_t$ sums over $\tau=0,\dots,t$, conflicting with $t=1,\dots,T$. | minor |
| N10 | notation.tex:38 vs 40 | Hat = binary prediction in $\hat{\mat Y}$, probability in $\hat y_v$. | minor |

**Used but not in notation.tex** (minor; local/algorithm-only): $u$ (method.tex:175), $e$ (171), $\mathcal{L}$ (174), $\mathcal{D}$ (205), $|\mathcal{D}^{\mathrm{te}}|$ (402), $\mat{W}$ (background.tex:58, 180), $\hat\theta_0$, operators Up, ConvBlock, MHA, head$_i$, Adapt/Init/Select/ExtraData/ExtraLoss. At least $u$, $\mathcal{L}$, $\mathcal{D}$ should be added or explained.
**Unused notation entries:** none.
**Typeface:** OK; $\theta$, $\phi$, $\psi$ plain italic though parameter vectors — one sentence ("parameter sets") would settle it (minor).

## 3. Acronyms
| # | Location | Problem | Severity |
|---|---|---|---|
| A1 | 234 raw "LoRA" vs 4 `\gls{lora}` (introduction.tex:144, related_work.tex:69, 203, background.tex:178) | Output correct (no raw before first \gls), but inconsistent with DSC (88× \gls). Decide and record. | minor |
| A2 | method.tex:202; experiment_results.tex:575 | "stochastic gradient descent" written out after `\gls{sgd}` (background.tex:140). | should fix |
| A3 | method.tex:232; related_work.tex:250, 252; tables/ch2_sota.tex:58–60 | "elastic weight consolidation" re-expanded after `\gls{ewc}` (related_work.tex:177); raw "EWC". | minor |
| A4 | related_work.tex:224–226, 278 | Raw "SAM" after `\gls{sam}`. | minor |
| A5 | tables/ch4_datasets.tex:8, ch6_hparams.tex:7, ch2_sota.tex:55 | Raw acronyms in tables. | minor |
| A6 | background.tex:194 "(rsLoRA)", 207 "(LwF)" | Defined inline, not in abbreviations.tex; apply consistently. | minor |

No unused abbreviations; CPU/GPU plain.

## 4. Numbers and precision
| # | Location | Problem | Severity |
|---|---|---|---|
| P1 | appendix.tex:115 "0.98 of the pretrained model" vs Fig. 1.1 "lung: DSC 0.979" and tab:ch6_main/ch6_few_shot (0.979); femoral pretrained 0.68 in text (experiment_results.tex:194, 409, 630) vs 0.684 in appA_matrices | Same quantity at two precisions; experiment_results.tex:94 sets matrix entries to two decimals, Fig. 1.1 breaks that. | should fix (state the rule once, apply in Fig. 1.1) |
| P2 | Fig. ch6_main_matrices | Cells ".86" without leading zero; differs from all other figures/tables; not in caption. | minor |
| P3 | experiment_results.tex:433 "50.3 against 100.7 million" | 100.7 (r = 2048) in no generated table or CSV; untraceable (only-verifiable-numbers rule). | should fix |
| P4 | experiment_results.tex:68, 538, 551 "40 GB" vs ch6_compute "(GiB)" | Mixed units. | minor |
| P5 | Fig. ch6_patellar_loss "3 × 10⁻⁴" vs tables "$3 \cdot 10^{-x}$" | × vs ·. | minor |
| P6 | ch6_main etc. "$r=1024$" vs others "$r = 1024$" | Spacing differs between script outputs. | minor |

Cross-chapter values consistent (Summary vs Ch. 6: 0.114, 0.130/0.135, 0.485/0.781, 0.289→0.046, 0.852/0.485/0.450, 0.429/0.438, 0.839 [0.811, 0.864], 0.124/0.289, 0.832→0.091, 0.337→0.284; Ch. 1 figure 0.979, 0.114; paper values in %: 70.85, 10.72, 96.99, 46.45, 14.78, 44.6→58.9 %). Abstracts empty, not checked.

## 5. Tense and person
| # | Location | Problem | Severity |
|---|---|---|---|
| V1 | experiment_results.tex:53, 69, 74 (present) next to 40–41, 54–55, 68 (past); :632 "We use checkpoint v1.1" after :627 "We used our own random split" | Present and past mixed for what was done. | should fix |
| V2 | method.tex:225, 243 | "et al." without `\ ` spacing. | minor |

## 6. Figures and tables
| # | Location | Problem | Severity |
|---|---|---|---|
| F1 | experiment_results.tex:173 (fig:ch6_main_matrices) | Caption lacks full split, original order, one run each, r values (only in panel titles), two-decimal rounding. | should fix |
| F2 | experiment_results.tex:141 (fig:ch6_main_metrics) | Conditions only via "strategies of Table 6.x"; full split, original order, one run, "mean DSC" missing. | should fix |
| F3 | experiment_results.tex:324 (fig:ch6_few_shot) | Lacks task order, number of runs, strategies/ranks, "mean DSC". | should fix |
| F4 | tables ch6_main, ch6_few_shot, ch6_rank, ch6_task_order, ch6_components (headers "Adapt.", "Forg.", "Ctrl. drop", "Final", "Transf.") | No caption expands the abbreviations. | should fix |
| F5 | tables/ch2_positioning.tex, ch2_sota.tex | Bold headers; all others plain. | minor |
| F6 | `tab:ch6_components`, `tables/ch6_hparams.tex`, `ch6_strategy_params.tex` only in the appendix (appendix.tex:60, 68, 85); mixed label prefixes (`tab:ch6_main`, `tab:app-volumes`, `tab:method-strategies`, `tab:positioning`) | Naming convention. | minor |
| F7 | thesis/figures/ch6_control_task_main.pdf | Generated, no longer included (removed 2026-11-04). | minor |
| F8 | tab:ch6_compute caption | Doesn't say times are from one run per strategy. | minor |

Every `fig:`/`tab:` label referenced; algorithms referenced; no `width=` on script plots.

## Priority
Should fix: T1–T4, N1–N4, A2, P1, P3, V1, F1–F4. Everything else minor.
