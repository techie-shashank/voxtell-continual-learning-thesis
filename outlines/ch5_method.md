# Ch. 5 Method — restructure outline v2 (approved by the author 2026-10-31)

Previous outline (2026-10-21): `backups/ch5_method_outline_2026-10-31_v1.md`.

Scope unchanged: what we built and why, with symbols, not values (values: Ch. 6 setup). Concepts as published: Ch. 3. Data, splits, prompts, few-shot subsets: Ch. 4 (referenced, not repeated).

Principle: each section uses only what comes before it. The protocol (contribution 1) is defined in one place, 5.1. Costs are discussed in one place, 5.4. Restructuring moves existing `% CLAUDE-DRAFT` paragraphs; new text only where marked (new).

Author decisions 2026-10-31: no deviation table for ZSCL/CPE-CLIP (prose lists stay); equal-updates principle in 5.1, values in Ch. 6; two algorithms, each in the section that defines its parts (option b); thesis-specific protocol choices move from Ch. 3.3 to 5.1.

## Chapter opening (3 sentences, rewrite)
The chapter defines the protocol and the strategies it compares; order: setting and protocol → VoxTell and the shared procedure → strategies → cost; values in Ch. 6.

## 5.1 Continual-learning setting and evaluation protocol — DONE 2026-10-31 (no subsections, author decision; order: protocol, entries, algorithm, run variables, pretrained, joint)
Optional subsections if it reads too dense: 5.1.1 Setting, 5.1.2 Evaluation protocol.
1. Tasks, their sets, shared volumes → forgetting on the same images (current 5.1 par. 1)
2. Scenario closest to TIL (current 5.1 par. 2)
3. Control task and why chosen (current 5.1 par. 3) + the "our control task vs SPU's control set" sentence from Ch. 3.3
4. Protocol: evaluate all tasks and the control task after every stage; matrix and control row **reminded, not redefined** (symbols defined in Ch. 3.3); why i > j is evaluated; reported metrics in Ch. 6 (current 5.2 par. 1, shortened, since Alg. 5.1 shows the loop)
5. Run variables: task order, k, equal-updates principle (current 5.2 par. 2; equal-updates sentences drafted 2026-10-31)
6. Entries: per-volume DSC averaged over a test set, same test volumes in all runs, per-volume values kept (current 5.2 par. 3, inference details → 5.2)
7. Evaluated parameters: one parameter set for all strategies except task-specific LoRA (one sentence, pointer to 5.3.2)
8. Pretrained-model reference (current 5.2 par. 5)
9. Joint fine-tuning; why intransigence is not computed (current 5.2 par. 6; forward reference to seq. FT settings fixed 2026-10-31)
10. **Alg. 5.1, protocol** (new, outer loop only, ~8 lines): for j = 0..T: if j > 0, θ_j ← Adapt_S(θ_{j−1}, j) (Sec. 5.2, 5.3); a_{i,j} ← Evaluate(Select_S(i, j), p_i, D_i^te); c_j likewise. No θ̃, no additional evaluations. Text: one sentence on Select.
- Pointers only: few-shot subset sampling (nested, one draw, Ch. 4.3), text-prompt wording (Ch. 4, l. 58).

## 5.2 VoxTell and its adaptation to one task — DONE 2026-10-31 (title 'Adapting VoxTell to One Task' kept; intro names the three strategy steps; parameter counts moved from 5.3.1; 24th-epoch sentence deleted, stated in Ch. 6 l. 64; Adapt cost paragraph moved to 5.4)
**Storyline v3 (author approved 2026-10-31; replaces the list below):** one model, VoxTell, used as released, whose implementation fixes where a strategy can act; every strategy runs the same procedure and differs only in three steps; the rest is shared, taken from VoxTell's pretraining where possible, with a reason for every deviation; each task ends with the last-epoch parameters, which are evaluated and carried forward. Order checked for dependencies (no term or symbol before it is introduced).
0. Scope (one sentence): the model we adapt and the procedure with which every strategy adapts it to one task
1. Model and why: checkpoint v1.1, architecture in Ch. 3, why VoxTell, pointer to Fig. 5.1
2. VoxTell as used: stage-4 keys/values ("an input of 192³ voxels" → 12³; used by distillation-based and prompt-tuning strategies); only cross-attention executed (LoRA, learned prompt tokens act there); text encoder frozen; parameter counts
3. The procedure (Alg. 5.2 float here): Adapt θ_{t-1} → θ_t; one procedure with the same settings, so differences are not caused by settings; the three steps (Init, ExtraData, ExtraLoss) → 5.3; shared steps take the settings of VoxTell's pretraining where possible (no tuning budget); following paragraphs describe the shared steps and their symbols
4. Patches and prompts; deviations with reasons (no prompts of absent structures, no augmentation, no deep supervision)
5. Loss
6. Optimisation: SGD μ, ω, η₀; batch size one + batch-128 caveat; U = E·N_t (N_t includes ExtraData); linear decay, reset per task; tables; not tuned per strategy (defense todo)
7. Evaluated parameters: last epoch, carried forward; validation per epoch, same seed; best-validation checkpoint as additional evaluation (not LoRA). Section ends here; 5.3 opens with its own back-reference (l. 239)
Inference (sliding window, threshold) stays in 5.1.

*Superseded list (v2):* 1. Checkpoint and why VoxTell; 2. Where the implementation differs from the paper, Fig. 5.1; 3. Parameter counts; 4. Training samples, what was left out; 5. Loss; 6. Optimiser, schedule, one shared configuration; 7. Validation and checkpoints; 8. Inference; 9. Alg. 5.2.

## 5.3 Continual-learning strategies — DONE 2026-10-31 (cost text moved to 5.4 as one block, to be condensed; replay subsection renamed; resume sentence cut; alpha/dropout caveat moved to Ch. 6.1.3 after the rank-choice paragraph; scaling-ablation sentence deleted, covered by Ch. 6 l. 267 caption and l. 281-284; opening no longer repeats the three steps)
1. Selection by family, alternatives not evaluated
2. What a strategy can change (trainable parameters, start of each task, added data, added loss, evaluated parameters); Table 5.1
3. 5.3.1 Sequential fine-tuning: definition, role as baseline (no cost or parameter counts)
4. 5.3.2 Task-specific and shared LoRA: + adapter selection and forgetting/control-task drop zero by construction (from current 5.2 par. 4); α/dropout sentence → Ch. 6
5. 5.3.3 Shared LoRA with replay (renamed); resume sentence cut
6. 5.3.4 Prompt-tuning strategy; scaling-ablation run → Ch. 6 (order swapped 2026-11-01: one strategy order in Ch. 1, 5, 6, 8 and all tables)
7. 5.3.5 Distillation-based strategy; weight ensemble as additional evaluation; teacher-on-CPU sentence cut unless needed for 5.4; Table 5.1 float placed here, referenced from the section opening
- No cost paragraphs in the subsections (→ 5.4).

## 5.4 Computational complexity — DONE 2026-10-31 (three paragraphs: protocol, Adapt per strategy, memory/storage/inference; 'small overhead' claim now backed by the shared-LoRA epoch times in Ch. 6.7; momentum only for parameters with gradients, checked in code)
1. Cost of Alg. 5.1: training linear, evaluation quadratic in T (current 5.2 last par., without the 1036 → Ch. 6)
2. Cost of Alg. 5.2 per strategy: backward reach, optimiser state, teacher pass, N_t (current 5.3 last par. + the five subsection cost paragraphs + current 5.5 par. 1, condensed)
3. Memory, storage, inference; Table 5.3; measured values in Ch. 6

## Ch. 3.3 changes (cross-chapter) — DONE 2026-10-31
- Keep: evaluation after every stage (ZSCL), matrix and its symbols a_{i,j}, c_j, SPU's control set, metric definitions.
- Move to 5.1: "We therefore also evaluate the model on a control task …" (own choice, reworded as concept: a control task measures loss of pretrained ability outside the sequence) and "Our control task instead comes from a dataset …" (background.tex l. 321).

## Moves to Ch. 6
24th-epoch validation; α and dropout of the LoRA runs; scaling-ablation run. (The 1036 inferences stay in 5.4: Ch. 6 l. 565 uses the number and points to `sec:method-complexity` for its derivation.) Check that Ch. 6 already states each before deleting from Ch. 5.
