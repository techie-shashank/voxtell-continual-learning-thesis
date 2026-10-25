# ZSCL — paper notes

Notes on the paper that the distillation-based strategy is adapted from. Read once, so the PDF does not have to be re-read.
Sections 1–7 are what the **paper** says, with locations; section 8 is **analysis for this thesis** (not from the paper).

| | |
|---|---|
| Paper | Zheng, Ma, Wang, Qin, Yue, You. *Preventing Zero-Shot Transfer Degradation in Continual Learning of Vision-Language Models.* arXiv:2303.06628v2 [cs.CV], 11 Aug 2023. 15 PDF pages (8 main + references + appendix) |
| Local PDF | `voxtell_paper/zscl.pdf` |
| Bib key | `zheng2023preventingzeroshottransferdegradation` (`@misc`, arXiv). **Published at ICCV 2023** (not stated in the arXiv PDF; the author must take the proceedings fields from the publisher page before the bib entry is changed) |
| Code | github.com/Thunderbeee/ZSCL (abstract, p. 1) |
| Notes written | 2026-10-21, from arXiv v2. Page numbers = PDF pages |

## 1. Problem and idea (abstract, Sec. 1, p. 1–2)
- Continual training of CLIP degrades its **zero-shot transfer ability** (performance on tasks/data not yet trained), in addition to the usual forgetting of learned tasks (p. 1–2, Fig. 1).
- Replay methods cannot access CLIP's private pre-training data; distillation-based CL methods "do not lay enough emphasis on the pre-trained model" (p. 2).
- ZSCL protects zero-shot transfer **in feature space** (distillation from the initial CLIP on a reference dataset) and **in parameter space** (weight ensemble during training) (p. 2).
- Contributions (p. 2): the problem study plus the MTIL benchmark; the ZSCL method; outperforms SOTA (e.g. +9.7 % Avg. and +10.9 % Transfer on MTIL, p. 2).

## 2. Setting (Sec. 3.1, p. 3)
- n tasks T^i = (D^i, C^i) trained in sequence; task-incremental (task identity t given at inference) and class-incremental (not given) settings.
- CLIP classification: class names → template "a photo of {c}" → text embeddings; cosine similarity s between image and text embeddings; fine-tuning with cross-entropy on τ-scaled similarities (Eq. 1).

## 3. Distillation in feature space (Sec. 3.2, p. 4)
- Similarity distribution of one image over m texts: p = Softmax(s_1, …, s_m) (Eq. 2).
- Image-side distillation: L_dist_img = CE(p, p̄) = −Σ_j p_j log p̄_j, p̄ from the teacher (Eq. 3). Text-side analogue L_dist_txt: distances from a text to a batch of images (p. 4).
- Total loss: L = L_ce + λ·(L_lwf_img + L_lwf_txt) (Eq. 4).
- Three design components studied (p. 4): **data source**, **teacher model**, **loss design**.
  - Data source: LwF uses current-task data, iCaRL selected previous data; ZSCL introduces a **reference dataset** — publicly available images with enough semantics, no labels, need not be seen in pre-training or paired with texts; texts can be class names, unrelated sentences or random tokens (p. 4).
  - Teacher: the **pre-trained (initial) model**, not the model after task i−1 (p. 4).
- Ablations, Table 1 (p. 6), MTIL Order I, metrics Transfer / Avg. / Last:
  - (a) loss: CE only 44.6 / 55.9 / 77.3; feature distance 47.6 / 58.7 / 77.1; image-only 56.5 / 68.9 / 82.1; text-only 56.7 / 69.0 / 82.6; both 56.8 / 69.2 / 83.0.
  - (b) image source: **current task 56.7 / 66.5 / 80.2**; ImageNet 56.8 / 69.2 / 83.0; CC 57.2 / 68.5 / 80.9; CIFAR100 55.2 / 65.9 / 80.7; Flowers 54.7 / 66.0 / 80.8. Text p. 7: current-task images give "a good Transfer score" but hinder learning new tasks (low Avg. and Last).
  - (d) teacher: initial 56.8 / 69.2 / 83.0; n−1 53.9 / 66.6 / 80.7; WiSE(0.5) 56.4 / 68.9 / 82.9; WiSE(0.8) 56.2 / 67.8 / 81.3.
  - Default (gray in Table 1): image + text distillation, initial CLIP, 100k ImageNet images, texts from ImageNet classes with a simple template.

## 4. Weight ensemble in parameter space (Sec. 3.3, p. 5)
- Weight consolidation (WC): L_WC = Σ_i (θ_i − θ̄_i)² (Eq. 5) — "hinders learning new tasks".
- WiSE-FT: f(x; (1−α)θ_0 + αθ_1) (Eq. 6), sensitive to α (Fig. 3).
- **Weight ensemble (WE)**, Eq. 7: θ̂_t = θ_0 for t = 0; θ̂_t = 1/(t+1)·θ_t + t/(t+1)·θ̂_{t−1} every I iterations. Related to SWA but without a modified LR schedule; aim: a better learning–forgetting trade-off; "much more robust" to I than WiSE-FT to α (p. 5).
- Table 2 (p. 6), components, MTIL Order I (Transfer / Avg. / Last): zero-shot 69.4 / 65.3 / 65.3; continual learning (sequential FT) 44.6 / 55.9 / 77.3; **+ distillation 58.9 / 70.5 / 83.8**; + WiSE-FT 61.7 / 71.6 / 83.3; + WE (= ZSCL*) 62.2 / 72.6 / 84.5; + WC 67.6 / 74.5 / 83.2; + WC + WiSE-FT 67.7 / 74.2 / 81.9; **+ WC + WE (= ZSCL) 68.1 / 75.4 / 83.6**.
- So the **full ZSCL = distillation + WC + WE**; ZSCL* = without WC (p. 6, p. 8 "ZSCL*, a variant without the WC loss"). Eq. 4 alone does not show the WC term.

## 5. Benchmark and metrics (Sec. 4, p. 5–6; Fig. 4)
- MTIL: 11 datasets from different domains (Aircraft, Caltech101, CIFAR100, DTD, EuroSAT, Flowers, Food, MNIST, OxfordPet, StanfordCars, SUN397), 1,201 classes; Order I (alphabetical) and Order II (random) (p. 6; Table 8 p. 13).
- Metrics (p. 6, Fig. 4b), on the task × training-step matrix: **Transfer** = average over the upper-right triangle (tasks not yet trained); **Avg.** = average over all timestamps; **Last** = average after the last task. Each task first averaged so every dataset has equal weight.
- Also class-incremental CIFAR100 / TinyImageNet / ImageNet100 (Tables 6, 7, 9).

## 6. Implementation (Sec. 5 p. 6; App. B p. 13)
- CLIP ViT-B/16; AdamW; label smoothing; 1K iterations per task (MTIL).
- Batch 64 (MTIL), 128 (class-incremental); LR searched in {1e-5, 1e-6, 1e-7}; weight decay 0, label smoothing 0.2 (MTIL, CIFAR100, TinyImageNet).
- **I ∈ {1, 10, 100}: "slight changes", fixed to 100. "A large λ hinders learning new knowledge, and λ = 1 is a good choice"** (App. B, p. 13).
- Reference set: 100k random ImageNet images, texts from the Conceptual Captions dataset (p. 7).

## 7. Results and limitations
- MTIL Order I (Table 3, p. 7): ZSCL 68.1 / 75.4 / 83.6 vs sequential FT 44.6 / 55.9 / 77.3, LwF 56.9 / 64.7 / 74.6, WiSE-FT 52.3 / 60.7 / 77.7. Order II (Table 4): ZSCL 64.2 / 74.5 / 83.4.
- Fig. 5 (p. 7): t-SNE, ZSCL keeps the feature distribution closest to the original CLIP.
- Limitation (Sec. 6, p. 9): **a reference dataset is needed**; future work: synthetic reference data.

## 8. Analysis for this thesis (NOT from the paper; verify before using)
1. **What the thesis's distillation-based strategy keeps from ZSCL:** teacher = the initial (pretrained) model (as Sec. 3.2 / Table 1d); a distillation loss on a similarity distribution added to the task loss with weight λ (Eq. 4).
2. **What differs** (from `code/src/continual/strategies/zscl/strategy.py`, `thesis_notes.md` §2):
   - Data source = **current-task batches**, no reference dataset. This corresponds to ZSCL's own ablation row "current" (Table 1b), which the authors report as worse for Avg./Last than a reference set.
   - Distribution = softmax **over voxels** of the dot product between the stage-4 text-guidance vector and the stage-4 image features (one "text" vs many spatial positions), not over texts for one image (Eq. 2). Only one direction; no text-side term.
   - Code uses KL(p_teacher ‖ p_student). Eq. 3 as printed is −Σ_j p_j log p̄_j (student probabilities weighting the teacher's log-probabilities), which is not the same expression. KL(teacher ‖ student) equals the cross-entropy H(p̄, p) minus the teacher's entropy, so it has the same gradient as the usual distillation cross-entropy. Don't claim it is identical to Eq. 3 as printed.
   - λ = 0.01 vs the paper's λ = 1.
   - **No WC term** (the full ZSCL has one, Table 2).
   - **Weight ensemble implemented with Eq. 7 and I = 10 (paper: I = 100), but not evaluated** (F1, `thesis_notes.md` §1); the evaluated model = sequential fine-tuning + distillation, i.e. the "+ Distillation" row of Table 2 in spirit, with current-task data.
   - Segmentation loss (BCE + Dice) instead of CE on similarities; SGD instead of AdamW.
3. The closest published reference point for the evaluated variant is LwF-style distillation on current data but with the initial model as teacher (ZSCL Table 1b "current" + 1d "initial"). `li2017learningforgetting` is in the bib; read LwF before claiming the similarity.
4. The thesis's metrics Average Performance, Final Performance and Transfer are ZSCL's Avg., Last, Transfer (Fig. 4b). Check one difference: ZSCL averages per task first; the thesis's matrix already has one value per task, so this is the same.
