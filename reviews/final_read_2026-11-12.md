# Final read of the rendered PDF (2026-11-12)

Two report-only readers (PDF pp. 1–68 and 69–137, every page rendered and read) plus whole-PDF checks in the main session. Printed page = PDF page − 14 from Ch. 1 on.

Whole-PDF checks: build clean (one template overfull box on the cover), A4, all fonts embedded, no "??", no undefined references or citations. PDF metadata (title, author) empty.

## Must fix
- Abstracts longer than half a page (chair Sec. 1.3): German 23 lines ≈ 63 % of the text block, English 20 lines ≈ 57 %; cut 3–5 lines each (author).
- Citation label "[De +22]" (De Lange et al.) with a space, in text (PDF 16, 17, 20, 26, 32, 46, 62, 64, 91) and bibliography (PDF 125): give the bib entry a label/shortauthor.
- PDF 99 (p. 85), App. A.3: heading + 4 lines, page otherwise empty; with the two float pages before it, three near-empty pages in a row.

## Should fix
- PDF 27 (p. 13): running head of Sec. 2.3 runs into the page number; needs a short title.
- PDF 30 (p. 16): "an multilayer perceptron (MLP)" (glossary first-use expansion after "an").
- PDF 41 (p. 27): Sec. 3.2 says Sec. 5.3 presents the strategies "in the same order"; it does not (3.2: LoRA, ZSCL, CPE-CLIP; 5.3: LoRA, replay, prompt tuning, distillation).
- Table 5.1 first referenced PDF 62 (p. 48), floats to PDF 67 (p. 53).
- PDF 86 (p. 72): gap of 4–5 lines before 6.7 and stretched paragraph spacing; PDF 88 (p. 74) larger gaps before "Second" and "Third".
- Sec. 6.6 (PDF 85–86): "first task learned poorly" + training-loss sentence repeated almost verbatim in the closing paragraph.
- Sec. 6.8 last paragraph (Chen et al., prior-work comparison) contradicts 6.8's roadmap; rules place prior-work comparison in the 6.2 conclusion.
- Summary para 2: "Our own work is the evaluation protocol, which combines … and a pretrained-model reference, the adaptation …" hard to parse; split.
- Summary: research question answered in substance but not marked as the answer (CLAUDE.md asks for an explicit answer).
- Bibliography [Hug26] (model card): title starts "[CVPR2026] VoxTell: …", no author/organisation, no year.
- Abstract few-shot wording (all strategies at every k) — author decided 2026-11-12 to keep.

## Minor
- Blank versos carry running heads (PDF 2, 4, 10, 14, 22, 48, 54, 118, 120, 122); "List of Abbreviations" head mixed case vs upper case for the others.
- Notation "Sec." entries: λ; L_KD → L_KD first defined in 5.3.5; p; p_t; p_c → p_t in 3.2.1, p_c in 5.1.
- "Two further differences come from the implementation" followed by three (PDF 60, p. 46).
- PDF 33 (p. 19) only 40 % filled (Table 2.2 moves on).
- Table 4.1: URLs magenta vs blue elsewhere; footnote uses "NIfTI" before its acronym is introduced.
- PDF 53 (p. 39): typewriter footnote with wide word gaps.
- Table 2.1 caption: control task "evaluated after the sequence" vs own protocol "after every stage".
- Ch. 4 opening promises "which properties of the data limit the conclusions"; no such section.
- "AdamW" used without introduction (PDF 42, p. 28).
- Table 2.2 vs text: Zhang/Liu comparison (PLOP vs pseudo-labels); MedSeqFT "five CT, five MRI tasks" vs "five segmentation tasks".
- Fig. 6.2 caption: "ranks as in Table 6.2" → "LoRA ranks".
- Differences in the text 0.001 off from subtracting rounded table values (0.059, 0.021, 0.170, 0.117): computed before rounding; one sentence in 6.1.3 would pre-empt the question.
- 6.6 promises "a possible explanation", 6.8 gives two.
- Fig. 6.3: loss starts at about 1.15–1.2, text says "about 1.0".
- Table A.2: "validation every 24 epochs" ambiguous.
- List of Abbreviations: uneven spacing; List of Tables lists only A.1–A.4 (Table A.5 is cited from the main text).
- Running head on PDF 115 shows A.6 while the top is A.5's table (standard LaTeX).
- Bibliography: DOI repeated as URL in ~9 entries; visited dates in US format (11/07/2026); event date and month repeated in proceedings.
- Summary ≈ 2.7 pages of text, 3.2 with heading: at the lower edge of 3–4 pages.
