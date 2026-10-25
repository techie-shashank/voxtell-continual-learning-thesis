# Review and rewrite plan — from first draft to submission

Agreed 2026-10-24. Submission: Sun 15.11.2026. Rerun cutoff: 1.11 (latest 3.11).
Starting point: complete first draft (abstracts pending), 261 paragraphs marked `% CLAUDE-DRAFT`, 49 `\todo`s, defense points in `thesis_tracker.md` §A.

## 1. Strategy in one paragraph

One quick read of the whole draft first, to catch the big problems while they are still cheap to fix. Then chapter by chapter, each brought to **content-final** (rewritten in your words, all its markers and todos resolved, section review passed) before the next. "Submission-ready" polish is not done per chapter, because changes in later chapters ripple back; it happens once, for the whole thesis, in the final review. Chapters that don't depend on the reruns come first, the results chapters last, so you rewrite them only once.

## 2. Timeline

| Dates | You | Claude |
|---|---|---|
| Sun 25.10 | **Pass 0: skim read** of the printed PDF (one sitting, about 4 h), notes in `my_review/pass0.md`; send supervisor email | Supervisor email draft; triage of your pass-0 notes into an issue list; pack for Ch. 4 |
| 26.10 | Rewrite **Ch. 4** Data (8 pp.) | Section reviews as you finish sections; pack for Ch. 5 |
| 27–28.10 | Rewrite **Ch. 5** Method (16 pp.) | Section reviews; pack for Ch. 3 |
| 29–30.10 | Rewrite **Ch. 3** Background (12 pp.) | Section reviews; chapter reviews of Ch. 4, 5 |
| 31.10–2.11 | Rewrite **Ch. 2** State of the Art (18 pp.) | Section reviews; chapter review of Ch. 3 |
| 1–3.11 | Copy finished reruns to `results/hpc/` | **Integrate reruns** (run_all.py, text switches in Ch. 5, 6, 7); resolve every `\todo{rerun}` to one version |
| 3–5.11 | Rewrite **Ch. 6** Experiments (22 pp.) | Section reviews; chapter review of Ch. 2 |
| 6.11 | Rewrite **Ch. 7** Discussion | Section reviews; chapter review of Ch. 6 |
| 7.11 | Final contributions; rewrite **Ch. 8** and **Ch. 1**; write the AI-use statement | Abstract drafts (EN/DE) from your Ch. 8; chapter reviews of Ch. 7, 8, 1 |
| 8.11 | Rewrite abstracts; decide on the final-review issues | **Final review** (FINAL_REVIEW.md, passes 1–6 condensed into one report, `reviews/final_review.md`); fixes you approve |
| **Mon 9.11** | **Send to supervisor** (ask for feedback by Thu 12.11) | — |
| 9–12.11 | Read the whole PDF once on paper (pass 7, below); defense-points answers | Citation check of rewritten chapters (citation-verifier, on your request); fixes you approve |
| 12–14.11 | Incorporate supervisor feedback | Apply the changes you decide; recompile; final formal check |
| 14.11 | Print, sign the declaration | Final compile without warnings |
| **15.11** | **Submit** | — |

Buffers: Ch. 2 and Ch. 6 are the largest; if one slips, take the day from 9–12.11, not from the supervisor's review time. Check **now** (supervisor email) whether the supervisor can read the thesis 9–12.11, and how submission works on a Sunday (online upload? printed copies?).

Pace: 261 marked paragraphs in about 13 days ≈ 20 per day. Many are short (captions, one-sentence paragraphs). Trim while you rewrite: about 10 pages of prose over the 50–60 target (repetition between Ch. 3/5, Ch. 2 prose, numbers in 7.1).

## 3. The loop for each chapter

1. **Claude prepares a chapter pack** `reviews/chN_pack.md` before you start: the chapter's page budget; known issues (from pass 0, earlier reviews, corrections); every `\todo` in the chapter with a proposed resolution; the defense points from `thesis_tracker.md` §A that live in this chapter; open author decisions. You work from this one file, not from the tracker.
2. **You rewrite, section by section, directly in the `.tex` file.** Remove `% CLAUDE-DRAFT` only from paragraphs you have rewritten in your own words — even if you agree with a draft paragraph, rewrite it (authorship, signed declaration).
3. **You leave instructions for Claude in the `.tex` file** where they apply (see §4) and resolve the todos you can.
4. **After each section: "section X.Y done, review"** → Claude runs the section review (CLAUDE.md checklist), reports issues, edits nothing.
5. You decide; Claude applies only what you approve (and your `% @claude` notes).
6. **When all sections pass: chapter review** (CLAUDE.md level 2) → status "Reviewed" in the CLAUDE.md chapter table.

Definition of **content-final** for a chapter: no `% CLAUDE-DRAFT`, no `% @claude`, no `\todo` except `\todo{rerun}` waiting for 1–3.11; section and chapter review passed; compiles without warnings.

## 4. How to give Claude your feedback

- **In the `.tex` file, next to the passage** (preferred; Claude finds them with `grep`):
  - `% @claude: <instruction>` — something to do (e.g. `% @claude: check this number against cl_metrics.csv`, `% @claude: shorten 6.3 by half a page, propose cuts first`).
  - `% @claude?: <question>` — something to explain or check, answer only.
  - Claude removes a note once it is done and reports it.
- **Bigger or cross-chapter notes:** `my_review/<topic>.md` (e.g. `my_review/pass0.md`, `my_review/ch5.md`), in any form — bullet list is fine.
- **In chat:** short commands, e.g. "Ch. 4.2 done, review", "apply my @claude notes in Ch. 5", "answer my @claude? notes", "chapter review Ch. 4".
- Text you rewrote yourself is never rephrased by Claude unless you ask for that passage.

## 5. Checklists

### Pass 0 — skim read (whole thesis, printed, no line edits)
Write one line per finding in `my_review/pass0.md` with page number.
- [ ] Does the story hold from the research question to the Summary? Where does it break?
- [ ] Is there any claim, interpretation or conclusion you don't agree with or couldn't defend orally?
- [ ] Anything missing that an examiner will ask for? Anything that should go?
- [ ] Which sections feel too long or repetitive?
- [ ] Figures and tables: does each one earn its place?
- [ ] Surprises: anything you did not know or do not remember deciding?

### Your rewrite checklist (every section)
- [ ] I agree with every sentence and can explain and defend it without notes.
- [ ] Every paragraph is in my own words; markers removed only for rewritten paragraphs.
- [ ] One idea per paragraph, clear topic sentence, the point first.
- [ ] Numbers: spot-check at least one per paragraph against the `% source:` comment.
- [ ] Citations: the cited paper says this (check `paper_notes/` if unsure; else `% @claude?`).
- [ ] Terms from the CLAUDE.md terminology list (strategy names, "control task", "task order", DSC …).
- [ ] Nothing repeated from an earlier chapter; cut what the reader already knows.
- [ ] No style "don'ts" (CLAUDE.md list), no "significant" without a test, no overclaiming.
- [ ] The section's `\todo`s resolved (§6) or a `% @claude` note left.

### Claude's section and chapter reviews
As defined in CLAUDE.md ("Review levels", "Section review checklist"); you don't need to run them yourself.

### Pass 7 — your final paper read (after sending to the supervisor)
- [ ] Read the PDF on paper, start to end, as an examiner would.
- [ ] Every figure and table: readable at print size, referenced, caption self-contained.
- [ ] Every defense point in `thesis_tracker.md` §A: I know the answer and where the thesis states it.

## 6. What happens to the markers and trackers

| Item | Rule | Deadline |
|---|---|---|
| `% CLAUDE-DRAFT` | removed by you only after rewriting the paragraph | before the final review (8.11) |
| `\todo{defense: …}` | decide per item: (a) fix in the text, (b) accept as a stated limitation (it must then appear in 7.3 or the section), or (c) keep only for the oral defense (move to tracker §A, remove from the text) | at the chapter review |
| `\todo{cite / check / ref}` | resolve; Claude proposes the fix in the pack | at the chapter review |
| `\todo{author / provisional}` | your decision; contributions after the results analysis | 7.11 |
| `\todo{rerun: …}` | Claude switches to one version after the cutoff, then removes the todo | 3.11 |
| `thesis_tracker.md` §A defense points | checked per chapter in the pack; kept after submission for the oral defense | ongoing |
| `thesis_tracker.md` §B, §C | Claude keeps current; you mark items done | ongoing |
| `thesis_notes.md` | record of decisions and facts; Claude updates it | ongoing |

Before sending to the supervisor (9.11): zero `% CLAUDE-DRAFT`, zero `\todo` (they print in the margin), zero `% @claude`, compile without warnings. `python scripts/list_todos.py` and `grep -rn "CLAUDE-DRAFT\|@claude" thesis/` must return nothing.

## 7. Front matter and formal items (not chapter-bound)

- [ ] Supervisor answers: separate Method and Discussion chapters, AI-use statement, page length, review dates (email 25.10).
- [ ] Declaration: "fur" → "für"; otherwise exactly the chair text.
- [ ] Cover: start date 15.05.2026 or 15.04.2026?
- [ ] Abstracts EN/DE, each ≤ half a page (7.–8.11).
- [ ] "Use of AI tools" statement from `ai_use_log.md`, in your words (7.11).
- [ ] CLAUDE.md chapter table updated.
- [ ] Bibliography: arXiv entries with peer-reviewed versions (ZSCL → ICCV 2023, VoxTell → CVPR 2026, others in tracker §C) — ask Claude to upgrade them (bib-entry-adder) before the final review.
