# Ranem et al. (ViT U-Net, continual hippocampus) — fact card (tier B)
| | |
|---|---|
| Paper | A. Ranem, C. González, A. Mukhopadhyay, "Continual Hippocampus Segmentation with Transformers"; 11 pages (8 text + references) |
| Bib key / Local PDF | ranem2022continualhippocampussegmentationtransformers / papers/t5_cl_medseg_networks/ranem2022continualhippocampussegmentationtransformers.pdf |
| Version read | Local PDF carries no arXiv stamp and no venue line; bib entry gives arXiv:2204.08043. Peer-reviewed venue not stated in the PDF |
| Written | 2026-10-22, by Claude |

## Facts (from the paper, each with location: Sec./p./Table/Fig.)
- Task / problem: how forgetting manifests in Transformer-based vs convolutional segmentation networks trained on a sequence of hippocampus datasets, and how CL methods should be applied to them (Abstract; Sec. 1).
- Data (Sec. 3.1, Table 2, p. 4): three T1-weighted MRI hippocampus datasets, labels merged into one "hippocampus" class: HarP 270 cases (216 train, 54 val), Dryad 50 (40/10), DecathHip (Medical Decathlon) 260 (208/52); random 80:20 split. Models are trained 2D slice-by-slice after nnU-Net preprocessing (Sec. 3.3).
- Method (two sentences): ViT U-Net = nnU-Net with a ViT placed between encoder and decoder that takes skip-connection features as input (V1: first skip only; V2: first and last skip), optionally with SPT/LSA (Sec. 2.1, Fig. 1). The study freezes or regularises (EWC) the U-Net or the ViT part and compares rehearsal (25 % of each earlier task), EWC, RWalk, MiB, PLOP and POD on nnU-Net vs ViT U-Net (Sec. 2.2–2.3).
- Setting: no text conditioning; domain-incremental (stated in Sec. 5), fixed order HarP → Dryad → DecathHip, 250 epochs per task (Sec. 3.3); no few-shot.
- Evaluation: Dice ± σ between patients; BWT and FWT (Eq. 1–2) (Sec. 3.3, 4.1). Hardware: Tesla T4 GPUs (Sec. 3.2).
- Best result: chosen backbone ViT U-Net V2 + SPT (Table 4: HarP 4.82, Dryad 16.19, DecathHip 89.69 Dice after sequential training without CL). Table 5 (BWT %, HarP / Dryad): Sequential nnU-Net −83.47 / −85.09 vs Sequential ViT −81.03 / −74.94; EWC nnU-Net −2.22 / −2.87 vs EWC ViT −1.76 / −3.95; Rehearsal nnU-Net −0.23 / −0.54 vs ViT −0.31 / −0.59. Rehearsal is the stated upper bound; EWC is close in BWT/FWT but about 10 % worse Dice on the last task than rehearsal (Sec. 4.5). Regularising only the ViT with EWC lowers retained knowledge (Sec. 4.4, Fig. 6d).
- Limitations stated by the authors: only domain-incremental learning and one anatomy (Sec. 5); the paper itself notes that the ViT U-Net reduces forgetting "only in some cases" with CL methods (Sec. 4.5); larger resource use than nnU-Net (Sec. 5).

## Check of the author's notes
- related_work.tex:81 "Ranem et al. observed that a Vision Transformer U-Net retained knowledge across sequential hippocampus segmentation tasks more effectively than its convolutional counterpart" → partly correct. True for plain sequential training (Table 5; Fig. 5a–b), but with CL methods the paper says the ViT U-Net lowers forgetting only in some cases (Sec. 4.5; e.g. Dryad BWT with EWC −3.95 ViT vs −2.87 nnU-Net). Also the models are 2D slice-wise, and BWT values near −80 % for both mean the gain is small in absolute terms.
- related_work.tex:81 "and that regularising the attention components directly interfered with the learned representations" → partly correct: the paper concludes that EWC on the ViT part interferes with the self-attention mechanism and lowers retained knowledge (Sec. 4.4, Fig. 6d; Sec. 6). "Learned representations" is the author's rewording; the paper speaks of the self-attention mechanism and maintained knowledge.
- related_work.tex:81 (context sentence) "The ranking is further sensitive to the architecture" → supported in spirit (Table 5 shows method results differ between backbones), but the paper does not state a ranking change explicitly.
- related_work.tex:200 (table) "Hippocampus | ViT U-Net compared with CNN | ViT retains more" → partly correct, same caveat as above (only clear without CL method).
- introduction.tex:27 cited among "Early work ... has largely considered task-specific or relatively compact models" → correct as a characterisation (nnU-Net-based task-specific models, Sec. 2.1).

## Relevance (NOT from the paper)
Shows that forgetting behaviour and the effect of regularisation depend on which architectural component (attention vs convolution) is constrained, which matters when choosing where to place adapters or penalties in a Transformer-based promptable model.
