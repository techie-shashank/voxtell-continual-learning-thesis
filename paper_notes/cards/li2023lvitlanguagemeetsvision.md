# LViT — fact card (tier B)
| | |
|---|---|
| Paper | Z. Li, Y. Li, Q. Li et al., "LViT: Language meets Vision Transformer in Medical Image Segmentation", arXiv:2206.14718v4 (27 Jun 2023); 12 pages |
| Bib key / Local PDF | li2023lvitlanguagemeetsvision / papers/t1_text_promptable/li2023lvitlanguagemeetsvision.pdf |
| Version read | arXiv v4 (IEEE-style layout); the PDF does not state a venue. A peer-reviewed journal version may exist; check before citing (bib entry is arXiv @misc) |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: 2D medical image segmentation with scarce, costly labels; medical text annotations are used to compensate for image-data deficiencies and to improve pseudo-labels in semi-supervised learning (Abstract; Sec. I).
- Data (Sec. IV-A, Table I, p. 6): QaTa-COV19, 9258 COVID-19 chest X-rays (train 5716 / val 1429 / test 2113), text annotations added by the authors; MosMedData+, 2729 CT slices of lung infection (2183 / 273 / 273); ESO-CT, 286 esophageal cancer CT cases collected by the authors (182 / 46 / 58) (Sec. IV-F). One foreground class (C = 1, Sec. IV-A). Text: structured descriptions of infection side, number of areas and location, verified by radiologists.
- Method (two sentences): double-U architecture with a U-shaped CNN branch (produces the mask) and a U-shaped ViT branch that merges image features with text vectors from a BERT embedding layer (no separate text encoder); a Pixel-Level Attention Module (PLAM) sits on the CNN skip connections (Sec. III-A, Fig. 2). For semi-supervised training, an Exponential Pseudo-label Iteration (EPI, EMA of predictions) and a Language-Vision (LV) loss that compares the pseudo-label with the mask of the most text-similar labelled case are used on unlabelled images (Sec. III-B, III-C).
- Setting: text conditioning by structured free-text annotations, required as input at inference as well (Sec. III, p. 3; Sec. V); 2D only (Sec. V); no continual learning; semi-supervised label ratios 25 % and 50 % (not few-shot).
- Evaluation: Dice (%) and mIoU (%); baselines U-Net, UNet++, AttUNet, nnUNet, TransUNet, Swin-Unet, UCTransNet, ConVIRT, TGANet, CLIP, GLoRIA, ViLT, LAVT; semi-supervised DTC, PLCT, MC-Net+ (Tables II, VII, VIII).
- Best result (Table II, p. 7): LViT-T (100 % labels) Dice 83.66 % / mIoU 75.11 % on QaTa-COV19 (best non-text baseline nnUNet 80.42 / 70.81) and 74.57 / 61.33 on MosMedData+ (nnUNet 72.59 / 60.36). LViT-T (1/4 labels) 80.95 / 71.31 on QaTa-COV19. ESO-CT: LViT-T 71.53 / 59.94 vs nnUNet 68.38 / 56.10 (Table VIII).
- Limitations stated by the authors: 2D model only; text input is needed at inference (Sec. V, p. 11).

## Check of the author's notes
- related_work.tex:25 "Early integrations of natural language use textual annotations as an auxiliary semantic supervision signal during training ... LViT combines a U-shaped convolutional branch with a Vision Transformer branch, fuses visual and textual tokens through pixel-level attention" → partly correct. (a) Text is not only a training signal: LViT needs the text as an input at inference (Sec. III, p. 3; Sec. V). (b) Text and image features are merged in the ViT branch; PLAM is a channel/spatial attention on the CNN skip connections, not the place where text and image tokens are fused (Sec. III-A.2–3, Fig. 2).
- related_work.tex:25 "and uses a language–vision loss together with iterative pseudo-labelling to exploit unlabelled images" → correct (EPI + LV loss, Sec. III-B, III-C).
- related_work.tex:25 "reporting improvements over the corresponding baselines on X-ray and CT datasets" → correct but vague; the data are 2D (X-rays and CT slices); concrete numbers in Table II (83.66 % Dice on QaTa-COV19).
- related_work.tex:152 (table) "X-ray, CT | Auxiliary text supervision; CNN–ViT fusion, pseudo-labels | Gains over baselines" → partly correct: "auxiliary" understates that text is a required input; add "2D" and a number.
- introduction.tex: not cited.

## Relevance (NOT from the paper)
Early example of text as an extra input for medical segmentation with limited labels (25–50 %), but 2D, single-target per dataset and with structured descriptions, so text does not select the target structure as in free-text promptable universal models.
