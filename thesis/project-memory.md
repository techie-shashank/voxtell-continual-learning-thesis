# Thesis Project Memory

This file is the single, repository-visible memory for the thesis. It combines persistent decisions, session history, progress, evidence gaps, open questions, and planned tasks. Update it after meaningful work; do not turn assumptions into scientific facts.

## Scope and Source of Truth

- Master's thesis on continual learning for promptable universal 3D medical image segmentation in few-shot settings.
- Markdown is the thesis source of truth; LaTeX conversion comes later.
- Scientific ownership remains with the author. Missing evidence is recorded as an open question rather than inferred.

## Repository Decisions

- Zotero bibliography is maintained in `thesis/references.bib` using BibTeX.
- Keep Zotero `file` fields for now, including local paths.
- Keep both `thesis/initial_proposal/Shashank_masters_thesis_proposal.docx` and its PDF snapshot.
- Keep `presentation/shashank_master_thesis.pptx` and `results/few_shot_cl_results_fixed.xlsx`; the user confirmed they do not contain large binary payloads.
- Root `.gitignore` excludes local datasets, model weights, generated experiments and outputs, environments, caches, and private source documents under `thesis/sources/`.
- `code/` is a Git submodule; code changes are versioned separately from the thesis repository.
- This file, `thesis/project-memory.md`, is the canonical memory location for both persistent and session information.

## Progress

- Thesis scaffold exists: `thesis/chapters/`, `evidence/`, `figures/`, `initial_proposal/`, `notes/`, `tables/`, `outline.md`, and `references.bib`.
- Added `thesis/evidence/evidence-ledger.md` as the evidence and reproducibility tracking template.
- Root `.gitignore` was created and representative ignore behavior was validated.
- `.github/` contains thesis instructions, planner/reviewer/evidence-auditor agents, and planning, drafting, revision, results-audit, and memory-maintenance prompts.
- `thesis/outline.md` exists but is currently empty.
- `thesis/references.bib` contains Zotero-exported entries with `file` fields; they are intentionally preserved.
- Root repository has no commits yet.
- Pre-commit audit found no obvious credentials in readable thesis and configuration text; representative datasets, outputs, experiments, and private source paths remain ignored.

## Session History

### Repository setup

- Confirmed that the proposal PDF is a snapshot of the DOCX and both should be retained.
- Confirmed that the presentation and results workbook should be retained.
- Established that private PDFs may be stored locally under ignored `thesis/sources/`, while the bibliography remains trackable.
- Added explicit memory-maintenance guidance to `.github/copilot-instructions.md`.
- Added `.github/prompts/maintain-thesis-memory.prompt.md`.
- Changed the memory design from external repository memory as the primary location to this tracked repository file as the single source of truth.

## Evidence Gaps and Open Questions

- The thesis outline has not yet been extracted from the proposal.
- Dataset versions, splits, case counts, preprocessing, training parameters, seeds, hardware, software environment, checkpoints, runtime, memory consumption, and computational complexity still need to be recorded where applicable.
- Bibliography metadata should be reviewed for correctness, but Zotero `file` fields should remain unless the author requests otherwise.
- Before the first commit, review tracked files for credentials, private paths, and other sensitive content.
- The results workbook was locked by another process during the automated scan; close it and perform a final manual review before staging.

## Planned Tasks

1. Review the initial proposal and extract factual objectives, research questions, methods, and planned experiments into `thesis/outline.md`.
2. Populate `thesis/evidence/evidence-ledger.md` with claims, citations, datasets, configurations, results, figures, tables, and reproducibility metadata.
3. Review bibliography metadata without removing Zotero `file` fields.
4. Review the initial tracked file set and create the first root commit.
5. Before drafting each section, consult this memory, the outline, evidence ledger, relevant results, figures and tables, and references.

## Maintenance Rules

- Record decisions, completed work, evidence discoveries, unresolved questions, and next steps after meaningful sessions.
- Keep persistent decisions, session history, evidence gaps, and planned tasks in their respective sections.
- Preserve the author's technical facts, values, citations, equations, terminology, and observations.
- Update `.github/` resources when the thesis workflow, terminology, evidence requirements, or author preferences change.
- Never invent scientific content, experimental results, citations, or missing metadata.
