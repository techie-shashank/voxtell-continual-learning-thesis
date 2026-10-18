# Final Review Procedure

Use this only when I ask for a final review pass. The goal is a submission-ready thesis that meets the supervisor and chair guidelines and that I can defend line by line.

## Rules for every pass
- **Report only, don't edit.** Output an issue list; I decide what to change. Fixes happen in separate tasks.
- **One pass per session**, started fresh, so the review is not influenced by earlier drafting.
- Review the whole thesis for that pass's focus only; don't mix in other kinds of issues except "must fix" findings.
- Each issue: file and line, what is wrong, why it matters, and a severity (must fix / should fix / minor). Don't rewrite the text in the report; describe the problem.
- Save each report as `reviews/passN_<name>.md` and add a line to `ai_use_log.md`.

## Preconditions (check before pass 1)
- All chapters are written, and I have rewritten every paragraph: `grep -rn "CLAUDE-DRAFT" thesis/` returns nothing.
- Results and figures are final and regenerated from `scripts/`.
- List every remaining `\todo{}`. They must all be resolved before pass 6.

## Pass 1 — Structure and common thread
- Do the research questions and objectives in the Introduction match what was done and achieved?
- Is every research question answered explicitly in the Discussion and Summary?
- Does each chapter deliver what CLAUDE.md requires, and does each chapter lead logically to the next?
- Is the split between theoretical and practical parts roughly balanced (chair)?
- Does the Summary state clearly which results are my original work, and is it 3–4 pages?
- Is the main content within about 50–60 pages? Which parts could be cut or moved to the appendix?

## Pass 2 — Technical correctness and traceability
- Every number in the text, tables and figures matches `results/` or the data. List any you can't trace.
- Method descriptions match `code/`.
- All parameters needed to reproduce each experiment are stated.
- Each algorithm has language-independent pseudocode, time and memory complexity, and measured runtime and memory.
- Equations are correct and consistent with the text; definitions are precise.
- Claims are not stronger than the evidence; variability and number of runs are reported.

## Pass 3 — Citations and bibliography
- Every non-obvious claim has a citation, and every cited key exists.
- Claims attributed to papers are plausible given what I provided; flag any you can't verify for me to check against the paper.
- Bibliography entries: required fields complete (pages; proceedings date, place, editor); peer-reviewed versions preferred over arXiv.
- Every figure not created by me cites its source in the caption.
- No uncited close paraphrase: flag passages that read like a source text.

## Pass 4 — Consistency
- One term per concept across all chapters; list deviations.
- Notation: each symbol has one meaning, is explained at first use and appears in the table of notation; scalar/vector/matrix conventions followed.
- Acronyms defined once, used consistently.
- Tense and person consistent.
- Figures and tables: same fonts and size as the text, consistent style, units, self-contained captions, each referenced in the text.
- Number formatting and precision consistent.

## Pass 5 — Language and style
- Grammar, spelling (British, -ise endings) and punctuation.
- Anything that breaks the writing style rules in CLAUDE.md: inflated words, filler phrases, formulaic patterns, repetition, vague statements, overclaiming.
- Unclear sentences: list them with what makes them hard to follow.
- Sections that change in voice or quality compared to the rest.

## Pass 6 — Formal compliance (chair and supervisor guidelines)
- Cover sheet complete as in the chair template.
- German declaration present and identical to the chair text (Sec. 1.2), with space for signature.
- Abstracts in English and German, each at most half a page, saying the same thing.
- Table of contents depth 3; table of notation present.
- Appendix: referenced from the text, each part names its section, thesis understandable without it.
- AI-use declaration done as agreed with the supervisor.
- `latexmk` compiles without errors and warnings; no `\todo`, `??` or undefined references in the PDF.

## Pass 7 — Examiner's view
Read the thesis as a critical examiner would:
- List the 15–20 questions an examiner is most likely to ask in the final presentation, starting with the hardest.
- List the weakest points of the thesis and what would strengthen each.
- Point out anything that suggests I may not understand my own work, so I can study it.

## My own steps (not done by Claude)
1. Fix the issues I accepted from each pass, then compile.
2. Read the full PDF myself in one go, ideally printed, and mark anything that doesn't sound like me.
3. Check a sample of citations against the actual papers.
4. Send the draft to my supervisor and work in their feedback (their feedback overrides these reports).
5. Prepare answers to the pass 7 questions.
6. Final check: compile cleanly, sign the declaration, submit the printed copy and archive files as the chair requires.
