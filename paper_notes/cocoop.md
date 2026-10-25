# CoCoOp (Zhou et al., CVPR 2022) — paper notes

Partial notes: method section only (what Ch. 3.3 and Ch. 5.4.5 need).

| | |
|---|---|
| Paper | Zhou, Yang, Loy, Liu. *Conditional Prompt Learning for Vision-Language Models.* CVPR 2022, pp. 16816–16825 |
| Local PDF | `voxtell_paper/Zhou_Conditional_Prompt_Learning_for_Vision-Language_Models_CVPR_2022_paper.pdf` (CVF open-access version; page numbers = proceedings pages) |
| Bib key | `zhou2022cocoop`; CoOp itself = `zhou2022coop` (IJCV 2022) |
| Notes written | 2026-10-22 |

## 1. CoOp as summarised in CoCoOp (Sec. 3.2, p. 16818)
- Instead of a hand-written context such as "a photo of a", CoOp introduces M learnable context vectors {v_1, …, v_M}, each with the dimension of the word embeddings; the prompt for class i is t_i = {v_1, …, v_M, c_i}, with c_i the word embedding of the class name; context vectors shared among all classes. CLIP stays frozen.
- Problem stated by CoCoOp: the learned context is static and overfits the base classes, generalising poorly to unseen classes (Sec. 1).

## 2. CoCoOp (Sec. 3.3, p. 16818, Fig. 2)
- A lightweight network, the **Meta-Net** h_θ, generates for each input image a conditional token π = h_θ(x) that is added to every context vector: v_m(x) = v_m + π; prompt t_i(x) = {v_1(x), …, v_M(x), c_i} (Eq. 2 and text).
- Context vectors and Meta-Net trained together; Meta-Net = two-layer bottleneck Linear–ReLU–Linear, hidden layer 16× smaller than the input; input = image-encoder output features.
- Result direction: instance-conditional prompts generalise better to new classes (Sec. 4.1, Table 1).

## 3. Analysis for this thesis (NOT from the paper)
- The meta-net of the prompt-tuning strategy follows the same idea (offset computed from the image, added to a text-side vector) but differs: it shifts the **text query** of VoxTell's prompt decoder from [q; mean image features], has a GELU and a wide hidden layer (2048), and holds 12.59 M of 12.60 M trainable parameters (`thesis_notes.md` §2). Say "inspired by", not "as in".
