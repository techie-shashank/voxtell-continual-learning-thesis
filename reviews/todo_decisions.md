# Decisions before the voice pass (2026-11-12)

Write your answer in the last column (OK = take my recommendation). Then the content is frozen and the voice pass runs without stopping.

Recommendation codes:
- **(a)** The sentence the marker is attached to already states the point. Remove the marker; the question and answer stay in `thesis_tracker.md` for the oral defence.
- **(b)** The text needs your reason or a check before the marker can go.
- **(c)** A source is needed (bib agent running).

## 0. Open questions on Ch. 1 (proposal `reviews/voice/ch1_introduction.tex`)

| # | Question | My recommendation | Your answer |
|---|---|---|---|
| 0.1 | l. 103 used "control task" before Sec. 1.4 introduces it. Change "our control task builds on this idea" to "our evaluation builds on this idea (Sec. 1.4)"? | Yes (tier-1 rule) | |
| 0.2 | Drop "With a fixed number of epochs, fewer volumes also mean fewer updates" in l. 156 (repeats l. 90)? | Yes | |
| 0.3 | Remove the D46 marker (l. 157); the reason is stated in Sec. 6.8, D46 stays in the tracker? | Yes (= row 18 below) | |
| 0.4 | Update objective 1 in CLAUDE.md to the serial comma, so both stay identical? | Yes | |
| 0.5 | Delete the commented-out old notes in `introduction.tex` l. 211–294 (not in the PDF)? | Yes, git keeps them | |
| 0.6 | Delete l. 172–173 "Each configuration was trained once, …" (technical detail, repeated in 6.8)? | Your call. Keeping it is defensible, because the chair wants limitations visible early | |

## 1. Author todos (only you can answer)

| # | Where | What is needed | Options | Your answer |
|---|---|---|---|---|
| 1 | `method.tex` l. 227 | Confirm the reason for choosing CPE-CLIP and ZSCL as templates: "both were developed for continual learning of a pretrained vision–language model, and CPE-CLIP for the few-shot setting." | (i) confirm as is; (ii) give me your actual reason (for example, how you found them), and I phrase it | |
| 2 | `method.tex` l. 310 (D56) | Why the learned prompt tokens of layer $L_p$ stay in the keys and values of all later prompt-decoder layers (the code does this, `cpe_clip/transformer.py:117-131`; you said it is intended) | (i) you give the reason; (ii) if there was no specific reason: state it as a design choice that was not tested ("We did not test removing them from the later layers.") and keep D56 as a defence point | |
| 3 | `related_work.tex` l. 276 (tracker 2026-10-28) | Are the meta-net and the gradient scaling a new method? | Suggestion (yours to accept or change): no. They are the adaptations needed to apply CPE-CLIP to VoxTell, evaluated only within the prompt-tuning strategy (scaling ablated in App. A) and not claimed as a contribution; this matches contribution 2. Then (a): remove the marker, answer in the tracker | |

## 2. Citations (bib agent done; two entries added to `literature.bib`, backup `thesis/bib_backups/literature_20261112_154147.bib`; diff checked: additions only)

| # | Where | Result | Recommendation | Your answer |
|---|---|---|---|---|
| 4 | `experiment_results.tex` l. 65 | All four values verified in the nnU-Net v2 code at tag v2.7.0, the version used in the runs (`nnUNetTrainer.py` l. 153, 552–554; `polylr.py` l. 5, 18). The paper (Nature Methods 2021, existing key `isensee2018nnunet…`, already the peer-reviewed version) gives momentum 0.99 with Nesterov and the poly schedule with exponent 0.9, but **not** the weight decay 3e-5. New entry `isensee2026nnunet` (`@online`, GitHub v2.7.0) | Replace the todo with `~\cite{isensee2026nnunet}` (the code is the only source for all four values) | |
| 5 | `related_work.tex` l. 166 | Bommasani et al., "On the Opportunities and Risks of Foundation Models", arXiv 2108.07258 (no peer-reviewed version exists; the report is cited as arXiv by its authors). New entry `bommasani2021opportunities`. Source, p. 3: "A foundation model is any model that is trained on broad data (generally using self-supervision at scale) that can be adapted (e.g., fine-tuned) to a wide range of downstream tasks". **Our sentence is a close paraphrase of this.** | Choose: (i) quote it in quotation marks with `\cite[p.~3]{bommasani2021opportunities}`; or (ii) attribute it explicitly: "Following Bommasani et al.~\cite[p.~3]{…}, we call a model a foundation model if …" (the definition is then marked as taken over in meaning, as the declaration requires). I recommend (ii) | |

## 3. Defence todos

| # | Where | Point (tracker ID) | Rec. | Note | Your answer |
|---|---|---|---|---|---|
| 6 | `experiment_results.tex` l. 76 | Main-comparison ranks chosen on test results (D21) | (a) | Sentence states the bias and reports r = 8 | |
| 7 | l. 157 | Distillation weight λ = 0.01 untuned (D25, D47) | (a) | Stated in the sentence | |
| 8 | l. 158 | Distillation term not logged separately (D47) | (a) | Stated in the sentence | |
| 9 | l. 175 | Replay lowers the control-task drop without control samples; explanation untested; may depend on task order | (a) | The sentence hedges it and names the order dependence | |
| 10 | l. 216 | Best-validation checkpoint with a noisy validation loss (D15) | (a) | Reported only as an additional evaluation | |
| 11 | l. 237 | "Conclusion drafted from Claude's suggestions accepted by the author" | (b) | The marker sits on a **comment line** (not in the PDF). Delete the comment line. Your part: make sure you can defend this conclusion in your own words (part of your read-through) | |
| 12 | l. 276 | Shared configuration understates task-specific LoRA on patellar; updates and LR schedule confounded (D16, D38) | (a) | Stated in the sentence | |
| 13 | l. 341 | Updates separated only at k = 5; one support set; one seed; LR untuned (D8, D9) | (a) | Stated in the sentence | |
| 14 | l. 383 | Rank and γ_r confounded (D20) | (a) | Stated in the sentence | |
| 15 | l. 398 | r = 1024: control-task drop not saturated (D37) | (a) | Stated in the sentence | |
| 16 | l. 439 | Paired intervals exclude zero for a pure re-initialisation difference (D40) | (a) | Stated in the sentence | |
| 17 | l. 530 | Zero-initialisation and training-setup explanations untested (D66) | (a) | Tests named; future work in the Summary | |
| 18 | l. 569 | Ranks chosen on test results, repeated in 6.8 (D21) | (a) | | |
| 19 | l. 570 | α and dropout differ between the LoRA variants (D19) | (a) | | |
| 20 | l. 583 | VoxTell v1.1 lists Stanford Knee (= SKM-TEA) among training sources | (a) | Stated in 6.8; volumes unknown, nothing more can be said | |
| 21 | `introduction.tex` l. 157 | Few-shot runs only for three strategies (D46) | (a) | = question 0.3 | |
| 22 | `method.tex` l. 189 | No augmentation, negative prompts, deep supervision (D17) | (a) | | |
| 23 | l. 206 | No per-strategy tuning of LR and epochs (D16) | (a) | | |
| 24 | l. 228 | Alternatives within each family not evaluated (D23) | (a) | | |
| 25 | l. 277 | Task-specific LoRA: control-task drop zero by construction, Final Forgetting near zero (D14). The marker asks to "state this wherever its results are compared" | (b) | I check Ch. 6 and the Summary for every comparison that uses these two values and list any sentence that lacks the qualification; then remove the marker | |
| 26 | l. 299 | Random replay samples, no selection criterion | (a) | | |
| 27 | l. 335 | Lower bound 0.25 of the gradient scale, set without a specific reason (D55) | (a) | | |
| 28 | l. 382 | Our weight ensemble differs from ZSCL's code (D57) | (a) | | |
| 29 | `appendix.tex` l. 43 | Software versions not logged per run (D32) | (a) | | |
| 30 | `appendix.tex` l. 119 | Components tested once each, one task order | (a) | | |

## 4. Not marked in the text, still open in the tracker

| # | Point | Status | Your answer |
|---|---|---|---|
| 31 | D34: does cropping to the non-zero region remove labelled voxels? | Unverified; needs the volumes on the HPC. Either check it (a short script on the HPC) or answer orally | Recommended oral answer below |
| 32 | D65: seq. FT k = 5 and joint FT k = 5 both have 300 updates, but control-task drop 0.010 vs 0.733 | Open. Check that no sentence in 6.8 or the Summary contradicts it (for example "the control loss comes from fine-tuning all parameters, not from the task sequence"). I can check and list | Checked 2026-11-12: no sentence contradicts it. Recommended oral answer below |
| 33 | D70: why the weight ensemble learned so little | Open, appendix only; answer orally | Recommended oral answer below |

### Recommended answers (Claude's suggestions, 2026-11-12; yours to accept, change or reject)

**D34 (cropping).** What the code does (`code/src/data/preprocess.py:19`, `code/src/data/dataset.py:60-74`): the bounding box is computed from the image with nnU-Net's `crop_to_nonzero`, and every mask is cropped to the same box, in training and in testing. A labelled voxel outside the box would therefore be missing from both training and evaluation, not counted as an error. The box contains every voxel with non-zero intensity, and a labelled cartilage, meniscus or lung voxel lies inside the anatomy, where MR and CT intensities are non-zero, so a loss could only occur where the image is exactly zero (for example padded borders). Suggested oral answer: "The crop is computed from the image and applied identically to image and mask. It can only remove voxels where the image is exactly zero, which a labelled structure inside the anatomy is not expected to have; we did not count it per volume." If you have half an hour on the HPC, a script that compares the foreground voxel count of each mask before and after cropping turns this into a checked fact.

**D65 (300 updates, different control-task drop).** The text makes no cross-strategy claim: Sec. 6.4 l. 331 says only that the control-task drop of joint fine-tuning rose with its number of updates, and l. 339 compares sequential fine-tuning with itself (k = 5 with 50 vs 1,080 updates per task). Suggested oral answer: "Within each strategy, the control-task drop rose with the number of updates. Across the two strategies, the same total number of updates gave very different drops, and we did not test why. The two differ in how the updates are organised: joint fine-tuning trains all six structures together in one continuous run, sequential fine-tuning trains 50 updates per structure and restarts the optimiser for each task." The earlier momentum calculation (tracker, 2026-11-10) is a possible mechanism, not a result; use it only if you can explain it yourself and say clearly that it is untested.

**D70 (weight ensemble).** Suggested oral answer, from the tracker: "The ensemble averages the pretrained weights and all snapshots with equal weight and is never reset (Sec. 5.3.5). After task t, the snapshots of that task are only about 1/t of the average, so it follows each new task less; its Adaptation per task falls from 0.83 to 0.00 over the sequence (Table A.5). We did not test this, for example with an ensemble restarted per task as in ZSCL's code." Check the two values against Table A.5 before the defence.

### Applied 2026-11-12
Ch. 1 proposal copied to `thesis/introduction.tex` (with 0.1–0.5; l. 172–173 kept). All 30 markers resolved: rows 1, 3, 6–30 removed (row 11: comment line deleted); row 2 replaced by "We did not test removing them from the later layers."; row 4 `\cite{isensee2026nnunet}`; row 5 attributed paraphrase with `\cite[p.~3]{bommasani2021opportunities}`. Row 25 check: every comparison of task-specific LoRA's retention says "by construction" (Ch. 6 l. 88, 148, 232, 475; Summary l. 45). One sentence to look at: Ch. 6 Sec. 6.8, "The contrast between sequential fine-tuning and task-specific LoRA … may therefore hold more generally": since task-specific LoRA retains by construction, the part of the contrast that is about retention is expected in any setting.
