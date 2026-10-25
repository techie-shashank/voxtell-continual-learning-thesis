# rsLoRA (Kalajdzievski) — paper notes

Sections 1–3 are what the **paper** says, with locations; section 4 is **analysis for this thesis**.

| | |
|---|---|
| Paper | Damjan Kalajdzievski (Tenyx). *A Rank Stabilization Scaling Factor for Fine-Tuning with LoRA.* arXiv:2312.03732v1 [cs.CL], 28 Nov 2023. 12 PDF pages |
| Local PDF | `voxtell_paper/rslora.pdf` |
| Bib key | `kalajdzievski2023rankstabilizationscalingfactor` (@misc arXiv; no peer-reviewed version found, `thesis_notes.md` §1 2026-10-21) |
| Notes written | 2026-10-22. Page numbers = PDF pages |

## 1. Setting and claim (abstract, Sec. 1–2.1, p. 1–2)
- LoRA sub-module: x_out = (W + γ_r B A) x_in + b, W ∈ R^{d2×d1}, A ∈ R^{r×d1}, B ∈ R^{d2×r}, B initialised 0, A iid with mean 0 and variance independent of r (Eqs. 1–2, p. 2). In LoRA as practised, γ_r = α/r (p. 2).
- Claim: dividing by r "results in slowed learning and stunted performance for LoRA with higher-rank adapters" (abstract); "causes gradient collapse as the rank increases ... such that LoRA fine-tuning using larger ranks performs no different than that with very small ranks" (p. 2).
- After fine-tuning, W + γ_r BA is stored as one matrix, so no extra inference cost (p. 2, p. 3).

## 2. Method and theory (Sec. 3, p. 3–4)
- Definition 3.1: an adapter is *rank-stabilised* if outputs and input gradients keep moments of order Θ_r(1) when inputs and output gradients do.
- Eq. 4: rsLoRA sets γ_r = α/√r. Theorem 3.2: in expectation over initialisation, all adapters are rank-stabilised iff γ_r ∈ Θ_r(1/√r); otherwise unstable or collapsing learning for sufficiently large r (p. 3). Analysis is in the limit r → ∞ (p. 3–4).
- The theorem says nothing about the quality of features learned with different ranks; practical benefit needs experiments (p. 4).

## 3. Experiments (Sec. 4, p. 4–5; App. B)
- Llama 2 fine-tuned on 20,000 OpenOrca examples, AdamW, LR 5e-5 constant; adapters in all linear attention and MLP modules; r ∈ {4, 8, 32, 128, 512, 2048} (p. 4).
- Fig. 2: LoRA converges to similar perplexity for all ranks; rsLoRA improves with higher rank. Fig. 3: LoRA gradient norm collapses with rank; rsLoRA keeps the same gradient norm across ranks at the start of training (p. 4–5).
- Ablations (p. 5, details App. B): same pattern with another model, dataset and optimiser; **same gradient-norm stability pattern with SGD**; LR sweep for LoRA r = 4 cannot match high-rank rsLoRA; adapters in attention modules only give similar results; rank-correcting only the initialisation is unstable.

## 4. Analysis for this thesis (NOT from the paper)
- Supports the Ch. 5 reason "α/√r because the shared adapter is trained with high ranks" (r up to 2048 in the rank ablation, same maximum rank as the paper's experiments).
- Evidence is from LLM fine-tuning; the SGD ablation matters because this thesis uses SGD.
- Caveat for Ch. 6: in this thesis α is fixed while r varies, so γ_r changes with r, as intended by rsLoRA; but the comparison with α/r was not run here.
