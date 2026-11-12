# Proofread of Chapter 1 after the style pass

Reviewed file: `thesis/introduction.tex` (AFTER), compared with `reviews/voice/ch1_introduction_before.tex` (BEFORE). Line numbers refer to AFTER. Prose only; LaTeX comments, the old-notes block and the three intentional content changes were not reviewed.

## A1 Grammar, articles, agreement, tense, punctuation

1. **l. 201, should fix.** "summarises the results, answers the research question and outlines future work." This list has three items but no serial comma. It is the only list in the chapter the pass missed.
   Fix: "answers the research question, and outlines future work."

2. **l. 98, minor.** "The closest works either use a two-dimensional (2D) model with full training sets ... or a 3D model without text prompts". "either" comes before the verb, but the alternatives are the two objects, so the structure is not parallel.
   Fix: "The closest works use either a two-dimensional (2D) model with full training sets ... or a 3D model without text prompts."

3. **l. 150, minor.** "To separate the effect of fewer volumes from that of fewer updates, further runs keep the number of updates ..." The purpose clause dangles: the implied agent is "we", but the subject is "further runs".
   Fix: "To separate ..., we add runs that keep the number of updates of the full training split" or keep the BEFORE structure ("Further runs keep ... and so separate the two effects").

4. **l. 161, minor.** "Joint fine-tuning trains the model on all six tasks at once and was run with the full training split and with each $k$." Present and past tense are coordinated under one subject. Both tenses follow the rule (method in the present, what was done in the past), but together they read awkwardly. BEFORE kept them in two sentences.
   Fix: "Joint fine-tuning trains the model on all six tasks at once. It was run with the full training split and with each~$k$."

5. **l. 87, minor.** "On the other hand, they may also change less of what it knew." After "On the one hand ... On the other hand", the word "also" is redundant.
   Fix: drop "also".

## A2 Tier-1 rules

1. **l. 19, minor (referent).** "Masks can be drawn by hand. However, this is laborious, ..." "this" points to an action (drawing masks by hand), not to a noun in l. 18. In BEFORE, the clause after "but" sat in the same sentence, so the reference was clear. As a separate sentence after "However", the referent is weaker.
   Fix: "However, drawing them is laborious, since ..."

2. **l. 66, should fix (referent/attachment).** "... lower the zero-shot accuracy on data the model was not trained on~\cite{...}, which in our setting corresponds to a loss of pretrained ability." The "which" clause comes right after "data the model was not trained on" and the citation. It can be read as attaching to "data" instead of to the lowering of accuracy. BEFORE used a separate sentence ("In our setting, this corresponds ...").
   Fix: restore the separate sentence, or write "... not trained on~\cite{...}. In our setting, such a lowering corresponds to a loss of pretrained ability."

3. **l. 137–141 and l. 109/119, minor (term before introduction, already in BEFORE).** "strategies" and "continual-learning strategies" are used in the research question and objectives. The text never says that the strategies are sequential fine-tuning plus five continual-learning strategies. Contribution 2 (l. 178) then speaks of "five continual-learning strategies" as if the reader already knew this. The style pass did not cause this, but the chapter does not meet the CLAUDE.md term definition ("strategy" = the six approaches).
   Suggestion: add one sentence at l. 137, for example "We compare six strategies: ..." (without a colon reveal: "We compare sequential fine-tuning, the baseline, with five continual-learning strategies."). The author has to approve this, since it adds content.

4. **l. 58, minor (where-clause).** "We call the learning of one new structure a \emph{task}, where each structure is named by one text prompt." The "where" clause does not define anything in the main clause. It adds a separate statement, so it reads as loosely attached (see also B4).

No insertions between subject and verb and no over-strong modal verbs were found. ("has to" in l. 19, 60, and 61 states a real requirement of the setting.)

## A3 Terminology, banned words, formulaic patterns

1. **l. 99, minor.** "Moreover, none of them measures ..." There is only one "Moreover", so this is not a chain. But BEFORE joined the two claims with "and", and the new connective adds nothing.
   Fix: "None of them measures ...".

2. **l. 20, 49, 61, and 158, minor.** "In addition," now opens four sentences in the chapter, three of them in consecutive paragraphs of Sec. 1.1–1.2 (l. 20, 49, 61). In BEFORE they were "also" inside the sentence. This makes a repeated connective pattern of the kind CLAUDE.md warns against ("chains of Moreover, Furthermore, Additionally").
   Fix: go back to "also" in at least two places (for example l. 49 "New structures may also become relevant ..."; l. 158 "We also report two secondary metrics.").

3. **l. 160, minor.** "As reference points, we evaluate the pretrained model in the same way and use joint fine-tuning as the upper reference." "reference" appears twice in one sentence, which is a clumsy double (tier 3).
   Fix: "We evaluate the pretrained model in the same way as a reference point and use joint fine-tuning as the upper reference."

No banned vocabulary, filler phrases, colon reveals, or "not only ... but also" were found. Terminology matches the CLAUDE.md list: free-text promptable, control task, control-task drop, joint fine-tuning, sequential fine-tuning, task-specific/shared LoRA, learned prompt tokens, families, DSC.

## A4 Hard-to-read sentences

1. **l. 149, should fix (garden path).** "All strategies are trained with the full training split, and sequential fine-tuning, task-specific LoRA, and shared LoRA are also trained with $k = 5$, 10, and 20 volumes per task." After "the full training split, and sequential fine-tuning", a reader first takes "sequential fine-tuning" as a further object of "trained with". The merge also creates a sentence with two lists. BEFORE had two sentences.
   Fix: restore the split: "All strategies are trained with the full training split. Sequential fine-tuning, task-specific LoRA, and shared LoRA are also trained with ..."

2. **l. 40, should fix (length).** "The VoxTell authors attribute this low value to the small share of knee images in the training data and to structures missing from it, and they suggest adapting the model with a few labelled examples as future work~\cite[Sec.~6]{...}." The sentence has about 45 words and two separate statements, an attribution and a suggestion. "as future work" at the end attaches to "examples" first.
   Fix: "... and to structures missing from it. As future work, they suggest adapting the model with a few labelled examples~\cite[Sec.~6]{...}." (The citation can cover both. `paper_notes/voxtell.md` §8 places both statements on p. 8.)

3. **l. 50, should fix (long fronted clause).** "Although retraining VoxTell from scratch on its training data together with each new structure would be expected to preserve most of what it could segment before, training the published model took about six days on 64 NVIDIA A100 GPUs ..." About 25 words come before the main clause, so the main claim (the cost) arrives late. This is the tier-3 rule against long fronted clauses that hide the main claim. The voice-sheet concession pattern (1.5) is meant for short concessions. BEFORE used two sentences with "However".
   Fix: restore the two sentences, or shorten the concession: "Retraining VoxTell from scratch together with each new structure would be expected to preserve most of what it could segment before. However, training the published model took ..."

4. **l. 17, minor (length, merged definition).** "Medical image segmentation assigns every voxel ... or to the background, and the voxels assigned to a structure form its mask." The sentence has 35 words with an embedded "such as" aside, and the definition of "mask" is tacked on with "and". "its" refers back across the whole clause.
   Fix: restore the split ("... or to the background. The voxels assigned to a structure form its mask.").

5. **l. 145, minor (already in BEFORE, made more visible by the serial comma).** "cover replay, regularisation, and parameter-efficient adaptation, the three families of continual-learning methods ..." The appositive after a serial-comma list can be read as a fourth list item.
   Fix: "cover replay, regularisation, and parameter-efficient adaptation, which are the three families ..."

6. **l. 43–45, minor.** "These values can only be read out once the structures are outlined, and the SKM-TEA authors name manual outlining as one obstacle ..." The merge joins two separate statements, a fact and an attribution, with "and". BEFORE kept them apart. This is tier 3 (separate statements in separate sentences).

## B Meaning check

1. **l. 39, minor (evaluation added).**
   BEFORE: "its mean \gls{dsc} was 10.72\,\%, averaged over four cartilages and two menisci"
   AFTER: "however, its mean \gls{dsc} was only 10.72\,\% (averaged over four cartilages and two menisci)"
   "only" adds an evaluative intensifier that BEFORE did not have. It fits "this low value" in the next sentence and the paper ("the model struggles", `paper_notes/voxtell.md` §8), so the claim is supported. Still, it is a strengthening the pass was not meant to make. Keep it if the author agrees.

2. **l. 40, minor (citation scope changed).**
   BEFORE: "... structures missing from it~\cite[Sec.~6]{...}. As future work, they suggest adapting the model with a few labelled examples." (no citation on the second sentence)
   AFTER: one sentence, with the citation at the end covering both claims.
   The citation now also supports the future-work suggestion. According to `paper_notes/voxtell.md` §8 this is correct (both statements are on p. 8), so the change is an improvement. Note, however, that the notes give "p. 8" and not a section number. The author should check that "Sec.~6" is the right locator for both statements.

3. **l. 33, minor (added contrast).**
   BEFORE: "In both models, the structure to segment is not tied to an output channel ..."
   AFTER: "In both models, however, the structure to segment is not tied ..."
   "however" now presents the shared property as a contrast to the different prompt vocabularies. Factually nothing changed. Mentioned only because it adds a rhetorical turn; acceptable.

4. **l. 58, minor (definition changed in form).**
   BEFORE: "We call the learning of one new structure, named by one text prompt, a \emph{task}."
   AFTER: "We call the learning of one new structure a \emph{task}, where each structure is named by one text prompt."
   In BEFORE, "named by one text prompt" was part of the definition of a task. In AFTER it becomes a separate general statement ("each structure is named by one text prompt"), so it is no longer clearly part of the definition. The intended meaning (one task = one structure = one text prompt) survives, but less precisely.
   Fix: "We call the learning of one new structure, which is named by one text prompt, a \emph{task}."

5. **l. 160, none in substance.**
   BEFORE: "The pretrained model is evaluated in the same way and serves as a reference. As an upper reference, joint fine-tuning ..."
   AFTER: "As reference points, we evaluate the pretrained model in the same way and use joint fine-tuning as the upper reference."
   The meaning is kept; listed only to confirm it was checked. The style point is A3.3.

No numbers moved to a different referent, no hedges were lost, and no other attribution changed. The "may" in l. 49, 67, and 87 and "would be expected" in l. 50 are all kept.

## C Voice consistency

1. **l. 129 and 131, should fix (overused "To X, we Y").** Two of the first three sentences of Sec. 1.4 open with a purpose clause ("To study the research question, we use ..."; "To see whether the results depend on the order of the tasks, we train them ..."). A third follows in l. 150 ("To separate ..., further runs keep ..."). The voice sheet (1.1) says "Not in every sentence of a paragraph". The first one is also weak: "To study the research question" justifies nothing specific.
   Fix: l. 129 back to "We study the research question with VoxTell ... as the pretrained model ...", and keep l. 131.

2. **Sec. 1.1–1.2, minor ("In addition," as a habit).** See A3.2. Four sentences open with the same connective, which reads more formulaic than the rest of the chapter.

3. **l. 84–88, minor.** The "On the one hand ... On the other hand" pair, after the "When ..." opener, makes this short paragraph more rhetorical than the surrounding plain paragraphs. It is acceptable once (voice sheet 1.6), but together with the redundant "also" (A1.5) it reads heavier than BEFORE.

The rest of AFTER reads consistently: plain, medium-length sentences, "we" for decisions, and the present tense for the method.

## Counts

| Severity | Count |
|---|---|
| must fix | 0 |
| should fix | 6 (A1.1, A2.2, A4.1, A4.2, A4.3, C1) |
| minor | 19 (A1.2–A1.5, A2.1, A2.3, A2.4, A3.1–A3.3, A4.4–A4.6, B1–B4, C2, C3) |

B5 is a confirmation, not a finding.

**Total: must fix 0, should fix 6, minor 19.**
