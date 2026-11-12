# Voice sheet

Source: my paper "Improving Feature Representation with Hybrid Mamba-LSTM Model for Cardiovascular Disease Classification Using ECG" (Diagnostics submission, version 19 January 2026), the only text written entirely by me. Line numbers below refer to that PDF.
Only features that occur several times in the paper are listed. Where this sheet conflicts with CLAUDE.md (writing style, tier rules, terminology), CLAUDE.md wins.

## 1. Features to use

**1.1 Purpose first, then the action.** "To X, we Y." is my standard way to justify a step.
- "To address the class imbalance in the datasets, we employed focal loss instead of standard cross-entropy loss." (l. 241–242)
- "To match the length and sampling frequency of the PTB-XL dataset, we applied a Butterworth bandpass filter …" (l. 133–134)
- Also l. 159, 182, 231, 300.
Use for design decisions in Ch. 4–6. Not in every sentence of a paragraph.

**1.2 Ranked results with values in parentheses.** The winner first, then "followed by", with "(metric: value)".
- "the hybrid model was the best in the PTB-XL dataset (F1: 0.847), followed by the standalone LSTM (F1: 0.829) and Mamba (F1: 0.827)" (l. 262–263)
- Also l. 16–17, 275–276, 348–350.
Use when a sentence compares several strategies or values. A single value that is the point of the sentence stays inline ("a control-task drop of 0.979").

**1.3 Hedged explanation after an observation.** Observation first, then a separate sentence that explains it with a hedge.
- "This can be attributed to the differences in the embeddings used for linear probing." (l. 283–284)
- "this can be due to class imbalance, however, misclassifications can also be attributed to weak patterns …" (l. 288–290)
- "This suggests that while the LSTM captures temporal dependencies, it lacks …" (l. 311–312)
Only where the thesis already gives an explanation. Never add new ones (CLAUDE.md, authorship).

**1.4 Short context-setting openers.** A paragraph or sentence starts by naming the case it is about.
- "In the multi-label setting, …" (l. 275), "In case of the binary task, …" (l. 261), "Regarding the training and inference times, …" (l. 292), "In our case, …" (l. 235)
Keep them short (a few words). No "it can be observed that" (CLAUDE.md tier 3).

**1.5 Concession before the claim.**
- "Although the downstream task is classification, we aim to (empirically) show …" (l. 172–173)
- "Although these models have achieved promising classification performance, recent research has emphasized …" (l. 42–43)
- Also "Despite …" (l. 67, 270), "despite producing …" (l. 351).

**1.6 Explicit turns.** "However," at the start of a sentence, "In contrast," and occasionally "On the one hand … On the other hand" (l. 49, 267, 313, 161–164). One turn per point, not chained.

**1.7 "We" for decisions and actions, passive for routine procedure.**
- "we applied" (l. 134, 149), "we used" (l. 187), "we performed" (l. 248, 277)
- "The models were trained with …" (l. 243), "The analysis was performed on …" (l. 301), "The PTB-XL dataset was split …" (l. 123)

**1.8 Small parenthetical asides.** References and examples in brackets inside the sentence: "(see Table 1)" (l. 261), "(Section 2.1)" (l. 97), "(e.g. the 12-lead ECG waveforms)" (l. 185). The thesis writes "for example" / "such as" instead of "e.g." and "i.e." (checked 2026-11-12: neither occurs in the text); keep it that way.

**1.9 Limitations named plainly.** "Several limitations should be considered." followed by one sentence per limitation, each with its consequence (l. 353–359).

**1.10 Sentence length.** Mostly medium to long (about 20–35 words), with a clause joined by "while", "whereas" or "although". Short sentences occur, mostly for a turn or a hedged explanation.

**1.11 Occasional summary opener.** "Overall, …" for a paragraph that sums up (l. 19, 260, 320). At most once per section.

## 2. Conventions

- **Serial comma** in lists of three or more ("PTB-XL, CPSC2018, and Chapman", l. 9, 95). The thesis is currently mixed; the voice pass makes it consistent.
- **Numbers:** three decimals for own results, as CLAUDE.md requires; "(metric: value)" in ranked comparisons (1.2).
- **Spelling:** British -ise (CLAUDE.md), although the paper is in US spelling.

## 3. Not taken from the paper

| In the paper | Why not | CLAUDE.md rule |
|---|---|---|
| "paramount importance" (l. 26), "revolutionized" (l. 38), "to leverage the complementary strengths" (l. 76), "comprehensive understanding" (l. 90), "synergy" (l. 344), "excels" (l. 342), "highlighting" as filler (l. 73) | generic layer, not voice | banned vocabulary |
| "it can be observed that" (l. 267, 282) | hides the subject | tier 3, subject first |
| "The F1-score, defined as the harmonic mean …, provides …" (l. 215–216) | definition between subject and verb | tier 1 |
| "We demonstrate that this hybrid model produces more robust and generalizable ECG embeddings" (l. 82–83) with mixed results | claim stronger than the evidence | defensibility |
| multi-label / multi-class; Hybrid / hybrid / Serial Hybrid | two terms for one concept | terminology |
| "…, however, …" joined by commas (l. 280, 289) | comma splice | grammar: new sentence or semicolon |
| "have being considered" (l. 5), "Tables 2, 3, and 4 summarizes" (l. 257), "is obtained was obtained" (l. 268), "defined ass" (l. 193) | slips | grammar |

## 4. Rules for the voice pass

1. Meaning, numbers, citations, cross-references, `\todo` and `% CLAUDE-DRAFT` markers stay unchanged. Sentence order may change within a paragraph, never across paragraphs.
2. No new explanations, interpretations or hedges that the text does not already contain.
3. A sentence where a voice edit would change meaning is left as it is and listed for the author.
4. Section by section, with a diff for the author to approve.
5. Not every feature in every paragraph: the aim is a consistent voice, not a pattern.
6. Lessons from the Ch. 1 proofread (2026-11-12): do not merge two separate statements into one sentence with ", and" (it caused two garden paths and a 45-word sentence); keep concessions and other fronted clauses short (about 12 words at most), otherwise use two sentences with "However,"; at most one "To X, we Y" per paragraph, and only where it states a real reason; keep "also" inside the sentence rather than turning it into "In addition,"; a "which" clause must follow the noun it refers to directly, not a citation or another noun.

## 5. Example (Ch. 6, Sec. 6.2, `experiment_results.tex` l. 143–150)

**Current text**

> In the primary metrics, the strategies formed two groups (…). The two strategies that update the pretrained weights adapted most and forgot most, whereas the LoRA strategies adapted less and retained much more. Sequential fine-tuning and the distillation-based strategy reached the highest Adaptation, 0.781 and 0.747, and the highest Final Forgetting, 0.782 and 0.734. Both lost the control task completely, with a control-task drop of 0.979, and so did joint fine-tuning, although it was trained without a task sequence and with the same total number of updates. The three LoRA strategies reached an Adaptation of 0.485, 0.471 and 0.472. Task-specific LoRA keeps every trained task by construction, and shared LoRA reached a Final Forgetting of 0.289 and a control-task drop of 0.237. With replay, these fell to 0.046 and 0.138, the lowest of the strategies with one parameter set, while the Adaptation of shared LoRA changed by only 0.001 [−0.002, 0.004]. The prompt-tuning strategy reached an Adaptation of 0.580 and a Final Forgetting of 0.510, between the two groups, but its control-task drop of 0.865 is close to that of the first group, although it keeps all pretrained weights frozen.

**Version A: light (conventions and number presentation only)**

> In the primary metrics, the strategies formed two groups (…). The two strategies that update the pretrained weights adapted most and forgot most, whereas the LoRA strategies adapted less and retained much more. Sequential fine-tuning reached the highest Adaptation (0.781), followed by the distillation-based strategy (0.747), and the two also had the highest Final Forgetting (0.782 and 0.734). Both lost the control task completely (control-task drop: 0.979), and so did joint fine-tuning, although it was trained without a task sequence and with the same total number of updates. The three LoRA strategies reached an Adaptation of 0.485 (task-specific LoRA), 0.471 (shared LoRA), and 0.472 (shared LoRA with replay). Task-specific LoRA keeps every trained task by construction, and shared LoRA reached a Final Forgetting of 0.289 and a control-task drop of 0.237. With replay, these fell to 0.046 and 0.138, the lowest of the strategies with one parameter set, while the Adaptation of shared LoRA changed by only 0.001 [−0.002, 0.004]. The prompt-tuning strategy fell between the two groups (Adaptation: 0.580; Final Forgetting: 0.510). However, its control-task drop (0.865) is close to that of the first group, although it keeps all pretrained weights frozen.

**Version B: full voice (also sentence order and turns)**

> In the primary metrics, the strategies formed two groups (…). The first group contains the two strategies that update the pretrained weights. They adapted most and forgot most. Sequential fine-tuning reached the highest Adaptation (0.781) and the highest Final Forgetting (0.782), followed by the distillation-based strategy (Adaptation: 0.747; Final Forgetting: 0.734). Both lost the control task completely (control-task drop: 0.979). Joint fine-tuning lost it as well, although it was trained without a task sequence and with the same total number of updates. In contrast, the three LoRA strategies adapted less (task-specific LoRA: 0.485; shared LoRA: 0.471; shared LoRA with replay: 0.472) and retained much more. Task-specific LoRA keeps every trained task by construction. With replay, the Final Forgetting of shared LoRA fell from 0.289 to 0.046 and its control-task drop from 0.237 to 0.138, the lowest values of the strategies with one parameter set, while its Adaptation changed by only 0.001 [−0.002, 0.004]. The prompt-tuning strategy fell between the two groups in Adaptation (0.580) and Final Forgetting (0.510). However, its control-task drop (0.865) is close to that of the first group, although it keeps all pretrained weights frozen.

Both versions keep every number, claim and reference of the current text; values and the assignment of the three LoRA values checked against `thesis/tables/ch6_main.tex`.
