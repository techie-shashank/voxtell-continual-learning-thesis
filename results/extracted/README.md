# Extracted results: `few_shot_cl_results_fixed.xlsx`

Machine-readable copy of every table in `results/few_shot_cl_results_fixed.xlsx`.
Nothing here was rounded, converted or recomputed.

| | |
|---|---|
| Source file | `results/few_shot_cl_results_fixed.xlsx` |
| Source SHA-256 | `a697b6fa3c51bf28505f3e69eebb9458cb6e259e11395033404086e89b2a803e` |
| Extracted on | 2026-10-17 |
| Script | `scripts/extract_results_xlsx.py` (Python standard library only) |
| Regenerate | `python scripts/extract_results_xlsx.py` (from the repository root) |

If the workbook changes, its SHA-256 changes. Rerun the script and update the hash above.

## Conventions

- **Values are the strings stored in the xlsx XML.** Excel stores numbers as IEEE doubles with up to 17 significant digits. For example, `0.70399999999999996` is how Excel stores a typed `0.704`, and `1E-3` is a typed `0.001`. Parse them as floats; do not compare them as text with rounded values.
- **Formula cells hold Excel's last cached result.** The formulas themselves are listed in `all_cells.csv` and summarised below.
- `#DIV/0!` is copied as is. Empty cells are empty strings.
- The header cell above the row labels is empty in the workbook and is named `row_label` in the CSVs.
- Columns that are completely empty within a table are dropped. This only affects `til_lora__rank4_only_patellar.csv`.
- Table titles (merged title rows in the workbook) are not inside the CSVs. They are in `index.csv`, column `table_title`.

## Files

| File | Content |
|---|---|
| `index.csv` | One row per table CSV: file, sheet, sheet visibility, cell range in the workbook, table title |
| `all_cells.csv` | Every non-empty cell of the workbook: sheet, cell, xlsx type (`n` number, `s` string, `str` formula string, `e` error), stored value, formula. Use it to trace any number to its cell |
| `dashboard.csv` | Sheet `Dashboard`, `A1:K27` |
| 35 block CSVs | One per evaluation-matrix block, listed below |

### Layout of an evaluation-matrix block

Rows are the evaluated structures in task order, followed by the retention row `aeropath (Retention)` and an `Average` row.
The columns are:

- `Pretrained`: the model before any continual training.
- One column per training stage, in task order. The header names the task trained in that stage, so the diagonal is the performance on a task right after training on it.
- The metric columns `Average Performance`, `Final Performance`, `Final Forgetting`, `Transfer` and `Final Retention Drop`.

The workbook does not state the metric of the matrix entries. The slides (slide 15 and the heatmap captions) call it the Dice coefficient.
Note that the slides draw the transposed matrix: trained tasks are the rows there.

### Spreadsheet metric formulas (standard 6-task block)

Notation: the block's first data row is row r₀. Columns `C`…`H` are stages 1…6 (task order). `B` is `Pretrained`. Formulas are quoted verbatim for the first block of each sheet; all other blocks use the same pattern (checked automatically for every block).

| Column | Row | Formula (first block, rows 3–10) | In words |
|---|---|---|---|
| `Average Performance` (I) | task rows | `AVERAGE(C3:H3)` | mean over all 6 stages of the performance on that task, including stages before the task was trained |
| `Final Forgetting` (K) | task rows 1–5 | `MAX(C3-H3, D3-H3, E3-H3, F3-H3, G3-H3)` | largest drop from any of stages 1–5 to the final stage. The max runs over all of stages 1–5, including stages before the task was trained |
| `Transfer` (L) | task rows 2–6 | row 4: `C4`; row 5: `AVERAGE(C5,D5)`; … row 8: `AVERAGE(C8,D8,E8,F8,G8)` | mean performance on a task over the stages before it is trained. No reference value (e.g. `Pretrained`) is subtracted |
| `Final Retention Drop` (M) | retention row | `(B9-H9)/B9` | relative drop on AeroPath from the pretrained model to the final stage |
| `Average Performance` (I) | `Average` | `AVERAGE(I3:I8)` | mean over the 6 tasks |
| `Final Performance` (J) | `Average` | `AVERAGE(H3:H8)` | mean over the 6 tasks at the final stage |
| `Final Forgetting` (K) | `Average` | `AVERAGE(K3:K7)` | mean over tasks 1–5 (last task excluded) |
| `Transfer` (L) | `Average` | `AVERAGE(L3:L9)` | mean over tasks 2–6 (L3 and L9 are empty and ignored by `AVERAGE`) |

Deviations from this pattern:
- **CIL-LoRA sheet:** in 12 of the 14 blocks, `(B-H)/B` is also filled into every task row. This gives `#DIV/0!` where `Pretrained` is 0, and a value for Femoral. Exceptions are `A34` (rank 128 + replay) and `A67` (rank 32), which only have the retention-row formula.
- **Sheet `TIL-LoRA (isolated)`** (hidden): 5 tasks, so the columns are shifted by one. Its retention formula is `AVERAGE(B9-G9)`, an *absolute* drop, not the relative `(B-G)/B`.
- **`til_lora__rank4_only_patellar.csv`**: one task only. The formulas are `I36 = AVERAGE(C36)`, `I38 = AVERAGE(I36:I36)`, `J38 = AVERAGE(C36)`, and `M37 = (B37-C37)/B37`.

The code (`code/src/continual/metrics.py`) computes these metrics with different formulas. Per the author's decision, the spreadsheet formulas take priority. The definition of the retention drop is still open.

### Block files

| File | Sheet (state) | Range | Title in workbook | Dashboard row |
|---|---|---|---|---|
| `zscl__original.csv` | ZSCL | A2:M10 | ZSCL (Task Order=Original) | 6 |
| `cil_lora__rank4_original.csv` | CIL-LoRA | A46:M54 | CIL-LoRA (Rank=4, Task Order=Original) | 7 |
| `cil_lora__rank32_original.csv` | CIL-LoRA | A68:M76 | CIL-LoRA (Rank=32, Task Order=Original) | 8 |
| `cil_lora__rank128_original.csv` | CIL-LoRA | A2:M10 | CIL-LoRA (Rank=128, Task Order=Original) | 9 |
| `cil_lora__rank256_original.csv` | CIL-LoRA | A13:M21 | CIL-LoRA (Rank=256, Task Order=Original) | 10 |
| `cil_lora__rank512_original.csv` | CIL-LoRA | A57:M65 | CIL-LoRA (Rank=512, Task Order=Original) | 11 (see flag 3) |
| `cil_lora__rank1024_original.csv` | CIL-LoRA | A79:M87 | CIL-LoRA (Rank=1024, Task Order=Original) | 4, 12 |
| `cil_lora__rank2048_original.csv` | CIL-LoRA | A90:M98 | CIL-LoRA (Rank=2048, Task Order=Original) | 13 |
| `cil_lora__rank256_reverse.csv` | CIL-LoRA | A24:M32 | CIL-LoRA (Rank=256, Task Order=Reverse) | — |
| `cil_lora__rank1024_reverse.csv` | CIL-LoRA | A134:M142 | CIL-LoRA (Rank=1024, Task Order=Reverse) | 14 |
| `cil_lora__rank128_original_replay0.1.csv` | CIL-LoRA | A35:M43 | CIL-LoRA (Rank=128, Task Order=Original, replay_fraction=0.1) | — |
| `cil_lora__rank1024_original_replay0.1.csv` | CIL-LoRA | A145:M153 | CIL-LoRA (Rank=1024, Task Order=Original, replay_fraction=0.1) | 27 (see flag 5) |
| `cil_lora__rank1024_original_5shot.csv` | CIL-LoRA | A101:M109 | CIL-LoRA (Rank=1024, Task Order=Original, 5-shot) | 20 |
| `cil_lora__rank1024_original_10shot.csv` | CIL-LoRA | A112:M120 | CIL-LoRA (Rank=1024, Task Order=Original, 10-shot) | 23 |
| `cil_lora__rank1024_original_20shot.csv` | CIL-LoRA | A123:M131 | CIL-LoRA (Rank=1024, Task Order=Original, 20-shot) | 26 |
| `til_lora__rank4_original.csv` | TIL-LoRA | A2:M10 | TIL-LoRA (Rank=4, Task Order=Original) | 3 |
| `til_lora__rank4_reverse.csv` | TIL-LoRA | A13:M21 | TIL-LoRA (Rank=4, Task Order=Reverse) | 15 |
| `til_lora__rank8_original.csv` | TIL-LoRA | A24:M32 | TIL-LoRA (Rank=8, Task Order=Original) | — |
| `til_lora__rank8_original__duplicate_A40.csv` | TIL-LoRA | A41:M49 | TIL-LoRA (Rank=8, Task Order=Original) | — (see flag 8) |
| `til_lora__rank4_only_patellar.csv` | TIL-LoRA | A35:M38 | TIL-LoRA (Rank=4, Task Order=Only Patellar) | 17 (see flag 4) |
| `til_lora__rank4_original_5shot.csv` | TIL-LoRA | A63:M71 | 5-shot TIL-LoRA (Rank=4, Task Order=Original) | 19 |
| `til_lora__rank4_original_10shot.csv` | TIL-LoRA | A52:M60 | 10-shot TIL-LoRA (Rank=4, Task Order=Original) | 22 |
| `til_lora__rank4_original_20shot.csv` | TIL-LoRA | A74:M82 | 20-shot TIL-LoRA (Rank=4, Task Order=Original) | 25 |
| `cpe_clip__original.csv` | CPE-CLIP | A2:M10 | CPE-CLIP (Task Order=Original) | 5 (see flag 2) |
| `fine_tuning__original.csv` | Fine-tuning | A2:M10 | Fine-Tuning (Task Order=Original) | 2 (see flag 1) |
| `fine_tuning__reverse.csv` | Fine-tuning | A46:M54 | Fine-Tuning (Task Order=Reverse) | 16 (see flags 6, 7) |
| `fine_tuning__original_5shot.csv` | Fine-tuning | A24:M32 | 5-shot Fine-Tuning (Task Order=Original) | 18 |
| `fine_tuning__original_10shot.csv` | Fine-tuning | A35:M43 | 10-shot Fine-Tuning (Task Order=Original) | 21 |
| `fine_tuning__original_20shot.csv` | Fine-tuning | A13:M21 | 20-shot Fine-Tuning (Task Order=Original) | 24 |
| `til_lora_isolated__rank8_original.csv` | TIL-LoRA (isolated) (hidden) | A2:L9 | Task-Incremental LoRA (rank=8, Task Order=Original) | — |
| `til_lora_isolated__rank16_original.csv` | TIL-LoRA (isolated) (hidden) | A12:L19 | Task-Incremental LoRA (rank=16, Task Order=Original) | — |
| `til_lora_isolated__rank32_original.csv` | TIL-LoRA (isolated) (hidden) | A22:L29 | Task-Incremental LoRA (rank=32, Task Order=Original) | — |
| `til_lora_isolated__rank64_original.csv` | TIL-LoRA (isolated) (hidden) | A32:L39 | Task-Incremental LoRA (rank=64, Task Order=Original) | — |
| `til_lora_isolated__rank128_original.csv` | TIL-LoRA (isolated) (hidden) | A42:L49 | Task-Incremental LoRA (rank=128, Task Order=Original) | — |
| `til_lora_isolated__rank8_reversed.csv` | TIL-LoRA (isolated) (hidden) | A52:L59 | Task-Incremental LoRA (rank=8, Task Order=Reversed) | — |

"Dashboard row" is the workbook row in `Dashboard`. Dashboard columns map to block cells as follows:
- `Average Performance` → `Average` row, `Average Performance`
- `Final Average Performance` → `Average` row, `Final Performance`
- `Final Forgetting` → `Average` row, `Final Forgetting`
- `Transfer` → `Average` row, `Transfer`
- `Relative Retention Drop` → `aeropath (Retention)` row, `Final Retention Drop`

21 of the 26 Dashboard data rows match their block exactly (all five values identical as stored). The Dashboard contains no formulas; all its values are typed or pasted.

## Data-quality flags (to be checked by the author)

1. **Dashboard row 2 (Fine-Tuning, Main)** holds typed, rounded values: `0.13`, `0.13`, `0.70399999999999996`, `1E-3`, `1`. The full values in `fine_tuning__original.csv` are `0.13040343513228819`, `0.13024868170671447`, `0.70352631520178543`, `1.2445761387210839E-3` and retention `0.9995576854435374`.
2. **Dashboard row 5 (CPE-CLIP):** retention drop `1`, but the block has `0.99984147368813514`.
3. **Dashboard row 11 (CIL-LoRA rank 512):** retention drop `0.58599999999999997`, but the block has `0.58634167830552997`.
4. **Dashboard row 17 (TIL-LoRA, Convergence Diagnosis):** `0.83899999999999997`, but the block has `0.83858853578567505`. The Dashboard says 50 epochs; the block title states no epoch count.
5. **Dashboard row 27 (CIL-LoRA + Replay):** retention drop `6.7445686536808996E-3`, but the block has `6.7445686536809039E-3`. The digits differ in the 16th place, so the value was pasted, not linked.
6. **Dashboard row 16:** method is written `FT`, while other rows use `Fine-Tuning`. It also has `LoRA Rank` = `4` for a method without LoRA.
7. **`fine_tuning__reverse.csv`:** the title says Task Order=Reverse, but the row and column labels are in the original order. The `Pretrained` value `0.68415092180172599`, which is the Femoral value in every other block, sits in the row labelled `Patellar`, and the row labelled `Femoral` has `0`. The labels were probably not updated for the reverse order. Check against the raw evaluation output.
8. **Duplicate block:** `TIL-LoRA` blocks at `A23` and `A40` have the same title and identical values.
9. **The hidden sheet `TIL-LoRA (isolated)`** has 5 tasks (no Lateral Meniscus) and matches the older runs shown in the intro-talk slides (e.g. slide 29). It contains the typo `Medial Mensicus` (A53) and uses an absolute retention drop (see deviations above).
10. **The `Pretrained` column** differs slightly between blocks although it is the same pretrained model. Femoral: `0.68415092180172599` / `0.68414774164557401` / `0.68415083115299502`. AeroPath: `0.97939328849315599` / `0.97939257323741902` / `0.97939284145831995`.
11. **The slides** (`presentation/shashank_master_thesis.pptx`) report numbers from older 5-task runs that differ from this workbook (e.g. Fine-Tuning final forgetting 0.812 on slides vs `0.70352631520178543` here). Do not use the slides as a source for numbers.
