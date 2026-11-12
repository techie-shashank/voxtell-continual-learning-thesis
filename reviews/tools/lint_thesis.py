"""Mechanical style checks for the thesis text (report only, never edits).

Usage: python reviews/tools/lint_thesis.py thesis/introduction.tex [more .tex files]
Prints one line per finding: file:line [check] matched text  |  sentence excerpt.
Checks follow CLAUDE.md (writing style, terminology, conventions) and style/voice_sheet.md.
ERROR = rule is unambiguous; WARN = needs a human look (heuristic, false positives expected).
"""
import re
import sys

BANNED = r"delve|crucial|pivotal|vital|paramount|leverag\w*|harness\w*|foster\w*|showcas\w*|underscor\w*|seamless\w*|comprehensive|holistic|intricate|nuanced|multifaceted|landscape|realm|tapestry|journey|cutting-edge|groundbreaking|game-changer"
WARN_WORDS = r"robust\w*|novel|highlight\w*"
FILLER = [
    r"it is important to note", r"it is worth (mentioning|noting)", r"plays? an? (crucial|key|vital|important) role",
    r"paves? the way", r"a testament to", r"in the realm of", r"when it comes to", r"this highlights the importance",
    r"it can be (observed|seen) that", r"not only\b.*\bbut also", r"in today's",
]
# (pattern, message, level)
TERMS = [
    (r"lifelong learning", "use 'continual learning'", "ERROR"),
    (r"incremental learning", "use 'continual learning' unless naming a scenario/paper term", "WARN"),
    (r"text-guided|language-driven|text-driven", "use 'free-text promptable'", "WARN"),
    (r"Dice score", "use DSC", "ERROR"),
    (r"\bordering\b", "use 'task order'", "ERROR"),
    (r"\bnaive\b", "use 'sequential fine-tuning'", "WARN"),
    (r"full fine-tuning|\bFFT\b", "use 'sequential fine-tuning'", "WARN"),
    (r"lower bound", "seq. FT is the baseline, never 'lower bound'", "WARN"),
    (r"TIL-LoRA|CIL-LoRA", "use task-specific / shared LoRA", "ERROR"),
    (r"ZSCL-based|CPE-CLIP-based", "use distillation-based / prompt-tuning strategy", "ERROR"),
    (r"retention drop|retention task", "use 'control-task drop' / 'control task'", "ERROR"),
    (r"background conflict", "use 'background shift'", "ERROR"),
    (r"task-aware", "term dropped 2026-10-31", "ERROR"),
    (r"joint training", "use 'joint fine-tuning' (except related work)", "WARN"),
    (r"learning accuracy|\bplasticity\b", "use 'Adaptation' (plasticity only as the broad property)", "WARN"),
    (r"Average Performance", "not reported; ZSCL's term is 'Avg.'", "ERROR"),
    (r"\b(paradigms?|categor(y|ies))\b", "use 'families' for CL method families", "WARN"),
    (r"zero-shot", "not for the control task", "WARN"),
    (r"\bmechanism\b", "not for a strategy (author 2026-10-30)", "WARN"),
    (r"Dice similarity", "use \\gls{dsc}", "WARN"),
]
US = re.compile(r"\b\w+(iz(e|es|ed|ing|ation|ations|er|ers)|yz(e|es|ed|ing))\b|\b(behavior\w*|color\w*|labeled|labeling|modeling|modeled|center(s|ed)?|favor\w*|gray|analog|catalog|program(?!m)|fulfill)\b", re.I)
US_OK = {"size", "sizes", "sized", "seize", "prize", "capsize", "resize", "resized", "voxelize", "tokenizer", "tokenizers", "tokenize", "tokenized"}


def clean(line):
    # drop comments
    line = re.sub(r"(?<!\\)%.*", "", line)
    # neutralise arguments that are keys, labels, urls
    line = re.sub(r"\\(cite|Cite|parencite|textcite)(\[[^\]]*\])*\{[^}]*\}", " CITE ", line)
    line = re.sub(r"\\(cref|Cref|autoref|ref|label|eqref|vref|url|href|input|includegraphics)(\[[^\]]*\])*\{[^}]*\}", " REF ", line)
    line = re.sub(r"\\(gls|Gls|glspl|Glspl|acrshort|acrlong)\{([^}]*)\}", r" GLS_\2 ", line)
    return line


def paragraphs(lines):
    """Yield (start_line_no, first_text_line) for each paragraph."""
    prev_blank = True
    for i, raw in enumerate(lines, 1):
        s = raw.strip()
        if not s:
            prev_blank = True
            continue
        if s.startswith("%"):
            continue
        if prev_blank:
            yield i, s
        prev_blank = False


def lint(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    out = []

    def add(level, ln, check, m, ctx):
        out.append((ln, level, check, m, ctx.strip()[:150]))

    in_math_env = False
    for ln, raw in enumerate(lines, 1):
        if re.search(r"\\begin\{(equation|align|algorithmic|tabular|tikzpicture)", raw):
            in_math_env = True
        if re.search(r"\\end\{(equation|align|algorithmic|tabular|tikzpicture)", raw):
            in_math_env = False
            continue
        if in_math_env:
            continue
        t = clean(raw)
        if not t.strip():
            continue
        tl = t.lower()
        for m in re.finditer(r"\b(" + BANNED + r")\b", tl):
            add("ERROR", ln, "banned word", m.group(0), t)
        for m in re.finditer(r"\b(" + WARN_WORDS + r")\b", tl):
            add("WARN", ln, "check word", m.group(0), t)
        for f in FILLER:
            for m in re.finditer(f, tl):
                add("ERROR", ln, "filler/formula", m.group(0), t)
        for pat, msg, lvl in TERMS:
            for m in re.finditer(pat, t, re.I):
                add(lvl, ln, "term: " + msg, m.group(0), t)
        for m in US.finditer(t):
            w = m.group(0)
            if w.lower() in US_OK or w.startswith("GLS_") or w[0].isupper() and w.lower() not in ("behavior", "color", "center"):
                continue
            add("ERROR", ln, "US spelling", w, t)
        for m in re.finditer(r"\b\w+n't\b|\b(it|that|there|we|they)'(s|re|ll|ve|d)\b", t, re.I):
            add("ERROR", ln, "contraction", m.group(0), t)
        for m in re.finditer(r"(^|[\s(])I(?=\s)", t):
            add("WARN", ln, "first person 'I'", "I", t)
        for m in re.finditer(r"\be\.\s?g\.|\bi\.\s?e\.|\betc\.", t):
            add("ERROR", ln, "e.g./i.e./etc. (thesis uses 'for example'/'such as')", m.group(0), t)
        for m in re.finditer(r"\bsignificant\w*", t, re.I):
            add("WARN", ln, "'significant' only for statistical significance", m.group(0), t)
        for m in re.finditer(r"---|\u2014", t):
            add("WARN", ln, "em dash", m.group(0), t)
        for m in re.finditer(r'(?<![`\'])"', t):
            add("ERROR", ln, "straight double quote (use ``...'')", '"', t)
        for m in re.finditer(r"\b(\w+) \1\b", t, re.I):
            if m.group(1).lower() not in ("that", "had"):
                add("ERROR", ln, "repeated word", m.group(0), t)
        if re.match(r"\s*REF\b", t) and re.match(r"\s*\\cref", re.sub(r"(?<!\\)%.*", "", raw)):
            add("ERROR", ln, "sentence starts with \\cref (use \\Cref)", "\\cref", t)
        # one sentence per line: a sentence end followed by a capital inside the line
        for m in re.finditer(r"[a-z0-9)\}][.?!] +[A-Z\\]", t):
            pre = t[max(0, m.start() - 6):m.start() + 1]
            if re.search(r"(et al|Fig|Eq|Sec|Tab|vs|cf|App|No|al)\.$", pre) or re.search(r"\b[A-Z]\.$", pre):
                continue
            add("WARN", ln, "two sentences on one line", t[m.start():m.end() + 10], t)
        # serial comma: 'A, B and C' with short items and no comma before and/or
        for m in re.finditer(r"(?:^|[\s(])((?:[\w$\\{}~.\-]+ ?){1,4}), ((?:[\w$\\{}~.\-]+ ?){1,4})(?<!,) (and|or) ", t):
            add("WARN", ln, "serial comma missing?", m.group(0).strip(), t)
        # three decimals for own DSC-type results (0.xx or 0.xxxx)
        for m in re.finditer(r"(?<![\d.])0\.(\d{2}|\d{4,})(?!\d)", t):
            add("WARN", ln, "decimals (own results use three)", m.group(0), t)
        if len(re.findall(r"\b(Moreover|Furthermore|Additionally|In addition)\b", t)) > 1:
            add("WARN", ln, "chained connectives", "Moreover/Furthermore", t)
    # paragraph-level: opening referents
    for ln, first in paragraphs(lines):
        t = clean(first)
        if re.match(r"\s*(This|These|It|Such|Its|They|Their)\b", t) and not re.match(r"\s*This (thesis|chapter|section|appendix)\b", t):
            add("ERROR", ln, "paragraph opens with a referent (tier 1)", t.split()[0], t)
    # connective chains across consecutive sentences
    prev = None
    for ln, raw in enumerate(lines, 1):
        t = clean(raw).strip()
        cur = re.match(r"(Moreover|Furthermore|Additionally|In addition),", t)
        if cur and prev:
            add("WARN", ln, "connective chain over consecutive sentences", cur.group(1), t)
        prev = bool(cur) if t else prev
    return sorted(out)


def main():
    total = {"ERROR": 0, "WARN": 0}
    for path in sys.argv[1:]:
        for ln, level, check, m, ctx in lint(path):
            total[level] += 1
            print(f"{path}:{ln} {level} [{check}] {m}  |  {ctx}")
    print(f"# {total['ERROR']} errors, {total['WARN']} warnings")


if __name__ == "__main__":
    main()
