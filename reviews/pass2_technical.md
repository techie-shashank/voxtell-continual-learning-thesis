# Pass 2 — Technical correctness and traceability (2026-11-12)

Report-only subagent pass (fresh agent, restarted in a new session). No files edited by the agent. Saved by the main session.

**Scope checked:** `thesis/method.tex` against `code/` at e5df182 (trainer, optimizer, losses, dataset/datamodule, base strategy, LoRA, CPE-CLIP, ZSCL, evaluation); `background.tex` Sec. 3.4 against `scripts/compute_cl_metrics.py`; configs of the main runs in `results/hpc/experiments/*/config.yaml`; `experiment_index.csv`; `thesis/tables/{cl_metrics,cl_differences,compute}.csv`; generated tables `ch6_hparams`, `ch6_strategy_params`, `ch6_compute`.

**Overall:** all metric equations match the reference implementation; all 40+ numbers checked trace to the CSVs; strategy descriptions match the code in substance. No must-fix errors.

## 1. Method vs code

| # | Location | Issue | Evidence | Severity |
|---|---|---|---|---|
| 1.1 | method.tex:217 | "The LoRA strategies store only the adapter after the last epoch" is not what the current code does: `Trainer.fit` writes `best_model.pt` (full state dict) whenever validation loss improves, for every strategy, including replay rerun `exp_20261023_014438_55e6abcf` (October code). The actual reason there is no best-validation evaluation for LoRA is that the LoRA configs define no `evaluation.extra`. Aug/Sep code may have differed (checkpoints not archived locally). Suggest "were evaluated only after the last epoch" unless the author confirms. | code/src/training/trainer.py:373-378; no `evaluation:` block in lora/shared/exp_20261023_014438_55e6abcf/config.yaml | should fix |
| 1.2 | method.tex:155-158, Alg. 2 | "differ only in three of its steps and in a factor on the gradient" omits (a) the distillation-based strategy's per-iteration weight-ensemble hook and (b) prompt tuning keeping VoxTell in eval mode, so prompt-decoder dropout (0.1) is off, whereas it is active (`model.train()`) for seq. FT, distillation and LoRA. Undocumented training difference; "same settings" (l. 155) not exact. | cpe_clip/model.py:89-92; base.py:354-356; zscl/strategy.py:152-177; thesis_notes §2 | should fix |
| 1.3 | method.tex:177, 213; Sec. 5.4 l. 408 | Validation "after every epoch" / "E·\|D_val\| validation passes for every strategy"; equal-updates runs validate every 24 epochs plus the last. Stated only in tab:app-hparams. | trainer.py:334; `validation_interval: 24` (exp_20261023_200332_9840ab20 etc.) | minor |
| 1.4 | method.tex:411 vs experiment_results.tex:549 | Sec. 5.4 names the teacher forward pass as "the only large addition" of distillation; Ch. 6 explains its cost by moving the 440 M teacher between CPU and GPU every iteration and the ensemble on GPU (ensemble also copies the full state dict 10× per epoch). Make consistent. l. 420 names only the ensemble for the highest memory, but the teacher is on GPU every step too. | zscl/strategy.py:141-144, 168-176 | should fix |
| 1.5 | method.tex:69-71, Alg. 1 | Select for task-specific LoRA at j = 0 ("adapter chosen by the task identity") undefined: no adapter yet; the pretrained model is evaluated. Wording only. | lora/task_specific/strategy.py:52-66 | minor |
| 1.6 | Alg. 2 l. 175 | ξ is a gradient hook, so SGD's weight-decay term is not scaled. "SGD step on ξ∇L with weight decay ω" is correct only if read that way. | cpe_clip/transformer.py:83-91 | minor |

**Verified correct:** batch 1 and one patch per volume per epoch with shuffle (datamodule.py:129); π_fg = 0.85 train and val (dataset.py:45, 80-98); validation RNG re-seeded per task (dataset.py:51, trainer.py:265); BCE + MONAI soft Dice 1:1 (losses.py:93-111); SGD Nesterov μ 0.99, ω 3e-5, η₀ 1e-4, linear per-iteration decay restarted per task (optimizer.py, trainer.py:276); evaluation after last epoch; replay `max(1, round(ρN))`, empty start under `include_retention_tasks: false`, cap 200, per-sample prompts (base.py:123-176); task-specific LoRA rebuilt from θ₀ every task, control task without adapter (task_specific/strategy.py:17-22, 54-61); shared LoRA one adapter; LoRA on q and v of `multihead_attn` only; tokens appended to memory with zero positional encoding, Xavier init, "replacement", shared meta-net 2d→2048→d with GELU on [q; mean memory], ξ = max(0.25, 1/t) on tokens and meta-net (`scale_meta_net: true`, exp_20261022_180923_7bcbb6cc); KD = KL(teacher‖student), softmax over 12³ voxels per L2-normalised guidance vector, `batchmean` = sum for B = 1 (matches Eq. method-kd); weight-ensemble running mean per epoch, never reset (matches Eq. bg-we); joint = 6×108×10 = 6,480 updates, same as seq. FT.

## 2. Metric equations vs `scripts/compute_cl_metrics.py`

All match: Adaptation (l. 116), Final Forgetting (max over j = 1..T−1, i = 1..T−1, l. 123-124), Final Performance (l. 118), Transfer (inner mean j = 1..i−1, outer i = 2..T, l. 125-126), control drop c₀ − c_T (l. 156). Same index convention (row = task, column = stage). Pretrained reference row correct (method.tex:100).

- DSC (bg-dsc, background.tex:256) leaves empty prediction + empty label undefined; code uses MONAI `ignore_empty=False` (returns 1, evaluation/test.py:36). Never occurs on the test sets. **minor** (footnote would close it).

## 3. Reproducibility (configs vs thesis)

Stated and matching configs: η₀, μ, ω, schedule, E = 10/216, batch 1, patch 192³, π_fg, loss, deep supervision off, no augmentation, seeds 42/42, split 70/15/15, k and nested first-k sets, ranks, α, γ_r, LoRA dropout, q/v, ρ, M_max, m, L_p, 0.25 floor, λ = 0.01, I_we = 10, text prompts, checkpoint v1.1, Qwen3-Embedding-4B, software versions.

| # | Item | Severity |
|---|---|---|
| 3.1 | Instruction prefix prepended to every text prompt before Qwen3 embedding ("Instruct: Given an anatomical term query …\nQuery: <prompt>", code/src/utils/text_embedding.py:14-20) not stated. Part of the released VoxTell pipeline, but changes the embedding. | should fix |
| 3.2 | Prompt-decoder dropout (0.1, active except in prompt tuning, see 1.2) and LoRA attention dropout 0 not in the parameter tables. | should fix |
| 3.3 | Early stopping disabled (trainer.py:53-56), `use_deterministic_algorithms: true` with warn_only, and `cudnn.benchmark = True` at evaluation (predictor.py:64, reproducible to ~1e-5) not listed. | minor |
| 3.4 | Validation set of joint fine-tuning = union of the six validation sets (138 samples), used for its best-validation checkpoint. Not stated. | minor |
| 3.5 | App. A l. 48-50: "In five runs … training was continued inside a task … drew samples and patches in a different order." joint_ft (SLURM 1850677) resumed after the last batch of epoch 10, so no training followed; only its epoch-10 validation is missing (thesis_notes §2). Statement does not hold for that run. | minor |
| 3.6 | 23 earlier runs without per-run code commit acknowledged (App. A l. 44-45). OK. | — |

## 4. Algorithms: pseudocode, complexity, measured cost

- Pseudocode for the protocol (Alg. 1) and Adapt (Alg. 2). Replay memory, Select and the ensemble update in prose/equations only; acceptable (see 1.2).
- **Time and memory complexity (should fix):** Sec. 5.4 gives complexity in words ("linear in epochs and samples", "evaluation grows quadratically with the number of tasks") and one exact count (1,036 inferences = 7·(6·24+4), correct). No asymptotic expressions per strategy: LoRA per-iteration cost (forming BA is O(d²r) per adapted projection, layers.py:73-110), memory in terms of |θ|, |φ| and activations, storage of task-specific LoRA O(T·4L_dec·d·r). The chair asks for time and memory complexity per algorithm; a short line of O(·) terms per strategy would make it explicit.
- Measured runtime, memory, hardware given (tab:ch6_compute, A100-SXM4-40GB) and match compute.csv (seq. FT 26.8 min / 31.4 GiB; distillation 37.1 min / 37.9 GiB; task-specific LoRA 18.1 min / 20.3 GiB; replay 26.4 min). Caveat: LoRA rows from Aug/Sep runs, others from October reruns, possibly different code and package versions — **minor**, one clause in the caption.

## 5. Spot-checked numbers (vs `cl_metrics.csv` / `cl_differences.csv` unless noted)

| Location | Number | Source | Verdict |
|---|---|---|---|
| exp:149 | Seq. FT Adapt 0.781, FF 0.782 | a9f4ca56 | ✓ |
| exp:149 | Distillation 0.747 / 0.734 | 65011743 | ✓ |
| exp:153-155 | LoRA Adapt 0.485/0.471/0.472; replay FF 0.289→0.046, control 0.237→0.138 | 668e608d, 90e8b4e6, 55e6abcf | ✓ |
| exp:156 | replay ΔAdapt 0.001 [−0.002, 0.004] | cl_differences (sign flipped) | ✓ |
| exp:157-158 | prompt tuning 0.580 / 0.510 / 0.865 | 7bcbb6cc | ✓ |
| exp:163 | distillation − seq. FT: FF −0.048 [0.039, 0.055], Adapt −0.035, FP +0.005 [0.001, 0.009] | cl_differences | ✓ (0.0345 → 0.035) |
| exp:211-212 | joint 0.852; gaps 0.367, 0.722 | 6a6e9cb5 | ✓ |
| exp:217 | Transfer 0.129/0.174/0.175/0.137; 0.001/0.002/0.043 | cl_metrics | ✓ |
| exp:231 | best-val seq. FT Adapt −0.059, FF −0.070 | cl_metrics | ✓ |
| exp:330-335 | k = 5 seq. FT 0.545 / 0.382 / 0.010 / FP 0.227; k = 10 control 0.305 | a67fb8c9, f041f82f | ✓ |
| exp:351 | equal updates 0.429 (−0.056 [0.040, 0.073]), 0.438 (−0.032 [0.025, 0.039]) | cl_differences | ✓ |
| exp:354 | FF 0.296, [−0.007, 0.018], control +0.097 | cl_differences | ✓ |
| exp:360-362 | 0.373; 0.170; control 0.733→0.979 | cl_metrics, cl_differences | ✓ |
| exp:400-402 | rank: Adapt 0.607→0.462, FF 0.546→0.284, control 0.978→0.091, FP 0.230 at r = 512, Transfer 0.045→0.170 | rank runs | ✓ |
| exp:433 | 50.3 vs 100.7 M parameters | 49,152·r | ✓ |
| exp:462-464 | order effect seq. FT +0.003 / −0.002 / +0.004; Transfer 0.014 vs 0.001 | 2dba6ff1 vs a9f4ca56 | ✓ |
| exp:475 | TS-LoRA 0.485 vs 0.478 | cl_metrics | ✓ |
| exp:622 | best-val distillation forgets 0.021 more [0.012, 0.029] | cl_differences | ✓ |
| exp:69 | 12 of 17 full-split runs in one job | compute.csv | ✓ |
| exp:184 | 55 of 163 samples | 5·11 + 108 | ✓ |
| exp:31 | 38 runs | experiment_index | ✓ |
| App:101-102 | WE Adapt 0.376, FP −0.011 [0.007, 0.017], FF 0.354 | cl_differences | ✓ |
| App:113 | scaling FF −0.063, control −0.117, FP +0.020 [0.014, 0.025], Adapt −0.032 [0.025, 0.040] | cl_differences | ✓ |
| summary:22–74 | 0.114; 0.130/0.135; 0.485/0.781; 0.289→0.046; 0.852/0.485/0.450; 0.429/0.438; 0.839; 0.124/0.289; 0.832→0.091; 0.337→0.284 | cl_metrics | ✓ |
| intro:39-40 | 70.85 %, 10.72 % | paper values (thesis_notes §1, §2) | ✓ |

No mismatches.

## 6. Claims vs evidence; variability

Variability reported well: every caption says "one run each"; bootstrap design and limits explained (exp:97-117); intervals not called significant; Sec. 6.8 covers single runs.

| # | Location | Issue | Severity |
|---|---|---|---|
| 6.1 | exp:285, 297; summary.tex:59 | "a four times larger rank … neither the rank … was the cause": with α = 16 fixed, r = 16 also halves γ_r (8 → 4), the confound stated for the rank experiment (exp:417-418). Sec. 6.8 l. 567 lists three confounded experiments but not this one. | should fix |
| 6.2 | summary.tex:57 | "The number of updates rather than the number of volumes was therefore the main reason …" is general; evidence is k = 5 only, one run per configuration, one support set. Should carry "at k = 5" (Ch. 6, exp:367, words it correctly). | should fix |
| 6.3 | exp:302 | "the Adaptation of task-specific LoRA is limited by the training length" contradicts the caveat at l. 298-301 (length and learning-rate decay not separated); "training length or schedule" would match. | minor |
| 6.4 | exp:183 | "Replay thus lowered this loss" is causal from one run per arm; hedged in the next sentences and 6.8 (l. 600). Acceptable. | minor |
| 6.5 | summary.tex:74-75 | "need not change together" rests on single runs with rank and γ_r confounded; wording weak enough. OK. | — |

**Severities:** must fix: none. Should fix: 1.1, 1.2, 1.4, 3.1, 3.2, 4 (O(·) complexity), 6.1, 6.2. Minor: 1.3, 1.5, 1.6, 2 (DSC empty case), 3.3–3.5, compute-table caveat, 6.3, 6.4.
