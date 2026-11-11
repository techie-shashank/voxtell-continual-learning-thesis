# Ch. 7 Discussion — outline revision 5 (PROPOSED 2026-11-10, awaiting author approval); older outlines and collected notes below

## Sec. 7.3 rewrite outline (APPROVED by the author 2026-11-10; label sec:disc-generalisation kept; ~1.5-1.75 p)
1. What may generalise and what not: protocol (requirements only) transferable; patterns that are large here AND reported in other settings (Chen et al., CA-SAM, SAM-Med3D-MoE, Beyond Forgetting, Lifelong nnU-Net); numbers and strategy ranking do not; zero-init hypothesis one sentence, ref to 7.2.
2. Which kind of task the results cover: not segmented in this data (cartilages in training labels, menisci not), same images for all tasks, small adjacent structures, one region/modality; untested: new modality, changing images, pathologies.
3. Practical use (current P3 tightened; unclear l. 153 removed; Ch. 8 implications pending Q1).
4. Extensions to the strategies: goal = one parameter set without task identity that keeps pretrained ability (author's point); text-prompt-similarity adapter selection (MedCRP-CL), MoE-Adapters (with its Ch. 2 caveats), replay across orders/ranks and with selection criteria, other teachers (PRIMED), per-strategy tuning; nested learning only after a verified bib entry.
5. Extensions to training and runs (current P4).
6. Extensions to the evaluation (current P5) + task sequences from other datasets/regions/modalities, control task the checkpoint never saw (v1.0), other models.
Open: author's answers to Q1-Q4 (Claude's recommendations given 2026-11-10).

**ON HOLD (author, 2026-11-10, later the same day):** 7.1 and 7.2 stay as they are for now; work continues on 7.3 only. Whether the Ch. 8 practical paragraph still moves into 7.3 is asked again with the 7.3 rewrite.

## Revision 5b (DECIDED 2026-11-10 by the author; supersedes the structure of revision 5 below)
- Keep the current three sections and labels: 7.1 Answer to the Research Question (`sec:disc-rq`), 7.2 Limitations and Threats to Validity (`sec:disc-limitations`), 7.3 Generalisation and Extensions (`sec:disc-generalisation`). Strengthen the content only.
- Q1: the Final Performance ceiling (observation A) is the main reading of 7.1. **No summary figure.**
- Q2: the practical implications move from Ch. 8 (para 'Within this setting') into 7.3, practical-use paragraph.
- Q3: **no table in Ch. 7**; limitations stay in prose.
- 7.1 = answer paragraph + three blocks: (a) ceiling and what lifted runs above it, with prior work; (b) number of updates, incl. the zero-initialisation hypothesis moved from 7.2 and the joint vs seq. FT k = 5 discrepancy (author's reading needed); (c) protocol. Paragraph-level change list: given to the author in session 2026-11-10.

## Revision 5 (PROPOSED 2026-11-10): full redraft after rereading Ch. 1-6

### Why the current chapter is weak (diagnosis)
1. **7.1 restates Ch. 6 rather than interpreting it.** Most sentences repeat a Ch. 6 metric (0.289, 0.046, 0.138, 0.309/0.574 ...). The 6.2 conclusion already says the same thing, and Ch. 8 says it a third time.
2. **The chapter has no thesis-level reading of its own.** It answers each experiment separately and never shows what all 33 sequence runs show together.
3. **The best interpretive idea is buried.** The update-count / zero-initialisation argument is the only idea that links four experiments (patellar, few-shot, equal updates, first task of shared LoRA), but since 2026-11-07 it sits inside "Limitations, First".
4. **Limitations take about 60 % of the chapter** as a list of caveats, with nothing on which conclusions are robust and which are fragile, so the reader cannot tell what still stands.
5. **Prior work is scattered.** There are four one-sentence citations (MedPEFT-CL, Beyond Forgetting, ZSCL, Silva-Rodríguez) and no section that says where our results agree with the literature, where they disagree and what is new. The chair grades exactly this ("merits and limitations in the context of the state of the art").
6. **Practical implications sit in Ch. 8.** The chair defines the Summary as results only.

### Cross-experiment observations the redraft would build on (all from existing tables, no new results)
- **A. Final Performance ceiling (observation, needs the author's reading).** Every configuration that uses one parameter set, trains on current-task data only and follows the original order ended with Final Performance between 0.117 and 0.233. The pretrained model has 0.114. This covers sequential fine-tuning at every k and with equal updates, the distillation-based strategy, prompt tuning, shared LoRA at every rank and every k, and the 5-volume equal-updates run. Their Adaptation spans 0.44 to 0.78. Only three things lifted Final Performance above this band: the task identity (task-specific LoRA, 0.404 to 0.485), stored samples (replay, 0.450) and the reverse order (shared LoRA, 0.345). Joint fine-tuning reached 0.852 with the same model, so the ceiling comes from the sequence, not from the model's capacity. Sources: ch6_main.tex, ch6_few_shot.tex, ch6_rank.tex, ch6_task_order.tex.
  - Caveat to state: Final Forgetting is partly tied to Adaptation by definition, because a strategy that forgets everything has FF ≈ Adaptation. This is why Final Performance, not Final Forgetting, carries the argument. The last task alone contributes about 1/6 of its diagonal value to Final Performance.
  - This is a different claim from the representation view the author rejected on 2026-11-06 (circular, features never measured). It is descriptive and claims no mechanism.
- **B. The number of updates links four experiments.** (i) The LoRA strategies learned nothing with 50 to 200 updates but learned with 1,080 on the same 5 volumes. (ii) Sequential fine-tuning kept the control task with 50 updates per task (drop 0.010) and lost it with 1,080 on the same 5 volumes (0.979). (iii) Patellar was not learned in 10 epochs but was learned in 50. (iv) Shared LoRA learned its first task poorly in both orders. Candidate mechanism: zero-initialised B, the author's hypothesis from 2026-10-22, with the evidence for and against kept in §1 below.
  - Examiner trap: joint fine-tuning with k = 5 had 300 updates in total and a control-task drop of 0.733. Sequential fine-tuning with k = 5 also had 300 in total (6 × 50) but a drop of 0.010. So "updates alone" does not explain the control-task loss. To be raised in the interview, not interpreted by Claude.
  - Few volumes cost little at equal updates (Adaptation −0.03 to −0.07), consistent with SEA-PEFT, where full fine-tuning did not improve from 5 to 10 shots (Table 1).
- **C. Agreement and disagreement with prior work** (facts from Ch. 2 and paper_notes):
  - Agrees: replay gave the best trade-off (Beyond Forgetting, Lifelong nnU-Net, MedPEFT-CL Table 8). Separate LoRA per task beat one sequential LoRA (LiLoRA 88.13 vs 46.21). Chen et al. found the same two outcomes as ours: sequential fine-tuning learned well and then collapsed (0.80 → 0.16), while task-specific LoRA learned less but was unaffected (0.60). Parameter-efficient methods trailed full fine-tuning on new structures (Silva-Rodríguez). Losses outside the adapted tasks also appear in CA-SAM (LwF −16.6 to −46.5 pp) and SAM-Med3D-MoE (0.541 → 0.400). The task order affected results (Lifelong nnU-Net, Beyond Forgetting).
  - Disagrees: ZSCL distillation preserved Transfer, ours did not. rsLoRA expects higher ranks to learn better, whereas our Adaptation fell with rank (with γ_r falling, α fixed). CPE-CLIP's gradient scaling had a weaker effect here than in its paper (App. A).
  - New in this thesis: 3D free-text model, update budget separated from volumes, pretrained ability measured outside the sequence.

### Proposed structure (about 6-7 pages; numbers only where an argument needs them, otherwise \cref to Ch. 6)
- **Opening** (2 sentences): what the chapter adds beyond the per-experiment conclusions of Ch. 6.
- **7.1 Answer to the Research Question** (~0.5 p). One paragraph: the answer in four claims, each pointing to the section that argues it. No metric values except the ones that define the answer.
- **7.2 One Trade-off Across Strategies and Settings** (~1.5 p; objectives 2 and 4). Observation A, with an optional synthesis figure (Adaptation against Final Performance, plus a panel with the control-task drop, for all sequence runs; colour = strategy, marker = experiment; generated from cl_metrics.csv). Argues that freezing the backbone, low rank or small γ_r, distillation and fewer updates moved runs *along* the trade-off. Only task identity, replay and the task order moved them *off* it. Prompt tuning and the distillation-based strategy appear as instances, not in paragraphs of their own. Prior work woven in here: LiLoRA, Chen et al., MedPEFT-CL, Beyond Forgetting.
- **7.3 The Number of Updates as a Common Factor** (~1.25 p; objective 3). Observation B: the four experiments, the zero-initialisation hypothesis with its evidence for and against, and the joint-vs-sequential k = 5 discrepancy (author's reading). Implication for evaluation: few-shot continual-learning comparisons have to fix or report the number of updates, not only k. Prior work here: Silva-Rodríguez (200 epochs), SEA-PEFT, the rsLoRA contrast.
- **7.4 Merits and Limits of the Evaluation Protocol** (~0.75 p; objective 1). Covers the control-task drop and Final Forgetting diverging in both directions, joint fine-tuning losing the control task without any sequence, and the pretrained reference revealing "no learning". Compared with the closest works (none measures pretrained ability) and with SPU and CA-SAM. The protocol's own limits stay here, next to the claim: one control structure, AeroPath and possibly SKM-TEA in the v1.1 training data, a joint reference only for i = T.
- **7.5 Implications for Adapting a Universal Model** (~0.5 p; moved from Ch. 8 para 6 and current 7.3 para 3). All conditional: task-specific LoRA for a closed set of structures with fixed text prompts (0.2 M parameters per task); replay without task identity, at the cost of storing patient data and 26.4 vs 19.8 min per epoch; plan the update budget, not the epochs; a frozen backbone alone did not preserve pretrained ability; universality is lost unless parameters are isolated or samples replayed.
- **7.6 Limitations and Threats to Validity** (~1.25 p). Leads with a **table of conclusions against their evidence**, with columns: conclusion, runs behind it, main threat, robust or fragile. Example: "Seq. FT forgets almost all" is robust (both orders, all k except 5, large effect). "Replay is best without task identity" is fragile (one run, one order, one rank). After the table, compact prose on the cross-cutting threats: single run per configuration with the task-specific original/reverse pair as the measured spread; the shared configuration; ranks chosen on test results; α and dropout differing between the LoRA strategies; the narrow scope; the data and checkpoint (own split, orientation, echo 1, v1.1 overlap); strategies not evaluated (PRIMED teacher, MedCRP-CL selection, EWC). The existing 7.2 sentences are reused but shortened.
- **7.7 Generalisation and Future Work** (~0.75 p). Separates what may transfer (mechanism-level observations A and B, as hypotheses) from what does not (the numbers). One kind of new task (D2). Future work ordered by which *fragile* conclusion in the 7.6 table it would firm up.

### Consequences for other chapters (if approved)
- Ch. 8: remove the practical paragraph (now 7.5) and cut the "training budget as a common factor" paragraph to one sentence with a reference to 7.3; keep the per-objective answers.
- Ch. 6: the conclusion of 6.6 refers to `sec:disc-limitations` for the zero-initialisation explanation; this pointer would change to the new 7.3.
- Optional new figure `thesis/figures/ch7_tradeoff.pdf` (script in scripts/, from cl_metrics.csv).

### Questions for the author before drafting (interview; reasoning-heavy chapter)
1. Do you accept observation A (Final Performance ceiling) as the central reading of 7.2, and do you want the synthesis figure?
2. Prior work: woven into 7.2-7.4 (recommended), or a separate section "Relation to Prior Work"?
3. Move the practical implications from Ch. 8 to Ch. 7 (7.5)?
4. Limitations as a table of conclusions against evidence, followed by short prose?
Later, during drafting: your reading of joint k = 5 vs seq. FT k = 5 (same 300 updates, control-task drop 0.733 vs 0.010); why 5 volumes cost so little at equal updates; whether you still defend the zero-initialisation hypothesis as your own; and the rsLoRA contrast.

---

# Older outlines (revision 2 approved 2026-10-24; revisions 3-4 of Sec. 7.1, 2026-11-06)

## Placement (approved 2026-10-24)
Own compact chapter (option A). Neither guideline prescribes a Discussion chapter: supervisor outline ends with Experiment and Results ("include the conclusions of each experiment") and Summary; chair structure = Introduction, main section, Summary (Sec. 1.7: most important results, own work stated, 3-4 pages). Discussion content is graded by the chair (Sec. 3.2: critical discussion of the results, limitations, generalisation or extension; Sec. 1.6.1: merits and limitations in the context of the state of the art). Fallback if the supervisor prefers: last section of Ch. 6 (same content, headings only). To confirm in the supervisor email together with the Method chapter.

## Outline revision 2 (approved 2026-10-24)
About 6 pages. Prior work integrated where it makes a point (no separate prior-work section). R = needs the reruns, N = now.
- **Intro** (N): 2 sentences. Drafted 2026-10-24.
- **7.1 Answer to the Research Question** (~1.5 pp.): one paragraph per objective (2, 3, 4, then 1), each ending in an explicit answer. Beyond Forgetting (order), MedPEFT-CL (after reruns). Obj. 2, 3 R; obj. 4 (order incl. last-step observation, rank as observed trade-off with alpha fixed) and obj. 1 N.
- **7.2 Training Budget as a Common Factor** (~1.5 pp., N): adapter-from-zero hypothesis, evidence for/against, Silva-Rodríguez et al., consequence for 7.1. Drafted 2026-10-24 (about 2 pp.).
- **7.3 Limitations and Threats to Validity** (~1.5-2 pp., N): main three first (shared budget + confounds; one run per configuration, D40; narrow scope), control-task proxy fourth; then internal / construct / external, one sentence each; SEER (prompt wording); PRIMED, MedCRP-CL as alternatives not evaluated.
- **7.4 Generalisation and Extensions** (~1 p., N): mechanism may hold for other models (hypothesis), numbers do not transfer; anatomy/CT untested; nothing about truly unseen structures (D2); future work with reasons: test of the hypothesis, seeds and support-set draws, rephrased text prompts, more task orders; joint reference only if the reruns fail; other models one sentence.

**Current structure (updated 2026-11-10; 7.2 'Training Budget' folded into the Limitations on 2026-11-07, so the old 7.3/7.4 are now 7.2/7.3):**
- **7.1 Answer to the Research Question** — organised by theme (2026-11-06).
- **7.2 Limitations and Threats to Validity** — shared configuration and confounds (incl. zero-initialisation hypothesis, Silva-Rodríguez), single run, narrow scope, protocol limits, internal validity, strategies not evaluated, external validity.
- **7.3 Generalisation and Extensions** (approved 2026-11-10): (1) quantitative results do not generalise, zero-initialisation explanation may; anatomy/CT untested; (2) one kind of new task (D2); (3) practical use: task identity for a closed set only, adapter memory, replay stores patient data and costs time; (4) extensions to training and runs, in the order of the 7.2 limitations: test of the hypothesis, per-strategy tuning, equal-updates runs at k = 10, 20 and other strategies, seeds and draws; (5) extensions to the evaluation: more task orders, rephrased text prompts, broader control task, other models. The joint-reference item is dropped (joint fine-tuning was run).

- **Summary (Ch. 8)**: most important results, own work stated (chair), short answer per objective, future-work list.

## Sec. 7.1 outline revision 3 (PROPOSED 2026-11-06, awaiting author approval)
Reason: the objective paragraphs restate Ch. 6 result by result with its numbers (CLAUDE.md: Discussion must not repeat per-experiment conclusions). 7.1 is ~1,600 words; target ~800. Rule for every objective paragraph: (1) answer with `\cref` to Ch. 6; (2) what links it to other experiments or how to read it; (3) prior work, where it exists; (4) main caveat in one clause, details in 7.2/7.3. Numbers only where the argument needs one.

- **Opening (keep as is, 5 sentences):** RQ with ref, scope, three-sentence overall answer, order.
- **Obj. 2 (4 paragraphs, ~500 words → 1 paragraph, ~5 sentences):** (1) no strategy combined adaptation and retention (6.2); (2) joint fine-tuning also lost the control task → loss of pretrained ability comes with fine-tuning the pretrained weights, loss of earlier tasks with the sequence; (3) prompt tuning: frozen backbone and fewer parameters do not by themselves explain retention, since shared LoRA also acts on every text prompt and retained more; property not tested; (4) replay the only addition that lowered forgetting without lowering Adaptation, as in MedPEFT-CL, at extra cost (→ 7.3). Cut: all Ch. 6 metric values, femoral-cartilage detail, distillation −0.048 (6.2 states it), patellar sentence (→ 7.2), separate 'In answer' paragraph. Open: universality sentence only if the author confirms it.
- **Obj. 3 (11 sentences → ~4):** (1) with ten epochs, only seq. FT learned in the few-shot settings; at k = 5 the number of updates decided whether the LoRA strategies learned (6.4), interpretation in 7.2; (2) the one effect of volumes at equal updates: shared LoRA's control-task drop +0.097; (3) caveat: k = 5 only, one draw, one run. Cut: equal-updates numbers, seq. FT 0.227/0.130, 50 vs 1,080 updates; 'more updates, more forgetting' stays only in 7.2.
- **Obj. 4 (2 paragraphs, ~370 words → 1 paragraph, ~5 sentences):** (1) rank and task order moved shared LoRA along the adaptation-retention trade-off (6.5, 6.6); task-specific LoRA independent of order by design and no gain from r = 8; seq. FT forgot almost everything in both orders; components did not keep the control task (App. A); (2) shared LoRA's metrics are a property of strategy and order: forgetting concentrated in the last step (lateral meniscus), structure vs position not separable; (3) Beyond Forgetting; (4) caveat: rank and γ_r confounded (→ 7.3). Cut: rank and order value ranges, 0.004.
- **Obj. 1 (8 sentences → ~5):** (1) protocol separated the effects as intended; (2) control task vs Final Forgetting (keep 0.237 vs 0.091) and pretrained reference row (keep 0.114), joint reference as half-sentence pointing to obj. 2; (3) gap vs MedPEFT-CL and Beyond Forgetting; (4) limits → 7.3 and requirements in one sentence.

## Collected notes (started 2026-10-22)

Not an outline yet. Collects points that span experiments, so they are not lost. The Discussion interprets results already reported in Ch. 6; it presents no new results. Open defense points: `thesis_tracker.md`.

## 1. Adapters that start from zero need many updates (hypothesis; author's idea, refined 2026-10-22)

**Wording (agreed 2026-10-22):** a hypothesis consistent with the observations, not a finding. "An adapter that starts from zero needs many updates before it changes the model's output; at high rank, ten epochs were not enough for the first task. Later tasks start from an adapter that has already moved, so they adapt within their ten epochs, even when the first task itself was not learned."

**Evidence for** (all reported in Ch. 6):
- Shared LoRA r = 1024, first task: training loss from ≈1.0 (empty prediction) only to 0.69 (original, LT) and 0.96 (reverse, LM) after 10 epochs; DSC right after training 0.29 and 0.01; the same structures reach 0.51 / 0.40 when trained later in the other order (6.6).
- Second task starts at 0.81 / 0.86 and falls to 0.56 in both orders, even in the reverse order where the first task was hardly learned (6.6) → the benefit is more likely the adapter having moved than knowledge of a similar structure.
- Rank: first-task Adaptation 0.69 (r = 4) → 0.28 (r = 2048), other tasks lose at most 0.17 (6.3).
- Patellar diagnosis: task-specific LoRA (always from zero) stays on the empty-prediction plateau for 10 epochs at r = 4/16, lr 3e-4, other seed; 50 epochs reach 0.839, with the drop at epoch 12 (6.4).
- Few-shot: with 50–200 updates per task neither LoRA strategy learns any task (6.5).
- Mechanism (from the LoRA formula, Hu et al. initialisation): B = 0 at the start, so the gradient of A is zero at the first step; only B moves at first.

**Evidence against / limits:**
- Rank dependence unexplained: at r = 4 the first task leaves the plateau within 3 epochs (loss 0.74 at epoch 3); rsLoRA's 1/√r scaling is meant to make learning rank-independent (6.3).
- Task-specific LoRA r = 4 learns most tasks from zero within 10 epochs (LT 0.64, MM 0.57); patellar is the exception (structure-dependent).
- "Similar structures help" cannot be separated from "adapter has moved" with these runs.
- Does not explain the retention difference between orders for shared LoRA (forgetting 0.124 vs 0.289; D41).

**Tests (future work only; author decided 2026-10-22 that no extra run is possible):** first task with more epochs at r = 1024; warm-started adapter (e.g. first task trained twice, or adapter initialised from another task) vs zero adapter; α or learning-rate sweep at high rank.

**Consequence for the research question:** under one shared training configuration (10 epochs), the parameter-efficient strategies are limited by training length, most in few-shot settings (D16, D39) — the comparison measures strategies under this budget, not at their best.

## 2. Other points to discuss (pointers)
- Order dependence of shared LoRA (D41), only two orders.
- Few-shot: data vs updates (D9, D39) once the equal-updates reruns are in.
- Variation between runs vs bootstrap intervals (D40, D11): task-specific original/reverse as the only repeat-like pair.
- Shared LoRA r = 1024 understates control-task retention (D37).
- Limitations list: `thesis_notes.md` §3, tracker section A (status open / author).

## 3. Prior work to compare with in the Discussion (from the Ch. 2 notes, 2026-10-23; facts only, interpretation is the author's)
- MedPEFT-CL (`paper_notes/NEW_medpeftcl2025.md`, Table 8): its PEFT part alone was worse than sequential fine-tuning; replay gave the largest single gain (2D CLIPSeg, full data).
- Silva-Rodríguez et al. (`paper_notes/cards/NEW_silvarodriguez2023fseft.md`): at K = 10, LoRA on the encoder only reached 38.49 vs 52.38 DSC for full fine-tuning on novel organs (3D, single task).
- SEA-PEFT (`paper_notes/cards/NEW_seapeft2026.md`): full fine-tuning did not improve from 5 to 10 shots.
- PRIMED (`paper_notes/chen2025forgingdynamicmemoryretrievalguided.md`, Table 4a): previous-task teacher better than initial-model teacher (D42).
- Beyond Forgetting (`paper_notes/cards/NEW_beyondforgetting2026.md`): no strategy meets all requirements; task order matters (10 permutations).
- SEER (`paper_notes/cards/NEW_seer2026.md`): VoxTell's sensitivity to prompt phrasing (D10).
- MedCRP-CL / MedPEFT-CL: adapter selection by text-prompt similarity (D43).
