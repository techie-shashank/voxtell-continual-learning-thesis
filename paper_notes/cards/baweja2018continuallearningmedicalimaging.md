# Baweja et al. (EWC for brain MRI) — fact card (tier B)
| | |
|---|---|
| Paper | C. Baweja, B. Glocker, K. Kamnitsas, "Towards continual learning in medical imaging", Medical Imaging meets NIPS Workshop (NIPS 2018), arXiv:1811.02496v1; 4 pages |
| Bib key / Local PDF | baweja2018continuallearningmedicalimaging / papers/t5_cl_medseg_networks/baweja2018continuallearningmedicalimaging.pdf |
| Version read | arXiv v1 (6 Nov 2018); footer names the Medical Imaging meets NIPS Workshop (workshop paper, p. 1) |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: two segmentation tasks in brain MRI learned one after the other; task A = CSF, grey matter, white matter (multi-class), task B = white matter lesions (WML); data of task A not available while learning B (Sec. 1, Sec. 3.1, p. 1–2).
- Data: UK Biobank, T1 and FLAIR MRI, 3D; 275 cases with WML selected: 87 for training task A, 88 for training task B, 100 for validation of both (Sec. 3.1, p. 2). Classes: 3 (task A) + 1 (task B).
- Method (two sentences): Elastic Weight Consolidation (EWC) adds a penalty that keeps parameters with high diagonal Fisher information for task A close to their task-A values while training on task B (Sec. 2, Eq. 2–3). Network is DeepMedic (3D CNN, default configuration); a new classification layer is added for task B (Sec. 3.1, p. 3).
- Setting: no text conditioning; sequential learning of two tasks with different label spaces (the paper calls it continual/lifelong learning; no scenario name); no few-shot.
- Evaluation: DSC (%) per class on 100 validation cases. Compared: DM-A and DM-B (single-task from scratch), multi-task joint training (stated upper bound), fine-tuning, L2 regulariser (λ = 0.005, 0.01, 0.1), EWC (λ = 10^6, 10^7) (Sec. 3.1–3.2, p. 3).
- Best result (Fig. 2 table, p. 3; text calls it "Table 2"): fine-tuning forgets task A (CSF/GM/WM 00.9/11.9/50.8, WML 62.1). EWC λ = 10^7: 79.2/88.7/94.4, WML 44.5; EWC λ = 10^6: 60.1/32.6/62.5, WML 53.4. Multi-task upper bound: 88.9/92.2/94.8, WML 63.8. At similar task-B DSC, EWC keeps more task-A DSC than L2 (Sec. 3.2).
- Limitations stated by the authors: a gap to the multi-task upper bound remains; large room for improvement before continual learning is practical (Abstract; Sec. 3.2; Sec. 4).

## Check of the author's notes
- related_work.tex:77 "Baweja et al. applied Elastic Weight Consolidation (EWC) to sequential brain MRI segmentation on UK Biobank data, reducing the degradation caused by unconstrained fine-tuning while remaining below joint training" → correct (Sec. 3.1–3.2, Fig. 2 table). Could add that the two tasks have different label spaces (tissue classes, then WML) and that EWC trades task-B DSC (44.5–53.4 vs 62.1 fine-tune) for retention.
- related_work.tex:192 (table row) "UK Biobank brain MRI | EWC | Below joint training" → correct.
- introduction.tex: not cited.

## Relevance (NOT from the paper)
Early, minimal example of regularisation-based continual segmentation in 3D MRI with a two-task sequence and explicit fine-tuning and joint-training reference points; shows the adaptation–retention trade-off controlled by λ.
