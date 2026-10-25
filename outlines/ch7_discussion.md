# Ch. 7 Discussion — outline revision 2 (APPROVED 2026-10-24) and collected notes

## Placement (approved 2026-10-24)
Own compact chapter (option A). Neither guideline prescribes a Discussion chapter: supervisor outline ends with Experiment and Results ("include the conclusions of each experiment") and Summary; chair structure = Introduction, main section, Summary (Sec. 1.7: most important results, own work stated, 3-4 pages). Discussion content is graded by the chair (Sec. 3.2: critical discussion of the results, limitations, generalisation or extension; Sec. 1.6.1: merits and limitations in the context of the state of the art). Fallback if the supervisor prefers: last section of Ch. 6 (same content, headings only). To confirm in the supervisor email together with the Method chapter.

## Outline revision 2 (approved 2026-10-24)
About 6 pages. Prior work integrated where it makes a point (no separate prior-work section). R = needs the reruns, N = now.
- **Intro** (N): 2 sentences. Drafted 2026-10-24.
- **7.1 Answer to the Research Question** (~1.5 pp.): one paragraph per objective (2, 3, 4, then 1), each ending in an explicit answer. Beyond Forgetting (order), MedPEFT-CL (after reruns). Obj. 2, 3 R; obj. 4 (order incl. last-step observation, rank as observed trade-off with alpha fixed) and obj. 1 N.
- **7.2 Training Budget as a Common Factor** (~1.5 pp., N): adapter-from-zero hypothesis, evidence for/against, Silva-Rodríguez et al., consequence for 7.1. Drafted 2026-10-24 (about 2 pp.).
- **7.3 Limitations and Threats to Validity** (~1.5-2 pp., N): main three first (shared budget + confounds; one run per configuration, D40; narrow scope), control-task proxy fourth; then internal / construct / external, one sentence each; SEER (prompt wording); PRIMED, MedCRP-CL as alternatives not evaluated.
- **7.4 Generalisation and Extensions** (~1 p., N): mechanism may hold for other models (hypothesis), numbers do not transfer; anatomy/CT untested; nothing about truly unseen structures (D2); future work with reasons: test of the hypothesis, seeds and support-set draws, rephrased text prompts, more task orders; joint reference only if the reruns fail; other models one sentence.
- **Summary (Ch. 8)**: most important results, own work stated (chair), short answer per objective, future-work list.

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
