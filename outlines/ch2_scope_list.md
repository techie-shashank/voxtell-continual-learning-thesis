# Ch. 2 scope: keep / mention / drop (proposal, 2026-10-26)

List decided by the author 2026-10-26; applied to `related_work.tex` and `tables/ch2_sota.tex` the same day (Ch. 2: 18 → 16 pp.). Covers the 46 works in Table 2.1 (`thesis/tables/ch2_sota.tex`, 45 rows; Zhang et al. and Liu et al. share one row). Revised 2026-10-26: LViT drop → mention, SAM-Med3D-MoE and CA-SAM mention → keep, CoCoOp added.

- **Keep**: full review in the text (findings, data, method, best result) + row in Table 2.1.
- **Mention**: stays cited in one sentence or half-sentence, no numbers, no table row.
- **Drop**: removed from Ch. 2 (none of the dropped works is cited in another chapter; checked with grep 2026-10-26).

Constraint: every tier C work of `papers/index.csv` (approved 2026-10-23) is kept; all 15 are (checked 2026-10-26). All drops and mentions are tier B.

Selection rule: keep a work if (a) the thesis builds on it (model, adapted method, metric), (b) it is one of the closest works to the gap (Table 2.2), or (c) a later chapter or a defense answer needs its findings. One or two representatives per family/sub-theme.

Framework works without a table row stay as they are: van de Ven (scenarios), De Lange, Liu et al. survey (families), Chaudhry, SPU (metrics), SEER (prompt wording; cited in Ch. 7; optional: give it a table row, since it covers the prompt-wording requirement).

| # | Work | Sec. | Proposal | Reason | Cited elsewhere |
|---|------|------|----------|--------|-----------------|
| 1 | SegVol | 2.1 | **Keep** (borderline, author 2026-10-26) | 3D model with text and spatial prompts; one of the 3D baselines in the VoxTell paper; text only as class names in a template | Ch. 1 |
| 2 | LViT | 2.1 | Mention | Half-sentence: text as extra input for a fixed class when labels are scarce, needed at inference (author's request 2026-10-26) | – |
| 3 | R-Super | 2.1 | Drop | Reports as training loss only; not promptable | – |
| 4 | CLIP-Driven Universal Model | 2.1 | **Keep** (author 2026-10-26) | 3D CT model with fixed CLIP class-name template; base of Zhang/Liu in 2.4 | – |
| 5 | SAT | 2.1 | Keep | Main 3D text-promptable competitor; VoxTell compares with it | Ch. 1, 3 |
| 6 | BiomedParse | 2.1 | Mention | 2D; one joint sentence with MedSAM-3 | – |
| 7 | MedSAM-3 | 2.1 | Mention | 2D; joint sentence with BiomedParse | – |
| 8 | VoxTell | 2.1 | Keep | The model adapted | Ch. 1, 3, 4, 5, 8 |
| 9 | Dissanayake et al. (review) | 2.2 | Mention | Used for the two-approach definition only; the row ("no single best method") gives nothing | Ch. 1 |
| 10 | UniverSeg | 2.2 | Mention | Example of the in-context approach we do not follow | – |
| 11 | Silva-Rodríguez et al. | 2.2 | Keep | Closest 3D few-shot fine-tuning work; shots overlap with ours | Ch. 7 |
| 12 | SEA-PEFT | 2.2 | Mention | Same setup as Silva-Rodríguez; one sentence | – |
| 13 | CLIP-LoRA | 2.2 | Keep | Our LoRA code comes from it; rank finding tested in Ch. 6 | Ch. 5 |
| 13a | CoCoOp (with CoOp) | 2.2 | Mention | Not in Table 2.1 so far (cited only in Ch. 1, 3, 5); one sentence next to CLIP-LoRA as the prompt-learning counterpart, so the source of our meta-net appears in Ch. 2; mechanism stays in Ch. 3.3 (added on the author's request 2026-10-26) | Ch. 1, 3, 5 |
| 14 | GIFT | 2.3.1 | Keep (short) | Single representative of replay, on the ZSCL benchmark | – |
| 15 | CGIL | 2.3.1 | **Drop** (author 2026-10-27) | Second replay example; not used elsewhere; replaced by a pointer to real-sample replay in 2.4.1 | – |
| 16 | ZSCL | 2.3.2 | Keep | Adapted method; ablation on current-task distillation used in Ch. 5 | Ch. 1, 3, 5, 8 |
| 17 | RAPF | 2.3.2 | Drop | Classification adapter; needs a paragraph on its family assignment | – |
| 18 | PRIMED | 2.3.2 | Keep | Medical ZSCL transfer; teacher ablation relevant to our distillation | Ch. 1, 7 |
| 19 | LiLoRA | 2.3.3 | Keep | Shared vs separate LoRA result mirrors our two LoRA strategies | – |
| 20 | MSLoRA-CR | 2.3.3 | **Keep** (tier C) | Medical LoRA per task with task identity given, the counterpart of our task-specific LoRA; tier C in `papers/index.csv` (approved 2026-10-23), so defended in the exam | Ch. 1 |
| 21 | S-Prompts | 2.3.3 | Mention | Needed only as example of a learned selector (defense D31) | – |
| 22 | CoLeCLIP | 2.3.3 | Mention | Task-specific prompt tokens; half-sentence | – |
| 23 | CPE-CLIP | 2.3.3 | Keep | Adapted method; gradient-scaling ablation used in Ch. 6 | Ch. 1, 3, 5, 8 |
| 24 | MoE-Adapters | 2.3.3 | **Mention** (author 2026-10-27; was Keep, borderline, 2026-10-26) | Baseline of MedCRP-CL and MedPEFT-CL; 5-shot result on the ZSCL benchmark; selector example (D31) | – |
| 25 | Baweja et al. | 2.4.1 | Mention | Early EWC example; half-sentence together with Ozdemir et al. (Ozdemir has no table row; its numbers in l. 227-228 go, the citation stays) | – |
| 26 | Bera et al. | 2.4.1 | **Keep** (borderline, author 2026-10-26) | 3D replay of crops selected by target fraction and difficulty, against random full volumes; the alternative to our random sample selection | – |
| 27 | SegGAN | 2.4.1 | Drop | 2D generative replay; C²GR covers generative replay | – |
| 28 | C²GR | 2.4.1 | Keep | Text-template universal model; source of our TIL naming (decision 2026-10-26) | – |
| 29 | González et al. (autoencoder selection) | 2.4.1 | Drop | Model-per-stage selection; not needed for the gap | – |
| 30 | Continual Segment | 2.4.1 | Mention | Joint sentence with CL-Net (frozen encoder, decoders per dataset) | Ch. 1 |
| 31 | CL-Net | 2.4.1 | Mention | Joint sentence with Continual Segment | Ch. 1 |
| 32 | Low-rank MoE | 2.4.1 | Drop | Another expert-per-dataset method; covered by the joint sentence | – |
| 33–34 | Zhang et al. / Liu et al. | 2.4.1 | Keep | Language-conditioned 3D continual segmentation; in Table 2.2 | Ch. 1 |
| 35 | Lifelong nnU-Net | 2.4.1 | Keep | Strategy comparison with task-order dependence, like ours | Ch. 1 |
| 36 | Ranem et al. | 2.4.1 | Mention | Half-sentence in the comparison-studies paragraph | Ch. 1 |
| 37 | Beyond Forgetting | 2.4.1 | Keep | Benchmark of 16 strategies, plasticity and transfer; used in Ch. 7 | Ch. 7 |
| 38 | SAM-Med3D-MoE | 2.4.2 | **Keep** (promoted) | 3D pretrained model; measures the drop on categories it was not adapted to (Other classes 0.541 → 0.400, box), a precedent for our control-task drop (`paper_notes/NEW_wang2024sammed3dmoe.md`, Table 1 p. 7) | – |
| 39 | CA-SAM | 2.4.2 | **Keep** (promoted) | Evaluates zero-shot on five unseen datasets after the sequence: CA-SAM stays close to frozen SAM, LwF and MoDA drop sharply (Table 2 p. 6); the closest precedent for our control task in continual segmentation; also reports task-order robustness (Table 8). Ch. 2 text does not mention this yet (`paper_notes/NEW_wang2026casam.md`) | – |
| 40 | RegCL | 2.4.2 | Mention | One sentence (single merged adapter, comparable to shared LoRA) | – |
| 41 | CLoPA | 2.4.2 | Drop | No task sequence | – |
| 42 | MedSeqFT | 2.4.2 | Keep | Sequential FT of a pretrained 3D model; in Table 2.2 | Ch. 1 |
| 43 | Chen et al. 2026 | 2.4.2 | Keep | Closest few-shot 3D continual work; in Table 2.2 | Ch. 1 |
| 44 | MedCRP-CL | 2.4.3 | Keep | Closest text-promptable continual work; Table 2.2 | Ch. 1, 7 |
| 45 | PA-EWC | 2.4.3 | Keep | Closest; Table 2.2 | Ch. 1 |
| 46 | MedPEFT-CL | 2.4.3 | Keep | Closest; Table 2.2 | Ch. 1, 7 |

Totals (recounted 2026-10-26; the first version said 19/20/8, which was off by one): Keep 25 rows (26 works), Mention 14 table works + CoCoOp, Drop 6 (R-Super, RAPF, SegGAN, González et al., low-rank MoE, CLoPA). Ozdemir et al. (no table row) is reduced to a mention.

Borderline cases MoE-Adapters, SegVol and Bera et al. moved to keep (author, 2026-10-26). RAPF stays dropped, although MedCRP-CL used it as a segmentation baseline (`paper_notes/NEW_medcrpcl2026.md:88`).

Estimated saving: Table 2.1 from about 4.6 to about 2.5 pages; text about 2–3 pages (paragraph l. 32–34, RAPF paragraph l. 153–159, S-Prompts/CoLeCLIP/MoE-Adapters paragraphs compressed, 2.4.1 regularisation and parameter-isolation paragraphs, 2.4.2 SAM paragraph). Total about 3.5 pages.

Side effects to handle when applying:
- Table 2.1 caption: "Works cited only for a definition, a mechanism or a single finding are not listed" stays valid; mentions fall under it.
- 2.5 summary sentences reference SAT/VoxTell, few-shot FT, VLM CL, Chen et al., Gao et al.: all kept.
- `literature.bib`: dropped entries become uncited; biblatex prints only cited works, so no bib change needed.
- Defense D31 relies on S-Prompts and MoE-Adapters as selector examples: both kept as mentions.
- Gap claim 2.5 (l. 339) says none of the four closest works measures pretrained ability outside the sequence. True, but CA-SAM and SAM-Med3D-MoE do, with spatial prompts; 2.4.2 should say so, so that the control task is not presented as new (defense D51).
