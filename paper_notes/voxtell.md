# VoxTell — paper notes

Notes on the paper that defines the base model of this thesis. Read once, so the PDF does not have to be re-read.
Every fact below has its location in the paper. Sections 1–9 are what the **paper** says; section 10 is **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Rokuss, Langenberg, Kirchhoff, Isensee, Hamm, Ulrich, Regnery, Bauer, Katsigiannopulos, Norajitra, Maier-Hein. *VoxTell: Free-Text Promptable Universal 3D Medical Image Segmentation.* arXiv:2511.11450v1 [cs.CV], 14 Nov 2025. 42 pages (8 main + references + 10-page supplement) |
| Local PDF | `voxtell_paper/voxtell.pdf` |
| Bib key | `rokuss2025voxtellfreetextpromptableuniversal` (`@misc`, arXiv) — check for a peer-reviewed version before submission |
| Affiliations | DKFZ Heidelberg (Division of Medical Image Computing), Heidelberg University, Helmholtz Imaging, Heidelberg University Hospital (p. 1) |
| Code | github.com/MIC-DKFZ/VoxTell (abstract, p. 1) |
| Checkpoint used in this thesis | `./models/voxtell_v1.1` (config `model.dir`), fold_0 `checkpoint_final.pth` (`code/src/model/builder.py:67`). The paper describes v1; differences to v1.1 are not documented in the paper |
| Notes written | 2026-10-19, from arXiv v1 |

Page numbers: main text p. 1–8; supplement restarts at p. 1 (written "S-p." below).

---

## 1. What VoxTell is (abstract, Sec. 1, p. 1–2)
- "a vision–language model for text-prompted volumetric medical image segmentation. It maps free-form descriptions, from single words to full clinical sentences, to 3D masks."
- Trained on 62K+ CT, MRI and PET volumes spanning 1K+ anatomical and pathological classes.
- Key idea: **multi-stage vision–language fusion** across decoder layers (text features modulate image features at every decoder resolution), instead of the single late fusion of MaskFormer-style models (SAT, BiomedParse).
- Claims: state-of-the-art zero-shot performance on unseen datasets; generalises to related unseen classes; cross-modality transfer; robust to linguistic variation (synonyms, rephrasing, typos); clinical-language and instance-specific segmentation.
- Contributions listed (p. 2): (1) the model, (2) multi-stage fusion, (3) SOTA text-promptable segmentation across CT/PET/MRI, (4) "towards open-set generalisation".

## 2. Related-work taxonomy used by the paper (Sec. 2, p. 2–3)
Three paradigms of text-guided medical segmentation:
1. **Closed-set via head mapping**: text selects a predefined head/class (CLIP-driven Universal Model, MultiTalent, CAT). Cannot segment arbitrary structures from text.
2. **Text as auxiliary guidance**: text as extra supervision for class-specific segmentation (QaTa-COV19, MosMed++ benchmarks; R-Super uses whole reports). Dataset-specific.
3. **Text-promptable segmentation**: masks from arbitrary text. 2D: BiomedParse (64 categories, nine modalities, Mask2Former-style late fusion), BoltzFormer/BiomedParseV2. 3D: SegVol (96K CT pretraining, 6K labelled, point/box/text, 200+ classes), Text3DSAM, SAT (22K scans, 497 classes, MaskFormer, late dot-product fusion).
- Paper's critique: most methods rely on fixed label sets, generalise poorly to free-form phrasing, and are not evaluated on unseen concepts/modalities (p. 3).

## 3. Architecture (Sec. 3, p. 3–4; S-p. 1, A.2)
Notation as in the paper: V ∈ R^{H×W×D} input volume; S scales.
- **Image encoder** f_enc: UNet-style, **ResEncL** (nnU-Net residual encoder L) with **six** stages, channels [32, 64, 128, 256, 320, 320] (S-p. 1). Produces Z = {z_1,…,z_S}, z_s ∈ R^{C_s×H_s×W_s×D_s} (Eq. 1).
- **Text encoder** f_text: frozen **Qwen3-Embedding-4B**; q = f_text(p) ∈ R^d (Eq. 2). Instruction prefix used for all prompts (S-p. 1): "Instruct: Given an anatomical term query, retrieve the precise anatomical entity and location it represents. Query: [text input]." Embeddings precomputed during training.
- **Prompt decoder** f_prompt: transformer, **six layers, eight heads, query dimension 2048**; q is the query, bottleneck features z_S are keys/values (Eq. 3). Output projected by stage-specific adapter MLPs (two-layer MLP, hidden 2048) to multi-scale text-guidance tensors T = {T_1,…,T_S}, T_s ∈ R^{G×C_s}, **G = 32** (guidance embedding dimension).
- **Decoder with cross-scale fusion** (Eqs. 4–6): z'_s = ConvBlock(concat(upsampled y_{s−1}, z_s)); y_s = concat(z'_s, T_s ⊙ z'_s) ∈ R^{(C_s+G)×H_s×W_s×D_s}, where ⊙ is a dot product along C_s giving G new channels. I.e. the MaskFormer dot product between text and image features is applied at **every** decoder scale.
- **Deep supervision** (Eq. 7): L = Σ_s λ_s L_seg(Ŷ_s, Y_s), L_seg = Dice + (binary) cross-entropy; λ_s = nnU-Net defaults [1, 1/2, 1/4, 1/8, 1/16] at all five decoder scales (S-p. 1, A.3).
- Rationale given: UNets remain SOTA in 3D medical segmentation vs transformers (p. 4); late fusion forces prompt-agnostic image features; location-specific prompts need repeated interaction (p. 4).
- Figure 2 (p. 3) is the architecture overview figure.

## 4. Training data and vocabulary (Sec. 4, p. 4–5; S-p. 1–8)
- **158 public datasets, >62,000 volumes (~4 TB), 1,087 concepts**, CT, multi-sequence MRI, PET; healthy and pathological; brain, thorax, abdomen, pelvis, musculoskeletal, vasculature (p. 4; S-p. 1). Full list: Tables 4–5 (S-p. 3–4). Vocabulary of all 1,078 anatomical labels: Table 10.
- Validation: **5% of each dataset** reserved for development and ablations (p. 5; S-p. 5).
- **Vocabulary construction** (Sec. 4, App. C): harmonise synonymous/overlapping labels across datasets; expand labels with an LLM (Claude Sonnet 4 with extended thinking) into variants and hierarchical aggregates (e.g. "left rib 1"–"left rib 12" → "left rib cage"); human expert review. Final: **1,087 unified concepts, 9,682 rewritten labels**. During training the default name is sampled with 25% probability, a rephrased variant with 75% (S-p. 1).
- **Instance-focused dataset** (App. B.3, Table 6): for ReXGroundingCT; semantic lesion datasets converted to instance prompts via TotalSegmentator anchors, TCIA DICOM-metadata prompts, ReXGroundingCT train split.
- **In-house radiotherapy cohort** (App. B.2): 203 SBRT lung-tumour patients, Heidelberg University Hospital, report-derived prompts translated from German with gpt-oss-120b; held out entirely.

### Knee / musculoskeletal content of the training data (relevant to SKM-TEA)
- **SKI10** (Table 4, S-p. 3): 100 MRI, 4 categories, "Cartilage, Bone".
- **Lower Extremity Muscles** [13] (Table 5, S-p. 4): 78 MRI, 126 categories, "Musculoskeletal Structures" (visible human female and male).
- Table 10 (vocabulary, extremities block): **femoral articular cartilage (100)**, left/right femur distal cartilage (78), **left/right patella cartilage (78)**, **tibial articular cartilage (100)**, **left/right tibia lateral cartilage (78)**, **left/right tibia medial cartilage (78)**, knee ligaments ACL/LCL/MCL/PCL (78), femur, patella, tibia bones. Numbers in brackets = number of training images with that label.
- **No meniscus label appears in Table 10's knee block.**
- The text says the knee region "is sparsely represented in the training set and features only a few segmentation targets" (p. 8) and "includes cartilage and meniscus structures absent from training data" (S-p. 9). **This conflicts with Table 10**, which lists femoral, patellar and medial/lateral tibial cartilage. Cite Table 10 for what was in training; quote the text only with care.

### Lung content (relevant to the control task)
- Table 10 (chest): lung (3427), left lung (4404), right lung (4404), plus lobes (3454 each).

## 5. Training configuration (Sec. 4 Implementation details p. 5; S-p. 1, A.1/A.3)
- Framework: **nnU-Net** ("We leverage the nnU-Net [77] framework", S-p. 1).
- Final model: **64 NVIDIA A100 (40 GB)**, batch size **128** (2 per GPU), ~**six days** (p. 5). Ablations: one A100, batch 2.
- **2,000 epochs × 250 iterations**, **SGD**, initial LR **1 × 10⁻⁴**, polynomial decay (S-p. 1).
- Patches **192³ voxels** (S-p. 1).
- Standard nnU-Net augmentation **except left–right mirroring** (laterality-sensitive structures) (S-p. 1).
- Three prompts per image (max for an A100 40 GB at batch 2): **two positive, one negative** (absent structure → teaches empty masks) (S-p. 1).
- **Foreground oversampling 85%** (S-p. 1).
- **Not stated anywhere in the paper**: target voxel spacing / resampling, intensity normalisation scheme, orientation handling. (Only implied through "nnU-Net framework".) Check the official code if needed.

## 6. Evaluation protocol and metrics (Sec. 5, p. 5)
- Evaluates **only on unseen datasets** (out-of-distribution images), not on held-out splits of training datasets (contrast to SAT's in-distribution protocol) (p. 5).
- Four axes: standard anatomical/pathological segmentation; robustness to prompts; generalisation to unseen concepts and modalities; clinical language / instance-level (p. 5).
- Metric: **Dice**; ReXGroundingCT additionally **HIT5%** = fraction of samples with Dice ≥ 5% (p. 5).
- Same standard terms as prompts for all methods, no prompt optimisation (p. 6).
- Baselines: TotalSegmentator, BiomedParse, Text3DSAM, SegVol, BiomedParseV2, SAT.

## 7. Results (numbers are Dice in %)
**Table 1 (p. 6), zero-shot, unseen datasets** — VoxTell / next best:
| Dataset (concept) | Modality | VoxTell | SAT |
|---|---|---|---|
| Pediatric-CT-SEG [84] (abdominal organs) | CT | 72.94 | 68.79 |
| **AeroPath [186] (lung & airway)** | CT | **89.65** | 87.98 (SegVol 88.67) |
| VEELA2025 [189] (liver & vessels) | CT | 60.56 | 37.65 |
| RADCURE [210] (head & neck) | CT | 51.28 | 54.33 |
| HVSMR-2.0 [154] (heart) | MRI | 52.72 | 43.38 |
| ACRIN NSCLC [94] (lung tumour) | PET | 83.24 | 77.13 |
| ISBI MS [37] (MS lesions) | MRI | 72.71 | 13.68 |
| Adrenal-ACC-Ki67 [148] | CT | 77.23 | 0.09 |
| HCC-TACE-SEG [147] (liver lesions) | CT | 73.24 | 62.28 |
| Pengwin [129] (bones w. fractures) | CT | 97.59 | 96.05 |
| BrainMetShare [66] | MRI | 48.19 | 22.16 |
| **Mean** | | **70.85** | 51.23 |

**Table 7 (S-p. 7), per prompt — AeroPath [186], 27 CT, category "Healthy (Known Concept)"**: VoxTell **lung 96.99**, trachea 82.31 (TotalSegmentator 96.44 / 74.02; SAT 96.93 / 79.02; SegVol 97.28 / 80.06). Table 7 caption: "Overview of held-out test datasets."

**Table 2 (p. 6), fusion ablation (validation set)**: Mask2Former 51.68; MaskFormer (SAT) 55.11; VoxTell 3 stages 60.16; 5 stages 61.54; + deep supervision 62.55; + scaling batch 2→128 69.43.

**Table 3 (p. 7), cross-modality / unknown concept**: breast cancer PET 72.27; pancreas tumour MRI 35.66; sarcoma MRI 40.34; bladder cancer MRI 25.76; esophageal tumour CT 69.07.

**Figure 3 (p. 7)**: prompt stability across synonyms/misspellings — VoxTell stable, baselines variable.

**Fig. 4 (p. 7)**: ReXGroundingCT (validation, both fine-tuned): VoxTell 28.2 Dice / 67.8 HIT5%, SAT 13.1 / 49.8.

**Radiotherapy cohort (p. 8)**: VoxTell 50.2 Dice; SAT 0.0, BiomedParseV2 1.2, SegVol 8.1.

**Table 8 (S-p. 9), text encoder ablation**: Qwen3-Embedding-4B 62.55 (chosen: medium size, ≈ best large models; large 7–8B models need >24 GB GPU memory). Others: EmbeddingGemma 56.77, SAT encoder 60.43, Qwen3-0.6B 62.24, E5-Mistral-7B 62.88, Linq-Embed-Mistral 62.78, Qwen3-8B 62.45.

**Table 9 (S-p. 10), SKM-TEA [50] zero-shot (knee MRI), Dice %:**
| Structure | BiomedParse | Text3DSAM | SegVol | BiomedParseV2 | SAT | **VoxTell** |
|---|---|---|---|---|---|---|
| Patellar cartilage | 0.44 | 0.0 | 0.0 | 0.0 | 0.01 | **0.07** |
| Femoral cartilage | 0.54 | 0.08 | 0.0 | 0.15 | 1.34 | **46.45** |
| Lateral tibial cartilage | 0.22 | 0.09 | 0.0 | 0.0 | 0.02 | **2.97** |
| Medial meniscus | 0.47 | 0.97 | 0.0 | 0.0 | 0.0 | **0.04** |
| Lateral meniscus | 0.72 | 0.1 | 0.0 | 0.0 | 0.0 | **0.0** |
| Medial tibial cartilage | 0.29 | 0.31 | 0.0 | 0.0 | 0.0 | **14.78** |
| Mean | 0.45 | 0.26 | 0.0 | 0.02 | 0.23 | **10.72** |

Caption: "Limitations of zero-shot segmentation on rare body regions … knee MRI (SKM-TEA dataset [50]), a modality and body region very rarely seen during training. Most prompts correspond to fully out-of-distribution (OOD) anatomical structures…". The paper does not state which SKM-TEA split, echo or preprocessing it used.

## 8. Limitations and future work stated by the authors
- p. 8: "performance on fully out-of-distribution (OOD) cases remains challenging. For example, results on the Stanford Knee dataset [50] (Appendix Tab. 9) … show that the model struggles with these concepts. In particular, the knee region is sparsely represented in the training set and features only a few segmentation targets, highlighting that the model's text-guidance cannot extrapolate to entirely unfamiliar spatial or visual patterns."
- p. 8: "**Future work could explore few-shot adaptation with minimal labeled examples**, and leveraging text supervision from radiology report-image pairs."
- S-p. 9: "These findings suggest a promising path for combining vision–language pretraining with **lightweight few-shot or report-level fine-tuning** to close remaining gaps."
- Conclusion (p. 8): "challenges remain in generalizing to entirely out-of-distribution anatomical regions."

## 9. Paper's references that this thesis also uses
- [50] Desai et al., SKM-TEA → bib `desai2021skmtea`.
- [186] Støverud et al., AeroPath (arXiv 2023 in the paper) → bib `støverud2023aeropathairwaysegmentationbenchmark`.
- [77] Isensee et al., nnU-Net, Nature Methods 18(2):203–211 (2021); [78] Isensee et al., "nnU-Net revisited" (ResEnc), 2024.
- [231] Zhang et al., Qwen3 Embedding, arXiv:2506.05176 (2025).
- [238] SAT, [53] SegVol, [236] BiomedParse, [237] BiomedParseV2, [216] Text3DSAM, [126] CLIP-driven Universal Model, [41] MaskFormer, [42] Mask2Former.

---

## 10. Analysis for this thesis (NOT from the paper; verify before using)
1. **Motivation is directly supported.** The authors name both the gap (knee = OOD, Table 9 mean 10.72 Dice) and the remedy this thesis studies ("few-shot adaptation with minimal labeled examples", p. 8; "lightweight few-shot … fine-tuning", S-p. 9). Cite p. 8 and Table 9.
2. **Knee cartilage is not entirely unseen.** Table 10 lists femoral, patellar and medial/lateral tibial cartilage from SKI10 (100 MRI) and Lower Extremity Muscles (78 MRI); menisci are absent. This fits this thesis's pretrained column: femoral cartilage 0.684, all others 0.000 (`thesis/tables/cl_metrics.csv`, eval matrices). The thesis should say "rarely seen" (Table 9 caption) rather than "never seen", and note the meniscus vs cartilage difference.
3. **Pretrained numbers differ from Table 9.** Paper: femoral 46.45, medial tibial 14.78, lateral tibial 2.97, others ≈0. This thesis: femoral 68.4, all others 0.0. Possible reasons (unverified): different test volumes (own random split, 24 scans), checkpoint v1.1 vs paper, preprocessing (identity affine, no resampling here; paper's preprocessing unknown), echo choice. Do not claim a reason without evidence.
4. **AeroPath** is a held-out test set of the paper, category "Healthy (Known Concept)"; VoxTell lung Dice 96.99 on all 27 volumes. This thesis's pretrained lung Dice on its 4 test volumes: 0.979 (consistent). Lung is heavily represented in training (Table 10: lung 3427, left/right lung 4404). Supports "known concept, unseen dataset" wording for the control task.
5. **Fine-tuning settings vs pretraining.** This thesis fine-tunes with SGD, LR 1e-4, poly decay, 192³ patches, 85% foreground — the same as VoxTell's pretraining (S-p. 1). Differences: deep supervision off (`model.deep_supervision: false` in configs) vs on in pretraining; one prompt per sample, no negative prompts (verify in code); 10 epochs. Each difference needs a reason in Method.
6. **Text encoder frozen** in VoxTell and in every strategy here. LoRA configs set `target_modules: [multihead_attn]`, `attn_parts: [q, v]`; which VoxTell module(s) this matches (prompt decoder only?) must be checked in `code/` before writing Method. The CPE-CLIP-based strategy adds learned prompt tokens to the decoder (`thesis_notes.md`).
