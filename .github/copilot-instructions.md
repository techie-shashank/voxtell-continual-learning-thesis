# Thesis Workspace Guidelines

This workspace contains an English Master's thesis on continual learning for promptable universal 3D medical image segmentation in few-shot settings. The thesis is drafted in Markdown and will later be transferred to LaTeX by the author.

## Scientific Standards

- Preserve the author's scientific ownership. Do not invent contributions, explanations, results, citations, equations, datasets, or numerical values.
- Use formal, objective, precise, concise, and evidence-based academic English.
- Identify unsupported claims, logical gaps, missing citations, contradictions, and ambiguous terminology instead of silently accepting them.
- Ask the author for missing information rather than guessing.
- Preserve all technical facts, numerical values, citations, equations, symbols, and observations when revising text unless the author requests a scientific change.

## Structure and Scope

- Organize explanations from general to specific, with one central idea per paragraph and a clear transition between subsections.
- In the introduction, provide enough context for readers unfamiliar with the topic.
- In the main theoretical section, define and motivate concepts but cite established methods concisely instead of explaining them at textbook length, as required by the supervisor.
- Keep the theoretical and practical parts approximately balanced.
- Describe practical algorithms and data structures independently of programming language, including pseudocode or flowcharts where appropriate.
- Report computational complexity, runtime, memory consumption, parameters, and other information required to reproduce experiments.

## Style and Consistency

- Maintain fixed terminology, capitalization, metric names, notation, and symbol definitions throughout the thesis.
- Use present tense for established facts, definitions, figures, and tables. Use past tense for implementation, training, experiments, and observations.
- Separate experimental observation, evidence, and possible explanation. Use cautious language for interpretations.
- Refer to each figure or table before discussing it, explain meaningful trends, and cite non-original sources in the caption and bibliography.
- Avoid conversational, promotional, exaggerated, or subjective language. Avoid words such as "clearly", "obviously", "remarkably", "groundbreaking", "revolutionary", "game-changing", and "very" unless justified by evidence.

## Workflow

- Treat Markdown files as the source of truth until the author performs the LaTeX conversion.
- Prefer small, reviewable edits and preserve the existing structure.
- Before drafting a new section, use the author's notes, outline, results, figures, tables, and references as the evidence base.
- When evidence is insufficient, return a concise list of questions or evidence gaps rather than filling them with general knowledge.

## Memory and Workspace Maintenance

- Consult `thesis/project-memory.md` when beginning a thesis-related session.
- Update it after meaningful decisions, completed setup steps, evidence discoveries, unresolved questions, and changes to the writing workflow.
- Keep `thesis/project-memory.md` as the single repository-visible memory for both persistent and session information.
- Keep current progress, planned next steps, repository decisions, and evidence gaps distinct; do not use memory to turn assumptions into scientific facts.
- Review `.github/` resources when the thesis workflow, terminology, evidence requirements, or author preferences change; update or add the smallest relevant resource.
- Preserve Zotero-exported `file` fields unless the author explicitly requests their removal.