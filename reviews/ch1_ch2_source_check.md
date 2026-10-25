# Source check of the Ch. 1/2 notes against the papers (2026-10-22/23)

Consolidated from the paper notes (`paper_notes/<key>.md`), fact cards (`paper_notes/cards/<key>.md`) and the tier A check (`reviews/ch1_ch2_tierA_citation_check.md`). Each item gives the location in the paper in the notes/card file. Not yet checked: works on the manual download list (TextMatch, Text3DSAM, few-shot review, Bera et al., SegGAN, French, UK Biobank). Since Ch. 1/2 are redrafted, this list is input for the new text, not an edit list for the old one.

Verdicts: **W** wrong · **P** partly correct / overstated · **U** unsupported or uncited · **M** missing context · **D** declaration risk (unmarked close paraphrase)

## introduction.tex
| Line | Work | Verdict | Issue |
|---|---|---|---|
| 3 | SAT | P | supports weaker results on unseen categories, not on unseen imaging characteristics |
| 13 | SAM 3 | W | cited for clinicians prompting "segment the left ventricle"; SAM 3 takes short noun phrases only and struggles with medical terms (Sec. 1 p. 1; App. B p. 18) |
| 13 | MedSAM, SAM-Med2D | P | "early approaches relied on visual prompts": not earlier than text-conditioned models |
| 13 | SegVol | W | cited as a spatial-prompt model; it also takes text prompts and its headline results use box + text |
| 13 | — | U | definition of universal models uncited |
| 20 | Yu et al. survey | **D** | near-copy of Yu p. 2 ("different modalities exhibit varying forgetting rates"); the finding is the survey's citation of its ref. [40] — cite the original if kept |
| 20 | French 1999 | — | not checked (PDF missing); French is about connectionist networks in general, not fine-tuning of pretrained models |
| 22 | Liu et al. survey | **D** | structure, wording and citation chain (Kirkpatrick, iCaRL, Yoon in that order) follow Liu p. 2 |
| 22 | Liu et al. survey | P | TIL/CIL/DIL only named in the survey (Sec. 6.3.1); use van de Ven (Key Points p. 1, Sec. 2.3) |
| 22 | — | U | stability–plasticity definition uncited (van de Ven p. 3) |
| 27 | Liu et al. survey | **D** | follows Liu p. 2's "early compact models … modern models combine" pattern |
| 27 | Liu et al. survey | P | survey covers VLMs/MLLMs, not segmentation models; applying it here is the thesis's own step |
| 27 | — | U | architecture description of free-text promptable models uncited (VoxTell or SAT) |

## related_work.tex
| Line | Work | Verdict | Issue |
|---|---|---|---|
| 25 | LViT | W | text is also required at inference, not only auxiliary supervision; fusion in the ViT branch, PLAM is on the CNN skips; 2D |
| 25 | QaTa-COV19 | M | text-annotated version comes from LViT, not Degerli 2022 |
| 25 | R-Super | M | also trained with 50–1.7K masks; +16.0 = F1 points in one setting (UCSF pancreas) |
| 32 | CLIP-Driven | W | transfer compared with other pre-training methods (Table 6), not dataset-specific models; not best on JHH_cardiac |
| 34 | BiomedParse | U | "limited on volumetric scans" not in its paper; SAT Sec. 2.3 (p. 8) can support it |
| 34 | SAT | P | "matched 72 nnU-Nets": paper says comparable, mean 78.81 vs 80.54 (n.s.); external sets are new centres with known classes → "cross-centre", not zero-shot |
| 38 | ReXGroundingCT | M | prompts are GPT-4-extracted findings, not raw report sentences; VoxTell's result is on the validation split |
| 50 | GIFT | P | keeps a pool of earlier class names ("stores no data at all"); failure list overstated (Suppl. E: DTD, EuroSAT, MNIST; CIFAR-100 only low resolution) |
| 50 | CGIL | P | "protect the shared embedding space" is the author's framing; both encoders frozen |
| 54 | RAPF | P | "between regularisation and PEA" is the author's placement; paper groups itself with frozen-backbone + added parameters; also replays sampled class features |
| 60 | CLIP-LoRA | P | shared configuration chosen from ablations on 3 datasets; authors call choosing matrices/rank "not trivial" |
| 60 | O-LoRA | P | backs only "constrain the direction"; NLP method; preceding sentence uncited (O-LoRA Table 2 SeqLoRA could support it) |
| 62 | S-Prompts | P | dependence on domain identification overstated: 80.12 % with random selection, "not fundamentally influenced" (Table 4) |
| 62 | CoLeCLIP | M | vocabulary updated every iteration, with a per-task LoRA in the text encoder |
| 62 | CPE-CLIP | — | covered by `paper_notes/cpe_clip.md` (diagnosis C-2.6) |
| 64 | MoE-Adapters | U | "misrouted input cannot recover" is the author's reasoning; only partly backed (Sec. 5 threshold; Sec. 4.3, Fig. 5) |
| 72 | Liu 2022 | P | conflict is in the paper; "because 3D scans capture complete regions" is the thesis's reasoning |
| 77 | ILT, MiB | M | natural-image methods (Pascal VOC, ADE20K) in a paragraph on medical segmentation |
| 77 | ILT | P | no "spatial information" (that is PLOP's Local POD); ILT also distils output logits |
| 77 | Ozdemir 2018 | M | main contribution is example selection for replay; distillation alone reported insufficient |
| 77 | — | U | "Neither addresses the label conflict directly" is the author's judgement |
| 81, 198 | Lifelong nnU-Net | P | use cases hippocampus, prostate, cardiac are **correct** for Sci. Rep.; "ranking depends on scenario … architecture" unsupported (neither varied); order dependence only via learning curves (Fig. 4) |
| 81, 200 | Ranem | P | ViT retains more only in plain sequential training; with CL methods "only in some cases" (Sec. 4.5) |
| 83 | González 2023 | W | stages are domains of one structure ("domain-specific"); models are fine-tuned from the previous one, not independent |
| 83 | Continual Segment | W | upper bound = four separate nnU-Nets, not an ensemble; decoders pruned (0.98 of one decoder); encoder trained on dataset 1 then frozen |
| 83 | CL-Net | W | existing decoders are updated (EMA) and share features; "nothing learned benefits others" wrong |
| 85 | Zhang 2023 | P | pseudo-labels are hard (Eq. 1) despite "soft" on p. 2; not better on JHH step 1 (0.887 vs 0.891); "closed output set" is the author's reading |
| 92 | SAM-Med3D-MoE | M | expert mask fused with the general decoder by a weighted sum; paper inconsistent on which parameters are trained; Fig. 2 shows a text prompt never described |
| 92 | CA-SAM | U | "slice by slice" not in the paper; 5 of 9 datasets natively 2D; 99.42 % over 5 unseen datasets; MoDA has lower forgetting (0.66 %) |
| 96 | MedSeqFT | W | buffer distillation is in the full fine-tuning step (previous encoder as teacher); LoRA distillation uses new-task data |
| 96 | MedSeqFT | M | +3.0 / −10.0 mm vs parallel FFT; vs sequential FT ≈ 2.2 / 5.6 mm (own calculation); transfer worse on kidney organ |
| 98, 105 | Chen 2026 | P | Table 1 gives 0.60 ± 0.08 (abstract/Table 4: 0.62 ± 0.07); use 0.80 → 0.16 form; MAE "normalised scale" not in the paper |
| 101 (comment) | CA-SAM | W | 76.90 % is Avg-IoU; final Last-IoU 76.12 % |
| 115 | Chen 2026 | P | "only through task-specific modules": paper also compares LwF, replay, sequential linear |
| 120 | Lifelong nnU-Net | P | see 81 |
| 162 | MedSAM-3 | M | fractions, not %; text-only Dice 0.08–0.57; best on 3 of 4 datasets; never evaluated in 3D |
| 164 | SAT | P | see 34 |
| 172 | GIFT | M | numbers are Order I |
| 174 | CGIL | W | "joint 86.29 %" = CoOp joint prompt tuning |
| 180 | LiLoRA | M | add "Single-type" |
| 182 | S-Prompts | M | metric: average accuracy, S-liPrompts, CDDB-Hard |
| 184 | CoLeCLIP | W | metric is **Last** (ODCL-CIL, Order I), not "Final" |
| 188 | MoE-Adapters | W | key `moe4cl2024` missing → `yu2024boostingcontinuallearningvisionlanguage` |
| 206 | CL-Net | W | 92.6 % is the 5-dataset continual experiment; 235/36 model: 85.7 % (C36), 86.1 % (U36) |
| 208 | Zhang 2023 | M | keep [0,1] form 0.817 / 0.466 |
| 210 | SAM-Med3D-MoE | M | "--" cells can be filled from Table 1 |
| 212 | CA-SAM | W | "2D slices" → "2D images" |
| 214, 234 | MedSeqFT | M | 5 MRI tasks, 2 transfer tasks and most compared methods missing |
| 236 | Chen 2026 | M | baselines also LwF, replay, sequential linear |

## Possible defence point
- Teacher choice of the distillation-based strategy: PRIMED (`chen2025forging…`, Table 4a) found the previous-task model a better teacher than the initial model, opposite to ZSCL.

## Bibliography findings (report only; fix on request)
- Missing entries: `wu2024gift` (CVPR 2025 / arXiv 2025), SAM-Med3D-MoE, CA-SAM, MedSeqFT; `moe4cl2024` duplicate key.
- Duplicate: `Zhao_2024` = `zhao2025foundation-9de` (same DOI).
- arXiv entries whose PDF states a venue: S-Prompts (NeurIPS 2022), DEN (ICLR 2018), Memmel (DART @ MICCAI 2021), SegVol (NeurIPS 2024), Continual Segment (ICCV 2023; bib title differs from v4), Baweja (NIPS 2018 workshop).
- Wrong author: LiLoRA 4th author "Qi Wang" → PDF "Cheems Wang".
- Fields: `ukbiobank` empty pages / no number (19(11):1523 per Baweja's reference list); `Ozdemir_2018`, `Zhang_2025` no editor/place.
- Preprint PDFs read for published entries (page numbers may differ): Ma_2024, Kirkpatrick, LwF, iCaRL, Kemker, CLIP, van de Ven, BiomedParse, CLIP-Driven.
