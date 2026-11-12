# Next steps (written 2026-11-12, evening) — read this first in a fresh session

State: voice pass, proofread, lint, numbers, citation/cross-reference checks and build are done and applied for ALL chapters and Appendix A (see `reviews/submission_checklist.md`, status line). 0 `\todo` markers. Build clean except preamble warnings (D12).

The previous session hit the 5-hour usage limit (resets 21:30 Europe/Berlin) with nine report-only subagents running in parallel. Lesson: run at most two agents at a time, give each the exact files and scope, and keep the main session short.

## Stopped agents (work saved; continue with SendMessage "Continue where you stopped and give the final report", one or two at a time)
Agent IDs are only valid in the session that started them. If the fresh session cannot reach them, restart the same task with the prompt summarised below.

| Order | Task | Agent ID (old session) | Scope |
|---|---|---|---|
| 1 | D pass 7 examiner's view | a18e23ea290ef1fbd | 15-20 likely questions with tracker IDs; weakest points; places the author must study. Was nearly done. |
| 2 | D pass 2 technical correctness | ac4aa349c4a606381 | method.tex vs code/; background.tex equations vs scripts/compute_cl_metrics.py; reproducibility; spot-check ~15 numbers |
| 4 | D pass 3 citations scope | ace122d2d1f4465b0 | uncited claims (all chapters), close paraphrase, figure sources in captions, own vs prior work, quotes; NOT per-citation for Ch. 2/3 |
| 5 | D pass 1 structure | ab253d3c9963f6500 | objectives/contributions vs results, RQ answered, theory/practice balance, Summary 3-4 pp., page count, what could move to the appendix |
| 6 | D pass 5 language | a4b3cbf7cada971a5 | unclear sentences, tier-1, overclaiming, repetition, voice differences (lint already done) |
| 7 | D pass 4 consistency | aea9559c7f57bbb4d | terms, notation table vs usage, acronyms, numbers repeated in Ch. 1/6/Summary |
| 8 | B4 bibliography | a5c88cd795dff8aee | required fields, peer-reviewed versions, duplicates, unused keys |
| — | D pass 6 formal compliance | aee487979324aeda4 | do in the main session with scripts instead: build log warnings/overfull/undefined, "??" in PDF, German declaration vs chair text word by word, TOC depth, figure placement/width, captions |

Save each report as `reviews/passN_<name>.md` (agents cannot write files).

## Steps 2-4 (D passes 1-7 and B4): DONE 2026-11-12 in a second session; reports `reviews/pass1_structure.md` … `pass7_examiner.md`, `reviews/b4_bibliography.md` (old agent IDs above were not reachable; tasks restarted fresh). Next: sort findings into 'mechanical: fix' / 'needs author decision', then fixes and regression run.

## Step 1 (citation checks of all chapters): DONE 2026-11-12 in the first session; all findings fixed, re-verified, build clean. Do not redo.

## Then
- D12: remove todonotes, fix preamble warnings (siunitx options, xcolor usenames, tracklang), 5 overfull boxes; zero warnings.
- E3 abstracts EN/DE: blocked on the author's answers to the six questions.
- Author: supervisor email (AI-use statement), full PDF read-through, locator checks with university access (Silva-Rodriguez MedIA, SKM-TEA NeurIPS, VoxTell CVPR supplement), sign and submit 15.11.
