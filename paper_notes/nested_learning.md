# Nested Learning (Behrouz et al.) — partial notes (tier A: cited for one sentence in Sec. 7.3)

Source: arXiv:2512.24695 v1 (31 Dec 2025), read 2026-11-10 by a web-fetch agent from the abs page and the HTML version (the PDF did not yield text). Items marked [S] come from a model-extracted summary of unread text: check against the paper before quoting.

- Title (abs page): "Nested Learning: The Illusion of Deep Learning Architectures". Authors: Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, Vahab Mirrokni. Abs-page comment: "A version of this work is published at Neural Information Processing Systems (NeurIPS) 2025".
- Idea (Abstract, Sec. 1.2): a model is represented as "a set of nested, multi-level, and/or parallel optimization problems, each of which with its own 'context flow'"; each component has "its own internal gradient flow". Optimisers are viewed as associative memories of gradients.
- Continuum Memory System (Sec. 7.1): "a chain of MLP blocks" updated at different frequencies; argued (not shown experimentally) to help against catastrophic forgetting because knowledge lost in one block may remain in others.
- Hope (Sec. 8.3): self-modifying Titans followed by the Continuum Memory System; called "a continual learning module" in the Abstract.
- Continual-learning experiments (Sec. 9.1, Fig. 6): class-incremental **text classification** (CLINC, Banking, DBpedia) with Llama-3 backbones; baselines ICL, EWC, InCA. Continual translation of new languages (Manchu, Kalamang; Fig. 8) [S for results].
- Other experiments: long context (NIAH, BABILong, LongHealth = clinical text QA), language modelling and commonsense reasoning [S], an optimiser comparison on ViT/ImageNet-21K [S]. **No image segmentation, no 3D, no medical imaging.**
- Task identity at inference: not discussed.
- Limitations stated: higher memory usage (Sec. 9.1); M3 optimiser may face computational overhead at scale (Sec. 7.2).
- Use in the thesis: one sentence in Sec. 7.3 as a recent continual-learning proposal evaluated only on text; no claim about its performance on segmentation.
