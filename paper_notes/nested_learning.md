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

## NeurIPS 2025 version (the version cited in the bib) — read 2026-11-11 from the proceedings PDF
Source: https://proceedings.neurips.cc/paper_files/paper/2025/file/4309616aaed8e848009bc4a7ef73b493-Paper-Conference.pdf (35 pages, matches bib pages 46968-47002). Text extracted with pdftotext; page numbers are the printed ones.

- Structure: 1 Introduction, 2 Nested Learning, 3 HOPE: A Self-Referential Learning Module with Continuum Memory, 4 Experiments, references, NeurIPS checklist (p. 25ff.), appendices A-F.
- Continuum Memory System (Sec. 3, p. 9, Eq. 30-31): "a chain of MLP blocks", the parameters of the l-th block "updated every C(l) steps" (chunk size per block = update frequency). A standard Transformer MLP is the special case with one block whose frequency is zero after pre-training. Motivation (Sec. 3, p. 9): knowledge from pre-training "needs to rarely be updated over time", hence one feed-forward knowledge storage per update frequency.
- Argument against forgetting (App. C, p. 29, paragraph "CMS Design Helps with Continual Learning"): when one block is updated, knowledge "potentially forgotten" in it "is still stored in other components", i.e. in blocks updated less often, and can flow back through backpropagation, "and so hardly forgetting important knowledge". Presented as "a simple answer", i.e. an argument, not an experiment.
- HOPE (Sec. 3, p. 9-10): self-modifying Titans (replaces attention) + CMS (replaces the MLP block).
- Experiments in this version: only language modelling and common-sense reasoning (Sec. 4, Table 1, p. 10; App. F, p. 35): 760M / 1.3B parameters trained from scratch on 30B / 100B tokens (FineWeb-Edu + long-context documents), AdamW; baselines Transformer++, RetNet, DeltaNet, TTT, Samba, Titans (and RWKV-7, Comba, Miras, DLA in App. F). Sec. 4 says continual-learning results are "in the appendix", but the appendices A-F of this PDF contain **no continual-learning experiment** (no CLINC/Banking/DBpedia, no translation). Those experiments appear only in arXiv v1 (see above). No images, segmentation, 3D or medical data.
- Task identity / task boundaries: not discussed.
- Limitations: no limitations section in the main text, although the checklist (p. 25, item 2) says they are discussed there.
- Consequence for the thesis: with the NeurIPS citation, nested learning's benefit against forgetting can be stated only as the authors' argument (App. C); "evaluated only with language models" holds for both versions.
