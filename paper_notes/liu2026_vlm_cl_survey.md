# Continual learning for VLMs: survey and taxonomy (Liu et al.) — partial notes

**Source: excerpt of Sec. 4 pasted by the author on 2026-10-21, not the full PDF.** Only what the excerpt says is recorded; extend from the PDF when available.

| | |
|---|---|
| Paper | Liu, Hong, Huang, Gomez-Villa, Goswami, Peng, Liu, van de Weijer, Tian. *Continual Learning for VLMs: A Survey and Taxonomy Beyond Forgetting.* arXiv:2508.04227 |
| Bib key | `liu2026continuallearningvlmssurvey` (@misc, arXiv) |
| Pages | the excerpt carries printed page numbers 12–16 (Sec. 4.2 starts on p. 12) |

## 1. Taxonomy (Sec. 4, "Taxonomy of VLM-CL Methods", Fig. 3)
- Three dominant paradigms: **(A) Multi-Modal Replay Strategies, (B) Cross-Modal Regularization (CREG), (C) Parameter-Efficient Adaptation (PEA)**.
- "these three categories of methods are not completely independent ... often appear in a hybrid form".

## 2. Cross-Modal Regularization (Sec. 4.2, p. 12–15, Fig. 5)
- Avoids explicit data rehearsal; preserves multimodal alignment through constraints during optimisation, with a frozen reference model or historical model states as guidance.
- Four paradigms:
  1. **Cross-modal structure preservation**: e.g. **ZSCL** aligns cross-modal similarity distributions of current and initial models (their Eq. 5); Mod-X, DKR, AwoForget, SeGP-CL, MG-CLIP.
  2. **Orthogonal and intrinsic subspace constraints**: GNSP, NuSA-CL, HMCL.
  3. **Asymmetric modality regularization**: DualTeacher, RAPF, SECA, SCD; **CPE-CLIP** and CLAP4CLIP mentioned for visual prompts / visually guided attention.
  4. **Fusion-level and hybrid regularization**: regularisation applied to cross-attention modules (CTP, MSPT, TRIPLET), PROOF, GIFT.

## 3. Parameter-Efficient Adaptation (Sec. 4.3, p. 15–17, Fig. 6)
- Restricts updates to a small set of task-specific parameters or modules, most of the backbone frozen; organised by four mechanisms:
  1. **Prompt-based parameter isolation**: S-liPrompt, LPI, PromptCCZSL; "Other approaches regulate prompt updates through gradient scaling (**CPE-CLIP**)".
  2. **Low-rank adaptation and subspace constraints**: LoRA; "sharing the same low-rank space across tasks can still introduce interference"; LW2G, KeepLoRA (orthogonal projections), CoDyRA, DAC.
  3. **Adapter-based parameter consolidation**: C-CLIP, CLAP4CLIP, ATLAS, DIKI, HypCL.
  4. **MoE-based adaptive routing**: MoE-Adapters, MoE-Confidence.
- Limitations: limited capacity as tasks grow; strict orthogonality may reduce plasticity; hybrids with regularisation and replay are increasingly explored.

## 4. Analysis for this thesis (NOT from the paper)
- Mapping used in Ch. 5.4: replay → (A); distillation-based → (B) cross-modal structure preservation (ZSCL); task-specific and shared LoRA → (C) low-rank; prompt tuning → (C) prompt-based (CPE-CLIP); shared LoRA + replay → hybrid (A)+(C); sequential fine-tuning → baseline outside the taxonomy.
- Not covered by the thesis: adapters, MoE, orthogonal / subspace constraints, asymmetric and fusion-level regularisation.
- Note: CPE-CLIP appears in two places of the survey (asymmetric modality regularisation and prompt-based PEA); the thesis uses the PEA placement, which matches what the prompt-tuning strategy does (learned tokens, frozen backbone).
