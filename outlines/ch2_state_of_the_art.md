# Ch. 2 State of the Art — outline, revision 2 (APPROVED 2026-10-23)

Decisions (author, 2026-10-23, on Claude's recommendations): Q1 gap = (i) 3D + (ii) free text + (iii) adapting a pretrained model + (iv) few-shot in the claim, (vi) retention of pretrained ability as a second sentence, (v) described as the setting; wording from the 2.5 interview. Q2 De Lange families as frame, Liu et al. VLM paradigms as refinement. Q3 Table 2.1 = all tier B and C works, compact columns, in the chapter. Q4 ≈ 11–12 pp. accepted; 2.1.2 and 2.3.1 shortened to 2–3 sentences each.

Revision 1 (2026-10-22) was based on the author's notes only. Revision 2 is based on the paper notes: 15 full notes (`paper_notes/<key>.md`), 33 fact cards (`paper_notes/cards/`), 25 tier A checks (`reviews/ch1_ch2_tierA_citation_check.md`), the consolidated corrections (`reviews/ch1_ch2_source_check.md`) and two recorded searches (`papers/search_log.md`). Index of all works: `papers/index.csv`.

## Ground rules (unchanged from revision 1, plus)
- Delivers: per work main findings, dataset (n, labels), method, best result; grouped by theme, compared critically; one summary table; ends with the gap.
- Boundaries: scenarios (TIL/DIL/CIL) and method families defined here at first use (`sec:cl-vlm` label kept, Ch. 3.2 points to it); mechanisms in equations stay in Ch. 3.3; our design decisions stay in Ch. 5 (one pointer sentence each).
- **Facts only from the notes/cards.** Every number as the paper reports it (% or [0,1]) **with its metric and setting** (e.g. "Last, ODCL-CIL, Order I"). Where a paper contradicts itself, use the main table and say so only if it matters.
- Peer-reviewed version cited where one exists (list in `reviews/ch1_ch2_source_check.md`); bib fixes only on request.
- Nothing from the old Ch. 1 sentences at `introduction.tex:20, 22, 27` (unmarked close paraphrase).
- "this thesis", "we"; strategy names as in CLAUDE.md; `\gls{}`.
- Budget ≈ 10 pp. text + tables. With ≈ 50 reviewed works this needs short treatment of distant works (one sentence + table row) and detail only for the closest (2.4.3, Chen 2026, Liu/Zhang).

## Chapter intro (3–4 sentences)
Three areas plus the few-shot constraint, in section order.

## 2.1 Text-Promptable Medical Image Segmentation (≈ 2 pp.) — `sec:text-promptable-seg`
1. **Spatial and text prompts as two parallel lines** (one paragraph): MedSAM, SAM-Med2D (spatial); SegVol takes both (box + text through CLIP); define *text-promptable* (umbrella) vs *free-text promptable*. Not "early approaches were visual".
2. **Text as an input to 2D segmentation** (2–3 sentences): LViT, TextMatch (text is needed at inference too, 2D), R-Super (report-derived losses, plus 50–1.7K masks). Corrects the "auxiliary supervision only" framing.
3. **Fixed-vocabulary text prompts:** CLIP-Driven Universal Model (ICCV 2023; numbers from that paper — check 3,410 = 2,100 train + 1,310 val), BiomedParse (2D; slice-wise limitation backed by SAT Sec. 2.3), MedSAM-3 (2D; text-only Dice 0.08–0.57), SAT (3D, 497 classes; "comparable" to 72 nnU-Nets, 78.81 vs 80.54; external tests = new centres, known classes), Text3DSAM.
4. **Free-text prompts: VoxTell** (`paper_notes/voxtell.md`; cite the CVPR 2026 version): data, fusion (one sentence), zero-shot 70.85 % vs 51.23 % SAT; **SKM-TEA 10.72 %** and the authors' few-shot future-work remark. **Prompt wording:** SEER finds VoxTell the most robust of five models but with an 18-point worst-case drop on PENGWIN (Table 1) → sets up the fixed-prompt limitation (D10).

## 2.2 Few-Shot Adaptation of Segmentation Models (≈ 1 p.) — NEW, `sec:sota-few-shot`
1. **Two meanings of few-shot:** the review (`theekshana26fewshot`) defines N-way K-shot on novel classes, often without weight updates; in-context models (UniverSeg: 71.8 held-out Dice vs 84.4 nnU-Net upper bound) are the extreme case. This thesis uses the other meaning, fine-tuning on k labelled volumes, which the review files under transfer learning. One-sentence definition of a shot.
2. **Few-shot fine-tuning of 3D segmentation foundation models:** Silva-Rodríguez et al. (K = 1/5/10 volumes; LoRA vs full fine-tuning; LoRA on the encoder only weak on novel organs), SEA-PEFT (same protocol, automatic adapter choice; full fine-tuning flat from 5 to 10 shots). These are the precedent for k = 5/10/20 (pointer to Ch. 5).
3. **Few-shot adaptation of vision–language models:** CLIP-LoRA (rank-2 LoRA, one configuration for 11 datasets, chosen from ablations on 3).
4. Bridge: all single-task; Chen 2026 is the only few-shot continual 3D work (2.4.2).

## 2.3 Continual Learning for Pretrained Vision–Language Models (≈ 2.5 pp.) — `sec:cl-vlm`
Opening:
- **Scenarios** after van de Ven (`van_de_Ven_2025`, defines them); one sentence that our setting fits none (`\cref{sec:bg-cl}`).
- **Method families:** replay, regularisation, parameter isolation (`delange2022`); VLM refinement into multimodal replay, cross-modal regularisation, parameter-efficient adaptation (`liu2026continuallearningvlmssurvey`, Sec. 4). *Q2.*
- **Evaluating a pretrained model:** forgetting/intransigence (Chaudhry), loss of zero-shot transfer (ZSCL), control set (SPU); equations in Ch. 3.4.
2.3.1 **Multimodal replay:** GIFT (synthesised pairs; keeps class names; Order I numbers), CGIL (latent replay, frozen encoders; "joint" = CoOp joint prompt tuning).
2.3.2 **Cross-modal regularisation:** ZSCL; RAPF (frozen encoders + linear adapter + feature replay; its own grouping is frozen-backbone methods — say where we place it and why); **medical:** PRIMED (BiomedCLIP, 2D classification, ZSCL-style distillation on retrieved data; previous-task teacher better than initial teacher → D42).
2.3.3 **Parameter-efficient adaptation:** LoRA (O-LoRA = NLP, orthogonal subspaces; LiLoRA, Single-type; MSLoRA-CR `Zhang_2025`: medical MLLM, summed per-task LoRA, 2D, no segmentation); learned prompt tokens (S-Prompts — selection matters less than claimed, 80.12 % with random selection; CoLeCLIP — Last, ODCL-CIL; CPE-CLIP); mixture of experts (MoE-Adapters; routing failure as our argument, backed by its Sec. 4.3/5).
Capacity argument: only as an expectation (or to Ch. 7).

## 2.4 Continual Learning for Medical Image Segmentation (≈ 3 pp.) — `sec:cl-medseg`
Opening: partial-annotation conflict (Liu 2022; "complete regions" as our reasoning); in our setting each task's mask labels one structure, VoxTell predicts one binary mask per text prompt.
2.4.1 **Networks trained for the tasks:**
- Regularisation/distillation: Baweja (EWC, NIPS 2018 workshop), Ozdemir (distillation + example selection), ILT and MiB **from natural-image segmentation**, Liu 2022/2023.
- Replay: Bera (crop selection by target-voxel fraction; 12 crops vs 3 volumes), SegGAN (2D slices; vs MiB + Dice loss), C^2GR (diffusion replay for a universal model trained from scratch, 20 tasks, 2D, task prompt from a fixed template).
- Parameter isolation: González (domain-specific experts, each fine-tuned from the previous), Continual Segment (pruned decoders, upper bound = 4 nnU-Nets), CL-Net (decoders updated by EMA and sharing features; 85.7 % C36 / 86.1 % U36; 92.6 % only for the 5-dataset experiment), low-rank MoE (per-task LoRA experts, CLIP-based gates).
- Language-conditioned: Zhang et al. (MICCAI 2023), extended in Liu et al. (MedIA 2024) — fixed CLIP class-name template, one head per class; one discussion, one table row.
- **Comparisons:** Lifelong nnU-Net (Sci. Rep.: hippocampus, prostate, cardiac; order dependence via learning curves; scenario and architecture not varied), Ranem (ViT helps only in plain sequential training), Beyond Forgetting (2026: no strategy meets all requirements; order matters; reports plasticity and forward transfer). These carry "no strategy can be assumed best in advance".
2.4.2 **Pretrained segmentation foundation models:**
- SAM-based: SAM-Med3D-MoE (points/boxes; experts fine-tuned separately, gated), CA-SAM (2D images, per-dataset alignment layers, VAE router), RegCL (LoRA merging; 2 of 5 domains medical), CLoPA (within-task adaptation, one sentence).
- 3D foundation models: MedSeqFT (self-supervised CT backbone; per-task heads; earlier tasks not re-evaluated; gains vs parallel FFT), **Chen 2026** (frozen 3D brain-MRI model, per-task LoRA + head, 16/32/64 shots, Table 1 Dice 0.60 ± 0.08; no text).
- Observation (two sentences, not a design argument): capability added per task is held in dedicated components reached by task identity, routing, or class heads.
2.4.3 **Continual learning of text-promptable segmentation models** (NEW, the closest works, most detail): MedCRP-CL (ICML 2026 per PDF), PA-EWC, MedPEFT-CL (WACV 2026). All 2D CLIPSeg; tasks = datasets; full data; descriptive or templated prompts; compare sequential fine-tuning, EWC, LwF, LoRA, ZSCL, MoE-Adapters; adapters chosen by prompt similarity (MedCRP-CL, MedPEFT-CL; D43); none measures loss of pretrained ability. Note their internal inconsistencies only where we use a number.

## 2.5 Summary and Research Gap (≈ 1 p. text + tables) — `sec:sota-summary`
1. **Table 2.1** (tier B and C works; tier A works cited for a mechanism are excluded, stated in the caption): Work | Data (dataset, n, modality, 2D/3D) | Approach (prompt type; CL setting in the paper's own terms) | Metric | Best reported result. `thesis/tables/ch2_sota.tex`, rebuilt without `\newline` in `p{}` cells. *Q3.*
2. **Gap paragraph** — interview first (Q1). Dimensions the notes support: (i) 3D; (ii) free-text prompts; (iii) adapting a *pretrained* universal model (vs C^2GR, trained from scratch); (iv) few-shot; (v) tasks = new structures in one dataset; (vi) retention of pretrained ability measured (none of the closest works does). The claim must keep at least 3D + free-text; any version without 3D is false (MedCRP-CL, PA-EWC, MedPEFT-CL). The search behind it is stated (`papers/search_log.md`: OpenAlex, PubMed, arXiv, citing works of VoxTell and SAT, 2026-10-23).
3. **What this thesis does** (3–4 sentences, no new algorithm, pointer to `\cref{sec:method-strategies}`).
4. **Table 2.2 positioning:** rows Zhang/Liu, MedSeqFT, Chen 2026, MedCRP-CL, PA-EWC, MedPEFT-CL, this thesis; columns Prompt | 3D | Pretrained model | Few-shot (k) | Task identity at inference | Pretrained ability measured | Strategies compared. "This thesis" row after the reruns (which strategies have few-shot runs).

## Questions for the author (block the outline)
**Q1 Gap (interview at 2.5, but the direction now):** which of (i)–(vi) do you want in the claim? My suggestion: (i)+(ii)+(iii)+(iv) in the claim, (vi) as a second sentence ("…and none measures how much of the pretrained model's ability outside the task sequence is retained"), (v) as a description of the setting, not a gap.
**Q2 Taxonomy:** De Lange's three families as the frame, Liu et al.'s VLM paradigms as the refinement (Ch. 5.4 already uses Liu)?
**Q3 Table 2.1 scope:** ≈ 45 rows (tiers B and C) ≈ 3 pages. Options: (a) all B and C; (b) only works discussed with a result in the text (≈ 30); (c) (a) in the appendix and a short version in the chapter — not allowed as the only version, since the thesis must be understandable without the appendix. Recommended: (a), compact columns.
**Q4 Page budget:** with 2.2 and 2.4.3 new, the chapter will be ≈ 11–12 pp. including tables, over the ≈ 10 guide. Accept, or cut 2.3.1 (multimodal replay) and the 2D text-input works (2.1.2) to one sentence each?

## Order of work after approval
2.1 → 2.2 → 2.3 → 2.4 → 2.5 text → Table 2.1 → (after the reruns) Table 2.2 row. Each section: draft from the notes with `% CLAUDE-DRAFT`, compile, then the citation-verifier on the section.

---

## Session handoff (written 2026-10-23, end of the sources + 2.1 session)

**Start of the next session — read only this:** this outline (sections above + this handoff), then for the section being drafted only its notes/cards. Do not reread `thesis_notes.md` or the diagnosis in full; grep them if needed.

**Status**
- Sources finished: 15 full notes (`paper_notes/<key>.md`), 33 cards (`paper_notes/cards/<key>.md`), 25 tier A sentence checks (`reviews/ch1_ch2_tierA_citation_check.md`). Index with tier, notes path, peer-reviewed venue: `papers/index.csv`. Cards/notes for works without a bib key at the time use file names `NEW_<name><year>`; the bib keys are now (`papers/index.csv` still lists the NEW_ names): `wang2024sammed3dmoe`, `wang2025casam`, `ye2025medseqft`, `gao2026medcrpcl`, `gao2025paewc`, `gao2026medpeftcl`, `liu2024universalextensible`, `silvarodriguez2023fseft`, `chen2024lowrankmoe`, `shu2025regcl`, `li2026c2gr`, `wang2026beyondforgetting`, `esmaeili2026clopa`, `ly2026seapeft`, `zhang2026seer`; GIFT = `wu2024gift`.
- All corrections to the author's old Ch. 1/2 notes, by line: `reviews/ch1_ch2_source_check.md` (use as input; the old 2.2–2.5 text is still in `thesis/related_work.tex` below the new 2.1 and is replaced section by section).
- **2.4 drafted and citation-checked, 2.5 text drafted after the gap interview, Tables 2.1 and 2.2 written (2026-10-23).** Remaining: page-budget decision (Ch. 2 = 19 pp.), Table 2.2 "This thesis" row after the reruns, chapter page count/todos/tracker at the end.
- **2.3 drafted and citation-checked 2026-10-23** (`reviews/ch2_s3_citation_check.md`, 3 partly supported + 2 uncited sentences fixed; O-LoRA dropped, scope sentence added, author decision). Next: 2.4.
- **2.2 drafted and citation-checked 2026-10-23** (`reviews/ch2_s2_citation_check.md`, 1 unsupported + 7 partly supported claims fixed); 2.1 approved by the author 2026-10-23. Next: 2.3.
- **Drafted:** chapter intro + 2.1 (`thesis/related_work.tex`, `% CLAUDE-DRAFT`), citation-checked (`reviews/ch2_s1_citation_check.md`) and fixed. Waiting for the author's feedback on scope and tone before 2.2.
- Author's old notes backed up: `backups/related_work_author_notes_2026-10-23.tex`. Bib backup before the update: `backups/literature_2026-10-23_before_bib_update.bib`.
- `literature.bib` updated (16 new entries, ~30 upgrades; provenance comments above each entry). Open bib decisions: `thesis_tracker.md` → C "Bibliography checks".

**Next steps**
1. Author's feedback on 2.1 → apply.
2. Draft 2.2 → citation check → fix → show. Then 2.3, 2.4 the same way (new 2.x replaces the old text of that section; keep `\label{sec:cl-vlm}` and `\label{sec:cl-medseg}`, Ch. 3 refers to `sec:cl-vlm`).
3. Before 2.5: interview the author on the gap (decisions above: Q1). Table 2.1 in `thesis/tables/ch2_sota.tex`; Table 2.2 "This thesis" row after the reruns (cutoff 2026-11-01).
4. At the end: Ch. 2 page count, `python scripts/list_todos.py`, tracker, AI-use log.

**Per-section workflow (keeps quality, saves tokens)**
- Draft from the cards/notes only; every number with metric and setting, in the paper's form; one sentence per line; `% CLAUDE-DRAFT` above every paragraph; `\gls{}` (glossary has ct, cta, mri, pet, dsc, …).
- Compile (`cd thesis && latexmk -pdf -interaction=nonstopmode thesis_main.tex`); check only warnings inside related_work.tex (old 2.3/2.4 notes still produce `subsec:zscl`, `moe4cl2024` warnings until redrafted).
- Then one `citation-verifier` run on the new section only (notes first, `papers/text/<key>.txt` by grep for gaps). Fix what it finds, in particular close paraphrases and generalisations without a source.
- At most two background agents at a time; ask for short final reports.

**Conventions and pitfalls found in this session**
- Notes and cards were written from arXiv/preprint versions; several bib entries now point to the published version (SAT, LViT, VoxTell, Chen 2025, Silva-Rodríguez, Continual Segment, González "wrong"). Do not use page/table locators for those; flag numbers for a check against the published version in the final review.
- Lifelong nnU-Net: notes follow the **Sci. Rep.** version (cardiac, not pulmonary embolism).
- Zhang et al. 2023 (MICCAI) and Liu et al. 2024 (MedIA) report the same continual-learning experiment (Liu 2024, Sec. 2.5): one discussion, one table row.
- In Git Bash, heredocs passed to Python can lose backslashes; write scripts with the Write tool into the scratchpad instead.
- Paper texts: `papers/text/<key or NEW_name>.txt` (git-ignored, like the PDFs).
