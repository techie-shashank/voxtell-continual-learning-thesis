# BiomedParse — fact card (tier B)
| | |
|---|---|
| Paper | T. Zhao, Y. Gu, J. Yang et al., "BiomedParse: a biomedical foundation model for image parsing of everything everywhere all at once", arXiv:2405.12971v3 (4 Jun 2024); 26 pages (main text pp. 1–11, then references, figures, supplement) |
| Bib key / Local PDF | zhao2025foundation-9de / papers/t1_text_promptable/zhao2025foundation-9de.pdf |
| Version read | arXiv v3 preprint. The bib entry cites the Nature Methods version (vol. 22, pp. 166–176, 2025) under a different title ("A foundation model for joint segmentation, detection and recognition of biomedical objects across nine modalities"). Same work, but the local PDF is not the published version; numbers below are from the preprint and may differ from the journal text |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: joint segmentation, detection and recognition ("image parsing") of biomedical objects from a text prompt, without bounding boxes (Abstract; Introduction, p. 2).
- Data (p. 3, Methods p. 8): BiomedParseData, built from 45 public segmentation datasets, 9 imaging modalities, 25 anatomic sites, about 1.1 million images, 3.4 million image–mask–label triples and 6.8 million image–mask–description triples; ontology of 3 categories, 15 meta-object types, 82 object types (labels harmonised and synonyms generated with GPT-4). 3D CT/MRI volumes are cut into in-plane 2D slices; 80/20 train/test split per dataset, slices of one volume kept in one split. Test set: 102,855 image–mask–label triples (Abstract; p. 4).
- Method (two sentences): SEEM-based modular model with an image encoder (Focal init.), a text encoder (PubMedBERT init.), a mask decoder and a meta-object classifier; the text prompt names the object type and the decoder outputs a per-pixel probability mask (p. 3; Methods p. 8–9; Fig. 1c). Invalid prompts are rejected with a Kolmogorov–Smirnov test on predicted pixel probabilities against per-type Beta distributions (Methods p. 9).
- Setting: text prompts built from a templated form "[OBJECT TYPE] in [ANATOMIC SITE] [MODALITY]" with GPT-4 paraphrases, i.e. a fixed set of 82 object types with varied wording (Methods p. 8); 2D only; no continual learning; no few-shot.
- Evaluation: Dice (median per task) vs SAM and MedSAM with oracle bounding boxes or Grounding-DINO boxes; nnU-Net/DeepLabV3+ numbers taken from the MedSAM study; MedSAM 50-task benchmark; precision/recall/F1 for recognition (p. 4–5; Methods p. 9).
- Best result: best Dice on the 102,855-triple test set, above MedSAM with oracle boxes (paired t-test p < 10^-4) (p. 4, Fig. 2a); on irregular-shaped objects 0.857 Dice, 39.6 % higher than the best competing method (p. 3); single prompt on 42 colon pathology images: median Dice 0.942 vs ≤ 0.75 for SAM/MedSAM without tight boxes (p. 4); object recognition average Dice 0.94 (p. 5); invalid-prompt detection AUROC 0.99 vs 0.61 Grounding DINO (p. 4).
- Limitations stated by the authors (Discussion, p. 7): no instance separation without post-processing; no conversational interaction; CT and MRI are reduced to 2D slices, so spatial information of the volumes is not used; 3D extension left to future work. Also: test split may overlap with training data of the compared models (Methods p. 9).

## Check of the author's notes
- related_work.tex:34 "BiomedParse adopts a modular architecture based on SEEM, comprising an image encoder, text encoder, mask decoder, and meta-object classifier, and performs segmentation, detection, and recognition jointly across nine biomedical imaging modalities by processing 3D volumes as in-plane 2D slices" → correct (p. 3; Methods p. 8).
- related_work.tex:34 "Although it achieved strong performance on 2D evaluation benchmarks, its slice-wise formulation does not explicitly model 3D spatial continuity" → correct (Discussion p. 7 states the 2D reduction as a limitation).
- related_work.tex:34 "limiting its performance on complete volumetric scans" → not supported by this paper: it reports no volumetric (3D) evaluation, only the stated limitation. A possible source: SAT (zhao2025sat, Sec. 2.3, p. 8) evaluates BiomedParse slice by slice on 11 3D datasets and attributes its false positives to the 2D slice-wise design.
- related_work.tex:160 (table) "Nine imaging modalities | Concept prompts; SEEM-based, 2D slices | Above MedSAM with oracle boxes" → correct (p. 4). Data column could give 3.4 M triples / 45 datasets / 82 object types.
- introduction.tex:3 cites `Zhao_2024` (not this key) for "text-promptable universal models designed to support segmentation across multiple structures, modalities, and tasks" → correct for this paper. Note: `Zhao_2024` and `zhao2025foundation-9de` in literature.bib are duplicate entries of the same Nature Methods article (same DOI 10.1038/s41592-024-02499-w).

## Relevance (NOT from the paper)
Large-scale text-promptable model across modalities, but 2D and with a closed 82-type ontology; useful to contrast slice-based text prompting with volumetric free-text models such as SAT and VoxTell.
