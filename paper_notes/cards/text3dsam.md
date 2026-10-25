# Text3DSAM — fact card (tier B)
| | |
|---|---|
| Paper | Y. Xin, G. C. Ates, W. Shao, "Text3DSAM: Text-Guided 3D Medical Image Segmentation Using SAM-Inspired Architecture", in J. Ma et al. (eds.), MedSegFM 2025, LNCS 16447, pp. 194–207, Springer, 2026, doi:10.1007/978-3-032-23496-4_11 |
| Bib key / Local PDF | text3dsam / papers/t1_text_promptable/text3dsam.pdf |
| Version read | Published Springer version (copyright line and LNCS page numbers on p. 194) |
| Written | 2026-10-23, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: 3D segmentation across modalities guided only by a text description of the target, without spatial prompts or a fixed class set (Abstract; Sec. 1, p. 195). Developed for a challenge: the development set extends the CVPR 2024 MedSAM on Laptop Challenge with further public 3D cases; hidden test set unpublished (Sec. 3.1, p. 199).
- Data: "over 200,000 3D image-mask pairs" across CT, MRI, PET, ultrasound and microscopy (Abstract; Sec. 1, p. 195); no per-dataset or per-class breakdown in the paper (dataset list only via a URL, footnote 1, p. 199). All volumes resized to 128 × 256 × 256 (Sec. 3.2, p. 200). Results are on the open validation set of the all-data track (Table 3).
- Method (two sentences): a DCFormer-based 3D image encoder (decomposed 3D convolutions plus one appended transformer layer), a TinyClinicalBERT text encoder, a prompt encoder that turns the text embedding (and, in later passes, the previous mask and SAM tokens) into sparse and dense embeddings, and a SAM-style transformer mask decoder with hypernetwork mask heads and a SegVol-inspired text–feature similarity map (Sec. 2.1–2.3, pp. 196–198; Sec. 3.2, p. 201). Prediction is coarse-to-fine: one text-only pass plus two refinement passes that feed back the mask (Sec. 2.2; Sec. 3.2, p. 201).
- Setting: text prompts are drawn at random from a predefined prompt file per class ID (e.g. "liver in abdominal CT") (Sec. 2, p. 195; Sec. 3.2, p. 201); trained once on the full data (30 epochs, AdamW, lr 1e-4, batch 16 per device, 16 × A100 80 GB, 15 h; 59.30 M parameters; Table 2, p. 201). Loss Dice + Focal (Sec. 2.4). No continual learning, no few-shot adaptation. The introduction claims "zero-shot generalization to unseen classes" (p. 195), but no experiment on unseen classes is reported.
- Evaluation: DSC and NSD for semantic, F1 at IoU 0.5 for instance segmentation; runtime cap 60 s per class (Sec. 3.1, p. 200). Baselines: CAT and SAT (Table 3). NSD values are not reported in the tables.
- Best result (Table 3, p. 204; PDF checked): average DSC 0.6091 vs SAT 0.5573 and CAT 0.5316; average F1_50 0.1131 vs CAT 0.1935 and SAT 0.0956, i.e. CAT has the higher F1. Per modality DSC: CT 0.6707 (SAT 0.6432, CAT 0.6035), MRI 0.5214 (SAT 0.4526), ultrasound 0.8337 (CAT 0.8180); microscopy and PET are instance tasks only, where SAT has the highest F1 (0.2475, 0.2623). The abstract nevertheless says it outperforms CAT "(Dice 0.5316, F1 50 0.1935)" (p. 194), which the F1 numbers contradict. Ablation: 2 passes best on average (DSC 0.5816 / 0.6091 / 0.5974 for 1 / 2 / 3 passes, Table 4, p. 205).
- Limitations stated by the authors (Sec. 4.1, p. 202; Sec. 6, pp. 204–205): weak instance segmentation and small objects due to coarse mask resolution; the fusion does not always interpret the prompt correctly (wrong structure segmented); failures on low-contrast microscopy and PET. Not stated: variability over runs, results on the hidden test set.

## Check of the author's notes
- introduction.tex:3 (cited with SAT, BiomedParse/Zhao_2024, VoxTell) "Deep learning-based segmentation has progressed from task-specific models developed for individual datasets towards text-promptable universal models designed to support segmentation across multiple structures, modalities, and tasks" → correct: one model, text-only prompts, five modalities (Abstract; Sec. 1, p. 195).
- related_work.tex: not cited and not named (grep, 2026-10-23); no summary-table row.

## Relevance (NOT from the paper)
A recent 3D text-promptable model comparable in scope to SAT and VoxTell, useful as evidence that the field moves towards universal text-promptable models; its prompts are short template descriptions per class, and its results are from a challenge validation set without variability, so it supports the trend statement but not claims about free-text robustness.
