# Pass 7 — Examiner's view (2026-11-12)

Report-only subagent pass (fresh agent, restarted in a new session). No files edited by the agent. Saved by the main session.

Sources read: CLAUDE.md, FINAL_REVIEW.md, thesis_tracker.md (Sections A–C), thesis_notes.md §0–1, Ch. 1, 5, 6 and 7 (Summary) in full, the metrics in Ch. 3, the splits and preprocessing in Ch. 4, the gap section of Ch. 2, Appendix A, the generated tables (`ch6_main`, `ch6_few_shot`, `ch6_hparams`, `ch6_strategy_params`), `results/experiment_index.csv` (patellar runs) and `code/src/continual/strategies/zscl/strategy.py`. Line numbers refer to the files as of 2026-11-12.

## 1. Likely examiner questions, hardest first

**Q1. Is "LoRA adapts much less" a property of LoRA, or of a training setup that was never tuned for it?**
- Where: `experiment_results.tex:68-69` (E = 10 by the 24 h job limit); `method.tex:160,202-209` and `ch6_hparams` (SGD, η0 = 1e-4, Nesterov μ = 0.99, batch size 1, linear decay to zero per task); `experiment_results.tex:571-578`.
- Tracker: D16, D18, D66, D72. Adequate as statements of limitation; none gives the mechanism the author has to explain.
- A good answer: Hu et al. trained LoRA with Adam(W); with SGD, a learning rate chosen for full fine-tuning and B = 0, the first updates of A are zero and the updates of B are small. The patellar diagnosis raised the learning rate only 3× (3e-4). E was set by wall-clock time ("12 of the 17 runs fit one job"), not by convergence. The honest conclusion is the one in `summary.tex:90`: the thesis cannot separate strategy from configuration.

**Q2. Could your test volumes be part of VoxTell v1.1's training data?**
- Where: `experiment_results.tex:630-633`, `method.tex:39`.
- Tracker: only the Section C note (l. 178-179, "Contact the authors…"). **No D-ID and no prepared answer.**
- A good answer: issue #15 lists "Stanford Knee" among the v1.1 sources. The pretrained model scores 0.00 on five of six structures, which argues against training on these labels. But femoral cartilage scores 0.68 with v1.1 against 46.45 % for v1.0; that is *consistent with* exposure to SKM-TEA, so it must not be used as evidence against leakage. Whether the authors were contacted, and what it means for femoral Adaptation and Transfer.

**Q3. Is the poor pretrained baseline (0.114) caused by your preprocessing, not by missing knowledge?**
- Where: `data_description.tex:124-133` (identity affine, stored axis order, 18 of 155 scans with flipped left–right axis), `experiment_results.tex:628`.
- Tracker: D4, D6. Partly adequate: no cause claimed, but no check run.
- A good answer: the plan is noResampling, so only orientation differs. The motivation (VoxTell poor on the knee) uses v1.0 paper numbers, not v1.1. Inference on volumes reoriented to canonical orientation would test it (**new experiment**, inference only).

**Q4. Sequential fine-tuning loses the lung completely after the first task. Did the model learn to ignore the text prompt?**
- Where: `method.tex:191` (no prompts of absent structures, one prompt per stage), `experiment_results.tex:179,192-197`.
- Tracker: D17 inadequate ("may lower absolute performance").
- To know: VoxTell pretraining used two positive and one negative prompt per image (`paper_notes/voxtell.md:67`). Within one stage every sample carries the same prompt; joint fine-tuning and replay show a volume with several prompts. *Suggestion, not a result:* plausible shared reason for the collapse of sequential fine-tuning, the strength of joint fine-tuning and the effect of replay. Cheap test: score each prompt's prediction against the mask of the last-trained structure (**new analysis**, inference only).

**Q5. Task-specific LoRA gets a control-task drop of zero because the protocol knows "lung" is not a trained task. Isn't that an oracle?**
- Where: `method.tex:71,278-281`, `experiment_results.tex:250`.
- Tracker: D14 ("by construction"), D31/D43 (task identity). Routing of *unknown* prompts not covered.
- A good answer: in deployment an unseen prompt must be detected and sent to the model without an adapter, which needs a selector (the failure mode MoE-Adapters reports, `related_work.tex:141`). With one fixed prompt per task the prompt identifies the task, so task-specific LoRA is the natural task-incremental solution; the comparison is about what is possible with one parameter set.

**Q6. The research question says "under few-shot conditions", yet the main comparison uses 108 volumes, and two strategies never ran few-shot.**
- Where: `introduction.tex:114,156-157`, `experiment_results.tex:595-596`.
- Tracker: D46, adequate only with the real priority; the tracker warns against blaming compute (few-shot runs took 4.8–9.8 h).
- Note: `method.tex:160` justifies untuned settings with "the compute budget left no room", which clashes with how cheap the few-shot runs were.

**Q7. "Updates, not volumes, explain the LoRA failure." How strong is that?**
- Where: `experiment_results.tex:349-373`, `summary.tex:56-58`. Tracker: D9, D39, D8, adequate.
- State: one k (5), one nested draw, one run per configuration. In the equal-updates runs the learning rate also decays over 1,080 instead of 50 updates; a higher total learning rate is part of what "more updates" means here.

**Q8. Sequential and joint fine-tuning at k = 5 both make 300 updates, yet control-task drops are 0.010 and 0.733. Why?**
- Tracker: D65, oral answer prepared.
- Derive: with μ = 0.99 the momentum time constant is about 100 steps; optimiser and schedule restart every task (`method.tex:207`), so 6 × 50 updates never build momentum, 300 continuous updates do. Possible explanation only, untested.

**Q9. What do your intervals cover? Can small differences be trusted?**
- Tracker: D11, D35, D40, adequate.
- Key fact: the two task-specific LoRA runs differ only in adapter initialisation, yet the interval of their difference, [0.004, 0.008], excludes zero (`experiment_results.tex:473-478`).

**Q10. Joint fine-tuning also loses the lung completely. In what sense is it an "upper reference"?**
- Where: `method.tex:105-112`, `experiment_results.tex:151,211-213`. Tracker: D12, still "reruns" (outdated).
- A good answer: upper reference for Final Performance only, not for retention of pretrained ability; shows the control-task loss comes from full-parameter training on knee data, not from the sequence; explains why intransigence is not computed (`method.tex:111-112`).

**Q11. The ranks were chosen on test results. Isn't the comparison biased?**
- Tracker: D21, D37, adequate.
- Facts: the bias favours the two LoRA configurations. r = 1024 understates control-task retention of shared LoRA (0.237 against 0.091 at r = 2048).

**Q12. Why did distillation barely help? Is your loss really ZSCL's?**
- Where: `method.tex:358-369,380-383`, `experiment_results.tex:162-167,222-227`. Tracker: D25, D42, D47.
- Missing: the code (`zscl/strategy.py:89-117`) L2-normalises only the guidance vectors, not the stage-4 features, and uses **no temperature**.
- A good answer: λ = 0.01 vs ZSCL's 1, not tuned; current-task data instead of a reference dataset; no weight-consolidation loss; size of the distillation term never logged.

**Q13. Which checkpoint is "the" result? At the best-validation checkpoint, distillation forgets more than sequential fine-tuning.**
- Where: `experiment_results.tex:230-232,621-622`. Tracker: Section C l. 180, D15 (outdated, "reruns").
- A good answer: why the last epoch is the consistent rule (it is the model carried forward); validation used one patch per volume, so it is noisy.

**Q14. Why LoRA only on q and v of the prompt-decoder cross-attention, with the convolutional encoder and decoder frozen?**
- Where: `method.tex:261-264`; contrast `experiment_results.tex:368` (Silva-Rodríguez et al. applied LoRA in the *encoder*).
- Tracker: D22, D50 cover q vs v. **Placement in prompt decoder vs convolutional backbone not covered.**
- A good answer: what the guidance can and cannot change when image features are frozen.

**Q15. How can Final Forgetting (0.782) exceed Adaptation (0.781) for sequential fine-tuning?**
- Where: `ch6_main`, `background.tex:305-312`. Tracker: D30, D53, D68 cover the parts, not this number.
- Answer: Final Forgetting averages tasks 1..T−1, Adaptation tasks 1..T; its maximum also runs over stages before a task was trained.

**Q16. Why does Adaptation of shared LoRA fall with rank, against rsLoRA's finding?**
- Tracker: D20, D66, adequate. Know: γ_r goes from 16 to 0.71; most of the fall comes from the first task.

**Q17. Patellar diagnosis: does each run change one factor?**
- Where: `experiment_results.tex:269-270,285`. Tracker: D38, incomplete.
- Not stated: the r = 16 run kept α = 16 (`experiment_index.csv`, run 89e6de63), so γ_r fell from 8 to 4; the "four times larger rank" run also halved the scale.

**Q18. Replay lowered the control-task drop although the memory holds no lung samples. Why?**
- Where: `experiment_results.tex:181-186`. Tracker: D54 covers cost only.
- Answer: untested; arose in the last task only. See Q4 for the prompt-mixture idea.

**Q19. Is the control task (one structure, CT, 4 volumes, in v1.1's training data) a valid proxy for pretrained ability?** Tracker: D28, adequate.

**Q20. What is new? The methods exist; the protocol combines Chaudhry, ZSCL and SPU.** Tracker: D45, D51, adequate. Novelty lies in the setting and evaluation, not a method; state the search caveat (OpenAlex top-30 per query).

## 2. Weakest points

1. **Training budget set by the job limit; the headline LoRA result depends on it.** Must fix (caveat or defence). `experiment_results.tex:68-69`, `method.tex:160,209`. Conceded at `:577` and `summary.tex:90`, but Sec. 6.2 and the Summary still open with "LoRA adapted less" as a finding (`experiment_results.tex:152`, `summary.tex:37`). *Suggestion:* qualify once with "within ten epochs". Fixing the cause would need new experiments.
2. **Possible SKM-TEA exposure in v1.1.** Must fix (defence answer and tracker entry). `experiment_results.tex:632-633`. Stated, but the consequence for femoral cartilage (0.68, entering Adaptation, Transfer and every pretrained reference) is not discussed.
3. **Orientation of the SKM-TEA input never checked.** Should fix. `data_description.tex:124-133`, `experiment_results.tex:628`. Inference-only check would settle it (**new experiment**, small); otherwise keep the caveat.
4. **No negative prompts and one prompt per stage; prompt collapse never considered.** Should fix. `method.tex:191`. *Suggestion:* one sentence in Sec. 6.8 naming it as untested.
5. **Zero control-task drop of task-specific LoRA rests on oracle routing.** Should fix. `method.tex:278-281`. One clause: it needs knowledge that the prompt lies outside the sequence.
6. **Scope of the research question vs what was run.** Should fix (defence). `introduction.tex:114`, `method.tex:160`. "The compute budget left no room to tune" conflicts with cheap few-shot runs and D46's "time of the thesis"; align the reason.
7. **Checkpoint choice reverses a comparison.** Minor; stated at `experiment_results.tex:621-622`, but `:162` opens "forgot slightly less" as a result; keep the hedge "at the last epoch".
8. **Diagnosis and rank experiments change γ_r implicitly.** Minor. `experiment_results.tex:285` (r = 16 with α = 16 halves γ_r), not stated, unlike the rank experiment (`:417-418`).
9. **Distillation loss without temperature or feature normalisation.** Minor. `method.tex:358-364` vs code; the difference from ZSCL (normalised CLIP embeddings with a logit scale) is not named among the differences (`:366-367`).
10. **"Forgot nothing".** Minor. `summary.tex:49` "forgot nothing by construction" vs `method.tex:281` and Ch. 6 "near zero by construction". One wording.
11. **Joint fine-tuning non-monotonic in k.** Minor. Final Performance 0.600 at k = 5 and 0.585 at k = 10 (`ch6_few_shot`); `experiment_results.tex:359` ("between 0.585 and 0.753") hides this. Answer: single runs.
12. **Uncited counterfactual.** Minor. `introduction.tex:53`: "Retraining … would be expected to preserve most of what it could segment before" needs a citation or softer modal.
13. **Summary length.** Minor. Prose of `summary.tex` looks like about 2 pages vs 3–4 required; check in the PDF.
14. **Stale tracker statuses.** Housekeeping. D7, D9, D12, D15, D24, D25, D26, D39 still say "reruns"; several "Where" columns cite the old Ch. 7/8 (D41, D61, D62, D67). Add D-IDs for Q2, Q4, Q5, Q14, Q17.

## 3. What the author must study before the defence

- **SGD with momentum 0.99, batch size 1, schedule restarting every task** (`method.tex:202-207`, `ch6_hparams`): effective step size μ/(1−μ); why 50 updates per task barely move the model (D65, Q8); why the learning-rate decay over U = E·N_t makes "more updates" also mean "more total learning rate" (`experiment_results.tex:298-301`).
- **LoRA mechanics** (`background.tex:175-197`, `method.tex:250-258`): with B = 0 the gradient w.r.t. A is zero at the first step; α/√r vs α/r and what γ_r does to the step size under SGD vs Adam; why merging gives no inference cost; the plateau at the empty prediction (loss ≈ 1.0 is the Dice term of an empty prediction, BCE near zero, `experiment_results.tex:288-290`).
- **Metric definitions in edge cases** (`background.tex:293-345`): why Final Forgetting can exceed Adaptation; why the maximum includes stages before training (D53); why Transfer excludes stage 0; for task-specific LoRA, tasks with i > j are evaluated with the *current* task's adapter (`method.tex:278`), which drives its Transfer (0.129 vs 0.137 for the pretrained model).
- **What the bootstrap covers** (`experiment_results.tex:97-117`): paired resampling of the 24 volumes, shared across tasks and stages; the 4 AeroPath volumes resampled separately; no training randomness, no multiple-comparison correction.
- **Distillation loss as implemented** (`method.tex:355-369`; `zscl/strategy.py:89-127`): direction of the KL divergence; normalised guidance but unnormalised features, no temperature, `batchmean` with B = 1; where its gradient flows; difference from ZSCL's image–text distillation.
- **Weight ensemble** (`method.tex:386-393`, App. A.4): never reset, equal-weight mean over 100 snapshots per task, so later tasks are diluted (D70); difference from ZSCL's public code (D57).
- **Prompt tuning** (`method.tex:311-343`): why frozen weights still change every output (tokens in keys/values, meta-net on the query); the meta-net holds 12.59 M of the 12.60 M parameters; the 0.25 floor, active only in tasks 5 and 6 (D55).
- **VoxTell architecture as executed** (`method.tex:140-149`): keys and values from encoder stage 4 (12³ voxels), not the bottleneck as in the paper; self-attention never executed (440.0 M vs 339.3 M parameters); how guidance E_s is fused at five decoder stages (underlies Q14).
- **Scenario argument** (`method.tex:31-34`; D31): defend "closest to task-incremental" against "domain-incremental with a prompt input" using van de Ven's definitions.
- **Version facts:** v1.0 numbers in the paper vs our v1.1 checkpoint; sources v1.1 added (AeroPath, "Stanford Knee"); consequences for the control task and the test volumes (Q2).
