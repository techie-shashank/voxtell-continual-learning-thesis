# Continual Segment — fact card (tier B)
| | |
|---|---|
| Paper | Z. Ji, D. Guo, P. Wang et al., "Continual Segment: Towards a Single, Unified and Non-forgetting Continual Segmentation Model of 143 Whole-body Organs in CT Scans", arXiv:2302.00162v4 (3 Sep 2023); 21 pages (main paper pp. 1–8, references to p. 11) |
| Bib key / Local PDF | ji2023continualsegmentsingleunified / papers/t5_cl_medseg_networks/ji2023continualsegmentsingleunified.pdf |
| Version read | arXiv v4; p. 1 footnote: "accepted by ICCV 2023". Note: the bib title says "Single, Unified and Accessible", the v4 PDF says "Single, Unified and Non-forgetting" |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: continual semantic segmentation (CSS) of organs in CT: new organ classes arrive dataset by dataset, earlier datasets are not accessible; datasets are partially labelled (background-label conflict) and differ by body part (Sec. 1, p. 1–2; Sec. 3 problem formulation).
- Data (Sec. 4 "Datasets", p. 5–6): four partially labelled 3D CT datasets, 2583 unique patients, 143 organ classes in total: TotalSegmentator (public) 1204 scans, 103 structures (face label removed); ChestOrgan (in-house) 292 scans, 31 chest structures (4 overlap with TotalSegmentator); HNOrgan 447 head-and-neck scans, 13 OARs; EsoOrgan 640 esophageal cancer scans, 1 label (esophagus). 20 % of each dataset held out as test set. Auxiliary tumour head trained on 304 esophageal (private) and 625 lung cancer (public) CTs.
- Method (two sentences): a General Encoder plus decoder is trained on the first dataset (TotalSegmentator, with auxiliary body-part and tumour heads), then the encoder is frozen and one new decoder per later dataset is added, each optimised by NAS and pruned by block-wise teacher–student distillation (Sec. 3.1–3.2, Fig. 2–3). Predictions of all decoders are combined by a rule-based body-part- and anomaly-aware merging module (Sec. 3.3, Eq. 3–6).
- Setting: no text conditioning (fixed class outputs per decoder); "continual semantic segmentation", class-incremental across datasets, architecture-based; two task orders (A: TotalSeg → ChestOrgan → HNOrgan → EsoOrgan; B: TotalSeg → HNOrgan → ChestOrgan → EsoOrgan); no few-shot (Sec. 4, p. 6).
- Evaluation: DSC (%), HD95 (mm), ASD (mm) after the last step on all datasets; baselines MiB, ILT (re-implemented with frozen encoder), PLOP, LISMO, RCIL, all re-implemented in nnU-Net; upper bound = one separate nnU-Net per dataset (Sec. 4, 4.1; Table 1). Hardware: one NVIDIA A100 (Sec. 4.1).
- Best result (Table 1, p. 6): All 143 classes, mean DSC 88.74 % (HD95 5.28 mm, ASD 1.14 mm) in both orders vs upper bound 89.02 % (4.41, 1.06); second-best RCIL 42.43 % (order A) / 39.85 % (order B); text: 0.28 % DSC below the upper bound (Sec. 4.2). Four pruned decoders total 14.669 MB, 0.98 of one original nnU-Net decoder (Table 1); running time +12 % vs one nnU-Net (Sec. 4.2). Without freezing the encoder, TotalSeg DSC drops from 93.24 % to 51.42 % after ChestOrgan (Table 2, Sec. 4.3).
- Limitations stated by the authors: none stated in a limitations section; the method is order-invariant only if the dataset used to train the General Encoder is the same (Sec. 4.2).

## Check of the author's notes
- related_work.tex:72 (cited for partial annotation: a structure annotated in one task may appear as unannotated background in a later dataset) → correct (Sec. 1, p. 2, "label conflict issue").
- related_work.tex:83 "Continual Segment instead shares a frozen general visual encoder across tasks and adds specialised decoders for new targets" → correct, but the encoder is trained on the first dataset (TotalSegmentator, step 1) and frozen afterwards; it is not a pre-existing general encoder (Sec. 3, 3.1).
- related_work.tex:83 "covering 143 whole-body organs across four partially annotated CT datasets containing more than 2,500 scans" → correct (2583 patients; Sec. 4).
- related_work.tex:83 "reported a mean DSC of 88.74 % against 89.02 % for an upper-bound ensemble of separately trained nnU-Net models" → partly correct: numbers correct (Table 1); the paper calls the upper bound four separate nnU-Net models, one per dataset, not an "ensemble" (the paper uses "Ensemble" for a different merging baseline in Table 4).
- related_work.tex:83 "Retention ... close to complete, since earlier components are never updated; the cost is that model size grows with the number of tasks" → partly correct: one decoder is added per task, but the paper prunes the decoders so that four decoders total 14.669 MB, 0.98 of one nnU-Net decoder (Table 1, Table 3). The growth claim needs this qualification. "Nothing learned for one task benefits the others" is the author's interpretation, not stated in the paper.
- related_work.tex:204 (table) "143 organs, >2,500 CT scans | Frozen encoder, added decoders | DSC 88.74 % (upper bound 89.02 %)" → correct.
- introduction.tex: not cited.
- Bib: the paper states acceptance at ICCV 2023; the bib entry is the arXiv @misc (peer-reviewed version exists per p. 1).

## Relevance (NOT from the paper)
Strongest example of architectural isolation for continual organ segmentation in 3D CT, with task-order comparison and an explicit separately-trained upper bound; contrasts with this thesis's single parameter set and few-shot regime (here, full datasets per task).
