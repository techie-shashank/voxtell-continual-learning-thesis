# Ch. 3 Theoretical Background — outline (APPROVED 2026-10-22)

Decisions: Q1 joint training and intransigence left out until the reruns finish; Q2 bootstrap only in Ch. 6 setup; Q3 (a) general LoRA equation in 3.3.1, Ch. 5 refers to it, soft Dice loss stays in Ch. 5; Q4 author adds the bib entries; Q5 Fig. 3.2 yes. Status: 3.1–3.4 drafted 2026-10-22, Fig. 3.2 built (`figures/tikz/ch3_metrics.tex`) (3.3 from paper_notes lora_hu, rslora, delange2022, zscl, cocoop, cpe_clip).

Scope: concepts as published, with citations; no own design choices, no values from our runs (Ch. 5 = own design, Ch. 6 = values). Readers are experts (chair 1.6.1): mention or cite standard methods, explain only what Ch. 5 and Ch. 6 need. Target about 9–10 pages, 2 figures. Notation: `thesis_notes.md` §5; every symbol listed there as "Ch. 3" is introduced here.

Resolves the Ch. 5 todos: "ref: Ch. 3" (method.tex:17), "evaluation matrix" (:63), "metrics" (:65), "VoxTell" (:129), "ZSCL" (:324), "CPE-CLIP" (:366).

## Chapter intro (2–3 sentences)
What the chapter provides and in what order.

## 3.1 Free-Text Promptable 3D Segmentation (about 3.5 pages)
3.1.1 Volumetric segmentation with encoder–decoder networks
- Segmentation of one structure as a voxel-wise binary decision: X, Y, Ŷ, f_θ(X, p) gives logits.
- U-Net-type encoder–decoder with skip connections at every resolution [`3d_unet`]; nnU-Net as the framework VoxTell is built on: patch-based training, sliding-window inference with Gaussian weighting [`isensee2018nnunetselfadaptingframeworkunetbased`]; residual encoder (ResEnc) [\todo{cite: nnU-Net revisited, Isensee et al. 2024}].
- One sentence on BCE + soft Dice as the usual loss. The equation stays in Ch. 5 (Eq. method-seg-loss).

3.1.2 Attention and transformer decoders
- Scaled dot-product attention and multi-head attention with W_q, W_k, W_v, W_o and d_h; cross-attention (queries from one source, keys and values from another) [\todo{cite: Vaswani et al. 2017}].
- Needed by Ch. 5: LoRA acts on W_q and W_v; the learned prompt tokens are appended to the keys and values.

3.1.3 Text conditioning and VoxTell
- Text embedding model, frozen, gives the query q [\todo{cite: Qwen3 Embedding}].
- VoxTell as published (`paper_notes/voxtell.md` §3), in thesis notation: image encoder (six stages), prompt decoder (text query attends to image features), stage-wise MLPs giving the guidance E_s with G vectors, fusion at every decoder resolution (paper Eqs. 4–6), deep supervision (Eq. 7). Contrast with single late fusion (MaskFormer-style; SAT) in one sentence.
- **Fig. 3.1** `figures/ch3_voxtell.pdf` (already built, overview without strategy marks), caption "adapted from [VoxTell, Fig. 2]".
- Pretraining as published, in two sentences (data size, three prompts per image incl. one negative). The differences of the released implementation (stage-4 keys/values, no self-attention) stay in Ch. 5.

## 3.2 Continual Learning (about 1 page; REDUCED 2026-10-22, drafted)
Split decided 2026-10-22: Ch. 1 = informal concepts (catastrophic forgetting, stability vs plasticity, few-shot), no formulas; Ch. 2 = scenario definitions (TIL/CIL/DIL) and method families, one sentence each with citation at first use (van de Ven, De Lange); Ch. 3.2 = only (1) the problem in symbols (tasks, stages, theta_t, evaluation matrix a_ij, forgetting as a_ij < a_ii, stability-plasticity, loss of pretrained ability per ZSCL) and (2) one paragraph on why our setting fits none of the scenarios. Method families: not in Ch. 3 (Ch. 2 and 5.4). Ch. 5.1 to shrink to the concrete instantiation later.

## 3.3 Methods Adapted by the Strategies (about 2.5 pages)
Only the mechanisms, as published; what we changed is in Ch. 5.4.
3.3.1 Low-rank adaptation: W = W_0 + (α/r)BA, initialisation, merging at inference [`hu2022lora`, Sec. 4.1]; rank-stabilised scaling γ_r = α/√r [`kalajdzievski2023rankstabilizationscalingfactor`] (see Q3).
3.3.2 Replay: memory of earlier samples mixed into training [`icarl2017` or other source, see Q4].
3.3.3 Knowledge distillation and ZSCL: teacher–student distillation [\todo{cite: Hinton et al. 2015}]; LwF (previous model as teacher, current data) [`li2017learningforgetting`]; ZSCL: initial model as teacher, similarity distributions on a reference set, weight ensemble Eq. 7, weight consolidation (`paper_notes/zscl.md` §3–4).
3.3.4 Prompt learning and CPE-CLIP: learned input tokens with a frozen backbone [\todo{cite: CoOp, Zhou et al. IJCV 2022}]; CoCoOp's meta-net conditioning on the image [`zhou2022cocoop`]; CPE-CLIP: layer-wise G-prompts, projection to vision prompts, gradient scaling α_t (written β_t here) (`paper_notes/cpe_clip.md` §2).

## 3.4 Evaluation Metrics (about 1.5 pages)
- DSC per volume, mean over a test set [\todo{cite: Dice 1945 or a metrics reference}].
- Evaluation matrix a_{i,j}, i = 1..T, j = 0..T [`Chaudhry_2018`; ZSCL Fig. 4b].
- Metric definitions (equations), as in `scripts/compute_cl_metrics.py`: Adaptation (diagonal, a_{k,k} term of the intransigence of Chaudhry et al.), Average Performance, Final Performance (ZSCL Avg., Last), Final Forgetting (Chaudhry Eq. 3), Transfer (ZSCL), control-task drop (SPU control set, `Zhang_2024_CVPR`).
- **Fig. 3.2** (new, TikZ): schematic T × (T+1) evaluation matrix with the cells each metric uses (diagonal, upper triangle, last column, column-wise max). Optional, see Q5.
- Why these metrics fit this setting: Ch. 6 setup (decision 2026-10-21), not here.

## Questions for the author (block the outline)
Q1 Joint reference: the reruns include joint fine-tuning. Define joint training and intransigence in 3.4 now (marked `\todo` until the results arrive), or keep both out until the runs finish (rule in notes §4: text describes existing runs)?
Q2 Bootstrap: explain the paired bootstrap in 3.4 as a concept, or only in Ch. 6 setup (notes §5 places N_boot in Ch. 6)?
Q3 LoRA equation: Ch. 5 (Eq. method-lora) already has W_0 + γ_r BA. Option (a): the general equation moves to Ch. 3 and Ch. 5 refers to it (Ch. 5 needs a small edit); option (b): Ch. 3 describes LoRA in words only. Same question for the soft Dice loss (proposal: it stays in Ch. 5).
Q4 Sources: which of the missing ones should be added to `literature.bib` (Vaswani, Hinton, CoOp, Qwen3 Embedding, nnU-Net revisited, a Dice reference)? Each needs a PDF or publisher page. For `van_de_Ven_2025`, `delange2022`, `PARISI201954`, `icarl2017` there are no paper notes; I may only attribute claims to them once you provide the paper or confirm what they say.
Q5 Fig. 3.2 (metrics schematic): yes or no?
