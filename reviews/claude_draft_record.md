# Record of Claude-drafted paragraphs (2026-11-12)

Saved before the `% CLAUDE-DRAFT` markers were removed at the author's request (2026-11-12).
Each entry: file, line of the marker in the version before removal, and the first words of the paragraph that followed it.
These paragraphs were drafted by Claude (outline, draft, voice pass in the author's style; see ai_use_log.md) and approved by the author.
Total: 243 markers.

## thesis/appendix.tex (19 markers)

- l. 10: This appendix complements \cref{chap:experiments}.
- l. 19: This section belongs to \cref{sec:data-splits,subsec:exp-data}.
- l. 26: \caption[Few-shot training volumes and test volumes]{Few-shot training volumes and test volumes, named as in t
- l. 36: This section belongs to \cref{subsec:exp-config}.
- l. 41: The runs used PyTorch 2.8.0 with CUDA 12.6 and cuDNN 9.10.2, MONAI 1.5.2, nnU-Net 2.7.0, Transformers 4.57.6, 
- l. 47: Runs that reached the 24-hour limit of a job were continued from their last checkpoint.
- l. 57: \caption[Training and evaluation settings shared by all runs]{Training and evaluation settings shared by all r
- l. 65: \caption[Parameters of the strategies]{Parameters of the strategies (\cref{sec:method-strategies}). Sequential
- l. 75: This section belongs to \cref{sec:exp-main}.
- l. 82: \caption[Additional evaluations]{Additional evaluations (full training split, original task order, one run eac
- l. 94: This section belongs to \cref{sec:exp-main}.
- l. 101: The weight ensemble follows \cref{eq:bg-we} and is updated every $I_{\mathrm{we}}$ training updates, counted a
- l. 111: The weight ensemble of the distillation-based strategy reached half the Adaptation of the student, 0.376 again
- l. 121: The per-task gradient scaling of the prompt-tuning strategy lowered its forgetting at a small cost in Adaptati
- l. 130: Both components differ from their published form.
- l. 140: This section belongs to \cref{chap:experiments}.
- l. 162: This section belongs to \cref{sec:exp-task-order}.
- l. 167: With $r = 1024$, the loss of the first task started at about 1.0, its value for an empty prediction, and fell 
- l. 176: \caption[Training loss of the first two tasks of shared LoRA]{Training loss $\mathcal{L}_{\mathrm{seg}}$ of sh

## thesis/background.tex (33 markers)

- l. 14: This chapter introduces the concepts on which \cref{chap:method} builds.
- l. 24: We consider the segmentation of one target structure in a 3D image volume.
- l. 33: VoxTell implements $f_\theta$ with a volumetric encoder--decoder network and attention between the text prompt
- l. 39: The 3D U-Net~\cite{3d_unet} is an encoder--decoder network for volumetric segmentation.
- l. 46: A whole volume and its intermediate features often do not fit into the memory of a GPU, so volumetric segmenta
- l. 54: Attention lets each of a set of query vectors collect information from a set of source vectors, weighting each
- l. 72: In self-attention, the query vectors and the source vectors are the same ($\mat{S} = \mat{U}$).
- l. 78: A transformer decoder layer combines attention blocks with a feed-forward network, two linear layers with a no
- l. 86: VoxTell is a vision--language model that maps a 3D volume and a free-text prompt to a segmentation mask of the
- l. 95: \caption[Architecture of VoxTell]{Architecture of VoxTell (adapted from~\cite[Fig.~2]{rokuss2025voxtellfreetex
- l. 106: VoxTell is built on the nnU-Net framework~\cite[Suppl.~Sec.~A]{rokuss2025voxtellfreetextpromptableuniversal}, 
- l. 115: The prompt decoder consists of $L_{\mathrm{dec}} = 6$ transformer decoder layers of the kind described in \cre
- l. 122: The decoder upsamples the features stage by stage and fuses the guidance into every stage~\cite[Eqs.~4--6]{rok
- l. 135: VoxTell was trained with a combination of the binary cross-entropy and the Dice loss~\cite[Sec.~3, Eq.~7, Supp
- l. 153: This section states the continual-learning problem in the notation of this thesis and defines three common con
- l. 162: In continual learning, a model is trained on a sequence of tasks $t = 1, \dots, T$, one after the other.
- l. 168: Van de Ven et al.\ distinguish three continual-learning scenarios by whether the task identity of an input is 
- l. 177: \Gls{lora} keeps a pretrained weight matrix $\mat{W}_0 \in \mathbb{R}^{d_{\mathrm{out}} \times d_{\mathrm{in}}
- l. 190: In the original formulation, the scaling factor is $\alpha / r$ with a constant hyperparameter~$\alpha$~\cite[
- l. 204: In knowledge distillation, a student model is trained to reproduce the output distribution of a teacher model,
- l. 210: ZSCL changes two choices of LwF to preserve CLIP's zero-shot transfer during continual learning~\cite[Sec.~3.2
- l. 227: Prompt learning adapts a frozen vision--language model by training a few input vectors instead of its weights.
- l. 233: CPE-CLIP applies prompt learning to few-shot class-incremental learning~\cite[Secs.~1 and~3]{D_Alessandro_2023
- l. 251: This section defines the segmentation metric and the continual-learning metrics computed from it.
- l. 254: The overlap between a binary prediction $\hat{\mat{Y}}$ and the label mask $\mat{Y}$ is measured with the \gls
- l. 265: Evaluating the model on every task after every stage shows how training on later tasks affects earlier ones~\c
- l. 280: \caption[Entries of the evaluation matrix used by each metric]{Entries of the evaluation matrix used by each m
- l. 289: We summarise the evaluation matrix with four metrics, three taken from the literature and one derived from it,
- l. 294: Adaptation measures how well each task is learned when it is trained,
- l. 304: Final Forgetting is the average forgetting of Chaudhry et al.\ after the last task~\cite[Sec.~3, Eq.~3]{Chaudh
- l. 315: The control-task drop follows SPU, which uses a control set to measure how much of a pretrained model's genera
- l. 326: Final Performance is the metric Last of ZSCL, the mean performance on all tasks after the last stage~\cite[Sec
- l. 336: Transfer is the metric of the same name in ZSCL~\cite[Sec.~4, Fig.~4b]{zheng2023preventingzeroshottransferdegr

## thesis/data_description.tex (11 markers)

- l. 14: This chapter describes the two public datasets used in this thesis.
- l. 31: The Stanford Knee MRI with Multi-Task Evaluation (SKM-TEA) dataset contains knee \gls{mri} scans of 155 patien
- l. 37: All scans were acquired with the 3D \gls{qdess} sequence on one of two 3\,T GE MR750 scanners, with patient co
- l. 46: Four tissues were segmented manually on all \gls{dicom} images, labelled as six structures: patellar cartilage
- l. 55: Each of the six segmented structures defines one task.
- l. 77: AeroPath contains 27 contrast-enhanced chest \gls{ct} scans (\gls{cta}) of patients undergoing diagnostic test
- l. 92: We split each dataset once, at random.
- l. 102: SKM-TEA also defines an official split of 86 training, 33 validation, and 36 test scans, whose test set consis
- l. 108: For the few-shot settings, we reduce the training split to its first $k$ volumes in the order of the shuffled 
- l. 120: We convert each SKM-TEA \gls{hdf5} file into two \gls{nifti} files, one for the first echo and one for the lab
- l. 129: When a volume is loaded, it is reoriented according to its affine and cropped to the bounding box of its non-z

## thesis/experiment_results.tex (69 markers)

- l. 14: This chapter reports the experiments with which we answer the research question.
- l. 24: \Cref{tab:ch6_experiments} lists the experiments and the objective of \cref{sec:intro-rq} that each addresses.
- l. 36: In the original task order, the structures are trained in the sequence lateral tibial cartilage, medial tibial
- l. 45: \caption[Overview of the experiments]{Overview of the experiments. Training volumes per task: 108 is the full 
- l. 51: With $k = 5$, 10, or 20 volumes per task (\cref{sec:data-splits,sec:app-volumes}) and $E = 10$ epochs, a task 
- l. 61: \Cref{sec:app-params} lists the settings that all runs share and the parameters of each strategy.
- l. 67: Each run was trained on one NVIDIA A100 GPU with 40\,GB of memory on a cluster where a job may run for at most
- l. 73: For the comparison of the strategies, we used rank $r = 4$ for task-specific LoRA and $r = 1024$ for shared Lo
- l. 82: We report the five metrics of \cref{sec:bg-metrics}.
- l. 89: For task-specific LoRA, the control-task drop is zero and Final Forgetting is near zero by construction (\cref
- l. 96: Each configuration was trained once, so we cannot estimate how results vary with the training randomness or wi
- l. 107: All runs are evaluated on the same test volumes, so the results of two runs are correlated, and overlapping in
- l. 125: In the comparison of the strategies, we ask how the six strategies trade adaptation against forgetting when ea
- l. 131: \caption[Results of the comparison of the strategies]{Results of the comparison of the strategies (full traini
- l. 140: \caption[Metrics of the strategies]{Metrics of the strategies of \cref{tab:ch6_main} (full training split, ori
- l. 145: In the primary metrics, the strategies formed two groups (\cref{tab:ch6_main,fig:ch6_main_metrics}).
- l. 160: Within the first group, the distillation-based strategy forgot slightly less than sequential fine-tuning at th
- l. 171: \caption[Evaluation matrices of the strategies]{Evaluation matrices of the strategies (full training split, or
- l. 176: The last row of each matrix in \cref{fig:ch6_main_matrices} shows when the control task was lost.
- l. 190: After the last task, sequential fine-tuning, the distillation-based strategy, and the prompt-tuning strategy s
- l. 204: Of all strategies, task-specific LoRA reached the highest Final Performance (0.485), because each task keeps i
- l. 214: In Transfer, the LoRA strategies stayed close to the pretrained model (task-specific LoRA: 0.129; shared LoRA:
- l. 219: The distillation-based strategy was less effective in our setting than ZSCL in its own evaluation.
- l. 227: Evaluating the checkpoint with the lowest validation loss instead of the parameters after the last epoch chang
- l. 236: We also evaluated two components adopted from the published methods, the weight ensemble of the distillation-b
- l. 243: No strategy combined the Adaptation of sequential fine-tuning with the retention of the LoRA strategies.
- l. 257: Task-specific LoRA did not learn patellar cartilage in the task sequence.
- l. 273: \caption[Training loss of the patellar diagnosis runs]{Mean training loss per epoch of task-specific LoRA trai
- l. 278: With 10 epochs, every run ended with a \gls{dsc} of 0.000 on the 24 patellar test volumes (95\,\% bootstrap in
- l. 291: Ten epochs were therefore too few for task-specific LoRA to leave the empty prediction on patellar cartilage.
- l. 302: In this experiment, we ask how the amount of labelled data affects adaptation and forgetting.
- l. 310: \caption[Results of the few-shot experiment]{Results of the few-shot experiment (original task order, one run 
- l. 319: \caption[Metrics over the number of training volumes]{Metrics over the number of training volumes per task (lo
- l. 324: Sequential fine-tuning learned every task in all three few-shot settings, and, with ten epochs per task, it fo
- l. 334: With 5 and 10 volumes per task, neither LoRA strategy learned any task, whereas with the full training split t
- l. 344: The equal-updates runs separate the number of volumes from the number of updates at $k = 5$.
- l. 354: Joint fine-tuning reached a Final Performance between 0.585 and 0.753 with 5 to 20 volumes per task, against 0
- l. 361: With ten epochs per task, sequential fine-tuning was the only one of the three strategies that learned the tas
- l. 374: In the LoRA rank experiment, we ask how the rank of the LoRA adapters affects adaptation and forgetting.
- l. 380: \caption[Results of the LoRA rank experiment]{Results of the LoRA rank experiment (full training split, origin
- l. 389: \caption[Metrics of shared LoRA over the rank]{Metrics of shared LoRA over the rank $r$ (logarithmic axis; ful
- l. 394: For shared LoRA, Adaptation, Final Forgetting, the control-task drop, and Final Performance changed monotonica
- l. 403: The evaluation matrices show which tasks drive these trends (\cref{sec:app-matrices}).
- l. 412: In shared LoRA, $\alpha = 32$ is the same for all ranks, so the scaling factor $\gamma_r = \alpha / \sqrt{r}$ 
- l. 416: For task-specific LoRA, $r = 8$ reached a lower Adaptation than $r = 4$ (0.404 against 0.485).
- l. 422: For shared LoRA with fixed $\alpha$, the rank sets a trade-off between adaptation and retention.
- l. 436: In the task-order experiment, we ask whether the results depend on the order in which the structures are learn
- l. 442: \caption[Results of the task-order experiment]{Results of the task-order experiment (full training split, one 
- l. 451: \caption[Metrics in the original and the reverse task order]{Metrics in the original (plain bars) and the reve
- l. 456: For sequential fine-tuning, no effect of the task order can be detected.
- l. 464: For task-specific LoRA, the task order changes neither the data nor the settings of a task.
- l. 477: For shared LoRA, the reverse order led to better retention.
- l. 486: For shared LoRA in the original order, most of the control-task drop and of the forgetting arose in the last s
- l. 496: In both orders, shared LoRA learned the first task poorly.
- l. 504: The training loss of shared LoRA with $r = 1024$ (\cref{sec:app-shared-loss}) fell only slowly from its value 
- l. 507: For sequential fine-tuning, the task order changed only Transfer, by 0.013, and the strategy forgot almost eve
- l. 530: \caption[Measured cost of the strategies]{Measured cost of the strategies in the comparison (full training spl
- l. 536: \Cref{tab:ch6_compute} reports the measured cost of the strategies in the comparison.
- l. 549: Three limitations affect the conclusions most: the hyperparameters shared by all strategies, the single run of
- l. 554: First, all strategies were trained with one set of hyperparameters, and neither the learning rate nor the numb
- l. 563: Within the ten epochs per task used for all strategies, shared LoRA with $r = 1024$ learned little on its firs
- l. 576: Second, each configuration was trained once, on one random split of each dataset and, in the few-shot settings
- l. 584: Third, the scope of the study is narrow.
- l. 597: Our results also cover only the strategies we evaluated, in the form we implemented them.
- l. 603: The evaluation protocol has two further limits.
- l. 612: Three further threats to internal validity come from how the runs were set up and evaluated.
- l. 618: Finally, the data and the checkpoint limit how far our numbers carry over to other evaluations.
- l. 630: The numerical results and the ranking of the strategies apply only to the setting studied here.
- l. 636: The contrast between sequential fine-tuning and task-specific LoRA (\cref{sec:exp-main}) has also been reporte

## thesis/introduction.tex (22 markers)

- l. 16: Medical image segmentation assigns every voxel of an image either to a structure, such as an organ or a tissue
- l. 23: Automatic segmentation with deep learning has commonly meant training one model for each dataset and its targe
- l. 30: Text-promptable models differ in the text they accept.
- l. 37: This thesis adapts VoxTell, which was trained on more than 62{,}000 \gls{ct}, \gls{mri}, and \gls{pet} volumes
- l. 44: Automatic segmentation of the knee cartilages and menisci is useful because quantitative biomarkers for osteoa
- l. 50: With few manual outlines available, VoxTell would have to learn the knee structures from a few labelled volume
- l. 60: Instead of being retrained from scratch, the model can be adapted to one new structure at a time.
- l. 67: The simplest way to learn a task is to fine-tune the model on its data.
- l. 78: \caption[Setting of this thesis]{Setting of this thesis.
- l. 88: With few labelled volumes per task, it is not clear in advance how the balance between stability and plasticit
- l. 95: The continual-learning results we found do not show how few labelled volumes shift the balance between stabili
- l. 101: In our literature search, we found no work that adapts a pretrained free-text promptable 3D segmentation model
- l. 111: This thesis addresses the following research question:
- l. 121: We pursue four objectives:
- l. 134: We study the research question with VoxTell~\cite{rokuss2025voxtellfreetextpromptableuniversal} as the pretrai
- l. 142: We compare sequential fine-tuning, the baseline, with five continual-learning strategies.
- l. 156: All strategies are trained with the full training split.
- l. 161: From the test results, we compute three primary metrics (\cref{sec:bg-metrics}): Adaptation, the \gls{dsc} on 
- l. 167: The study uses one model, one dataset for the tasks, one control task, one fixed text prompt per structure, an
- l. 178: The contributions of this thesis are:
- l. 187: Sequential fine-tuning, LoRA, replay~\cite[Sec.~3.1]{delange2022}, ZSCL, and CPE-CLIP are existing methods, an
- l. 196: \Cref{chap:sota} reviews text-promptable medical image segmentation and few-shot adaptation of segmentation mo

## thesis/method.tex (43 markers)

- l. 14: This chapter describes how we address the research question and the reasons for the main design choices.
- l. 24: We consider a sequence of $T = 6$ tasks built from SKM-TEA.
- l. 30: Each task has one fixed text prompt, which names its target structure during training and at inference, so the
- l. 36: The control task (\cref{sec:bg-metrics}) is the segmentation of the lung in the AeroPath test volumes $\mathca
- l. 45: The protocol trains a strategy on the $T$ tasks in sequence and, after every stage~$j$, evaluates it on the te
- l. 51: Each entry $a_{i,j}$ or $c_j$ is the per-volume \gls{dsc} between the binary prediction and the label mask, av
- l. 60: All entries of all runs use the same test volumes: the 24 SKM-TEA test volumes for the tasks and the 4 AeroPat
- l. 65: \Cref{alg:protocol} summarises the protocol.
- l. 91: The protocol has two variables that are set per run.
- l. 99: As a reference, we apply the same metrics to the pretrained model itself, treating it as if it had been evalua
- l. 104: As an upper reference, we use joint fine-tuning, which trains one model on the training sets of all six tasks 
- l. 118: This section describes VoxTell as we use it and the procedure \textsc{Adapt}, which adapts it to task~$t$ in s
- l. 121: We start every run from version~1.1 of the released VoxTell checkpoint~\cite{rokuss2025voxtellfreetextpromptab
- l. 129: \caption[VoxTell as used in this thesis and the parts changed by the strategies]{VoxTell as used in this thesi
- l. 139: Two properties of the released implementation determine where the strategies of \cref{sec:method-strategies} a
- l. 152: \textsc{Adapt} (\cref{alg:adapt}) starts from the parameters~$\theta_{t-1}$ of the previous stage and trains o
- l. 194: In every epoch, each training volume contributes one patch of $192^3$ voxels.
- l. 201: The loss $\mathcal{L}_{\mathrm{seg}}$ is the unweighted sum of the binary cross-entropy and the soft Dice loss
- l. 208: The trainable parameters are optimised by \gls{sgd} with Nesterov momentum~$\mu$, weight decay~$\omega$, and i
- l. 219: All strategies are evaluated with the parameters after the last epoch.
- l. 231: We compare five continual-learning strategies with sequential fine-tuning, the baseline, which has no mechanis
- l. 242: \Cref{tab:method-strategies} summarises how the six strategies differ in the steps of \cref{alg:adapt}.
- l. 248: Sequential fine-tuning trains all parameters except those of the frozen text encoder on each task in turn, and
- l. 257: Both LoRA strategies keep all pretrained weights frozen and train a low-rank update $\gamma_r\mat{B}\mat{A}$ (
- l. 262: The scaling factor is the rank-stabilised $\gamma_r = \alpha / \sqrt{r}$ of rsLoRA (\cref{eq:bg-rslora})~\cite
- l. 268: We apply LoRA to the query and value projections $\mat{W}_q$ and $\mat{W}_v$ of the cross-attention in all $L_
- l. 275: The two strategies differ in how the adapters are used across tasks.
- l. 285: At stage~$j$ of the protocol, task-specific LoRA evaluates a task $i \le j$ with the adapter trained on task~$
- l. 296: Shared LoRA with replay adds to shared LoRA a memory of training samples from earlier tasks, which are trained
- l. 304: Let $\mathcal{M}_t$ be the memory after task~$t$.
- l. 312: We draw the stored samples at random so that the comparison with shared LoRA shows the effect of replay itself
- l. 320: The prompt-tuning strategy is adapted from CPE-CLIP~\cite{D_Alessandro_2023} (\cref{subsec:bg-prompt}).
- l. 334: The second component is a meta-net $h_\psi$, a two-layer perceptron with a hidden width of 2048, parameters~$\
- l. 346: One set of tokens and one meta-net are trained through all tasks and used for every task at inference, so the 
- l. 360: The distillation-based strategy is adapted from ZSCL~\cite{zheng2023preventingzeroshottransferdegradation} (\c
- l. 366: The loss compares how the stage-4 guidance relates to the stage-4 image features (\cref{fig:ch5_voxtell}).
- l. 387: \caption[Overview of the strategies]{Steps of \cref{alg:adapt} in which the six strategies differ. The column 
- l. 393: The loss is computed on the patches of the current task instead of a reference dataset, so the strategy needs 
- l. 399: The strategy also maintains a weight ensemble following \cref{eq:bg-we}, from which the next task is not train
- l. 409: \Cref{alg:protocol} calls \textsc{Adapt} $T$ times and evaluates $T+1$ stages, each on the $T$ task test sets 
- l. 416: Adapting to task~$t$ takes $E\,N_t$ updates and, with one validation pass after every epoch, $E\,|\mathcal{D}_
- l. 426: In asymptotic terms, every strategy needs $O(E\,N_t)$ forward and backward passes per task, and the distillati
- l. 433: Memory depends mainly on whether the backward pass reaches the image encoder, because only then are the activa

## thesis/related_work.tex (30 markers)

- l. 14: This thesis adapts a pretrained free-text promptable 3D segmentation model to a sequence of new target structu
- l. 23: Promptable segmentation models differ in how the target is selected: either by a spatial prompt marked in the 
- l. 32: Several text-promptable models select their target from a fixed vocabulary.
- l. 43: VoxTell, the model adapted in this thesis, accepts a text prompt that may be a single anatomical term or a ful
- l. 49: The VoxTell authors report robustness to synonyms, rephrasings, and typos~\cite{rokuss2025voxtellfreetextpromp
- l. 58: Each task in this thesis comes with only a few labelled training volumes, so this section reviews how pretrain
- l. 66: Silva-Rodríguez et al.\ fine-tuned a Swin UNETR, pretrained on partially labelled \gls{ct} scans, to one organ
- l. 73: For vision--language models, CLIP-LoRA adds rank-2 LoRA modules to the query, key, and value projections of ev
- l. 84: The works above adapt a model to one target or dataset at a time, each time starting from the same pretrained 
- l. 94: VoxTell combines a frozen text encoder with an image encoder and lets the encoded text prompt attend to the im
- l. 99: Continual-learning scenarios differ in whether the task identity of an input is given at inference~\cite{van_d
- l. 107: The multimodal replay method reviewed here avoids storing real images by generating the replayed data.
- l. 113: ZSCL, a cross-modal regularisation method, showed that continual fine-tuning of CLIP also lowers its zero-shot
- l. 124: PRIMED transfers ZSCL's distillation on reference data to medical 2D image classification with BiomedCLIP~\cit
- l. 131: Parameter-efficient methods freeze most of the pretrained model and train a small set of added parameters~\cit
- l. 144: Other methods train learned prompt tokens, which are vectors added to the input of a frozen model.
- l. 154: The distillation and prompt-learning methods do not carry over directly to VoxTell.
- l. 165: Unlike the methods for vision--language models, which classify images or generate text, the methods reviewed i
- l. 175: Early work on continual learning for medical image segmentation applied regularisation and distillation.
- l. 181: In natural-image segmentation, MiB was the first method to explicitly address background shift, by treating ol
- l. 188: Replay methods for segmentation either store selected parts of earlier data or generate the replayed data.
- l. 196: Parameter-isolation methods keep separate parts of the model for different tasks or structures.
- l. 205: Some studies compare existing methods instead of proposing a new one.
- l. 219: SAM-Med3D-MoE and CA-SAM add task-specific parts to a pretrained \gls{sam}-based model, which is prompted with
- l. 229: Two works adapt pretrained 3D models without spatial prompts.
- l. 242: Three recent works by Gao and colleagues are the closest to this thesis.
- l. 249: MedCRP-CL clusters the tasks by the CLIP embeddings of their text prompts and trains one LoRA module per clust
- l. 265: Text-promptable 3D models such as SAT and VoxTell are trained once on many structures, and VoxTell's zero-shot
- l. 274: In our search\footnote{Keyword queries in OpenAlex, PubMed, and arXiv and a search of the works citing VoxTell
- l. 280: Unlike the closest works, which each propose a new method, this thesis adapts existing methods to VoxTell and 

## thesis/summary.tex (11 markers)

- l. 14: Universal segmentation models such as VoxTell~\cite{rokuss2025voxtellfreetextpromptableuniversal} segment many
- l. 26: We compared sequential fine-tuning, the baseline, with five continual-learning strategies that build on existi
- l. 31: No strategy adapted as well as sequential fine-tuning while retaining as much as the LoRA strategies.
- l. 46: With the full training split and in the original task order, only two of the LoRA strategies kept most of what
- l. 55: With 5 volumes and as many updates as on the full training split, task-specific and shared LoRA reached an Ada
- l. 65: The task order and the rank mainly affected shared LoRA (\cref{sec:exp-task-order,sec:exp-rank}).
- l. 73: The control task showed an effect that Final Forgetting alone would have missed (\cref{sec:exp-rank}).
- l. 80: Several limitations should be considered (\cref{sec:exp-limitations}).
- l. 89: The main extension of this work is a strategy that adapts as well as sequential fine-tuning while retaining as
- l. 97: For shared LoRA with replay, runs in other task orders and at other ranks would show whether its benefit holds
- l. 105: Equal-updates runs with 10 and 20 volumes per task and few-shot runs of the distillation-based and prompt-tuni

## thesis/tables/ch2_positioning.tex (1 markers)

- l. 3: \begin{table}[!tb]  [(table content)]

## thesis/tables/ch2_sota.tex (1 markers)

- l. 4: {\footnotesize  [(table content)]

## thesis/tables/ch5_strategies.tex (1 markers)

- l. 6: \small\renewcommand{\arraystretch}{1.2}\setlength{\tabcolsep}{4pt}

## thesis/thesis_main.tex (2 markers)

- l. 138: {\selectlanguage{german}%  [(translation of the approved English abstract, 2026-11-12; to be checked by a native German speaker)]
- l. 161: Universal segmentation models such as VoxTell segment many anatomical structures named by a free-text prompt,   [(content approved by the author 2026-11-12: problem, setup, trade-off with Adaptation 0.781 vs at most 0.485, few-shot result, control task, open question from the Summary)]

## Added after marker removal

- 2026-11-13, thesis/thesis_main.tex, English abstract: sentence "Continual-learning strategies aim to limit this forgetting." (suggested by Claude, added at the author's request); German abstract: "Strategien des kontinuierlichen Lernens sollen dieses Vergessen begrenzen." (translation, to be checked by a native German speaker)
- 2026-11-13, thesis/introduction.tex, Sec. 1.1, l. 18: 'Masks can be drawn by hand. However, drawing them is laborious, ...' merged into 'Drawing masks by hand is laborious, since ...' (suggested by Claude, approved by the author)
- 2026-11-13: 'five such strategies' (EN) / 'fünf solchen Strategien' (DE) in the abstracts (suggested by Claude, applied at the author's request)
- 2026-11-13, thesis/introduction.tex, Sec. 1.1, l. 22: 'For instance, the developers of the universal model SAT compared it with 72 nnU-Nets, one trained on each of their datasets' replaced by 'For instance, the SAT authors report that their single model performs comparably to 72 nnU-Nets, one per dataset' (suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex, Sec. 1.1, l. 23: 'In such models, the structure to segment is specified by an additional input, the prompt' replaced by 'Many universal models receive the structure to segment as an additional input, the prompt' (suggested by Claude, approved by the author)
- 2026-11-13: 'No strategy combined high adaptation with high retention.' (EN) / 'Keine Strategie verband hohe Anpassung mit hohem Erhalt.' (DE) replaces the longer sentence (suggested by Claude, applied at the author's request)
- 2026-11-13: 'only' (EN) / 'nur' (DE) dropped before '5, 10, and 20 volumes' (suggested by Claude, applied at the author's request)
- 2026-11-13, thesis/introduction.tex, Sec. 1.1, l. 40-41: 'which reflects the degeneration' -> 'which changes with the degeneration' (closer to SKM-TEA's 'sensitive to'); sentence 'These values are measured within the segmented structures.' deleted (repeated l. 39) (suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex, Sec. 1.1, l. 39: 'because quantitative biomarkers for osteoarthritis are measured within these structures' -> 'because quantitative \gls{mri} measures biomarkers for osteoarthritis within these structures' (introduces quantitative MRI before l. 41 uses it; suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex, Sec. 1.1, l. 45: 'would be expected to preserve' -> 'would probably preserve' (suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex, caption of Fig. 1.1: 'learned from a few labelled volumes' -> 'learned from labelled volumes of that structure' (main comparison uses the full split of 108 volumes); 'After every task, the same model has to segment all of these structures, with the lung standing for its pretrained ability.' -> 'The lung stands for the pretrained ability of the model.' (repeated the brace label); thesis/figures/tikz/ch1_setting.tex brace label 'new structures, one after another, few labelled volumes each' -> 'new structures, one after another' (suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex, Sec. 1.2, l. 60-61: 'continual fine-tuning' -> 'fine-tuning on one task after another' (suggested by Claude, approved by the author); sentence 'In our setting, such a lowering corresponds to a loss of pretrained ability.' deleted (author's proposal: it conflated pretrained ability with zero-shot accuracy)
- 2026-11-13, thesis/introduction.tex, Sec. 1.2, l. 82: 'The continual-learning results we found do not show' -> 'Published continual-learning results do not show' (read as the thesis's own results; suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex, Sec. 1.2, l. 82: topic sentence broadened from 'how few labelled volumes shift the balance' to 'where the balance ... lies for a model like VoxTell, with full or with few labelled volumes' so that the paragraph also motivates the full-split comparison (Sec. 6.2) (suggested by Claude, option A, approved by the author)
- 2026-11-13, thesis/introduction.tex, Sec. 1.2, l. 82: 'with full or with few labelled volumes' -> 'with many or with few labelled volumes' (readability; suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex, Sec. 1.2, l. 90: 'Other works measure it for CLIP ... builds on this idea' -> 'Other works measure it on data outside the task sequence, for CLIP ... builds on this approach' (explicit referent; suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex: few-shot definition at end of Sec. 1.2 paragraph ('In this thesis, few-shot means ...') deleted and merged into Sec. 1.3: 'As few-shot conditions, we use k = 5, 10, and 20 ...' -> 'By few-shot conditions, we mean training the model on k = 5, 10, or 20 labelled volumes per task, where one shot is one labelled training volume.' (suggested by Claude, approved by the author)
- 2026-11-13, thesis/notation.tex: section of first use of k updated from sec:intro-problem to sec:intro-rq (follows the merge of the few-shot definition)
- 2026-11-13, thesis/introduction.tex, Sec. 1.3, l. 102: clause 'and is the only one in which all strategies are compared' removed (repeated Sec. 1.4, l. 137-138; suggested by Claude, approved by the author)
- 2026-11-13, thesis/introduction.tex: cross-reference cuts (suggested by Claude, approved by the author): l. 90 '(\cref{sec:intro-approach})' removed; Sec. 1.5 sentence 'The works reviewed in \cref{sec:sota-summary} do not study the setting of \cref{sec:intro-problem}.' deleted (repeated the gap claim of Sec. 1.2); Sec. 1.6 the six appendix \cref targets removed (each appendix section is referenced from Ch. 5-6)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 26-27: CLIP citation moved from sentence end to directly after 'CLIP'; SegVol citation added to the training-data sentence (numbers checked in the SegVol paper: 96K CTs SimMIM pre-training, 6K labelled CTs, over 200 categories) (suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 31: CLIP-Driven Universal Model sentence: 'together with a global image feature' added, 'generates the output convolutions of each class' -> 'generates the weights of the last convolution layers for each class', locator [Sec.~3.2] added (checked in papers/text/Liu_2023.txt, Sec. 3.2, p. 4; suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 32: \cite{Liu_2023} added to the training-data sentence (numbers are in the abstract, Fig. 2 and Sec. 4, not in Sec. 3.2, so the sentence should not inherit the new locator)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 36: 'On the test splits of 72 datasets, which hold 22,186 scans in total, SAT's larger variant ...' split into 'SAT was trained and tested on 72 datasets with 22,186 scans in total.' + 'On their test splits, its larger variant, SAT-Pro, ... ~\cite[Suppl.~Table~3]{zhao2025sat}' (22,186 = whole SAT-DS, Sec. 4.2; numbers in Suppl. Table 3, DSC, All; suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 39: 'attribute BiomedParse's false positives to its slice-wise design' -> 'attribute ... most likely to its slice-wise design' (matches the SAT authors' 'likely because', Sec. 2.3; suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 47-50: SEER sentence rewritten to say what SEER is (front-end with a VLM that rewrites the request into a canonical prompt for a frozen segmentation model) and that its authors compared five models; new sentence 'SEER itself reached a worst-case DSC of 95.47 % on PENGWIN [Table 1]'. All claims checked in papers/text/NEW_seer2026.txt (Table 1 p. 6, pp. 2, 4, 5, 7). 'With VoxTell as the frozen model' left out: the paper does not name its backbone (suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 47-51: SEER paragraph clarified: sentence split (what SEER is / 'Its authors compared it with five existing text-promptable models ...'), 'Among these five models', last sentence 'SEER reached the highest worst-case DSC of all six, 95.47 % on PENGWIN' (checked in Table 1) (suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 47: 'SEER is a front-end in which a vision--language model rewrites a free-text request into a canonical prompt for a frozen segmentation model' -> 'SEER places a vision--language model before a frozen segmentation model to turn a free-text request and the image into a canonical prompt' (image grounding added, jargon 'front-end' avoided; SEER Sec. 2.2 p. 4, Sec. 3.2 pp. 7-8; suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 49: 'to 0.01 %' -> 'to 0.01 % on average' (SAT's mean free-text DSC on PENGWIN, SEER Table 1; worst case 0.00) (suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.1, l. 49-50: VoxTell/SAT sentence split into 'Among these five models, VoxTell kept the highest mean and worst-case DSC under free-text requests.' and 'SAT, in contrast, reached a DSC of 96.05 % on ... PENGWIN with the class-name prompt, but only 0.01 % on average with free-text requests.' (readability; SEER Table 1; suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.2, l. 64: ', and with 30 in a larger-data setting' added (Silva-Rodriguez et al. Sec. 4.3.1: K = {1, 5, 10} low data regime, K = 30 large data regime; matches Table 2.2) (suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.2, l. 72: CLIP-LoRA sentence: 'best' -> 'highest', '72.5 % against 70.9 % at one shot' -> '72.5 % at one shot against 70.9 % for the next-best method', locator [Table~2] added (fact card, arXiv v2; CVPRW table number unchecked) (suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.2, l. 73-74: own citations added to the CLIP-LoRA ablation sentence ([Sec. 6, Fig. 3]) and the 'not trivial' sentence ([Sec. 7]), checked in papers/text (arXiv v2), so that they do not inherit the new [Table 2] locator
- 2026-11-13, thesis/related_work.tex, Sec. 2.2, l. 81: 'The two 3D studies' -> 'The two 3D studies, by Silva-Rodriguez et al. and SEA-PEFT,' (referent named; both confirmed 3D in their papers) (suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, end of Sec. 2.2: sentence 'Among the works found in our search, only Chen et al. adapt a pretrained 3D medical model to a sequence of tasks ...' deleted (repeated the gap claim of Sec. 2.5 and previewed Sec. 2.4) (suggested by Claude, approved by the author)
- 2026-11-13, thesis/tables/ch2_sota.tex (Table 2.2): Silva-Rodriguez row 'Mean DSC, 9 organs, 10 shots: 77.79 %, LoRA (full FT 76.93 %)' -> 'Mean DSC, 9 known organs, 10 shots: LoRA 77.79 % (full FT 76.93 %)'; Beyond Forgetting row 'Domain-CL: 0.789, PNN (joint 0.830)' -> 'Domain-CL: PNN 0.789 (joint 0.830)' (method before value, consistent; suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.3, l. 90-91: opening reworded: 'Methods that add tasks to such a model while keeping its text-conditioned abilities have been developed for pretrained VLMs such as CLIP, and this section reviews them. They were developed ...' -> 'This section reviews continual-learning methods that add new tasks to a pretrained VLM such as CLIP while keeping the abilities it gained in pretraining. These methods were developed ...' (suggested by Claude, approved by the author)
- 2026-11-13, thesis/related_work.tex, Sec. 2.3, l. 103: clause ', where Bera et al. also compare how the stored data are selected' removed (previewed l. 173) (suggested by Claude, approved by the author)
- 2026-11-13, citation rule applied (thesis_notes.md 2026-11-13): related_work.tex l. 31 [Sec.~3.2] removed and l. 32 repeat \cite{Liu_2023} removed; l. 52 SEER [Table~1] citation removed; l. 72 CLIP-LoRA [Table~2] citation removed; l. 74 [Sec.~7] citation removed; l. 204 \cite{wang2025casam} added to the first CA-SAM sentence; background.tex l. 190 CLIP cited ('the zero-shot transfer of CLIP~\cite{radford...}'); introduction.tex l. 89 \cite{radford...,Zhang_2024_CVPR}
- 2026-11-13, thesis/introduction.tex, Sec. 1.2, l. 89: 'for CLIP~\cite{radford...,Zhang_2024_CVPR}' -> 'for a pretrained vision--language model~\cite{Zhang_2024_CVPR}' (Ch. 1 stays conceptual; CLIP no longer named in Ch. 1, so rule 6 does not apply) (suggested by Claude, approved by the author)
- 2026-11-14, thesis/related_work.tex, Sec. 2.3, l. 103: 'which shared LoRA with replay uses' -> 'which our strategy shared LoRA with replay uses' (marked as a thesis strategy, as l. 78, 111, 140) (suggested by Claude, approved by the author)
- 2026-11-14, thesis/introduction.tex, Sec. 1.2, after l. 54: new sentence 'At inference, it is known which task an input belongs to, its task identity~\cite[Sec.~1]{delange2022}.' (De Lange Sec. 1 scope: 'we assume it is known which task a given sample belongs to'; defines the term used in l. 128; aligns with Ch. 3/5) (suggested by Claude, approved by the author)
- 2026-11-14, thesis/related_work.tex, Sec. 2.3, l. 122: close paraphrase of Liu et al. Sec. 4.3 ('sharing the same low-rank space across tasks can still introduce interference') reworded: 'Liu et al. point out that restricting the updates of several tasks to the low-rank space of one LoRA does not by itself prevent interference between them.' (suggested by Claude, approved by the author)
- 2026-11-14, thesis/summary.tex, future work (replay paragraph), l. 92: 'Replaying such samples would avoid storing the volumes of earlier tasks.' -> combined with orthogonal-subspace constraints and their caveat (Liu et al. Sec. 4.3: 'strict orthogonality constraints ... may reduce available optimization directions, potentially limiting model plasticity') (suggested by Claude, approved by the author)
- 2026-11-14, thesis/summary.tex, l. 92: orthogonality addition reversed the same day; sentence restored to 'Replaying such samples would avoid storing the volumes of earlier tasks.' (author's decision on Claude's recommendation; see thesis_notes.md 2026-11-14)
- 2026-11-14, thesis/tables/ch2_sota.tex (Table 2.2 caption): 'MTIL: the eleven-dataset benchmark of ZSCL' -> 'MTIL: multi-domain task-incremental learning, a benchmark of eleven datasets from ZSCL' (expansion from ZSCL Sec. 1/4 and GIFT Sec. 4.1) (suggested by Claude, approved by the author)
- 2026-11-14, thesis/related_work.tex, Sec. 2.4.1, l. 170: 'We therefore do not adopt these methods.' -> 'We therefore do not adopt methods for background shift.' (referent made explicit; EWC/distillation/replay/ILT not rejected) (suggested by Claude, approved by the author)
- 2026-11-14, thesis/related_work.tex, Sec. 2.4.1, after l. 176: new sentence 'The diffusion model is trained on each task together with the segmentation network, and both receive the same learned task prompt, which is computed from the templates.' (C2GR Sec. 3.2-3.3, pp. 5-6; grounds the Summary caveat at summary.tex l. 91) (suggested by Claude, approved by the author)
- 2026-11-14, thesis/related_work.tex, Sec. 2.4.1, l. 186: 'the text prompt names the target structure' -> 'a new structure is named by its text prompt and needs no head of its own' (direct contrast to 'adds a head' in l. 185) (suggested by Claude, approved by the author)
- 2026-11-14, Table 2.2 (tables/ch2_sota.tex): scenario labels unified to the caption's abbreviations: Bera et al. 'DIL, ``task incremental''' -> 'DIL, TIL'; Zhang et al. 'class-incremental' -> 'CIL'; Chen et al. 'task-incremental' -> 'TIL' (each the paper's own term). liu2024universalextensible dropped everywhere (Table 2.2 and Table 2.1 rows now 'Zhang et al.' with zhang2023 only; related_work.tex l. 164 ILT baseline now cites zhang2023; l. 182 cites zhang2023 only): all mechanism and numbers are in Zhang et al. (MICCAI 2023, Table 2 p. 8); Liu et al. (MedIA 2024) is a journal paper merging that work with the CLIP-Driven Universal Model and adds nothing the thesis uses (author's proposal, checked by Claude)
- 2026-11-14, Table 2.2 (tables/ch2_sota.tex), Zhang et al. row: comparison '(PLOP 0.799 / 0.362)' -> '(pseudo-labels only 0.770 / 0.456)' (Zhang Table 2, p. 8, LwF row = pseudo-labelling; same reference as related_work.tex l. 184; PLOP was the weakest-but-one baseline on the tumour) (suggested by Claude, approved by the author)
