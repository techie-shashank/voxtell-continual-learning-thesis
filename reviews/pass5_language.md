# Pass 5 — Language and style (2026-11-12)

Report-only subagent pass (fresh agent, restarted in a new session). No files edited by the agent. Saved by the main session. Mechanical lint and proofread items not repeated.

## A. Must fix
1. **experiment_results.tex:628**: "The SKM-TEA files store no orientation" contradicts data_description.tex:125, 132 (*our* NIfTI files have no orientation; the annotation files record it, 18 of 155 scans flipped). Wrong wording.
2. **method.tex:102**: "Because the order of the columns matters for some metrics, we compute this reference once for each task order." For the pretrained reference all columns are identical; what changes with task order is the order of the *rows* (e.g. Transfer). Wrong or unclear.
3. **method.tex:387**: "…smaller than ZSCL's interval of 100, for which ZSCL reports only slight changes between intervals of 1, 10, and 100." "for which" attaches to "interval of 100" but refers to the interval in general. Tier-1 referent.
4. **experiment_results.tex:335**: "The control task was lost gradually with k = 10 (control-task drop: 0.305)". A drop of 0.305 is not a lost control task.
5. **introduction.tex:188**: contribution 3, "…with three of the strategies and joint fine-tuning, which separates fewer volumes from fewer updates…": which-clause follows "joint fine-tuning" but refers to the analysis. Tier-1 referent / voice-sheet rule 6.
6. **summary.tex:57**: "The number of updates rather than the number of volumes was therefore the main reason…" stronger than Ch. 6 ("consistent with an effect of the number of updates", l. 370; "explains most", l. 350).
7. **related_work.tex:266**: "VoxTell's zero-shot results … show that *their* zero-shot generalisation does not extend to the knee structures" generalises to SAT without a SAT knee result. Overclaim.

## B. Unclear or hard-to-follow sentences
8. **method.tex:338**: elided verb in "and the meta-net the query" — garden path. (should fix)
9. **method.tex:341**: two stacked reasons ("As CPE-CLIP scales …, we scale …, since the meta-net holds …"); unclear which carries the decision. (should fix)
10. **method.tex:204**: inserted condition "so with the pretraining learning rate, each of our updates rests on one patch instead of 128 …" makes the causal chain hard to follow. (should fix)
11. **method.tex:280**: Final Forgetting condition for task-specific LoRA is dense; reason after a long condition. (should fix)
12. **experiment_results.tex:69**: "We train each task for E = 10 epochs so that 12 of the 17 runs … fit into one such job." Purpose reads oddly (why 12 of 17?); present tense clashes with past-tense setup. (should fix)
13. **experiment_results.tex:567**: 60+ words, colon, three-part list of confounds. (should fix)
14. **experiment_results.tex:571**: "…learned nothing on patellar cartilage at any rank tested, as in the few-shot settings": attachment of "as in…" ambiguous. (should fix)
15. **experiment_results.tex:575–576**: link between "trained with SGD" and the Hu et al. quote about Adam and α left implicit; the γ_r sentence doesn't say how it belongs to the second explanation. (should fix)
16. **background.tex:311**: "…also counts gains that a task made while later tasks were trained and lost again by the end" hard to parse. (should fix)
17. **background.tex:285** (Fig. 3.2 caption): "…namely their maximum for Final Forgetting…": referent of "their" and meaning of "namely" unclear. (should fix)
18. **experiment_results.tex:196**: "this loss began right after training" — after training on femoral cartilage or after the next task? (should fix)
19. **related_work.tex:39**: two which-clauses and an apposition in one sentence. (should fix)
20. **experiment_results.tex:292**: "…well before epoch 50, after which the run was evaluated": referent of "after which" unclear. (minor)
21. **background.tex:79**: "two linear layers with a nonlinearity between them that are applied…": "that" ambiguous. (minor)
22. **experiment_results.tex:609–615**: "two further limits" announced, but the first has four sub-points before "The second limit…". (minor)
23. **summary.tex:99**: "C²GR replays generated samples …, but trains its generative model on the data of each task": point of the contrast implicit. (minor)

## C. Tier-1 violations (other)
24. **introduction.tex:96**: "Existing continual-learning results do not show…" general claim without condition ("in the works we found"). (should fix)
25. **experiment_results.tex:329**: "with fewer volumes it forgot less": condition "with ten epochs per task" missing at first statement. (should fix)
26. **method.tex:291**: "Keeping such entries conflicts with storage limits and privacy constraints" categorical; needs condition or "can conflict". (should fix)
27. **summary.tex:49**: "Task-specific LoRA (r = 4) forgot nothing by construction" stronger than Ch. 5/6 ("near zero", can be positive, method.tex:280–281). (should fix)
28. **summary.tex:60**: "…reached 0.839 with 50 epochs, although its learning rate then also decayed more slowly." "Although" wrong connective for a confound. (should fix)
29. **experiment_results.tex:252**: "It is the only strategy that uses the task identity" — terminology says "beyond the text prompt" (as method.tex:272). (minor)
30. **appendix.tex:101, 103**: "The weight ensemble … halved the Adaptation of the student" imprecise (the ensemble's own Adaptation is half); "The ensemble learned less of each task" treats a weight average as a learner. (should fix)
31. **method.tex:256**: "rsLoRA showed that α/r slows learning at high ranks" names a method as actor; background.tex:192 describes the same result differently ("collapse", "learn no better"). Make them agree. (minor)

## D. Overclaiming or tone
32. **experiment_results.tex:183**: "Replay thus lowered this loss" — causal from one pair of runs, four control volumes, no paired interval in the text. (should fix)
33. **experiment_results.tex:473**: "The two runs therefore show how much a single run varies with its initialisation" — two runs give one instance, not the size of the variation. (should fix)
34. **experiment_results.tex:643**: "has also been reported in another setting and may therefore hold more generally" — one study is thin support; l. 645 partly takes it back. (minor)
35. **experiment_results.tex:213**: "These gaps show how far all strategies remain from…" summarising moral sentence. (minor)
36. "significant" used once, correctly (experiment_results.tex:117).

## E. Repetition
37. **introduction.tex:45 and 47**: "measured within these structures" / "These values are measured within the segmented structures" back to back. (should fix)
38. **experiment_results.tex:245–253 vs 146–158, 206**: Sec. 6.2 conclusion restates the results paragraph (control task lost incl. joint FT, l. 150–151 → 246; prompt tuning lost the control task despite frozen weights, l. 158 → 247; task-specific LoRA keeps tasks by construction, l. 154 → 250; highest Final Performance, l. 206 → 251). Should conclude rather than repeat. (should fix)
39. **experiment_results.tex:350 and 367**: "the number of updates explains most of the failure" twice in one section. (minor)
40. **method.tex:155 and 209**: same point twice in Sec. 5.2 (shared settings). (minor)
41. **related_work.tex:122, 227, 278**: three "our control task follows…" remarks; keep one in the gap section. (minor)
42. **experiment_results.tex:501–504 vs 528–529**: first task learned poorly repeated in the conclusion; could be a half-sentence. (minor)

## F. Sections whose voice or quality differs
43. **related_work.tex:132–142 and 250–256**: one method per sentence with numbers, no comparison until the last sentence; more catalogue-like than the rest of Ch. 2. (should fix)
44. **method.tex:224–232** (Sec. 5.3 opening): formulaic "X represents family Y"; survey referred to four times in six sentences. (should fix)
45. **experiment_results.tex:107–117** (paired bootstrap): densest, most procedural paragraph; meta-statements in four consecutive sentences. (minor)
46. **experiment_results.tex:508–511**: eight loss values in three sentences; log-like. (minor)
47. **experiment_results.tex:560–618** (Sec. 6.8): counting framework used repeatedly ("Three limitations…", "First/Second/Third", "two further limits", "Three further threats", "Finally"); more formulaic than the voice sheet. (minor)
48. **Chapter openings** (background:15, data_description:15, method:15, experiment_results:15, appendix:11): all "This chapter/appendix describes/introduces/reports…". Acceptable but uniform. (minor)
49. **Tense in Ch. 6**: Sec. 6.2 past ("reached", "fell"), Sec. 6.5 present ("Adaptation falls from 0.607…", l. 400, 413). (minor)

## G. Grammar, punctuation, terminology
50. **method.tex:191**: bare "prompts" in "we add no prompts of absent structures" → "text prompts" (lint missed it). (should fix)
51. **appendix.tex:12**: list breaks parallelism ("…\cref{sec:exp-components} analyses…"). (minor)
52. **summary.tex:38, introduction.tex:118**: "few-shot conditions" vs decision 2026-11-12 "few-shot settings" for k = 5, 10, 20 (RQ itself may keep "conditions"). (minor)
53. **related_work.tex:155**: "prompt-learning methods" next to "prompt-tuning strategy"; check consistency in Ch. 2. (minor)
54. **related_work.tex:166**: "the methods for vision–language models, which classify images or generate text" — the models classify; paragraph opens with "Unlike…" (back-reference opening rule); same at l. 281. (minor)
55. **background.tex:192–193**: tense mix "Kalajdzievski showed…" / "The paper also proves…". (minor)
56. **summary.tex:16**: "…VoxTell still segments most structures poorly": "still" has no reference point. (minor)
57. **summary.tex:89**: "The main extension of this work is a strategy that…" — a goal stated as fact. (minor)
58. **data_description.tex:18**: opening promises "which properties of the data limit the conclusions"; no such section, points scattered (l. 50, 82, 112). (minor)
59. **method.tex:287**: replay cross-referenced to `sec:cl-vlm`, but Ch. 2 reviews replay of stored samples in `subsec:cl-medseg-net` (related_work.tex:111). (minor)
60. Serial comma, `--` ranges, ``'' quotes, -ise spelling, sentence-initial `\Cref` spot-checked by grep: no misses.

## Priorities
A1–A7 first (1, 2, 4, 30 misstate facts; 3, 5 referent errors; 6, 7 overclaim). Then Method strategies (8–11) and Sec. 6.8 (13–15). Then the Sec. 6.2 conclusion repetition (38) and the Sec. 5.3 opening (44).
