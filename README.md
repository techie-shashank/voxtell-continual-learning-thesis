# VoxTell Continual Learning Thesis

This repository contains the working materials for a Master's thesis on continual learning for promptable universal 3D medical image segmentation in few-shot settings, using VoxTell.

## Repository structure

```text
thesis/          Markdown thesis source, proposal, references, evidence, and project memory
assets/          Thesis figures and other source assets
results/         Experimental result files
presentation/    Presentation material
code/            VoxTell implementation as a Git submodule
experiments/     Local generated experiment output (ignored by Git)
```

## Thesis workflow

Markdown is the thesis source of truth until the author performs the LaTeX conversion. Begin with [thesis/outline.md](thesis/outline.md), and use the [evidence ledger](thesis/evidence/evidence-ledger.md) to connect claims, results, figures, tables, citations, and reproducibility information to their sources.

The single repository-visible memory for persistent decisions, session history, evidence gaps, and planned tasks is [thesis/project-memory.md](thesis/project-memory.md). It is updated throughout the thesis workflow.

## References

The bibliography is maintained in [thesis/references.bib](thesis/references.bib), exported from Zotero in BibTeX format. Zotero `file` fields are currently preserved for local reference management.

## Code and experiments

The implementation and its installation, configuration, training, evaluation, inference, and continual-learning instructions are documented in [code/README.md](code/README.md). The `code/` directory is a Git submodule and is versioned separately from this thesis repository.

Datasets, model weights, local environments, generated experiment outputs, and private source documents are excluded by [.gitignore](.gitignore). Do not commit medical data, credentials, or other sensitive material.

## Writing standards

The workspace guidance and thesis-specific Copilot resources are in [.github/](.github/). They enforce evidence-grounded writing, consistent terminology and notation, reproducible reporting, and explicit handling of unresolved questions.
