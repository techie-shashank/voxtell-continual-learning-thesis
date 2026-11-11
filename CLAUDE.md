# Master's Thesis — Instructions for Claude

This is my master's thesis at the Pattern Recognition Lab (LME), FAU Erlangen-Nürnberg. I am the author, and the thesis must be my own original work that I can fully explain and defend. Your role is assistant, critic and editor, not ghostwriter. Read this file fully before every task.

## About this thesis
- **Title:** Continual Learning for Promptable Universal 3D Medical Image Segmentation in Few-Shot Settings
- **Thesis type:** Master's thesis in Computer Science
- **Author:** Shashank Shashank
- **Advisors:** Prof. Dr.-Ing. habil. Andreas Maier, Dr.-Ing. Tomás Arias Vergara
- **Started / submission deadline:** 15.04.2026 / 15.11.2026
- **Language:** English, British spelling with -ise endings (matches my existing drafts)

**Research question**
How do different continual-learning strategies trade off adaptation performance and catastrophic forgetting when adapting free-text promptable universal 3D medical image segmentation models under few-shot conditions?

**Objectives** (as in Ch. 1, Sec. 1.3; reworded 2026-11-01: questions in terms known by Sec. 1.3, no terms that Sec. 1.4 introduces)
1. Develop an evaluation protocol for the setting of the research question that measures adaptation, the forgetting of earlier tasks and the loss of pretrained ability separately (reworded 2026-11-06: adaptation added, setting no longer repeated).
2. Compare continual-learning strategies with each other and with fine-tuning on each task in turn, and determine how they trade adaptation against forgetting (reworded 2026-11-06: tied to the research question).
3. Investigate how the number of labelled volumes per task influences adaptation and forgetting, separating the effect of fewer volumes from that of fewer updates.
4. Analyse how the order of the tasks and the design choices within the strategies influence adaptation and forgetting.

**Contributions — FINAL** (decided 2026-10-26, option A: descriptive, one per objective; reworded 2026-11-01: four items, each saying what was delivered and how, in the terms of Sec. 1.4; wording as in Ch. 1, Sec. 1.5). Findings belong in Ch. 6–8 with their caveats, not in the contributions.
1. An evaluation protocol that measures the loss of pretrained ability separately from the forgetting of earlier tasks, through a held-out control task, with the pretrained model and joint fine-tuning as reference points (reworded 2026-11-06: states what the protocol makes possible).
2. A comparison of sequential fine-tuning and five continual-learning strategies adapted to VoxTell under one shared training configuration, together with a diagnosis of why task-specific LoRA did not learn patellar cartilage.
3. An analysis of how the amount of labelled data affects adaptation and forgetting, with three of the strategies and joint fine-tuning, which separates fewer volumes from fewer updates by training on five volumes with as many updates as on the full training split (reworded 2026-11-06).
4. An analysis of how the task order and the rank of the LoRA adapters affect adaptation and forgetting, with two task orders and ranks from r = 4 to r = 2048 (reworded 2026-11-06: purpose first, scope brief; objective 4 kept, 'number of trainable parameters' rejected because rank and gamma_r are confounded; App. A components not a contribution, as decided 2026-11-05, since appendix-only; replay is reported with the comparison in Sec. 6.2 since 2026-11-04).

Every objective must be addressed in the Method or Experiment & Results chapters, and every final contribution must be supported by the results.

## Sources of truth (in order of priority)
1. Supervisor guidelines: `guidelines/Thesis_Outline.pdf`
2. Chair guidelines: `guidelines/drichtl_en.pdf` (LME thesis guidelines, Dec 2024)
3. The actual code in `code/` and data in `results/`
4. My explicit instructions in the current session
5. This file
6. Existing chapter text — **lowest priority**

Where the supervisor and chair guidelines differ, follow the supervisor. If one of my instructions conflicts with a guideline, point out the conflict before doing it.

Chapters 1 and 2 (current text) are the author's notes, not drafts (decision 2026-10-22). They are redrafted like the other chapters: outline, approval, section-by-section drafting with `% CLAUDE-DRAFT`, interview first for reasoning-heavy parts. Use them for content and selection of works, not as a reference for facts, style or terminology; claims about papers need the paper or paper notes (citation-verifier for the rest). They may contain errors, weak arguments and inconsistent terms.

## Project layout
- `thesis/` — LaTeX source. Main file: `thesis/thesis_main.tex`
- `thesis/*.tex` — one `.tex` file per chapter, directly in `thesis/` (flat layout, see chapter table), plus `abbreviations.tex` and `appendix.tex`
- `thesis/figures/`, `thesis/tables/` — figures and outsourced tables. Generated figures are never edited by hand; regenerate via `scripts/`
- `thesis/literature.bib` — the bibliography, maintained by hand (no Zotero). Edit it only when I ask, following the bibliography rules below.
- `code/` — implementation. **Read-only.**
- `results/` — raw experiment outputs. **Read-only. Never modify, move or delete.**
  - `results/hpc/experiments/` — **single source of truth** for every experiment (config, eval matrix, per-task outputs); `results/hpc/logs/` — SLURM logs.
  - `results/experiment_index.csv` — the only maintained file in `results/`: one row per experiment (parameters, status, SLURM logs). Generated by `scripts/build_experiment_index.py`; only the columns `label`, `role`, `notes` are edited by hand and are kept on rerun.
  - `results/few_shot_cl_results_fixed.xlsx` — my manual summary, superseded by the scripts. Not a source for numbers.
- `scripts/` — scripts that turn `results/` and data into figures and tables. `python scripts/run_all.py` rebuilds everything in order (index → per-volume scores → metrics → tables → figures → compute table). `compute_cl_metrics.py` is the reference implementation of the CL metrics (not `code/src/continual/metrics.py`). Generated: `thesis/tables/cl_metrics.csv`, `per_volume_dice.csv`, `compute.csv`, `ch6_*.tex` (bare `tabular`, caption in the chapter), `thesis/figures/ch6_*.pdf`
- `guidelines/` — supervisor and chair guidelines
- `ai_use_log.md` — log of how AI was used (see below)
- `thesis_notes.md` — decisions, verified facts about the experiments (with sources), limitations, open questions. **Read before writing any chapter**; update it when a decision is made or a fact is verified
- `thesis_tracker.md` — defense points (examiner questions with current answer, location, status), items waiting for the reruns, open items for the author, and the generated list of `\todo` markers (`python scripts/list_todos.py`). Keep it current at the end of every task
- `paper_notes/` — one notes file per key paper, with page/table locations, written from the PDF. **`paper_notes/voxtell.md` covers the VoxTell paper (`voxtell_paper/voxtell.pdf`) completely; use it instead of re-reading the PDF.** Its last section is analysis, not paper content. `paper_notes/zscl.md`, `cpe_clip.md` and `lora_hu.md` cover ZSCL, CPE-CLIP and LoRA the same way; `liu2026_vlm_cl_survey.md` holds partial notes (author excerpt) on the VLM continual-learning survey
- `datasets/` — the dataset papers (SKM-TEA, AeroPath); `voxtell_paper/` — the VoxTell paper
- `FINAL_REVIEW.md` — the final review procedure. Use it only when I ask for a final review pass.

## Chapter status
| # | Chapter | File | Status |
|---|---------|------|--------|
| 1 | Introduction | `thesis/introduction.tex` | Author's notes — to be redrafted (decision 2026-10-22); objectives/contributions final after the results |
| 2 | State of the Art | `thesis/related_work.tex` | Author's notes — to be redrafted (decision 2026-10-22), next |
| 3 | Theoretical Background | `thesis/background.tex` | Full draft (all paragraphs `% CLAUDE-DRAFT`, 2026-10-22) — author rewrite pending |
| 4 | Data Description | `thesis/data_description.tex` | Full draft (all paragraphs `% CLAUDE-DRAFT`, 2026-10-19) — author rewrite pending |
| 5 | Method | `thesis/method.tex` | Full draft (all paragraphs `% CLAUDE-DRAFT`, 2026-10-21; restructured 2026-10-31, `outlines/ch5_method.md` v2: 5.1 Evaluation Protocol, 5.2 Adapting VoxTell to One Task, 5.3 strategies, 5.4 complexity) — author rewrite pending |
| 6 | Experiment & Results | `thesis/experiment_results.tex` | Full draft (all paragraphs `% CLAUDE-DRAFT`; switched to the reruns 2026-10-26) — author rewrite pending. Appendix A drafted (38 runs) |
| 7 | Discussion | `thesis/discussion.tex` | Full draft (all paragraphs `% CLAUDE-DRAFT`, 2026-10-24; switched to the reruns 2026-10-26) — author rewrite pending |
| 8 | Summary | `thesis/summary.tex` | Full draft (all paragraphs `% CLAUDE-DRAFT`; rewritten 2026-11-11 from `outlines/ch8_summary.md` rev. 2) — author rewrite pending |

Structure decisions (provisional, to confirm with the supervisor):
- **Method** is a separate chapter, although the supervisor's outline doesn't list one: the chair requires a practical part with algorithms, pseudocode and complexity, and this needs its own place.
- **Discussion** is a separate but compact chapter (approved by the author 2026-10-24; neither guideline prescribes it, but the chair grades critical discussion, limitations and generalisation, and its Summary is results-only, 3-4 pages; fallback: last section of Ch. 6). Each experiment's own conclusion stays in Experiment & Results (supervisor); the Discussion covers what spans all experiments.
- The last chapter is called **Summary**, as both the supervisor's outline and the chair guidelines name it.

## Build
```bash
cd thesis && latexmk -pdf thesis_main.tex
```
Document class and packages (from `thesis_main.tex` and `thesis/lmedoc/`; read 2026-10-17):
- **Class:** `lmedoc/lmedoc` with options `english,mt` (LME template, based on `report`, twoside, 12 pt, A4 via `geometry`, `\onehalfspacing`). Don't edit files in `thesis/lmedoc/`.
- **Engine:** `latexmk -pdf` runs pdfLaTeX + biber. The magic comment in `thesis_main.tex` says `xelatex`; the preamble supports both.
- **Bibliography:** `biblatex` (backend biber, style `trad-alpha`, `backref`), `\addbibresource{literature.bib}`.
- **Glossaries:** yes, `glossaries-extra` with `abbreviations`, `shortcuts=true`, style `long-short`. Define acronyms with `\newabbreviation` in `thesis/abbreviations.tex`, use `\gls{}`; printed with `\printunsrtglossary` (no makeglossaries step).
- **Cross-references:** `hyperref` (so `\autoref` works), `cleveref` (options `noabbrev,capitalise,nameinlink`, so `\cref` works too), `varioref`, `hypcap`.
- **Algorithms:** `algorithm`/`algorithmic` loaded in `thesis_main.tex` (added 2026-10-21).
- **Vectors/matrices:** `\vec{}` and `\mat{}` are both bold (`\bm`), defined by the template in `lmedoc/math.sty:138-139` (checked 2026-10-21). Don't redefine them.
- **Other:** `booktabs`, `tabularx`, `caption`/`subcaption`, `siunitx`, `tikz`, `amsmath`/`amssymb`/`mathtools`/`bm`, `xcolor`, `enumitem`, `nowidow`, `microtype`.

After every LaTeX edit, compile and fix any errors you introduced, including undefined references or citations. The final version must compile without errors and without warnings (the lab checks this at archiving).

## Formal requirements (from the guidelines)
**Length:** main content about 50–60 pages (supervisor); may be longer with many figures; appendix excluded. Length is not a quality criterion: prefer compact text.

**Front matter, in this order:**
1. Cover sheet as in the chair template: topic, thesis type, author, date and place of birth, chair and department, advisors, start and finish dates.
2. The German declaration from the chair guidelines (Sec. 1.2), copied exactly. **Never modify, translate or rephrase it.** I sign it by hand.
3. Abstract in English and in German, each at most half a page.
4. Table of contents (depth 3).
5. Table of notation.

**Layout:** A4, 12 pt, line spacing 1.2 (bibliography 1.0). The template handles this; don't change layout settings.

**Figures**
- Font family the same as the main text, size about the same. Generate plots at their final printed width so they are not scaled; use LaTeX-matching fonts.
- Every figure has a number and a caption and is referenced in the text (`\autoref{}` or `\figurename~\ref{}`).
- Figures not created by me must cite their source in the caption and the bibliography.
- Placement `[tb]` or `[p]`. Width only via `\linewidth` (e.g. `width=0.45\linewidth`). Exception: TikZ diagrams and script plots that are built at their final width are included at natural size (no `width=`), so their fonts are not rescaled.
- Font size in all figures (plots and diagrams): 10–11 pt at print size, i.e. about the text size as the supervisor requires (decided 2026-10-21). Plot scripts use 10 pt for labels, ticks, legends and cell values.
- File names relate to the section where the figure appears (e.g. `figures/ch4_class_distribution.pdf`).
- When a results table is too dense, add a bar plot (supervisor).
- How figures are made (decided 2026-10-21): plots by Python scripts in `scripts/` (vector PDF); architecture and concept diagrams in TikZ following the rules below; image content inside diagrams only from our own data (`scripts/make_diagram_assets.py`); figures from papers only redrawn, with "adapted from~\cite[Fig.~X]{key}" in the caption.

**TikZ diagram rules** (author's rules, 2026-10-21; font size adapted to the chair guideline)

*Process (mandatory)*
1. Each figure is its own standalone file `thesis/figures/tikz/<chN_name>.tex` (`\documentclass[12pt,tikz,border=2pt]{standalone}`, shared preamble `figures/tikz/preamble.tex` with the thesis fonts and packages). `scripts/build_tikz.py` compiles it to `thesis/figures/<chN_name>.pdf`, which the thesis includes with `\includegraphics`. Variants of one design share a body file.
2. Before writing code, list the nodes, their rows/columns, and every connection (source anchor → target anchor, straight or orthogonal).
3. After writing, compile, then render with `pdftoppm -png -r 400`. View the full image and zoomed crops of every region (a grid of at least 3×2 crops).
4. Check every item of the visual checklist against the crops. Fix, recompile, re-inspect. Repeat until every item passes.
5. Only then report back, stating which checks were verified and any compromise made.

*Code rules*
- No absolute coordinates except a single origin. Place nodes with `positioning` (`right=6mm of x`), `matrix` or `chains`; derived points (`(a |- b)`) are fine.
- Every connection goes between named anchors (`(a.east) -- (b.west)`), never to hand-tuned points.
- Orthogonal routing (`-|`, `|-`) for all non-trivial connections. No diagonal lines unless they are semantically meaningful.
- Define junction points with `\coordinate`; branch residual/skip connections from a point on the line at least 3 mm from any node.
- Define spacing, line widths, arrow tips, colours and fonts once as styles or macros at the top of the file. Elements of the same kind use the same style.
- When several arrows enter one node, give each its own anchor (`north west`, `west`, `south west`, or `yshift` offsets). Never converge them on one point.
- Draw each path exactly once.
- At least 5 mm between consecutive boxes in a chain, so arrows have a visible shaft.
- Labels go on edges with `node[above]` / `node[midway, right]` and get `inner sep` padding. They never sit on lines or in gaps between boxes.

*Visual checklist (on the 400 dpi crops)*
- [ ] No arrowhead overlaps a node border or enters a node.
- [ ] No line crosses a label, a box, or another box's border unless it intentionally enters that box.
- [ ] No two parallel lines closer than 2 mm.
- [ ] Nodes meant to align (rows, columns, matching boxes/circles) share exact x or y coordinates.
- [ ] Every line starts and ends exactly on its intended element, with no gaps and no overshoot.
- [ ] All dashed/dotted lines of one kind look identical in weight.
- [ ] Labels of corresponding elements have consistent spacing (e.g. the input and output image captions).
- [ ] Text fits inside its box with padding; nothing is clipped.
- [ ] Font at final print width matches the thesis: 10–11 pt (`\small`, `\footnotesize` in the 12 pt class); never `\scriptsize` for labels. (The author's original rule said 7–9 pt; the chair guideline requires font size matching the main text, l. 74 of `guidelines/chair_guidelines.md`.)
- [ ] The figure fits the text width (16.2 cm) without scaling below 100 %.

**Mathematics and notation**
- Every symbol without a universal meaning is explained in the text at first use, even though there is a table of notation.
- Each symbol has exactly one meaning throughout the thesis (indices like i, j are exempt) and appears in the table of notation.
- Scalars: lowercase italic; vectors: bold lowercase; matrices: bold uppercase (use `\vec{}` and `\mat{}`).

**Algorithms (practical part)**
- Describe all algorithms and data structures independently of the programming language, with pseudocode (`algorithmic`) or flow charts.
- For each algorithm, give time and memory complexity, plus measured runtime and memory consumption with the hardware used.

**Bibliography**
- BibTeX/BibLaTeX, cited with `\cite{}`.
- All required fields filled: pages for articles; date, place and editor for proceedings.
- Cite the peer-reviewed publisher version when one exists, not arXiv or Google Scholar BibTeX.
- `thesis/literature.bib` is maintained by hand. When you notice missing fields, duplicate keys or arXiv entries that have a peer-reviewed version, report them; fix them only when I ask.

**Appendix**
- The thesis must be understandable without the appendix.
- Every appendix part is referenced from the main text and states which section it belongs to.

## Authorship and originality
- The ideas, argument, interpretations and conclusions are mine. Do not invent research ideas, interpretations of results, limitations or future work and present them as settled. If something is missing, ask me, or offer options clearly marked as suggestions for me to choose from.
- Before drafting reasoning-heavy text (motivation, design decisions, conclusions of experiments, Discussion, Summary), interview me first: ask short, specific questions and build the text from my answers.
- Prefer these modes, in this order: (1) questions and outlines, (2) feedback and critique on my text, (3) explaining concepts so I can write about them, (4) drafting. Draft prose only when I ask for it.
- Mark every paragraph you draft with a LaTeX comment `% CLAUDE-DRAFT` on the line above it. I remove the marker only after I have rewritten the paragraph in my own words. Never remove these markers yourself.
- Never copy or closely paraphrase text from papers or other sources. Direct quotes must be in quotation marks with a citation, and should be rare. Everything taken over literally or in meaning must be marked as such (required by the signed declaration).
- Clearly separate my contribution from prior work. Never let prior work sound like mine, or my work sound like it was done by others.

## AI-use log
After each task, append one line to `ai_use_log.md`:
`YYYY-MM-DD | chapter/section | what you did (outline / feedback / explanation / draft / translation / LaTeX fix / script)`
The chair's declaration states the work was done without outside help, and neither guideline mentions AI. Provisional decision until I confirm with the supervisor: the official declaration stays unmodified, and the front matter gets a separate short "Use of AI tools" statement, written by me from this log. [RECORD THE SUPERVISOR'S ANSWER HERE.] Keep the log factual and short.

## Citations — strict rules
- Only cite keys that already exist in `thesis/literature.bib`. Check with `grep` before using a key.
- Never invent bibliography entries, authors, years, dataset sizes or paper results. When I ask you to add or fix an entry, take every field from the publisher page, the paper itself or official documentation, leave out fields you cannot verify (e.g. no guessed year), say where each field came from, and keep a backup of the file before editing.
- Only attribute a claim or a number to a paper if I have provided that paper or notes on it. If unsure what a paper says, ask.
- If a sentence needs a source I don't have, write `\todo{cite: <type of source needed>}` and list it in your summary.
- Every non-obvious factual claim needs a citation or must follow from my own results.

## Facts, numbers and reproducibility
- Every number about my experiments must come from `results/`. Say which file it came from.
- Every fact about the dataset (size, capture process, labels, splits, preprocessing, metadata, source link) must come from the data files, `code/` or official dataset documentation I provide, never from memory.
- Descriptions of the method must match what `code/` actually does. If the code and my notes disagree, ask me instead of guessing.
- Tables and figures are produced by scripts in `scripts/`, not typed by hand.
- All parameters needed to reproduce each experiment must be stated in the thesis (chair requirement).
- Report numbers with consistent precision and units throughout.

## Defensibility
Write every chapter as if the examiners will question each sentence. The chair grades correctness of statements, critical discussion, limitations, generalisation, and consideration of alternative strategies.
- Every design decision needs a stated reason: why this method, dataset, metric, baseline or hyperparameter, and which alternatives were considered.
- Claims must be no stronger than the evidence. Use "significant" only for statistical significance. Don't generalise beyond the data and setup tested.
- Report variability (e.g. mean ± std over seeds or folds) where it applies, and state the number of runs.
- Include negative and unexpected results; don't hide them.
- State limitations and threats to validity honestly, and discuss how the approach could generalise or be extended.
- Continual-learning and few-shot evaluation must be defensible. Make sure the thesis states: the task or dataset order and whether results depend on it; how forgetting is measured on earlier tasks; lower and upper reference points (e.g. sequential fine-tuning and joint training) where they apply; the number of shots and how support sets were sampled, with variability across different samples; and which free-text prompts were used for training and evaluation, and whether results depend on prompt wording. If any of these is missing or doesn't apply, ask me rather than assume.
- When you find a weak point an examiner could attack, flag it as `\todo{defense: ...}` and mention it in your summary.

## Writing style — must read as careful human academic writing
The goal is clear, precise, concise writing in my voice. Good human writing is specific and plain; generic, inflated prose is what makes text look machine-generated. The chair gives style, syntax and punctuation high priority.

**Do**
- Make concrete, specific statements: names, numbers, conditions, comparisons.
- One idea per paragraph, starting with a clear topic sentence.
- Vary sentence length and structure naturally. Short sentences are fine.
- Prefer verbs over nominalisations ("we compared", not "a comparison was performed") and active voice where natural.
- Use plain words. Use technical terms only where needed, and define them.
- Hedge once, where uncertainty is real ("suggests", "may"), not in every sentence.
- Let paragraphs end when the point is made.

**Don't**
- Inflated or cliché vocabulary: delve, crucial, pivotal, vital, paramount, leverage, harness, foster, showcase, underscore, highlight (as filler), seamless, robust (unless a technical meaning), comprehensive, holistic, intricate, nuanced, multifaceted, landscape, realm, tapestry, journey, cutting-edge, groundbreaking, game-changer, novel (unless truly new and justified).
- Filler phrases: "It is important to note that", "It is worth mentioning", "In today's rapidly evolving…", "plays a crucial/key role", "paves the way", "a testament to", "in the realm of", "when it comes to", "This highlights the importance of".
- Formulaic patterns: lists of three by habit; repeated "not only… but also"; "X is not just Y, it is Z"; rhetorical questions; colon reveals; every paragraph ending with a summarising or moral sentence; chains of "Moreover", "Furthermore", "Additionally".
- Em dashes as a habit, excessive bold or italics, and bullet lists where prose belongs.
- Repeating the same point in different words; empty signposting beyond one short sentence at chapter starts.
- Overclaiming or promotional tone about my own work.

**Sentence and paragraph rules** (derived from the Ch. 1 revision, 2026-10-25). Three tiers; don't apply tier 3 as if it were tier 1.

*Tier 1 — always*
- Nothing inserted between subject and verb or between a verb and its number; definitions get their own sentence or follow the main clause with "where …" (not "a mean DSC, the overlap between …, of 70.85 %").
- Every "this", "such a", "it" has its referent in the preceding sentence; never across a paragraph break or at a section start.
- Modal verbs no stronger than the argument ("has to" only for real necessity; otherwise "would have to", "can").
- No term before it is introduced, in text, captions and figure labels alike (e.g. "strategy", $k$, "control task").
- General claims state the condition under which they hold (e.g. "fewer volumes mean fewer updates" only with a fixed number of epochs).
- Claims about prior work match how Ch. 2 and `paper_notes/` describe it; check before generalising over several works.
- A sentence starting with a cross-reference uses `\Cref`.

*Tier 2 — depends on the chapter*
- Detail belongs where it is defined or used: Introduction and problem statement stay conceptual; Method and Experiment & Results give every parameter the text uses; the complete parameter lists may go to the appendix (decided 2026-11-02, chair Sec. 1.9: technical details in the appendix).
- A caption contains what is needed to read the figure, using only terms already defined: short in Ch. 1; self-contained in results chapters (metric, task order, $k$, number of runs). Figures don't repeat a paragraph or contradict the text's definitions.
- Each point once within an argument and across neighbouring paragraphs; deliberate recaps are expected in chapter openings, Discussion and Summary.
- Each definition in one place; later chapters may remind in a half-sentence with a reference, never redefine differently.

*Tier 3 — preferences*
- Two sentences instead of a semicolon when the clauses are separate statements; keep a semicolon for short, tightly linked clauses. Don't let splitting make the prose choppy.
- Subject first; avoid long participial openers and fronted clauses that hide the main claim.
- Say what is actually measured (a property of a structure, not the structure); no clumsy doubles.
- Paragraph openings pick up the previous paragraph's end, and a section opening continues from the previous section (most important in Ch. 1, 2, 7, 8; Method and Results sections may open with a plain statement of scope).
- Claim → reason → definition or detail; a definition does not interrupt an argument.
- Define positively and leave contrasts to the chapter that covers them (except Ch. 2 and 3, where the contrast is the content).

## Consistency across the whole thesis
- Terminology: one term per concept, used everywhere (see list below). Add new terms when introduced.
- Notation: one symbol per quantity, defined before first use, listed in the table of notation.
- Person: "we" for my own work and decisions ("we propose", "we evaluate"); passive only where the actor doesn't matter ("the volumes were resampled to…"). Never "I".
- Spelling: British with -ise endings (e.g. normalisation, generalisation, analyse, labelled, behaviour, modelling). Keep established names and quoted titles in their original spelling. Tense: present for describing the method and what results show; past for what was done in experiments.
- Acronyms defined once at first use in the main text [using `\gls{}` / `\acrshort{}` if glossaries is used].
- Figures and tables share one visual style: fonts, colours, axis labels with units, self-contained captions.
- Cross-references with `\autoref{}` / `\figurename~\ref{}` and `~\cite{}`. One sentence per line in `.tex` files.

## What each chapter must deliver
- **Introduction:** problem statement, motivation, objectives, main contributions, connection to prior work with citations, thesis outline. Understandable for readers outside the field (chair).
- **State of the Art:** for each reviewed work, its main findings, dataset (number of samples, groups/labels), methods and best results; group works by theme and compare them critically; a summary table of all reviewed works (supervisor); end with the gap this thesis addresses.
- **Theoretical Background:** concepts relevant to the problem, the ML/DL methods used, evaluation metrics, with figures explaining concepts and architectures (supervisor). Readers are experts (chair): explain what is needed to understand my work, cite standard textbook methods instead of re-deriving them.
- **Data Description:** number of samples, how the data was captured, link if open source, metadata summary table, figures of the data and its distributions (supervisor); splits, preprocessing, quality issues, licensing/ethics where relevant.
- **Method:** what I did and why; algorithms as language-independent pseudocode with complexity, runtime and memory (chair); justified design choices; enough detail to reproduce.
- **Experiment & Results:** setup, the parameters the text uses (complete lists in Appendix A), baselines, metrics and why they fit; results with the conclusion of each experiment (supervisor); bar plots where tables are dense.
- **Discussion (compact):** what spans all experiments: answers to each research question, comparison with prior work, merits and limitations, threats to validity, generalisation and extensions. Don't repeat the per-experiment conclusions.
- **Summary:** most important results, stating clearly which results are my original work; 3–4 pages (chair); answers each research question; future work; no new results.

Every research question raised in the Introduction must be answered explicitly in the Discussion and Summary.

## Revising existing drafts (any finished draft; no longer chapters 1 and 2, which are redrafted, decision 2026-10-22)
1. **Diagnose first, no edits.** Review the chapter against the guidelines, this file and the section checklist below. Output an issue list grouped as structure, content and argument, citations, and language, each with file and line and a severity (must fix / should fix / minor).
2. **I decide** which issues to address.
3. **Fix in order:** structure → content and argument → citations → language. Never polish sentences in a section whose structure may still change.
4. **One section at a time.** Show proposed changes or a revised outline first; edit only after I approve. Drafted text gets `% CLAUDE-DRAFT`.
5. Chapters 1 and 2 get a final revision after the results are finished, so that objectives and contributions match what was actually achieved.

## How to work with me
- Propose an outline before drafting any new section and wait for my approval.
- Work on one section at a time, never a whole chapter in one go.
- Make minimal, targeted edits. Don't reformat or rephrase text you weren't asked to touch.
- Mark anything uncertain with `\todo{}` rather than guessing.
- Be direct in feedback. Tell me when an argument is weak, unclear or unsupported; don't flatter.
- Don't run git commits; I review the diff and commit myself.
- End every task with a short summary: what changed, open `\todo`s, issues I need to verify, and the line added to `ai_use_log.md`. Before the summary, update `thesis_tracker.md` (new or resolved defense points and open items; rerun `python scripts/list_todos.py`).

## Review levels
Reviews happen at three levels. In every review, report issues only; don't edit unless I ask.
1. **Section review** — after I have rewritten a section (no `% CLAUDE-DRAFT` left in it). Run the checklist below on that section only. Keep the report short.
2. **Chapter review** — when all sections of a chapter have passed section review. Check what single sections can't show: does the chapter deliver everything required, do the sections connect without gaps or repetition, is terminology consistent across sections, does it fit the page budget, and does it link correctly to earlier and later chapters?
3. **Final review** — when the whole thesis is complete, following `FINAL_REVIEW.md`.

After a chapter passes chapter review, update its status in the chapter table to "Reviewed".

## Section review checklist (aligned with the chair's grading criteria)
1. Does it deliver what the chapter must deliver (see above) and keep the common thread to the research questions?
2. Correctness: is every claim supported by a citation or my own results? Are definitions precise?
3. Are all numbers traceable to `results/` or the data?
4. Is every design choice justified, with alternatives considered? What would an examiner ask?
5. Consistency: terminology, notation, tense, person, figure style.
6. Compactness: any repetition, filler or vague sentences to cut?
7. Comprehensibility and style: any sentence that breaks the writing style rules? Check the tier-1 sentence and paragraph rules explicitly (insertions, referents, modal strength, terms before introduction, conditions of claims, prior work); report tier-3 cases only where they hurt readability.
8. Formal rules: figures, captions, references, notation, as in "Formal requirements".
9. Any `% CLAUDE-DRAFT` paragraphs I still need to rewrite?

## Terminology and notation
Provisional choices; change them here if I decide otherwise, then apply everywhere.
- **continual learning** — not "lifelong learning" or "incremental learning" (unless citing a paper's own term)
- **catastrophic forgetting** — loss of performance on earlier tasks after training on new ones
- **few-shot** — training or adaptation with a small number of labeled examples per task; always state the number of shots
- **free-text promptable segmentation** — segmentation guided by a free-text prompt naming the target structure; always "free-text promptable", not "text-guided" or "language-driven"
- **universal segmentation model** — one model for many anatomical structures and/or modalities [CONFIRM DEFINITION]
- **task** — one training stage on one target structure (one text prompt) of SKM-TEA in the continual-learning sequence; the model is trained on task 1, then task 2, and so on. In this thesis a task is not a dataset (the six tasks share one dataset)
- **task order / task sequence** — the order in which the tasks are trained; use these two terms only (not "ordering"). The two orders used are **original** and **reverse**
- **adaptation** — performance on the current task after training on it. Metric "Adaptation": mean of the diagonal a_{i,i} of the evaluation matrix, i.e. the a_{k,k} term of the intransigence measure of Chaudhry et al. (2018), reported without its joint-training reference. Not "learning accuracy" or "plasticity" (plasticity is the broader property; intransigence needs the reference)
- **joint fine-tuning** — the upper reference: the pretrained model fine-tuned on all six tasks at once (full split and each k). "Joint training" only when describing a related work's reference or the general concept (decided 2026-10-27)
- **Pretrained model (reference row)** — the same metrics computed for the never-updated pretrained model, one row per task order; not a strategy
- **retention** — performance kept on earlier tasks after training on later ones, and on the control task; a property, not a metric: measured by Final Forgetting (within the sequence) and the control-task drop (outside it) (decided 2026-10-22)
- **transfer** — forward transfer: performance on a task before it is trained, metric Transfer (ZSCL); backward transfer appears as negative Final Forgetting (Chaudhry) and has no metric of its own (decided 2026-10-22)
- **families (of continual-learning methods)** — replay, regularisation, parameter isolation (De Lange) and, for vision–language models, multimodal replay, cross-modal regularisation, parameter-efficient adaptation (Liu et al.). Not "groups", "paradigms" or "categories", except when quoting a paper (decided 2026-10-25)
- **primary / secondary metrics** — primary: Adaptation, Final Forgetting, control-task drop; secondary: Final Performance, Transfer. ZSCL's Avg. is not reported and is named only by ZSCL's own term, not as "Average Performance" (decided 2026-10-22; name 2026-11-02)
- **DSC** — Dice similarity coefficient (`\gls{dsc}`), not "Dice score". Own results as fractions with three decimals (0.979); values quoted from a paper keep that paper's % form (10.72 %)
- **background shift** — in continual segmentation, a structure that is foreground in the masks of one task is labelled as background in the masks of another (term cited to MiB, Ch. 2.4; decided 2026-10-27). Does not arise in this thesis (one binary mask per text prompt). Not "background conflict"
- **control task** — a held-out task that is never trained on and is used only to measure the loss of pretrained ability (AeroPath, prompt "lung", test split). Term follows SPU's "control set". Not "retention task" and not "zero-shot" (lung is a known concept for VoxTell; AeroPath was held out in the paper (v1.0) but is among the training sources of the checkpoint we use, v1.1, GitHub issue #15; decided 2026-11-07). "Held-out" means never trained on in our adaptation
- **control-task drop** — Dice on the control task of the pretrained model minus that of the final checkpoint; absolute, positive = loss. Not "retention drop"

Strategies (decided 2026-10-18; names describe the mechanism, not a CL scenario):
- **strategy** — one of the six approaches evaluated in this thesis: sequential fine-tuning (the baseline) and the five **continual-learning strategies**; "continual-learning strategy" means the five only (decided 2026-10-31, Ch. 5 opening). **method** only for published algorithms (e.g. the original ZSCL). **configuration** — a strategy with its settings (e.g. rank r, k shots). Not "mechanism" (author 2026-10-30): published work is a "method", ours a "strategy"
- **sequential fine-tuning** — all parameters trained on each task in turn, no continual-learning mechanism (code `naive_sequential_finetuning`). The **baseline**; never "lower bound" (it has the highest Adaptation). Table/figure label: "Seq. fine-tuning". Not "naive", "full fine-tuning", "FFT" (except inside a related work's description)
- **task-specific LoRA** — one LoRA adapter per task, selected by the task identity at inference (code `lora`, folder `task_specific`). Always state the rank r. Not "TIL-LoRA"
- **shared LoRA** — one LoRA adapter shared by all tasks (code `shared_lora`). Always state the rank r. Not "CIL-LoRA"
- **shared LoRA with replay** — shared LoRA plus a replay memory of samples of earlier tasks only; the control task stays held out (rerun `exp_20261023_014438_55e6abcf`, option c, switched 2026-10-26; the earlier run with control-task volumes is not reported). Label: "Shared LoRA + replay"
- **distillation-based strategy (adapted from ZSCL)** — this thesis's adaptation of ZSCL as evaluated: all parameters trained, plus feature distillation from the frozen pretrained model on current-task data; no reference dataset. The weight ensemble is reported as an additional evaluation, not as part of the strategy (renamed 2026-10-21, kept after the reruns 2026-10-26, `thesis_notes.md` §1). Full name at first use: "distillation-based strategy (adapted from ZSCL)"; afterwards "distillation-based strategy". Table/figure label: "Distillation-based". Never "ZSCL-based"; plain "ZSCL" only for the original paper
- **prompt-tuning strategy (adapted from CPE-CLIP)** — this thesis's adaptation of CPE-CLIP as evaluated: all pretrained weights frozen; trained are learned prompt tokens appended to the cross-attention memory of the first prompt-decoder layers plus a meta-net that shifts the text query. Per-task gradient scaling is active on tokens and meta-net in the reported run; the earlier run without it is the scaling ablation (renamed 2026-10-21, name kept after the reruns 2026-10-26 because it describes the mechanism, `thesis_notes.md` §1). Full name at first use: "prompt-tuning strategy (adapted from CPE-CLIP)"; afterwards "prompt-tuning strategy". Table/figure label: "Prompt tuning". Never "CPE-CLIP-based"; plain "CPE-CLIP" only for the original paper. Here "prompt" always means the learned prompt tokens, never the text prompt
- **task identity / one parameter set** — only task-specific LoRA uses the task identity beyond the text prompt, to select its adapter; all other strategies use **one parameter set for all tasks**. The text prompt names the target structure in every strategy. The term "task-aware inference" is no longer used (dropped 2026-10-31: defined in Ch. 5.1 but used nowhere else). The setting is described as closest to task-incremental learning (Ch. 5.1; decided 2026-10-26, as C²GR names its text-prompted setting; reasoning revised 2026-10-31 after van de Ven 2025 Sec. 2.4): with one fixed text prompt per task, the prompt identifies the task, so the model never has to infer it (not CIL) and always knows which task an input belongs to (not DIL). Otherwise use TIL/CIL/DIL only to describe related work in its own terms
- **learned prompt tokens** — the trainable vectors of the prompt-tuning strategy; **text prompt** — the free-text input naming the target structure. Never a bare "prompt" where both are possible
- [Symbol]: [meaning]
