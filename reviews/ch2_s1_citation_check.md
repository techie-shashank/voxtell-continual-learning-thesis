# Citation check: Chapter 2 intro and Section 2.1 (Text-Promptable Medical Image Segmentation)

File: `thesis/related_work.tex`, lines 13–65 (from `\chapter{State of the Art}` to before `\section{Continual Learning for Vision--Language Models}`).
Checked: 2026-10-23, by Claude (citation-verifier). Report only; no thesis or bib edits.

Sources used, in order: `paper_notes/voxtell.md`; `paper_notes/cards/<key>.md`; `papers/text/<key>.txt` (grep of the matching passages); `voxtell_paper/voxtell.pdf` (pdftotext). The CVPR 2026 open-access PDF and supplement of VoxTell returned HTTP 403, so the VoxTell checks are against arXiv v1 only.

The chapter intro (l. 16–19) has no citations and makes no factual claim about other work.

## Table

| line | key | locator | verdict | evidence (quote + location) | fix needed |
|---|---|---|---|---|---|
| 28 | Ma_2024 | – | SUPPORTED | "MedSAM is a promptable segmentation method where users can use bounding boxes to specify the segmentation targets" (Fig. 2b caption, papers/text/Ma_2024.txt l. 170–171) | – |
| 28 | cheng2023sammed2d | – | SUPPORTED | "more comprehensive prompts involving bounding boxes, points, and masks" (Abstract, txt l. 29–31) | Bib is arXiv @misc. Check whether a peer-reviewed version exists |
| 30 | radford2021learningtransferablevisualmodels | – | SUPPORTED | Cited only to identify CLIP. SegVol: "leveraging the text encoder from CLIP model" (Sec. 2.2, SegVol txt l. 192) | – |
| 30 | du2025segvoluniversalinteractivevolumetric | – | SUPPORTED | "Given a word or phrase as the text prompt, we complete it using the template 'A computerized tomography of a [text prompt]' … The off-the-shelf text encoder is frozen" (Sec. 2.2, txt l. 194–196). Point/box prompts via positional encoding (l. 197) | – |
| 31 | du2025segvoluniversalinteractivevolumetric | – | PARTLY | (a) "6K labeled CT volumes" (Abstract), "over 200 categories" (App., txt l. 937): OK. (b) 0.8593 vs 0.6668 (Table 2, p. 6): these are averages of per-category **median** Dice ("in terms of the median value of Dice score", Table 2 caption). SAM-Med2D used **point prompts with five-step correction**, not a box (txt l. 302–304). SegVol used "bounding box and text prompt" (l. 362). (c) "+5.85 %" is the paper's own wording ("boosted by 5.85%", Sec. 3.3, txt l. 467). It was measured on 19 tasks of the internal 20 % test split, not AMOS22, and the paper does not say whether it is relative or absolute | Say "average of per-class median DSC". Note that SAM-Med2D was prompted with points. Attach the 5.85 % to "the internal test split", or drop it. Do not write "percentage points" |
| 36 | li2023lvitlanguagemeetsvision | – | SUPPORTED (with caveat) | 83.66 % Dice on QaTa-COV19 (Table II, txt l. 536). The text annotations "were provided and verified by two professionals from the Department of Radiation Oncology" (txt l. 479–481) | 83.66 % is for **100 % labels** (LViT-T, Table II). The paragraph is about scarce labels, so either say "with all labels" or quote 80.95 % (1/4 labels). Bib is arXiv @misc; a journal version (IEEE TMI) probably exists, so verify it |
| 36 | textmatch2024 | – | SUPPORTED | QaTa-COV19 Dice 83.56 at 5 % labels (Table 1, p. 7). The prompts are those extended by LViT (Sec. 3, p. 6). Text is input at training and test time (card; Fig. 1, Sec. 2) | – |
| 37 | bassi2025learningsegmentationradiologyreports | – | SUPPORTED | An LLM extracts tumour count, location and diameters, which become Volume and Ball losses (Sec. 2). "few (50), medium (344) … masks … up to +16%" (contributions, txt l. 84–86). Fig. 4: +16.0 F1 (%) on UCSF-Test pancreas (l. 325) | Optional: note that the reports came from 2.2K pancreatic CTs (Fig. 4 caption). Bib is arXiv @misc |
| 41 | Liu_2023 | – | SUPPORTED | "A computerized tomography of a [CLS]" (Table 1, txt l. 170). The text-based controller generates the parameters of the class-wise output convolutions (Sec. 3.2) | Simplification: the controller input is the CLIP embedding **concatenated with pooled image features**. Acceptable as written |
| 42 | Liu_2023 | – | SUPPORTED | "14 public datasets of 3,410 CT scans … 25 organs and 6 types of tumors" (Fig. 2 caption, txt l. 109–110). BTCV: Universal Model 86.13 vs Swin UNETR 82.06 (Table 3, txt l. 308–310; BTCV 5-fold validation, l. 272) | Numbers are from arXiv v5; the bib cites ICCV 2023. Check them against the ICCV version |
| 43 | zhao2025sat | – | SUPPORTED | Knowledge-enhanced text encoder (BERT, PubMed), 497 classes, 6-layer query decoder on 3D U-Net features (Sec. 4.2, 4.4–4.5; card) | – |
| 44 | zhao2025sat | – | PARTLY | 78.81 vs 80.54, "comparable" (p > 0.09) and "approximately 1/5 of the ensemble of nnU-Nets" (txt l. 259–264; Suppl. Table 3) are supported. The paper uses "comparable" itself. But **"Trained on 22,186 scans"** is not right: SAT-DS has 22,186 scans, and each dataset was split "80% for training and 20% for testing" (txt l. 987) | "built from 22,186 scans (80 % used for training)", or "a collection of 22,186 scans". Bib is arXiv @misc; check for a peer-reviewed version |
| 45 | zhao2025sat | – | SUPPORTED | GPT-4 maps reports and conversations to SAT terms (Sec. 2.6, Fig. 9, txt l. 479–482). The fixed vocabulary is stated as a limitation (Sec. 3) | – |
| 46 | text3dsam | – | SUPPORTED | "average Dice of 0.6091 … on the open validation set, outperforming … SAT (Dice 0.5573 …)" (Abstract, txt l. 25–27; Table 3, p. 204). Prompts come "from a predefined text prompt file" per class ID (Sec. 3.2, txt l. 301–302) | The paper does not name the challenge as one "on text-guided 3D segmentation". It says the development set extends the MedSAM on Laptop Challenge, all-data track (Sec. 3.1). Use "a 3D segmentation challenge (all-data track)", or cite the challenge. The SAT number is a challenge baseline |
| 50 | zhao2025foundation-9de | – | SUPPORTED (with caveat) | "45 publicly available biomedical segmentation datasets across 9 imaging modalities, comprising 1.1 million images" (txt l. 347–348), "82 … object types" (l. 27). On 102,855 test triples it beats "MedSAM with oracle bounding box as input (paired t-test p-value < 10-4)" (l. 172–175) | 1.1 M images is the whole dataset (80/20 split), so write "a dataset of about 1.1 million images". The source read is the arXiv v3 preprint under a different title; the bib points to Nature Methods 2025. Check the numbers there. Duplicate bib entry `Zhao_2024` (same DOI) |
| 51 | zhao2025foundation-9de | – | SUPPORTED | "BiomedParse currently treats non-2D modalities such as CT and MRI by reducing them to 2D slices, thus …" (Discussion, txt l. 334) | – |
| 51 | zhao2025sat | – | SUPPORTED (with caveat) | "SAT-Pro consistently outperforms BiomedParse in all 30 categories except myocardium" (Sec. 2.3, txt l. 361–362). This is on 11 of the 72 datasets | It is SAT-Pro against BiomedParse **without oracle**. Against BiomedParse (Oracle) the count is 23 of 30 (l. 363). Name SAT-Pro and the non-oracle setting |
| 52 | carion2026sam3segmentconcepts | – | SUPPORTED | Cited to identify SAM 3. Title matches arXiv:2511.16719v2 | Bib is arXiv @misc; check for a peer-reviewed version |
| 52 | liu2026medsam3delvingsegmentmedical | – | SUPPORTED | Phrases "limited to no more than three words" (txt l. 116, 239). T+I Dice 0.7772–0.9058, T only 0.0826–0.5687 on BUSI, RIM-ONE, ISIC 2018, Kvasir-SEG (Table 2, p. 6) | Optional: only the detector is fine-tuned (encoders frozen, Sec. 3.2), and the box is derived from ground truth |
| 55 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | "maps free-form descriptions, from single words to full clinical sentences, to 3D masks" (Abstract, PDF p. 1) | Close paraphrase of the abstract wording ("free-form descriptions, from single words to … clinical sentences, to 3D masks"). Rephrase, or quote it with quotation marks |
| 56 | (no cite; `\cref` to background) | – | SUPPORTED | "Trained on 62K+ CT, MRI, and PET volumes" (Abstract), "1,087 unified concepts" (Sec. 4 / App. C), "fusion across all decoder stages" (Sec. 2, PDF txt l. 157) | Add the VoxTell cite, or rely on l. 55 (acceptable) |
| 57 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | Table 1 (p. 6), zero-shot on 11 held-out datasets: Mean Dice VoxTell 70.85, SAT 51.23 (notes §7; PDF Table 1). SAT is the second-best mean | Checked against arXiv v1 only. The bib now points to CVPR 2026; the CVF PDF was not accessible (HTTP 403). Check that Table 1 is unchanged in the CVPR version |
| 58 | desai2021skmtea | – | SUPPORTED | Dataset identification only. VoxTell ref. [50] = Desai et al., SKM-TEA (notes §9) | – |
| 58 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | Table 9 (Suppl., S-p. 10): VoxTell mean 10.72 on SKM-TEA. Caption: "a modality and body region very rarely seen during training". p. 8: "Future work could explore few-shot adaptation with minimal labeled examples" | "few-shot adaptation with minimal labelled examples" is the paper's wording verbatim, without quotation marks. Quote it or rephrase it. Check that the CVPR supplement still has Table 9 |
| 61 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | "including synonyms, rephrasings, and minor typographical [errors]" (Sec. 5, PDF txt l. 273). Fig. 3 (p. 7) | – |
| 62 | zhang2026seer | – | PARTLY | Five baselines compared: SAT, BiomedParseV2, Text3DSAM, MedSAM3, VoxTell (Table 1, p. 6). But **MedSAM3 is a 2D model** (frame-wise), so "five text-promptable 3D models" is wrong for one of them. The prompts were not rephrased: "each raw request q_i is **generated** under one of eight predefined clinical styles" (Sec. 2.1, txt l. 157). The test prompts are "free-text clinical prompts introduced in SEER-Trace" (Sec. 3.1, l. 349–350) | "five text-promptable models on 3D data", and "free-text requests that an LLM generated in eight clinical styles" |
| 63 | zhang2026seer | – | PARTLY | SAT on PENGWIN: label 96.05 → free-text **mean** 0.01 (Table 1): supported. "VoxTell was the most robust" is **not the paper's claim**. The paper calls VoxTell "the strongest baseline" (Sec. 3.2, txt l. 400). VoxTell's Std. is not the lowest: BrainMetShare Std. SAT 2.53, Text3DSAM 0.93 vs VoxTell 3.35 (these baselines collapsed to near-zero Dice). VoxTell has the highest free-text and worst-case Dice of the baselines | "VoxTell kept the highest free-text and worst-case DSC among the baselines". Say that SAT's 0.01 % is the mean free-text DSC |
| 64 | zhang2026seer | – | SUPPORTED | VoxTell PENGWIN: label 97.59, worst Dice 79.34 over clinically equivalent rephrasings (Table 1, p. 6) | The card was written from arXiv v3; the bib is MICCAI 2026 (Springer). Check the numbers in the published version |

## Uncited non-obvious claims

- l. 27 "In the models that adapt the Segment Anything Model (SAM) to medical images, this input is spatial." This overgeneralises, and l. 52 contradicts it: MedSAM-3 adapts SAM 3 with text. Restrict it to "MedSAM and SAM-Med2D", or to SAM/SAM 2-based adaptations.
- l. 35 "In other 2D work, text accompanies a single fixed target class …". It is supported for LViT/TextMatch, but the paragraph also contains R-Super (l. 37), which is **3D CT** and multi-tumour, so the topic sentence does not cover it.
- l. 40 "Most text-promptable models select their target from a fixed vocabulary." This is a field-level generalisation without a citation. Support it with the examples that follow, or with a survey, or soften it to "The following models …".
- l. 49 "Two widely used text-promptable models work on 2D images." "Widely used" has no evidence. Drop it, or cite usage.

## Problem list

1. SegVol (l. 31): the metric is the average of per-class median DSC, and the SAM-Med2D baseline used point prompts, not a box. The 5.85 % comes from the internal 20 % split and its unit is ambiguous.
2. SAT (l. 44): it was not trained on 22,186 scans; 80 % of each dataset was used for training.
3. SEER (l. 62–63): "five … 3D models" (MedSAM3 is 2D). The prompts were "generated", not "rephrased". "Most robust" overstates the paper ("strongest baseline"), and VoxTell's Std. is not the lowest.
4. LViT (l. 36): 83.66 % is with 100 % labels, in a paragraph about scarce labels.
5. SAT vs BiomedParse (l. 51): 29/30 is SAT-Pro vs the non-oracle BiomedParse; it is 23/30 vs the oracle.
6. Text3DSAM (l. 46): the paper does not describe the challenge as "text-guided 3D segmentation"; name the challenge or the track.
7. Close paraphrase / verbatim without quotation marks: l. 55 (VoxTell abstract) and l. 58 ("few-shot adaptation with minimal labelled examples").
8. Version mismatches between the source read and the bib entry:
   - VoxTell: arXiv v1 read, bib is CVPR 2026 (CVF PDF blocked, 403).
   - SEER: arXiv v3 read, bib is MICCAI 2026.
   - BiomedParse: arXiv v3 read, bib is Nature Methods.
   - CLIP-Driven Universal Model: arXiv v5 read, bib is ICCV.

   Numbers were not compared with the published versions.
9. Bibliography (report only):
   - `Zhao_2024` duplicates `zhao2025foundation-9de` (same DOI).
   - These are arXiv @misc entries; check for peer-reviewed versions: `cheng2023sammed2d`, `li2023lvitlanguagemeetsvision` (journal version probably exists), `zhao2025sat`, `bassi2025learningsegmentationradiologyreports`, `carion2026sam3segmentconcepts`, `liu2026medsam3delvingsegmentmedical`.
   - The SegVol card is out of date ("bib entry is arXiv @misc"); the bib is now NeurIPS.
   - The SEER card says "no bib entry yet"; `zhang2026seer` now exists.

## Counts

SUPPORTED 23 (incl. 4 with caveats), PARTLY SUPPORTED 4, NOT SUPPORTED 0, WRONG SOURCE 0, CANNOT VERIFY 0 (published versions of VoxTell, SEER, BiomedParse and the CLIP-Driven Universal Model not checked; see problem 8). Uncited claims: 4.

Key existence (re-checked at end, after parallel bib edits): all 16 cited keys are present exactly once in `thesis/literature.bib`.
