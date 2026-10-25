# R-Super — fact card (tier B)
| | |
|---|---|
| Paper | P. R. A. S. Bassi, W. Li, J. Chen et al., "Learning Segmentation from Radiology Reports", arXiv:2507.05582v1 (8 Jul 2025); 13 pages (text pp. 1–10) |
| Bib key / Local PDF | bassi2025learningsegmentationradiologyreports / papers/t1_text_promptable/bassi2025learningsegmentationradiologyreports.pdf |
| Version read | arXiv v1 (LNCS-style layout); no peer-reviewed venue stated in the PDF |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: 3D tumour segmentation in abdominal CT (pancreatic and kidney tumours) when masks are scarce but CT–report pairs are plentiful; use radiology reports to supervise segmentation directly (Abstract; Sec. 1).
- Data (Sec. 3 "Datasets", p. 7–8): AbdomenAtlas 2.0, 9,262 CT–mask pairs (344 pancreatic, 1,674 kidney tumour CTs); AbdomenAtlas-Small subset (50 pancreatic, 50 kidney tumour, 100 normal CTs); UCSF-Train (private) 6,718 CT–report pairs without masks (2,229 pancreatic, 2,738 kidney tumour, 1,751 normal); UCSF-Test 169 kidney tumour, 139 pancreatic tumour, 100 normal CTs; JHH-Test (external, unseen hospital) 50 pancreatic tumour + 50 normal CTs. Training used 50, 344 or 1.7K masks plus 2.2K pancreatic / 2.7K kidney tumour reports (Fig. 4 caption).
- Method (two sentences): a zero-shot LLM (Llama 3.1 70B AWQ) extracts tumour count, location (organ/sub-segment) and diameters from each report (Sec. 2, p. 2). Two losses turn these into voxel-wise supervision: a Volume Loss on an intermediate layer matching segmented tumour volume per organ to the report-derived volume (with 10 % tolerance), and a Ball Loss on the output that places top-N voxels within a "highest probability ball" per reported tumour (Sec. 2.1–2.2, Eq. 1–5, Fig. 1–2). Segmenter: MedFormer (Sec. 3).
- Setting: reports are a training signal only; no text conditioning at inference (fixed tumour outputs); no continual learning; low-mask regime with 50 masks per tumour type (not called few-shot).
- Evaluation: F1-Score (tumour detection), AUC, sensitivity, specificity, DSC and NSD (DSC/NSD only on JHH-Test); baselines: standard segmentation, nnU-Net, Models Genesis, multi-task learning, report-guided pseudo-labels, CLIP-like (Table 1–2). Significance: paired permutation test (F1) and DeLong (AUC), p < 0.05 (Table 2 caption).
- Best result: up to +16.0 F1 (%) over segmentation trained without reports on UCSF-Test pancreatic tumours with 344 masks; +9.7 with 50 masks; +4.3 on kidney with 1.7K masks; +9.2 on external JHH-Test (Fig. 4, p. 7; Sec. 1 contributions). JHH-Test pancreas with 344 masks: DSC 59, NSD 69, F1 91, AUC 92 vs segmentation 51/59/82/84 (Table 2).
- Limitations stated by the authors: reports give imperfect diameters (handled by tolerance) (Sec. 2.1); losses not applied where reports lack tumour sizes (<11 % of cases) (Sec. 2.2); requires pre-saved organ masks (Sec. 2.1, footnote 8). No limitations section.

## Check of the author's notes
- related_work.tex:25 "R-Super replaces short descriptions with unconstrained radiology reports, parsing them with a large language model into tumour count, location, and diameter, and converting these attributes into volume and ball losses that supervise 3D segmentation directly" → correct (Sec. 2). "Replaces short descriptions" is the author's framing relative to LViT/TextMatch, not a claim of the paper.
- related_work.tex:25 "trained on 6,718 CT–report pairs, it increased F1 scores by up to 16.0 % over mask-only training" → partly correct: UCSF-Train has 6,718 CT–report pairs, but the training used about 2.2K pancreatic and 2.7K kidney tumour reports plus 50–1.7K masks (Fig. 4 caption; Sec. 3 "Training"). +16.0 is in F1 percentage points, for pancreatic tumours on UCSF-Test with 344 masks (Fig. 4). Should say the reports supplement, not replace, the masks.
- related_work.tex:156 (table) "6,718 CT–report pairs | Losses derived from reports by an LLM | F1 up to +16.0 %" → partly correct, same caveats (masks also used; F1 points).
- introduction.tex: not cited.
- Placement: the paper has no text prompt at inference, so it is text-supervised segmentation, not text-promptable segmentation (consistent with the author's grouping under "auxiliary supervision").

## Relevance (NOT from the paper)
Shows radiology reports as weak 3D supervision that reduces the need for masks; relevant as an alternative route to label-efficient adaptation, but it conditions nothing on text at inference and does not address continual learning.
