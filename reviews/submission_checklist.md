# Submission checklist (from 2026-11-12, deadline 15.11.2026)

Checks are grouped by the level at which they can actually be checked. A = during the voice pass, section by section. B = scripts and agents on the final text of each chapter. C = after each chapter. D = once, on the whole thesis. E = author only.
Order of chapters for A: Ch. 1 → Summary → Ch. 6 (two rounds) → Ch. 5 → Ch. 2 → Ch. 3 → Ch. 4 → Appendix.

## Order of execution (decided 2026-11-12)
1. Start (Thu): E1 supervisor email; B2 regenerate tables and figures; B4 bibliography check in the background.
2. Per chapter, pipelined: A (with E2 for that chapter's todos) → author approves the diff → B1, B3, B5, B6 and C1–C3 on that chapter while A runs on the next one. Author reads each approved chapter in the PDF (first part of E4).
3. After Ch. 1 and Summary: E3 abstracts (interview, same voice).
4. After all chapters: D1–D11 as report-only passes in a fresh session (FINAL_REVIEW.md), then fixes.
5. End: E4 full read-through of the PDF → fixes → D12 final build → E5 submit.
Timing: Thu Ch. 1 + Summary + abstracts; Fri Ch. 6 + Ch. 5; Sat Ch. 2–4 + Appendix, D passes in the evening; Sun D fixes, read-through, final build, submission.

## Per-chapter loop (decided 2026-11-12, replaces the single A pass)
0. Todos decided before the voice pass (`reviews/todo_decisions.md`, done 2026-11-12: 0 markers left).
1. Claude: voice pass B as a proposal file (`reviews/voice/chN_*.tex`); focus A1–A3, A13, A15, A16.
2. Claude: `python reviews/tools/lint_thesis.py <file>` (A2, A4–A9, B5 mechanically) `python reviews/tools/check_numbers.py <file>` (B1), and `python reviews/tools/check_refs.py <file>` (over-citing, citation placement, unnecessary cross-references; author request 2026-11-12, every flag judged by hand); integrity check of citations, numbers, crossrefs, markers against the pre-pass version.
3. Fresh proofreader subagent (report only, `reviews/voice/chN_proofread.md`): grammar, tier 1, terms, meaning drift BEFORE vs AFTER.
4. Claude: mechanical findings fixed; meaning-related ones into a numbered "please decide" list.
5. Author: answers the list, approves the diff.
6. Claude: apply, build (author OK), citation-verifier (B3) in the background, tracker and log. Any later change to a citation is re-verified by the citation-verifier on exactly the changed sentences (author request 2026-11-12).
7. Author: reads the chapter in the PDF.
Whole thesis: the seven FINAL_REVIEW passes as seven separate fresh subagents in parallel (Sat afternoon), then regression run of lint, numbers and build on all chapters.
Status 2026-11-12 (late): step 1 done: citation-verifier on every chapter complete, all findings fixed and re-verified, build clean. Steps 2-4 (B4, D passes 1-7) run in a separate session per reviews/next_steps.md. B6 done (check_floats.py).

## A. Voice pass, per section (Claude edits, author approves one diff per chapter)
- [ ] A1 Voice B as in `style/voice_sheet.md`
- [ ] A2 Style rules of CLAUDE.md: no banned words, filler phrases or formulaic patterns
- [ ] A3 Tier-1 rules: no insertions between subject and verb, referents in the preceding sentence, modal strength, no term before its introduction, conditions of general claims, prior work as in Ch. 2 / `paper_notes/`, `\Cref` at sentence start
- [ ] A4 Grammar, confusable words, British -ise spelling, no contractions
- [ ] A5 Punctuation: serial comma, `--` for ranges, ``…'' quotation marks, hyphenation of compound modifiers
- [ ] A6 Tense and person: present for the method and what results show, past for what was done; "we", never "I"
- [ ] A7 Terminology list and notation of CLAUDE.md; every symbol defined at first use
- [ ] A8 Abbreviations via `\gls`, defined once
- [ ] A9 Numbers: three decimals for own results, one rule for small counts in words, units with `siunitx`
- [ ] A10 Cross-references: only where they help; point to the right place
- [ ] A11 Claims no stronger than the evidence; "significant" only statistically; runs and variability stated
- [ ] A12 Missing citations flagged as `\todo{cite: …}`
- [ ] A13 Prior work and own contribution clearly separated
- [ ] A14 `\todo`s in the section: resolved in the text, or (defense todos) moved to the tracker for the oral defense; author decides
- [ ] A15 Sentences where a voice edit could change meaning: listed for the author, not changed
- [ ] A16 `% CLAUDE-DRAFT` markers unchanged

## B. Verification on the final text of each chapter
- [ ] B1 Numbers: every number in text and captions matched against `thesis/tables/*.csv` and `results/` by script; mismatch list
- [ ] B2 Tables and figures regenerated with `python scripts/run_all.py`; none edited by hand
- [ ] B3 Citation-verifier per chapter: each `\cite` supports its sentence, locators correct, no overclaiming (earlier checks of Ch. 1/2 from 23.10. are outdated)
- [ ] B4 Bibliography: required fields, peer-reviewed versions, duplicate keys, unused entries
- [ ] B5 Greps: banned words and phrases, US spellings, "I ", contractions, bare "prompt"
- [ ] B6 Every figure, table and appendix part referenced in the text

## C. After each chapter
- [ ] C1 The chapter delivers what CLAUDE.md requires for it
- [ ] C2 Sections connect; no repetition across sections; terms consistent across sections
- [ ] C3 Build compiles; no new warnings, undefined references or citations

## D. Whole thesis, once
- [ ] D1 Objectives ↔ contributions ↔ experiments ↔ Summary; every objective addressed, research question answered explicitly
- [ ] D2 No contradictions between chapters; the same numbers and claims in Abstract, Ch. 1, Ch. 6, Summary
- [ ] D3 Repetition across chapters; length (main text ~80 pp. vs 50–60, supervisor's answer)
- [ ] D4 Continual-learning defensibility: task order and dependence on it, how forgetting is measured, reference points, k and sampling with variability, text prompts and dependence on wording
- [ ] D5 All parameters for reproducing each experiment stated (Ch. 6, App. A)
- [ ] D6 Each algorithm: pseudocode, time and memory complexity, measured runtime and memory with hardware
- [ ] D7 Table of notation and list of abbreviations complete and used
- [ ] D8 Figures: 10–11 pt, readable in black and white, table captions above and figure captions below, sources for adapted figures; equations numbered consistently
- [ ] D9 Front matter: cover sheet complete, German declaration identical to the chair text, abstracts EN and DE (each at most half a page, same content), TOC depth 3, notation, AI-use statement
- [ ] D10 PDF layout: page breaks, headings at page bottom, blank pages, float positions, overfull boxes, short captions in the lists
- [ ] D11 Appendix referenced from the main text, each part names its section, thesis understandable without it
- [ ] D12 `todonotes` removed; final build without errors and warnings; no `??`

## E. Author only
- [ ] E1 Supervisor: AI-use statement, length, submission on Sunday 15.11.
- [ ] E2 Author todos `method.tex` l. 227 and l. 310; decisions on the defense todos
- [ ] E3 Abstracts: content from the author (interview)
- [ ] E4 Full read-through of the PDF; can explain every sentence
- [ ] E5 Sign the declaration, submit, archive as the chair requires
