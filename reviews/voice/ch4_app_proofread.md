# Proofread of the Ch. 4 and Appendix A voice proposals, 2026-11-12

Report from the proofreader subagent, saved by the main session. All facts checked against results/data_stats, the annotation files, cl_metrics.csv, cl_differences.csv and the appendix tables: no mismatch. Ch. 4: must 0, should 2, minor 3. Appendix: must 1, should 5, minor 3.

Applied:
- Ch. 4: serial comma in the table caption; "VoxTell's training labels include ``lung'', in 3,427 training cases" (lower-case label as in the text prompt); App. A.4 citation added to the annotator sentence (a new claim; previously uncited).
- Appendix (must): "Its Final Forgetting of 0.354, ..., is lower only because ..." had an insertion between subject and verb: split.
- Appendix (should): "Sec. A.4 also uses its metrics" (ambiguous "its"); "the evaluation matrix of every reported run, from which ..." ("which" after "run", and the claim covered best-validation metrics that A.5 does not contain): now "gives, for every reported run, the evaluation matrix from which its metrics after the last epoch are computed"; "these results" across a paragraph break; "is not part of any experiment in that table" contradicted A.4 belonging to Sec. 6.2: back to "is not listed in Table 6.1"; repeated table pointers in A.3 and A.4 reduced.
- Appendix (minor): "analyses the effect" in the overview sentence.

Not applied:
- "For comparing the strategies with each other" (was "continual-learning strategies"): broader and more accurate (sequential fine-tuning uses the same split); kept.
- qDESS "two inherently registered 3D echoes" uncited: the preceding sentence cites SKM-TEA; left.
- "lower only because the ensemble learned less of each task": firm causal claim from the original text, supported in part by the diagonal (0.83 -> 0.00); for the author.
