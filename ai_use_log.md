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
2026-10-26 | Ch. 6.1.2 | LaTeX edit: removed one sentence that duplicated Ch. 4.3 word for word in content (split sizes); other candidates checked and kept (not pure duplicates)
2026-10-26 | Ch. 2 | feedback: counted reviewed/cited works and advised on scope (no edits)
2026-10-26 | Ch. 2 | outline: keep/mention/drop list for the works in Table 2.1 (outlines/ch2_scope_list.md), nothing applied
2026-10-26 | Ch. 2 | explanation: where CoCoOp is cited; corrected stale note in thesis_notes.md
2026-10-26 | Ch. 2 | outline: added CoCoOp as a mention in 2.2 to the scope list
2026-10-26 | Ch. 2 | feedback: rechecked mention list against paper notes; LViT to mention, SAM-Med3D-MoE and CA-SAM to keep, totals corrected (outlines/ch2_scope_list.md)
2026-10-26 | Ch. 2 | feedback: checked scope list against approved tiers (papers/index.csv); MSLoRA-CR to keep; assessed effect on quality
2026-10-26 | Ch. 2 | outline: borderline cases moved to keep (author's decision); proposed changes for 2.1, nothing applied
2026-10-26 | Ch. 2 | draft/LaTeX edit: applied scope list (Table 2.1 45 to 25 rows; mentions condensed; drops removed; new sentences on CoOp/CoCoOp, CA-SAM, SAM-Med3D-MoE, 2.5 precedent)
2026-10-26 | Ch. 2.5 | LaTeX fix: table placement (positioning table first, at its reference; summary longtable on a new page; reference sentence moved)
2026-10-26 | Ch. 2.4.1, Tables 2.1/2.2 | feedback: subsection title, positioning-table columns and both captions reviewed; nothing applied
2026-10-26 | Ch. 2.4.1, Table 2.1 | explanation/feedback: purpose of positioning-table columns, not-stated cells, title alternatives; nothing applied
2026-10-26 | Ch. 2.4, Table 2.1 | LaTeX edit/draft: 2.4.1 renamed with definition sentence; positioning table reduced to 7 columns, caption rewritten
2026-10-26 | Ch. 2 | feedback: short paragraphs after the cut listed with merge/keep recommendation; nothing applied
2026-10-26 | Ch. 2 | LaTeX edit: merged short paragraphs (5 places), two bridge clauses reworded
2026-10-26 | Ch. 2, Table 2.1 | feedback: proposal to replace Aim/Pretrained-ability columns (MedSeqFT transfer test found); nothing applied
2026-10-27 | Ch. 2.5, Table 2.1 | LaTeX edit/draft: Aim column dropped (point moved to 2.5 text), columns renamed Pretrained model / Control task, caption definitions
2026-10-27 | Ch. 2, Sec. 2.x (CL for VLMs), opening sentence | LaTeX fix: rewrote the scenario-criterion sentence to match van de Ven et al. (task identity given / not needed / inferred)
2026-10-27 | Ch. 2.3 | LaTeX edit: reworded the van de Ven scenario sentence (l. 94) for clarity
2026-10-27 | Ch. 2 | LaTeX edit: formal-language pass over the chapter (21 wording changes, no content changes except SAT PENGWIN numbers replacing 'failed almost completely')
2026-10-27 | general | explanation: register of academic language per chapter, from the chair guidelines
2026-10-27 | Ch. 2.4.1 | feedback + LaTeX edit: rechecked the 21 formal-language replacements; corrected one overstatement (Beyond Forgetting model growth)
2026-10-27 | Ch. 3-8 | feedback: scan for informal language (about 10 clear cases), recommendation on timing; nothing applied
2026-10-27 | Ch. 5-8 | LaTeX edit: 10 informal phrasings replaced (numbers from cl_metrics.csv where vague)
2026-10-27 | Ch. 2 | feedback: academic-writing review of the chapter text (issue list, no edits)
2026-10-27 | Ch. 2 (+ Ch. 1 l. 140, abbreviations.tex) | LaTeX edit: fixed the academic-writing issues from the review (abbreviations LoRA/EWC/MLP, percentage points, split long sentences, terminology, search footnote, PA-EWC table locator, % units, cites)
2026-10-27 | Ch. 1 | feedback: academic-writing review of the chapter (issue list, no edits)
2026-10-27 | Ch. 2.3, opening paragraph (scenarios) | LaTeX edit: condensed the van de Ven scenario descriptions from six sentences to three
2026-10-27 | Ch. 2.3, scenario paragraph | LaTeX edit: removed the clause on separate parameters in task-incremental learning (covered by the De Lange sentence and Ch. 7)
2026-10-27 | Ch. 1 (+ Ch. 7/8 term, CLAUDE.md) | LaTeX edit: fixed the academic-writing issues from the review (repetition in 1.1, retraining claim, stability-plasticity claim, terms introduced in 1.4, joint fine-tuning reference moved and term unified, metric and replay citations, long sentences)
2026-10-27 | Ch. 1.4 | LaTeX edit: removed the Chaudhry/intransigence sentence after Adaptation (attribution stays in Ch. 3.4)
2026-10-27 | Ch. 1.1 | LaTeX edit: merged the retraining sentences, dropped the 158-public-datasets clause
2026-10-27 | Ch. 2.3, evaluation paragraph | LaTeX edit: condensed the paragraph on Chaudhry/ZSCL/SPU (11 to 6 sentences, forgetting definition made precise) and moved the ZSCL benchmark sentence to GIFT
2026-10-27 | Ch. 2.3, opening | LaTeX edit: added a two-sentence section opening and moved the evaluation paragraph before the families paragraph
2026-10-27 | Ch. 2.3, opening | LaTeX edit: replaced the two-sentence section opening by one transition sentence
2026-10-27 | Ch. 2.3, scope and outline | feedback: assessed level of detail of the VLM continual-learning review and proposed a revised outline (no edits)
2026-10-27 | Ch. 2.3 / Ch. 3.2 | feedback: assessed whether scenarios, metrics and families belong in Ch. 2 or Ch. 3 (no edits)
2026-10-27 | Ch. 2.3 | LaTeX edit/draft: restructured 2.3 (subsections removed, metrics paragraph removed, numbers cut to those used later, ZSCL/PRIMED teacher contrast, new opening and closing paragraph from author's Q1 answer and Claude-selected Q2 points)
2026-10-27 | Ch. 2.3 / Ch. 3.2 | feedback: whether to remove or move the scenario definitions (no edits)
2026-10-27 | Ch. 2.3 / Ch. 3.2 / Table 2.1 | LaTeX edit: moved scenario definitions from Ch. 2.3 to Ch. 3.2 (one-sentence pointer kept in Ch. 2, positioning only in 3.2), caption reference added
2026-10-27 | Ch. 2.3, replay paragraph | feedback: why only generative replay works are reviewed (no edits)
2026-10-27 | Ch. 2.3, replay paragraph | feedback: whether the replay paragraph can be removed (no edits)
2026-10-27 | Ch. 2.3, replay paragraph | feedback: whether to add, keep or drop replay works (no edits)
2026-10-27 | Ch. 2.3, replay paragraph | LaTeX edit: dropped CGIL, added pointer to real-sample replay in 2.4.1
2026-10-27 | Ch. 2.3, ZSCL/PRIMED paragraphs | feedback: merging the two ZSCL paragraphs, need for PRIMED (no edits)
2026-10-27 | Ch. 2.3, ZSCL paragraph | LaTeX edit: merged the two ZSCL paragraphs into one, SPU sentence made precise (outside the task sequence)
2026-10-27 | Ch. 1, strategies paragraph | LaTeX edit: split the LoRA sentence into three for readability
2026-10-27 | Ch. 2.3, MoE-Adapters / MSLoRA-CR | feedback: whether to demote both to mentions and drop their table rows (no edits)
2026-10-27 | Ch. 2.3 / Table 2.1 | LaTeX edit: MoE-Adapters reduced to a two-sentence mention in the LoRA paragraph, table row removed
2026-10-27 | Ch. 2.3 closing paragraph / Ch. 5 prompt tuning | LaTeX edit: closing paragraph cut to limitations of prior work with pointer to Ch. 5; token-placement reason added to Ch. 5
2026-10-27 | Ch. 2.3 closing paragraph | LaTeX edit: scoped the opening claim to VoxTell, removed the external-data clause
2026-10-27 | Ch. 2.4 | LaTeX edit: renamed the three subsections (starting point and prompt type) and rewrote the roadmap sentence
2026-10-27 | Ch. 2.4 title | LaTeX fix: manual line break in the section title to avoid hyphenation
2026-10-27 | Ch. 2.4 opening paragraph | feedback (opening, length, flow, focus, clarity); no edits
2026-10-27 | Ch. 2.4 opening + 2.4.1 | draft: shortened section opening to bridge + roadmap; moved background-conflict point into 2.4.1 (3 sentences); removed uncited expectation and Liu example
2026-10-27 | Ch. 2.4 opening + 2.4.1 | draft: moved background-shift definition and Liu example back into the section opening; 2.4.1 keeps only the consequence
2026-10-27 | Ch. 2.4 opening | LaTeX edit: removed the roadmap sentence (repeated the subsection titles)
2026-10-28 | Ch. 2, Sec. 2.4.1 | feedback: placement of the ILT/MiB sentence (2.3 vs 2.4), no edits
2026-10-28 | Ch. 2, Sec. 2.4.1 | draft: split regularisation/background-shift paragraph in two, shortened background-shift reasoning, cited ILT baseline use
2026-10-28 | Ch. 2, Sec. 2.4.1 | LaTeX edit: topic sentence reworded to author's wording (regularisation and distillation)
2026-10-28 | Ch. 2, Sec. 2.4.1 | feedback: checked MiB paper for priority claim and term, proposed opening
2026-10-28 | Ch. 2, Sec. 2.4.1 | draft: background-shift paragraph rewritten (MiB first in natural images, P./X. Liu distinguished, no-conflict reasoning)
2026-10-28 | Ch. 2, Sec. 2.4.1 | draft: no-conflict sentence reworded (each mask is the target for one text prompt)
2026-10-28 | Ch. 2, Sec. 2.4.1 | draft: MiB sentences merged, added MiB baseline sentence (Like ILT), 'In medical image segmentation' opening
2026-10-28 | Ch. 2, Sec. 2.4.1 | LaTeX fix: reworded MiB sentence to remove overfull hbox (lines 178-183)
2026-10-28 | Ch. 2, Sec. 2.4.1 (parameter-isolation paragraph, Zhang et al.) | feedback + draft (restructured paragraph)
2026-10-28 | Ch. 2, Sec. 2.4.1 | LaTeX fix: reworded MiB sentence again, overfull hbox gone in XeLaTeX build
2026-10-28 | Ch. 2, Sec. 2.4.1 (Zhang et al. mechanism sentence) | feedback + draft (precision fix: controller, pooled features, class template)
2026-10-28 | Ch. 2, Sec. 2.4.1 (Zhang et al. paragraph) | draft (condensed to 5 sentences, Liu et al. folded into citation)
2026-10-28 | Ch. 2, Sec. 2.4.1 (Zhang et al. results sentence) | feedback + draft (comparison changed from PLOP to pseudo-labelling baseline)
2026-10-28 | Ch. 2, Sec. 2.4.1 (Ranem et al. sentence) | feedback + LaTeX wording fix (elliptical clause made explicit)
2026-10-28 | Ch. 2, Sec. 2.4 (subsection titles, overview sentence) | feedback + draft (parallel titles, split sentence)
2026-10-28 | Ch. 2, Sec. 2.4 overview and 2.4.2 opening | feedback + draft (foundation-model definition with todo cite, opening sentence)
2026-10-28 | Ch. 2, Sec. 2.4.2 (SAM-based methods, RegCL, synthesis) + Table 2.2 row | feedback + draft (trimmed to 8 sentences, control-task link, RegCL removed)
2026-10-28 | Ch. 2, Sec. 2.4.2 synthesis paragraph, Sec. 2.5 | feedback + draft (synthesis paragraph deleted, observation folded into 2.5 as one sentence)
2026-10-28 | Ch. 2, Sec. 2.4.3 (Gao critique paragraph) | feedback + draft (outside-sequence sentence deleted as duplicate of 2.5; test-time sentence completed and merged)
2026-10-28 | Ch. 2, Sec. 2.5 (Summary and Research Gap) | feedback + draft (removed repetitions of Ch. 1: VoxTell number, protocol, k values, references, families; positioning sentence now names the comparison studies)
2026-10-28 | Ch. 2, Sec. 2.5 para 1 | draft (varied the repeated 'X does A, but B' pattern)
2026-10-28 | Ch. 2, Table 2.1 (positioning) | LaTeX fix (column widths rebalanced, caption shortened, short LoT caption, two cells shortened)
2026-10-28 | Ch. 2, Table 2.1 caption | LaTeX fix (caption shortened, control task refers to Sec. 1.4, few-shot footnote; repaired a broken \textsuperscript from an interrupted command)
2026-10-28 | Ch. 2, Sec. 2.5 positioning sentence | draft (adapted methods vs compared strategies; defense todo on meta-net/gradient scaling)
2026-10-28 | Ch. 1 (gap paragraph), Ch. 2 (2.4.1, 2.5), Table 2.2 | draft + terminology fix (precedents for measuring pretrained ability in Ch. 1 and 2.5; 'strategies' -> 'methods' for other authors' work)
2026-10-29 | all chapters, chapter/section openings | feedback (whether outline, chapter and section openings are needed; flagged outline mismatch and stacked headings)
2026-10-29 | all chapters + appendix | feedback (scan of stacked headings: Ch. 1, 3.1, 4.1, 6.1 without lead-in)
2026-10-29 | Ch. 3.1, 4.1, 6.1 | feedback (recommendation for fixing stacked headings)
2026-10-29 | Ch. 3, Sec. 3.1 | feedback + outline (diagnosis of structure and paragraph focus, revised outline proposed)
2026-10-29 | Ch. 3, Sec. 3.1 lead-in + 3.1.1 | draft/restructure (problem setup moved to section level, new 2-sentence lead-in, VoxTell content moved from 3.1.1 to 3.1.3, notation refs retargeted)
2026-10-29 | Ch. 3, Sec. 3.1 lead-in | feedback (generality of the problem-setup paragraph; theta vs frozen text encoder)
2026-10-29 | Ch. 3, Sec. 3.1 lead-in + 3.1.3, notation | draft (problem setup tied to the one-structure setting; theta defined as all VoxTell parameters except the frozen text encoder)
2026-10-29 | Ch. 3, Sec. 3.1 lead-in | language (grammar and clarity: split long sentences, removed subject-verb insertion, linked Z to z_v)
2026-10-29 | Ch. 3, Sec. 3.1 lead-in; Fig. 3.1/5.1 | LaTeX fix (removed pointer sentence to the loss equation) + feedback (loss arrow in VoxTell figure)
2026-10-29 | Fig. 3.1/5.1, Ch. 3 caption | LaTeX fix (removed loss node from shared VoxTell TikZ body, caption adjusted, figures rebuilt)
2026-10-29 | Ch. 3, Sec. 3.1.2 | draft/restructure (VoxTell and implementation remark removed, paragraph split, long sentence split)
2026-10-29 | Ch. 3, Sec. 3.1.3 | draft/restructure (paragraphs reordered to data flow, implementation remarks replaced by one pointer to Ch. 5, link to 3.1.2, fusion/late-fusion and training paragraphs split)
2026-10-29 | Ch. 3, Sec. 3.1 | LaTeX fix (build check after restructuring: no errors, no undefined references)
2026-10-29 | Ch. 3, Sec. 3.1.2 | language (grammar and clarity: inputs of each projection explicit, notation remark moved before the equation, long sentences split)
2026-10-29 | Ch. 3, Sec. 3.1 lead-in | language (removed repeated 'This thesis adapts VoxTell' framing)
2026-10-29 | Ch. 3, Sec. 3.1 lead-in + 3.1.1 | language (repetition removed, U-Net description before the attributed claim, patch/sliding-window sentence split into own paragraph)
2026-10-29 | Ch. 3, Sec. 3.1.3 + Fig. 3.1 caption | language (insertions removed, long sentences and semicolons split, bottleneck defined, ambiguous referents fixed)
2026-10-29 | Ch. 3, Sec. 3.1.3 | feedback + LaTeX fix (verified facts against paper_notes/voxtell.md and code/src/model; corrected the s=0 output sentence and the foreground-sampling wording)
2026-10-29 | Ch. 3, Sec. 3.1.3 | LaTeX fix (deleted late-fusion paragraph on author's decision; tracker note for Ch. 2)
2026-10-29 | Ch. 3.1.3, Ch. 5.3, notation, Table 6.x (script) | terminology fix ('soft Dice' -> 'Dice loss' everywhere; one sentence in Ch. 5 that the Dice term uses probabilities; hparams table regenerated)
2026-10-29 | Ch. 3.1.3, Ch. 5.3 | LaTeX fix (removed Dice-rationale sentence, merged pretraining paragraphs; Ch. 5 states patch size and foreground fraction follow VoxTell pretraining, author-confirmed)
2026-10-29 | Ch. 5.3 (method.tex:175) | feedback (verified 'follow the pretraining of VoxTell' against paper notes, code and run configs; schedule exponent and SGD settings not stated in the paper)
2026-10-29 | Ch. 5.3 (method.tex:175) | feedback (checked nnU-Net v2 and VoxTell repository code for optimiser and schedule defaults; defense point added)
2026-10-29 | Ch. 5.3 (method.tex:175) | draft (optimiser/schedule sentence split: what follows VoxTell, what follows nnU-Net defaults, exponent 1 stated as a choice; todo cite nnU-Net code)
2026-10-29 | Ch. 3.1.3 Fig. 3.1 (background.tex) | feedback + LaTeX/TikZ fix (caption length; figure switched to the paper's version with bottleneck keys/values; caption shortened; pointer sentence rephrased)
2026-10-29 | Ch. 3.1.3 Fig. 3.1 caption (background.tex:134) | LaTeX fix (caption revised for style rules: subject-verb insertion, unclear 'Its', vague verb, \gls{mri}; one statement per sentence)
2026-10-29 | Ch. 3.1.3 Fig. 3.1 (background.tex) | LaTeX fix (float moved and \cref moved to the first sentence of 3.1.3 so the figure is on the page of its reference; compiled and checked p. 25)
2026-10-29 | Ch. 3.1.3 Fig. 3.1 (background.tex) | LaTeX fix (float placement reverted to after the first-reference paragraph, \cref back in "four parts" sentence; figure now top of p. 26; compiled and checked)
2026-10-29 | Ch. 3.2 CL setting paragraphs (background.tex:150-175) | LaTeX fix (language revision: semicolons split, dangling modifier, subject-verb insertion, stage definition, ambiguous appositive/which; control-task sentence made accurate)
2026-10-29 | Ch. 3 structure (background.tex, method.tex 5.1/5.2, notation.tex) | outline + LaTeX restructure (3.2 and 3.3 merged, evaluation matrix moved to 3.3, task-aware inference moved to Ch. 5; compiled and checked)
2026-10-30 | Ch. 3.2 opening (background.tex) | language fix + terminology check (mechanisms -> methods)
2026-10-30 | Ch. 1-3 terminology (introduction.tex, related_work.tex, ch2_sota.tex) + Ch. 3.3 (background.tex) | LaTeX fix ('mechanism' -> method/strategy wording) + draft (joint-training reference, 2 sentences)
2026-10-30 | Ch. 5 title vs. method/strategy terminology | feedback (no edits)
2026-10-30 | Ch. 5.4 (method.tex l. 237) | language fix ('two of its mechanisms' removed)
2026-10-30 | all chapters (background, method, discussion, summary) | terminology pass method/strategy ('mechanism' removed, our work never 'method')
2026-10-30 | terminology ('mechanism') | feedback (no edits)
2026-10-30 | Ch. 5.4.1 (method.tex l. 259) | language fix ('what they add' -> 'their components')
2026-10-30 | Ch. 2.3 (related_work.tex l. 98, 147) | LaTeX/text edit: scenario definition reduced to pointer to Ch. 3.2.1 (avoid duplicate definition)
2026-10-30 | Ch. 3.2.1 (background.tex l. 172-176) | language/clarity edit: scenario positioning paragraph reordered (claim -> reason -> CIL/DIL contrasts)
2026-10-30 | Ch. 3.2.1 -> Ch. 5.1 | restructure: scenario positioning moved to Method setting section, Ch. 3 overview updated
2026-10-30 | Ch. 2.3 (related_work.tex l. 103) | language fix: 'refine these families into' -> 'group methods into' (parameter-efficient adaptation is not a refinement of parameter isolation)
2026-10-30 | Ch. 3.2 (background.tex overview, 3.2.4, 3.2.5) | flow fixes: overview names the four methods and the shared order with Ch. 5.4; CoCoOp sentence linked to prompt-tuning meta-net; ZSCL penalty moved before weight ensemble
2026-10-30 | Ch. 3.2.3-3.2.4, Ch. 5.4.3 | content trim: replay subsection reduced to rehearsal + overfitting + privacy (iCaRL alternative moved to Method replay with defense todo); ZSCL opening shortened (overlap with Ch. 2); 'weight-consolidation loss' named in Ch. 3 to match Ch. 5
2026-10-30 | Ch. 3.2.3 -> Ch. 5.4.3 | restructure: replay subsection removed from Background, overfitting/privacy sentences moved to Method replay; overview list updated
2026-10-30 | Ch. 3.2.3 (background.tex, distillation/ZSCL) | language/clarity edit: temperature attachment, colon split, long ZSCL loss sentence split (Eq. citations per sentence)
2026-10-30 | Ch. 2.3 (l. 114-115, 147), Ch. 3.2 overview/3.2.4 | repetition trim: ZSCL weight-constraint sentence and CPE-CLIP session description in Ch. 2 reduced to pointers; duplicate CoCoOp meta-net sentence removed from Ch. 3, CoCoOp named in overview
2026-10-30 | Ch. 5.4.4 (method.tex l. 352) | LaTeX/text fix: weight ensemble now references eq:bg-we instead of re-describing ZSCL Eq. 7
2026-10-30 | Ch. 3.2.4 (background.tex, prompt learning / CPE-CLIP) | language/clarity edit: semicolons split, bare 'prompt' -> context vectors / prompt tokens, redundant 'CLIP stays fixed' removed, Eq. locators split (2-4 / 6-8)
2026-10-30 | Ch. 5.4.5 (method.tex l. 385, 388) | notation fix: own gradient scale written as max(0.25, beta_t) with cref to eq:bg-cpe-scaling; beta_t keeps its single Ch. 3 definition
2026-10-30 | Ch. 3.3 (background.tex, Evaluation Metrics) | structure/clarity: scope sentence added; Chaudhry accuracy->DSC sentence moved into matrix paragraph; control task and c_j defined in own sentences before Fig. 3.2
2026-10-30 | Ch. 3.3 (background.tex, Evaluation Metrics) | restructure: \paragraph heading per metric with its own equation; joint-training sentences moved into Adaptation paragraph; built and checked pages 31-33
2026-10-30 | Ch. 3.3 (background.tex, Evaluation Metrics) | language/clarity edit: long sentences and semicolons split, subject-verb insertion in Final Forgetting removed, k->i index in Adaptation, caption colon/semicolons split, Transfer definition made precise
2026-10-30 | Ch. 3.3 (background.tex, metric paragraphs) | language edit: 'Higher values are better' removed for the three DSC-mean metrics; direction for Final Forgetting folded into the backward-transfer sentence
2026-10-30 | Ch. 3.3 (background.tex, Adaptation / Final Performance) | structure edit: joint-training definition and De Lange soft upper bound moved from Adaptation to Final Performance; 'Adaptation omits the joint-training reference' removed
2026-10-30 | Ch. 3.3 (background.tex l. 298) | language edit: 'summand' -> 'diagonal entry'
2026-10-30 | Ch. 3.3 (background.tex, Final Forgetting) | content trim: index-convention note and pre-training-stages remark removed, max rationale kept in one sentence; defense point D53 added
2026-10-30 | Ch. 3.3 (background.tex, Final Performance) | language edit: vague 'describes the model that a run delivers' sentence removed; referent made explicit
2026-10-30 | Ch. 3.3 (background.tex, Transfer) | explanation (with seq. FT eval matrix example) + clarity rewrite of last sentence; pointer to pretrained-model reference row
2026-10-30 | Ch. 4 (data_description.tex, all sections) | language edit: grammar and clarity pass (sentence splits, insertions removed, referents made explicit, two caption clarifications); no content added
2026-10-30 | Ch. 4.1 (data_description.tex, section opening) | LaTeX/structure fix: stacked heading resolved, dataset sentence moved into a lead-in plus one draft pointer sentence
2026-10-30 | Ch. 4.1.1 (data_description.tex) | content trim on author's approval: acquisition parameters and pathology breakdown removed, annotator sentences merged
2026-10-30 | scripts/plot_data.py, Table 4.1 | script: hospital name capitalised, Ch. 4 tables/figures regenerated
2026-10-30 | Ch. 4.2 + Ch. 3.3/5.1 refs, scripts/plot_data.py | structure/LaTeX fix on author's approval: Table 4.2 and Fig. 4.1 removed, text prompts listed in prose, script prints medians instead
2026-10-30 | Ch. 4.1 Fig. 4.1, scripts/plot_data.py | script + caption edit: example figure at 600 dpi, opaque labels, cropped knee panels, lung outline, legend fixed; caption extended
2026-10-30 | Ch. 4.1 Fig. 4.1 | script + caption edit: lung as opaque fill; explanation of coronal blur from SKM-TEA App. A.1-A.2 (ZIP2 zero-padding)
2026-10-30 | Ch. 4.1.1 + Fig. 4.1 caption | draft sentence (acquired slices, ZIP2 zero-padding, Desai App. A.1-A.2) and caption clause on coarse slice direction; only source numbers
2026-10-30 | Fig. 4.1 + Ch. 1 setting figure | script: lung colour changed to #b5179e (validated with dataviz palette checker), figures regenerated
2026-10-30 | Fig. 4.1 + Ch. 1 setting figure | script: meniscus colours reassigned (validated pairwise for touching structures), figures regenerated
2026-10-30 | Fig. 4.1 + Ch. 1 setting figure | script: lung and lateral-meniscus colours swapped, figures regenerated
2026-10-30 | Ch. 4.1.1 (data_description.tex) | draft: annotation files defined, voxel-size sentence simplified, slice breakdown and zero-padding sentence removed
2026-10-30 | Ch. 4.1.1, 4.2 (data_description.tex) | edit: duplicate size/spacing numbers removed from text (kept in Table 4.1), redundant reason sentence removed
2026-10-30 | Ch. 4.1.1, 4.2 + literature.bib | bibliography: two entries added via bib-entry-adder (DATASET.md, AeroPath Zenodo record), URL footnotes replaced by \cite
2026-10-30 | thesis_main.tex preamble + literature.bib | LaTeX fix: British bibliography dates (biblatex language=british, backref strings kept), version and month fields fixed
2026-10-30 | thesis_main.tex preamble | LaTeX fix reverted: British bibliography dates removed on author's request
2026-10-30 | Ch. 4.1 Fig. 4.1 caption | language edit: caption shortened (structure lists removed, orientation and resolution notes kept)
2026-10-30 | Ch. 4.1 (+ refs in Ch. 3, 5, 7) | structure edit: subsections merged, dataset-choice paragraph moved to section start and shortened, size paragraph reduced to one sentence
2026-10-30 | Ch. 4.1 (dataset choice) | language/content edit: interpretation and VoxTell-conflict sentences removed, one position from Suppl. Table 10
2026-10-30 | Ch. 4.1 (VoxTell training labels) | fact check against VoxTell PDF Table 10; inferred 'two knee MRI datasets' clause removed, citation narrowed
2026-10-30 | Ch. 4.1 | edit: VoxTell training-label sentence moved from the dataset-choice paragraph to the tasks paragraph, reworded with the tasks as subject
2026-10-30 | Ch. 4.1 | edit: acquisition and distribution paragraphs merged (no rewording)
2026-10-30 | Ch. 4.1 | edit: licence sentences moved into the opening paragraph (after the dataset choice), mirroring Sec. 4.2
2026-10-30 | Ch. 4.3 + scripts/plot_data.py | structure edit: splits table removed, cross-tab printed by the script, sentence keeps the 7/24 figure
2026-10-30 | Ch. 4.2 (AeroPath) | content trim on author's approval; VoxTell Table 7/10 locators verified in the PDF, ranking claim replaced by label counts
2026-10-30 | Ch. 4.2 (AeroPath) | edit: VoxTell lung count stated as training cases for the label 'lung' only (Table 10 caption: training case frequency)
2026-10-30 | Table 4.1 + scripts/plot_data.py | script: row 'Volumes used' renamed 'Volumes'; verification from results/ that only the 4 AeroPath test volumes were used in the reported runs
2026-10-30 | Ch. 4.2, 4.6 | edit: undocumented lung-label origin stated once (4.6), with the sources checked; duplicate sentence in 4.2 removed
2026-10-30 | Ch. 4.2 (AeroPath) | edit: two paragraphs merged (no rewording); section kept
2026-10-30 | Ch. 4.3 (data splits) | language edit + stale-fact fix (checkpoint selection per Method), AeroPath usage sentence moved into the split paragraph
2026-10-30 | Ch. 4.3 (official split) | draft: paragraph rewritten from the author's stated reason (no invented motivation); AeroPath paper checked for an official split; D3 updated
2026-10-30 | Ch. 4.3 (split procedure) | language edit: three sentences merged into two, fractions stated once
2026-10-30 | Ch. 4.3 (few-shot subsets) | language edit: active voice, colon construction removed, two sentences made specific
2026-10-30 | Ch. 4.4 (preprocessing) | language edit: label-map description stated once (checked against code/scripts/h5_to_nifti.py), unclear 'Its' fixed, ITK-SNAP clause removed
2026-10-30 | Ch. 4.4 (last sentence) | language edit: subject first, sentence opens with \Cref
2026-10-30 | Ch. 4 (Sec. 4.5 dissolved) + discussion.tex ref | structure edit: data-quality facts moved to 4.1/4.2/4.4, Sec. 4.5 removed, setup limitations pending for 7.3
2026-10-30 | Ch. 7.3 (discussion.tex) | draft: setup/model limitations and pretrained-DSC comparison moved from former Sec. 4.5 into existing paragraphs (author-approved text), two items dropped
2026-10-30 | Ch. 4.4 (plans.json footnote) | edit: redundant data identifier removed from footnote
2026-10-30 | Ch. 5 (all sections) | language edit: grammar and clarity (long sentences split, insertions removed, referents clarified, intransigence index k -> i), no content change
2026-10-30 | Ch. 5 (opening sentence) | language edit: vague 'what we built ... and why' replaced
2026-10-30 | Ch. 5 (opening paragraph) | language edit: section overview split, one verb per item, 'built on this procedure' clarified, pointer sentence split
2026-10-30 | Ch. 5 (opening sentence) | language edit: 'each design choice' weakened to 'the main design choices' (not every choice has a recorded reason)
2026-10-30 | Ch. 5.1 (first two paragraphs) | edit: sentences repeating Ch. 1/3/4 removed; not-domain-incremental point moved to the scenario paragraph, definition not repeated
2026-10-30 | repo | added backups/ and LaTeX build files to .gitignore, untracked them from the index (files kept on disk) (script)
2026-10-30 | Ch. 1-8, Table 2.2 | citation pass: verified every \cite against paper texts/notes; fixed 8 inaccurate or over-strong claims; removed about 85 repeated citations (299 -> 216 citation commands); page locators to section locators; 2 missing ZSCL citations added; citation rule proposed in thesis_notes.md (feedback/LaTeX fix)
2026-10-30 | Ch. 6, Appendix A | number check: every number in Ch. 6 text, tables and Appendix A recomputed independently from results/hpc/experiments (configs, eval matrices, eval/run/SLURM logs); issue list to the author, no thesis edits; thesis_notes.md §2 TIL-LoRA order entry corrected (script/feedback)
2026-10-30 | Ch. 6, Ch. 7.3 (one count), Table 6.1, App. A captions | LaTeX fix: corrected the number issues of the Ch. 6 check (task-specific LoRA order statement, time/memory summary, joint epoch time, Transfer comparison rule, comparison count 34/152 -> 49/182, interval sign, rank/femoral/few-shot wording); 'joint fine-tuning' and 'per structure' in the generating scripts, tables regenerated (LaTeX fix/script)
2026-10-30 | Ch. 6.1.4, 6.5 | LaTeX fix: joint fine-tuning comparison rule aligned with the other strategies (few-shot vs full split); joint k = 10 vs 5 made descriptive; decision recorded in thesis_notes.md (LaTeX fix)
2026-10-31 | Ch. 1-7, App. A | cross-reference cleanup: removed 100 unnecessary \cref/\ref (repeats, references next to a citation, back-references to just-read definitions, Ch. 2.5 recap references); 4 sentences reworded or deleted to fit (LaTeX fix)
2026-10-31 | whole thesis | cross-reference check against chair/CLAUDE.md rules (float references, sentence-start \Cref, hard-coded numbers, undefined labels, appendix references, rendered names); Ch. 2.5 \tablename~\ref -> \Cref for consistency (LaTeX fix)
2026-10-31 | Ch. 1, 2, 5, 6, 7 | cross-reference pass 2: removed 18 optional references, contribution 3 points to Ch. 6, Silva-Rodríguez section reference replaced by citation, two wrong references corrected (LaTeX fix)
2026-10-31 | Ch. 5.3, 6.1.3 | draft: one sentence in 5.3 on the per-task seed of the validation patches (verified in code/); 6.1.3 reference to 5.3 restored (draft/LaTeX fix)
2026-10-31 | Ch. 5.1, notation | draft: task-order and few-shot paragraphs merged (repeats of Ch. 1/4/6 removed), control-task paragraph shortened, reason now VoxTell's reported AeroPath lung DSC instead of our result, public availability as reproducibility; notation row D_c^tr removed (control task has no training set) (draft/LaTeX fix)
2026-10-31 | Ch. 5.1, 5.4.2, CLAUDE.md | LaTeX fix/draft: scenario paragraph rewritten (reasons for not CIL/DIL per van de Ven Sec. 2.4), parameter-selection sentence moved to 5.4.2 ('beyond the text prompt'), term 'task-aware inference' dropped (unused); CLAUDE.md terminology entry updated
2026-10-31 | Ch. 3.2.1, 5.1, 5.2 | LaTeX fix: protocol-variables paragraph moved from 5.1 to 5.2 (after the protocol definition), referent of 'Each entry' made explicit; D_t -> D_t^tr in 3.2.1 (one symbol per quantity)
2026-10-31 | Ch. 5 Method | feedback: structural diagnosis of the chapter (focus of Sec. 5.2, ordering, scattered complexity), no edits
2026-10-31 | Ch. 5 Method | outline: from-scratch restructure proposal (protocol after strategies, model section split off, single complexity section), no edits
2026-10-31 | Ch. 5 Method | outline: revised restructure proposal (merge model and adaptation sections, single algorithm for the whole run in the protocol section), no edits
2026-10-31 | Ch. 5 Method | outline: restructure proposal revised (setting and protocol merged, algorithm at end of strategies, 4 sections), no edits
2026-10-31 | Ch. 5 Method | outline: consolidated restructure outline with assessment of remaining weaknesses, no edits
2026-10-31 | Ch. 5 Method | outline: options for algorithm placement (protocol-level algorithm in 5.1 vs one complete-run algorithm after the strategies), no edits
2026-10-31 | Ch. 5 Method, Ch. 3.3 | feedback: remaining weaknesses of the restructure outline (protocol definitions split between Ch. 3.3 and Ch. 5.1), no edits
2026-10-31 | Ch. 5.2 (protocol), outline | draft: equal-updates principle in run-variables paragraph; LaTeX fix: joint fine-tuning settings pointer; outline v2 saved (outlines/ch5_method.md)
2026-10-31 | Ch. 5.1, Ch. 6 captions | feedback: task-specific LoRA Final Forgetting check (eval matrices), review of 5.1 outline, no edits
2026-10-31 | Ch. 5.1, 5.3 (5.4.2), Ch. 3.3, Ch. 6 captions, refs | LaTeX fix/draft: Sec. 5.1 restructured (setting + protocol, new algorithm paragraph, run-count sentence), task-specific LoRA evaluation paragraph moved and corrected (Final Forgetting not zero by construction), Ch. 3.3 control-task sentences, captions, labels and references updated; built
2026-10-31 | Ch. 5.1 | feedback: subsections vs one section for 5.1, no edits
2026-10-31 | Ch. 5.1, refs | LaTeX fix: subsections 5.1.1/5.1.2 removed, references in Ch. 1, 3, 6, 7, 8 and notation retargeted to sec:method-setting-protocol; built
2026-10-31 | Ch. 5.1 | feedback: options for a shorter section title, no edits
2026-10-31 | Ch. 5 opening, 5.1 title | draft/LaTeX fix: 5.1 title shortened to 'Setting and Evaluation Protocol'; opening split into shorter sentences, 'strategy' scope stated (baseline + five CL strategies; 'strategies' covers all six), not built
2026-10-31 | Ch. 5 opening | draft: strategy scope folded into the 5.3 sentence ('six strategies ... sequential fine-tuning, which serves as the baseline, and five continual-learning strategies'), meta-sentence removed, not built
2026-10-31 | CLAUDE.md terminology | strategy entry: six approaches incl. the baseline; 'continual-learning strategy' = the five
2026-10-31 | Ch. 5.2, Ch. 6 caption | LaTeX fix/draft: Sec. 5.2 restructured (retitle, intro naming the strategy steps, paragraph split, parameter counts moved from 5.3.1, 24th-epoch sentence removed, cost paragraph moved to 5.4); caption references updated; not built
2026-10-31 | Ch. 5.2 | LaTeX fix: section title reverted to 'Adapting VoxTell to One Task' (author)
2026-10-31 | Ch. 5.3, Ch. 6.1.3 | LaTeX fix/draft: Sec. 5.3 restructured (cost paragraphs moved to 5.4, replay subsection renamed, resume and ablation-run sentences removed, alpha/dropout caveat moved to Ch. 6.1.3, opening sentence shortened); not built
2026-10-31 | Ch. 5.4 | draft/LaTeX fix: complexity section condensed to three paragraphs (numbers checked in compute.csv, momentum-buffer claim checked in code), Table 5.3 caption sentence added; chapter restructure complete, built
2026-10-31 | Ch. 5.1 | LaTeX fix: section title changed to 'Evaluation Protocol' (matches Contribution 1; author approved), not built
2026-10-31 | Ch. 5.1 | language: Select sentence on task-specific LoRA split in two, control-task case (no adapter) added to match Sec. 5.3.2, not built
2026-10-31 | Ch. 5.1 | language: algorithm paragraph, Evaluate sentence names a_{i,j}/c_j, Select sentence for task-specific LoRA states pretrained parameters + adapter, not built
2026-10-31 | Ch. 5.1 | language: Select sentence reworded ('determines which parameters are used to evaluate task i after stage j'), not built
2026-10-31 | Ch. 5.1 | language: joint fine-tuning comparison, 'Final Performance, overall and per structure' -> 'Final Performance, on the final DSC of each structure' (Final Performance defined as mean only), not built
2026-10-31 | Ch. 5.2 opening | language: 'VoxTell as we use it' garden path fixed; 'changes this procedure in three steps' -> 'can change at three points', one sentence naming what Init/ExtraData/ExtraLoss do (checked against Alg. 5.2), not built
2026-10-31 | Ch. 5.2 opening | language: 'these steps' -> 'these changes'; built, paragraph checked on rendered page 44, no warnings from it
2026-10-31 | Ch. 5.2 | feedback/LaTeX fix: implementation properties checked against official VoxTell repo; paragraph opening reworded (released implementation, only stage-4 memory contradicts Eq. 3), thesis_notes.md updated, not built
2026-10-31 | Ch. 5.2 | LaTeX fix: stage-4 sentence reworded (released model vs Eq. 3) + justification sentence; checkpoint evidence (pos_embed buffer, strict load) recorded in thesis_notes.md, not built
2026-10-31 | Ch. 5.2 | LaTeX fix: Fig. 5.1 moved after its first reference and set to [p] (now on p. 45, next to the architecture text); accidental URL paste on 'Every' (l. 126) reverted; built
2026-10-31 | Ch. 5.2 | LaTeX fix: implementation paragraph shortened (100.7 M difference dropped, four sentences repeating Ch. 3.1.3 cut, 'text encoder frozen in every strategy' kept), not built
2026-10-31 | Ch. 5.2 | LaTeX fix: built and checked rendered p. 44-45 after paragraph cut (no errors, Fig. 5.1 still on p. 45)
2026-10-31 | Ch. 5.2 | language: frozen-text-encoder sentence moved before the parameter count (author's choice), not built
2026-10-31 | Ch. 5.2, Ch. 6.1 | LaTeX fix: batch-size/epoch reason moved from 5.2 to 6.1 and corrected to match measured run times (author's option a); two author todos resolved; tracker D18 updated, not built
2026-10-31 | Ch. 5.2 | feedback: Eq. method-seg-loss checked against code/src/training/losses.py and trainer.py (BCE mean + MONAI DiceLoss, weights 1:1, no deep supervision); correct, no edit
2026-10-31 | Ch. 5.2 | language: loss intro sentence tightened (equal weights stated; symbols no longer redefined, refers to Ch. 3); equation kept, not built
2026-10-31 | Ch. 5.2 | LaTeX fix: Fig. 5.1 caption shortened (skip sentence and 'for illustration' cut, legend pointer merged, one sentence per line); built
2026-10-31 | Ch. 5.2 | language: notation pointer before loss equation set in parentheses, not built
2026-10-31 | Ch. 5.1, 5.2, 6.1 | LaTeX fix: evaluation-inference paragraph moved from 5.2 to 5.1 (replaces forward reference), Table 6.2 caption refers to 5.1 and 5.2; built
2026-10-31 | Ch. 5.2 | language: optimiser paragraph tightened (linear/exponent-1 and patch-size repetitions removed, N_t definition merged), not built
2026-10-31 | Ch. 5.2 | LaTeX fix: E and eta_0 defined at first use in the schedule sentence (E definition lost in earlier edit), not built
2026-10-31 | Ch. 5.2, Ch. 6.1 | LaTeX fix: provenance of optimiser values (VoxTell pretraining, nnU-Net defaults, exponent 1) moved from 5.2 to 6.1.3 next to Table 6.2; built
2026-10-31 | Ch. 5.2 | language: definition of U split from the schedule sentence, not built
2026-10-31 | Ch. 5.2 (Fig. 5.1), Ch. 1, Ch. 3 | LaTeX fix: Fig. 5.1 caption refers to the example volume of Fig. 4.1 instead of naming test volume MTR_005; Fig. 1.1 and Fig. 3.1 captions checked, no change; built
2026-10-31 | Ch. 5.2 (Fig. 5.1), Ch. 1, Ch. 3 | LaTeX fix: Fig. 5.1 caption refers to the example volume of Fig. 4.1 instead of naming test volume MTR_005; Fig. 1.1 and Fig. 3.1 captions checked, no change; build hit a corrupted .aux (concurrent write), clean after rebuild
2026-10-31 | Ch. 5.2 (Fig. 5.1) | LaTeX fix: caption back to 'in an SKM-TEA volume' (author-approved wording), volume ID kept as source comment; built
2026-10-31 | build | LaTeX fix: build broken by OneDrive sync (null bytes in .aux, *-SAVE-ERROR files); generated files cleaned (latexmk -c) and rebuilt, clean (147 pages)
2026-10-31 | Ch. 5.2 (validation/checkpoint paragraph) | feedback + draft: compressed paragraph (7 -> 4 sentences), moved defense todo to Ch. 6 component evaluations
2026-10-31 | Ch. 5.2 (Fig. 5.1) | LaTeX fix: caption 'layout adapted from' -> 'adapted from' (CLAUDE.md rule), 'not a prediction' added as in Fig. 3.1, not built
2026-10-31 | Ch. 5.2 | LaTeX fix: Algorithm 2 source moved before the training paragraph; now on p. 46 inside Sec. 5.2 (was p. 47, after Sec. 5.3 started); built
2026-10-31 | Ch. 5.2 (opening, patches, optimiser, closing) | feedback + interview + draft: framing of the shared procedure (author's confirmed reasons), hook points moved to section end, batch-size caveat, deviation reasons
2026-10-31 | Ch. 5.2 (implementation paragraph, Alg. 5.2, iterations sentence) | LaTeX/draft fix: stated where the strategies act, split stage-4 sentence, text-encoder sentence merged, N_t in Alg. 5.2
2026-10-31 | Ch. 5.2 (whole-section pass) | feedback + draft: weakened shared-procedure claim, pretraining settings listed once in the opening, batch-size reason aligned with Ch. 6 and moved to optimiser paragraph, duplicate prompt sentence removed
2026-10-31 | Ch. 5.2 (second whole-section pass) | draft fix: merged purpose of shared procedure into l. 121, referent of 'same learning rate' fixed, wording 'in any strategy'
2026-10-31 | Ch. 5.2 (restructure) | outline v3 + reorder: one-sentence scope, procedure paragraph with the three steps and settings principle placed before Alg. 5.2, closing paragraph removed, duplicate clause cut
2026-10-31 | Ch. 5.2 (language pass) | language edit: grammar, tier-1 fixes, cuts of repeated wording; no content change
2026-10-31 | Ch. 5.2 (procedure paragraph) | LaTeX/draft fix: deleted signpost sentence before Alg. 5.2
2026-11-01 | Ch. 6.2, 7.3, 7.4 (replay framing) | feedback + draft: replay counted as one of the six strategies in Ch. 6.2 and three captions; sentences added to Ch. 7.3 (replay scope, cost) and 7.4 (data storage)
2026-11-01 | Ch. 5.3 (Table 5.1) | feedback + LaTeX fix: table moved to the end of 5.3 with a one-sentence reference; caption corrected (wrong claim about the next task's start for task-specific LoRA removed, "strategies" instead of "continual-learning strategies", columns explained)
2026-11-01 | Ch. 5.3 (opening paragraph) | language edit: grammar and clarity, tier-1 fixes (referent of 'Replay', parentheses, semicolon split), unsupported 'best suited' replaced by a stated reason with author todo
2026-11-01 | Ch. 1.3, 1.5 (objectives vs contributions) | feedback: overlap between objectives, Approach and Scope and contributions diagnosed; options offered, no edits
2026-11-01 | Ch. 1.5 (contributions) | feedback: recommendation (option 1, four contributions one per objective, trim Sec. 1.4) with proposed wording; no edits
2026-11-01 | Ch. 1.4, 1.5 (contributions) | draft: four contributions (one per objective) without repeated detail; Sec. 1.4 update counts and bootstrap detail removed; CLAUDE.md, thesis_notes, tracker updated
2026-11-01 | Ch. 1.3, 1.5 (objectives vs contributions) | feedback: whether either list can be dropped, checked against supervisor guidelines; no edits
2026-11-01 | Ch. 6.1 (Table 6.1) | script: make_setup_tables.py lists shared LoRA + replay in the comparison row; table regenerated
2026-11-01 | Ch. 5.3 | explanation: options for the reasons for choosing LoRA and random replay (suggestions, not drafted); LaTeX fix: Table 5.1 float moved so it stays in Sec. 5.3; thesis built
2026-11-01 | Ch. 1.3, 1.5 (objectives, contributions) | feedback: quality diagnosis (terms before introduction, vague objects, term mismatch, patellar diagnosis mapping) and proposed rewrite; no edits
2026-11-01 | Ch. 5.3.2, 5.3.3 | draft: reasons for choosing LoRA and random replay samples (from options accepted by the author); author todo on replay replaced by a defense todo
2026-11-01 | Ch. 1.3, 1.5 (objectives, contributions) | draft: objectives reworded as questions without terms introduced later, contributions as deliverables with means; patellar diagnosis moved to C2; CLAUDE.md, thesis_notes, tracker updated
2026-11-01 | Ch. 8 (para 2, own work) | draft: own-work paragraph aligned with the four contributions; 'these runs' referent fixed; tracker updated
2026-11-01 | Ch. 5.3.1 (sequential fine-tuning) | language edit: grammar and clarity; vague 'restriction of the parameters' and overclaiming last sentence ('shows the effect of their components') rewritten
2026-11-01 | Ch. 5.3.2 (LoRA) | language edit: grammar and clarity; semicolons split, appositive and long code sentence rewritten, q/v reason moved next to the cross-attention reason, reason for LoRA as its own paragraph
2026-11-01 | Ch. 5.3 (review fixes) + Ch. 1, 8, tables, scripts | diagnosis + LaTeX fix/draft: subsections 5.3.4/5.3.5 swapped and one strategy order applied in Ch. 1, 5, 6, 8, notation and generated tables (scripts make_setup_tables.py, make_results_tables.py); Table 5.1 reference in the opening; paragraph reorders in 5.3.2/5.3.3; gradient-scale floor as fifth CPE-CLIP difference (author todo); ensemble wording; parameter pointer; De Lange baseline sentence; replay configuration sentence; semicolon splits; thesis built
2026-11-01 | Ch. 5.3.2 (LoRA) | feedback + language edit: six sentences cut or merged (repeat of Ch. 3 B-initialisation, unchanged-modules list, code-split detail, duplicate CLIP-LoRA mention, restated main difference, duplicate 'zero by construction')
2026-11-01 | Ch. 5.3 (opening) | language edit: Table 5.1 reference shortened; duplicate pointer to parameter values cut (already in chapter opening and Sec. 5.2)
2026-11-01 | Ch. 5.3.2, 6.1.4, 6.2, 7.3, 8 (task-specific LoRA forgetting) | LaTeX fix/draft: run result moved from Ch. 5 to Ch. 6.1.4 (Final Forgetting at most 0.0016, only patellar, verified in cl_metrics.csv and eval matrices); 'Final Forgetting zero by construction' / 'forgets nothing' corrected in Ch. 6, 7, 8
2026-11-01 | Ch. 5.3.3 (replay) | feedback + language edit: replay definition and selection criteria now refer to Ch. 2 instead of repeating it (iCaRL sentence cut), overfitting sentence cut, M_t defined, capacity not reached stated, double 'same' and passive 'therefore' fixed
2026-11-01 | Ch. 5.3.4 (prompt tuning) | feedback + language edit: CPE-CLIP description cut (in Ch. 3), CoCoOp sentence points to Ch. 3, ablation sentence turned into the reason for keeping gradient scaling, base-session clause split, naming sentence corrected (meta-net holds most parameters)
2026-11-01 | Ch. 5.3.4 (prompt tuning notation) | LaTeX fix: m and psi defined at first use, layer query q_l introduced (q is the text query of Ch. 3), GELU abbreviation added, notation-table row for q_l
2026-11-01 | Ch. 5.3.2, 5.3.4 + literature.bib | bibliography: three entries added at the author's request (Glorot & Bengio 2010, He et al. 2015, Hendrycks & Gimpel 2016; fields from PMLR, CVF Open Access/mlanthology, arXiv), cited for Kaiming/Xavier initialisation and GELU; thesis built
2026-11-01 | Ch. 5.3.4 (token placement) | explanation (why convolution has no token sequence) + draft: reason for placing the learned prompt tokens rewritten (convolutional image encoder; text encoder run without gradients, verified in code)
2026-11-01 | Ch. 5.3.4 (token placement) | feedback + draft: removed sentence repeating the prompt-decoder/cross-attention placement (l.314, l.316, l.265); reason condensed to two sentences
2026-11-01 | Ch. 5.3.4 (token placement) | feedback + draft: dropped the exclusivity claim ('only part of VoxTell'); reason stated as why the tokens are not in the encoders
2026-11-01 | Ch. 5.3.4 (parameter count) | feedback + draft: parameter count made checkable (meta-net width from code, formula 3d^2+2d, values m=2, L_p=3 with table reference)
2026-11-01 | Ch. 5.3.2, 5.3.4, 5.4 | feedback + draft: removed parameter-count sentences duplicated by Table 5.2 and Table 6.x; meta-net hidden width added to its definition; added the missing in-text reference to Table 5.2 and the measured parameter counts to the pointer to the compute table
2026-11-01 | Ch. 5.3.4 | LaTeX/prose move: sentence on untuned m and L_p moved to the token paragraph
2026-11-01 | Ch. 5.3.4, 5.4, Table 5.2 | feedback (checked tokens/meta-net against code) + draft: tokens act on keys/values, meta-net on query, stated separately; carry-over of layer-L_p tokens to later layers described; complexity table and Sec. 5.4 sentence adjusted
2026-11-01 | Ch. 5.3.4 (differences from CPE-CLIP) | feedback + draft: five-point difference list compressed to what is kept/dropped/added (repeated points removed); 0.25 lower bound and its todo moved to the gradient-scaling paragraph; figure 5.x kept unchanged
2026-11-01 | Ch. 5.3.4 (gradient scaling) | feedback + draft: removed restatement of CPE-CLIP's scaling targets (in Ch. 3) and merged into one sentence; dropped repeated 'not part of CPE-CLIP'
2026-11-01 | Ch. 5.3.4 (differences from CPE-CLIP) | feedback + draft: difference paragraph removed (contrast already in P1-P3); lower-bound origin and naming reason merged into the gradient-scaling paragraph
2026-11-01 | Ch. 5.3.5 | feedback (checked against code, Ch. 3, ZSCL notes) + draft: subsection restructured (difference list folded into the paragraphs of each design choice), wrong 'stage 4 coarsest' claim removed, ZSCL App. B reason for I_we added; 5.3.4 0.25 todo changed to defense
2026-11-01 | Ch. 8 (l.23) | LaTeX fix: wrong 'coarsest decoder stage' replaced (stage 4 is not the coarsest)
2026-11-01 | Ch. 5.3.5 (weight ensemble) | explanation (I_we counted per epoch; ensemble not reset across tasks, from code) + draft: ensemble update and task-boundary sentences reworded, naming sentence rewritten; todo to check ZSCL's behaviour
2026-11-01 | Ch. 5.3.5 (weight ensemble) | explanation + draft: checked ZSCL paper (silent) and official code (ensemble restarted per task, next task trained from ensemble); todo completed with the difference and a defense todo
2026-11-01 | Ch. 5.3.5, 6.x (l.283), 7 (l.174) | draft: ZSCL ensemble difference stated neutrally in 5.3.5; Ch. 6 caveat and Ch. 7 list of adaptations aligned
2026-11-01 | Ch. 5.3.5 (weight ensemble) | draft: ensemble paragraph shortened from nine to six sentences
2026-11-01 | Ch. 5.3/5.4, Tables 5.1/5.2 | LaTeX + draft: Tables 5.1 and 5.2 merged into one overview/cost table; Sec. 5.4 trimmed to the essentials (protocol cost, adaptation cost, memory, storage, pointer to measured values); compiled (0 errors, 0 undefined refs, 17 pre-existing overfull boxes; OneDrive-corrupted aux files cleaned)
2026-11-01 | Ch. 5.3, Table 5.1 | LaTeX: column 'stored after T tasks' dropped (storage growth stated in Sec. 5.4), caption adjusted; compiled (0 errors, 0 undefined refs, 17 pre-existing overfull boxes; OneDrive-corrupted aux cleaned)
2026-11-01 | Ch. 5.4 | LaTeX: unused tables/ch5_complexity.tex deleted (merged into Table 5.1)
2026-11-01 | Ch. 5.3, Table 5.1 | feedback + LaTeX: headers clarified (|phi|, parameters at the start of task t, added data or loss, added time and memory), 'all prompt-decoder layers', teacher-copy cell reworded, task~t-1 tied; compiled clean (0 errors, 0 undefined refs, 17 pre-existing overfull boxes)
2026-11-01 | Ch. 5.3/5.4, Table 5.1 | feedback: redesign options for Table 5.1 and whether per-strategy cost belongs in the table or in Sec. 5.4 prose (recommendation: table by the strategy-specific algorithm steps, cost in prose + Table 6.10); no thesis edits
2026-11-01 | Ch. 5.2-5.4, Table 5.1 | feedback: which of the five problems found with Table 5.1 to fix and how (proposals, no edits)
2026-11-01 | Ch. 5.2-5.4, Table 5.1, notation | draft + LaTeX: Table 5.1 rebuilt by algorithm steps (cost column removed), gradient factor xi in Alg. 5.2 and text, P dropped, momentum sentence and per-strategy additions in Sec. 5.4, Select_S; built clean
2026-11-01 | Ch. 5.3, Table 5.1 | draft + LaTeX: all table cells written out (no '--'), caption rewritten in full sentences and shortened; built clean
2026-11-01 | Ch. 5.3, Table 5.1 | draft + LaTeX: Select column dropped, '--' for nothing added, caption sentence on Sec. 5.2 parameter counts corrected, 5.3 opening refers to Alg. 5.2 only; built clean
2026-11-01 | Ch. 5.4 | draft: generic cost symbols kappa, kappa_S removed (complexity stated as iterations per task), teacher-pass and prompt-token sentences corrected; notation table updated
2026-11-01 | Ch. 5.3, Table 5.1 | feedback: whether Table 5.1 is a summary of Sec. 5.3 and what follows for its role and placement; no edits
2026-11-01 | Ch. 5.3, Table 5.1 caption | feedback: whether the caption should call the table a summary (no); no edits
2026-11-01 | Ch. 5.4 | explanation (LoRA forward/backward/inference merge, checked in code) + draft: LoRA cost sentence corrected to forward and backward pass
2026-11-01 | Ch. 5.3/5.4, Table 5.1 | feedback: placement of Table 5.1 checked in the PDF (floats into Sec. 5.4, 5 pages after its first reference); fix proposed, no edits
2026-11-01 | Ch. 5.4 | draft: sentence on the cost of the LoRA/prompt additions shortened (claim + reference to Ch. 6, no colon reveal)
2026-11-01 | Ch. 5.3.5, Table 5.1 | LaTeX: float source moved up two paragraphs so the table appears in Sec. 5.3 (p. 52) instead of Sec. 5.4; built clean
2026-11-01 | Ch. 5 (all sections) | feedback: list of passages that could be cut or tightened (no edits)
2026-11-01 | Ch. 5.1-5.3 | feedback: proposed wording for six cuts of repeated sentences (no edits)
2026-11-01 | Ch. 5.2, Table 6.x hparams, notation | draft + script: Eq. 5.1 (segmentation loss) replaced by one sentence; Dice smoothing 1e-5 moved to ch6_hparams via make_setup_tables.py (with code check); epsilon removed from notation
2026-11-01 | build | LaTeX fix: diagnosed failing latexmk build (OneDrive SAVE-ERROR on .bbl/.bcf); rebuild succeeded, no source changes
2026-11-02 | Ch. 6 opening + Sec. 6.1 | feedback: diagnosis of grammar, clarity, flow and repetition across chapters, with proposed wording (no edits)
2026-11-02 | Ch. 6 opening + Sec. 6.1, Sec. 6.2 (moved paragraph), Table 6.1 script, method.tex l. 214 | draft + script: applied the approved revision (correctness fixes, restructure of 6.1.3, cuts of repetition)
2026-11-02 | Ch. 6.1, Ch. 7 l. 151 | LaTeX fix: removed stacked heading (subsection 'Overview of the Experiments' merged into Sec. 6.1 opening); reference repointed to Table 6.1
2026-11-02 | Ch. 6.1, Table 6.1 | script + LaTeX fix: Table 6.1 compacted from 9 to 7 rows (make_setup_tables.py: replay+scaling and few-shot+equal-updates merged), moved after the first paragraph of 6.1.1 so it floats next to its citation; build fixed (OneDrive SAVE-ERROR, latexmk -c)
2026-11-02 | Table 6.1 | script: rows reordered by reporting section (6.2 comparison, components, joint; 6.3-6.6)
2026-11-02 | Ch. 6.2, Table 6.1 | LaTeX fix + script: Sec. 6.2 paragraphs reordered (joint fine-tuning, then replay, weight ensemble, gradient scaling, then checkpoint selection; no text changed); weight ensemble added to the components row; rows: comparison, joint, components
2026-11-02 | Ch. 6.2/6.3, refs in Ch. 1, 5, 7, 8, App. A, Table 6.1 | draft + LaTeX fix + script: components split into new Sec. 6.3 'Components of the Strategies' (2-sentence opening drafted, paragraphs moved unchanged), checkpoint selection kept at end of 6.2, scaling clause removed from 6.2 conclusion, references repointed
2026-11-02 | Ch. 6.3 conclusion | draft: conclusion of the components experiment, built from Claude's suggestions accepted by the author
2026-11-02 | Ch. 6.1 | LaTeX/text edit: limitation statements moved out of the setup (paragraph 'Some factors were not varied' cut, covered by Sec. 7.3; budget clauses in 6.1.1 shortened to the design reason)
2026-11-02 | Ch. 1 approach, Ch. 6.1.1 | text edit: cross-chapter repetition of the few-shot configuration removed (Ch. 6 'reduce both' clause and 'first' k; Ch. 1 'one draw' and 'with k = 5')
2026-11-02 | Ch. 6.1.2, Ch. 7 l. 168 | text edit: over-explanation trimmed (version caveat clause, reproducibility paragraph 4 -> 3 sentences, meta sentence in Table 6.2 caption, alpha/dropout limitation cut from 6.1.2 with its defense todo moved to Ch. 7)
2026-11-02 | Ch. 6.1.2, Ch. 7 l. 168 | text edit: version-provenance sentence cut from 6.1.2 (fact moved to Ch. 7 limitation, defense todo moved), cluster name removed (24-hour limit kept)
2026-11-02 | Ch. 5.2-5.3, 6.1.2, App. A.2, CLAUDE.md | text edit + LaTeX fix: Tables 6.2/6.3 moved to new App. A.2 (Training and Strategy Parameters); six values only in the table added to Ch. 5 prose, eta_0 to 6.1.2; references repointed; CLAUDE.md parameter rule adjusted
2026-11-02 | Ch. 6.1.2, App. A.2, Ch. 7 l. 142/168 | text edit: software versions and reproducibility paragraph moved from 6.1.2 to App. A.2 (pointer sentence added), Ch. 7 references repointed; stray comment placement fixed
2026-11-02 | Ch. 6.1.2 l. 67, Ch. 7 l. 133 | text edit: repeated E = 10 value and repeated 'not at their best settings' clause removed
2026-11-02 | Ch. 6.1.3 metrics paragraph | text edit: tightened (sentence split, claim before reason), omitted metric named by ZSCL's own term Avg. with citation; CLAUDE.md terminology updated
2026-11-02 | Ch. 6.1.1 | text edit: subsection trimmed to what is new (sequence, strategies per order, update counts, equal-updates configuration, joint samples), repeats of Ch. 1/4/5 removed; retitled 'Task Orders and Few-Shot Settings'
2026-11-02 | Ch. 6.1.3 | text edit: task-specific LoRA metrics paragraph condensed (result sentence and repeated mechanism removed; per-run values moved to thesis_notes.md section 2)
2026-11-02 | Ch. 6.1.3 | text edit: sentence restricting Transfer comparisons to one task order removed (rule never at risk in the thesis)
2026-11-02 | Ch. 6.1.3 bootstrap paragraphs | text edit: tables half-sentence corrected (patellar table shows intervals); paired-bootstrap paragraph tightened (count of pairs removed, grammar, split sentence); verification of bootstrap pipeline (read-only script, 5 checks)
2026-11-02 | Ch. 7 l. 146 | text edit: '182 comparisons' replaced by 'multiple comparisons' (count removed from Ch. 6)
2026-11-02 | Ch. 6.1.3 | text edit: paired-bootstrap definition merged into the bootstrap paragraph (method first, motivation second); next paragraph opens with 'these paired intervals'
2026-11-04 | Ch. 6.1.3 bootstrap paragraphs | text edit: paired bootstrap merged into the bootstrap paragraph (intervals in the text identified as paired, checked against cl_differences.csv); repeated caveats and the two-runs example (in Ch. 7) cut
2026-11-04 | Ch. 6.1.3 comparisons paragraph | text edit: enumeration of compared pairs condensed to three kinds (7 -> 4 sentences), inaccuracies on replay removed
2026-11-04 | Ch. 6.1.3 comparisons paragraph | text edit: list of comparison kinds cut (inferable from Table 6.1), kept as source comment; paragraph now 3 sentences
2026-11-04 | Ch. 6.1.3 comparisons sentences | text edit: readability (interpret instead of read, comparisons named in one clause, reason for no significance made explicit)
2026-11-04 | Ch. 6.1.3, 6.2, 6.3, 6.6 | text edit: 23 paired intervals of large differences removed from the text, 15 kept where a statement depends on them; rule stated in 6.1.3
2026-11-04 | Ch. 6.2 figures 6.1-6.3, plot_results.py | script + LaTeX fix: shared LoRA with replay added to the three comparison figures (shared-LoRA colour, hatched bar / dashed line), legends refitted, captions updated; build fixed (OneDrive aux corruption)
2026-11-04 | Ch. 6 results tables (main, rank, few-shot, task order), make_results_tables.py | script + caption edit: best value per column bolded (main: six strategies; rank: shared-LoRA sweep), task-specific LoRA's by-construction values marked with a dagger and not ranked; few-shot caption '6k volumes' corrected to '6k samples'
2026-11-04 | Ch. 6.2 | text edit: eight repetitions removed (evaluation rule, joint definition, control-task values, differences vs seq. FT, femoral clause, joint interpretation kept only in the conclusion, 'without replay' qualifier)
2026-11-04 | Ch. 6.2-6.7 openings | text edit: lists of strategies, ranks, k and update counts that repeat Table 6.1 and Sec. 6.1.1 folded into the question sentence with a reference (6.2, 6.3, 6.4, 6.6, 6.7; 6.5 unchanged)
2026-11-04 | Ch. 6 result captions (Tables 6.2, rank, few-shot, task order, components; Fig. 6.1) | caption edit: shortened (evaluation rule, bold hedge, double dagger note, joint definition, legend repeat removed), 'one run each' added, arrow line unified
2026-11-04 | Ch. 6.1, 6.2 | text edit: 12 semicolons split into sentences, 7 grammar/tier-1 fixes (insertions l. 26 and Transfer, tense, idiom, subject of l. 65, modal of the 6.2 conclusion weakened to 'may'), bootstrap block split into two paragraphs
2026-11-04 | Ch. 6.2 first results paragraph and conclusion | text edit: topic sentence names the two groups, 'two LoRA strategies' corrected (replay pointed to 6.3), prompt-tuning position made exact (between in Adaptation/Forgetting, near first group in control-task drop)
2026-11-04 | Ch. 6.2 results paragraphs | text edit: parenthetical values written into the sentence (prompt tuning, 0.25), evaluation-matrix sentence rephrased
2026-11-04 | Ch. 6.2 evaluation-matrix sentences | text edit + number check: prompt-tuning count corrected from seven to six (eval_matrix of 7bcbb6cc), 'femoral cartilage after the patellar task' rephrased in two sentences
2026-11-04 | Ch. 6.2, plot_results.py | LaTeX fix + script: Figure 6.3 (control task over the sequence) removed, paragraph now refers to the Ctrl rows of Figure 6.2; figure call disabled in the script
2026-11-04 | Ch. 6.2, 6.3, App. A.3, make_results_tables.py | LaTeX fix + script + text edit: additional-evaluations table moved to new App. A.3 without duplicated last-epoch rows; best-validation check trimmed to two sentences; selected-epoch paragraph cut
2026-11-04 | Ch. 6.2 distillation paragraph, Ch. 7 l. 168 | text edit: limitation and generalisation sentences removed from Results (covered by Ch. 5 and Ch. 7 l. 36), scope kept as a half-sentence, logging limitation moved to Ch. 7 Limitations
2026-11-04 | Ch. 6.2 | text edit: prompt-tuning paragraph removed (repeated result, method fact, explanation already in Ch. 5 l. 332 and Ch. 7 l. 34); 'although it keeps all pretrained weights frozen' added to the first results paragraph
2026-11-04 | Ch. 6.2 outline, 6.3 replay paragraph | text edit: Sec. 6.2 paragraphs reordered (primary metrics together, Final Performance then joint, Transfer, check, conclusion), replay's Final Performance added to 6.2 and its repeat removed from 6.3, derived differences in the conclusion replaced by the values
2026-11-04 | Ch. 6.2 | LaTeX fix + text edit: figure references placed where the values are used, duplicate reference removed, forward reference to 6.7 reworded, figure order swapped (matrices first) and opening citation order adjusted
2026-11-04 | Ch. 6.2 | LaTeX fix: float order corrected to table, bar plot, matrices (matrices float placed before the control-task paragraph that first uses it), opening citation order restored; build fixed (OneDrive .out/.bcf corruption)
2026-11-04 | whole thesis | build check: clean build without errors or undefined references; remaining warnings and boxes classified (todo margin notes, template lmedoc packages.sty, cover logo)
2026-11-04 | Ch. 6.2 conclusion and first results paragraph | text edit: conclusion limited to what 6.2 shows (training-configuration explanation left to Ch. 7.2, task-specific LoRA's retention marked as by construction, recommendation phrased as a result), 'train all parameters' made precise
2026-11-04 | Ch. 6.2 first results paragraph | text edit: 'update all weights outside the text encoder' replaced by 'update the pretrained weights' (the distinguishing property)
2026-11-04 | Ch. 6.2 best-validation check | text edit: two sentences, unsupported 'therefore evaluate after the last epoch' removed (check shows a trade-off, not a worse result)
2026-11-04 | Ch. 6.2 joint fine-tuning paragraph | text edit: reference to the evaluation matrices in Appendix A.4 added for the per-structure values
2026-11-04 | Ch. 6.2, 6.3 replay | text edit: replay's strategy-level results (primary metrics, control-task course, end state) reported in 6.2 like the other strategies; 6.3 keeps the with/without comparison
2026-11-04 | Ch. 6.2 | text edit: flow fixes (LoRA group by metric, colon reveal removed, separate paragraph for the LoRA end state)
2026-11-04 | Ch. 6.2 Transfer | text edit: Transfer of shared LoRA with replay (0.175) added, consistent with 'three LoRA strategies'
2026-11-04 | Ch. 6.2 | text edit: LoRA end-state and joint fine-tuning paragraphs merged (one topic: Final Performance at the top of the range and its reference)
2026-11-04 | Ch. 6.3 | text edit: grammar, clarity and repetition (opening states which comparisons are separate runs and where tab:ch6_components is; replay numbers kept compact; ensemble explanation restated as per-task share ~1/t; ZSCL differences shortened to a pointer to Sec. 5.3; checkpoint reason added to the scaling paragraph; conclusion de-duplicated)
2026-11-04 | Ch. 6.2/6.3, Ch. 1, 7, 8, 5 | restructure (author decision): replay comparison moved from 6.3 to 6.2 (draft paragraph); 6.3 renamed 'Weight Ensemble and Gradient Scaling', opening and conclusion drafted (conclusion from Claude's suggestion accepted by the author); contribution 4 reworded; follow-up refs and Ch. 7/8 sentences; make_setup_tables.py components row
2026-11-04 | Ch. 6 structure | reorder by objective (author decision): patellar diagnosis and amount of labelled data before LoRA rank and task order, weight ensemble/gradient scaling last; patellar opening reworded with comparison values; refs fixed (few-shot -> sec:exp-main, rank->task-order link moved into the task-order loss paragraph); Ch. 1 outline order; make_setup_tables.py and make_appendix_tables.py group order (App. A groups now match Table 6.1)
2026-11-04 | Ch. 6.2 replay | text edit (author approved): standalone replay paragraph dissolved; Adaptation interval added to the primary-metrics sentence (l. 144), control-task part merged into the control-task paragraph
2026-11-04 | Ch. 6.2 | text edit (author approved): flow fixes (two groups introduced in P1; joint control-task drop moved to the primary metrics; topic sentence for the checkpoint check; 'its DSC fell' wording; end-state link 'This loss began right after training'; double 'with'; two conclusion sentences merged)
2026-11-04 | Ch. 6.2 -> 6.3 | text edit (author approved): patellar failure of task-specific LoRA named in the Final Performance paragraph with pointer to sec:exp-patellar; stale section number in a comment replaced by labels
2026-11-04 | Ch. 6.3 | text edit (author approved): sentence added after the starting-point observation (not varied by the diagnosis; pointer to sec:disc-budget)
2026-11-05 | Ch. 6-8, App. A.3 | precision rule (author decision): matrix entries in the prose rounded to two decimals from the raw values, rule sentence in 6.1.4; weight-ensemble evaluation matrix added to App. A.3 (make_appendix_tables.py, appA_we_matrix.tex) with one draft sentence
2026-11-05 | Ch. 6.3 | text edit: grammar and flow (starting-point sentence moved after the tested explanations; redundant 'configuration of the sequence' sentence cut; loss sentences split and set in past tense; 'neither ... nor' conclusion)
2026-11-05 | Ch. 6.3 Table/Fig. 6.3 | script + caption: baseline run labelled 'settings of the sequence' in table (make_results_tables.py) and legend (plot_results.py), regenerated; table caption gloss for 'none' removed; figure caption 'lie almost on top of each other'
2026-11-05 | Ch. 6.3 | text edit (author approved): setting values dropped from the method sentence (in Table 6.3 and P2); epoch-22 sentence states that the run was evaluated after epoch 50 (checked in code)
2026-11-05 | Ch. 6.4 Fig. 6.4 | script + caption: legend entry 'five volumes, 1,080 updates' (plot_results.py), figure regenerated; caption states the logarithmic axis
2026-11-05 | Ch. 6.4 | text edit: grammar, clarity, compactness (opening split with table ref; long sentences split; control-task course reworded; full-split LoRA reference moved to the topic sentence; 'about zero'; shared LoRA forgetting stated with its paired interval; joint: same total updates as seq. FT, 6,480 updates for the full split added (SLURM log); conclusion: 'only one of the three strategies', 'hardly moved', repeated shared-LoRA comparison removed)
2026-11-05 | Ch. 6.4 Table 6.4 | script + caption: joint fine-tuning rows show the total number of updates (make_results_tables.py), table regenerated
2026-11-05 | Ch. 6.4 Fig. 6.4 | script: markers at the axis limits no longer clipped (clip_on=False in few_shot, plot_results.py), figure regenerated; rank and task-order figures checked, not affected
2026-11-05 | Ch. 6.4 Table 6.4 caption | text edit: '6k samples' (wrong for the full-split row) replaced by 'trains on all six tasks at once in a single stage'
2026-11-05 | Ch. 6.3, 6.1.4 | table removal (author decision): Table 6.3 dropped (values to prose and Fig. 6.3 legend; 50-epoch interval added to the prose), figure caption self-contained, 6.1.4 interval sentence updated; make_results_tables.py: patellar table removed, generated file deleted
2026-11-05 | scripts | cleanup: unused replay table removed from make_results_tables.py, generated ch6_replay.tex deleted
2026-11-05 | Ch. 6.4 | text edit: ambiguous 'these two' replaced by 'those with k = 5 and with the full split'
2026-11-05 | Ch. 6.4 | text edit (author approved): seq. FT paragraph tightened (orphan shared-LoRA comparison cut; k = 10/20 values left to Table 6.4; control-task course in one sentence; 'instead of 0.781')
2026-11-05 | Ch. 6.4 | text edit (author approved): LoRA and equal-updates paragraphs tightened (k = 20 per-structure values and derivable differences cut; equal-updates topic sentence covers both LoRA and seq. FT)
2026-11-05 | Ch. 6.4 | text edit (author approved): joint fine-tuning paragraph tightened (Final Performance as a range, k = 10 caveat cut, control-task drop with endpoints and table reference)
2026-11-05 | Ch. 6.4 conclusion | text edit (author approved): conclusion condensed (evidence repeated from the paragraphs above cut, interpretation merged; hedge levels kept; '50 to 200 updates per task' placed after the scope)
2026-11-05 | Ch. 6.4 conclusion | text edit: limitation sentence split; 'the separation' named; terms aligned with the equal-updates paragraph
2026-11-05 | Ch. 7, Ch. 8 | text edit: 'data and updates' aligned to 'the number of volumes and the number of updates' (consistent with Sec. 6.4 and objective 3)
2026-11-05 | Ch. 6.5 | text edit (author approved): alpha/gamma_r sentence moved from the opening into the confound paragraph, with reference to Sec. 5.3
2026-11-05 | Ch. 6.5 | text edit: factual fix (Final Performance gain from femoral cartilage only, not 'two structures'; menisci added; checked in eval matrices); single-run interval caveat; matrix paragraph topic sentence with App. A pointer; patellar sentence cut (in 6.3); conclusion: TS-LoRA moved next to the trade-off, rsLoRA reminder shortened with reference to Sec. 3, repeated capacity/scale clause cut
2026-11-05 | Ch. 6.5 | text edit (author approved): Final Performance and Transfer trend split into two sentences with explicit ranks and exact values
2026-11-05 | Ch. 6.5 | text edit (author approved): interval-width sentence cut (general one-run caveat is in Sec. 6.1.4; rank differences reported without intervals)
2026-11-05 | Ch. 7.2 | reference fix: task-specific LoRA values (0.64, 0.57) cited to sec:exp-main instead of sec:exp-rank (checked in the r = 4 matrix)
2026-11-05 | Ch. 6.5 | text edit (author approved): alpha/r clause cut from the confound paragraph (choice of rsLoRA justified in Sec. 5.3)
2026-11-05 | Ch. 6.5 conclusion | text edit (author approved): repeated Final Performance plateau cut; rsLoRA design-intent sentence cut; task-specific LoRA sentence moved to the end with its rank choice (r = 4)
2026-11-05 | Ch. 6.5 Fig. 6.5 caption | text edit: setting (full split, original order, one run per rank) and pointer to Transfer in Table 6.5 added
2026-11-05 | Ch. 6.5 | text edit (author approved): condition 'with fixed alpha' added to the trade-off claim; 'moderate' dropped; lateral tibial sentence split with the structure as subject; task-specific LoRA paragraph moved after the shared-LoRA confound paragraph
2026-11-05 | Ch. 6.6 | text edit: grammar, clarity, compactness (ambiguous 'it' fixed; first-task contrast of seq. FT moved to the shared-LoRA paragraph; task-specific LoRA mechanism condensed; repeated explanation of the interval limit cut; shared LoRA Adaptation interval given instead of interval widths; control-task values already in 6.2 referenced; 'lowered the DSC on'; loss described in past tense; conclusion without repeated numbers and repeated clause; figure caption with setting)
2026-11-05 | Ch. 6.6 | text edit (author approved): task-specific LoRA sentence no longer claims the order leaves training unchanged (data and settings unchanged; initialisation differs), reference placed at the Ch. 5 reminder
2026-11-05 | Ch. 6.4, 6.6 | text edit (author approved): openings point to the evaluation matrices in App. A.4 for the per-task values
2026-11-05 | Ch. 6.6 | text edit (author approved): interval-limit sentence made explicit (an interval excluding zero shows that two trained models differ, not that the varied factor caused it)
2026-11-05 | Ch. 6.6 | text edit (author approved): first-task comparison of shared LoRA split per structure ('trained last' instead of 'later in the other order')
2026-11-05 | Ch. 6.6 | text edit (author approved): first-task observation moved into its own paragraph after the last-step paragraph (retention block together, first task next to the training loss); last-step values of three cartilages compressed
2026-11-05 | Ch. 6.6, App. A.5 | script + text (author approved): training-loss figure of the first two shared-LoRA tasks generated (plot_results.py, appA_shared_lora_loss.pdf), App. A.5 with draft sentence and caption, pointer from Sec. 6.6, App. A intro updated; build after clean (OneDrive aux corruption) without errors or undefined references
2026-11-05 | Ch. 6.6 | text edit (author approved): shared LoRA named at the start of the last-step, first-task and training-loss paragraphs
2026-11-05 | Ch. 6.6 | text edit (author approved): r = 4 contrast in the training-loss paragraph names shared LoRA (task-specific LoRA also uses r = 4)
2026-11-05 | Ch. 6.6 | text edit (author approved): order in the last-step claim matched to the evidence (control-task drop, then forgetting)
2026-11-05 | Ch. 6.6 | text edit (author approved): training-loss paragraph states r = 1024, which second-task value belongs to which order, and the order of the r = 4 run
2026-11-05 | Ch. 6.7 -> App. A, Ch. 1, 6.1, 6.2, 7, 8 | restructure (author decision): weight-ensemble and gradient-scaling section moved to App. A (markers kept), one-sentence pointer in 6.2, Table 6.1 row dropped (make_setup_tables.py), 6.1 factor list, App. A intro and matrices sentence, contribution 4 reworded (Ch. 1, Ch. 8, CLAUDE.md), Ch. 7 objective-4 question and answer, Ch. 8 component sentence cut
2026-11-05 | Ch. 6.7 -> App. A.4, Ch. 1, 6.1, 6.2, 7, 8 | restructure (author decision): weight ensemble and gradient scaling moved to App. A.4 (text moved, opening adapted), one-sentence draft pointer in 6.2, contribution 4 and outline narrowed, Ch. 7/8 component results cut, Table 6.1 row dropped (make_setup_tables.py), App. A intro and matrix note updated; clean build
2026-11-05 | whole thesis | check of the components move (all references, numbers, section numbers, contributions, abstract); references to App. A.4 added in Ch. 5 (l. 385) and Ch. 7 (l. 165)
2026-11-05 | Ch. 5, Ch. 7 | text edit (author approved): main text keeps one pointer to App. A.4 (Sec. 6.2); orphaned scaling-ablation caveat removed from Ch. 7 l. 165, ensemble clause trimmed in l. 173, reference dropped in Ch. 5 l. 385
2026-11-05 | Ch. 1 outline | text edit (author approved): patellar diagnosis added to the Ch. 6 sentence; appendix sentence lists all six appendix sections
2026-11-05 | Ch. 1 | text edit (author approved): gradient-scaling and weight-ensemble sentences cut from the strategy paragraph (defined in Ch. 5, results in App. A.4); outline's appendix sentence names 'two components adopted from ZSCL and CPE-CLIP'
2026-11-05 | Sec. 5.4, Sec. 6.7 | feedback: whether both sections are needed; overlap list, no edits
2026-11-05 | Sec. 5.4, Sec. 6.7 | text edit (author approved): overlap removed; 5.4 drops measured claim and table description, 6.7 refers back to 5.4 for backward/forward pass, adapter-storage sentence cut
2026-11-05 | Sec. 6.7 | feedback: section review (numbers checked against compute.csv, teacher CPU/GPU transfer against code) and proposed revision; no edits
2026-11-05 | Sec. 6.7 | script (scratchpad, not in repo): measured validation time per epoch from SLURM logs 1844922-24; revised proposal uses existing strategy terms; no edits
2026-11-05 | Sec. 6.7 (Computational Cost) | text edit (author approved): overlap/derived numbers cut, existing strategy terms; script: val_minutes column added to make_compute_table.py, compute.csv regenerated
2026-11-05 | Ch. 7 l. 49, Ch. 8 l. 59 | text edit (author approved): undefined 'parameter-efficient strategies' replaced by 'task-specific and shared LoRA'
2026-11-06 | Sec. 6.7 | text edit (author approved): 'taken from the logs of the runs' cut from the opening sentence
2026-11-06 | Sec. 6.7 | text edit (author approved outline): table no longer read out in prose; topic sentence for the other-runs paragraph; conclusion relates measurements to Sec. 5.4
2026-11-06 | Sec. 6.7 | text edit (author approved): repeated table reference cut from the comparison paragraph
2026-11-06 | Sec. 6.7 | text edit (author approved): sentence on the superseded seq. FT run removed; defense point D58 added to tracker
2026-11-06 | Sec. 6.7 | text edit (author approved): second-job/evaluations sentence removed
2026-11-06 | Sec. 6.7, Table ch6_compute | script + text edit (author approved): Wall-clock column dropped (make_compute_table.py), caption and joint total hours trimmed; built
2026-11-06 | Sec. 6.7 | text edit (author approved): sentence on distillation peak memory near the GPU limit removed
2026-11-06 | Sec. 6.7, Table ch6_compute caption | text edit (author approved): caption tightened (parameter counts left to Sec. 5.2, 'wall-clock' and 'jobs' removed)
2026-11-06 | Sec. 6.7, Table ch6_compute | script + text edit (author approved): replay row added to the compute table; few-shot, joint and replay sentences cut; checked dependants (Ch. 7 l. 165, Ch. 6 l. 68); built
2026-11-06 | Sec. 6.1 l. 68 | text edit (author approved): job claim stated as 12 of 17 full-split runs in one job (compute.csv), reference to Sec. 6.7 removed
2026-11-06 | Sec. 6.7 | text edit (author request): distillation and equal-updates sentences tightened, evaluation-spread sentences and repeated conclusion clause cut; defense point D59
2026-11-06 | Sec. 6.7 | text edit: inference sentence moved from the conclusion to the evaluation paragraph (one-sentence paragraph avoided)
2026-11-06 | Sec. 6.7 | text edit (author approved): evaluation paragraph removed, inference finding merged into the conclusion
2026-11-06 | Sec. 6.7 | text edit (author approved): other-runs paragraph removed, opening adjusted; defense point D60
2026-11-06 | Sec. 6.7 | text edit (author approved): conclusion paragraph removed; GPU-fit/inference sentence moved to the end of the comparison paragraph
2026-11-06 | Sec. 6.7 | text edit (author request): grammar/flow pass; comparison point of 'cheaper' and causal link of the distillation sentence added
2026-11-06 | Sec. 6.7 | text edit (author approved): opening sentence merged into the paragraph, table float moved after the heading; built
2026-11-06 | Sec. 6.1, Sec. 6.7 | text edit (author request): GPU memory unit unified to GiB (logs report MiB, 40960 MiB = 40 GiB); source comment added
2026-11-06 | Sec. 6.1, 6.7 | explanation: A100 memory unit checked against NVIDIA documents, nvidia-smi logs and JEDEC definition; defense point D61
2026-11-06 | Ch. 7 | feedback: diagnosis review of the whole chapter against Ch. 1-6, results tables and paper notes (no edits)
2026-11-06 | Ch. 7 (all sections) | text edits (author request 'fix all'): review issues fixed; Silva-Rodriguez Sec. 4.3.2 and SEER Table 1 checked in the PDFs; 4 new author todos; not built
2026-11-06 | Ch. 7 (all sections) | language pass and cuts (author request): grammar, tier-1 insertions, repetitions removed, paragraphs reordered in 7.1 obj. 2 and split in 7.2; no content added; not built
2026-11-06 | Ch. 7 opening | language fix (author request): semicolon, vague 'possible common cause', repeated 'discusses'; not built
2026-11-06 | Ch. 7 opening | language fix (author question): redundant relative clause removed; not built
2026-11-06 | Ch. 7 opening | explanation + language fix: undefined term 'training budget' in the chapter overview replaced by 'short training of ten epochs per task'; not built
2026-11-06 | Sec. 7.1 opening | text edit (author approved): paragraph cut from 7 to 4 sentences, overall answer condensed to one sentence; not built
2026-11-06 | Sec. 7.1 opening | text edit (author approved): reference to Sec. 1.3 and 'universal' added to the RQ restatement; not built
2026-11-06 | Sec. 7.1 opening | language fix (author request): overall-answer sentence split in two, insertion removed, condition k = 5 stated; not built
2026-11-06 | Sec. 7.1 opening | draft (author request): overall answer rewritten from the conclusions of Sec. 6.2, 6.4-6.6 (adaptation and forgetting rise and fall together; replay the exception); not built
2026-11-06 | Sec. 7.1 opening | text edit (author request): overall answer condensed from 6 to 3 sentences; not built
2026-11-06 | Ch. 7 | explanation/feedback (author question): role of Ch. 6 conclusions in the Discussion; restructuring of 7.1 suggested, no edits
2026-11-06 | Sec. 7.1 | outline (author request): revision 3 proposed in outlines/ch7_discussion.md (objective answers without restating Ch. 6); no thesis edits
2026-11-06 | Sec. 7.1 | draft (author approved outline rev. 3): objective answers rewritten in the order 1-4 without restating Ch. 6; ~1,600 -> ~950 words; not built
2026-11-06 | Sec. 7.1 | text edit (author approved): flow fixes (joint reference no longer repeated, single answer in obj. 2, obj. 4 reordered with answer sentence, prior-work sentence moved); not built
2026-11-06 | Sec. 7.1 | text edit (author approved): opening cut to two sentences (overall answer and scope sentence removed, covered by the objective answers, Sec. 7.3 and Ch. 8); obj. 3 sentence names its scope; not built
2026-11-06 | Sec. 7.1 obj. 1 | text edit (author approved): paragraph tightened (objective wording from Ch. 1, pretrained-reference point restored, concrete answer, requirements sentence cut); not built
2026-11-06 | Sec. 7.1 obj. 1 | text edit (author approved): result numbers replaced by qualitative statements with references to Ch. 6; not built
2026-11-06 | Ch. 1, Sec. 1.3 and 1.5 | feedback (author question): review of objectives and contributions against Ch. 5-7; no edits
2026-11-06 | Ch. 1 Sec. 1.3, 1.5; Ch. 7 obj. 1-2 | text edits (author approved): objectives 1-2 and contributions 3-4 reworded, Ch. 7 aligned, CLAUDE.md record updated; not built
2026-11-06 | Ch. 1 Sec. 1.5 | text edit (author request): App. A components removed from contribution 4 again (decision 2026-11-05); feedback on keeping the patellar diagnosis; not built
2026-11-06 | Ch. 1 Sec. 1.5 | language fix (author approved): contribution 1 reworded for readability; CLAUDE.md record updated; not built
2026-11-06 | Ch. 1 Sec. 1.5 | text edits (author approved): contributions 1 and 4 reworded, novelty sentence added to the closing paragraph; objective 4 kept; CLAUDE.md record updated; not built
2026-11-06 | Ch. 1 Sec. 1.5 | language fix (author approved): contribution 4 gives the rank range instead of 'seven ranks of shared LoRA'; not built
2026-11-06 | Ch. 1 Sec. 1.3, 1.5 | language fix (author approved): objective 1 referent made explicit; contribution 3 purpose-first, parallel to contribution 4; CLAUDE.md record updated; not built
2026-11-06 | Ch. 1 Sec. 1.5 | language fix (author approved): contribution 3 restructured (analysis as subject, 'by' clause); not built
2026-11-06 | Sec. 7.1 obj. 1 | draft (author approved structure): what is established vs combined, two protocol limits, answer without 'where each arose'; not built
2026-11-06 | Sec. 7.1 obj. 1 | language fix (author approved): vague 'parts' replaced by named measures and references; not built
2026-11-06 | Ch. 7 | explanation (author question): answer to the research question summarised from Ch. 6/7; no edits
2026-11-06 | Sec. 7.1 | draft (author approved outline): section restructured around questions (answer, why strategies differ, configuration and order, protocol); chapter opening and 7.2 reference adjusted; not built
2026-11-06 | Sec. 7.1 | interview (D1-D6) and draft from the author's answers; section rewritten as discussion points; not built
2026-11-06 | Ch. 7 Discussion | explanation: how to write the Discussion yourself (purpose, structure, guiding questions per objective, limitations mapping, pitfalls); no text drafted
2026-11-06 | Sec. 7.1 | interview questions (20, grouped by objective) for a redraft of 7.1; no text drafted
2026-11-06 | Sec. 7.1 | interview Q1-Q2: feedback on author's answer to the research question (checked against ch6_main.tex), suggested wording offered as option
2026-11-06 | Sec. 7.1 | interview Q4: feedback on author's sharing/prompt-tuning answer (checked against ch6_main, ch6_rank, paper notes); explanation of a representation view
2026-11-06 | Sec. 7.1 | interview Q6: feedback on author's joint-fine-tuning answer (checked against ch6_main, ch6_few_shot, Ch. 6 l. 291/405, paper notes SPU/ZSCL)
2026-11-06 | Sec. 7.1 | interview Q6 settled (joint fine-tuning one sentence); recorded in thesis_notes
2026-11-06 | Sec. 7.1 | interview Q8 settled (option c); recommendation on Q4a (representation view)
2026-11-06 | Sec. 7.1 | interview Q4a settled (representation view); remaining questions 11/14/17/18 with data
2026-11-06 | Sec. 7.1 | interview Q11/Q14 feedback, Q17 settled, Q18 comparison with MedPEFT-CL and Beyond Forgetting prepared from paper notes
2026-11-06 | Sec. 7.1 | interview closed (Q11, Q14, Q18 settled); outline revision 4 proposed
2026-11-06 | Sec. 7.1 | draft (outline rev. 4 approved, from author's interview answers Q1-Q18): section rewritten by theme; tracker D48 updated, D61-D62 added; not built
2026-11-06 | Sec. 7.1 | LaTeX/text edit: seven compaction edits approved by the author (repetition removed, universality merged into representation paragraph); backup backups/discussion_2026-11-06_before_7.1_compact.tex
2026-11-06 | Sec. 7.1 | LaTeX/text edit: representation paragraph shortened from 13 to 7 sentences (author approved proposed version)
2026-11-06 | Sec. 7.1 (opening + representation paragraph) | language edit: grammar and flow (insertions between subject and verb removed, colon reveals split, referents checked)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: CPE-CLIP content moved into the prompt-tuning paragraph, published-methods paragraph reduced to ZSCL (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: prompt-tuning paragraph reordered, limit vs shared LoRA stated (author chose option b)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: prompt-tuning paragraph restructured for clarity (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: ZSCL comparison corrected to Transfer vs Transfer, Table 1b argument added (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: prompt-tuning paragraph shortened, untested candidates removed (did not explain the difference to shared LoRA); author approved (a) only
2026-11-06 | Sec. 7.1 | LaTeX/text edit: few-shot paragraph removed, its methodological sentence moved into the opening (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: placement half-sentence removed from prompt-tuning paragraph; task-order sentence restricted to the original order (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: P2 reframed from representation view to what each strategy changes; prompt-tuning paragraph merged into P2 (author approved option A); notes and tracker D48, D61 updated
2026-11-06 | Sec. 7.1 | LaTeX/text edit: gap sentence repeating Ch. 1/2 replaced by one sentence with reference (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: P2 dissolved: universality into opening, new paragraph on replay vs the two strategies that stay close to the pretrained model, ZSCL paragraph linked (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: universality sentence removed from opening (moves to Summary); notes and tracker updated
2026-11-06 | Sec. 7.1 | LaTeX/text edit: opening, control-task sentences merged and reference point of 'further' made explicit (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: replay-cost sentence removed (covered in 7.3/7.4), link sentence to the two stay-close strategies reworded as contrast with replay (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: ZSCL paragraph shortened, repeated list and ablation replaced by references to Ch. 5.4.4 and Ch. 2 (numbers kept in parenthesis; author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: task-order paragraph shortened, joint-fine-tuning sentence removed from protocol paragraph (repetition of Ch. 6; author approved)
2026-11-06 | Sec. 7.1 | draft/LaTeX edit: rank answer for Obj. 4 added, closing reading for replay/stay-close paragraph (Claude's suggestion, author instruction), linking openings for order and protocol paragraphs; notes, tracker D63
2026-11-06 | Sec. 7.1 | LaTeX/text edit: 'stay close' paragraph removed (Adaptation confound, repeats Ch. 6.2), MedPEFT-CL moved to opening, ZSCL opening adjusted; D63 deleted (author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: CPE-CLIP sentence added, linking opening for the published-methods paragraph, referent fixed in protocol paragraph (author approved)
2026-11-06 | Sec. 7.1 opening | language/flow edit: comparison point of 'similar Adaptation' named, MedPEFT-CL claim made precise (Table 8 checked), links to control task and few-shot, condition added to the few-shot comparability claim
2026-11-06 | Sec. 7.1 opening | language edit: the four strategies named instead of 'one parameter set'; control-task sentence as 'every strategy except task-specific LoRA' (author approved)
2026-11-06 | Sec. 7.1 opening | language/flow rewrite on author request (no content removed): pattern -> exceptions with numbers -> prior work -> limit -> control task -> few-shot topic sentence -> consequence -> scope
2026-11-06 | Sec. 7.1 opening | language edit: two repetitive few-shot sentences merged (author approved)
2026-11-06 | Sec. 7.1 opening | language edit: comparability sentence reduced to the implication (confound already in Ch. 1, 5, 6; author approved)
2026-11-06 | Sec. 7.1 | LaTeX/text edit: CPE-CLIP sentence deleted, ZSCL paragraph opening simplified (author decision); tracker D64 added
2026-11-07 | Sec. 7.2 | feedback: whether Sec. 7.2 (training budget) is needed; overlap with 7.1, 7.3, Ch. 6; options keep / shrink / fold into 7.3
2026-11-07 | Sec. 7.2/7.3, Ch. 6, Ch. 8 | LaTeX/text edit: Sec. 7.2 folded into first limitation of 7.3 (draft, author approved), references retargeted
2026-11-07 | Sec. 7.1, 7.3 | feedback: cut candidates (repetitions with 7.1/7.3/Ch. 2/App. A, low-value threats)
2026-11-07 | Sec. 7.1, 7.3, App. A.2 | LaTeX/text edit: cut list applied (repetitions removed, two logging caveats moved to App. A.2; author approved all)
2026-11-07 | Sec. 7.3 | explanation: learning rate in the 50-epoch patellar run (eta_0 unchanged, decay stretched; checked config and optimizer.py)
2026-11-07 | Sec. 7.3 | LaTeX/text edit: 50-epoch confound wording (author's choice); explanation/check of the task-specific LoRA run pair (configs, eval matrices, seed order in code)
2026-11-07 | Sec. 7.3 | feedback: single-run paragraph needed; proposed tightening (signpost cut, caveat sentence shortened)
2026-11-07 | Sec. 7.3 | feedback: suitability of the task-specific LoRA run pair as example of run-to-run variation (lower bound)
2026-11-07 | Sec. 7.3, Sec. 6.6 | LaTeX/text edit: single-run paragraph rewritten (author approved); GPU non-determinism clause removed in Ch. 6
2026-11-07 | Sec. 7.3 | feedback: verified best-validation sentence (cl_differences.csv, method.tex l. 211, Ch. 6 l. 203-204)
2026-11-07 | Sec. 7.3, 7.4 | LaTeX fix: checkpoint sentence now gives values with direct table refs; adapter-size ref -> tab:ch6_compute; Ch. 7 number-vs-reference check
2026-11-07 | Sec. 7.3 | draft: replay-cost sentence shortened, clause on extra updates added (author approved suggestion)
2026-11-07 | Sec. 7.3, Sec. 6.2 | draft/LaTeX edit: internal-validity paragraph rewritten (checkpoint rule reverses distillation vs seq. FT forgetting order; author approved); Ch. 6 caveats added
2026-11-07 | Sec. 7.3, 7.4 | LaTeX/text edit: replay-cost sentence removed from 7.3, epoch time added to 7.4 replay cost sentence (author approved)
2026-11-07 | Sec. 7.3 | LaTeX/text edit: adaptations sentence shortened, refs to Sec. 5.3 subsections (author approved)
2026-11-07 | Sec. 7.3 | LaTeX/text edit: task-specific LoRA by-construction sentence removed (author approved)
2026-11-07 | Sec. 7.3 | LaTeX/text edit: paragraphs regrouped by subject (protocol, internal, strategies, data); three topic sentences new (author approved)
2026-11-07 | Sec. 7.3 | LaTeX/text edit: strategies-paragraph topic sentence reworded (author approved)
2026-11-07 | Sec. 7.3 (+Ch. 1, 2, 4, 5) | explanation/check: VoxTell checkpoint version (HF card, README, download script); consequences listed, no thesis edits
2026-11-07 | Ch. 4/5/7 (control task, data) | check: VoxTell v1.1 training data via HF card and GitHub issues #6, #13, #15, #17 (web-fetch agent); facts recorded in thesis_notes, no thesis edits
2026-11-07 | Ch. 4, 5, 7 + bib | LaTeX/text edit: v1.1 training-data corrections (minimal fix, author approved); bib: two @online entries added by bib-entry-adder (issue #15, HF model card)
2026-11-07 | bib | LaTeX fix: issue #15 URL linked to the comment; build checked (no undefined refs/citations)
2026-11-07 | bib | LaTeX fix: model card entry given label Hug26 and sorttitle (no author on the card); rebuilt, no undefined refs
2026-11-07 | Sec. 7.3 | LaTeX/text edit: orientation sentence shortened, consequence added (author approved)
2026-11-07 | Sec. 7.3 | LaTeX/text edit: data paragraph reordered, topic sentence and v1.1 link reworded (author approved)
2026-11-07 | Sec. 7.2 | feedback + LaTeX/text edit: cross-chapter repetition check; R1-R5 applied (budget merge, SEER -> ref to Ch. 2, intransigence shortened, other strategies -> MedCRP-CL clause, single-run sentences merged), R6 kept (author: best call)
2026-11-07 | Sec. 5.1 | LaTeX/text edit: duplicate trained-once sentence removed (author approved); Ch. 1 l. 173 noted for final revision
2026-11-07 | Sec. 7.1 | feedback + LaTeX/text edit: repetition check both directions; ZSCL ablation numbers replaced by ref to Ch. 2 (author approved); Ch. 8 example alignment noted
2026-11-07 | Sec. 7.2 | language edit: grammar/flow pass (tier-1 insertions removed, long sentences split, internal-validity paragraph reordered, alpha/dropout consequence added)
2026-11-10 | Sec. 7.3 | language edit: grammar/clarity/flow pass (repeated pretrained DSC cut, long sentences split, ordinal list of extensions regrouped into two paragraphs, alpha/gamma_r wording)
2026-11-10 | Sec. 7.3 | language edit: formal/academic register pass (informal phrases replaced, 'LoRA failures' and 'large loss' made precise, SPU reference to Sec. 2 instead of unverified paraphrase)
2026-11-10 | Sec. 7.3 | language edit: opening sentence register ('The numbers of' -> 'The quantitative results reported in')
2026-11-10 | Sec. 7.3 | feedback: structure check against outline rev. 2 and interview decisions (thesis_notes 2026-10-24 items 7-9); no edits
2026-11-10 | Sec. 7.3 | LaTeX/text edit: two author-confirm todos removed after approval; outline file updated to current Ch. 7 structure
2026-11-10 | Sec. 7.3 | fact check + LaTeX/text edit: six lines corrected against code, Ch. 5/6 and tables (hypothesis condition, replay samples not volumes, 'both' forgetting and drop, task-specific adapter init as test, few-shot runs of other strategies, shared-LoRA last-step sentence)
2026-11-10 | Sec. 7.3 | feedback: repetition check of 7.3 against 7.1 and 7.2; cuts proposed, no edits
2026-11-10 | Sec. 7.3 | LaTeX/text edit: repetition cuts approved by author (scope sentence merged, forgetting claim -> ref to 7.1, tuning remedy, hypothesis wording, last-step clause)
2026-11-10 | Sec. 7.3 | LaTeX/text edit: flow repair after cuts (opening linked to end of 7.2, hypothesis restated once, replay transition, extension paragraphs split consistently, verb agreement)
2026-11-10 | Sec. 7.3 | outline: new outline proposed after reading Ch. 1-6 (no edits)
2026-11-10 | Ch. 7 | outline: diagnosis of current Ch. 7 and full redraft outline (revision 5) proposed after rereading Ch. 1-6 and App. A; written to outlines/ch7_discussion.md, no thesis edits
2026-11-10 | Ch. 7 | outline: structure decisions recorded (revision 5b: three sections kept, ceiling reading, no figure, no table); paragraph-level change list for the redraft given, no thesis edits
2026-11-10 | Ch. 7 | feedback: critique of own revision-5b outline vs current Ch. 7 prose (strengths, risks of the ceiling reading), no thesis edits
2026-11-10 | Ch. 7 | feedback: cost-benefit of the 7.1 rewrite vs minimal fix, options given, no thesis edits
2026-11-10 | Sec. 7.3 | feedback + outline: diagnosis of Sec. 7.3 and rewrite outline proposed; 7.1 rewrite put on hold by the author; no thesis edits
2026-11-10 | Sec. 7.3 | outline approved by author; recommendations for Q1-Q4 and feedback on the author's future-work point (coverage, wording, citation of nested learning), no thesis edits
2026-11-10 | Sec. 7.3, Ch. 8 | draft: Sec. 7.3 redrafted from the approved outline (CLAUDE-DRAFT); Ch. 8 practical paragraph moved into 7.3 and replaced by a pointer; bib entry behrouz2025nestedlearning added via bib-entry-adder; paper_notes/nested_learning.md written
2026-11-10 | Sec. 7.3 | feedback: repetition check of the redrafted 7.3 against 7.1 and 7.2; cuts proposed, no edits
2026-11-10 | Sec. 7.3 | LaTeX/text edit: repetition cuts approved by the author (12 items: scope, Chen merge, task-order and single-run sentences, hypothesis merged into tests, task-kind merge, replay clauses, updates point, extension opening, MedCRP-CL, replay reason, intervals clause)
2026-11-10 | Sec. 7.3 | language edit: first paragraph (formal register, grammar, flow) on author request
2026-11-10 | Sec. 7.3 | text edit: prior-work paragraph shortened on author approval (CA-SAM sentence removed, Chen et al. and replay sentences merged)
2026-11-10 | Sec. 7.3 | text edit: task-kind paragraph removed (covered by 7.2 and the extension); same-images point merged into the evaluation extension, on author approval
2026-11-10 | Sec. 7.3 | text edit: practical-use paragraph removed (facts in Ch. 5/6), closed-set point moved into the main-extension paragraph, planning paragraph opening adjusted, on author approval
2026-11-10 | Sec. 7.3, Ch. 8 | text edit: planning paragraph removed (repetition of 7.1/7.2/Ch. 6/Ch. 8), update-budget recommendation added to the training extensions, Ch. 8 pointer restored, on author approval
2026-11-10 | Sec. 7.3 | language edit: prior-work paragraph (formal register, grammar, flow; replay claims matched to Ch. 2) on author request
2026-11-10 | Sec. 7.3 | text edit: main-extension opening corrected (condition 'in the comparison of the strategies', 'one parameter set for all tasks' instead of 'without the task identity'), on author approval
2026-11-10 | Sec. 7.3 | text edit: task-specific LoRA sentence corrected to match the code (adapter selected by the task identity given by the protocol; derivation from the text prompt stated as a possibility), on author approval
2026-11-10 | Sec. 7.3 | text edit: MoE-Adapters sentences merged, misassignment detail cut (in Ch. 2), on author approval
2026-11-10 | Sec. 7.3 | language edit: nested-learning sentence split, 'a recent proposal' removed, on author approval
2026-11-10 | Sec. 7.3 | language edit: replay sample-selection sentence clarified (random draw vs selection by training difficulty), on author approval
2026-11-10 | Sec. 7.3 | text edit: MoE-Adapters sentence shortened (mechanism detail cut, in Ch. 2), on author approval
2026-11-10 | Sec. 7.3 | language edit: main-extension paragraph (formal register, connectives, sentence splits) on author request
2026-11-10 | build | LaTeX fix: full latexmk build run on author request; behrouz2025nestedlearning now resolves (stale .bbl from 2026-11-07 was the cause)
2026-11-10 | Sec. 7.3 | text edit: training-extension sentences condensed (tuning vs rank selection separated and corrected; few-shot-runs sentence and update-budget recommendation removed as repetition of 7.2, Ch. 5, Ch. 8), on author approval
2026-11-10 | Sec. 7.3 | text edit: evaluation-extension paragraph condensed (control-task sentences merged, other-models sentence removed as covered by the first paragraph), on author approval
2026-11-10 | Sec. 6.6, 7.3, Ch. 8 | text edit: open task-order question reworded to "lateral meniscus itself or the tasks trained before it" (was structure vs position), consistently in three places, on author approval
2026-11-10 | Sec. 7.3 | text edit: checkpoint-v1.0 extension removed (author: option 2); broader-control-task sentence kept
2026-11-10 | Ch. 7 | feedback: full chapter read against Ch. 6 tables, Ch. 2, notes and guidelines; issue list and pass verdict (no edits to the thesis)
2026-11-10 | Ch. 7 (7.1, 7.2, 7.3), Ch. 8 l. 54 | text edit: review fixes on author request ('fix all except 3'): metric coupling, few-shot answer, task-specific LoRA by construction, gamma_r, rsLoRA and CPE-CLIP comparison, second explanation next to zero-init, MedCRP-CL wording, Chen et al. caveat, nested-learning reason, universality hedge, equal-updates extension (draft, CLAUDE-DRAFT)
2026-11-10 | Sec. 7.1 para 1 | text edit: flow and length (claim, metric caveat, Final Performance trade-off, two exceptions), on author approval
2026-11-10 | Sec. 7.1 para 1 | text edit: metric-coupling caveat removed, trade-off stated in Final Performance only (concision), on author request
2026-11-10 | Sec. 7.1 para 1 | text edit: replay definition clause removed (defined in Sec. 5.3), on author request
2026-11-10 | Sec. 7.1 | text edit: numbers repeated from Ch. 6 removed (answer, task-order paragraphs), protocol paragraph keeps the two diverging pairs; flow and grammar pass, 'prompts' -> 'learned prompts' (terminology), on author request
2026-11-10 | Sec. 7.1 para 1, task-order para | text edit: answer reframed on author approval (full-split trade-off; no run with one parameter set and current-task data above Final Performance 0.233 in the original order; joint k = 5 reference; two exceptions with their cost); reverse-order exception added
2026-11-10 | Sec. 7.1 para 1 | text edit: split into trade-off and exceptions paragraphs, joint line states what it adds (one parameter set holds all six structures), readability, on author approval
2026-11-10 | Sec. 7.1 para 1 | text edit: two opening sentences merged into one, on author request
2026-11-10 | Sec. 7.1 paras 1-2 | text edit: language pass (formal register, no insertions between subject and verb, hedged inference 'suggests'), on author request
2026-11-10 | Sec. 7.1 para 1 | text edit: joint fine-tuning sentences merged into one, on author request
2026-11-10 | Sec. 7.1 para 1 | text edit: joint sentence now states the ruled-out explanations (model, number of volumes) instead of the obvious conclusion, on author question
2026-11-10 | Sec. 7.1 para 1 | text edit: joint fine-tuning sentence removed (author: obvious; VoxTell is universal, seq. FT k = 5 already learns each structure)
2026-11-10 | Sec. 7.1 paras 1-3, Sec. 7.3 para 2 | text edit: answer verified against eval matrices and rewritten (end-of-sequence content, explicit answer first in para 2, Beyond Forgetting agreement, new control-task paragraph scoped to the comparison); 7.3 replay sentence reduced to Lifelong nnU-Net (Beyond Forgetting now in 7.1), on author approval
2026-11-10 | Sec. 7.1 paras 1-2 | text edit: numbers repeated from Ch. 6 removed (0.781, 0.450); only the synthesised 0.233 kept, on author request
2026-11-10 | Sec. 7.1 para 2 | text edit: three sentences on the two exceptions folded into the opening sentence (5 -> 3 sentences), on author request
2026-11-10 | Sec. 7.1 para 2 | text edit: repeated descriptions of replay and task-specific LoRA removed (one sentence per strategy: mechanism, effect, cost), on author request
2026-11-10 | Sec. 7.1 few-shot para | text edit: equal-updates sentences merged, 'less trained model' reading left to Ch. 6.4, on author question
2026-11-10 | Sec. 7.1 few-shot para | text edit: scope sentence removed (covered by Sec. 7.2), on author question
2026-11-10 | Sec. 7.1 | text edit: paragraph order (ZSCL, CPE-CLIP after order and rank), order/rank paragraph split, protocol paragraph placed relative to SPU, CA-SAM, SAM-Med3D-MoE, 'because' -> 'as'; feedback: interpretations of the few-shot results listed for the author
2026-11-10 | Sec. 7.1 few-shot para, Sec. 7.2 | text edit: interpretations B (LoRA strategies need more updates, Silva-Rodriguez et al. moved here from 7.2) and D (fewer updates move seq. FT along the trade-off, trained tasks only) added on author choice
2026-11-10 | Sec. 7.1 few-shot para | text edit: trade-off contrast for seq. FT removed (covered by para 1), seq. FT fact stated before its explanation, Silva-Rodriguez comparison numbers dropped (7 -> 5 sentences), on author request
2026-11-10 | Sec. 7.1 task-order para | text edit: reverse-order sentence shortened to the exception to the 0.233 statement, on author question
2026-11-10 | Sec. 7.1 | text edit: CPE-CLIP paragraph removed (rested on appendix-only gradient-scaling results; decision 2026-11-05), on author question
2026-11-10 | Sec. 7.1 protocol para | text edit: divergence shown with within-metric pairs (shared LoRA r = 1024 vs 2048; seq. FT k = 20 vs full split) instead of single-run cross-metric values; SPU/CA-SAM/SAM-Med3D-MoE sentence compressed, on author question
2026-11-10 | Sec. 7.2 | text edit: limits of the 7.1 answer added (grouping after the results, Final Performance includes the last task, 0.233 from single runs), first limitation split (configuration and confounds / LoRA slow-start hypotheses), checkpoint passage shortened, semicolon split, on author approval
2026-11-10 | Sec. 7.1 rank para, Sec. 7.2 slow-start para | text edit: repetitions between 7.1 and 7.2 removed (gamma_r confound as half-clause in 7.1; few-shot no-learning case only referenced in 7.2), on author approval
2026-11-11 | Sec. 7.2 slow-start para | text edit: language made formal and precise (colon reveal split, 'is open'/'did not help'/'candidate' replaced, 'full fine-tuning' replaced by the shared configuration, rank stated, empty-prediction claim narrowed since shared LoRA's first task reached 0.29), on author request
2026-11-11 | Sec. 7.2 slow-learning and 'Second' paras | text edit: paragraph focus (closing sentence on what the slow learning means for LoRA's Adaptation; gamma_r sentence tied to the r = 4 vs 1024 difference; vague 'different seeds' clause cut; last sentence split), on author approval
2026-11-11 | Sec. 7.2 slow-learning para | text edit: shortened from 10 to 5 sentences for page budget (evidence for/against each hypothesis cut, observations remain in Ch. 6), on author approval
2026-11-11 | Sec. 7.2 'Second' para | text edit: example and conclusion shortened (Ch. 6 numbers removed, point now that an interval excluding zero does not prove an effect), shared-LoRA caveat reworded as no repeated configuration, on author approval
2026-11-11 | Sec. 7.2 | text edit: paragraph on the limits of the 7.1 answer removed (repeated 7.1 and the 'Second' para); post-hoc grouping moved as one sentence into the threats paragraph ('Four further threats'), on author approval
2026-11-11 | Sec. 7.2 'Third' para | text edit: language made formal and precise (terms 'full training split'/'original task order', subject-first sentence, vague 'same holds' replaced, two wording sentences merged; 'pretrained VoxTell is sensitive to the wording' corrected to match Ch. 2: robust but not completely), on author request
2026-11-11 | Sec. 7.2 | text edit: flow between paragraphs (slow-learning para linked to the shared configuration; protocol para marked as 'further'; text-prompt sentence moved after the scope sentence; multiple-comparisons sentence moved to the end of 'Second'), on author approval
2026-11-11 | Sec. 7.2 'Third' para | text edit: text-prompt robustness sentence simplified (ambiguous relative clause removed), on author approval
2026-11-11 | Sec. 7.2 protocol-limits para | text edit: control-task sentences merged (pretrained DSC 0.98 and repeated 'four test volumes' cut), on author approval
2026-11-11 | Sec. 7.2 protocol-limits para | text edit: test-volume and label-origin points split into two sentences, on author approval
2026-11-11 | Sec. 7.2 | text edit: 'strategies not evaluated' paragraph moved after 'Third' (scope); overview sentence on the remaining limitations added, on author approval
2026-11-11 | Sec. 7.2 threats para | text edit: post-hoc grouping sentence removed ('Three further threats'); defense point kept in tracker; explanation of Ch. 5.3 alternatives sentence, on author request
2026-11-11 | Sec. 7.3 prior-work para | text edit: language made formal and concise (Chen numbers cut, caveat shortened, formulaic closing replaced; replay claim scoped to strategies with one parameter set, as in 7.1), on author request
2026-11-11 | Sec. 7.3 prior-work para | text edit: 'preprint' remark removed, 'two tasks' moved into the setting description, on author approval
2026-11-11 | Sec. 7.1, 7.3 | text edit: Lifelong nnU-Net replay agreement moved from 7.3 into the 7.1 prior-work sentence (3D verified in paper notes); 7.3 paragraph now only on Chen et al., on author approval
2026-11-11 | Sec. 7.3 main-extension para | text edit: topic sentence states the goal (no task identity, pretrained ability kept); replay sentences linked to it (closest among evaluated strategies) and merged, on author approval
2026-11-11 | Sec. 7.3 main-extension para | text edit: repetitions removed (7.1 recap in one sentence, MedCRP-CL grouping referenced to 7.2, rephrased-prompt point once) and language made formal (fronted 'Judged by', vague 'serve', 'however' between subject and verb), on author approval
2026-11-11 | Sec. 7.3 extension paras | text edit: language made formal and precise ('slow start' -> 'slow learning' as in 7.2; two long sentences split; purpose of per-strategy tuning stated; 'ranks' instead of 'configurations'; 'Further extensions' not repeated; 'wording' replaced; comparison with the lung made parallel), on author request
2026-11-11 | Sec. 7.3 | text edit: replay extension moved out of the main-extension paragraph into its own paragraph ('came closest to this goal' framing dropped), on author instruction
2026-11-11 | Sec. 7.3 training extensions para | text edit: shortened from 8 to 4 sentences (extensions that only invert a 7.2 limitation listed in one sentence; tests of the two LoRA explanations kept), on author approval
2026-11-11 | Ch. 7 review | feedback: whole chapter reviewed; RQ one-line answer drafted, then withdrawn as repetition of 7.1 (belongs in Ch. 8); text edit: 7.3 scope 'In the comparison of the strategies', 7.2 'strategies' -> 'methods', on author approval
2026-11-11 | Sec. 7.1 few-shot para | text edit: seq. FT k = 5 kept the control task added (D65, first part), the three observations explained by the equal-updates runs named explicitly, on author approval
2026-11-11 | Ch. 8 Summary | outline (rev. 2) after reading Ch. 1-7, approved by the author; draft: whole chapter rewritten (8 paragraphs, ~1,060 words, all % CLAUDE-DRAFT), on author request
2026-11-11 | Ch. 1 Sec. 1.4, Ch. 8 para 1 | text edit: control task 'not trained on during the adaptation' (AeroPath is in the training data of checkpoint v1.1), on author approval
2026-11-11 | Ch. 8 paras 3-6 | text edit: sentences copied from Sec. 7.1 reworded (few-shot para led by the equal-updates result; rank and protocol sentences rephrased), content unchanged, on author approval
2026-11-11 | Ch. 8 | text edit: review fixes (few-shot scope 'other two strategies run with few volumes'; referent of the 0.233 sentence; paragraph 3 opens with the answer to the research question; protocol topic sentence covers both examples; 'main reason'; VoxTell cited at first mention), on author approval
2026-11-11 | Ch. 7 / Ch. 8 structure | feedback: assessed proposal to move 7.2/7.3 into Ch. 6 and merge 7.1 with Ch. 8 (no edits)
2026-11-11 | Ch. 6-8 structure | outline: paragraph-by-paragraph mapping for dissolving Ch. 7 into Ch. 6 and the Summary (outlines/restructure_ch6_ch8.md); no thesis text changed
2026-11-11 | Ch. 6-8 structure | outline revision: recommendations on the four open choices; 7.3 generalisation paragraphs kept together in 6.8 (Chen et al. no longer moved to 6.2)
2026-11-11 | Ch. 6 Sec. 6.8 | LaTeX restructure: Sec. 7.2 and 7.3 P1-P2 moved verbatim into new Sec. 6.8 'Limitations and Generalisation'; one opening sentence drafted (CLAUDE-DRAFT); references repointed, on author approval
2026-11-11 | Ch. 6 Sec. 6.2, 6.4, 6.5, 6.6 | LaTeX restructure: prior-work sentences moved from Sec. 7.1 into the conclusions; one sentence added to 6.6 (ranking unchanged, from ch6_task_order.tex) and a half-sentence to 6.2, on author approval
2026-11-11 | Ch. 8 Summary paras 6-9 | draft: protocol paragraph extended (SPU sentence moved from 7.1), limits cut to two sentences, future work rewritten from Sec. 7.3 (compressed), on author approval
2026-11-11 | Ch. 1, Ch. 6, thesis_main | LaTeX restructure: Ch. 7 Discussion removed; Ch. 1 outline paragraph and Ch. 6 opening updated (one sentence each, CLAUDE-DRAFT); build checked, on author approval
2026-11-11 | CLAUDE.md, tracker, outlines | bookkeeping after the restructure: chapter table, structure decision, chapter deliverables, tracker locations, superseded outlines, on author approval
2026-11-11 | Summary para 2 | draft: contributions paragraph shortened to the statement of own work (repeated Sec. 1.5 wording and '38 runs' sentence removed), on author approval
2026-11-11 | Summary para 2 | text edit: 'diagnosis of the patellar failure' -> 'diagnosis of why task-specific LoRA did not learn patellar cartilage', on author approval
2026-11-11 | Summary paras 2-3 | text edit: strategies introduced ('We compared six strategies'), both data settings named in the opening of para 3 (108 vs 5-20 volumes), para 3 split before the two exceptions ('ended above 0.233'), on author approval
2026-11-11 | Summary para 2 | text edit: baseline and the five strategies named with the methods they build on; 'adaptation of these methods to VoxTell', on author approval
2026-11-11 | Ch. 6 / Summary | feedback: checked which results of Summary paras 3-7 Ch. 6 explains (explained / candidates untested / open); no edits
2026-11-11 | Ch. 6.2 | explanation: one-line answer to the research question from the results of Sec. 6.2; no edits
2026-11-11 | Summary paras 3-4 | draft: answer to the research question reframed (two groups by outcome, ceiling and exceptions with costs, joint FT lost the control task), after author's critique round; tracker D68, D69 added, on author approval
2026-11-11 | Ch. 6 Sec. 6.2, 6.6 | text edit: 6.2 conclusion aligned with the Summary (prompt-tuning link to Ch. 5, LoRA retention wording); 6.6 conclusion: 0.233 ceiling sentence restored from former 7.1 after checking cl_metrics.csv, on author approval
2026-11-11 | Summary paras 8-9 | draft: main extension reframed as the adaptation gap of the LoRA strategies (universality sentence removed); generated-replay clause (C2GR) added to future work, on author approval
2026-11-11 | Summary future work (paras 8-9) | feedback: critique of the two future-work paragraphs and proposed restructure (no edits)
2026-11-11 | Summary future work | explanation: reason for citing nested learning taken from paper_notes/nested_learning.md; version mismatch (notes arXiv v1, bib NeurIPS) flagged
2026-11-11 | paper_notes/nested_learning.md | notes: NeurIPS 2025 version read (CMS Sec. 3, forgetting argument App. C, no CL experiment in this version); reason for citing nested learning in Summary future work checked
2026-11-11 | Summary future work | outline: revised structure of the two future-work paragraphs (main extension with tests, task identity in one sentence, scope)
2026-11-11 | Summary future work (paras 8-9) | draft: two paragraphs redrafted from the approved outline
2026-11-11 | Summary future work (paras 8-10), Sec. 6.8 | draft: future work reframed (gap first tested against the configuration, new strategies conditional), split into three paragraphs; one sentence on the tests added to 6.8
2026-11-11 | Summary future work (paras 8-9) | text edit: test-runs sentence cut (repeated Sec. 6.8), para 9 reordered, on author approval
2026-11-11 | Summary future work (para 8) | text edit: candidates reduced to MoE-Adapters and nested learning, task-specific LoRA sentence removed, on author approval
2026-11-11 | Summary future work | draft: separate replay paragraph (other configurations, sample selection, generated replay), para on further runs reduced, on author approval
2026-11-11 | Summary future work | text edit: paragraphs reordered (main extension, further runs, replay, scope), on author approval
2026-11-11 | Summary future work | feedback: paragraph split checked, no merge recommended (no edits)
2026-11-11 | Summary future work (replay para) | text edit: replay paragraph compressed to two sentences, on author approval
2026-11-11 | Summary (whole chapter) | feedback: honest critique of the full chapter, numbers checked against ch6 tables (no edits)
2026-11-11 | Ch. 6.8 opening | text edit: two overview paragraphs merged into one, 'configuration' clash removed (also first para), on author approval
2026-11-11 | Summary (RQ answer, paras 3, 5, 6, future work) | draft: explicit answer paragraph and evidence paragraphs reworded on author approval; claims checked in eval matrices
2026-11-11 | Ch. 6.8 (scope of few-shot runs) | text edit: reason 'time available' added as opening phrase on author approval; advice on whether to state it
2026-11-11 | Ch. 6.8 (scope of few-shot runs) | text edit: reason reworded as priority to the full-split comparison, author's choice
2026-11-11 | Summary (paras 3-6) | text edit: evidence cut to key numbers, exceptions paragraph rebuilt, on author approval; 'kept most' checked in eval matrices
2026-11-11 | Summary (protocol, few-shot, limits, future work) | text edit: points 5-6 of the critique applied on author approval
2026-11-11 | Summary (whole chapter) | feedback: honest assessment on author request, no edits
2026-11-11 | Summary (answer, exceptions paragraphs) | text edit: one-sentence answer restored as topic sentence; exceptions opener refined, on author approval
2026-11-11 | Summary (answer paragraph) | text edit: Final Performance comparison sentence added on author approval; checked in eval matrices
2026-11-11 | Summary (paras 3-4) | feedback: re-check of the author's fixes for points 1-3, no edits
2026-11-11 | Summary (several paragraphs) | feedback on reviewer comments + text edits: seven fixes applied (comparison for joint FT, consistency, confound, ranking scope, protocol evidence, framing, source for l. 15)
2026-11-11 | Summary (future work) | text edit: further-runs and scope paragraphs merged, replay moved before them, on author approval
2026-11-11 | Summary (whole chapter) | feedback: third check after author's edits, no edits
2026-11-11 | Summary (l. 15) | feedback: checked support for the label-scarcity claim, no edits
2026-11-11 | Summary (l. 15) | text edit: scarcity claim replaced by conditional wording, on author approval
2026-11-11 | Summary (l. 15) | feedback: advised against 'annotation scarcity' wording, no edits
2026-11-11 | Summary (l. 15) | feedback: recommended dropping the few-labelled-volumes clause, no edits
2026-11-11 | Summary (l. 15) | text edit: few-labelled-volumes clause dropped, on author approval
2026-11-11 | Summary (paras 3 and 5) | text edit: few-shot results merged into one paragraph, patellar sentence shortened, on author approval
2026-11-11 | Summary (few-shot paragraph) | text edit: patellar sentence split into two for readability, on author request
2026-11-11 | Summary (few-shot paragraph) | text edit: grammar and flow of the patellar sentences, on author request
2026-11-11 | Appendix A (float placement) | LaTeX fix: placeins loaded, \FloatBarrier before each appendix section so tables appear before the next section; Table A.4 placement [!tb]
2026-11-11 | Appendix A.1 | text edit: removed two sentences that repeated Sec. 4 (same set per k, nested, same test volumes); provenance kept as source comment, on author approval
2026-11-11 | Appendix A.1 (Table A.1 caption) | text edit: caption states that volumes are named as in the dataset releases, on author approval
2026-11-11 | Appendix A.2 | text edit: sentence on how the parameter tables are generated turned into a source comment, on author request
2026-11-11 | Sec. 6.2 / App. A.2 | text edit: sentence on the unlogged distillation term moved from App. A.2 to Sec. 6.2 after the lambda sentence, on author approval
2026-11-11 | Appendix A.2 | text edit: run history (reruns, code-version dates, task-boundary evidence) removed, software and resume paragraphs shortened to reproduction info; defense point D32 updated, on author approval
2026-11-11 | Appendix A.2 | LaTeX fix: unescaped underscore in a \todo (introduced by Claude) removed; corrupted aux files cleaned and thesis rebuilt
2026-11-11 | Appendix A.2/A.3 (Tables A.3, A.4 captions) | text edit: captions corrected and tightened (ensemble-interval row explained, xi = 1 for the no-scaling run, run history removed, references attached to the right terms), on author request
2026-11-11 | Appendix A.3 (Table A.4 caption) | text edit: no-scaling explanation shortened, on author approval
2026-11-11 | Appendix A.4 | text edit: section shortened (opening, untested 1/t explanation and conclusion paragraph removed; closing caveat for both components), defense point D70 added, on author approval
2026-11-11 | Appendix A (all sections) | text edit: style pass (insertions, tense, informal wording, wrong reference to parameters in A.3, ranks added to Fig. A.1 caption); script: matrix captions as "Evaluation matrix of <strategy>" in make_appendix_tables.py, tables regenerated; on author approval
2026-11-11 | Appendix A.5 | text edit: sentence explaining the run identifiers in the matrix captions, on author approval
2026-11-11 | Appendix A.5 | script: matrix sort key with replay and epoch tie-breakers (consistent order in the few-shot group), tables regenerated; LaTeX fix: \raggedbottom for the matrix pages
2026-11-12 | Appendix A.6 | text edit: provenance clause removed from the opening; Fig. A.1 caption names the loss and pairs the tasks with their order, on author approval
2026-11-12 | Ch. 2 (Table 2.2) / List of Tables | LaTeX fix: short caption for Table 2.2 so the List of Tables shows one line
2026-11-12 | Ch. 4, Ch. 6 | text edit: experiment names aligned (few-shot experiment introduced in Sec. 6.4; "LoRA rank experiment"; Ch. 4 "few-shot settings"; gamma_r statement in 6.8 extended to the whole rank experiment), on author approval
2026-11-12 | List of Abbreviations (abbreviations.tex; Ch. 1, 3, 5, 6) | LaTeX fix: entries sorted alphabetically, unused IQR removed, CPU/GPU/SGD added and their uses converted to \gls; template untouched
2026-11-12 | List of Abbreviations / CLAUDE.md | LaTeX fix: CPU and GPU removed from the list and written plainly again (author decision); CLAUDE.md acronym rule extended by this exception
2026-11-12 | whole thesis | feedback: submission-readiness assessment and three-day plan
2026-11-12 | style / CLAUDE.md | outline: voice sheet (style/voice_sheet.md) from the author's Diagnostics paper, with two example rewrites of Sec. 6.2 l. 143-150; CLAUDE.md: spelling reason, tier-3 context openers, voice pointer (author approved)
2026-11-12 | whole thesis | outline: submission checklist (reviews/submission_checklist.md) merged from the author's list and CLAUDE.md, with workflow
2026-11-12 | whole thesis | outline: order of execution added to reviews/submission_checklist.md
2026-11-12 | Ch. 1 | draft: voice pass B (proposal in reviews/voice/ch1_introduction.tex, not applied); B2 tables and figures regenerated, unchanged
2026-11-12 | whole thesis | outline: decision list of all 30 todos and the Ch. 1 questions (reviews/todo_decisions.md); bib-entry-adder started for the two cite todos
2026-11-12 | Ch. 2, Ch. 6 / bibliography | script (agent): bib-entry-adder added isensee2026nnunet and bommasani2021opportunities with provenance; results added to reviews/todo_decisions.md
2026-11-12 | Ch. 1, 2, 5, 6, App. | LaTeX fix: applied Ch. 1 voice proposal and the author's todo decisions (30 markers resolved, two citations added); recommended oral answers D34, D65, D70 (reviews/todo_decisions.md)
2026-11-12 | whole thesis | script: reviews/tools/lint_thesis.py (style lint) and check_numbers.py (B1 number tracing); run on Ch. 1 (one serial comma fixed); proofreader subagent started on Ch. 1
2026-11-12 | Ch. 1 | LaTeX fix: 19 proofreader findings applied (mostly reverting voice-pass merges), build clean; voice-sheet lessons added; citation-verifier started on Ch. 1
2026-11-12 | Ch. 1 | draft: one sentence introducing the six strategies (Sec. 1.4), author approved
2026-11-12 | Summary | draft: voice pass B proposal (reviews/voice/summary.tex, not applied); Ch. 1 l. 151 'five continual-learning strategies' (author approved); proofreader started
2026-11-12 | Ch. 1 / Summary | feedback (agents): Ch. 1 citation-verifier (reviews/citations_ch1_2026-11-12.md; two missing citations added: VoxTell Table 1, SKM-TEA Sec. 2); Summary proofread saved and 12 fixes to the proposal
2026-11-12 | Ch. 1 / Summary | LaTeX fix: Summary voice proposal applied (author approved); Ch. 1 six citation-verifier recommendations applied (author approved); build clean; citation-verifier started on Summary
2026-11-12 | Summary | LaTeX fix: four citation-verifier recommendations applied in Future Work (author approved); report reviews/citations_summary_2026-11-12.md
2026-11-12 | Ch. 6 | draft: voice pass B proposal rounds 1-2 (reviews/voice/ch6_experiment_results.tex, not applied); round-1 proofread applied (16 fixes); round-2 proofreader running
2026-11-12 | Ch. 6 | LaTeX fix: round-2 proofread applied to the Ch. 6 proposal (21 fixes); full diff reviews/voice/ch6_diff.txt
2026-11-12 | Ch. 6 | LaTeX fix: Ch. 6 voice proposal applied (author approved, incl. three pre-existing content corrections); build clean; citation-verifier started
2026-11-12 | Ch. 5 | draft: voice pass B proposal (reviews/voice/ch5_method.tex, 20 edits, not applied); proofreader started
2026-11-12 | Ch. 5 | LaTeX fix: proofread applied to the Ch. 5 proposal (15 fixes; one citation added, zhang2023, author to approve)
2026-11-12 | Ch. 5, notation | LaTeX fix: Ch. 5 proposal applied, notation S = strategy (author approved); script reviews/tools/check_refs.py (citation/cross-reference density and placement) run on Ch. 1, 5, 6, Summary; Ch. 6 citation-verifier report reviews/citations_ch6_2026-11-12.md
2026-11-12 | Ch. 1, 5, 6, Summary | LaTeX fix: 12 citation/cross-reference changes (over-citing removed, Ch. 6 verifier findings; author approved); build clean; tracker D71, D72; citation-verifier on the changed sentences started
2026-11-12 | Ch. 2, 3, 4, App. A | draft: voice pass B proposals (reviews/voice/{related_work,background,data_description,appendix}.tex, not applied); proofreaders running
2026-11-12 | Ch. 6, Summary | LaTeX fix: six citation fixes after re-verification (locators, MoE-Adapters/nested-learning support, C2GR claim, Hu et al. condition); second re-verification started
2026-11-12 | Ch. 4, App. A | LaTeX fix: proofread applied to the proposals (10 fixes, one citation added)
2026-11-12 | Ch. 4, App. A | LaTeX fix: proposals applied (author approved; 'only because' softened to 'mainly because'); citation-verifier on Ch. 4 started
2026-11-12 | Ch. 6 | LaTeX fix: Hu et al. sentence reworded (close paraphrase flagged by citation-verifier)
2026-11-12 | Ch. 2, 3 | LaTeX fix: proofread applied to the proposals (49 fixes)
2026-11-12 | Ch. 2, 3, 4 | LaTeX fix: Ch. 2 and 3 applied, Ch. 4 citation fixes (5 citations added, 3 rephrasings; author approved); build clean; citation-verifiers on Ch. 2, Ch. 3 and changed sentences; bib-entry-adder for AeroPath (author request)
2026-11-12 | bibliography | script (agent): AeroPath entry upgraded to PLOS ONE 2024 (author request), build clean; tracker D75
2026-11-12 | whole thesis | feedback (agents): B6 reference check script (reviews/tools/check_floats.py, all referenced); B4 bibliography check and the seven FINAL_REVIEW passes started as report-only subagents; Ch. 2 citation-verifier paused (author request); Ch. 3 citation report saved (reviews/citations_ch3_changed_2026-11-12.md), fixes deferred
2026-11-12 | whole thesis | outline: next steps after usage limit (reviews/next_steps.md): fresh session, resume stopped agents two at a time, D pass 6 by script
2026-11-12 | Ch. 1, 3, 4, 6 | LaTeX fix: Ch. 3 citation findings (De Lange locator x2, VoxTell locator, loss wording, CPE-CLIP Sec. 2.3, SKM-TEA tracks, Hu et al. as direct quote); paper_notes/delange2022.md corrected; Ch. 2 verifier resumed; re-verification of the six changes started
2026-11-12 | Ch. 1, 2, 3 | LaTeX fix: Ch. 2 citation-verifier findings (CA-SAM derived numbers removed, Chen et al. shots, Silva-Rodriguez, MSLoRA-CR, MoE-Adapters, SEER, SAT, four locators); Ch. 1 De Lange citation removed from own reasoning; CPE-CLIP and VoxTell locators; build clean; final re-verification started
2026-11-12 | Ch. 2 | LaTeX fix: SAT sentence wording after final re-verification; step 1 complete
2026-11-12 | front matter | draft: English abstract (author approved) and German translation (to be checked by a native speaker) in thesis_main.tex, marked CLAUDE-DRAFT; each on its own page
2026-11-12 | whole thesis | feedback: final review passes D1 structure, D2 technical, D3 citations (scope), D4 consistency, D5 language, D7 examiner (report-only subagents) and D6 formal (scripts), B4 bibliography; reports in reviews/pass1-7_*.md and reviews/b4_bibliography.md; no thesis edits
2026-11-12 | whole thesis | feedback: sorted all D-pass and B4 findings into reviews/fix_list_2026-11-12.md (29 mechanical items, 37 author decisions); no thesis edits
2026-11-12 | front matter, Ch. 1-6, App. A, notation, scripts | LaTeX fix: mechanical items M1-M29 of reviews/fix_list_2026-11-12.md (todonotes removed, template warnings filtered with silence, tocdepth 3, cover dates 01.06./30.11.2026 and place of birth per author, method.tex l. 217 per author (Q5a), 6 citations/locators added, gls for SGD/EWC/SAM, notation entries, results captions completed, table labels via scripts + run_all, tracker statuses); bib fixes M6-M12 delegated to bib-entry-adder; changed citations sent to citation-verifier; not built
2026-11-12 | Ch. 1, 2, 3, 5, 6, 7, App. A, notation, scripts, CLAUDE.md | LaTeX fix + draft: author decisions Q6-Q37 of reviews/fix_list_2026-11-12.md applied as recommended (wording corrections, hedges, gamma_r confound, v1.1 exposure and single-prompt caveats in 6.8, oracle routing, Q24 implementation details, O(.) complexity paragraph drafted, ensemble details to App. A.4, loss values to App. A.6, 6.2 conclusion condensed, Sec. 1.4 metrics shortened, objective 4 narrowed, q_{g,v} -> w_{g,v}, tense in Ch. 6, dropout row in tab:app-hparams); tracker D76-D82; changed citations sent to citation-verifier; not built
2026-11-12 | front matter, Ch. 6 | LaTeX fix: siunitx warnings redirected (l3 msg), bibliography emergencystretch, Hu et al. sentence and own gamma_r reasoning reworded after citation re-check; build clean (137 pp., no warnings); cover end date and CLAUDE.md dates per author
2026-11-12 | whole thesis | feedback: combined diff of both sessions checked (no markers lost, all edits present, no duplicates); abstract few-shot wording flagged, kept by author decision
2026-11-12 | whole thesis | LaTeX fix: 243 CLAUDE-DRAFT markers removed at the author's explicit request (conflict with the CLAUDE.md rule pointed out first); record of all drafted paragraphs saved to reviews/claude_draft_record.md; build clean
2026-11-12 | CLAUDE.md | chapter status table updated to final text (markers removed, record file); rebuild after disk-full check: clean
2026-11-12 | front matter (notation) | LaTeX fix: notation table checked in the PDF; group headings kept with their rows (\*), Strategies group now starts on p. xiii; build clean
2026-11-12 | front matter (notation), Ch. 3 | LaTeX fix: notation checked by script both ways (all 103 listed symbols used; MHA/head_i and Up/ConvBlock added to the table; ConvBlock explained in Sec. 3.1.3); build clean
2026-11-12 | whole thesis, submission | feedback + script: final read of the rendered PDF by two report-only readers (reviews/final_read_2026-11-12.md); clean LaTeX source package assembled in submission/latex_sources (59 files, builds standalone); no thesis edits
2026-11-12 | Ch. 2, 3, 5, 6, App. A, notation, bib | LaTeX fix from the final PDF read: De Lange shorthand DeL+22, model-card title, short running head Sec. 2.3, 'a separate MLP', 'same order' dropped, 'Three further differences', Table 5.1 moved to its first reference, App. A.3 near-empty page removed (FloatBarrier), notation rows split (p; lambda/L_KD) with correct sections, 'LoRA ranks' in Fig. 6.2 caption; build clean
2026-11-12 | Ch. 6, Summary, front matter | LaTeX fix: four text decisions applied (6.6 repetition removed, Chen et al. moved to the 6.2 conclusion, Summary own-work sentence split, explicit answer to the RQ); abstracts replaced by the author's shortened English (serial comma, 'and lost the control task' added) and Claude's German translation, both on one page (each under half a page); stale submission folder deleted; build clean
2026-11-12 | front matter | LaTeX fix: abstract layout reverted to the original template (both on one page, \vspace{5.0cm} between); both abstracts shortened to fit (risk sentence, 'separately from ...' clause and 'No strategy combined ...' sentence dropped; 'one after another' merged; 'three of the six strategies'); proposal for author approval; build clean
2026-11-12 | front matter | LaTeX fix: author's 165-word abstract restored (with the approved tweaks) in the template's own heading layout; template placeholder gap \vspace{5.0cm} removed (1 cm still overflowed by 2 lines); both abstracts on page v, each under half a page; build clean
2026-11-12 | front matter | LaTeX fix: abstracts EN/DE: numbers (Adaptation 0.781, at most 0.485) removed, few-shot scope moved to its own sentence (author approved); fit on page v checked; build clean
2026-11-12 | front matter (notation) | LaTeX fix: every notation meaning checked against its definition in the text; Up (stage s+1 to s) and beta_t (CPE-CLIP's scale of session t) corrected; build clean
2026-11-12 | Ch. 1-6 | feedback: float positions checked against first references by script (all floats in their own section, at most 3 pages after the first mention; Table 2.1 one page before, on the facing page); no edits
2026-11-12 | Ch. 2 | LaTeX fix: Table 2.1 now after its first reference (reference sentence moved up to the closest-works paragraph as 'contrasts our setting with these works'; table input moved after that paragraph); build clean
