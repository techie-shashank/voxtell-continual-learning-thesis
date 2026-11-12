# Proofread of the Summary voice proposal (2026-11-12)

Reviewed: `reviews/voice/summary.tex` (AFTER) against `thesis/summary.tex` (BEFORE). Report returned by the proofreader subagent and saved here by the main session (subagent could not write files). Line numbers refer to AFTER as reviewed.

Counts: must fix 1, should fix 5, minor 13.

## Must fix
- l. 102, C²GR attribution: "Replaying generated samples instead would avoid storing patient data, as C$^2$GR does~\cite{li2026c2gr}." makes the citation cover "avoid storing patient data"; related_work.tex l. 189 supports only that C²GR replays diffusion-generated image–mask pairs.

## Should fix
- l. 58–59: "therefore" now follows "Sequential fine-tuning again forgot most …", so the conclusion about the LoRA strategies reads as following from sequential fine-tuning's forgetting.
- l. 68: "although its Adaptation was lower" turns a trade-off cost ("at a lower Adaptation") into a concession.
- l. 23–24: "It was not trained on …" refers to "the lung", not the control task.
- "However," at sentence start four times (l. 16, 53, 71, 79) plus "In contrast," (l. 38) in about 35 sentences; three created by splitting.
- l. 112: "With checkpoint v1.0 of VoxTell, which was not trained on AeroPath" attaches "which" to VoxTell (v1.1 was trained on AeroPath).

## Minor
- l. 57 "that with the full training split" stands for two values: "those" (also in BEFORE).
- l. 95 "MoE-Adapters, which selects": acceptable as one method's name (also in BEFORE).
- l. 79 "uses one": referent among singular/plural nouns after the split.
- l. 94 "achieves this" refers two sentences back (unchanged from BEFORE).
- l. 39 "Under few-shot conditions" vs CLAUDE.md "few-shot settings" (also in BEFORE; echoes the research question).
- l. 16: long fronted material; "its" points forward across "models".
- l. 36 "The reason is that …": clumsy rendering of "because".
- l. 51 "joint fine-tuning trained on all six tasks": "was trained on".
- l. 60 "Runs with as many updates" lost its comparison.
- l. 102 "instead" ambiguous.
- l. 86 "only" added in "The study also covers only one model".
- C: P4, P6, P7 each turn on a "However," sentence; P1 now six short declaratives in a row (choppy).

## Checks passed
- P3 "respectively" 0.130/0.135 correct (ch6_main.tex l. 7, 12); P5 "respectively" 0.429/0.438 correct (ch6_few_shot.tex, rows "5 (1,080)").
- P8 reordering: "therefore" now follows "each configuration was trained once", the correct premise.
- No banned words, filler, subject–verb insertions or over-strong modals; serial commas and tense correct.
