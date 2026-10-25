# Whole-thesis pass, 2026-10-23 (Ch. 1–6, Appendix A)

Scope: all drafted text (Ch. 1–6, App. A). Ch. 7/8 are empty; 6.2 and 6.7 wait for the reruns.
Backup of every chapter file before this pass: `backups/2026-10-23_before_whole_thesis_pass/`.
Rerun-dependent passages (tracker B) and author decisions were not reworded.
All edited paragraphs keep their `% CLAUDE-DRAFT` marker.

Severity: **M** must fix · **S** should fix · **m** minor. Status: **fixed** · **open** (needs the author or the reruns).

## Structure (cross-chapter repetition and order)

| ID | Sev | Issue | Where | Status |
|---|---|---|---|---|
| S1 | M | Research-gap paragraph of 1.2 nearly verbatim in 2.5 | `introduction.tex` 1.2, `related_work.tex` 2.5 | fixed: 1.2 compressed to one sentence pointing to 2.5 |
| S2 | M | "Does not propose a new method" stated three times | 1.4, 1.5, 2.5 | fixed: removed from 1.4 (1.5 and 2.5 keep it) |
| S3 | M | Stability–plasticity sentence and ZSCL zero-shot degradation in both 1.2 and 3.2 (same citations); ZSCL degradation also in 2.3 and 3.3.3 | 1.2, 2.3, 3.2, 3.3.3 | fixed: definitions of stability/plasticity merged into 1.2; 3.2 keeps only the formal statement in matrix terms; 3.3.3 points back to 1.2. Matches the decision of 2026-10-22 (Ch. 1 informal, Ch. 3.2 symbols only) |
| S4 | M | Control-task role and reasons for choosing it written twice (4.2 and 5.1) | `data_description.tex` 4.2, `method.tex` 5.1 | fixed: 4.2 keeps the data facts (not in VoxTell's training, 96.99 %, lung frequent) and points to 5.1 for role and selection |
| S5 | M | Checkpoint rule (last epoch vs best validation) stated eight times | 5.2, 5.3, Table 5.1, 5.4.1, 5.4.2, 5.4.5, 6.1.3 | fixed: kept in 5.3 (with the reason) and Table 5.1 (column); 5.4.4 keeps it where it explains the ensemble; others removed or replaced by a pointer |
| S6 | S | Ch. 5 restates Ch. 3: ZSCL (5.4.4 para 1), CPE-CLIP incl. its ablation (5.4.5 para 1; ablation sentence appeared four times: 2.3, 3.3.4, 5.4.5 twice), Hu et al. q/v finding (5.4.2), VoxTell pretraining recipe (5.3) | 3.3, 5.3, 5.4 | fixed: one-sentence back-references; CPE-CLIP ablation kept only in 2.3 (as a finding) and referenced from 5.4.5 |
| S7 | S | 5.5 repeated the memory statements of 5.4.1–5.4.5 | 5.5 | fixed: compressed to the cross-strategy comparison, storage growth and inference |
| S8 | S | 6.1 repeated Ch. 4/5: same test volumes, nested few-shot sets, validation/test sets independent of k, optimiser follows VoxTell, α/dropout difference, γ_r over rank, checkpoint rule | 6.1.2, 6.1.3 | fixed: removed or replaced by pointers; "γ_r not compared with α/r" moved to 6.3 next to the confound |
| S9 | S | 6.1.4 re-defined the metrics in words already used in 3.4 | 6.1.4 | fixed: 6.1.4 now gives only the choice (primary/secondary, retention as property, Transfer within one order, Average Performance dropped) |
| S10 | S | Scenario explanation and "task-aware inference" defined in 3.2 and again in 5.1, with a circular reference (3.2 → 5.1 for the term) | 3.2, 5.1, 5.4 | fixed: term defined in 3.2; 5.1 one sentence; duplicate sentence in 5.4 intro removed |
| S11 | S | Sentence on VoxTell's knee explanation copied verbatim from 1.1 into 4.1.2 | 4.1.2 | fixed: removed in 4.1.2, pointer to 1.1; the "rarely seen vs absent" reading stays in both chapters (decision D2) |
| S12 | m | Cross-reference density (246 `\cref`; Ch. 1: 36, Ch. 5: 61) | all | partly fixed: refs to the previous section, repeated targets within a paragraph and refs whose content was removed are gone (about 15). Remaining refs point to definitions or values the reader needs. Further pruning is a language-polish item for the final review |
| S13 | M | **Length**: main text pp. 1–78 without 6.2, 6.7, Ch. 7, Ch. 8 (projected ≈ 90) vs 50–60 (supervisor, guidance only, decision 2026-10-22). Ch. 2 = 18 pp. (incl. 4.6 pp. tables), Ch. 5 = 16 pp. This pass removed repetition, not content | all | **open (author)**: candidates for cuts below |

Cut candidates (for the author to decide; not done):
1. Ch. 2: shorten 2.4.1 (early networks: Baweja, Ozdemir, ILT/MiB, Liu et al.) and 2.1 (2D works LViT, TextMatch, R-Super, BiomedParse, MedSAM-3) to one paragraph each; move Table 2.1 to the appendix and keep Table 2.2 in the chapter (would need the supervisor's OK: the outline asks for a summary table).
2. Ch. 3: 3.1.2 attention equation (experts know it; cite Vaswani) and 3.3.2 replay (half a page) could shrink.
3. Ch. 5: the cost paragraphs of 5.4.x could move entirely into Table 5.2 + 5.5.
4. Ch. 6: Table 6.2/6.3 could move to the appendix with a short summary in the text.

## Content and argument

| ID | Sev | Issue | Where | Status |
|---|---|---|---|---|
| C1 | M | Fusion equation written for s = 4, …, 0, but at s = 0 the implementation computes the logits as one dot product (as 5.3 says); Ch. 3 and Ch. 5 contradicted each other | `background.tex` Eq. bg-voxtell-fusion | fixed: equation for s = 4, …, 1, one sentence on s = 0 (checked in `code/src/model/voxtell_model.py:442-447`) |
| C2 | M | No stated reason for choosing VoxTell (D1; tracker said "Ch. 5.3, text", but it was missing) | 5.3 | fixed: one sentence with the author's reason (2026-10-21: free text + highest mean zero-shot DSC in its paper's comparison, ahead of SAT), pointing to 2.1 for the numbers |
| C3 | M | Ch. 4 intro: control task "never trained on" contradicts the replay exception stated two paragraphs later | `data_description.tex` intro | fixed: wording removed |
| C4 | S | 3.1.2 says VoxTell's prompt decoder uses self- and cross-attention blocks; the implementation executes only cross-attention | 3.1.2 | fixed: pointer to 5.3 |
| C5 | S | Catastrophic forgetting cited to French (1999), for which there are no notes (CLAUDE.md citation rule) | 3.2 | fixed: citation removed, back-reference to 1.2 (De Lange) |
| C6 | m | Average Performance described as "mean over all entries after the first stage" (ambiguous; the script uses stages 1 to T) | 6.1.4 | fixed |
| C7 | m | Patellar diagnosis assigned to objective 4 in Table 6.1 although it is not an objective (tracker C) | `tables/ch6_experiments.tex` (generated) | open (author) |
| C8 | m | 1.1 refers the pretrained mean DSC 0.114 to `sec:exp-main`, which is still empty | 1.1 | open (resolves with 6.2 after the reruns) |

## Citations and locators

| ID | Sev | Issue | Status |
|---|---|---|---|
| R1 | m | VoxTell supplement locators mixed ("S-p." in Ch. 3, "Table 7/10" without "Supplementary" in 4.2) | fixed: "Suppl. p." in Ch. 3, "Supplementary Table" in 4.2 |
| R2 | m | Ch. 6 says "objective stated in the introduction" without a reference | fixed: `\cref{sec:intro-rq}` |
| R3 | m | Table 5.2 caption "Chapter 6" as text | fixed: `\cref{tab:ch6_compute}` |

## Language and terminology

| ID | Sev | Issue | Status |
|---|---|---|---|
| L1 | m | LoRA used in Ch. 1 before it is expanded | fixed (1.4) |
| L2 | m | "PET" not via `\gls` in 3.1.3 | fixed |
| L3 | m | "UNet decoder" (5.4) vs "convolutional decoder" (3.1.3) | fixed: "convolutional decoder" |
| L4 | m | "multi-modal" vs "multimodal" | fixed |
| L5 | m | `\cref` at sentence start in Ch. 4 | fixed: `\Cref` |
| L6 | m | Ambiguous "place the works … ourselves" (2.3) | fixed |
| L7 | m | Acronyms LoRA, rsLoRA, CLIP, SAM, ZSCL, LwF written by hand, not via `\gls`; CLIP never expanded | open (tracker C; decide whether to add them to `abbreviations.tex`) |

## Formal / compile

| ID | Sev | Issue | Status |
|---|---|---|---|
| F1 | m | Section 2.3 heading 8 pt too wide | fixed (line break in the heading, TOC entry unchanged) |
| F2 | m | Overfull boxes from margin `\todo` notes (5 places) | open: disappear when the todos are resolved |
| F3 | m | 4 overfull bibliography entries (e.g. D'Alessandro et al.) | open: `literature.bib` is edited only on request |
| F4 | m | Cover sheet title 26.7 pt too wide (template `deckblatt`) | open (author; template not edited) |

## Not changed on purpose (author items, see tracker C)
Declaration "fur" → "für" (never modified by Claude); cover start date 15.05.2026 vs 15.04.2026 in CLAUDE.md; abstracts EN/DE and table of notation missing; objectives/contributions provisional; old notes commented out at the end of `introduction.tex`; CLAUDE.md chapter table still lists Ch. 1/2 as "author's notes" although both are now drafted.
