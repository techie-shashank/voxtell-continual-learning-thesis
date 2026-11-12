# Restructure: Ch. 7 Discussion dissolved into Ch. 6 and the Summary

Status: **approved and implemented 2026-11-11** (steps 1-5).
Decision behind it (author, 2026-11-11): remove Ch. 7. The prior-work comparisons of 7.1 go into the Ch. 6 conclusions, the cross-experiment answer of 7.1 merges with Ch. 8 into one Summary, 7.2 and the generalisation paragraphs of 7.3 become Sec. 6.8, and the extensions of 7.3 replace the future-work paragraph of the Summary.
Reasons: the supervisor's outline has no Discussion; 7.1 and Ch. 8 overlap by necessity (both answer the RQ); Ch. 7 + 8 ≈ 12 pages against a budget of ≈ 7.

Line numbers refer to `thesis/discussion.tex` (D), `thesis/summary.tex` (S) and `thesis/experiment_results.tex` (E) as of 2026-11-11.
Text moves with its `% CLAUDE-DRAFT` marker, `% source:` comments and `\todo{defense}` markers.
New linking words are kept to the minimum; nothing is reworded beyond what the new place requires.

## 1. Where every paragraph of Ch. 7 goes

| Ch. 7 paragraph | Content | Destination | Change needed |
|---|---|---|---|
| D 17-18 | Chapter opening | **dropped** | – |
| 7.1 P1, D 26-31 | RQ answer: 0.233 ceiling; what is left after the last task | **Summary** para 3 (already holds the ceiling, S 36) | 'segmented little beyond the structures trained last' and femoral cartilage dropped: already in 6.2 (E 179-180, 192) |
| 7.1 P2, D 34-40 | Replay and task-specific LoRA as the exceptions; Beyond Forgetting, MedPEFT-CL, Lifelong nnU-Net | facts: **Summary** para 3 (already there, S 37-40); prior work: **6.2 conclusion** (after E 221) | two sentences on prior work, appended to the conclusion |
| 7.1 P3, D 43-47 | Pretrained ability not kept; task-specific LoRA keeps the control task because it is evaluated without an adapter | **dropped**, duplicate of the 6.2 conclusion (E 217-221) | add the reason as a half-sentence to E 220 ('task-specific LoRA by construction') ('..., which evaluates the control task with the pretrained model') |
| 7.1 P4, D 50-55 | Few-shot; Silva-Rodríguez | facts: already in **6.4 conclusion** (E 319-323) and Summary para 4; Silva-Rodríguez: **6.4 conclusion**, after E 320 | one sentence |
| 7.1 P5, D 58-63 | Task order; Beyond Forgetting Sec. 4.4; ranking from two orders may not hold | facts: **6.6 conclusion** (E 454-458); prior work + caveat: **6.6 conclusion**, after E 457 | two sentences |
| 7.1 P6, D 66-68 | Rank; contrast with rsLoRA | **6.5 conclusion**, after 'at a cost in Adaptation' (E 374) | two sentences |
| 7.1 P7, D 71-75 | Distillation-based strategy vs ZSCL (Transfer) | **6.2, new paragraph** after the Transfer paragraph (E 199-200), since it is about Transfer | drop the `\cref{sec:exp-main}` (now the same section) |
| 7.1 P8, D 78-86 | Protocol: control-task drop vs Final Forgetting; pretrained reference; SPU, none of the closest works | **Summary** para 6 (already holds both examples, S 60-62) | add 'neither metric can stand in for the other' and the SPU / closest-works sentence (supports contribution 1 as own work); the seq. FT k = 20 example dropped (one example per direction is enough in a summary) |
| 7.2 all, D 93-157 | Limitations and threats to validity | **new Sec. 6.8** after 6.7, label `sec:exp-limitations` | see Sec. 2 below |
| 7.3 P1, D 167-170 | What generalises: numbers and ranking do not, the protocol does | **6.8**, as a whole, after the limitations (revised 2026-11-11: kept with P2, not split) | – |
| 7.3 P2, D 173-175 | Chen et al.: the same contrast in another setting, so it may hold more generally | **6.8**, after P1 (revised 2026-11-11: it is a generalisation argument, not a per-experiment comparison, so it does not go to 6.2) | – |
| 7.3 P3, D 178-187 | Main extension: keep pretrained ability without task identity (MoE-Adapters, text-prompt similarity, nested learning) | **Summary**, future work, compressed to ≈ 5 sentences | MedCRP-CL reference points to 6.8 |
| 7.3 P4, D 191-193 | Replay in other orders/ranks; selection criteria | **Summary**, one clause | Bera et al. / MedPEFT-CL selection criteria dropped (examiner question, not a main extension) |
| 7.3 P5-P6, D 196-206 | Tests of the slow-learning explanations; runs; evaluation extensions | **Summary**, future work, compressed (as S 75-77 now, plus equal-updates runs at k = 10/20 and tuning on the validation split) | – |

## 2. New Sec. 6.8 Limitations and Generalisation

Placed after 6.7 Computational Cost, as the last section of Ch. 6.
Content: D 93-157 in the present order (three main limitations, slow learning of LoRA, single runs, scope, strategies not evaluated, protocol, internal threats, data and checkpoint), then D 167-175 (what generalises: protocol; Chen et al.).
Reason for the order: the limitations end with the scope of the study, and the generalisation paragraphs answer the question this raises, what carries over beyond it.
Changes:
- opening: plain statement of scope (limitations, then what generalises), no back-reference opener;
- D 102: `\cref{sec:disc-rq}` → `\cref{sec:exp-few-shot}`;
- D 106 todo: 'tests in sec:disc-generalisation' → 'tests in the Summary';
- D 167: `\cref{sec:disc-limitations}` dropped (same section); D 173 `\cref{sec:disc-rq}` → `\cref{sec:exp-main}`;
- refs to the same chapter stay as they are (`\cref` to 6.x sections).

Repetition inside Ch. 6 to check afterwards (not part of the move): the confound paragraph (D 97-99) repeats the caveats at the ends of 6.3, 6.4 and 6.5. A collected list at the end of the chapter is a deliberate recap, so it stays; flagged for the chapter review.

## 3. Summary (becomes Ch. 7)

One chapter without sections, as now. Target ≤ 1,300 words (now 1,085), i.e. about 4 pages including the chapter opening (chair: 3-4 pages).

| # | Paragraph | Source |
|---|---|---|
| 1 | Context, setting, control task | S 15-18, unchanged |
| 2 | Contributions (own work) | S 22-28, unchanged |
| 3 | Answer to the RQ, full training split | S 31-41, unchanged |
| 4 | Few volumes | S 45-49, unchanged |
| 5 | Task order and rank | S 53-56, unchanged |
| 6 | What the protocol showed | S 60-62 + D 82-83 (two sentences) |
| 7 | Limits | S 66-70 cut to 1-2 sentences with `\cref{sec:exp-limitations}` |
| 8 | Future work: main extension | D 178-187, compressed |
| 9 | Future work: tests, runs, evaluation | S 75-77 + D 191-192 clause + D 196-206, compressed |

## 4. Other changes

- `thesis_main.tex`: comment out `\include{discussion}`; `discussion.tex` copied to `backups/discussion_2026-11-11_before_restructure.tex` and then deleted from `thesis/` (or kept unused; author's choice).
- Ch. 6 opening (E 15-17): one sentence pointing to 6.8.
- `introduction.tex:174`: `sec:disc-limitations` → `sec:exp-limitations`; `introduction.tex:208`: outline sentence ('Chapter 6 ... and states the limitations; Chapter 7 summarises ...').
- E 234, E 458: `sec:disc-limitations` → `sec:exp-limitations`; E 458 'is discussed in' stays.
- `summary.tex`: `sec:disc-rq` (S 32, 60) → `sec:exp-main` / the Ch. 6 sections; `sec:disc-generalisation` removed.
- CLAUDE.md: chapter table (Summary = Ch. 7), structure decision ('Discussion dissolved 2026-11-11'), 'What each chapter must deliver' (limitations and prior-work comparison in Ch. 6, RQ answer in the Summary), the rule 'answered in the Discussion and Summary' → 'in the Summary'.
- `thesis_tracker.md`: locations 'Ch. 7' in D8, D10, D14, D16, D28, D41-D43, D46, D54, D57, D64-D66 → new places.
- `outlines/ch7_discussion.md`, `outlines/ch8_summary.md`: marked superseded by this file.
- Build once after the structural edit (undefined references).

## 5. Order of work (one step at a time, each shown before editing)

1. Sec. 6.8 (move 7.2, fix refs).
2. Prior-work sentences into 6.2, 6.4, 6.5, 6.6 (one diff for all four, since each is 1-4 sentences).
3. Summary paragraphs 6-9.
4. Remove Ch. 7, fix refs, Ch. 6 opening, Ch. 1 outline sentence, build.
5. CLAUDE.md, tracker, superseded outlines.

## 6. Choices (resolved 2026-11-11 unless marked open)

1. 6.8 title: **'Limitations and Generalisation'** (Claude's recommendation after choice 2 put the generalisation paragraphs into 6.8; the title names both criteria the chair grades). Author asked for the recommendation; confirm with the outline.
2. Chen et al.: **in 6.8 with the rest of the generalisation paragraphs** (revised after the author's question: D 173-175 argues that a result may hold more generally, so moving it to 6.2 would change its function).
3. Protocol transferability (D 168-170): **in 6.8**, as part of 7.3 P1 kept whole; the Summary's future work keeps its existing half-sentence on other free-text promptable models (S 77).
4. Replay extensions (D 191-193): **one clause** in the Summary. The limitation (replay only at r = 1024, original order) is already in 6.8 (D 123-125), so a full paragraph would repeat it; the selection criteria are an examiner question (D54), not a main extension.
5. `discussion.tex`: delete after the backup (recommended) or keep unused. **Open.**
