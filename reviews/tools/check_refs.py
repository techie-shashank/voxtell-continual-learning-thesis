r"""Citation and cross-reference density and placement (report only, never edits).

Usage: python reviews/tools/check_refs.py thesis/introduction.tex [more files]

Flags, per paragraph (prose only, comments skipped):
  PLACE   \cite not attached with '~', or placed after the sentence's full stop
  REPEAT  the same key cited again within the same paragraph (often over-citing)
  DENSE   three or more \cite commands in one sentence
  XREF2   the same \cref/\Cref target referenced twice in one paragraph
  XREF3   three or more cross-reference commands in one sentence
  SELF    a cross-reference to the section the sentence is in
  BACK    a paragraph that starts with a cross-reference back to an earlier section
Every flag needs a human decision: a repeated key can be right (two claims from one paper).
"""
import re
import sys
from collections import Counter

CITE = re.compile(r"\\(?:cite|cites|Cite|parencite|textcite)(?:\[[^\]]*\])*((?:\{[^}]*\})+)")
XREF = re.compile(r"\\(?:cref|Cref|autoref|ref|vref)\{([^}]*)\}")
LABEL = re.compile(r"\\label\{((?:sec|subsec|chap):[^}]*)\}")


def keys_of(m):
    return [k.strip() for grp in re.findall(r"\{([^}]*)\}", m.group(1)) for k in grp.split(",")]


def paragraphs(lines):
    para, start = [], None
    for i, raw in enumerate(lines, 1):
        s = raw.strip()
        if not s or s.startswith("\\section") or s.startswith("\\subsection") or s.startswith("\\chapter") or s.startswith("\\begin{") or s.startswith("\\end{"):
            if para:
                yield start, para
            para, start = [], None
            continue
        if s.startswith("%"):
            continue
        if start is None:
            start = i
        para.append((i, re.sub(r"(?<!\\)%.*", "", raw)))
    if para:
        yield start, para


def main():
    total = Counter()
    for path in sys.argv[1:]:
        lines = open(path, encoding="utf-8").read().splitlines()
        # current section label per line
        cur, sec_of = None, {}
        for i, l in enumerate(lines, 1):
            m = LABEL.search(l)
            if m:
                cur = m.group(1)
            sec_of[i] = cur
        n_cite = n_xref = 0
        for start, para in paragraphs(lines):
            seen_keys, seen_x = Counter(), Counter()
            for idx, (ln, t) in enumerate(para):
                cites = list(CITE.finditer(t))
                xrefs = list(XREF.finditer(t))
                n_cite += len(cites)
                n_xref += len(xrefs)
                for m in cites:
                    pre = t[max(0, m.start() - 2):m.start()]
                    if m.start() > 0 and not pre.endswith("~") and not pre.endswith("{") and not pre.endswith("("):
                        print(f"{path}:{ln} PLACE  cite without '~': ...{t[max(0, m.start() - 30):m.end()]}")
                        total["PLACE"] += 1
                    if re.search(r"\.\s*~?$", t[:m.start()]) and not re.search(r"(et al|Sec|Eq|Fig|Tab|App|p|pp|cf)\.\s*~?$", t[:m.start()]):
                        print(f"{path}:{ln} PLACE  cite after the full stop: ...{t[max(0, m.start() - 30):m.end()]}")
                        total["PLACE"] += 1
                    for k in keys_of(m):
                        if seen_keys[k]:
                            print(f"{path}:{ln} REPEAT {k} cited again in the paragraph starting l. {start}")
                            total["REPEAT"] += 1
                        seen_keys[k] += 1
                if len(cites) >= 3:
                    print(f"{path}:{ln} DENSE  {len(cites)} citation commands in one line")
                    total["DENSE"] += 1
                if len(xrefs) >= 3:
                    print(f"{path}:{ln} XREF3  {len(xrefs)} cross-references in one line")
                    total["XREF3"] += 1
                for m in xrefs:
                    for tgt in m.group(1).split(","):
                        tgt = tgt.strip()
                        if seen_x[tgt]:
                            print(f"{path}:{ln} XREF2  {tgt} referenced twice in the paragraph starting l. {start}")
                            total["XREF2"] += 1
                        seen_x[tgt] += 1
                        if tgt == sec_of.get(ln):
                            print(f"{path}:{ln} SELF   {tgt} referenced inside its own section")
                            total["SELF"] += 1
                if idx == 0 and re.match(r"\s*(As|Like|Unlike|In)?\s*[^.]{0,40}\\[cC]ref\{(sec|subsec|chap):", t) and re.match(r"\s*(As (described|shown|discussed|stated)|Like|Unlike|Recall)", t):
                    print(f"{path}:{ln} BACK   paragraph opens with a back-reference")
                    total["BACK"] += 1
        print(f"# {path}: {n_cite} citation commands, {n_xref} cross-references")
    print("# flags:", dict(total))


if __name__ == "__main__":
    main()
