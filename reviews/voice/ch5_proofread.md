# Proofread of the Ch. 5 voice proposal, 2026-11-12

Report from the proofreader subagent, saved by the main session. Counts: must fix 0, should fix 8, minor 14. No contradictions with Ch. 6 Sec. 6.1 or with background.tex beyond those listed.

Applied to `reviews/voice/ch5_method.tex` (15 fixes):
- (should) "It trains all parameters ..." pointed to "Each training sample": "Joint fine-tuning trains ...".
- (should, from split) "The others belong to ...": "The parameters that cannot be updated belong to ...".
- (should, from split) "In medical imaging, such constraints restrict what may be kept from earlier patients." was uncited (De Lange has no medical claim) and "such constraints" included storage: now "privacy rules may prevent storing the data and annotations of earlier tasks~\cite{zhang2023continuallearningabdominalmultiorgan}" (paper_notes: p. 1 abstract, p. 2). Author to approve.
- (should, from split) "The strategies therefore differ only in the cost of one iteration." contradicted replay adding iterations: "For a given $N_t$, ...".
- (should, pre-existing) Final Forgetting maximum "over all stages before the last" vs Eq. bg-forgetting (j = 1..T-1): corrected.
- (should) 17-word fronted purpose clause on random replay samples: back to the BEFORE sentence.
- (should, pre-existing) "except the two LoRA strategies" implied a best-validation evaluation of replay, which does not exist (ch6_components.tex): "except the three LoRA strategies".
- (minor) four serial commas; dangling "To obtain the binary prediction"; $\mathcal{S}$ at first use in running text; "whose template, CPE-CLIP, is listed by the survey ..."; "since the meta-net holds ...".

Not applied:
- (should) notation.tex l. 61 defines $\mathcal{S}$ as "continual-learning strategy", but it also covers sequential fine-tuning: should be "strategy" (author to approve; outside Ch. 5).
- (minor) tense of design justifications mixed ("We use ... because" vs "We chose ... because"): both acceptable.
- (minor) notation: bar for mean ($\bar{\vec f}$) and for teacher ($\bar q_{g,v}$); $q$ for query and distribution. Listed in notation.tex; changing symbols now would touch Ch. 3, 5 and the table of notation. Defence point rather than an edit.
