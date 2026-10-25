# SAT (Segment Anything with Text) — fact card (tier B)
| | |
|---|---|
| Paper | Z. Zhao, Y. Zhang, C. Wu et al., "Large-Vocabulary Segmentation for Medical Images with Text Prompts", arXiv:2312.17183v5 (18 Jul 2025); 74 pages (main text pp. 1–22, supplement pp. 33 ff.) |
| Bib key / Local PDF | zhao2025sat / papers/t1_text_promptable/zhao2025sat.pdf |
| Version read | arXiv v5; no peer-reviewed venue stated in the PDF |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: one 3D segmentation model for many targets across CT, MRI and PET, prompted by medical terminology as text instead of spatial prompts or one model per dataset (Abstract; Sec. 1; Fig. 1).
- Data (Sec. 4.2, p. 16; Sec. 4.6): SAT-DS, 72 public datasets, 22,186 3D scans (CT, MRI, PET), 302,033 annotations, 497 classes, 8 body regions; 80/20 train/test split per dataset. SAT-DS-Nano subset: 49 datasets, 13,303 images, 429 classes. External: AbdomenAtlas 1.1 and LiQA, excluded from training (Sec. 2, p. 4). Knowledge: 6,502 anatomy concepts with definitions, UMLS terms and relations (Sec. 4.1).
- Method (two sentences): a text encoder (12-layer BERT pre-trained on PubMed) and a 3D U-Net visual encoder are first aligned by contrastive learning on a multimodal anatomy knowledge tree (definitions, relations, atlas segmentations) (Sec. 4.4; Suppl. A.1, p. 33). For segmentation, the text embedding of a term is refined by a 6-layer transformer query decoder attending to multi-scale U-Net features and dotted with per-voxel decoder features to give a sigmoid mask (Sec. 4.5, Eq. 6–9). Two sizes: SAT-Nano (110M) and SAT-Pro (447M) (Abstract).
- Setting: text conditioning by medical terms from the fixed 497-class vocabulary; free-form reports or conversations are handled by GPT-4 extracting terms from a terminology list (Sec. 2.6, Fig. 9); no continual learning; no few-shot. SAT-Ft = SAT-Pro fine-tuned per dataset (Sec. 2.1).
- Evaluation: DSC and NSD (tolerance 1), class-, region- and dataset-wise macro averages (Sec. 4.8–4.9). Baselines: 72 nnU-Nets, U-Mamba, SwinUNETR (one per dataset), MedSAM (tight/loose boxes), BiomedParse (Sec. 4.7).
- Best result: average DSC over 497 classes SAT-Pro 78.81 vs nnU-Nets 80.54, U-Mamba 79.80, SwinUNETR 75.01; "comparable" to nnU-Nets (paired t-test p > 0.09) with about 1/5 of their combined parameters (447M vs 2.2B+); SAT-Ft 81.41 (Suppl. Table 3, p. 39; Sec. 2.1). Vs MedSAM (Tight) on 32 datasets: DSC 82.47 vs 75.39 (Suppl. Table 4), +7.1 % in the abstract. Vs BiomedParse on 11 datasets: better on 29 of 30 categories (Sec. 2.3). External: +2.9 DSC over second-best MedSAM (Sec. 2.4), +3.7 % average DSC over baselines (Abstract). Knowledge-injected text encoder: +1.54 DSC over other encoders on SAT-DS-Nano (Sec. 2.5).
- Limitations stated by the authors (Sec. 3, p. 14): still behind specialists (e.g. nnU-Nets) in some regions; limited generalisation to unseen categories, incl. unseen lesions (open-vocabulary left to future work); deployment speed; demographic and regional dataset bias. Internal: lesions remain weak (Lesion DSC 51.39 vs nnU-Nets 57.52, Suppl. Table 3).

## Check of the author's notes
- related_work.tex:34 "SAT ... combines a 3D U-Net visual backbone, a knowledge-injected 12-layer BERT text encoder, and a Transformer query decoder to align textual queries with 3D visual features" → correct (Sec. 4.4–4.5; Suppl. A.1).
- related_work.tex:34 "Trained on 22,186 3D scans across 72 datasets covering 497 segmentation categories" → correct (Sec. 4.2).
- related_work.tex:34 "the model in its SAT-Pro configuration matched an ensemble of 72 specialist nnU-Nets" → partly correct: the paper says "comparable" (no significant difference, p > 0.09), but the mean DSC is lower (78.81 vs 80.54; Suppl. Table 3). "Matched" overstates; "comparable to" is the paper's word.
- related_work.tex:34 "and showed improved zero-shot generalisation on external multi-centre datasets" → partly correct: SAT-Pro is best on the two external datasets (AbdomenAtlas 1.1, LiQA) (Sec. 2.4), but these test unseen centres with known classes; the paper does not call this zero-shot and states it "does not involve new classes" (Sec. 2, p. 4). "Zero-shot" should be replaced by "cross-centre".
- related_work.tex:38 "SAT conditions segmentation on terms from a fixed vocabulary of categories, so that free-form input such as a radiology report must first be mapped to these terms by an external language model" → correct (Sec. 2.6, Fig. 9; Sec. 3 limitation ii).
- related_work.tex:164 (table) "22,186 scans, 497 categories | Concept prompts; 3D U-Net, BERT, query decoder | Matches 72 nnU-Nets" → partly correct; better "Comparable to 72 nnU-Nets (DSC 78.81 vs 80.54)".
- introduction.tex:3 (cited with others) "text-promptable universal models ... designed to support segmentation across multiple structures, modalities, and tasks" → correct.
- introduction.tex:3 "text-promptable universal models can still exhibit reduced performance on previously unseen tasks, particularly when the target task or imaging characteristics differ substantially from those represented during pretraining" → partly supported: SAT states limited generalisation to unseen categories (Sec. 3, ii); it does not discuss unseen imaging characteristics as a cause.
- introduction.tex:11 "deploying separate models for an increasing number of anatomical structures, modalities, and datasets becomes less practical" → correct (Sec. 1, p. 1; Sec. 3, p. 12; Fig. 3c: each specialist covers 12 classes on average).
- Additional support available: SAT Sec. 2.3 (p. 8) attributes BiomedParse's false positives to its 2D slice-wise design; this could back the author's claim at related_work.tex:34 that slice-wise processing limits BiomedParse on volumes.

## Relevance (NOT from the paper)
The main 3D text-promptable baseline before VoxTell: large closed vocabulary, term-level prompts, no free-text sentences; it shows SAT-Ft (per-dataset fine-tuning) helps, but not how adaptation affects other classes.
