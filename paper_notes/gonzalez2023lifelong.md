# Lifelong nnU-Net — paper notes

Read as prior work for Ch. 2 (State of the Art): the reference benchmark comparing standard continual-learning methods for 3D medical image segmentation on a conventional (non-foundation, non-promptable) network.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | González, Ranem, Pinto dos Santos, Othman, Mukhopadhyay. *Lifelong nnUNet: a framework for standardized medical continual learning.* *Scientific Reports* 13:9381 (2023), DOI 10.1038/s41598-023-34484-2, open access CC BY 4.0. Received 25 October 2022, accepted 2 May 2023 (p. 12). 13 pages; journal page numbers = PDF pages. Title spelling "nnUNet"; the body text writes "Lifelong nnU-Net" |
| Local PDF | `papers/t5_cl_medseg_networks/gonzalez2023lifelong_scirep.pdf` (text: `papers/text/gonzalez2023lifelong_scirep.txt`) |
| Secondary | Research Square preprint v1, 26 April 2022, DOI 10.21203/rs.3.rs-1582100/v1, `papers/t5_cl_medseg_networks/gonzalez2023lifelong.pdf`. Earlier notes were written from it; it differs substantially (see "Differences between preprint and Sci. Rep. version" below). Do not cite numbers from it |
| Bib key | `gonzalez2023lifelong` (`@article`, *Scientific Reports* 13(1):9381, 2023 in the bib), matches the version read |
| Version read | **Sci. Rep. 13:9381 (2023)**, the published version. No supplementary material is referenced; dataset sizes, hyperparameters, hardware and runtimes are in the main text |
| Code | github.com/MECLabTUDA/Lifelong-nnUNet ("Code availability", p. 12); trained models on request |
| Notes written | 2026-10-22 by Claude from the preprint; revised 2026-10-23 by Claude against the Sci. Rep. version. Locators are Sci. Rep. page numbers plus section heading, table, figure or equation (the published version has no line numbers). Tables 1–3 were checked on the PDF page images (p. 3, p. 6) because the text extraction is garbled |

## 1. Problem and idea (abstract and introduction; p. 1–2)
- Deep-learning segmentation is mostly evaluated statically (all data shuffled, in-distribution test), which assumes all data are available centrally and acquisition does not change after deployment (p. 1, Fig. 1 p. 2).
- Continual segmentation in medicine lacks a standardised framework; earlier work neither builds on a high-performing segmentation pipeline nor tests popular methods on several open benchmarks (p. 1).
- Proposal: **Lifelong nnU-Net**, a continual-learning extension of nnU-Net with training and evaluation modules and five CL methods; contributions include a performance and run-time comparison (p. 1–2).
- Stated findings (p. 2): no method consistently reaches positive backward transfer; rehearsal forgets least while keeping plasticity; task-specific heads are only minimally relevant for segmentation. (Task order is not among the listed findings in this version; it is discussed in the Results, p. 5, see Sec. 7.)

## 2. Setting (p. 2, p. 7–8, p. 9–10)
- Scenario named by the authors: **domain-incremental learning** ("incremental domain learning", stated as a limitation of scope in the Discussion, p. 7; also requirement 2 in Methods, p. 7).
- A **task = one dataset of the same anatomy**; the datasets of each anatomy are tasks T1…Tn (Results intro p. 2; Datasets p. 8). Same structure(s) across tasks after label alignment ("Aligning label characteristics", p. 8, Fig. 10 p. 9).
- Default: whole model trained sequentially with one shared head, so no task identity is needed at inference ("Multihead architectures", p. 5). Multi-head variants (task-specific last layer, head selected with known task identity at inference; body plastic or frozen after the first task) are evaluated on the cardiac data (p. 5, Fig. 5 p. 6; Methods p. 8–10, Fig. 11 p. 10).
- Not few-shot: 20 % of each dataset is held out for testing (p. 8); the training sets are the rest of each dataset (no subsampling mentioned).
- Notation: F_i trained only on T_i; F_[1,2,3] trained sequentially; F_{1,2,3} static (joint) model; F_i(T_j) = performance of F_i on the test data of T_j ("Notation", p. 8).

## 3. Method (framework and the five CL methods; p. 7–12)
- Framework requirements (Methods, p. 7): state-of-the-art static segmentation (2D and 3D), domain-incremental evaluation via common dataset formats and label alignment, evaluation that tracks all tasks during training, existing CL methods including multi-head models.
- **Label alignment** (p. 8, Fig. 10 p. 9): labels of different datasets mapped to one structure, e.g. prostate central gland + peripheral zone merged into prostate; hippocampus head + body merged. Incremental label learning is mentioned as an alternative, not studied.
- **Multi-head** (p. 8–10, Fig. 11 p. 10): head replicated before each new task; optional freezing of the shared body after the first task; split point set by the user; in the multi-head experiments the split point is `seg_outputs`.
- Methods ("Continual learning methods", p. 11; no pseudocode boxes, one example command in Fig. 12 p. 10):
  - **Rehearsal**: memory buffer of previous-task samples interleaved with new data.
  - **EWC**: Fisher-information-weighted penalty on deviation from the previous parameters, weighted by λ.
  - **LwF**: record old-model outputs on new data, create a new head, train it with the shared body frozen, then fine-tune body and all heads.
  - **Riemannian Walk (RW)**: EWC combined with Path Integral, Fisher computed online.
  - **MiB**: modified cross-entropy plus knowledge distillation to the previous model.
- Which parameters are trained: the whole network in the single-head experiments (p. 5). No extra modules besides the heads.

## 4. Data ("Datasets", p. 7–8; Table 4 p. 8; Figs. 7–9 p. 9)
- Three use cases, open data only (p. 7–8). Sizes from **Table 4 (p. 8)** (number of cases; mean resolution, spacing and ROI fraction also given there):
- **Prostate, T2-weighted MRI**, 4 sources: ISBI (site A), I2CVB (site C), UCL (site D) from the Multi-site Dataset for Prostate MRI Segmentation, plus Medical Segmentation Decathlon prostate (DecathProst) (p. 8). Cases: UCL 13, I2CVB 19, ISBI 30, DecathProst 32 (Table 4).
- **Hippocampus, T1-weighted MRI**, 3 sources: HarP (senior healthy subjects and Alzheimer's patients), Dryad (fifty healthy subjects), DecathHip (healthy adults and schizophrenia patients) (p. 8). Cases: HarP 270, Dryad 50, DecathHip 260 (Table 4).
- **Cardiac MRI** (left ventricle LV, myocardium MI, right ventricle RV; multi-class): M&Ms challenge data, 75 labelled cases from Siemens and 75 from Philips scanners (p. 8; Table 4).
- All 3D. Split: 20 % of each dataset for testing, fixed across experiments, released with the code (p. 8). Validation: a validation set is monitored with Dice (p. 10); the example command uses fold 0 (`-f 0`, Fig. 12 p. 10).
- Task orders: UCL → I2CVB → ISBI → DecathProst; HarP → Dryad → DecathHip; Siemens → Philips (p. 4, Tables 1–2). A second prostate order ISBI → UCL → DecathProst → I2CVB is shown only as learning trajectories (Fig. 4 p. 4; text p. 5). Table 3's caption mentions "both training orders" for cardiac, but the second cardiac order is not described elsewhere.

## 5. Implementation ("Experimental details and hyperparameters", p. 11–12; "Hardware and run times", p. 6–7)
- nnU-Net **3D full-resolution**, patch-based (p. 11). Trained from scratch, no pretraining mentioned.
- **250 epochs per dataset** (p. 11).
- nnU-Net auto-configuration of the **first dataset** is kept for all later tasks (p. 11).
- Hyperparameters from earlier work or short preliminary runs (p. 11). Stated values (p. 11–12): rehearsal 25 % of previous-task cases; EWC λ = 0.4; LwF distillation temperature 8 (hippocampus) and 64 (prostate); RW λ = 0.4 and α = 0.9 for the Fisher values; MiB α = 0.9 (hippocampus) and 0.75 (prostate).
- **Inconsistencies in the paper:** (a) p. 5 names the Table 1 defaults as λ = 0.4 (EWC), T = 2 (LwF), α = 0.9 (MiB), λ = 0.4 (RW), which conflicts with the LwF temperatures and the prostate MiB α given on p. 11–12 (possibly the p. 5 values refer to cardiac only; not stated). (b) The example rehearsal command uses `-samples_in_perc 0.15` (Fig. 12 p. 10), the text says 25 % (p. 11).
- Cardiac hyperparameter sweep: three settings per regularisation/distillation method (Table 2 p. 3), chosen retrospectively (p. 5).
- Hardware (p. 6): 8 NVIDIA Tesla T4 (16 GB), 2 Intel Xeon Silver 4210 CPUs, 256 GB DDR4 RAM; one GPU per experiment, except LwF on prostate (2 GPUs).
- **Runtime, Table 3 (p. 6)**, seconds per epoch, mean (± std over the anatomy; cardiac over both orders), Prostate / Hippocampus / Cardiac: Seq. 214.3 / 117.3 / 194.5; EWC 215.25 / 131.0 / 197.3; LwF 423.3 / 233.3 / 174.7; MiB 365.5 / 212.0 / 281.5; RW 223.5 / 136.1 / 202.3; Reh. 206.0 / 140.3 / 195.5. Text (p. 6–7): MiB needs much more time than sequential training; the LwF epoch time grows with sequence length (prostate); methods whose epoch time grows linearly with sequence length may be best avoided.
- Number of runs/seeds and the meaning of the ± values in Tables 1–2: **not stated**.

## 6. Evaluation protocol and metrics ("Evaluation logic and metrics", p. 10–11; Fig. 3 p. 4)
- Segmentation metric: Dice (Eq. 1, p. 10); tables report Dice in %.
- **BWT** (Eq. 2, p. 11): F[…,i,…](T_i) − F[…,i](T_i), i.e. performance on T_i after later tasks minus right after training T_i; negative = forgetting.
- **FWT** (Eq. 3, p. 11): F[…,i](T_i) − F_i(T_i), the continual model right after T_i vs a model trained only on T_i (authors note that other definitions use all future tasks, p. 11).
- Both reported **relative** to the right-hand term (p. 11). In this version BWT/FWT appear only as a scatter plot (Fig. 3 p. 4, averaged per use case), not as table values.
- **Inter-task performance**: separate model per task tested on all tasks (Fig. 2 p. 3; p. 11).
- Training trajectories on all tasks' validation sets (p. 10; Fig. 4 p. 4).
- Reference points: **static model** (joint training on shuffled data of all datasets of an anatomy) as upper bound (Table 1 caption p. 3; p. 4); sequential training without CL method ("Seq.") as the trivial baseline (p. 4). Rehearsal is described as an "additional upper bound" where storing data is not allowed (p. 4).
- Reported Dice is that of the **final model** after the last task (Table 1 and 2 captions, p. 3).

## 7. Results
- **Independent models (Fig. 2, p. 3; text p. 2):** in-distribution Dice ≥ 86 % for all models (diagonal of Fig. 2; cardiac = RV). I2CVB is an outlier for prostate. HarP model 86 % on Dryad, Dryad model 50 % on HarP, attributed to HarP's larger size (p. 2). For RV, the Siemens model does well on Philips (91 %), the Philips model reaches 50 % on Siemens (Fig. 2; p. 2–4).
- **Table 1 (p. 3), Dice % of final model** (UCL / I2CVB / ISBI / DecathProst | HarP / Dryad / DecathHip; ± values omitted here, identical to the preprint values):
  - Static 70.91 / 93.05 / 92.27 / 91.90 | 90.48 / 94.12 / 93.99
  - Seq. 85.16 / 21.04 / 93.09 / 91.91 | 20.20 / 57.19 / 90.92
  - EWC 86.87 / 58.53 / 88.43 / 87.79 | 88.01 / 86.09 / 31.93
  - LwF 85.30 / 22.89 / 92.37 / 91.48 | 3.90 / 46.00 / 90.85
  - MiB 86.31 / 48.87 / 92.96 / 92.11 | 82.45 / 85.27 / 20.75
  - RW 84.08 / 26.51 / 93.18 / 92.07 | 7.33 / 34.87 / 91.07
  - Reh. 85.94 / 90.64 / 93.39 / 91.55 | 88.17 / 92.07 / 91.16
- **Table 2 (p. 3), cardiac, Dice % of final model after Siemens → Philips** (Siemens LV / MI / RV | Philips LV / MI / RV):
  - Seq. 80.5 / 68.5 / 64.8 | 96.1 / 87.0 / 93.2
  - EWC λ = 0.1: 95.2 / 85.1 / 90.3 | 94.1 / 81.5 / 88.9; λ = 0.2: 95.4 / 85.1 / 89.9 | 94.5 / 81.7 / 89.9; λ = 0.4: 92.9 / 83.2 / 88.0 | 93.6 / 82.0 / 87.0
  - LwF T = 2: 74.2 / 64.0 / 60.6 | 96.0 / 86.8 / 92.2; T = 5: 69.3 / 61.2 / 54.7 | 96.0 / 85.4 / 91.3; T = 10: 74.7 / 50.3 / 61.7 | 96.1 / 85.8 / 92.3
  - MiB α = 0.8: 94.5 / 85.1 / 90.5 | 94.9 / 83.3 / 90.6; α = 0.9: 91.5 / 80.3 / 80.5 | 95.9 / 86.7 / 92.4; α = 1.0: 92.7 / 84.1 / 88.4 | 94.5 / 83.0 / 89.9
  - RW λ = 0.4: 82.8 / 71.0 / 67.3 | 96.1 / 86.7 / 93.1; λ = 0.8: 74.8 / 67.4 / 69.6 | 96.1 / 85.8 / 91.6; λ = 1.0: 74.8 / 65.4 / 71.1 | 96.0 / 85.4 / 91.7
  - Reh. 93.9 / 83.6 / 84.5 | 96.0 / 86.6 / 92.9
- Rehearsal prevents forgetting best over all anatomies; EWC and MiB are named as alternatives when data cannot be stored; LwF and RW do not translate well to segmentation (p. 4; Discussion p. 7).
- Loss of plasticity: DecathProst 91.91 % (Seq.) → 87.79 % (EWC); DecathHip 90.92 % → 31.93 % (EWC), 20.75 % (MiB) (p. 4); for cardiac, forgetting of Siemens for LwF/RW and plasticity loss on Philips for EWC/MiB, most visible for MI and RV (p. 4). In Fig. 3 EWC has negative FWT, rehearsal near zero (p. 5).
- **Hyperparameters (p. 5, Table 2):** lower λ for EWC and lower α for MiB help on cardiac; other settings did not improve LwF or RW. The authors state that this does not carry over to prostate and hippocampus and that a plasticity–rigidity trade-off cannot be reliably selected from other use cases.
- **Order effect (p. 5, Fig. 4):** in UCL → I2CVB → ISBI → DecathProst, UCL recovers after the I2CVB stage, attributed to the good transfer of ISBI/DecathProst models to UCL; in ISBI → UCL → DecathProst → I2CVB, older tasks deteriorate continually and EWC starts low on the last task. The authors conclude that task order matters for comparing methods and ideally all orders should be tested, which is computationally prohibitive for 3D networks; prospectively the order is given (p. 5). Only trajectories of Seq., EWC and rehearsal are shown; no per-order table of all methods.
- **Multi-head (Fig. 5 p. 6; text p. 5):** cardiac only; one vs separate heads makes minimal difference; freezing the body after the first task prevents forgetting on Siemens at a slight cost on Philips.
- **Qualitative (Fig. 6, p. 6; text p. 5–6):** Seq., LwF and RW give scattered masks with extra components; EWC keeps the hippocampus shape but not the prostate; rehearsal keeps shapes (prostate mask too large, one extra component); MiB gives reasonable masks, slightly under-segmenting the prostate.
- Discussion (p. 7): no method gave positive BWT (best methods reach about zero, Fig. 3), so independent per-task models would outperform all CL methods; positive FWT only for prostate; task-specific heads do not change performance much, with plastic or frozen body.

## 8. Limitations and future work (authors; Discussion p. 7; "Tuning the plasticity/rigidity tradeoff", p. 5)
- Only the 3D full-resolution nnU-Net; 2D and low-resolution variants not repeated (p. 7).
- Only the **domain-incremental** scenario (p. 7).
- Limited catalogue of methods; growth hoped for (p. 7). Keeping a larger part of the network task-specific is suggested for further study (p. 7).
- Hyperparameters cannot be tuned on past or future data in a real continual setting; the paper relies on literature defaults and preliminary runs and tunes only retrospectively on cardiac (p. 5). Not listed as a limitation in the Discussion.

### Differences between preprint and Sci. Rep. version
- **Third use case:** preprint = pulmonary embolism in chest CT (CADPE, FUMPE; both orders); Sci. Rep. = cardiac MRI from M&Ms (Siemens, Philips; LV, MI, RV). All pulmonary embolism results (preprint Table 2 with BWT values, the failure of rehearsal in FUMPE → CADPE, CADPE/FUMPE in Fig. 2) are gone.
- **Tables:** preprint Table 2 (pulmonary embolism, Dice + BWT) replaced by a cardiac hyperparameter sweep (Table 2); new Table 3 (runtime per epoch) and Table 4 (dataset sizes). Table 1 values are unchanged; only the row order differs (Reh. last).
- **Dataset sizes:** preprint referred to a supplement not in the PDF; Sci. Rep. gives them in Table 4 (p. 8).
- **Hyperparameters, hardware, runtimes:** stated in the Sci. Rep. main text (p. 5, 6, 11–12); preprint deferred them to the supplement/code.
- **Task order:** preprint listed "task order is crucial" as a key finding and showed it with the two pulmonary embolism orders; Sci. Rep. drops it from the findings list and supports it with learning trajectories for a second prostate order (Fig. 4).
- **Multi-head:** preprint referred to Supp. Table 3 across methods (with an LwF exception); Sci. Rep. shows cardiac only, four settings including a frozen body (Fig. 5), and makes no LwF-specific statement.
- **Methods presentation:** preprint Algorithms 1–5 and Listings 1–2 (incl. `-ewc_lambda 2.4`) replaced by prose and one command-line figure (Fig. 12).
- **Metrics:** preprint mentioned Dice and IoU; Sci. Rep. defines only Dice (Eq. 1). BWT/FWT are Eq. 2/3 (preprint Eq. 1/2) and shown only in Fig. 3, not as table values.
- **Limitations:** the preprint's explicit "no full hyperparameter search" limitation became a separate section on tuning the plasticity–rigidity trade-off (p. 5) plus a retrospective sweep.
- The preprint's total "1,000 epochs for four datasets" is not restated; 250 epochs per dataset is unchanged.

## 9. Check of the author's notes (re-checked against Sci. Rep., 2026-10-23)
| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:81` | "comparing rehearsal, EWC, Learning without Forgetting, Riemannian Walk, and MiB" | **Correct** (p. 2, p. 11). |
| `thesis/related_work.tex:81` | "across hippocampus, prostate, and cardiac segmentation" | **Correct for the published version** (cardiac MRI, M&Ms; p. 8, Table 2). (Was "wrong" against the preprint, which used pulmonary embolism CT.) |
| `thesis/related_work.tex:81` | "under domain-incremental settings" | **Correct** (p. 7). |
| `thesis/related_work.tex:81` | "reported that their relative ranking depends on the scenario, the task sequence, and the dataset" | **Partly correct.** Supported: the paper says task order is important when comparing methods (p. 5, Fig. 4), and results differ between use cases, e.g. hyperparameter choices from cardiac do not transfer to prostate/hippocampus (p. 5). Not supported: "scenario" (only domain-incremental). Note the order evidence is trajectories of three methods for one prostate order pair, not a ranking table per order. Suggested: "task order and use case (dataset)". |
| `thesis/related_work.tex:120` | "the ranking of such strategies depends on the scenario, the task sequence, and the architecture" | **Partly wrong.** Architecture was not varied (only 3D full-res nnU-Net, limitation p. 7); scenario not varied. Only task-order and use-case dependence are supported. |
| `thesis/related_work.tex:198` (summary table) | Data "Hippocampus, prostate, cardiac"; result "Ranking depends on setting" | **Data correct** for the published version (was wrong against the preprint). Result partly correct, see above; could add case counts from Table 4. |
| `thesis/related_work.tex:230` (positioning table) | Language none; 3D FM no; few-shot no; DIL; Rehearsal, EWC, LwF, RWalk, MiB | **Correct** (no text input, nnU-Net trained from scratch, full training data, domain-incremental, five methods). Paper's own abbreviation is "RW", not "RWalk". |
| `thesis/introduction.tex:27` | cited as early work that "considered task-specific or relatively compact models" | **Partly correct.** It uses a conventional 3D nnU-Net (not a foundation model); the default setting is single-head, not task-specific; multi-head is a variant evaluated only on cardiac (p. 5, Fig. 5). |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
1. **Relation to this thesis:** same broad question (which CL strategy trades off forgetting and plasticity best for 3D segmentation), but tasks are **datasets of one anatomy** (domain-incremental) rather than **different structures from one dataset**; model trained from scratch, no pretrained ability to protect, no text prompt, full data instead of few-shot (smallest training sets still around 10–26 cases: 80 % of the 13–32 prostate cases in Table 4, an inference from the 20 % split, not stated by the paper).
2. **Gap claim:** does **not** weaken "no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model" (no language, no pretrained model).
3. Useful support for design decisions: (a) testing more than one task order (p. 5, Fig. 4) supports the original/reverse orders; (b) the static (joint) model as upper reference; (c) BWT/FWT definitions close to Chaudhry-style forgetting. Their FWT compares with an independently trained model, not with pretrained-model performance as in ZSCL's Transfer used in this thesis; (d) the hardware/runtime table (Table 3) is a precedent for reporting compute per strategy; (e) the cardiac sweep (Table 2) and p. 5 show that the plasticity–rigidity setting is use-case dependent, relevant for justifying fixed hyperparameters.
4. Rehearsal is the strongest method in all three use cases (Tables 1–2), a possible comparison point for shared LoRA + replay. The preprint's buffer-size argument (FUMPE → CADPE) is not in the published version; do not cite it.
5. Bib: the read version now matches the bib (Sci. Rep. 2023). Title in the paper is "Lifelong nnUNet"; check that the bib title uses the published spelling.
