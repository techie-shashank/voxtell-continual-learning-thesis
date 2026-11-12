# B4 — Bibliography check (2026-11-12)

Report-only subagent pass (fresh agent, new session). `thesis/literature.bib` not edited. Saved by the main session.

**Scope.** 130 entries, no duplicate keys; 80 cited (biber: "Found 80 citekeys"); every cited key resolves. `thesis_main.blg` (Biber 2.21, 12 Nov 17:24): no warnings or errors. Rendered bibliography checked with `pdftotext`.

**Most important finding: protect acronyms in titles.** `trad-alpha` applies `\MakeSentenceCase*` to titles of article, inproceedings, inbook, misc, online (`trad-standard.bbx:92`); unprotected acronyms print lower case. Confirmed in the PDF.

## 1. Cited entries: wrong lowercasing (title not brace-protected) — must fix
| Key | Prints as |
|---|---|
| universeg | "Universeg: universal…" |
| 3d_unet | "3d u-net: learning…" |
| cheng2023sammed2d | "Sam-med2d" |
| liu2026continuallearningvlmssurvey | "…for vlms…" |
| gonzalez2023lifelong | "Lifelong nnu-net" |
| chen2026fewshotcontinuallearning3d | "…for 3d brain mri…" |
| Zhang_2025 | "…over lora…" |
| kalajdzievski2023rankstabilizationscalingfactor | "…with lora" |
| Liu_2023 | "Clip-driven universal model…" |
| guo2025continuallearningdrivenmodelaccurate | "…anatomies in ct" |
| liu2026medsam3delvingsegmentmedical | "Medsam3: delving…" |

Hyphenated words ("Few-Shot", "Vision-Language") are lowercased correctly.

## 2. Cited entries: missing required fields
**Articles**
- **Ma_2024**: no `pages`; prints "15(1), January 2024". Article number **654** (PMC10803759, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10803759/). Must fix.
- **theekshana26fewshot**: no `pages`; `articleno = {11}`, `numpages = {36}` not printed by trad-alpha, entry shows only "58(1)". Should fix. Also journal abbreviated ("ACM Comput. Surv.") unlike all others (minor); `year = 2025` vs `issue_date = January 2026` (minor).
- **gonzalez2023lifelong**: no `doi`; `publisher = {Nature Publishing Group UK London}` mixes publisher and place. Should fix.

**@inproceedings / @inbook** (booktitle, date, pages, place, editor, publisher)
- **desai2021skmtea**: missing pages, editor, publisher, location, volume (NeurIPS Datasets and Benchmarks). Core dataset paper. Must fix.
- **memory_replay_cropping**: missing series/volume (LNCS), doi. Should fix.
- **3d_unet**: missing series/volume (LNCS), doi, place. Should fix.
- **Chaudhry_2018** (@inbook): missing editor, LNCS series/volume, place. Should fix.
- **Ozdemir_2018** (@inbook): missing series/volume; editors print oddly after "Proceedings, Part IV." Should fix.
- **van_de_Ven_2025** (@inbook): missing editor of the reference work, place (editor not looked up). Should fix.
- **universeg, Kirillov_2023_ICCV, Zhang_2024_CVPR, zhou2022cocoop, he2015delving**: no publisher, no place; Kirillov, Zhang_2024_CVPR, cocoop also no DOI. Should fix.
- **rokuss2025voxtellfreetextpromptableuniversal, chen2025forgingdynamicmemoryretrievalguided**: CVPR 2026, no publisher/DOI, only CVF URL; IEEE version may not exist yet. Minor.
- **Zhang_2025** (ACM MM): no editor, no `eventdate`; non-standard `collection`, duplicated `series = {MM ’25}` with curly apostrophe. Minor.
- **Most other proceedings** (CVF/IEEE, ICCV/CVPR workshops, AAAI, WACV): no `editor`; these venues usually list none. Mention once. Minor.
- **hu2022lora** (ICLR): no pages, no place; ICLR has neither. Acceptable.
- **che2026loraloraparameterefficientarchitecture**: `number = 24` on inproceedings prints "volume 40 of number 24"; use `issue` or move into booktitle. Should fix.

**@misc / @online**: all have `url`; @online have `urldate`; arXiv @misc lack `urldate` (acceptable, eprint fixes version). **rokuss2026voxtellmodelcard**: no author, no date (minor).

## 3. arXiv preprints among cited entries
No peer-reviewed version found for any; fine to keep as arXiv:
- cheng2023sammed2d (2308.16184), liu2026continuallearningvlmssurvey (2508.04227), chen2026fewshotcontinuallearning3d (2602.23533), guo2025continuallearningdrivenmodelaccurate (2503.12698), kalajdzievski2023rankstabilizationscalingfactor (2312.03732), ye2025medseqft (2509.06096; TMI template, no acceptance found).
- liu2026medsam3delvingsegmentmedical (2511.19046): v1 24 Nov 2025, v2 14 Sep 2026, no journal-ref (https://arxiv.org/abs/2511.19046); authors match the bib.
- hinton2015distilling, hendrycks2016gelu, bommasani2021opportunities, zhang2025qwen3embedding (technical report), baweja2018continuallearningmedicalimaging (workshop): generally arXiv-only.
- li2026c2gr (2606.23473), wang2026beyondforgetting (2605.06160): posted May/June 2026, **not checked** for a later venue; check just before submission (minor).

No cited entry uses arXiv where a published version is known; earlier upgrades (støverud, chen2025forging, zou2023, …) in place.

## 4. Duplicates
- **Zhao_2024** (unused) and **zhao2025foundation-9de** (cited): same DOI 10.1038/s41592-024-02499-w (2024 online vs 2025 issue). Delete the unused one. Should fix.
- støverud2023… (PLOS ONE) and aeropath_zenodo (Zenodo dataset): different works, correct.

## 5. Consistency issues (cited entries)
- Unicode en dash in `pages`: Kirkpatrick_2017, Chaudhry_2018, van_de_Ven_2025 (bib l. 340, 811, 556); Chaudhry's booktitle also has "–". Minor.
- Single hyphen in pages: universeg, delange2022, Kirillov_2023_ICCV, Zhang_2024_CVPR; rendered correctly. Minor.
- Non-ASCII key `støverud2023aeropathairwaysegmentationbenchmark`: builds, portability risk; renaming needs every `\cite` changed. Minor.
- **desai2021skmtea**: key on the line after `@inproceedings{` (grep-based tools can miss it); "Christopher Re" should be "R{\'e}". Minor.
- **NIPS2017_3f5ee243**: editor "U. Von Luxburg" parsed with first name "U. Von", prints "U. V. Luxburg"; should be `{von Luxburg}, U.` Should fix.
- bommasani2021opportunities: `and others` (only truncated entry; acceptable for 100+ authors). Minor.
- Mixed DOI/URL: Ma_2024, Kirkpatrick_2017, Liu_2023, D_Alessandro_2023, Zhang_2025, Chaudhry_2018, van_de_Ven_2025 have `url = http://dx.doi.org/...` duplicating the DOI; Liu_2023 and D_Alessandro_2023 lowercase DOIs. Minor.
- Nature journal publisher inconsistent (Ma_2024 vs gonzalez2023lifelong vs none). Minor.
- `isensee2018…` is the 2021 Nature Methods paper (key only; label from `year`). Minor.
- efron1993bootstrap: publisher Chapman & Hall, DOI of the Springer reprint. Minor.
- Kirillov_2023_ICCV: `month = {10}` vs month macros elsewhere. Minor.
- Malformed DOIs (full URL in `doi`) only in unused entries: MP-COVID-19-SegBenchmark, PARISI201954, DAYARATHNA2024103046.

## 6. Unused entries (50, not printed)
DAYARATHNA2024103046, Degerli_2022, Litjens_2017, MP-COVID-19-SegBenchmark, PARISI201954, Zhao_2024, baharoon2025rexgroundingct3dchestct, baid2021rsnaasnrmiccaibrats2021benchmark, bassi2025learningsegmentationradiologyreports, carion2026sam3segmentconcepts, chen2024lowrankmoe, dolz2019hyperdensenethyperdenselyconnectedcnn, douillard2021ploplearningforgettingcontinual, esmaeili2026clopa, fm_review, frascaroli2024clipgenerativelatentreplay, french1999catastrophic, gonzalez2023wrongcontinuallearningmedical, harnessprogresscancer, heller2023kits21challengeautomaticsegmentation, huang2024classincrementallearningclipadaptive, icarl2017, ilharco2022patchingopenvocabularymodelsinterpolating, karani2018lifelonglearningapproachbrain, kemker2017measuringcatastrophicforgettingneural, li2018hdenseunethybriddenselyconnected, luo2025empiricalstudycatastrophicforgetting, ma2021abdomenct1kabdominalorgansegmentation, ma2023unleashingstrengthsunlabeleddata, memmel2021adversarialcontinuallearningmultidomain, milletari2016vnet, nauffal2024noninvasive, newgenerativereplayapproach, oktay2018attentionunetlearninglook, pham2000current, qazi2026clmedicalimaging, shu2025regcl, text3dsam, textmatch2024, ukbiobank, wang2019organrisksegmentationhead, wang2020nonlocalunetbiomedicalimage, wang2023orthogonalsubspacelearninglanguage, wang2023tracecomprehensivebenchmarkcontinual, wang2024comprehensivesurveycontinuallearning, weightedresunet, yoon2018lifelonglearningdynamicallyexpandable, yu2026recentadvancesmultimodalcontinual, yushkevich2006itksnap, zou2023segment

## Suggested order of fixes (bib-entry-adder, when the author asks)
1. Brace-protect the 11 titles in §1.
2. Ma_2024: `pages = {654}`.
3. Complete desai2021skmtea.
4. theekshana26fewshot: pages or eid.
5. Complete 3d_unet, memory_replay_cropping, Chaudhry_2018, Ozdemir_2018 (series, volume, DOI, editor, place; @inproceedings rather than @inbook).
6. Fix che2026 number and the Von Luxburg editor name.
7. Delete Zhao_2024.
