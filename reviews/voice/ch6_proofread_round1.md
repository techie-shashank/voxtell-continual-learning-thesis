# Proofread of Ch. 6 voice proposal, round 1 (Sec. 6.1–6.2), 2026-11-12

Report from the proofreader subagent, saved by the main session. Counts: must fix 1, should fix 5, minor 13. All number–label assignments in Sec. 6.2 verified against `thesis/tables/ch6_main.tex`.

Applied to `reviews/voice/ch6_experiment_results.tex` (16 fixes):
1. (must, pre-existing) "shared LoRA … lost most of it in the last task" contradicted 0.96 → 0.74 and 0.93 → 0.84 and l. "kept most of the control task": now "most of its control-task drop arose in the last task" (author to approve).
2. (should) "To fit 12 of the 17 runs …" turned a result into a purpose: back to the BEFORE wording.
3. (should) "even though it keeps all pretrained weights frozen" attached to "the first group": subject named, "although" restored.
4. (should) "This loss began right after training." lost its scope (false for prompt tuning): scope restored.
5. (should) "came closest" without anchor: "(0.450)".
6. (should) Transfer values unlabelled: labels added.
7–18 (minor): LoRA values moved out of the coordinated verbs; serial comma l. 84; "the distillation-based strategy and the prompt-tuning strategy"; one "In contrast," removed in the conclusion; "At the same time," restores the link of "Its Adaptation changed by only 0.001"; "These gaps show"; passive "was reached by" replaced; "lowered this loss"; ", and we did not test" split; "same total number of updates as sequential fine-tuning"; "To show an alternative rank".

Not applied: "respectively" list in the Final Performance paragraph kept (labels would make it heavy); short sentences in the main paragraph kept (version B approved by the author); "stayed close" in Transfer (0.129–0.175 against 0.137) left to the author.
