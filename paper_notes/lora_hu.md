# LoRA (Hu et al.) — paper notes

Notes on the parts of the LoRA paper that the thesis cites. Not a full summary.
Sections 1–3 are what the **paper** says, with locations; section 4 is **analysis for this thesis**.

| | |
|---|---|
| Paper | Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang, Chen. *LoRA: Low-Rank Adaptation of Large Language Models.* ICLR 2022 (local PDF is arXiv "Version 2", 26 pages) |
| Local PDF | `voxtell_paper/lora_hu.pdf` |
| Bib key | `hu2022lora` (@inproceedings, ICLR 2022) |
| Notes written | 2026-10-21. Page numbers = PDF pages |

## 1. Method (Sec. 4.1, p. 4)
- For a frozen pretrained weight W₀ ∈ R^{d×k}, the update is constrained to a low-rank decomposition: W₀ + ΔW = W₀ + BA, B ∈ R^{d×r}, A ∈ R^{r×k}, r ≪ min(d, k); h = W₀x + BAx (Eq. 3). W₀ frozen, A and B trained.
- Initialisation: random Gaussian for A, zero for B, so ΔW = BA = 0 at the start.
- ΔWx is scaled by α/r, α a constant in r; with Adam, tuning α ≈ tuning the learning rate; α set to the first r tried and not tuned.
- No additional inference latency: W = W₀ + BA can be merged; switching tasks = subtract BA, add B'A' (p. 4–5).

## 2. Applying LoRA to Transformers (Sec. 4.2, p. 5)
- Only attention weights (W_q, W_k, W_v, W_o of the self-attention module) are adapted; MLP modules frozen "for simplicity and parameter-efficiency".
- Example given: r = 4 with only the query and value projections adapted reduces the GPT-3 checkpoint from 350 GB to 35 MB.

## 3. Which weights to adapt (Sec. 7.1, Table 5, p. 10) and rank (Sec. 7.2, Table 6, p. 10)
- Fixed budget of 18M parameters on GPT-3 175B (r = 8 for one weight type, r = 4 for two, r = 2 for four).
- Table 5 (validation accuracy, WikiSQL / MultiNLI): W_q 70.4 / 91.0; W_k 70.0 / 90.8; W_v 73.0 / 91.0; W_o 73.2 / 91.3; W_q,W_k 71.4 / 91.3; **W_q,W_v 73.7 / 91.3**; all four 73.7 / 91.7. Caption: "Adapting both W_q and W_v gives the best performance overall."
- Text: putting all parameters in W_q or W_k is clearly worse; adapting W_q and W_v is best, so it is preferable to adapt more weight types with a smaller rank.
- Table 6: for {W_q, W_v}, a rank as small as 1 already suffices on these datasets.

## 4. Analysis for this thesis (NOT from the paper)
- The thesis cites Sec. 7.1 / Table 5 for the choice of W_q and W_v. The evidence is from the **self-attention of GPT-3 on NLP tasks**; the thesis applies it to the **cross-attention of VoxTell's prompt decoder**, which was not tested. Say so.
- Differences in the thesis's implementation (`code/src/continual/strategies/lora/common/layers.py`): scaling α/√r (rsLoRA) instead of α/r; A initialised Kaiming-uniform instead of Gaussian; optimiser SGD instead of Adam.
