# Literature search record (Ch. 2)

Purpose: the basis for the gap statement in Ch. 2.5 ("to our knowledge, no prior work …"), which must state databases, terms and date (diagnosis Ci-6). Not thesis text.

## Inclusion rule (proposed 2026-10-22, to approve)
A work is reviewed in Ch. 2 if it falls in at least one theme and either is close to our setting or is needed for a specific argument:
1. **t1** Text-promptable medical image segmentation (text as target specification; language as auxiliary supervision only as context).
2. **t2** Few-shot adaptation of segmentation models (fine-tuning on k labelled volumes, or in-context models as the other meaning of few-shot).
3. **t3** Continual-learning foundations used by the thesis: scenarios, method families, evaluation of forgetting and of the loss of pretrained ability.
4. **t4** Continual learning for pretrained vision–language models.
5. **t5/t6** Continual learning for medical image segmentation: task-specific networks (t5) and pretrained segmentation foundation models (t6).

Excluded: general medical segmentation background cited only in Ch. 1 (nnU-Net, U-Net variants, dataset papers of other chapters); continual learning of LLMs (TRACE, Luo et al.), unless needed for an argument.

## Tiers
- **A**: cited for one mechanism, definition or dataset → the citing sentence is checked by the citation-verifier; no notes.
- **B**: a row in the summary table → fact card (dataset, n, labels/groups, method in two sentences, best result with metric; page/table for each).
- **C**: closest works, defended in the exam → full notes in `paper_notes/`, read by the author.

## Search 1 — 2026-10-22, by Claude (web search engine, not a bibliographic database)
| # | Query | Relevant new hits |
|---|---|---|
| 1 | continual learning text-promptable medical image segmentation model | MedCRP-CL (arXiv 2605.20297), PA-EWC (arXiv 2511.20732) |
| 2 | few-shot continual learning 3D medical image segmentation | none on the combination; few-shot-only works (MAML 3D U-Net, BiGRU few-shot) not taken |
| 3 | continual learning segment anything model medical image segmentation forgetting LoRA | RegCL (arXiv 2507.12297); EvoSAM, CoSAM/MoDA (reserve) |
| 4 | catastrophic forgetting fine-tuning universal medical segmentation foundation model vision-language | MedPEFT-CL (arXiv 2511.17668, WACV 2026); SAMed-2 (reserve) |
| 5 | parameter-efficient fine-tuning few-shot 3D medical image segmentation foundation model benchmark | Silva-Rodríguez et al. FSEFT (arXiv 2303.17051); SEA-PEFT (reserve) |
| 6 | VoxTell fine-tuning adaptation continual few-shot free-text segmentation 2026 | **no work adapting VoxTell continually**; VoxTell published at CVPR 2026; GitHub issue #16 (2026-10-19) asks whether text prompting survives fine-tuning (not citable, but shows the question is open) |
| 7 | incremental learning text-driven universal organ segmentation CLIP embedding new classes 3D CT | Universal Model, extensible version (Liu et al. 2024) |
| (id) | SAM-Med3D-MoE / MedSeqFT / CA-SAM / GIFT | identified: arXiv 2407.04938 (MICCAI 2024), 2509.06096, 2511.17201 (CVPR 2026 Findings?), CVPR 2025 pp. 2813–2823 |

Also found while searching, not proposed: Low-rank MoE for continual medical segmentation (arXiv 2406.13583, proposed as tier B after all, see index), "Continual Segmentation under Joint Nonstationarity" (arXiv 2605.20538, unclear relevance).

Facts about new works above come from search snippets only and are unverified until the PDFs are read.

## Search 2 — to be done by the author (≈20–30 min)
The thesis should name real databases. Proposed: run these in **Google Scholar** and **PubMed** (and arXiv listing search), restricted to 2018–2026, and note the date and hit counts here:
1. `"continual learning" AND segmentation AND ("text prompt" OR "vision-language" OR "language-guided") AND medical`
2. `("continual" OR "incremental" OR "lifelong") AND "foundation model" AND "3D" AND segmentation AND medical`
3. `"few-shot" AND ("continual" OR "incremental") AND segmentation AND (MRI OR CT)`
4. `VoxTell` (citing works) and `SAT "text prompts"` citing works with "continual"
New hits that pass the inclusion rule go into `index.csv` (proposal = "new (search 2)").

## Search 2 — 2026-10-23, by Claude via official APIs (replaces the planned manual search)
Script: `papers/search/run_search.py` (rerunnable); raw hits: `papers/search/raw_2026-10-23.jsonl`.
- Keyword search: OpenAlex (6 queries × top 30, 2018–2026), PubMed (3 Boolean queries, all hits: 2, 1, 4), arXiv (4 queries on abstracts, all hits: 46, 37, 5, 1). Semantic Scholar keyword search dropped (HTTP 429, unauthenticated rate limit).
- Citation search: works citing VoxTell (Semantic Scholar 23; OpenAlex found no record) and SAT (Semantic Scholar 107, OpenAlex 55).
- 461 hits → 332 unique titles → 316 not already in the index or bib → 43 pass a keyword prefilter (continual/incremental/lifelong/forgetting/few-shot AND segmentation in title or abstract; OpenAlex hits have no abstract, so title only). All 23 VoxTell-citing works screened by title regardless of the prefilter.
- Caveat: OpenAlex returns relevance-ranked top 30 per query, so coverage is not exhaustive; the PubMed and arXiv counts are complete for their queries.

### Screening of the 43 + 23 (by Claude, title/abstract; to approve)
Proposed for inclusion:
| Work | Why | Tier |
|---|---|---|
| C^2GR: Coupled Comprehensive Generative Replay for a Continually Learnable Universal Segmentation Model (arXiv 2606.23473, 2026) | task-incremental continual learning of a **universal** medical segmentation model across imaging modalities and targets; closest new hit to the gap claim | C |
| Beyond Forgetting in Continual Medical Image Segmentation: A Comprehensive Benchmark Study (arXiv, 2026) | benchmark of CL strategies for medical segmentation; relevant to objective 1 (evaluation protocol) and to the "no strategy dominates" argument | B |
| CLoPA: Continual Low Parameter Adaptation of Interactive Segmentation for Medical Image Annotation (arXiv, 2026) | parameter-efficient continual adaptation of a **promptable** (interactive) medical model | B |
| Self-auditing Parameter-Efficient Fine-Tuning for Few-Shot 3D Medical Image Segmentation (LNCS, 2026; SEA-PEFT) | few-shot PEFT for 3D segmentation, next to Silva-Rodríguez et al. | B |
| Skill-Evolving Grounded Reasoning for Free-Text Promptable 3D Medical Image Segmentation (SEER, arXiv 2603.08215, 2026; cites VoxTell) | not continual, but reports that free-text promptable 3D models are sensitive to prompt phrasing → evidence for defence point D10 (prompt wording) | A |

Considered, not proposed: continual **test-time** adaptation papers (5; unlabelled domain shift at test time, a different problem); few-shot meta-learning / prototype methods (8; the in-context meaning of few-shot is already covered by UniverSeg and the review); natural-image or remote-sensing CL (3); further replay variants for medical segmentation (BBR-Net, generative replay 2025; replay already covered); Classifier-Free Incremental Learning (2024; reserve); Few-Shot Adaptation of Training-Free Foundation Model for 3D (2025; reserve); remaining VoxTell citers (none continual).

Result for the gap claim: no hit adapts a free-text promptable 3D segmentation model continually. Closest: C^2GR (universal model, task-incremental) and, among the works already noted, Liu et al. 2024 (CLIP class-name embeddings, CT, per-class heads).
