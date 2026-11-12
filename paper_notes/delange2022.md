# Continual learning survey (De Lange et al.) — paper notes

Partial notes: the parts used by Ch. 2 and Ch. 3 (definitions, taxonomy, baselines). Sections 1–4 are what the **paper** says; section 5 is **analysis for this thesis**.

| | |
|---|---|
| Paper | De Lange, Aljundi, Masana, Parisot, Jia, Leonardis, Slabaugh, Tuytelaars. *A Continual Learning Survey: Defying Forgetting in Classification Tasks.* IEEE TPAMI 44(7), 2022, pp. 3366–3385 (bib) |
| Local PDF | `voxtell_paper/delange.pdf` = **author's version** (arXiv:1909.08383v3, 16 Apr 2021), 29 pages. Page numbers below are this version's pages, not the TPAMI pages; cite by **section** |
| Bib key | `delange2022` |
| Notes written | 2026-10-22 |

## 1. Problem (Sec. 1, p. 1)
- "The major challenge is to learn without catastrophic forgetting: performance on a previously learned task or domain should not significantly degrade over time as new tasks or domains are added."
- This is "a direct result of a more general problem in neural networks, namely the stability-plasticity dilemma [20], with plasticity referring to the ability of integrating new knowledge, and stability retaining previous knowledge while encoding it."
- Data may be available only temporarily "due to storage constraints or privacy issues" (p. 1).

## 2. Settings (Sec. 2, p. 2–3)
- Task incremental setting: a sequence of tasks, training data of one task at a time, limited or no access to data of previous tasks (Eq. 1).
- "task" = an isolated training phase with a new batch of data (new classes, domain or output space). Subdivision following [32] by P(Y) and P(X): **class incremental** (one output space for all observed classes), **task incremental** (separate output spaces; requires the task label at test time to select the output nodes), **incremental domain** (same labels, changing input distribution); plus data incremental (no notion of task). The survey's experiments use task incremental classification.

## 3. Taxonomy (Sec. 3, Fig. 1, p. 3–4)
Three families "based on how task specific information is stored and used":
- **Replay** (Sec. 3.1): store samples in raw format or generate pseudo-samples; replayed while learning a new task. *Rehearsal* methods "explicitly retrain on a limited subset of stored samples while training on new tasks"; performance "upper bounded by joint training"; "might be prone to overfitting the subset of stored samples". iCaRL stores exemplars per class selected to approximate class means; Rolnick et al. reservoir sampling. Constrained optimisation (GEM, A-GEM) and pseudo-rehearsal / generative replay are the other branches.
- **Regularisation-based** (Sec. 3.2): extra loss term, no raw inputs stored. *Data-focused*: knowledge distillation from a previous model to the model trained on new data; LwF uses "the previous model output as soft labels for previous tasks"; vulnerable to domain shift between tasks. *Prior-focused*: importance-weighted penalties on parameter changes (EWC, SI, MAS).
- **Parameter isolation** (Sec. 3.3): different parameters per task; growing branches or fixed parts with masks; "typically require a task oracle" at prediction.

## 4. Baselines and findings used here (Sec. 5–6)
- Baselines: finetuning (starts from the previous task model); joint training on all data of the sequence, "a soft upper bound"; basic rehearsal with full memory (R-FM) or partial memory R/T per task (R-PM) (Sec. 5, p. 7–8).
- Summary claim: task ordering "to have insignificant impact on performance" (Sec. 1, p. 2; Sec. 6.6) — for their classification benchmarks.

## 5. Analysis for this thesis (NOT from the paper)
- Citable for: catastrophic forgetting definition and stability–plasticity dilemma (Sec. 1); scenario definitions (Sec. 2) for Ch. 2; the three families (Sec. 3) for Ch. 2; rehearsal mechanism (Sec. 3.1) for Ch. 3.3; joint training as soft upper bound (Sec. 6.2.1 and 6.3.1; corrected 2026-11-12 by citation-verifier, Sec. 5 only lists the baselines).
- The thesis's replay = rehearsal with randomly drawn stored samples (code `random.sample`); the survey does not state how R-FM/R-PM select samples in the parts read, so do not cite it for random selection.
- Task-order finding (insignificant impact) is for classification; compare in Ch. 7 with own original/reverse results, without generalising.
