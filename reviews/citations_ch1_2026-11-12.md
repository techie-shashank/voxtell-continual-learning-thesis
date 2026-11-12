# Citation check: `thesis/introduction.tex` (Ch. 1), 2026-11-12

Scope: every `\cite` in `thesis/introduction.tex` (44 key occurrences on 31 lines; the commented-out notes at the end of the file are not checked). This supersedes the October checks of Ch. 1 in `reviews/`.

Sources used (step 2 order):
- **VoxTell**: `paper_notes/voxtell.md`, verified against `voxtell_paper/voxtell.pdf` (arXiv v1) **and** the CVPR 2026 version that the bib entry now points to: main paper `openaccess.thecvf.com/content/CVPR2026/papers/Rokuss_VoxTell_Free-Text_Promptable_Universal_3D_Medical_Image_Segmentation_CVPR_2026_paper.pdf` (proceedings pp. 37538–37557) and the CVPR supplement `.../supplemental/Rokuss_VoxTell_Free-Text_Promptable_CVPR_2026_supplemental.pdf`. The quoted passages are the same in both versions.
- **SKM-TEA**: `datasets/skm_tea_paper.pdf` (arXiv 2203.06823v1; the bib cites the NeurIPS 2021 D&B version on OpenReview, which has the same sections).
- **AeroPath**: `datasets/aeropath_paper.pdf` (arXiv v1).
- **De Lange**: `paper_notes/delange2022.md` + `voxtell_paper/delange.pdf` (author version). **ZSCL**: `paper_notes/zscl.md`. **LoRA**: `paper_notes/lora_hu.md` + `voxtell_paper/lora_hu.pdf`. **CPE-CLIP**: `paper_notes/cpe_clip.md`. **CoCoOp**: `paper_notes/cocoop.md`. **Chaudhry**: `paper_notes/chaudhry2018.md`. **Liu survey**: `paper_notes/liu2026_vlm_cl_survey.md` + `papers/text/liu2026continuallearningvlmssurvey.txt`. **SPU**: `paper_notes/spu.md`.
- **SAT**: `paper_notes/cards/zhao2025sat.md` + `papers/text/zhao2025sat.txt` (arXiv v5; bib is npj Digit. Med. 2025). **nnU-Net**: `papers/other/isensee2018nnunetselfadaptingframeworkunetbased.pdf` (arXiv 1904.08128v2 = preprint of the Nature Methods paper in the bib). **MedSAM / SAM-Med2D**: `papers/text/Ma_2024.txt`, `papers/text/cheng2023sammed2d.txt`.
- **Ch. 2 works**: `paper_notes/cards/ji2023continualsegmentsingleunified.md`, `cards/guo2025continuallearningdrivenmodelaccurate.md`, `zhang2023continuallearningabdominalmultiorgan.md`, `NEW_ye2025medseqft.md`, `NEW_medcrpcl2026.md`, `NEW_paewc2025.md`, `NEW_medpeftcl2025.md`, `chen2026fewshotcontinuallearning3d.md`, `NEW_wang2026casam.md`, `NEW_wang2024sammed3dmoe.md`.

Bib/source identity (step 3): every entry matches the paper read (title, authors, year), with these version differences, none of which changes a verdict: VoxTell bib = CVPR 2026 (notes/PDF = arXiv v1; checked both); SAT bib = npj Digit. Med. 2025 (read arXiv v5); nnU-Net bib = Nature Methods 2021 (read arXiv v2 of the same work, title differs: "Automated Design of Deep Learning Methods for Biomedical Image Segmentation"); CA-SAM bib = CVPR Findings 2026 (notes from arXiv v1, 2025).

## Focus items

**(1) `\cite[Sec.~6]{rokuss…}` on l. 41 and l. 42.** Correct for both. In arXiv v1 and in the CVPR 2026 paper, p. 8 (CVPR proceedings p. 37545) holds the last part of **Sec. 6 "Results and Discussion"**: the run-in paragraph "Limitations." starts at the bottom of the left column and continues at the top of the right column, directly followed by the heading "7. Conclusion". Both the knee attribution and the few-shot future-work sentence are inside this "Limitations." paragraph, i.e. in Sec. 6, not in Sec. 7. Optional precision: `[Sec.~6, Limitations]` or `[p.~8]`. Supplement Sec. E ("Zero-shot segmentation on rare body regions") repeats both points and could be added. Defence note: the authors' "structures entirely absent from training" conflicts with their own Suppl. Table 10 (femoral, patellar and tibial cartilage labels from SKI10 and Lower Extremity Muscles; no meniscus). The thesis reports this as the authors' attribution, so the citation is correct, but an examiner may ask about it (`paper_notes/voxtell.md` §4).

**(2) l. 21 "Masks of the same structure also differ between readers" → `desai2021skmtea`.** Supported. SKM-TEA Sec. 1, p. 1: dense annotations "are cumbersome to curate and are prone to inter-reader variations". The statement is a general remark in the introduction about MRI annotations, with no measurement and no reference in SKM-TEA. It does not quantify reader variability for the SKM-TEA labels. Acceptable as cited; if an examiner wants evidence, a primary source on inter-reader variability would be stronger.

**(3) SKM-TEA paragraph (l. 45–48).** l. 45 is supported (Sec. 2 and Fig. 2). l. 46–48 have **no citation**, although all three restate SKM-TEA content (listed under uncited claims below):
- T2 (l. 46): SKM-TEA Sec. 2, p. 3: "T2 relaxation time … which is sensitive to collageneous tissue degeneration [46]". The content matches ("reflects" vs "sensitive to"), but SKM-TEA itself cites [46] for this, so it is a secondary source.
- l. 47 "These values can only be read out once the structures are outlined": Fig. 2 caption says "Tissue segmentations of articular cartilage and the meniscus are used to create tissue-wise T2 maps". The source does not say "only".
- l. 48 "The SKM-TEA authors name manual outlining as one obstacle to the use of quantitative MRI": SKM-TEA Sec. 2, p. 3: qMRI "implementation is hampered due to extremely long scan times and the need to manually localize regions-of-interest (ROIs) in the image [40, 29, 41]". The content matches, but the sentence attributes the point to the SKM-TEA authors by name and has no `\cite`. SKM-TEA in turn cites [40, 29, 41].

**(4) l. 103–105.** All seven keys are supported. Gao ×3 (MedCRP-CL, PA-EWC, MedPEFT-CL): 2D CLIPSeg, full training splits. Chen et al.: 3D FOMO backbone, no text prompt. None of the four measures loss of pretrained ability, according to each notes file. SPU measures it for CLIP (control-set drop, Eq. 6). CA-SAM measures zero-shot IoU on five unseen datasets after the sequence (box prompts at test). SAM-Med3D-MoE measures "Ori tasks" and "Other classes" against the baseline (6-point and box prompts). One caveat: SAM-Med3D-MoE is not a sequential continual-learning setup (experts are fine-tuned separately and then merged). The sentence does not claim it is, so it holds.

## Table

| line | key | locator | verdict | evidence (quote + location) | fix needed |
|---|---|---|---|---|---|
| 21 | desai2021skmtea | – | SUPPORTED | "cumbersome to curate and are prone to inter-reader variations" (Sec. 1, p. 1) | optional `[Sec.~1]`; general remark without data (see focus 2) |
| 24 | isensee2018nnunetselfadaptingframeworkunetbased | – | SUPPORTED | "nnU-Net automatically adapts to any new dataset" (arXiv v2, Sec. 2); per-dataset pipelines throughout | none (key name says 2018, entry is Nature Methods 2021; cosmetic) |
| 26 | zhao2025sat | – | SUPPORTED | "comparable performance to 72 nnU-Nets--the strongest specialist models trained on each dataset" (Abstract; Sec. 2.1) | none |
| 27 | zhao2025sat | – | SUPPORTED | SAT takes "3D volumes as visual inputs along with text prompts" (Sec. 1) | none |
| 27 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | free-form descriptions mapped to 3D masks; text prompt input (Abstract; Sec. 3) | none |
| 28 | Ma_2024 | – | SUPPORTED | MedSAM: "users can use bounding boxes to specify the segmentation targets"; SAM "requires points or bounding boxes" | none |
| 28 | cheng2023sammed2d | – | SUPPORTED | "prompts such as points and bounding boxes"; SAM-Med2D supports "boxes, points, and masks" (Abstract) | none (bib is arXiv @misc) |
| 32 | zhao2025sat | – | SUPPORTED | Term-level prompts from a fixed 497-class vocabulary; free text is mapped to terms by GPT-4 (Sec. 2.6, Fig. 9; card) | none |
| 32 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | "free-form descriptions, from single words to full clinical sentences, to 3D masks" (Abstract, p. 1) | none |
| 35 | zhao2025sat | – | SUPPORTED | Text embedding refined by the query decoder and "dotted with per-voxel decoder features" (Sec. 4.5, Eq. 6–9; card) | none (claim spans l. 34–35) |
| 35 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | Text-guidance tensors fused by a dot product at every decoder scale; one prompt-conditioned output (Sec. 3, Eqs. 3–6) | none |
| 38 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | "Trained on 62K+ CT, MRI, and PET volumes" (Abstract, p. 1; Sec. 4) | none |
| 40 | desai2021skmtea | – | SUPPORTED | Dataset reference; VoxTell Table 9 evaluates "knee MRI (SKM-TEA dataset [50])" | none |
| 40 | rokuss2025voxtellfreetextpromptableuniversal | Suppl. Table 9 | SUPPORTED | VoxTell "Mean Dice … 10.72" over patellar, femoral, lateral/medial tibial cartilage and medial/lateral meniscus (Suppl. Table 9, arXiv S-p. 10 and CVPR supplement) | none. Note: Table 9 is only in the separate CVPR supplement, not in pp. 37538–37557 |
| 41 | rokuss2025voxtellfreetextpromptableuniversal | Sec. 6 | SUPPORTED | "the knee region is sparsely represented in the training set and features only a few segmentation targets"; "anatomical structures entirely absent from training" (Sec. 6, "Limitations." paragraph, p. 8 / CVPR p. 37545) | locator correct; optional `[Sec.~6, Limitations]`. Defence: conflicts with the paper's own Suppl. Table 10 (focus 1) |
| 42 | rokuss2025voxtellfreetextpromptableuniversal | Sec. 6 | SUPPORTED | "Future work could explore few-shot adaptation with minimal labeled examples" (Sec. 6, "Limitations." paragraph, p. 8 / CVPR p. 37545) | locator correct; same in Suppl. Sec. E ("lightweight few-shot or report-level fine-tuning") |
| 45 | desai2021skmtea | – | SUPPORTED | qDESS "can extract quantitative biomarkers for osteoarthritis" (Sec. 2, p. 3); "Tissue segmentations of articular cartilage and the meniscus are used to create tissue-wise T2 maps" (Fig. 2) | optional `[Sec.~2, Fig.~2]` |
| 54 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | "trained on 64 A100 GPUs with a batch size of 128, requiring roughly six days" (Sec. 5, p. 5; Suppl. A.1) | optional `[Sec.~5]` |
| 63 | delange2022 | Sec. 2 | PARTLY SUPPORTED | Sec. 2 defines the **task incremental setting**: "many methods relax the general setting to an easier task incremental one. The task incremental setting considers a sequence of tasks … given limited or no access to data … from previous tasks". Sec. 1 defines continual learning more generally as "learning from an infinite stream of data" | The sentence gives Sec. 2's definition of the task-incremental setting as the definition of continual learning in general. Either say "task-incremental continual learning" / "the task-incremental setting of continual learning", or cite it as the setting this thesis follows |
| 69 | delange2022 | Sec. 1 | SUPPORTED | "performance on a previously learned task or domain should not significantly degrade over time as new tasks or domains are added"; "catastrophic forgetting" (Sec. 1, p. 1) | none |
| 70 | zheng2023preventingzeroshottransferdegradation | – | SUPPORTED | Continual training of CLIP degrades its zero-shot transfer ability on tasks not yet trained (Abstract; Sec. 1, p. 1–2, Fig. 1) | none. ZSCL shows this for CLIP; "pretrained vision–language models" generalises from one model family, acceptable with "can" |
| 73 | delange2022 | Sec. 1 | SUPPORTED | "the stability-plasticity dilemma [20], with plasticity referring to the ability of integrating new knowledge, and stability retaining previous knowledge while encoding it" (Sec. 1, p. 1) | Close paraphrase of the definition (same word pairs "retain(ing) previous knowledge" / "integrat(ion/ing) new knowledge"). It is attributed by name, but consider quotation marks or rewording to meet the declaration. The term itself comes from De Lange's [20], so "De Lange et al. call" is fine, but they did not coin it |
| 98 | ji2023continualsegmentsingleunified | – | SUPPORTED | Encoder frozen, "one new decoder per later dataset is added" (Sec. 3.1–3.2; card) | none |
| 98 | guo2025continuallearningdrivenmodelaccurate | – | SUPPORTED | "one lightweight decoder per anatomy or group of anatomies is added" (Sec. 4, p. 22–23; card) | none |
| 98 | zhang2023continuallearningabdominalmultiorgan | – | SUPPORTED | "lightweight class-specific … heads"; new heads added per new class (Sec. 2.2, p. 4–6; notes) | none |
| 98 | ye2025medseqft | – | SUPPORTED | "Each task gets a randomly initialised segmentation head" (Sec. III-D, p. 4; notes) | none. MedSeqFT calls itself "sequential fine-tuning", not a continual-learning method, but it targets forgetting; acceptable |
| 103 | gao2026medcrpcl | – | SUPPORTED | Backbone CLIPSeg, "All 2D images"; "Not few-shot. All training images of each task are used" (Sec. 3–4.1, Table 1; notes) | none |
| 103 | gao2025paewc | – | SUPPORTED | "Not few-shot: full training splits"; "2D only" (Sec. 4.1–4.2, p. 8; notes) | none |
| 103 | gao2026medpeftcl | – | SUPPORTED | "Not few-shot: full training splits (Table 1)"; "2D only (352×352)" (p. 5; notes) | none |
| 103 | chen2026fewshotcontinuallearning3d | – | SUPPORTED | Frozen 3D FOMO backbone, BraTS 3D MRI, no language interface (Sec. 2–3; notes) | none |
| 105 | Zhang_2024_CVPR | – | SUPPORTED | Control set = ImageNet zero-shot accuracy, "C. Drop" vs the frozen model (Sec. 1; Sec. 5.1, Eq. 6) | none |
| 105 | wang2025casam | – | SUPPORTED | Frozen 2D SAM, box prompts at test; zero-shot IoU on five unseen datasets after all nine tasks (Sec. 4.1.2, 4.4; Table 2; notes) | none |
| 105 | wang2024sammed3dmoe | – | SUPPORTED | Prompts "6 points or a bounding box"; performance on "Ori tasks" and "Other classes" vs baseline SAM-Med3D (Table 1, p. 7; notes) | none. Not a sequential CL setup; the sentence does not claim it is |
| 134 | rokuss2025voxtellfreetextpromptableuniversal | – | SUPPORTED | Model reference | none |
| 134 | desai2021skmtea | – | SUPPORTED | Manual segmentations of "(1) patellar cartilage, (2) femoral cartilage, (3, 4) lateral and medial tibial cartilage, and (5, 6) lateral and medial meniscus" (Sec. 4.1) | none (also supports l. 135) |
| 137 | støverud2023aeropathairwaysegmentationbenchmark | – | SUPPORTED | "27 CT images … with corresponding trachea and bronchi annotations" (Abstract) | none as a dataset reference. The paper documents only airway labels, not the lung labels used (Ch. 4 l. 81 says so). Bib is arXiv @misc: check for a peer-reviewed version before submission |
| 143 | hu2022lora | – | PARTLY SUPPORTED | "W₀ is frozen … A and B contain trainable parameters"; low-rank update ΔW = BA (Sec. 4.1, Eq. 3). Hu et al. use "adapter" for a **different** method (Houlsby adapter layers, Sec. 3, 5.1), not for the LoRA update | Mechanism supported. The term "called the adapter" is the thesis's convention and is not Hu's; make it explicit ("which we call the adapter") |
| 147 | D_Alessandro_2023 | – | SUPPORTED | Frozen CLIP plus "learnable prompts in both the language and the vision encoder" (Abstract; Sec. 4) | none. The meta-net is correctly marked as an addition in l. 148 |
| 148 | zhou2022cocoop | – | SUPPORTED | Meta-Net "generates for each input image a conditional token π" added to the context vectors (Sec. 3.3, p. 16818) | none ("inspired by" fits the differences listed in notes §3) |
| 149 | zheng2023preventingzeroshottransferdegradation | – | SUPPORTED | Distillation from the initial (pretrained) model in feature space (Sec. 3.2; Table 1d) | none |
| 150 | liu2026continuallearningvlmssurvey | Sec. 4 | SUPPORTED | "Existing methods are grouped into three main paradigms: (a) Multi-Modal Replay … (b) Cross-Modal Regularization … (c) Parameter-Efficient Adaptation" (Fig. 1 caption; Sec. 4) | Minor: the survey's names are "multi-modal replay" and "cross-modal regularisation" (also CLAUDE.md terminology). The mapping of strategies to families is the thesis's own (notes §4) |
| 161 | Chaudhry_2018 | – | SUPPORTED | Forgetting = "max_{l} a_{l,j} − a_{k,j}", averaged over earlier tasks; IoU-type measures allowed (Sec. 3, Eq. 3, p. 5) | optional `[Sec.~3, Eq.~3]` |
| 165 | zheng2023preventingzeroshottransferdegradation | – | SUPPORTED | Last = average after the last task; Transfer = average over the upper-right triangle (tasks not yet trained) (Sec. 4, Fig. 4b) | optional `[Sec.~4, Fig.~4b]` as in Ch. 3 |
| 191 | delange2022 | Sec. 3.1 | SUPPORTED | Replay: store samples or generate pseudo-samples, "replayed while learning a new task" (Sec. 3.1) | none |

## Uncited non-obvious claims in the range

- **l. 39**: "On datasets it was not trained on, VoxTell reached a mean DSC of 70.85 %". No citation; the next sentence's cite does not cover it. Source: VoxTell Table 1 (Sec. 6, p. 6), mean 70.85 over 11 unseen datasets. Hint: `\cite[Table~1]{rokuss…}`. **Must fix.**
- **l. 46**: T2 relaxation time "reflects the degeneration of collagen-rich tissue". Uncited. SKM-TEA Sec. 2 says "sensitive to collageneous tissue degeneration [46]". Hint: cite `desai2021skmtea` [Sec.~2], or SKM-TEA's [46] as the primary source.
- **l. 47**: "These values can only be read out once the structures are outlined". Uncited, and stronger than the source. SKM-TEA Fig. 2 says segmentations "are used to create tissue-wise T2 maps". Hint: cite Fig. 2 and drop "only" or limit it to tissue-wise values.
- **l. 48**: "The SKM-TEA authors name manual outlining as one obstacle to the use of quantitative MRI". The sentence attributes the point by name but has no `\cite`. Source: Sec. 2, p. 3 ("the need to manually localize regions-of-interest (ROIs)", citing [40, 29, 41]). Hint: add `\cite[Sec.~2]{desai2021skmtea}`.
- **l. 52**: "Retraining VoxTell from scratch … together with each new structure would be expected to preserve most of what it could segment before". Hedged reasoning without a source. De Lange Sec. 5 calls joint training "a soft upper bound", which would support it. Hint: cite that or keep it as the thesis's expectation.
- **l. 101**: "The methods for pretrained vision–language models reviewed in Sec. cl-vlm were developed and evaluated on classification or on tasks with text output". This rests on Ch. 2. It is true only if PA-EWC, MedPEFT-CL and MedCRP-CL are not counted among those methods: they evaluate VLM-CL methods (ZSCL, MoE-Adapters, LoRA) on 2D CLIPSeg segmentation (`NEW_paewc2025.md` §9). Check against the content of `sec:cl-vlm`.
- l. 18–19 (drawing masks is laborious, slice by slice) and l. 104 (none of the closest works measures pretrained ability) are uncited but acceptable. SKM-TEA Sec. 1 ("cumbersome to curate") could back l. 19. l. 104 follows from the four works cited in l. 103 (each notes file: "Loss of pretrained ability: not measured").

## Side notes (bib / notes, report only)
- `paper_notes/voxtell.md` header still says the bib entry is `@misc` (arXiv). It is now `@inproceedings` CVPR 2026, pp. 37538–37557. Locators in the notes (p. 8, Table 9) remain valid. Table 9 lives in the separate CVPR supplement.
- arXiv-only entries cited in Ch. 1: `cheng2023sammed2d`, `guo2025continuallearningdrivenmodelaccurate`, `ye2025medseqft`, `chen2026fewshotcontinuallearning3d`, `støverud2023aeropathairwaysegmentationbenchmark`, `liu2026continuallearningvlmssurvey`. Check each for a peer-reviewed version (AeroPath possibly has a journal version, not verified here).

## Counts
- SUPPORTED: 42
- PARTLY SUPPORTED: 2 (l. 63 `delange2022` Sec. 2; l. 143 `hu2022lora`)
- NOT SUPPORTED: 0
- WRONG SOURCE: 0
- CANNOT VERIFY: 0
- Uncited claims: 6 flagged (l. 39 must fix; l. 46, 47, 48 SKM-TEA paragraph; l. 52; l. 101), plus 2 acceptable
- Close paraphrase flagged: 1 (l. 73, De Lange definition)
