# Length: cut proposal (2026-10-26) — for the author's decision, nothing applied

## Starting point
- Main content Ch. 1–8: **pp. 1–102** of `thesis_main.pdf` (2026-10-26), including about 5 blank pages from the two-sided template (chapters start on odd pages; layout is not changed).
- Running text (words outside floats, `scratchpad/length_stats.py`, about 420 words per page): Ch. 1 5.1 · Ch. 2 12.7 · Ch. 3 8.4 · Ch. 4 5.2 · Ch. 5 12.6 · Ch. 6 16.4 · Ch. 7 10.2 · Ch. 8 3.2 → **about 74 pages of text**, plus 33 floats (figures, tables, algorithms) and Table 2.1 (4.6 pp).
- Targets in the guidelines: supervisor "no more than 50-60 pages. But it can be longer if there are many figures and appendices" (`supervisor_guidelines.md:53`); chair "reference: 40 pages for bachelor thesis, 75 pages for master thesis, excluding appendix" (`chair_guidelines.md:194`). Both: length is not a quality criterion.

## Recommended target: about 75–80 pages (chair reference; justified by the many figures)
Reaching 60 would need cutting about 40 % of all text, including content the chair grades (limitations, alternatives, complexity). Ask the supervisor in the pending email whether about 75 pages with 30+ figures/tables is acceptable.

## Proposals per chapter (estimated saving in pages)

| Ch. | Now | Proposal | Saving | Target |
|---|---|---|---|---|
| 1 | 8 | 1.4 "Approach and Scope" repeats Ch. 5/6 details (ranks, k, metric definitions); keep one paragraph each, definitions only in Ch. 3 | 1 | 7 |
| 2 | 18 | (a) Table 2.1: 47 rows → the about 20 works discussed in the text; the rest stays in the text or moves to an appendix table (supervisor requires a summary table, so it stays in Ch. 2); (b) 2.1: shorten 2D works to one paragraph; (c) 2.3: compress the VLM continual-learning review (long method-by-method descriptions) to the three families with the 1–2 closest works each | 5–6 | 12 |
| 3 | 12 | 3.3 "Methods adapted by the strategies" overlaps 5.4.2–5.4.5 (LoRA, ZSCL, CPE-CLIP details): keep the concepts in 3.3, keep our changes only in 5.4 (already noted in the tracker); 3.1 VoxTell details that 5.3 repeats (decoder stage, fusion) only once | 2–3 | 9–10 |
| 4 | 8 | 4.5 "Data quality and limitations" overlaps 7.3 (split, orientation): keep the facts in 4.5, only a reference in 7.3 | 0.5 | 7.5 |
| 5 | 16 | (a) 5.4.4/5.4.5: the "differs from ZSCL in six points" and CPE-CLIP difference lists into one compact table (Table 5.1 extended by a column "difference from the original method"); (b) 5.3: implementation details (self-attention never executed, parameter counts) shortened, counts stay in Table 5.2 | 2–3 | 13–14 |
| 6 | 26 | (a) Fig. `ch6_main_matrices` (full page) duplicates App. A matrices → move to App. A, keep the reference; (b) rank and task order each have a table and a figure with the same numbers → keep the figure, tables to App. A; (c) few-shot table (21 rows) → App. A, the updated figure stays (Transfer only in the table: state it); (d) 6.4 patellar diagnosis: table stays, loss figure → App. A, text shortened; (e) 6.7 cost: one paragraph + table; (f) Table 6.3 strategy parameters stays (reproducibility) | 5–6 | 20–21 |
| 7 | 10 | 7.1 repeats many numbers of Ch. 6: answer each objective in 3–4 sentences with references instead of numbers; 7.2 shortened to the hypothesis and its test; 7.3 kept (graded: limitations, threats to validity) | 2.5–3 | 7–7.5 |
| 8 | 3 | keep (chair: 3–4 pages) | 0 | 3–3.5 |
| **Total** | **≈ 102** | | **≈ 18–23** | **≈ 79–84** incl. about 5 blank pages |

## Notes
- Everything moved to the appendix stays referenced from the text, with the section it belongs to (chair rule); the thesis must stay understandable without the appendix, so no result that a conclusion rests on moves out of the main text.
- Order: decide the target and the cuts **before** the rewrite, so no text is rewritten that is cut later.
- Cuts in Ch. 1, 2, 3 are best done together with the author's rewrite; moves of floats in Ch. 6 are mechanical and can be done by Claude on request.

## First candidates: repeated text and text without added value (2026-10-26, author's priority)
Found with `scratchpad/repetition_scan.py` (sentences sharing much of their wording across chapters) and a topic check. Not candidates: the deliberate results recap of Ch. 8, the self-contained table and figure captions, and Ch. 1 content needed by readers outside the field.

| # | Passage | Repeats | Proposal | Saving (pp.) |
|---|---|---|---|---|
| R1 | Ch. 7.1, `discussion.tex:25-75` (about 1,500 words) | per-experiment results of 6.2-6.6 with the same numbers | per objective 3-4 sentences: the cross-experiment answer and the comparison with prior work; numbers by reference | 2.0 |
| R2 | Ch. 7.2 first paragraph, `discussion.tex:79-87` | the four results of 6.3-6.6 | one sentence with references | 0.2 |
| R3 | Ch. 8 future work, `summary.tex:63-67` | Ch. 7.4 almost word for word | 1-2 sentences + reference to 7.4 | 0.3 |
| R4 | Ch. 1.4 metrics paragraph, `introduction.tex:154-162` | definitions of 3.4, choice of 6.1.4 | name the three primary metrics, refer to 3.4 | 0.2 |
| R5 | Ch. 1.4 strategies paragraph, `introduction.tex:139-148` | 5.4 opening and Table 5.1 | names with one clause each | 0.15 |
| R6 | gap and "this thesis does" twice: Ch. 1.2 `introduction.tex:95-100` and Ch. 2.5 `related_work.tex:326-348` (incl. 343-347, which repeats 1.4/1.5) | each other, 1.4, 1.5 | evidence of the gap stays in 2.5; Ch. 1 one sentence + reference; 2.5 l. 343-347 one sentence | 0.4 |
| R7 | ZSCL and CPE-CLIP mechanism in three places: Ch. 2.3 `related_work.tex:145-149, 193-196`, Ch. 3.3.3/3.3.4 `background.tex:189-228`, Ch. 5.4.4/5.4.5 | each other | Ch. 2 keeps the results (its role) with one clause on the mechanism; Ch. 3 keeps the mechanism; Ch. 5 keeps only the differences of our adaptation | 1.2 |
| R8 | LoRA initialisation, `background.tex:165` and `method.tex:263` | each other | Ch. 5 only the deviation (Kaiming-uniform) | 0.1 |
| R9 | loss, `background.tex:33` and `method.tex:158` | each other | Ch. 3 one clause, equation only in Ch. 5 | 0.1 |
| R10 | "task-specific LoRA: zero by construction" in `method.tex:76-77`, `experiment_results.tex:130-131`, captions of 6.2/6.3, Ch. 7.3 | each other | definition in 5.2 and the captions; references elsewhere | 0.15 |
| R11 | "one run per configuration; intervals cover only test volumes; differences of a few hundredths" in 6.1.4, `experiment_results.tex:341`, `:498`, `discussion.tex:138-146` | each other | full statement once in 6.1.4, as a limitation in 7.3; short pointers in 6.3 and 6.6 | 0.3 |
| R12 | no per-strategy tuning, `method.tex:175`, `experiment_results.tex:37-38`, `discussion.tex:132` | each other | decision in 5.3, limitation in 7.3; 6.1.1 one clause | 0.1 |
| R13 | splits and definition of k, `experiment_results.tex:53`, `:62` | `data_description.tex:128`, `method.tex:42` | 6.1.2 keeps only the values with their reasons | 0.2 |
| R14 | joint reference introduced twice in Ch. 6, `experiment_results.tex:29`, `:164` | each other | keep once | 0.05 |
| V1 | chapter openings listing the sections (Ch. 6 `:15-17`, Ch. 7 `:14-15`, others to check) | the table of contents | one short sentence (style rule) | 0.15 |
| V2 | section openings of 6.2-6.6 listing which strategies were trained (`experiment_results.tex:163, 401, 465`, ...) | Table 6.1 | question + reference to Table 6.1 | 0.2 |
| V3 | VoxTell facts (training data, prompt types) in Ch. 1 `introduction.tex:33, 39` and Ch. 2.1 `related_work.tex:53-54` | each other | the numbers once (2.1); Ch. 1 conceptual | 0.1 |
| | **Total** | | | **≈ 5.9** |

Repetition alone saves about 6 pages; the rest of the target needs the float moves in Ch. 6 (about 5-6 pp., no content lost) and content selection in Ch. 2 (Table 2.1, 2.3).

## Check of the candidates for pure duplication (2026-10-26, author: remove only pure duplicates)
Only `experiment_results.tex:53` (split sizes, identical to Ch. 4.3) was a pure duplicate and was removed. R1-R14 and V1-V3 all carry a local function (new detail, premise of an argument, required by the chair in that place, or signposting) and stay; shortening them is a rewrite decision for the author.
