# Citation check: Ch. 3 + changed sentences in Ch. 4/6 (2026-11-12), saved by the main session

Ch. 3: 42 citations, 38 supported, 3 partly, 1 cannot verify (Dice 1945, no PDF). Changed sentences: 7 supported, 2 partly.

Must fix
1. background.tex (Final Performance paragraph): De Lange "soft upper bound" cited as Sec. 5; correct locator Sec. 6.2.1. Same error in paper_notes/delange2022.md §4 (also affects introduction.tex, which cites [Sec.~5] for the same claim).

Should fix
1. experiment_results.tex (Sec. 6.8): Hu et al. say "roughly the same ... if we scale the initialization appropriately"; the sentence drops hedge and condition, and the SGD contrast is our inference.
2. background.tex (VoxTell parts): "frozen" text encoder not in Secs. 1 and 3; add Sec. 5 or Suppl. Sec. A.2.
3. background.tex (CPE-CLIP setting): "task identity is not given at evaluation" is in CPE-CLIP Sec. 2.3, not cited.
4. VoxTell cited as CVPR 2026, locators checked in arXiv v1 (Suppl. A/A.2, Eqs. 2-7, Fig. 2, Suppl. Tables 7, 9, 10): compare with the CVPR supplement before submission.

Minor
- VoxTell loss: "sum" of BCE and Dice not stated ("combines").
- data_description.tex: "is distributed in two benchmark tracks" -> "enables two benchmark tracks".
- rsLoRA theorem: "in expectation over initialization"; Sec. 2.1 belongs to the previous sentence.
- Optional locators: van de Ven Sec. 2.4; Desai Sec. 4.1 (four tissues), Secs. 4.1-4.2 (one scan per patient); LwF Sec. 3; Vaswani Sec. 3.2.
- Uncited minor claims in background.tex: positional encoding (Vaswani Sec. 3.5); "single word to clinical sentence" (VoxTell abstract); 6^3 voxels (derived); combination at s = 0 (code); distillation as regulariser (De Lange Sec. 3.2); ZSCL matrix without stage 0 (Fig. 4b).
