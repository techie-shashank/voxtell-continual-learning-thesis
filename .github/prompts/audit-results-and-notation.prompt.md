---
name: Audit Results and Notation
description: "Audit a thesis section for observation-interpretation separation, figure and table handling, notation consistency, and reproducibility gaps."
argument-hint: "Provide the section together with its equations, figures, tables, metrics, and notation list."
agent: "Thesis Reviewer"
---
Audit the supplied section without rewriting its scientific content.

Check:

- whether figures and tables are referenced before discussion
- whether observations are separated from possible explanations
- whether every non-universal symbol is defined and used consistently
- whether metric names, capitalization, and terminology remain fixed
- whether numerical claims match the supplied tables or results
- whether the method and experiment description contains the parameters needed for reproduction

Report concrete findings first. If information is missing, mark it as requiring author input rather than inferring it.