# SPU (Zhang et al., CVPR 2024) — paper notes

Partial notes: problem setting and evaluation metrics. Sections 1–2 are what the **paper** says; section 3 is **analysis for this thesis**.

| | |
|---|---|
| Paper | Zhang, Janson, Aljundi, Elhoseiny. *Overcoming Generic Knowledge Loss with Selective Parameter Update.* CVPR 2024 |
| Local PDF | `voxtell_paper/spu.pdf` = arXiv:2308.12462v4 (19 Apr 2024), 17 pages; cite by **section/equation** |
| Bib key | `Zhang_2024_CVPR` (bib has `month = {June}`, biber warns: not an integer) |
| Notes written | 2026-10-22 |

## 1. Problem (abstract, Sec. 1, Sec. 3)
- Updating a foundation model on new data risks losing its "generic knowledge" acquired in pre-training (Sec. 1).
- Knowledge base formulated "as the zero-shot classification ability on a diverse control set containing a wide range of classes"; goal: improve on datasets where the pretrained model is weak "while preserving its original ability on a control set, without revisiting it" (Sec. 1).
- Setting (Sec. 3): class-incremental sequence of tasks; evaluation on the test sets of the sequence "and a small control set D_control ⊂ D_p sampled from the pre-training distribution".
- Method (Sec. 4, not used here): localise updates to the first MLP layer of transformer blocks and update a sparse set of task-relevant parameters (Fig. 1).

## 2. Evaluation (Sec. 5.1 "Evaluation Metrics", Eqs. 4–6)
- Control set = ImageNet validation set; report zero-shot accuracy on it "and compare it with that from the frozen pre-trained models".
- Over N_D datasets/sequences, M_i = model after training on D_i, M_f = frozen model:
  - Acc. In. = (1/N_D) Σ_i [Acc.(M_i) − Acc.(M_{f_i})] (Eq. 4)
  - Avg. F = (1/N_D) Σ_i F.(M_i) (Eq. 5)
  - **C. Drop = (1/N_D) Σ_i [C.(M_f) − C.(M_i)]** (Eq. 6): control-set accuracy of the frozen model minus that of the trained model.
- Headline: SPU control-set drop 0.94 % (Sec. 5.2); abstract says 0.9 %.

## 3. Analysis for this thesis (NOT from the paper)
- Control-task drop = c_0 − c_T follows Eq. 6 for one sequence (N_D = 1), with the final checkpoint as M_i, DSC instead of accuracy.
- Similarity (updated 2026-11-13, after the decision of 2026-11-07): SPU's control set is sampled from the pre-training distribution; the thesis's control task (AeroPath lung) is likewise from VoxTell's training data, since AeroPath is among the training sources of checkpoint v1.1 (GitHub issue #15; it was held out only in the paper, v1.0). Ch. 5 (method.tex, Sec. 5.1) states this parallel. Earlier version of this line said AeroPath was not trained on; that was true only for v1.0.
