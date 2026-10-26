# Rerun results overview (2026-10-26)

Facts only, for the author's interpretation. Source: `thesis/tables/cl_metrics.csv` (point estimate, 95 % bootstrap interval over test volumes) and `thesis/tables/cl_differences.csv` (paired differences A − B). One seed per configuration; intervals reflect test-volume sampling only. "last" = main evaluation, parameters after the last epoch; "best-val" = checkpoint with the lowest validation loss.

## 1. Main comparison (full data, original order)

| Run | Adaptation | Final Forgetting | Control-task drop | Final Performance | Transfer |
|---|---|---|---|---|---|
| Pretrained model | 0.114 | 0.000 | 0.000 | 0.114 | 0.137 |
| Seq. fine-tuning, last (rerun) | 0.781 [0.76, 0.80] | 0.782 [0.76, 0.80] | 0.979 | 0.130 | 0.001 |
| Seq. fine-tuning, best-val (rerun) | 0.723 | 0.712 | 0.979 | 0.130 | 0.001 |
| Seq. fine-tuning, best-val (old run) | 0.717 | 0.704 | 0.979 | 0.130 | 0.001 |
| Task-specific LoRA r = 4 | 0.485 | 0.000 | 0.000 | 0.485 | 0.129 |
| Shared LoRA r = 1024 | 0.471 | 0.289 | 0.237 | 0.233 | 0.174 |
| Shared LoRA + replay, no control volumes (rerun) | 0.472 | 0.046 | 0.138 [0.12, 0.16] | 0.450 | 0.175 |
| Shared LoRA + replay, with control volumes (old) | 0.429 | 0.039 | 0.007 | 0.446 | 0.148 |
| Distillation-based, last (rerun) | 0.747 | 0.734 | 0.979 | 0.135 | 0.002 |
| Distillation-based, best-val (rerun) | 0.745 | 0.732 | 0.979 | 0.135 | 0.002 |
| Distillation-based, weight ensemble (rerun) | 0.376 | 0.354 | 0.979 | 0.124 | 0.007 |
| Prompt tuning, scaling active, last (rerun) | 0.580 | 0.510 | 0.865 [0.84, 0.88] | 0.155 | 0.043 |
| Prompt tuning, scaling active, best-val (rerun) | 0.576 | 0.505 | 0.863 | 0.155 | 0.039 |
| Prompt tuning, scaling inactive, best-val (old) | 0.608 | 0.568 | 0.979 | 0.135 | 0.043 |
| Joint fine-tuning (upper reference) | – | – | 0.979 | 0.852 [0.84, 0.87] | – |

Paired differences:
- Replay − shared LoRA: control-task drop −0.100 [−0.103, −0.096]; Final Forgetting −0.243 [−0.259, −0.226]
- Replay − task-specific LoRA: Final Performance −0.034 [−0.059, −0.011]
- Distillation − seq. fine-tuning (both last): Adaptation −0.035 [−0.041, −0.027]; Final Forgetting −0.048 [−0.055, −0.039]
- Prompt tuning scaled (last) − unscaled (old, best-val): Adaptation −0.029; Final Forgetting −0.058 [−0.069, −0.048]; control-task drop −0.115 [−0.137, −0.098]. Mixed checkpoints: the like-for-like comparison is scaled best-val (0.576 / 0.505 / 0.863) vs unscaled best-val.
- Joint full − task-specific LoRA: Final Performance +0.367 [+0.345, +0.389]

## 2. Task order (sequential fine-tuning, last epoch)
Reverse − original: Adaptation +0.003 [−0.005, +0.010]; Final Forgetting −0.002 [−0.009, +0.005].

## 3. Few-shot, k = 5 / 10 / 20 (10 epochs)

| Run | k = 5 | k = 10 | k = 20 | full (108) |
|---|---|---|---|---|
| Seq. FT Adaptation | 0.545 | 0.616 | 0.616 | 0.781 |
| Seq. FT Final Forgetting | 0.382 | 0.522 | 0.573 | 0.782 |
| Seq. FT control-task drop | 0.010 | 0.305 | 0.979 | 0.979 |
| Task-specific LoRA Adaptation | 0.114 | 0.115 | 0.116 | 0.485 |
| Shared LoRA Adaptation | 0.115 | 0.116 | 0.140 | 0.471 |
| Joint Final Performance | 0.600 | 0.585 | 0.753 | 0.852 |
| Joint control-task drop | 0.733 | 0.894 | 0.979 | 0.979 |

Joint k = 10 − k = 5: Final Performance −0.014 [−0.037, +0.013].

## 4. Equal updates (k = 5, 216 epochs = 1,080 updates per task, as with full data)

| Run | Adaptation | Final Forgetting | Control-task drop | Final Performance |
|---|---|---|---|---|
| Seq. FT k = 5 (50 updates) | 0.545 | 0.382 | 0.010 | 0.227 |
| Seq. FT k = 5, equal updates | 0.712 | 0.714 | 0.979 | 0.117 |
| Task-specific LoRA k = 5 | 0.114 | 0.000 | 0.000 | 0.114 |
| Task-specific LoRA k = 5, equal updates | 0.429 | 0.000 | 0.000 | 0.429 |
| Shared LoRA k = 5 | 0.115 | 0.000 | −0.001 | 0.115 |
| Shared LoRA k = 5, equal updates | 0.438 | 0.296 | 0.334 | 0.192 |

Paired: equal updates − 50 updates, Adaptation: task-specific LoRA +0.315 [+0.293, +0.334]; shared LoRA +0.323 [+0.306, +0.341]; seq. FT +0.167 [+0.142, +0.190]. Task-specific LoRA k = 5 equal updates − full data: −0.056 [−0.073, −0.040].

## 5. Reproducibility notes (thesis_notes.md §2)
Runs resumed inside a task are not bit-reproducible; reruns without such a resume reproduce the old runs exactly.
