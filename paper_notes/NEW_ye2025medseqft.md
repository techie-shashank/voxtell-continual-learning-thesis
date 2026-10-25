# MedSeqFT — paper notes

Read as prior work for Ch. 2 (State of the Art): sequential fine-tuning of a self-supervised 3D foundation model over a series of segmentation tasks, with a sample buffer and LoRA-based distillation to keep pretrained knowledge.
Sections 1–8 are what the **paper** says, with locations; sections 9–10 are a check of the author's notes and **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Ye, Wu, Luo, Zhang, Chen, Dang, Zhang, Xia. *MedSeqFT: Sequential Fine-tuning Foundation Models for 3D Medical Image Segmentation.* arXiv:2509.06096v1 [cs.CV], 7 Sep 2025 (p. 1, margin). 10 PDF pages: p. 1–9 paper, p. 9–10 references. No appendix or supplement |
| Local PDF | `papers/t6_cl_medseg_foundation/NEW_ye2025medseqft.pdf` |
| Bib key | none yet (author's notes use the literal label `[MedSeqFT]`; planned key `NEW_ye2025medseqft`) |
| Version read | **arXiv preprint v1 (7 Sep 2025).** Typeset in the IEEE Transactions on Medical Imaging template, but the running head is the unfilled placeholder "VOL. XX, NO. XX, XXXX 2020" (every page). The PDF does **not** state acceptance at any peer-reviewed venue. Check for a published version before citing |
| Code | "Code will be released" (abstract, p. 1); no URL given |
| Notes written | 2026-10-23, by Claude, from the arXiv preprint v1. Page numbers = PDF pages (identical to the paper's page numbers) |

## 1. Problem and idea (abstract, Sec. I; p. 1–2)
- Downstream segmentation tasks for foundation models arrive one after another in clinical practice (abstract, p. 1).
- **Parallel fine-tuning** (one independent copy of the pretrained model per task) shares no knowledge between tasks; **multi-task fine-tuning** needs all datasets at once, suffers from optimisation conflicts and cannot add tasks incrementally (p. 1–2, Sec. I; Fig. 1a–b).
- Proposal: **sequential fine-tuning**, where the model refined on one task initialises the next (Fig. 1c, p. 1; Sec. I, p. 2). The stated challenge is balancing specialisation against keeping earlier knowledge, i.e. avoiding catastrophic forgetting (p. 2).
- Two components: **Maximum Data Similarity (MDS)** selection of downstream samples close to the pretraining distribution, and **Knowledge and Generalization Retention Fine-Tuning (K&G RFT)**, a LoRA-based distillation scheme (abstract; p. 2).
- Stated aim of the refinement: a better pretrained model for later and unseen tasks, i.e. "representational capacity" (abstract, p. 1), tested on two unseen tasks (Sec. V-A, p. 8).

## 2. Setting (Sec. III-A–B, p. 3–4; Sec. IV-E, p. 6–7)
- The authors do **not** use continual-learning scenario terms (task-/class-/domain-incremental); they call the setting "sequential fine-tuning" / "sequential learning problem" (Sec. III-A, p. 3).
- **A task = one dataset** D_t with its own segmentation task (p. 3, Sec. III-A), e.g. Liver (liver + tumour), HepaV (hepatic vessel + tumour) (Table I, p. 5; Fig. 2, p. 3).
- Output: a **series of models** M_1 … M_n, M_t adapted for task D_t (p. 3). Each task gets a **randomly initialised segmentation head**; encoder and decoder are initialised from the previous model (Sec. III-D, p. 4; Sec. IV-E, p. 7). Whether earlier heads are kept, and whether earlier tasks are re-evaluated after later training, is **not stated**; all reported results are per task (Tables II–V), apparently from M_t (not stated explicitly).
- Task identity at inference: not discussed. Since each task has its own head and its own model M_t, the task is implicitly known (my reading, not stated).
- Not few-shot: 80:20 train/test split of every dataset (official split for WMH) (Sec. IV-A, p. 5; Table I).
- Task order (CT set): only the first task (Liver) is stated (Sec. IV-E, p. 7); the rest of the order is not stated, tables list Liver, HepaV, Pancreas, Colon, Lung. MRI order: not stated. Only one order is tested; order effects are not studied.

## 3. Method (Sec. III, p. 3–4; Fig. 2)
- Base adaptation is **full fine-tuning (FFT)**, chosen over PEFT on "empirical evidence" (Sec. III-B, p. 4).
- **Task 1:** M_0 is fully fine-tuned, then LoRA-based KD and reparameterisation produce M_1 (p. 4, step 1).
- **MDS** (Sec. III-C, p. 4): all training samples of D_t pass through the **original** model M_0 and its SSL head; the SSL loss per sample is averaged over 1000 runs (random masking); the **K samples with the lowest loss** go into the buffer for the next stage. Value of K: **not stated**. Buffer accumulates over tasks (step 4, p. 4).
- **K&G RFT** for tasks t > 1 (Sec. III-D, p. 4), three steps:
  1. **KD-based FFT:** M_t-init (encoder from E_t-1, decoder from DE_t-1, new random head) trained on D_t with L_seg = Dice + cross-entropy; buffer samples go through E_t-init and the frozen E_t-1, MSE distillation loss L_kd on the outputs ("soft constraint"). The two losses are computed separately, "each updating only its corresponding parameters" (p. 4); which parameters each loss updates is not specified further.
  2. **LoRA-based KD:** E_t-1 and the trained E_t-mid are frozen; LoRA modules are inserted into every linear layer of E_t-1 and trained with an MSE refinement loss L_refine to reproduce E_t-mid **on the new task data** (not on the buffer) ("hard constraint", p. 4).
  3. **Reparameterisation:** LoRA merged into E_t-1, W' = W + BA (Eq. 1, p. 4), giving M_t with no extra parameters.
- Note: the distillation teacher in step 1 is the **previous** encoder E_t-1, not M_0; M_0 is used only for MDS scoring (p. 4). The decoder's fate in steps 2–3 (taken from M_t-mid or not) is not stated.

## 4. Data (Sec. IV-A, p. 4–5; Table I, p. 5)
All 3D. Train/test counts from Table I; 80:20 split except WMH (official split).
- **CT multi-task set (5 tasks):** Liver (from LiTS; liver + tumour) 104/27; HepaV (MSD; hepatic vessel + tumour) 242/61; Pancreas (MSD; pancreas + tumour) 224/57; Colon (MSD; colon tumour) 100/26; Lung (MSD; lung tumour) 50/13.
- **MRI multi-task set (5 tasks):** PanSegData (pancreas; 385 T1W scans used of 767 from five centres) 308/77; ISLES 2022 (ischaemic stroke lesion; DWI, ADC, FLAIR; 250 public cases of 400 from three centres) 200/50; HNTSMRG 2024 (head-and-neck GTVp and GTVn, T2W; Task 1 training set) 120/30; ISPY1 (breast tumour; three sequences) 128/33; WMH (white-matter hyperintensities; T1W + FLAIR) 60/110.
- **Transfer set (unseen):** COVID-19-20 (CT lung lesions) 159/40; Kidney (from KiTS; kidney + tumour) 168/42.
- Counting: abstract says "two multi-task datasets covering ten 3D segmentation tasks"; contributions say "12 diverse CT and MRI datasets" (p. 2), i.e. 10 + 2 transfer (consistent).
- No validation split mentioned.

## 5. Implementation (Sec. IV-B, p. 5)
- Built on the **nnU-Net** framework; two training frameworks: supervised fine-tuning and LoRA-based KD.
- Backbones: **VoCo (Swin-Base)** and **UniMiSS+**, both CT-pretrained self-supervised models.
- Supervised fine-tuning: 25,000 iterations, AdamW, batch size 2, patch 32×160×160; lr 3e-4 (VoCo), 1e-4 (UniMiSS+).
- LoRA-based KD: **rank r = 2**; lr 3e-5 (VoCo), 1e-4 (UniMiSS+); distillation iterations 5,000 (VoCo, CT), 20,000 (VoCo, MRI), 12,500 (UniMiSS+).
- Compute (Table VII, p. 9; Sec. V-C): FFT ~21.1 h for 5 CT tasks; MedSeqFT ~27.0 h (+5.9 h): first stage ~4.2 h, KD-based FFT ~19.9 h, LoRA-based KD ~2.9 h. GPU memory overhead described only qualitatively ("minimal", "negligible"). **Hardware (GPU type) not stated.**
- Number of runs/seeds, variance: **not stated**; no ± values in any table.

## 6. Evaluation protocol and metrics (Sec. IV-C–D, p. 5–6)
- Metrics: **Dice (%)** and **HD95** (mm); for multi-class datasets the mean over classes (Sec. IV-C, p. 5).
- Per-task performance on each task's test set; averages over five tasks. No forgetting metric, no evaluation matrix, no backward/forward transfer metric.
- Comparisons (Table II): training from scratch (TFS), FFT (parallel, independent per task), ACNorm; PEFT: head fine-tuning, LoRA (r = 2, 4, 8, 16, 32), Adapter (γ = 2, 4, 8), Conv-Adapter, Med-Adapter, Mona; multi-task: MTLoRA (r = 16, 32, 64), UniSeg. All with VoCo and the same number of iterations (p. 5–6).
- **"FFT" in the tables is parallel fine-tuning from M_0**, not sequential fine-tuning. Vanilla sequential fine-tuning ("Seq. FT") appears only in the ablation (Table III).
- Transfer test: pretrained model vs MedSeqFT-refined model (after the CT sequence), both then fine-tuned with FFT on COVID-19-20 and Kidney (Sec. V-A, p. 8; Table VI).

## 7. Results
- **Table II (p. 6), VoCo, CT, average Dice / HD95:** TFS 57.6 / 84.9; FFT 65.3 / 60.4; ACNorm 65.3 / 59.9; Conv-Adapter 65.5 / 53.0; best LoRA (r = 16) 64.1 / 62.5; UniSeg 66.1 / 63.5; MTLoRA (r = 64) 64.0 / 50.8; **MedSeqFT 68.3 / 50.4**. Per task MedSeqFT: Liver 76.5 / 19.5, HepaV 69.8 / 18.8, Pancreas 69.0 / 12.7, Colon 49.8 / 160.1, Lung 76.4 / 40.7.
- Text claims (p. 6): SSL pretraining beats TFS by 7.7 % Dice and 24.5 mm HD95; PEFT mostly below FFT; MedSeqFT improves Dice by "3.0%" and HD95 by "10 mm" over FFT (own check: 68.3 − 65.3 = 3.0 points; 60.4 − 50.4 = 10.0 mm).
- **Inconsistency:** the text says MedSeqFT "achieves the best Dice score across all five datasets" (p. 6), but on Liver UniSeg has 77.7 (bold) vs MedSeqFT 76.5 (Table II). MedSeqFT's Liver result equals FFT because task 1 is trained with FFT (p. 7).
- **Ablation, Table III (p. 6), average Dice / HD95:** FFT 65.3 / 60.4; Seq. FT 66.1 / 56.0; Seq. FT + Random buffer 65.8 / 56.4; Seq. FT + MDS 67.1 / 54.8; Seq. FT + K&G RFT 67.1 / 54.7; Seq. FT + MDS + K&G RFT (full) 68.3 / 50.4. Vanilla Seq. FT already beats parallel FFT "on most metrics" (p. 7). MDS beats random selection of the same buffer size (p. 7).
- **UniMiSS+, Table IV (p. 7), average Dice / HD95:** TFS 63.6 / 50.3; FFT 67.4 / 40.5; UniSeg 69.0 / 35.2; **MedSeqFT 69.9 / 33.6** (+2.5 Dice, −6.9 mm vs FFT, p. 8). Conv-Adapter 62.6 / 49.8, i.e. 4.8 below FFT (p. 8).
- **MRI, VoCo, Table V (p. 7), average Dice / HD95:** TFS 69.3 / 29.0; FFT 73.2 / 19.4; UniSeg 73.4 / 18.9; **MedSeqFT 74.6 / 18.0** (+1.4 Dice, −1.4 mm vs FFT, p. 8). On WMH FFT (77.9) is below TFS (78.1); MedSeqFT 78.6 / 4.3 (+0.5 Dice, −1.1 mm vs TFS, p. 8).
- **Transfer, Table VI (p. 8), Dice / HD95:** COVID-19-20: TFS 53.8 / 91.1, FFT 65.5 / 54.2, FFT w/ MedSeqFT 66.8 / 45.9. Kidney: TFS 90.7 / 29.9, FFT 96.4 / 4.0, FFT w/ MedSeqFT 96.3 / 4.5. Kidney tumour: TFS 29.4 / 180.2, FFT 68.5 / 91.6, FFT w/ MedSeqFT 72.0 / 81.9.
- **Inconsistency:** the text reports "average improvements of 3.5% in Dice and 9.7 mm in HD95" over FFT (p. 8). Own calculation: these equal the **kidney tumour** column alone (72.0 − 68.5 = 3.5; 91.6 − 81.9 = 9.7); the mean over the three columns is +1.6 Dice (own calc). On kidney organ the refined model is slightly worse (96.3 vs 96.4; HD95 4.5 vs 4.0).
- **Analyses (Sec. V-A–B, p. 8–9):** smoother loss landscape than FFT on Lung (Fig. 5); most encoder parameters unchanged after refinement, deeper layers change more, maximum mean absolute change 0.016 (VoCo) and 0.012 (UniMiSS+) (Fig. 4); shallow VoCo linear layers show no change.
- Qualitative (Fig. 3, p. 5; Sec. IV-H, p. 8): fewer missed tumour regions than SSL (FFT), Conv-Adapter, UniSeg.

## 8. Limitations stated by the authors
- Only a "modest increase in training time" is acknowledged (+5.9 h, Sec. V-C, p. 9; Sec. VI).
- Future work: selective refinement of pretrained components; extension to multi-modal imaging tasks (Sec. VI, p. 9).
- No explicit limitations section; task order, few-shot data, forgetting on earlier tasks and number of runs are not discussed.

## 9. Check of the author's notes
`thesis/introduction.tex` contains no sentence about MedSeqFT (searched "MedSeqFT", "sequential fine-tun").

| Location | Claim (quoted/abridged) | Verdict |
|---|---|---|
| `thesis/related_work.tex:96` | "adapts the shared parameters of a self-supervised 3D foundation model directly, and consequently has to protect the pretrained representation explicitly" | **Correct** in substance: FFT of the encoder/decoder of a CT-pretrained SSL model (Sec. III-B, p. 4; Sec. IV-B, p. 5). |
| `thesis/related_work.tex:96` | "scores the training samples of each task with the self-supervised loss of the original model and retains those most representative of the pretraining distribution in a small buffer" | **Correct** (Sec. III-C, p. 4). Buffer size K is not stated in the paper, so "small" is the paper's word only for the subset ("a small subset", p. 4). |
| `thesis/related_work.tex:96` | "knowledge distillation on these samples, applied through LoRA modules, then balances adaptation … against retention of the pretrained features" | **Partly wrong.** Distillation on the **buffer samples** happens in the KD-based **full** fine-tuning step (MSE to the frozen previous encoder E_t-1); the **LoRA** step distils E_t-mid into LoRA modules **on the new task data**, not on the buffer (Sec. III-D, p. 4). The teacher is the previous encoder, not the original pretrained model. |
| `thesis/related_work.tex:96` | "the low-rank updates are merged into the encoder weights so that each task begins from a single backbone" | **Correct** (Eq. 1, p. 4; step 4, p. 4). |
| `thesis/related_work.tex:96` | "Over five sequential CT tasks with a VoCo backbone, it exceeded full fine-tuning by 3.0 percentage points in mean DSC and reduced the 95th-percentile Hausdorff distance by 10.0 mm" | **Correct numbers** (Table II, p. 6: 68.3 vs 65.3; 50.4 vs 60.4 mm). Missing context: the "full fine-tuning" baseline is **parallel** FFT from the pretrained model; against vanilla **sequential** FFT the gain is 2.2 points and 5.6 mm (Table III, own calc 68.3 − 66.1, 56.0 − 50.4). |
| `thesis/related_work.tex:96` | "it transferred better than full fine-tuning to unseen segmentation tasks" | **Partly correct.** Better on COVID-19-20 and kidney tumour, marginally worse on kidney organ (96.3 vs 96.4 Dice, 4.5 vs 4.0 mm) (Table VI, p. 8). Also: the comparison is FFT from the refined vs from the original pretrained model, not MedSeqFT vs FFT on the unseen task. |
| `thesis/related_work.tex:96` | "the closest to the class-incremental strategies compared in this thesis, all of which adapt a single set of parameters shared across tasks" | **Partly wrong.** The encoder is shared and carried forward, but each task gets a new randomly initialised segmentation head (p. 4, p. 7) and results are per-task models M_t; earlier tasks are never re-evaluated after later ones (Sec. III-A, Tables II–V). The paper does not call its setting class-incremental. |
| `thesis/related_work.tex:102–104` (% SUMMARY TABLE) | "VoCo backbone, Liver -> HepaV -> Pancreas -> Colon -> Lung; mean DSC 68.3 % (FFT 65.3 %), HD95 50.4 mm (FFT 60.4 mm); further 5 MRI datasets (Table V) and 2 transfer datasets" | **Mostly correct.** Numbers correct (Table II). Order: only Liver as first task is stated (p. 7); the rest is the table order, not stated as the training order. Also UniMiSS+ backbone (Table IV) is missing. |
| `thesis/related_work.tex:115` | "MedSeqFT adapts a segmentation foundation model that has no language interface" | **Partly correct.** No language interface: correct. VoCo and UniMiSS+ are **self-supervised** pretrained backbones, not segmentation foundation models in the sense of a pretrained segmenter (p. 5); segmentation heads are trained from scratch per task (p. 4). |
| `thesis/related_work.tex:214` (summary table) | Data "Five CT tasks"; approach "Sample buffer, LoRA distillation, merged updates"; result "DSC 68.3 % (FFT 65.3 %)" | **Partly correct.** Result correct (Table II). Data incomplete: also 5 MRI tasks and 2 unseen CT transfer tasks (Table I). Approach omits that the main adaptation is full fine-tuning with feature distillation on the buffer (p. 4). |
| `thesis/related_work.tex:234` (positioning table) | Language none; 3D FM yes; few-shot no; "sequential tasks"; strategies "Proposed method, full fine-tuning" | **Partly correct.** Language/3D/few-shot/setting correct (Table I 80:20 splits). Strategies incomplete: TFS, FFT, ACNorm, six PEFT methods (head FT, LoRA, Adapter, Conv-Adapter, Med-Adapter, Mona), two multi-task methods (MTLoRA, UniSeg), and vanilla Seq. FT in the ablation (Table II–III, p. 5–6). |

## 10. Analysis for this thesis (NOT from the paper; verify before using)
1. **Relation to this thesis:** shares the idea of adapting one pretrained 3D model over a sequence of segmentation tasks with a single carried-forward encoder, and uses LoRA and distillation. But the goal differs: MedSeqFT optimises **per-task performance of the current model M_t** and the transferability of the refined backbone; it does **not** measure forgetting of earlier tasks (no evaluation matrix, no BWT/forgetting), uses a new head per task, full training sets (not few-shot), one task order, no seeds/variance, and a backbone without text input.
2. **Gap claim** ("no prior work has studied the continual adaptation of a free-text promptable 3D medical segmentation model"): **not weakened.** VoCo and UniMiSS+ have no language interface and are not promptable (Sec. IV-B, p. 5).
3. Facts usable for the gap/positioning: (a) not few-shot (80:20 splits, Table I); (b) no forgetting measurement of earlier tasks; the "catastrophic forgetting" addressed is loss of pretrained/previous representation, judged only by current-task Dice and unseen-task transfer (Sec. III-D, V-A); (c) task-specific heads, so it is not comparable to a single shared-parameter, prompt-selected model.
4. Possible support for design decisions: rank r = 2 LoRA as a strong "hard constraint" against representational drift (p. 5); vanilla sequential FFT beating parallel FFT (Table III) is the opposite emphasis to this thesis, which measures forgetting of earlier tasks.
5. Positioning table: "sequential tasks" is fair; consider adding "no forgetting evaluation" and "per-task heads". The phrase "closest to the class-incremental strategies" in l. 96 should be reconsidered (see §9).
6. Bib: arXiv only; check whether a peer-reviewed (e.g. IEEE TMI) version exists before adding the entry.
