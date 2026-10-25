# TextMatch — fact card (tier B)
| | |
|---|---|
| Paper | A. Li, X. Zeng, P. Zeng, S. Ding, P. Wang, C. Wang, Y. Wang, "Textmatch: Using Text Prompts to Improve Semi-supervised Medical Image Segmentation"; 10 pages incl. references |
| Bib key / Local PDF | textmatch2024 / papers/t1_text_promptable/textmatch2024.pdf |
| Version read | Manuscript PDF without venue header or page numbers of the proceedings (pp. 1–10); the bib entry gives MICCAI 2024, LNCS, pp. 699–709, which the PDF itself does not state |
| Written | 2026-10-23, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: semi-supervised 2D medical image segmentation (few labelled, many unlabelled images) in which every image, labelled or not, comes with a text prompt; the text is used to reduce pseudo-label noise and to structure the feature space (Abstract; Sec. 1, pp. 2–3; Sec. 2 "Problem Setting", p. 4).
- Data (Sec. 3, p. 6): QaTa-COV19, 9258 chest X-ray radiographs with manual COVID-19 lesion masks; MosMedData+, 2729 CT slices of lung infection. Text prompts are those extended by Li et al. (LViT) and describe whether both lungs are infected, the number of lesion regions and their approximate location. Labelled fractions 5 %, 15 %, 25 %, following earlier work (p. 6). Number of test images: not stated.
- Method (two sentences): a Mean Teacher framework (student and EMA teacher) with a ConvNeXt-Tiny image encoder, a BERT text encoder and several Bilateral Prompt Decoders that refine visual and text tokens through multi-head attention in both directions before a segmentation head (Sec. 2, pp. 3–4, Eq. 1–5; Sec. 3 "Implementation Details", p. 6). Unlabelled pairs are perturbed in image and text (GPT-generated paraphrases, N = 3 views) for an MSE consistency loss, the averaged teacher prediction is a Dice-supervised pseudo-label, and the pseudo-labels drive an InfoNCE contrastive loss towards foreground/background prototypes (Sec. 2, Eq. 6–12, pp. 4–6).
- Setting: 2D images only; binary lesion segmentation (foreground/background prototypes, Eq. 9); text prompts are available at training and test time; no continual learning; "few labelled" means a percentage of the training set, not a number of shots. Training: Adam, batch size 48, learning rate 3e-4, temperature 0.9, λ1 = λ3 = 0.1, λ2 = 0.1 (QaTa) / 0.5 (MosMed), four RTX 2080Ti GPUs (p. 6).
- Evaluation: Dice and mIoU in % (p. 6). Baselines: image-only MC-Net+ and PLCT; image+text LAVT, TGCPA, LViT-T (Table 1, p. 7).
- Best result (Table 1, p. 7): QaTa-COV19 Dice / mIoU 83.56 / 71.67 (5 %), 86.21 / 75.64 (15 %), 87.26 / 77.12 (25 %); best previous multi-modal LViT-T 77.24 / 66.31 at 5 %. MosMedData+ 72.46 / 58.12 (5 %), 75.73 / 60.93 (15 %), 76.46 / 62.69 (25 %). Average gains: +10.19 % (QaTa) and +5.03 % (MosMed) over the best image-only method, +5.94 % and +2.92 % over existing multi-modal methods (pp. 6–7). With 5 % labels it reaches or exceeds the multi-modal baselines trained with 25 % (p. 7). Ablation (Table 2, p. 8): baseline 75.14 Dice at 5 %, BPD adds on average 3.88 % Dice; each module contributes.
- Limitations stated by the authors: none stated (Sec. 4, p. 8 is a summary only). Not stated: variability over runs or label subsets, test-set sizes.

## Check of the author's notes
- related_work.tex:25 "TextMatch extends this semi-supervised principle within a Mean Teacher framework" → correct (Sec. 2, p. 3); LViT-T is one of its baselines (Table 1).
- related_work.tex:25 "through bidirectional image--text attention" → correct: the Bilateral Prompt Decoder refines both modalities by mutual prompting with multi-head attention (Sec. 2, Eq. 2–3, p. 4).
- related_work.tex:25 "consistency regularisation over augmented image--text views" → correct (MCR, Eq. 6–7, p. 4).
- related_work.tex:25 "and pseudo-label guided contrastive learning" → correct (PGCL, Eq. 9–11, p. 5).
- related_work.tex:25 "reaching a Dice similarity coefficient (DSC) of 83.56 % on QaTa-COV19 with 5 % labelled data" → correct (Table 1, p. 7). The paper calls the metric "Dice".
- related_work.tex:25 (paragraph frame) "Early integrations of natural language use textual annotations as an auxiliary semantic supervision signal during training ... reduce the pixel- or voxel-level annotation required" → partly correct for TextMatch: the text prompt is also an input at inference (both encoders feed the decoder, Fig. 1, Sec. 2), so it is not supervision only; and TextMatch is 2D, so "voxel-level" does not apply to it.
- related_work.tex:154 (table) "QaTa-COV19, 5 % labelled | Auxiliary text supervision; Mean Teacher | DSC 83.56 %" → correct for the number; "auxiliary text supervision" is partly correct for the reason above. The row could also mention MosMedData+ (72.46 % at 5 %, Table 1) and that the data are 2D.
- introduction.tex: not cited (grep, 2026-10-23).

## Relevance (NOT from the paper)
An example of text helping when labels are scarce, but in 2D binary lesion segmentation with semi-supervision (unlabelled data available), not in 3D few-shot adaptation of a pretrained universal model and without any forgetting analysis.
