# Pass 1 — Structure and common thread (2026-11-12)

Report-only subagent pass (fresh agent, restarted in a new session). No files edited by the agent. Saved by the main session.

PDF basis: `thesis/thesis_main.pdf`, 136 pages; printed page numbers from `pdftotext -layout`.

| Ch. | Pages | Printed pages (blank) |
|---|---|---|
| 1 Introduction | 1–7 | 7 (p. 8 blank) |
| 2 State of the Art | 9–22 | 14 (Table 2.2 longtable ≈ pp. 20–22) |
| 3 Theoretical Background | 23–33 | 11 (p. 34 blank) |
| 4 Data Description | 35–39 | 5 (p. 40 blank) |
| 5 Method | 41–53 | 13 (p. 54 blank) |
| 6 Experiments and Results | 55–76 | 22 |
| 7 Summary | 77–80 | ≈3.4 |
| App. A | 81–102 | 22 |

**Precondition not met (must fix).** 241 `% CLAUDE-DRAFT` markers remain (intro 22, related_work 30, background 34, data 12, method 43, experiment_results 70, summary 12, appendix 18). No `\todo` left. Structure reviewed only; length estimates may change after the author's rewrite.

## 1. Objectives ↔ contributions ↔ experiments ↔ Summary

| Obj. | Contribution | Where addressed | Summary |
|---|---|---|---|
| 1 Protocol | C1 | Sec. 5.1; evidence in Sec. 6.5 | l. 73–76 |
| 2 Compare strategies | C2 | Secs. 5.3, 6.2, 6.3 | l. 32–37, 47–52 |
| 3 Labelled data | C3 | Sec. 6.4 | l. 38–39, 56–58 |
| 4 Order and design choices | C4 | Secs. 6.5, 6.6 (+ App. A.4) | l. 65–69 |

Every objective addressed, every contribution supported; research question answered explicitly at `summary.tex:32`.

Gaps:
- **RQ says few-shot; central comparison is not few-shot** (`introduction.tex:114,118` vs `experiment_results.tex:595–596`). The six-strategy comparison uses 108 volumes; only three strategies ran with k = 5/10/20, and the two LoRA strategies learned nothing there within ten epochs. Stated honestly in 6.8 and Summary (l. 38), but the thread from title/RQ to main result is weak. **Should fix** (framing in Sec. 1.3/1.4 and Summary opening; no new runs): present the full split as the reference for reading the few-shot settings, or narrow the RQ wording.
- **Objective 4 vs C4 scope** (`introduction.tex:126` vs `:189`). Objective 4 promises "design choices within the strategies"; main text varies only the LoRA rank. Replay is a strategy, not a design choice; WE and gradient-scaling ablations are in App. A.4 with one sentence in the main text (`experiment_results.tex:238–239`); λ, ρ, m, L_p, α "set once and not tuned". **Should fix**: narrow Objective 4 to the rank, or name A.4 as part of it (but A.4 not a contribution, decision 2026-11-05).
- **C2 "a diagnosis of why task-specific LoRA did not learn patellar cartilage"** (`introduction.tex:187`): Sec. 6.3 (l. 298–301) leaves the cause confounded (more updates vs slower LR decay); 6.8 (l. 572) says no run tests the deeper explanation. "Why" too strong. **Minor.**

## 2. Chapter deliverables and flow
- **Ch. 1:** all elements present. Sec. 1.4 (`introduction.tex:133–176`, ≈1.3 pp.) already defines all five metrics, every strategy with rank, joint fine-tuning, control task — Ch. 3/5 detail; tier-2 says the Introduction stays conceptual. **Should fix** (also length).
- **Ch. 2:** findings, data, results, grouping, summary table (Table 2.2), gap present. Gap paragraph (l. 275–283) followed by ≈3 pages of table: acceptable. Ch. 3 opening (`background.tex:13–16`) doesn't pick up the gap. **Minor.**
- **Ch. 3:** (a) `background.tex:246–248` introduces our own control task and c_j inside "concepts as published"; control task also defined in Ch. 1 (l. 137) and Ch. 5 (method.tex:37): three definitions vs tier-2 "each definition in one place". **Should fix.** (b) `background.tex:41–43, 48–72` re-derive U-Net, patch training and full multi-head attention; only the "appended rows" property (l. 67) is used later. **Minor** (length).
- **Ch. 4:** all present; supervisor's "figures … of the data distribution" met only by example slices (Fig. 4.1); structure-size distributions only in text (`data_description.tex:62`). **Minor.**
- **Ch. 5:** pseudocode, reasons, alternatives, complexity present. Complexity in words only (`method.tex:400–423`; see pass 2). **Minor.** `method.tex:38` justifies the control task by a result ("segments well (Sec. 6.2)") — forward dependency; l. 41 (paper's 96.99 %) suffices. **Minor.**
- **Ch. 6:** all present; prior-work comparison in conclusions of 6.2, 6.4, 6.5, 6.6 but not 6.3. **Minor.** Sec. 6.2 uses ranks chosen in 6.5 from test results (l. 74–76), justification three sections later. **Minor.**
- **Appendix:** each part names its section. Task-order conclusion uses App. A.6 loss curves as evidence (`experiment_results.tex:508–511, 528–529`), numbers in text, so readable. **Minor.** A.4 acceptable (summarised in 6.2).
- **Flow:** Ch. 4→5, 5→6, 6.8→Summary connect well; Ch. 2→3 does not.

## 3. Theory vs practice
Theory (Ch. 2+3) 25 pp.; practice (Ch. 4+5+6) 40 pp.; ≈38:62 vs chair's "approximately equally split". **Should fix** in the sense that cuts (§5) should come mainly from Ch. 5 and 6. Don't pad Ch. 3.

## 4. Summary
Original work stated at `summary.tex:27–28`; positioning at l. 76. ≈3.4 pages. **OK.** Header comment says "Chapter 8" (`summary.tex:2`). Cosmetic.

## 5. Length
Main content pp. 1–80, 4 blank, ≈76 pages of content. 12 figures (Fig. 5.1 a full `[p]` page), ~10 tables incl. a 3-page longtable; floats ≈13–15 pp., text ≈61–63 pp. **Should fix**: aim ≈65–68 pp. and argue the rest with figures; 60 would need cutting results.

Candidates (≈ savings):
1. Sec. 1.4, `introduction.tex:133–176` (≈0.7 p.): reduce to the conceptual approach.
2. Sec. 3.1.1–3.1.2, `background.tex:35–72` (≈0.7 p.): cite U-Net and transformer; keep cross-attention with appended rows and symbols used in Ch. 5.
3. Sec. 2.4.1 background shift `related_work.tex:182–186` + ILT l. 178–179 (≈0.4 p.): one sentence. Table 2.2 stays but could lose a column / tighter font (≈0.5 p.).
4. Sec. 5.3.5 ensemble details `method.tex:386–394` (≈0.3 p.): move to App. A.4.
5. Sec. 6.6 task-specific LoRA paragraph `experiment_results.tex:469–478` and 6.8 l. 584–586 (≈0.4 p.): same point twice.
6. Sec. 6.6 training-loss paragraph `experiment_results.tex:508–511` (≈0.3 p.): to App. A.6, keep one sentence.
7. Sec. 6.8 threats paragraph `experiment_results.tex:618–622` (≈0.4 p.): repeats 6.1.2 (l. 74–76), 5.3.2 (l. 274), 6.2 (l. 230–232). More generally 6.8 (≈3.5 p.) could drop ~1 p. by not restating numbers.
8. Sec. 6.7 + 5.4 (≈0.3 p.): 6.7 l. 547–549 re-explains cost reasons from 5.4.

Total ≈5–6 pages; each moved item keeps a one-sentence summary in the main text.

## 6. Repetition across chapters (should fix unless noted)
- Task-specific LoRA "zero/near-zero by construction" ~8 times: `method.tex:279–281`, `experiment_results.tex:90, 154, 250, 516, 645`, plus three captions (captions fine). Keep definition (Ch. 5) and one reminder (6.1.3).
- ZSCL's current-task-data ablation 3×: `related_work.tex:118`, `method.tex:381`, `experiment_results.tex:224`.
- Teacher choice (initial vs previous model, ZSCL vs PRIMED) 3×: `related_work.tex:128–129`, `method.tex:351`, `experiment_results.tex:605`.
- "Fixed epochs ⇒ fewer volumes mean fewer updates" 3×: `introduction.tex:90`, `method.tex:95–96`, `experiment_results.tex:52`. Minor.
- Control task definition and AeroPath-in-v1.1 caveat: `introduction.tex:137–138`, `background.tex:246–248`, `data_description.tex:84–85`, `method.tex:37–39`, `experiment_results.tex:613`, `summary.tex:110`. Define once (Ch. 5), caveat once (Ch. 4, 6.8 recap).
- Metric definitions `introduction.tex:161–170` duplicate Sec. 3.3.
- Family coverage argument `introduction.tex:152`, `method.tex:225–231`. Minor.
- "Few-shot"/"shot" defined twice, `introduction.tex:93`, `related_work.tex:64`. Minor.
- VoxTell 70.85 % / 10.72 % at `introduction.tex:39–40` and `related_work.tex:47`. Minor.
- LoRA slow first-task learning / zero-init hypothesis: `experiment_results.tex:528–530`, `:571–578`, `summary.tex:90`. Minor.

## Severities
- **Must fix:** 241 `% CLAUDE-DRAFT` paragraphs (precondition).
- **Should fix:** few-shot framing; Objective 4 scope; Sec. 1.4 too detailed; control task defined three times; length; theory/practice imbalance; repetitions in §6.
- **Minor:** "diagnosis of why" in C2; Ch. 2→3 link; no distribution plot in Ch. 4; complexity in words; control-task choice justified by a Ch. 6 result; no prior-work comparison in 6.3; 6.2 uses ranks chosen in 6.5; 6.6 uses App. A.6 as evidence; stale "Chapter 8" comment.
