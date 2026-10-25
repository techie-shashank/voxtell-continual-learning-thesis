# CPE-CLIP — paper notes

Notes on the paper that the prompt-tuning strategy is adapted from. Read once, so the PDF does not have to be re-read.
Sections 1–6 are what the **paper** says, with locations; section 7 is **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | D'Alessandro, Alonso, Calabrés, Galar. *Multimodal Parameter-Efficient Few-Shot Class Incremental Learning.* arXiv:2303.04751v2 [cs.CV], 8 Jan 2024. 11 PDF pages |
| Published | ICCV Workshops 2023, pp. 3385–3395 (bib entry `D_Alessandro_2023`, @inproceedings, DOI 10.1109/ICCVW60793.2023.00364). The local PDF is arXiv v2; page numbers below are PDF pages, not proceedings pages |
| Affiliations | Neuraptic AI; Public University of Navarra (p. 1) |
| Notes written | 2026-10-21, from arXiv v2 |

## 1. Problem and idea (abstract, Sec. 1, p. 1–2)
- Few-Shot Class-Incremental Learning (FSCIL): a base session with many classes and examples, then sessions with few examples of new classes; task ID not given at evaluation (p. 1, Sec. 3 p. 3).
- Instead of adding modules to a backbone, CPE-CLIP (Continual Parameter-Efficient CLIP) uses frozen CLIP plus **learnable prompts in both the language and the vision encoder**, and **prompt regularisation** (p. 1–2).
- Claims < 0.3 % of the parameters trainable (p. 2); Table 5 (p. 9): about 400K learnable parameters.

## 2. Method (Sec. 4, p. 3–5; Fig. 1 p. 4)
- **Language encoder, G-Prompt**: L learnable tokens g prepended to the word embedding of the class name, [g_1…g_L, w] (p. 3–4). Layer-specific prompts up to depth D: Θ_g ∈ R^{D×L×d_NLP}. "Replacement": the output embeddings for the prompt tokens are discarded and new prompts are inserted in each layer up to D (Eqs. 2–4). Text representation = last hidden state of [EOS], linear projection (Eq. 5).
- **Vision encoder**: vision prompts derived from the language prompts through a learnable linear projection f_PROJ, Θ_fPROJ ∈ R^{d_NLP×d_CV}: g̃_i = f_PROJ(g_i) (p. 4). Vision prompts use **accumulation** instead of replacement: prompts of earlier layers are kept and concatenated (Eqs. 6–7), up to depth D (Eq. 8). Image representation = [CLS] state, linear projection (Eq. 9).
- **Classification**: softmax over cosine similarities between the image and each class-name text representation (Eq. 10).
- **Prompt regularisation** (p. 5): scaling factor α_t = |C_t| / Σ_{τ=0}^{t} |C_τ| (Eq. 11), C_t = classes of session t; the gradients of **both Θ_g and Θ_fPROJ** are multiplied by α_t (Eqs. 12–13), so the prompts are updated less as more classes have been seen.

## 3. Experiments and implementation (Sec. 5, p. 5–6)
- Benchmarks: CIFAR100 (60 base classes + 8 sessions × 5-way 5-shot), miniImageNet (same split), CUB200 (100 base + 10 sessions × 10-way 5-shot) (p. 5–6), splits of Tao et al.
- OpenAI CLIP 16×16 patches (ViT-B/16) from HuggingFace, Avalanche library; **SGD with momentum, LR 0.00325, weight decay 1e−5, cosine annealing with warm-up**; base session batch 32, 3 epochs (CIFAR100, miniImageNet) or batch 4, 6 epochs (CUB200); new sessions batch 4, 5 epochs; one GeForce RTX 2080 Ti (p. 6).
- Metrics: top-1 accuracy per session, performance dropping rate PD (last vs base session), average accuracy across sessions (p. 6).
- Hyperparameter search on CUB200, L ∈ {2, 4}, D ∈ {1, 3, 6, 9, 12}, 5 runs each: best **L = 2, D = 12** (70.23 avg.; Table 1 p. 6).

## 4. Results (Tables 2–5, p. 7–9)
- CIFAR100: Avg. 83.42, PD 7.31 (CLIP zero-shot 70.58 / 6.40). miniImageNet: 86.13 / 7.46 (zero-shot 75.35 / 3.96). CUB200: 70.79 / 16.98 (zero-shot 58.56 / 10.15).
- Training time and parameters (Table 5): CPE-CLIP 400K params; 0.69 h / 0.65 h / 0.27 h on the three benchmarks.

## 5. Ablation (Sec. 5.5, Fig. 2, p. 8–9; CUB200)
- **Removing prompt regularisation** gives the largest degradation, especially in middle sessions (Fig. 2, "No Regularization").
- Removing vision prompts: "does not appear to have a marked effect" on forgetting; slightly lower performance. Removing accumulation: slightly lower in the initial sessions.

## 6. Limitations stated by the authors (Sec. 6, p. 9–10)
- Depends on CLIP's vocabulary; unreliable for labels not well represented in it or ambiguous.
- Effect of regularisation for many sessions not explored; α_t approaches zero as sessions increase, so prompts may stop being updated, which can harm generalisation under distribution shift.

## 7. Analysis for this thesis (NOT from the paper; verify before using)
From `code/src/continual/strategies/cpe_clip/` and `thesis_notes.md` §2.
1. **Kept:** frozen pretrained model; learnable prompt tokens inserted layer-wise up to a depth (2 tokens, as the paper's best L = 2); "replacement" mode; a per-task gradient scale on the prompt tokens.
2. **Different:**
   - Location: the tokens are appended to the **cross-attention memory (image-side keys/values) of the first 3 of 6 prompt-decoder layers** of VoxTell, not to the input of a text encoder and a vision encoder. VoxTell's text encoder (Qwen3-Embedding-4B) stays untouched. There are no separate language and vision prompts and no f_PROJ.
   - Depth: 3 of 6 layers (paper's best: D = 12 of 12).
   - **Meta-net** (2d → 2048 → d, GELU) that adds an offset to the text query from [query; mean image memory]: not in CPE-CLIP. It holds 12,587,008 of the 12,599,296 trainable parameters. The author must say where this design comes from (it resembles conditional prompt learning, CoCoOp, ref. [64] in CPE-CLIP; CoCoOp is not in `literature.bib`).
   - Scale: γ_t = max(0.25, 1/t), applied to the tokens only (paper: α_t = |C_t|/Σ|C_τ| on Θ_g and f_PROJ). With one structure per task and no base session, |C_t|/Σ_{τ≤t}|C_τ| = 1/t, so the code's formula equals the paper's for this setting except for the 0.25 floor. **Inactive in the run (γ_t = 1 throughout, F2).** Because the paper's own ablation names regularisation as its most important component, the evaluated strategy lacks CPE-CLIP's key mechanism — another reason for the name "prompt tuning".
   - Segmentation loss (BCE + Dice) instead of classification CE; no base session; 10 epochs per task; init Xavier-uniform.
3. Both CPE-CLIP and the thesis use SGD with momentum (different LR and schedule).
