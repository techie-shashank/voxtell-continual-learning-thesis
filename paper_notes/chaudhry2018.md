# RWalk / forgetting and intransigence (Chaudhry et al., ECCV 2018) — paper notes

Partial notes: Sec. 3 (metrics). Sections 1–2 are what the **paper** says; section 3 is **analysis for this thesis**.

| | |
|---|---|
| Paper | Chaudhry, Dokania, Ajanthan, Torr. *Riemannian Walk for Incremental Learning: Understanding Forgetting and Intransigence.* ECCV 2018, LNCS, pp. 556–572 (bib) |
| Local PDF | `voxtell_paper/chaudhary_riemann.pdf` = arXiv:1801.10112v3 (14 Aug 2018), 22 pages; page numbers below are arXiv pages, cite by **section/equation** |
| Bib key | `Chaudhry_2018` |
| Notes written | 2026-10-22 |

## 1. Metrics (Sec. 3, p. 4–6)
- **Index convention (reversed w.r.t. this thesis):** a_{k,j} ∈ [0, 1] = accuracy on the held-out test set of task j after training incrementally on tasks 1 to k (j ≤ k). Average accuracy A_k = (1/k) Σ_{j=1}^{k} a_{k,j} (p. 5).
- "some other task specific measure of correctness (e.g., IoU for object segmentation) can also be used while the definitions of forgetting and intransigence remain the same" (Sec. 3, p. 5).
- **Forgetting** (Eq. 3, p. 5): f_j^k = max_{l ∈ {1,…,k−1}} a_{l,j} − a_{k,j}, for j < k; "the difference between the maximum knowledge gained about the task throughout the learning process in the past and the knowledge the model currently has about it". Average forgetting F_k = (1/(k−1)) Σ_{j=1}^{k−1} f_j^k; lower is better. f ∈ [−1, 1]; negative forgetting = positive backward transfer.
- Why max instead of a_{j,j} (as in GEM [15]): example a_{1,1..4} = 0.7, 0.8, 0.6, 0.5 → f = 0.3 with max, 0.2 with a_{1,1}; max captures changes along the learning process (p. 5).
- **Intransigence** (Eq. 4, p. 6): I_k = a*_k − a_{k,k}, with a*_k the accuracy on task k of a reference model trained on ∪_{l=1}^{k} D_l (all data at once); lower is better; "an approximation can be proposed" when the reference is too expensive. Negative I_k = positive forward transfer.
- Trade-off: strong regularisation → less forgetting, more intransigence; weak → the opposite (p. 4).

## 2. Setting
- Incremental classification with multi-head (task given) or single-head evaluation (Sec. 2.1); MNIST and CIFAR-100 experiments.

## 3. Analysis for this thesis (NOT from the paper)
- Thesis a_{i,j} = task i after stage j, so Chaudhry's a_{k,j} corresponds to the thesis's a_{j,k}. Final Forgetting = F_T with this mapping; the max over l = 1, …, T−1 includes stages before task i was trained, which exist in the thesis matrix because every task is evaluated at every stage (kept unchanged, `thesis_notes.md` §1 2026-10-18).
- Adaptation = mean of a_{k,k}, the second term of Eq. 4, without the reference a*_k (no joint run until the reruns).
- DSC in place of accuracy is covered by the IoU remark on p. 5.
