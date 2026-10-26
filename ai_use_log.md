# AI-use log

Format: `YYYY-MM-DD | chapter/section | what was done (outline / feedback / explanation / draft / translation / LaTeX fix / script)`

2026-10-17 | project setup | LaTeX fix: compiled thesis and reported warnings; recorded class/packages in CLAUDE.md; created empty chapter files 4–8 and added them to thesis_main.tex; created this log (no thesis text written)
2026-10-17 | results/extracted | script: extracted all xlsx tables verbatim to CSV (scripts/extract_results_xlsx.py), wrote results/extracted/README.md with formula documentation and data-quality flags; listed missing HPC information (no thesis text written)
2026-10-18 | Method/Experiments – CL metrics | feedback: checked metrics.py against Excel CL formulas; literature search on held-out control-task metrics (explanation, no edits)
2026-10-18 | Method/Experiments – control-task metric | feedback: recommendation on final vs averaged value, naming, and justification of single control task (no edits)
2026-10-18 | results/ + scripts/ – CL metrics | script: removed results/extracted and its script; built results/experiment_index.csv (scripts/build_experiment_index.py), reference CL metrics (scripts/compute_cl_metrics.py -> thesis/tables/cl_metrics.csv), control-task figure (scripts/plot_control_task.py -> thesis/figures/ch6_control_task_main.pdf); added control-task terms to CLAUDE.md (no thesis text written)
2026-10-18 | Method – CL metrics | feedback: compared forgetting definitions from 3 papers provided by author; computed candidate extra metrics (LA, BWT, pretrained reference) for discussion (no edits)
2026-10-18 | Method – CL metrics | explanation: why Average/Final Performance do not isolate adaptation; checked plasticity metrics in Wang et al. survey (no edits)
2026-10-18 | scripts/ – CL metrics | script: restored Chaudhry Eq. 3 forgetting, added Adaptation (diagonal mean) and Pretrained-model reference rows to compute_cl_metrics.py, regenerated thesis/tables/cl_metrics.csv; terminology in CLAUDE.md; reviewed new bib entries (no thesis text written)
2026-10-18 | results/ audit | feedback: audited HPC artifacts against the earlier information checklist (configs, per-volume scores, splits, prompts, curves, compute, code version); added replay/control-task note to experiment_index.csv (no thesis text written)
2026-10-18 | project notes | outline: created thesis_notes.md (decisions, verified facts with sources, limitations, open questions), pointer in CLAUDE.md; proposed writing workflow (no thesis text written)
2026-10-18 | scripts/ – Phase 0 results | script: per-volume Dice extraction (extract_per_volume.py), paired bootstrap over test volumes in compute_cl_metrics.py, LaTeX tables per experiment group (make_results_tables.py), result figures (plot_results.py, replaces plot_control_task.py), compute table (make_compute_table.py), run_all.py; updated CLAUDE.md and thesis_notes.md (no thesis text written)
2026-10-18 | Ch1 Introduction, Ch2 State of the Art | feedback: diagnosis only (issue list by structure/content/citations/language, term inventory with proposed CLAUDE.md entries, result-dependent statements) in reviews/ch1_ch2_diagnosis.md; no thesis text edited
2026-10-18 | terminology – strategy names | LaTeX fix/script: recorded strategy terminology in CLAUDE.md (also fixed 'task' and 'task order' entries) and thesis_notes.md; renamed strategies in scripts/_results.py and plot_results.py; regenerated tables and figures, fixed widths and legends (no thesis text written)
2026-10-18 | Experiments – variability | explanation: paired bootstrap over test volumes with worked example; recorded author decisions (no extra runs, heatmap abbreviations) in thesis_notes.md
2026-10-18 | Experiments – variability | recorded author decision on variability reporting in thesis_notes.md
2026-10-18 | Ch. 4 Data Description – preparation | script + outline: fact sheet from dataset papers and code (thesis_notes.md), HPC data-statistics script (scripts/hpc/data_stats.py), figure/table script (scripts/plot_data.py, tested on mock data, mock outputs deleted), proposed chapter outline and interview questions (no thesis text written)
2026-10-18 | Ch. 4 Data Description – HPC script | script: data_stats.py now logs progress immediately and reads each volume once (fix after silent run on the HPC)
2026-10-19 | Ch. 4 Data Description – facts | feedback: verified SKM-TEA label order (official DATASET.md vs skm_tea.py), AeroPath licence and lung-label documentation (README, Zenodo); recorded author's answers and open points in thesis_notes.md (no thesis text written)
2026-10-19 | VoxTell paper / Ch. 4 | explanation: read the VoxTell paper and wrote paper_notes/voxtell.md (facts with page/table locations, analysis marked separately); updated thesis_notes.md and CLAUDE.md; listed options for justifying the random split (no thesis text written)
2026-10-19 | Ch. 4 Data Description – figures/tables | script: plot_data.py extended with official SKM-TEA annotation files (spacing, orientation, official split, pathology), generated ch4 tables and figures from the HPC statistics, fixed figure orientation/aspect and table widths; recorded data facts and corrected split rationale in thesis_notes.md (no thesis text written)
2026-10-19 | Ch. 4 Data Description | draft: complete chapter (all paragraphs marked CLAUDE-DRAFT) from approved outline and author interview; abbreviations in abbreviations.tex; todonotes in preamble; HPC --examples-only option and three-panel example figure in plot_data.py; LaTeX fixes (pdf extension, cref)
2026-10-19 | Ch. 4 Data Description – figure | script: regenerated ch4_examples with coronal knee slice (examples_extra.npz), updated caption, removed todo; explanation of PDF vs PNG figures
2026-10-19 | planning | outline: recorded figure-format decision; proposed next steps (no thesis text written)
2026-10-19 | bibliography / planning | LaTeX fix: removed 5 duplicate bib entries, replaced Colab entry with skmtea_tutorial (fields from SKM-TEA README); CLAUDE.md updated for hand-maintained bib; workflow advice and status section in thesis_notes.md (no thesis text written)
2026-10-19 | planning | recorded author's confirmation of the workflow in thesis_notes.md
2026-10-19 | project overview | outline: wrote thesis_overview.md (summary of topic, data, strategies, metrics, results numbers without interpretation, limitations, status; no thesis text written)
2026-10-21 | Ch. 5 Method | outline + notation proposal + interview questions; fact sheet from code/configs/logs in thesis_notes.md (corrected checkpoint fact); LaTeX fix: added algorithm/algorithmic to preamble (no thesis text written)
2026-10-21 | Ch. 5 Method | explanation: evaluation of code findings F1-F5 and options under HPC outage; recorded author decisions in thesis_notes.md (no thesis text written)
2026-10-21 | Ch. 5 Method / Ch. 6 | script: scripts/selected_epochs.py (selected epoch per task from run.log, added to run_all.py); explanation: advice on reporting limitations honestly (no thesis text written)
2026-10-21 | Ch. 5/6, notes | LaTeX fix/script: renamed ZSCL-based to Distillation-based (CLAUDE.md, scripts/_results.py, regenerated tables/figures); fixed CLAUDE.md build notes; recorded interview answers; outline revision (Ch. 3/5/6 boundary) and supervisor email draft (no thesis text written)
2026-10-21 | Ch. 3/5/6 structure | explanation: chapter boundary Ch. 3/5/6, role of Alg. 1/2, naming options for CPE-CLIP-based; recorded author's method justifications (no thesis text written)
2026-10-21 | Ch. 5 / terminology | LaTeX fix/script: renamed CPE-CLIP-based to Prompt tuning (CLAUDE.md, scripts, regenerated tables/figures), recorded decisions and approved Ch. 5 outline; explanation: where to describe VoxTell (no thesis text written)
2026-10-21 | Ch. 5 Method | outline: detailed Ch. 5 outline (outlines/ch5_method.md), notation list (thesis_notes.md §5); paper notes for ZSCL and CPE-CLIP written from the PDFs (no thesis text written)
2026-10-21 | Ch. 5 Method | feedback: assessed author's answers on setting, ranks, replay, distillation, prompt tuning, checkpoint rule; checked rank evidence in cl_metrics.csv and code history (no thesis text written)
2026-10-21 | Ch. 5 Method | outline: recorded final design rationales (replay, distillation, checkpoint rule) in thesis_notes.md and outlines/ch5_method.md (no thesis text written)
2026-10-21 | Ch. 5 Method, opening + 5.1 | draft: chapter opening and Sec. 5.1 (all paragraphs CLAUDE-DRAFT), section skeleton with labels; LaTeX fix: added dsc abbreviation
2026-10-21 | Ch. 4 / bib / conventions | LaTeX fix: Ch. 4 checkpoint sentence corrected, Dice score -> \gls{dsc}; CoCoOp pages from the PDF (backup in scratchpad); DSC format recorded in CLAUDE.md and thesis_notes.md; explanation: why the setting is in Ch. 5
2026-10-21 | Ch. 5.1 / Ch. 6 notes | draft: 5.1 reduced to protocol concepts (task order, few-shot setting); moved values and reasons to outlines/ch6_experiments.md
2026-10-21 | Ch. 5.2 Evaluation Protocol | draft: Sec. 5.2 incl. Alg. 1 and complexity (all paragraphs CLAUDE-DRAFT); LaTeX fix: algorithmic Require/Ensure renamed to Input/Output
2026-10-21 | Ch. 3/5 figures | figure: TikZ VoxTell diagram in two variants (figures/tikz/voxtell.tex, setup.tex) based on the author's Figma layout, corrected to the code; script: scripts/make_diagram_assets.py (knee patch from own data); notes: notation and distillation-feature correction
2026-10-21 | figures / CLAUDE.md | rules: added the author's TikZ diagram rules to CLAUDE.md (font size adapted to the chair guideline); figure: rebuilt the VoxTell diagram as standalone files under these rules (positioning, orthogonal routing, 400 dpi crop checks); script: scripts/build_tikz.py added to run_all.py
2026-10-21 | Ch. 3/5 figures | figure: corrected prompt-decoder layer to the executed code path (forward_pre: no self-attention, positional encoding on keys only), separate LN boxes, no highlighted layer; notes: verified decoder-layer facts and unused self-attention parameters in thesis_notes.md
2026-10-21 | figures / scripts / CLAUDE.md | figure: skips shown as a brace over all encoder stages, keys/values route below the column; script: plot fonts raised to 10 pt, heatmap ticks rotated, Ch. 4 legend in 3 columns, axis labels Dice -> DSC; rules: natural-size inclusion and 10-11 pt font rule in CLAUDE.md
2026-10-21 | Ch. 5 figure | figure: stage-4 label moved to the keys/values route, legend symbols now copies of the figure marks; explanation: whether Ch. 5 repeats the architecture, other Ch. 5 figures
2026-10-21 | Ch. 3/5 figures | figure: Ch. 3 variant reduced to the overview (panel switch); Ch. 5 keeps overview + layer panel + strategy marks
2026-10-21 | Ch. 5 figure / notes | explanation: verified the distillation marks of Fig. 5.1 against the code; recorded distillation details in thesis_notes.md
2026-10-21 | Ch. 5.3 Adapting VoxTell to One Task | draft: Sec. 5.3 incl. Fig. 5.1 with caption, Eq. for the segmentation loss, Alg. 2 and its complexity (all paragraphs CLAUDE-DRAFT); LaTeX fix: Ch. 4 cross-reference to Sec. 5.3
2026-10-21 | Ch. 4 / Ch. 5.3 | LaTeX fix: short captions for the Ch. 4 figures and tables in the lists; removed the crop todo from 5.3 (kept as open item in thesis_notes.md); explanation: meaning of 'compute budget', forward reference to Fig. 5.1
2026-10-21 | Ch. 5.3 | draft: replaced 'compute budget' by the author's concrete reasons (GPU memory, 24 h job limit, simplicity)
2026-10-21 | Ch. 5.4 part 1 | draft: opening of 5.4 with selection rationale, Table 5.1 (tables/ch5_strategies.tex, written by hand), 5.4.1 sequential fine-tuning, 5.4.2 task-specific and shared LoRA (Eq. for LoRA), 5.4.3 replay (all CLAUDE-DRAFT)
2026-10-21 | Ch. 5.4 / notes | draft: selection rationale now follows the three families of De Lange et al. (author's excerpt); LoRA q/v reason grounded in Hu et al. Sec. 7.1 / Table 5 with its limitation; paper notes paper_notes/lora_hu.md; explanation: parameter counts verified from logs and code
2026-10-21 | Ch. 5 intro / 5.4 | draft: sequential fine-tuning described as a strategy without CL mechanism that serves as the baseline (author chose option a); strategy count made consistent
2026-10-21 | Ch. 5.4 / notes | draft: selection rationale rebased on the taxonomy of Liu et al. (VLM-CL survey, author's excerpt); notes paper_notes/liu2026_vlm_cl_survey.md
2026-10-21 | Ch. 5.4 part 2 | draft: 5.4.4 distillation-based strategy (Eq. for L_KD, six differences to ZSCL, weight ensemble not evaluated) and 5.4.5 prompt-tuning strategy (Eq. for the meta-net, differences to CPE-CLIP, inactive gradient scaling) (all CLAUDE-DRAFT)
2026-10-21 | Ch. 5.4.4 | draft: ZSCL ablation now cited with both outcomes (transfer kept, average/final accuracy lower)
2026-10-21 | Ch. 5.5 Computational Complexity | draft: Sec. 5.5 and Table 5.2 (tables/ch5_complexity.tex, written by hand); corrected the LoRA cost statement in 5.4.2 to the implementation (dense BA per forward, merged at inference); chapter status updated in CLAUDE.md
2026-10-22 | code / reruns | code (author-authorised, one-off): last-epoch checkpoints, run_info logging, task-boundary resume, ZSCL ensemble persistence and evaluation, CPE-CLIP meta-net scaling, tagged evaluations, joint training; configs and smoke tests in code/configs/continual/rerun_2026_10/
2026-10-22 | code / reruns | code review of all rerun changes: fixed ZSCL resume early in a task, after_task before completion state, shared-LoRA boundary restore, weights-only best/last checkpoints, removal of recovery files after a task; README updated (sync, storage, checks)
2026-10-22 | code / reruns | explanation + code: checked host and GPU memory of the distillation rerun; evaluator releases each cell's models (gc, empty_cache); README memory checks
2026-10-22 | code / reruns | final review of all code changes and configs before the HPC runs; go-ahead given; README: durations, smoke folders excluded
2026-10-22 | code / reruns | git: on the author's request committed the rerun changes to code/ main (6598fdc) and pushed to origin/main for pulling on the HPC
2026-10-22 | code / reruns | code (author-authorised): replay option include_retention_tasks and replay memory persisted across resumes (found: memory lost at resume in the original replay run); configs for replay without/with control volumes, smoke test, README
2026-10-22 | Ch. 5 / reruns | draft: replay described without control-task volumes (author's option c); with-control config removed; CLAUDE.md terminology and thesis_notes.md updated
2026-10-22 | code / reruns | git: on the author's request committed the replay change to code/ main and pushed
2026-10-22 | Ch. 5.3 / scripts / code (prepared, not applied) | recommendation on few-shot update-count confound and shared training configuration; one-sentence draft + defense todo in 5.3; script compare_strategies.py (paired bootstrap differences); validation_interval patch and equal-updates configs prepared in scratchpad (script)
2026-10-22 | code / reruns | code (author-authorised): training.validation_interval in trainer and loss plot; 3 equal-updates configs (k = 5, 216 epochs) + smoke config; README updated
2026-10-22 | code / reruns | git: on the author's request committed and pushed the validation-interval change (code/ 566ff30); fallback note for late reruns in thesis_notes.md
2026-10-22 | Ch. 5.1, 5.4.3 | draft: replay text reverted to the existing run (control-task volumes, memory lost at resume in task 6) so the text does not depend on reruns; list of rerun-dependent passages in thesis_notes.md §4; CLAUDE.md replay entry
2026-10-22 | Ch. 3 | outline: proposed structure of Theoretical Background (outlines/ch3_background.md) with 5 open questions; no thesis text
2026-10-22 | Ch. 3.1 | draft: chapter intro and Sec. 3.1 (encoder-decoder networks, attention, VoxTell as published, Fig. 3.1 caption); decisions and notation recorded in thesis_notes.md
2026-10-22 | tooling | script: agents .claude/agents/bib-entry-adder.md and citation-verifier.md (find/verify/add bib entries; check that citations support the text)
2026-10-22 | bibliography | bib entries (on request, via bib-entry-adder): added milletari2016vnet, dice1945measures, isensee2024nnunetrevisited, hinton2015distilling, zhou2022coop, zhang2025qwen3embedding, efron1993bootstrap; completed NIPS2017_3f5ee243; upgraded ZSCL, LwF, Kemker, CLIP to peer-reviewed versions; backup thesis/bib_backups/literature_20261022_164952.bib
2026-10-22 | Ch. 3.1, Ch. 5.3 | LaTeX fix: replaced cite todos by the new keys
2026-10-22 | Ch. 3.2 | draft: Sec. 3.2 (problem in symbols, evaluation matrix, forgetting, relation to CL scenarios); chapter split of CL concepts recorded
2026-10-22 | reruns | checked smoke and resume test outputs with the author (all passed); launch commands; job IDs and parallelism note in thesis_notes.md; reproducibility facts (cudnn.benchmark, empty patches) recorded
2026-10-22 | paper notes | notes from PDFs: paper_notes/rslora.md, delange2022.md, cocoop.md
2026-10-22 | Ch. 3.2, 3.3 | draft: Sec. 3.3 (LoRA/rsLoRA, replay, distillation/LwF/ZSCL, prompt learning/CoOp/CoCoOp/CPE-CLIP); 3.2 stability-plasticity cite
2026-10-22 | Ch. 5.4.2 | LaTeX fix / draft: LoRA paragraph now refers to the Ch. 3 equations (author's option a); Ch. 5 refs to Ch. 3 replaced by \cref
2026-10-22 | paper notes | notes from PDFs: paper_notes/chaudhry2018.md, spu.md
2026-10-22 | Ch. 3.4 | draft: Sec. 3.4 (DSC, six metric definitions with sources); figure: Fig. 3.2 TikZ (figures/tikz/ch3_metrics.tex); LaTeX fix: remaining Ch. 3/Ch. 5 cross-references
2026-10-22 | tracking | script: thesis_tracker.md (34 defense points, rerun items, author items) and scripts/list_todos.py; CLAUDE.md pointer
2026-10-22 | Ch. 6 | outline: chapter structure (6.1–6.7, now vs reruns) and 4 interview questions for 6.1.4; tracker D35
2026-10-22 | Ch. 6.1 | draft: 6.1.1-6.1.3 (overview, data/task orders/few-shot, training configuration); script: make_setup_tables.py (3 generated tables), rank table incl. task-specific r=8 (index roles); skeleton 6.2-6.7
2026-10-22 | Ch. 3.4, Ch. 6.1.4 | draft: 6.1.4 (metric choice, reference row, bootstrap, pre-defined comparisons) after the author's Q1-Q4 decisions; Average Performance removed from Ch. 3.4, Fig. 3.2 and all Ch. 6 tables/figures; CLAUDE.md retention/transfer terms
2026-10-22 | Ch. 6.3 | draft: rank experiment setup and results (no conclusion yet; interview questions); figure/table metric order primary-first
2026-10-22 | Ch. 6.1, 6.3, 6.4 | draft: 6.3 conclusion (author's answers), new Sec. 6.4 patellar diagnosis; script: diagnosis table (make_results_tables.py), training-loss figure (plot_results.py), Table 6.1 row; index roles for 4 diagnosis runs
2026-10-22 | Ch. 6.8, Ch. 4, Ch. 5 | draft: 6.8 computational cost (measured time/memory from compute.csv); LaTeX fix: 20 Ch. 4/5 references to Ch. 6 resolved with \cref
2026-10-22 | Ch. 6.5, 6.6 | draft: LoRA parts of few-shot and task-order experiments (results only; conclusions open); code check of adapter initialisation vs seeding; tracker D39-D41
2026-10-22 | Ch. 6.3, 6.6, Ch. 7 notes | draft: 6.6 training-loss evidence and conclusion (author's hypothesis, refined), pointer in 6.3; outline notes: outlines/ch7_discussion.md (hypothesis with evidence for/against)
2026-10-22 | Ch. 6 | LaTeX fix: float placement (Table 6.3 [tbp], others [tb]) so tables appear at their sections; script: group spacing in result tables; layout check of all Ch. 6 pages
2026-10-22 | Ch. 6.1, Ch. 5.3, App. A | draft: software environment in 6.1.3 (author's versions), Appendix A (volumes, evaluation matrices); script: make_appendix_tables.py; LaTeX fix: MONAI Dice check resolved (verified in MONAI 1.5.2 source)
2026-10-22 | planning | outline: plan to submission and page-budget guidance recorded (thesis_notes.md §0); Ch. 1/2 status changed to notes to be redrafted (CLAUDE.md)
2026-10-22 | Ch. 2 | outline: State of the Art outline from the author's notes and the Ch. 1/2 diagnosis (outlines/ch2_state_of_the_art.md), with questions for the author
2026-10-22 | Ch. 2 | outline: plan for collecting sources (three tiers, paper index, notes) before revising the Ch. 2 outline
2026-10-22 | Ch. 2 | outline: step 1 of the source plan — paper index with tiers (papers/index.csv), web search and search record (papers/search_log.md)
2026-10-23 | Ch. 1/2 sources | script + outline: PDF download (papers/download_papers.py), paper notes (8 full, 25 cards, via subagents), tier A citation checks, consolidated source check (reviews/ch1_ch2_source_check.md)
2026-10-23 | Ch. 2 sources | script: download of 7 new works, recorded API literature search (papers/search/run_search.py); notes on the new works via subagents
2026-10-23 | Ch. 2 sources | script + outline: recorded API search and screening (papers/search_log.md, search 2); notes on 7 new works via subagents; index/tracker updated
2026-10-23 | Ch. 2 | outline: revision 2 of the State of the Art outline from the paper notes (outlines/ch2_state_of_the_art.md); Ch. 7 pointers to prior work
2026-10-23 | Ch. 2 intro, 2.1 | draft (all paragraphs % CLAUDE-DRAFT, from paper notes/cards); LaTeX fix: PET abbreviation, broken ref in old 2.4 notes; bib: update via bib-entry-adder (author-authorised, backup in backups/)
2026-10-23 | Ch. 2.1 | draft revision after citation check (reviews/ch2_s1_citation_check.md): 4 overstatements, 2 close paraphrases of VoxTell, 4 uncited generalisations fixed
2026-10-23 | bibliography | bib update via bib-entry-adder (16 new entries, ~30 upgrades to peer-reviewed versions, field fixes; author-authorised)
2026-10-23 | Ch. 2 | outline: session handoff written (outlines/ch2_state_of_the_art.md)
2026-10-23 | Ch. 2.2 | draft (few-shot adaptation, from fact cards) + citation check via citation-verifier
2026-10-23 | Ch. 2.2 | draft revision after citation check (reviews/ch2_s2_citation_check.md): 1 unsupported, 7 partly supported claims fixed, 2 citations added
2026-10-23 | Ch. 2.3 | draft (continual learning for pretrained VLMs, from notes/cards; replaces old 2.3 text) + citation check via citation-verifier
2026-10-23 | Ch. 2.3 | draft revision after citation check (reviews/ch2_s3_citation_check.md): 3 partly supported claims, 2 uncited generalisations, 3 close paraphrases fixed; O-LoRA dropped and scope sentence added (author decision)
2026-10-23 | Ch. 2.4 | draft (continual learning for medical image segmentation, from notes/cards; replaces old 2.4 text) + citation check via citation-verifier
2026-10-23 | Ch. 2.4 | draft revision after citation check (reviews/ch2_s4_citation_check.md): 1 unsupported synthesis claim, 5 partly supported, 4 uncited/overgeneral sentences, 2 close paraphrases fixed
2026-10-23 | Ch. 2.5 | interview (gap claim, motivation, framing) — answers recorded in thesis_notes.md
2026-10-23 | Ch. 2.5 | draft of summary, gap and positioning text from the author's interview answers; section renamed "Summary and Research Gap"
2026-10-23 | Ch. 2.5 | LaTeX edit: exact few-shot scope sentence and strategy-selection sentence (author decision)
2026-10-23 | Ch. 2.5 | Table 2.1 (ch2_sota.tex) and Table 2.2 (ch2_positioning.tex) written from paper notes; old tables replaced; LaTeX fixes (overfull cells)
2026-10-23 | Ch. 2.5 | LaTeX edit: Table 2.1 compacted (data column shortened, metric merged into result column; author decision)
2026-10-23 | Ch. 1 | outline (revision 1, outlines/ch1_introduction.md) and interview questions Q1-Q7; no prose drafted
2026-10-23 | Ch. 1 | interview round 1 recorded; recommendations for Q4-Q6; source check for knee clinical relevance (SKM-TEA paper)
2026-10-23 | Ch. 1 | outline revision 2 (rebuilt from thesis content, independent of old introduction text)
2026-10-23 | Ch. 1.1 | draft (all paragraphs % CLAUDE-DRAFT, from VoxTell notes, SKM-TEA paper, cl_metrics.csv); figure recommendation
2026-10-23 | Ch. 1.4, Ch. 5.1 | figure (TikZ, ch1_protocol: protocol overview without notation, checked on 400 dpi crops) + caption draft; one reference sentence in 5.1
2026-10-23 | Ch. 1.2 | draft (all paragraphs % CLAUDE-DRAFT, from interview answers Q2/Q3, Ch. 2.3-2.5, De Lange/ZSCL notes, experiment_results.tex update counts)
2026-10-23 | Ch. 1.3 | draft (research question unchanged; objectives per interview Q3-Q5, % CLAUDE-DRAFT)
2026-10-23 | Ch. 1.4 | draft (setting, strategies, data amounts, measures, delimitations; % CLAUDE-DRAFT; from method/experiment chapters and Table 6.1)
2026-10-23 | Ch. 1.5, 1.6 | draft (provisional contributions per Q6, own vs prior work; thesis outline; % CLAUDE-DRAFT)
2026-10-23 | Ch. 1 | citation check via citation-verifier (reviews/ch1_citation_check.md); figure redesign proposal
2026-10-23 | whole thesis | status check (what is still missing apart from the reruns); no thesis edits
2026-10-23 | Ch. 1, 2.5, 4.2 | LaTeX/citation fixes after the citation check (wording, locators, added citations, CoCoOp attribution); figure: Ch. 1 setting figure (TikZ + image assets script) replaces the matrix figure
2026-10-23 | Ch. 7 | outline (revision 1 proposed) and interview questions
2026-10-23 | whole thesis (Ch. 1-6, App. A) | feedback + LaTeX edit: cross-chapter repetition removed, inconsistencies fixed (Ch. 3 fusion eq., control-task wording, checkpoint rule, citations/locators, terminology); issue list in reviews/whole_thesis_pass_2026-10-23.md; no new content
2026-10-24 | reruns | read sacct status with the author; resume commands for the six timed-out runs; run status in thesis_tracker.md §B
2026-10-24 | reruns | checked the copied rerun folders (configs, commits, eval matrices, reproduction of old few-shot runs); job-to-folder map in thesis_tracker.md §B (script in scratchpad)
2026-10-24 | Ch. 7 | outline alternatives and placement of the discussion (guideline check); outline revision 2 approved
2026-10-24 | Ch. 7 intro, 7.2; Ch. 6.6; Ch. 1.6 | draft (Ch. 7 intro and 7.2 from the author's hypothesis and interview answers; 6.6 last-step observation from the eval matrices; % CLAUDE-DRAFT); LaTeX fix (Ch. 7 cross-references in Ch. 1 and Ch. 6)
2026-10-24 | Ch. 7.3 | draft (limitations and threats to validity from thesis_notes §3, tracker defense points and interview answers; SEER, PRIMED, MedCRP-CL from paper notes; % CLAUDE-DRAFT)
2026-10-24 | Ch. 7.4 | draft (generalisation, task-aware inference in practice, future work from the interview answers Q7-Q9; % CLAUDE-DRAFT)
2026-10-24 | Ch. 7.1 | draft (objective 4: task order and rank, from the interview answers Q3, Q4, Q5; % CLAUDE-DRAFT); interview questions for objective 1
2026-10-24 | Ch. 7.1 | draft (objective 1: evaluation protocol, from the author-approved suggestions; % CLAUDE-DRAFT)
2026-10-24 | Ch. 6.2; plan | outline (6.2 detailed outline and interview questions Q1-Q5 from the existing runs); plan change recorded (draft from existing runs, reruns as a bonus)
2026-10-24 | Ch. 6.2 | explanation (Claude's suggested reading of the main comparison and recommendations for interview Q1-Q5, offered as options for the author to decide)
2026-10-24 | Ch. 6.2; Ch. 1.3, 1.5, Ch. 5.4.3 | draft (6.2 from the existing runs; conclusion from Claude's suggestions accepted by the author; % CLAUDE-DRAFT); script (replay row added to the main table in make_results_tables.py, Table 6.1 replay row points to 6.2 in make_setup_tables.py); LaTeX fix (references to the dropped Strategy Components section)
2026-10-24 | Ch. 6.5, 6.6 | draft (sequential fine-tuning results from the existing few-shot and reverse-order runs; % CLAUDE-DRAFT); interview questions for the conclusions
2026-10-24 | Ch. 6.5, 6.6, 7.1, Ch. 8 | draft (6.5/6.6 conclusions and 7.1 objectives 2-3 from the author-accepted conclusions; MedPEFT-CL from paper notes; % CLAUDE-DRAFT); outline (Ch. 8 summary with interview questions)
2026-10-24 | Ch. 7.1, Ch. 8 | explanation (Claude's recommendations for the Ch. 8 interview Q1-Q4, offered as options for the author); LaTeX fix (7.1 opening sentence corrected: gradual trade-off within shared LoRA)
2026-10-24 | Ch. 8; Ch. 1.6 | draft (Summary from the approved outline and the author-accepted recommendations Q1-Q4; % CLAUDE-DRAFT); LaTeX fix (Ch. 8 reference in the thesis outline)
2026-10-24 | Front matter; Ch. 3.4, 4.5, 4.6, 5, 7.3 | draft (table of notation from thesis_notes §5, checked against all chapters); LaTeX fix (symbol clashes n, m, C, p renamed; Ch. 5 ref); explanation/facts (D4-D6 from VoxTell plans.json, D29 from ZSCL Fig. 4b; Ch. 4 preprocessing/limitations and 7.3 corrected: orientation, not scale); bib (yushkevich2006itksnap added from Crossref, Zhang_2024_CVPR month fixed; backup backups/literature_2026-10-24_before_itksnap.bib); LaTeX fix (VoxTell supplement locators unified)
2026-10-24 | Front matter | LaTeX fix (Notation added to the table of contents)
2026-10-24 | Whole thesis | outline (review and rewrite plan REVIEW_PLAN.md: strategy, timeline to submission, feedback conventions, checklists)
2026-10-24 | code / reruns | diagnosed truncated recovery checkpoints; code (author-authorised): atomic checkpoint writes, committed and pushed (code/ e5df182); resume plan; storage plan
2026-10-24 | reruns | joint_ft restart (1849225) recorded in thesis_tracker.md
2026-10-24 | Ch1 introduction.tex l.18 | feedback (register and precision of one drafted sentence)
2026-10-24 | Ch1 introduction.tex l.18, 23-26 | feedback + minimal edit (register of l.18 as agreed; SAT sentence moved after the universal-model sentence)
2026-10-24 | Ch1 introduction.tex l.29-33 | LaTeX edit (approved: SAT sentence trimmed, contrast marker, output-channel sentence framed for both models)
2026-10-24 | Ch1 introduction.tex l.36-41 | LaTeX edit (approved: structure list shortened, label-list argument compressed to one sentence with ref to 4, own 0.114 result removed)
2026-10-24 | Ch1 introduction.tex l.39-44 | LaTeX edit (approved: dangling label-list sentence removed; biomarker paragraph simplified)
2026-10-24 | Ch1 introduction.tex l.46-49 | draft (from author's version, approved: few-shot reason, sequential arrival with Qazi cite, retention requirement, retraining cost)
2026-10-24 | Ch1 introduction.tex l.46-49 | LaTeX edit (callback to manual annotation; 'this problem' replaced by explicit retraining clause)
2026-10-24 | Ch1 introduction.tex l.46-49 | LaTeX edit (author's reframed paragraph: grammar fixes, few-labelled-volumes sentence added, Qazi cite kept)
2026-10-25 | reruns | status update (13 of 15 finished) in thesis_tracker.md
2026-10-25 | Ch. 1, end of 1.1 / start of 1.2 | feedback (transition and repetition, no edits)
2026-10-25 | Ch1 introduction.tex end of 1.1 / start of 1.2 | LaTeX edit (option 1: retention sentence removed from 1.1; continual-learning definition added and requirement sentences merged at start of 1.2; repeated manual-annotation sentence cut from few-shot paragraph)
2026-10-25 | Ch1 Fig. ch1_setting | feedback (verified knee overlays against label mapping; critique of text amount and caption; redesign suggestions from author's reference image; no edits)
2026-10-25 | Ch1 Fig. ch1_setting | script + TikZ + caption draft (landscape knee/lung crops in make_diagram_assets.py; requirement boxes replaced by one brace; pretrained DSC from cl_metrics.csv added; caption shortened to terms defined before the figure)
2026-10-25 | Ch1 Fig. ch1_setting | script (Ch. 1 images: full uncropped slices, bicubic resampling to square pixels at ~535 dpi instead of nearest-neighbour crops); figure rebuilt
2026-10-25 | Figures (Ch1/3/4/5) | explanation (which samples and slices the image figures use; screenshot vs. script trade-off; no edits)
2026-10-25 | Figures (Ch1/3/4/5) | explanation (how the slice images are produced; resampling check of label areas; verification steps; no edits)
2026-10-25 | Ch1 1.2 l.55-89 | feedback (few-shot paragraph length, 'In this thesis', transitions, CL-medseg sentence, strategy-options sentence; no edits)
2026-10-25 | Ch1 1.2-1.3 | LaTeX edit (forgetting sentence moved before dilemma; few-shot paragraph opened with link to dilemma and shortened; duplicate claim merged into next paragraph opening; CL-medseg sentence corrected; strategy-choice sentence rewritten, option b; update numbers moved to 1.3)
2026-10-25 | Ch1 1.2 l.62-63, 79-80, 88 | feedback (forgetting-definition placement, few-shot definition length, incorrect 'did not face' claim; no edits)
2026-10-25 | Ch1 1.2-1.3 | LaTeX edit (zero-shot loss linked to pretrained ability; forgetting definition moved to 1.3; few-shot definition shortened; incorrect 'did not face' sentence deleted) + feedback on flow of 1.2
2026-10-25 | Ch1 1.1-1.2 | feedback + proposed revision (flow of 1.2 restructured; sentence-level readability proposals for 1.1 and 1.2; not yet applied)
2026-10-25 | Ch1 1.1-1.2 | LaTeX edit (approved readability revisions in 1.1; 1.2 restructured: setting, forgetting/dilemma, few-shot, existing results, gap)
2026-10-25 | Ch1 1.1-1.3 + Fig. 1.1 caption | LaTeX edit (six semicolon sentences split into two)
2026-10-25 | Writing style (all chapters) | feedback (derived writing rules from the Ch1 1.1-1.2 revision; proposed for CLAUDE.md, not added)
2026-10-25 | Writing style (all chapters) | explanation (scope of the derived writing rules: general vs. chapter-specific)
2026-10-25 | CLAUDE.md writing style | rules added (tiered sentence and paragraph rules from the Ch1 revision; section review checklist item 7 extended), approved by author
2026-10-25 | All chapters (1-8, appendix) | feedback (tier-1 pass: 44 findings in reviews/tier1_pass_2026-10-25.md; no edits)
2026-10-25 | Ch1 1.1-1.6 | LaTeX edit (line-by-line readability pass: tier-1 findings #1-3 fixed; insertions split, referents made explicit, 'task' defined before continual learning, long sentences split, metric definition and outline sentences reworded)
2026-10-25 | Ch1 1.2-1.5, Ch2 2.5, Ch5 5.4 | LaTeX edit (conciseness/completeness pass on Ch1: secondary metrics and retention defined, bootstrap and missing joint-training reference stated, repetition and cross-references cut; 'families' as the one term for CL method categories, also in CLAUDE.md)
2026-10-25 | Ch1 1.1 l.55, 1.2 l.63-67 | LaTeX edit (retraining claim softened; 1.2 opening paragraph: repeated few-shot clause and task-list sentence cut, CL definition and requirements sentence reworded)
2026-10-25 | Ch1 (all) | LaTeX edit (punctuation pass: combined citation via \cites, caption comma splice, dangling 'with a bootstrap', serial comma in outline replaced by rewording, spaces before \todo)
2026-10-25 | Ch1 1.2 l.92, Ch2 2.2 l.72 | LaTeX edit ('fine-tuning' -> 'training' in the few-shot definition; Ch1 already changed by the author)
2026-10-25 | Ch1 1.3, 1.5 | LaTeX edit ('adaptation performance' defined under the RQ; contribution 3 'adaptation configuration' -> 'configuration of the strategies') + explanation (Adaptation vs Final/Average Performance as adaptation measure)
2026-10-25 | Ch1 1.4 | LaTeX edit (Adaptation definition: average over the six tasks made explicit) + explanation (relation Final Performance = Adaptation - 5/6 Final Forgetting, checked on cl_metrics.csv)
2026-10-25 | Ch1 1.2 | LaTeX edit (stability-plasticity sentence reworded without the noun 'adaptation')
2026-10-25 | Ch2 2.1 para. 1 | LaTeX edit (SegVol training data and AMOS22 comparison corrected from the paper, 2D qualifier, SAM abbreviation added)
2026-10-25 | Ch. 2 (all sections, Table 2.1) | line edit of own draft for readability, flow, consistency (sentence splits, term fixes, tier-1 findings #4-#12, lost 2.1 fix re-applied, SAM/IoU glossary entries) (LaTeX fix / draft)
2026-10-25 | Ch. 2.1 para. 1 | removed repeated definitions of promptable/free-text promptable (defined in Ch. 1.1), topic sentence with reference to Ch. 1 (draft)
2026-10-25 | Ch. 1.1 | SAT detail (497 classes, language-model mapping) removed, kept in Ch. 2.1; reference added (draft)
2026-10-25 | Ch. 1.1, 2.1 | removed two redundant cross-references between Ch. 1 and Ch. 2 (LaTeX fix)
2026-10-25 | Ch. 2.1 para. 1 | removed 'five correction steps' detail of the SAM-Med2D baseline (draft)
2026-10-25 | Ch. 2.1 para. 1 | readability rewrite of SegVol sentences (split list, plain pretraining wording, metric definition in own sentence) (draft)
2026-10-25 | Ch. 2.1 para. 1 | removed sentence on SegVol's median-per-category metric (stated in Table 2.1) (draft)
2026-10-25 | Ch. 2.1 para. 2 | R-Super sentences rewritten for flow (contrast with LViT/TextMatch first, split into three sentences) (draft)
2026-10-25 | Ch. 2.1, Table 2.1 | cut A1 (LViT/TextMatch/R-Super to 3 sentences, numbers only in table) and A3 (Text3DSAM removed from text and table) (draft)
2026-10-25 | Ch. 2.1, Table 2.1 | TextMatch removed from text and table (author decision) (draft)
2026-10-25 | Ch. 2.1 para. 3 | SAT part shortened from 5 to 3 sentences (author's wording, formatting and referent fix) (LaTeX fix)
2026-10-25 | Ch. 2.1 | B1 applied: comparisons kept in text only where the argument uses them (SegVol, CLIP-Driven, BiomedParse, MedSAM-3, SAT in SEER shortened; numbers remain in Table 2.1) (draft)
2026-10-25 | Ch. 2.1, Ch. 3.1 | VoxTell paragraph in 2.1 shortened (repeats of Ch. 1 removed, SAT contrast kept, 10.72 % as one clause); training-data sentence moved from Ch. 3 (background.tex:75) to 2.1 (author decision) (draft)
2026-10-25 | Ch. 2.1 | removed fixed-prompt pointer sentence after SEER (covered in Discussion 7.x, discussion.tex:142-144) (draft)
2026-10-26 | reruns | status update (14 of 15 finished, joint_ft resume) in thesis_tracker.md
2026-10-26 | Ch. 2.2 | answered author's five questions on placement, scope, review-paper opening, UniverSeg/zero-shot, level of detail; proposed a trimmed outline for 2.2 (feedback)
2026-10-26 | Ch. 2.2 | revised outline for 2.2 with CLIP-LoRA as implementation reference; checked LoRA layer code origin (outline)
2026-10-26 | Ch. 2.2 | redrafted 2.2 from the approved outline (purpose opening, UniverSeg not zero-shot, numbers cut to those the argument uses, CLIP-LoRA as code and placement source) (draft)
2026-10-26 | Ch. 5.3, Ch. 2.2 | added code-source sentence for the LoRA layers (adapted from CLIP-LoRA loralib, URL footnote); 2.2 wording 'took' -> 'adapted' (draft)
2026-10-26 | Ch. 2.2 | rewrote para. 1 for readability (two approaches to few-shot from review Sec. 2.2, UniverSeg as example of the first, thesis follows the second) (draft)
2026-10-26 | Ch. 2.2 | rewrote last paragraph (review Sec. 5.6 sentence cut, sentence on the sequential setting added as bridge to Chen et al.) (draft)
2026-10-26 | Ch. 2.2 | feedback on clarity and focus of paras 2-3 (Silva-Rodriguez/SEA-PEFT, CLIP-LoRA), proposed rewrites; defense point D50 added (feedback)
2026-10-26 | Ch. 2.2 | applied approved rewrites of paras 2-3 (findings first, LoRA 5->10 shots added, 'therefore' removed, q/v named) (draft)
2026-10-26 | Ch. 2.2 | para. 2 numbers reduced from ten to three (known-organ comparison in words) (draft)
2026-10-26 | Ch. 2.2 | feedback: keep the shot-range sentence, proposed more precise wording (feedback)
2026-10-26 | Ch. 2.2 | split CLIP-LoRA implementation sentence in two; shot-range sentence made precise; feedback on line 94 (Chen et al. not a pure segmentation sequence) (draft)
2026-10-26 | Ch. 2.2 | Chen et al. sentence made precise (pretrained 3D medical model, one segmentation task); shot-range sentence reverted on author's request (draft)
2026-10-26 | Ch. 2.3 | para. 1 scenario definitions rewritten for readability (last sentence kept pending author decision); explained the scenario positioning and its weak point, D31 reopened (draft / explanation)
2026-10-26 | Ch. 2.3 | transition sentence on our setting vs scenarios: both reasons in one line (prompt names target, no task identity) (draft)
2026-10-26 | Ch. 2.3 | checked which scenario the closest prior works (text-promptable / universal segmentation) assign to their setting; proposed positioning line (explanation)
2026-10-26 | Ch. 2.3, Ch. 3.2 | scenario positioning changed to 'closest to task-incremental learning' (2.3 one line, 3.2 paragraph); CLAUDE.md terminology rule and thesis_notes decision log updated; D31 answered (draft)
2026-10-26 | Ch. 2.3 | para. 2 lines 117-118 merged into one signpost sentence; feedback on the evaluation-ideas paragraph (draft / feedback)
2026-10-26 | Ch. 2.3 | evaluation-ideas paragraph split for readability (one definition per sentence, ZSCL named, SPU insertion removed, \Cref at sentence start) (draft)
2026-10-26 | Ch. 2.3, 6, 7, 8 | register fixes: 'told' replaced in the scenario definitions (Ch. 2.3), referent fixed; 'cannot tell' replaced by 'cannot determine' / 'does not show' (7 places in Ch. 6-8) (LaTeX fix / language)
2026-10-26 | reruns | final check of all 15 reruns (completeness, configs, commits, logs, mechanisms, reproduction of old runs); reproducibility facts and limitations updated in thesis_notes.md; status in thesis_tracker.md
2026-10-26 | scripts | analysis scripts extended for the reruns (index columns, tagged evaluations, joint runs, per-row bootstrap seed, counterpart and selected-epoch rules); full pipeline rebuilt
2026-10-26 | results index / scripts | roles of the reruns assigned on the author's request (backup kept); make_setup_tables and make_results_tables adapted to the new roles; pipeline rebuilt; stale numbers in the text listed in thesis_tracker.md
2026-10-26 | Ch. 6/7 (reruns) | results overview of the reruns (facts, outlines/rerun_results_overview.md) and interview questions for the interpretation
2026-10-26 | Ch. 5.2 | draft (approved changes): joint fine-tuning reference, evaluated vs carried-forward parameters, evaluation cost
2026-10-26 | Ch. 5 (5.1, 5.3-5.4), Ch. 4.4, Ch. 1, CLAUDE.md | draft: switched to the rerun decisions (last-epoch rule, additional evaluations, replay without control volumes, weight ensemble, active gradient scaling); Table 5.1 column removed
2026-10-26 | Ch. 6, App. A, scripts | draft: Ch. 6 switched to the reruns (6.1, 6.2 rewritten incl. joint reference and additional evaluations, 6.5 equal updates, 6.6, 6.7); tables ch6_main/ch6_few_shot extended, new ch6_components; paired differences for tagged evaluations; appendix with all 38 runs
2026-10-26 | Ch. 7, Ch. 6.1.3 | draft: Ch. 7 switched to the reruns following decisions Q1-Q9 (objectives 1-4, budget hypothesis, limitations, extensions); author-confirm todos for new readings; 6.1.3 reproducibility of resumed runs
2026-10-26 | Ch. 8, Ch. 1, Ch. 2, Ch. 3, CLAUDE.md | draft: Ch. 8 and the rerun spots of Ch. 1/2 switched to the reruns; Ch. 3 intransigence reference corrected; chapter status table updated; contributions left provisional
2026-10-26 | Ch. 1.5, Ch. 8 (contributions) | outline: proposal for the final contributions (options A/B), no edits
2026-10-26 | Ch. 1.5, Ch. 8, Ch. 2.5, Ch. 7, CLAUDE.md | draft: final contributions (option A, author's decision) applied; Ch. 8 own work threefold; provisional todos removed; CLAUDE.md objectives aligned with Ch. 1.3
2026-10-26 | Ch. 6 figures | script: ch6_main_metrics with joint reference line, ch6_few_shot with equal-updates markers and joint curve (palette slot 6 validated with the dataviz validator); captions updated
2026-10-26 | front matter, all chapters | LaTeX fix: declaration 'fur' -> 'f"ur' (copied text otherwise identical to the chair's); outline: length cut proposal (outlines/length_cut_proposal.md), nothing applied
2026-10-26 | all chapters | outline: list of repeated and low-value passages as first cut candidates (outlines/length_cut_proposal.md), nothing applied
