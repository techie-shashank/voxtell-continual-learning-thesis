# RegCL (continual SAM adaptation by regression merging) — fact card (tier B)
| | |
|---|---|
| Paper | Y.-c. Shu, Z. Lin, X. Zhou, Y. Wang, "RegCL: Compact Continual SAM Adaptation for Visual Grounding in Multi-Sensorial Media", arXiv:2507.12297v2 (28 Aug 2026); in: 2nd International Workshop on Multi-Sensorial Media and Applications (Mulsemedia '26), 10–14 Nov 2026, Rio de Janeiro, ACM, 10 pages, doi:10.1145/3841456.3841509 (p. 1, ACM reference format) |
| Bib key / Local PDF | NEW_regcl2025 (no bib entry yet) / papers/t6_cl_medseg_foundation/NEW_regcl2025.pdf |
| Version read | arXiv v2, the camera-ready version of the ACM workshop paper (peer-reviewed workshop, CC BY 4.0). The 2025 key and earlier title refer to arXiv v1 (2025), which was not read; the v1 title is not given in this PDF, so check the arXiv listing before citing either version. The v2 framing is "visual grounding in multi-sensorial media", not medical segmentation |
| Written | 2026-10-23, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: continual adaptation of SAM to a sequence of visually different 2D segmentation domains with a single constant-size adapter, without replay and without a growing library of domain-specific modules (Abstract; Sec. 1).
- Data (Sec. 4.1): five 2D datasets in the order Kvasir → CAMO → ISTD → ISIC → COD. Medical data are still evaluated, but only two 2D RGB datasets: Kvasir-SEG (gastrointestinal polyps) and ISIC (skin lesions); the others are camouflaged objects (CAMO, COD) and shadows (ISTD). No 3D, CT or MRI data. Dataset sizes and splits not stated.
- Method (two sentences): for each new domain an AugModule adapter (a LoRA-style module from SAMCL with N matrices B_i sharing one matrix A) in the frozen SAM ViT-B/16 image encoder is trained, then merged with the running adapter in closed form, W̄_t = (P_t + C_t)^−1 (P_t W̄_{t−1} + C_t W_t), where C_t = X_tᵀX_t is the input-feature inner-product matrix of the current task and P_t its running sum over earlier tasks (Sec. 3.2–3.3, Eq. 5–6; Algorithm 1, p. 5). Non-linear parameters (0.35 % of AugModule) are averaged arithmetically (Eq. 7; Table 5); default "RegCL+Seq" trains each adapter starting from the previous one, "RegCL" (independent) from the same initialisation, which makes the result invariant to task order (Sec. 3.3.1).
- Setting: domain-incremental, task identity not given, non-replay; one merged adapter at inference (Sec. 3.1). Mask decoder and prompt encoder frozen, point prompts; no text prompts. Not few-shot (full training sets; 20 epochs, batch 8, lr 0.005, cosine; Sec. 4.1). Loss MSE + focal + 10·Dice (Eq. 10).
- Evaluation: mIoU, mF1, mMAE; continual metrics ACC (mean of final row), BWT and FWT following GEM (Sec. 4.1, p. 6). Baselines: SAM, SAM3, LoRA-Seq, EWC, SPPA, LAG, O-LoRA, TIES, MagMax, DOP; Upper Bound = independent adapter per dataset (Table 1). Number of seeds not stated; no variance except across orders (Table 4).
- Best result (Table 1, p. 6): ACC mIoU RegCL+Seq 0.775 (BWT −0.007, FWT 0.668), RegCL 0.759 (BWT −0.024), vs DOP 0.771, MagMax 0.741, LoRA-Seq 0.691 (BWT −0.125), EWC 0.716, SAM 0.647, SAM3 0.745, Upper Bound 0.820. TIES has BWT 0.000 but ACC 0.736. Six task orders for independent RegCL: ACC mIoU 0.741–0.753, std ±0.005 (Table 4). With 300 replay samples per dataset: RegCL+Replay 0.809 mIoU vs ER 0.808, DER 0.804 (Table 2).
- Limitations stated by the authors: none stated explicitly; the conclusion names integration with non-visual sensory streams as future work (Sec. 5).

## Where it fits in Ch. 2 (suggestion)
- Sec. "Segmentation Foundation Models" (related_work.tex l. 87–94), as a contrast to SAM-Med3D-MoE and CA-SAM: a single shared adapter for SAM without task identity or routing, i.e. an exception to the "dedicated component" pattern stated at l. 94; best cited only briefly, since its medical part is two 2D RGB datasets.

## Relevance (NOT from the paper)
Its LoRA-Seq baseline corresponds to shared LoRA here (one adapter trained along the sequence) and shows clear forgetting (BWT −0.125 mIoU). It is the closest reviewed example of one shared parameter set without task identity for a segmentation foundation model, but it is 2D, point-prompted, not few-shot, and only two of five domains are medical. Cite the ACM workshop version (v2) unless the author decides otherwise.
