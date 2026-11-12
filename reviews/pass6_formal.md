# Pass 6 — Formal compliance (2026-11-12)

Done in the main session with scripts, report only. Source: `thesis/thesis_main.log`, `thesis_main.blg` and `thesis_main.pdf` of the build finished at 17:24 by a parallel session (136 pages), and the `.tex` sources at that time.

## Build
| # | Issue | Where | Severity |
|---|---|---|---|
| 1 | 4 package warnings: xcolor option `usenames` obsolete; siunitx options `binary-units` and `abbreviations` removed; tracklang no `datatool` support for `english`. Also "language number for Austrian undefined" (babel, info line, not a warning). | log l. 224, 439, 525, 529, 1358 | must fix (zero warnings at archiving; = D12) |
| 2 | `todonotes` still loaded although 0 `\todo` remain in the chapters. | `thesis_main.tex:49` | must fix (D12) |
| 3 | Overfull hbox 26.7 pt on the cover sheet (logo line, template `deckblatt`). Check whether it shows; may need a template-side workaround outside `lmedoc/`. | log l. 1730, input line 93 | should fix |
| 4 | 4 overfull hboxes (0.3–2.4 pt) in the bibliography, entry D'Alessandro et al. ("Multi-modal parameter-…"). | log l. 2094–2112 | minor |
| 5 | 24 underfull vboxes during output (page breaks). Not warnings, but check those pages for visible gaps in the read-through (D10). | log | minor |
| 6 | No undefined references or citations; biber log clean; no `??` in the PDF text. | — | OK |

## Front matter
| # | Issue | Where | Severity |
|---|---|---|---|
| 7 | Start date on the cover is **15.05.2026**, CLAUDE.md says 15.04.2026. One of them is wrong; author to check the registration. | `thesis_main.tex:89`, `CLAUDE.md:10` | must fix |
| 8 | Place of birth is a country ("India"); the chair template asks for the place of birth. Author to decide (city?). | `thesis_main.tex:86` | should fix |
| 9 | Abstracts: empty at the time of this check; added later the same evening by the parallel session (English approved by the author, German a Claude translation marked `% CLAUDE-DRAFT`). Remaining: German to be checked by a native speaker; half-page limit to be confirmed in the next PDF. | `thesis_main.tex:126–160` | should fix (author) |
| 10 | German declaration: word-by-word identical to the chair text (`guidelines/chair_guidelines.md:25–31`), including "Punkt 2.5"; signature line present. | `thesis_main.tex:97–117` | OK |
| 11 | AI-use statement not yet in the front matter (waiting for the supervisor's answer, E1). | — | must fix (author) |
| 12 | TOC depth: not set (report default 2). The thesis has no `\subsubsection`, so depth 2 already shows every heading; setting `\setcounter{tocdepth}{3}` would satisfy the rule formally without changing output. | `thesis_main.tex` | minor |
| 13 | Table of notation, list of abbreviations, lists of figures and tables present. | `thesis_main.tex:149, 179–189` | OK |

## Floats and figures
| # | Issue | Where | Severity |
|---|---|---|---|
| 14 | All figures included at natural size are 14.6–16.2 cm wide, within the 16.2 cm text width (script plots and TikZ, allowed exception). | `figures/*.pdf` | OK |
| 15 | Two appendix tables use `[tbp]` and `[!tb]`; rule is `[tb]` or `[p]`. `[tbp]` is harmless; `!` overrides float parameters. | `appendix.tex:63, 80` | minor |
| 16 | Table captions above, figure captions below in all floats checked. | all chapters | OK |
| 17 | `figures/ch6_control_task_main.pdf` exists but is not included anywhere (generated, unused). | `thesis/figures/` | minor |

## Appendix
| # | Issue | Where | Severity |
|---|---|---|---|
| 18 | Every appendix section opens with "This section belongs to …" and the appendix is referenced from Ch. 1 and Ch. 6. | `appendix.tex` | OK |

## Precondition of FINAL_REVIEW.md not met
| # | Issue | Where | Severity |
|---|---|---|---|
| 19 | 241 `% CLAUDE-DRAFT` markers remain (intro 22, related work 30, background 34, data 12, method 43, results 70, summary 12, appendix 18). By the author's rules each marks a paragraph not yet rewritten in the author's own words. Only the author removes them; with the declaration "ohne fremde Hilfe" this is the most important open formal point. | all chapters | must fix (author) |
