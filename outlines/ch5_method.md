# Ch. 5 Method — detailed outline (proposed 2026-10-21, chapter structure approved by the author)

Scope: what we built and why, with symbols, not values (values: Ch. 6 setup). Concepts as published: Ch. 3. Data, splits, prompts, few-shot subsets: Ch. 4 (referenced, not repeated). Notation: `thesis_notes.md` §5. Facts: `thesis_notes.md` §2 "Method fact sheet". Target length about 10–11 pages.

Status markers: ✅ reason from the author exists · ❓ reason still needed from the author · ⚠ defense point (`\todo{defense: …}`)

## Chapter opening (3–4 sentences)
What the chapter covers and in which order: setting → protocol → adapting VoxTell to one task → strategies → complexity. Pointer: values and runs in Ch. 6.

## 5.1 Continual-learning setting (~1 p)
Purpose: the thesis-specific instantiation of the CL problem from Ch. 3.
- Tasks: the six SKM-TEA structures, one fixed text prompt each (refer to `tab:ch4_structures`); a task is a target structure, not a dataset. The six tasks share the same volumes and differ only in the target (Ch. 4 l. 63). ⚠ An examiner may ask whether this is continual learning at all, since the images do not change between tasks: what changes is the prompt-conditioned output. ✅ The images stay the same, but the masks and the text prompt change with every task: new target classes appear.
- Information at inference: the text prompt names the target in every strategy; task identity is given only to task-specific LoRA (task-aware inference). All other strategies use one parameter set for all tasks.
- Task order and few-shot setting as protocol variables (concepts only); concrete orders, k values and their reasons moved to Ch. 6 (`outlines/ch6_experiments.md`), author decision 2026-10-21.
- Few-shot settings: k ∈ {5, 10, 20} and full data, nested first-k subsets, one subset per k (refer to `sec:data-splits`). ✅ about 5 %, 10 %, 20 % of the 108 training volumes. ⚠ one support set per k.
- Control task: AeroPath, text prompt "lung", test split only, never trained on except through replay. ✅ Reason: high pretrained performance on a known concept from an unseen dataset, public; follows SPU's control set (`Zhang_2024_CVPR`).
- Notation introduced: T, t, p_t, 𝒟_t^tr/val/te, k, 𝒟_c^te, p_c.

## 5.2 Evaluation protocol (~1.5 p, Alg. 1) — objective 1
Purpose: how the evaluation matrix and the control row are produced. Definitions of matrix and metrics: Ch. 3. Choice of metrics and why they fit: Ch. 6 setup.
- Stages j = 0 … T, where j = 0 is the pretrained model θ_0. After every stage: evaluate on the test sets of all T tasks (including tasks not trained yet) and on the control task → column j of a_{i,j} and c_j.
- Each entry = mean DSC over the same test volumes (24 SKM-TEA, 4 AeroPath); identical test set in every run and cell.
- Which parameters are evaluated per strategy at stage j (task-specific LoRA: adapter of task i for i ≤ j, current adapter for i > j, no adapter for the control task; all other strategies: one parameter set). Consequence stated as a fact: forgetting ≈ 0 and control-task drop = 0 for task-specific LoRA by construction.
- Pretrained reference row: the same metrics for the never-updated model, one per task order.
- What the protocol does not contain: no joint-training (multi-task) reference, so no intransigence measure. ✅ compute (budget spent on other configurations). ⚠
- **Alg. 1 — Continual adaptation and evaluation protocol.** Input: θ_0, task sequence, strategy, test sets. Loop over t: ADAPT (Alg. 2) → θ_t; loop over i and the control task: EVALUATE → a_{i,t}, c_t. Output: evaluation matrix and control row.
- Complexity of Alg. 1: T adaptation stages; (T+1)·(T+1) evaluation cells, each over |𝒟^te| volumes with sliding-window inference (cost per volume ∝ number of tiles). Measured time: Ch. 6.

## 5.3 Adapting VoxTell to one task (~2 p, Alg. 2, Fig. 5.1)
Purpose: the pipeline shared by all strategies; each strategy in 5.4 is defined by what it changes in it.
- Model as used (architecture itself in Ch. 3): each prompt-decoder layer is pre-norm cross-attention + FFN only (`forward_pre`; the self-attention module is unused, 100.7 M parameters never updated; `thesis_notes.md` §2); checkpoint v1.1; text encoder frozen in all strategies; prompt decoder (L_dec layers, dimension d) reads its keys/values from encoder stage 4, not the bottleneck (code fact, differs from the paper's description).
- **Fig. 5.1** (own drawing, `figures/ch5_voxtell_strategies.pdf`): VoxTell block diagram (same as the Ch. 3 figure) with the parts each strategy trains marked: all weights (sequential fine-tuning, distillation-based), LoRA in cross-attention q/v, prompt tokens + meta-net in the first L_p decoder layers, the stage-4 features used by the distillation loss. **Built 2026-10-21:** `thesis/figures/tikz/voxtell.tex` with `\voxannotatetrue`.
- Training samples: one 192³ patch per training volume per epoch, centred on a random foreground voxel with probability π_fg, otherwise uniformly placed; batch size 1; one text prompt per sample.
  - No negative prompts, 10 epochs, batch size 1: ✅ time and compute (quantify in Ch. 6: 18–24 h per full-data run, 24 h job limit).
  - No data augmentation: ✅ for simplicity; identical for all strategies. ⚠ may lower absolute performance, most in the few-shot settings.
  - Deep supervision: ✅ not used (no claimed benefit).
- Loss: ℒ_seg = ℒ_BCE + ℒ_Dice (equation, weights 1:1). Reason: the same loss as VoxTell's pretraining (`paper_notes/voxtell.md` §3), there with deep supervision.
- Optimisation (form only): SGD with Nesterov momentum μ and weight decay ω; LR η_0 with polynomial decay over the U = E·N_t iterations of the task, updated every iteration; new optimiser and schedule for every task. Reason: follows VoxTell's pretraining (SGD, η_0, polynomial decay; `paper_notes/voxtell.md` §5). Values: Ch. 6 table.
- Validation and checkpoint (state exactly, ⚠ F3/F4):
  - after every epoch, validation loss on 𝒟_t^val, one random patch per volume, re-drawn every epoch;
  - sequential fine-tuning, distillation-based, prompt tuning: evaluated checkpoint = lowest validation loss; LoRA strategies: last epoch;
  - every strategy continues to the next task from the last-epoch state.
  - ✅ not a deliberate choice, stated as such; last-epoch evaluation named as the consistent CL rule (evaluated model = model carried forward), the three best-validation strategies as deviating from it; quantified in Ch. 6. Quantification (selected epochs): Ch. 6 setup.
- Inference: sliding window with patch size 192³, 50 % overlap, Gaussian weighting, sigmoid, threshold 0.5, no test-time augmentation. ❓ (Claude to verify) whether DSC is computed on the cropped volume and that the crop never removes labelled voxels.
- **Alg. 2 — Adapting to one task.** Input: current θ, task t, strategy hooks. Steps: INIT(t) → φ; for each epoch: shuffle 𝒟_t^tr ∪ EXTRA_DATA(t); for each sample: sample patch, forward, ℒ = ℒ_seg + EXTRA_LOSS, update φ, LR step; validate; keep best checkpoint. AFTER_TASK(t). The four hooks are written in a distinct font and filled per strategy in Table 5.1.
- Complexity of Alg. 2: per iteration one forward + backward pass through the parts of the network on the gradient path; per task U iterations; memory = parameters + optimiser state (one momentum buffer per trained parameter) + activations of one 192³ patch.

## 5.4 Continual-learning strategies (~4.5 p)
Opening: **Table 5.1 — strategy overview**: rows = strategies, columns = trained parameters φ / INIT / EXTRA_LOSS / EXTRA_DATA / AFTER_TASK / parameters used at inference. Selection rationale (✅ author): one strategy per major family — parameter isolation, shared parameter-efficient adaptation, rehearsal, distillation-based regularisation, prompt-based; alternatives (EWC, LwF, …) not evaluated ⚠ (limitation, future work). Check the families against the taxonomy cited in Ch. 2/3 (`delange2022`).

Each subsection: mechanism → hooks → trainable parameters (formula and count) → what differs from the original method → reasons → complexity.

### 5.4.1 Sequential fine-tuning (~0.3 p)
- All parameters trained on each task in turn, no CL mechanism; the baseline. Not a "lower bound" (highest Adaptation, CLAUDE.md).
- φ = θ (440,029,541 parameters of the segmentation model; text encoder frozen).

### 5.4.2 Task-specific and shared LoRA (~1.2 p)
- Common part: ΔW = γ_r·\mat{B}\mat{A} added to the query and value projections of the cross-attention in all L_dec prompt-decoder layers; \mat{A} Kaiming-uniform, \mat{B} zero, so training starts from f_{θ_0}; dropout on the LoRA input path; all other weights frozen.
  - ✅ placement: cross-attention is where the text query attends to the image features, VoxTell's core mechanism; LoRA on attention as in CLIP-LoRA (`zanella2024lowrankfewshotadaptationvisionlanguage`); q/v as in Hu et al. (`hu2022lora`) — check what Hu et al. report before citing. Do not cite the multi-stage fusion as a reason (LoRA does not touch it).
  - ✅ γ_r = α/√r (rsLoRA, `kalajdzievski2023rankstabilizationscalingfactor`): allows high ranks for the shared adapter; α fixed across ranks.
  - Trainable parameters: 2 projections × L_dec layers × 2rd = 4·L_dec·r·d = 49,152·r.
- Task-specific LoRA: INIT(t) rebuilds the model from θ_0 and creates a new adapter, so adapters are trained independently of each other (no sequential dependency); AFTER_TASK stores the adapter; inference by task identity (5.2). Storage: T adapters.
- Shared LoRA: one adapter created once and trained through all tasks; one parameter set at inference, also for the control task.
- ⚠ The two variants use different α and dropout (no known reason; values in Ch. 6) → comparison is between configurations. ✅ each variant at the rank where it performed better (shared: Final Performance plateaus at r = 1024; task-specific: r = 4 > r = 8). ⚠ chosen on test-split results → state the selection bias; report task-specific r = 8.
- Complexity: compute overhead O(r·d) per token in 2·L_dec projections, negligible against the image network; gradients still flow through the UNet decoder up to the prompt decoder; optimiser state only for 49,152·r parameters.

### 5.4.3 Replay (~0.6 p)
- Combined with shared LoRA only. Memory ℳ: initialised before task 1 with round(ρ·|𝒟_c^tr|) control-task training volumes; after task t, round(ρ·N_t) volumes of task t (at least 1) are added; capacity M_max (never reached); EXTRA_DATA(t) = ℳ_{t−1}, each memory volume with its own text prompt, sampled like the task's volumes.
- ✅ ρ = a single value, not tuned. ✅ stand-in for VoxTell's unavailable pretraining data (ZSCL names the same problem for CLIP); memory = knowledge from before task 1 + SKM-TEA tasks. ⚠ the control task is then trained on, so its control-task drop is not comparable with the other strategies. ⚠ initial sampling not seeded (memory content changed after a job resume).
- Complexity: N_t grows to |𝒟_t^tr| + |ℳ_{t−1}|; memory stores volume references only.

### 5.4.4 Distillation-based strategy, adapted from ZSCL (~1.2 p)
- ZSCL in one paragraph (details Ch. 3): distillation from the initial model on a reference dataset + weight ensemble (+ weight consolidation in the full method) (`paper_notes/zscl.md` §3–4).
- Ours: φ = θ; teacher f_{θ_0} frozen; EXTRA_LOSS = λ·ℒ_KD on the current task's batch: for each of the G guidance channels, distribution over the stage-4 voxels of the dot product between the L2-normalised guidance vector and the stage-4 **encoder** features; ℒ_KD = KL(teacher ‖ student) (equation).
- Kept from ZSCL: initial model as teacher; distillation of a similarity distribution between the text-derived and image representations.
- Changed: current-task data instead of a reference dataset (ZSCL's own ablation "current", Table 1b); distribution over voxels instead of over texts; one direction only; no weight-consolidation term; λ differs from the paper's; segmentation loss and SGD.
- Weight ensemble (Eq. 7 of ZSCL) implemented but not part of the evaluated models (F1): state it plainly; the strategy is named after what was evaluated.
- ✅ current-task data: no reference dataset needed beyond the task data (ZSCL's own "current" ablation, Table 1b); stage 4: where text and image interact in the prompt decoder, coarse 12³ level, cheapest; λ = 0.01 not tuned (ZSCL: λ = 1).
- Complexity: one extra teacher forward pass per iteration (no backward); teacher held on the CPU and moved to the GPU each iteration (time, measured in Ch. 6); memory: an extra copy of θ (teacher, CPU) and of the ensemble (GPU).

### 5.4.5 Prompt-tuning strategy, adapted from CPE-CLIP (~1.2 p)
- CPE-CLIP in one paragraph (details Ch. 3): frozen CLIP, layer-wise prompts in language and vision encoder coupled by a projection, gradient scaling per session (`paper_notes/cpe_clip.md` §2).
- Ours: all VoxTell parameters frozen; φ = {\mat{V}_l (m tokens, first L_p decoder layers), ψ}. Tokens appended to the cross-attention memory of layer l ("replacement": fresh tokens per layer, zero positional encoding); meta-net h_ψ adds an offset to the text query from [query; mean of the image memory] in the same layers.
- Trainable parameters: L_p·m·d + meta-net (12,599,296; the meta-net holds 12,587,008 of them) — state this, the name "prompt tuning" understates it.
- Kept: frozen backbone; layer-wise learned tokens up to a depth; replacement mode; per-task gradient scale on the tokens.
- Changed: tokens in the prompt decoder's image memory, not in the text and vision encoders; no projection between token sets; added meta-net; depth L_p of L_dec; scale β_t = max(0.25, 1/t) on the tokens only (equals CPE-CLIP's formula for one new structure per task, except the floor) — implemented but inactive in the evaluated run (β_t = 1, F2). CPE-CLIP's own ablation names this regularisation as its most important component, so the evaluated strategy lacks it (cite `paper_notes/cpe_clip.md` §5).
- ✅ meta-net inspired by CoCoOp (add bib entry); m = 2 and L_p = 3 not tuned (m = 2 happens to equal CPE-CLIP's best L = 2).
- Complexity: forward through the whole frozen network; backward through the UNet decoder and prompt decoder only; tokens add m keys/values to L_p cross-attentions; optimiser state for 12.6 M parameters.

## 5.5 Complexity summary (~0.7 p, Table 5.2)
- **Table 5.2**: per strategy — trainable parameters (formula), extra compute per iteration, extra memory during training, stored parameters after T tasks, inference cost (all: one forward per tile; task-specific LoRA: adapter swap).
- One paragraph comparing them; pointer to the measured runtime and memory on the A100 in Ch. 6 (`tab:ch6_compute`), as the chair requires measured values for each algorithm.

## Not in Ch. 5 (where it goes instead)
- VoxTell architecture as published, CL metrics, LoRA/rsLoRA, distillation, prompt tuning, replay, Dice → Ch. 3.
- Hyperparameter values, configurations per experiment, hardware, selected-epoch counts, bootstrap, measured runtime/memory, metric choice and why it fits → Ch. 6 setup.
- Interpretation of results (e.g. why prompt tuning loses control-task performance despite frozen weights) → Ch. 6/7.

## Open items before drafting
- ✅ all author answers received 2026-10-21 (see `thesis_notes.md` §1). Open: report task-specific LoRA r = 8 (author to confirm); CoCoOp bib entry (author).
- Claude: verify the DSC computation on cropped volumes; check `delange2022` taxonomy terms; ZSCL bib entry → ICCV 2023 version (author to take fields from the publisher page).
