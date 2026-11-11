# Ch. 8 Summary — outline revision 2 (APPROVED 2026-11-11; drafted 2026-11-11)

Author decisions 2026-11-11: framing of Sec. 7.1 (trade-off with one parameter set, exceptions with their costs); own work in the wording of the Ch. 1.5 contributions, no method details; one or two key numbers per result; no practical recommendation (removed 2026-11-10). Target about 3 pages (chair Sec. 1.7: 3-4 pages); drafted at about 1,060 words.

1. Problem and setting (~120 words): universal model fails on rare structures; question; VoxTell, six SKM-TEA structures (pretrained 0.114), AeroPath lung as control task.
2. Own work (~150): prior methods in one sentence; four contributions as in Ch. 1.5; 38 runs.
3. Main result: trade-off (~220): one parameter set + current-task data: more Adaptation, more forgetting of earlier tasks and of pretrained ability; 0.233 in the original order; exceptions task-specific LoRA (task identity) and replay (stored data); joint fine-tuning 0.852.
4. Few-shot (~140): seq. FT learned, LoRA hardly; seq. FT k = 5 forgot less and kept the control task; equal updates at k = 5 point to updates; k = 10, 20 confounded.
5. Order and rank (~100): mainly shared LoRA; reverse order numbers; rank and gamma_r confounded.
6. Protocol (~90): control task vs Final Forgetting (r = 1024 -> 2048); pretrained reference for few-shot LoRA.
7. Limitations (~100): as Sec. 7.2.
8. Future work (~150): main extension (no task identity); tests of the two LoRA explanations (corrected); repeated runs; broader evaluation.

---

# Ch. 8 Summary — outline revision 1 (APPROVED 2026-10-24 with Claude's recommendations for Q1-Q4; drafted 2026-10-24)

Requirements: chair Sec. 1.7 (most important results, which results are the author's own work, 3–4 pages); supervisor outline (Summary as the last chapter); CLAUDE.md (answers each research objective, future work, no new results). One chapter without sections; one idea per paragraph. Every number already appears in Ch. 6 and is cited from there.

1. **Problem and setting** (about 0.5 p.): adapting a free-text promptable universal 3D segmentation model (VoxTell) to new structures one after another with few labelled volumes; six SKM-TEA knee structures as tasks, the AeroPath lung as control task; why forgetting matters for a universal model.
2. **What this thesis did — own work stated** (about 0.5 p.): the evaluation protocol (evaluation after every task, control task, pretrained reference row, few-shot settings k = 5/10/20, two task orders, paired bootstrap); the five strategies — existing methods (LoRA, ZSCL, CPE-CLIP, replay) adapted by us to VoxTell, named after the mechanism actually evaluated; 30 runs; analysis scripts. Clear split between prior methods and own contribution (Q2).
3. **Answer per objective** (about 1.5 p.), one paragraph each, order 2, 3, 4, 1, matching 7.1:
   - Obj. 2: no strategy combined high Adaptation with retention; full-update strategies + prompt tuning end barely above the pretrained model and lose the control task; LoRA strategies retain more at about 0.23–0.25 lower Adaptation; replay best Final Performance (caveats).
   - Obj. 3: in few-shot only seq. FT learned; with 5 volumes it forgot less and kept the control task; volumes vs updates confounded.
   - Obj. 4: order strongly affects shared LoRA only; rank trades adaptation for retention (α fixed); replay.
   - Obj. 1: protocol separates adaptation, forgetting and loss of pretrained ability; control task and reference row changed how results read.
4. **Common factor and main limitations** (about 0.5 p.): adapter-from-zero hypothesis (untested), one budget for all strategies, one run per configuration, narrow scope.
5. **Future work** (about 0.5 p.): from 7.4, in the author's priority order (Q3).

Contributions: provisional until the author finalises them (CLAUDE.md); the Summary uses the same wording as Ch. 1.4 once final.

## Interview questions (block the draft)
Q1 **Most important result.** Which one or two results should the Summary lead with? Suggestion: (a) the all-or-nothing trade-off incl. prompt tuning forgetting despite a frozen backbone; (b) in few-shot only sequential fine-tuning learned.
Q2 **Own work.** What exactly do you claim as yours? Suggestion: the protocol and its control task; adapting ZSCL, CPE-CLIP and LoRA to a free-text promptable 3D model; the experiments and their analysis. The strategies themselves are prior work. Anything else (e.g. the code pipeline, the patellar diagnosis)?
Q3 **Future work priority.** 7.4 lists: test of the training-budget hypothesis, seeds and support-set draws, rephrased text prompts, more task orders, other models. Keep this order or change it?
Q4 **Practical message.** Should the Summary end with a recommendation for someone adapting such a model (e.g. "use task-specific LoRA if the set of structures is closed, otherwise shared LoRA with replay, and budget enough updates"), or stay with the results only?
