r"""B6: every figure, table, algorithm and appendix section is referenced in the text (report only).

Usage (from the repository root): python reviews/tools/check_floats.py
"""
import glob
import re

FILES = ['introduction', 'related_work', 'background', 'data_description', 'method',
         'experiment_results', 'summary', 'appendix']
COMMENT = re.compile(r"(?<!\\)%.*")
LABEL = re.compile(r"\\label\{([^}]*)\}")
REF = re.compile(r"\\(?:cref|Cref|autoref|ref|vref|eqref|pageref)\{([^}]*)\}")

texts = {}
for f in FILES:
    texts[f'thesis/{f}.tex'] = COMMENT.sub('', open(f'thesis/{f}.tex', encoding='utf-8').read())
for p in glob.glob('thesis/tables/*.tex'):
    texts[p] = COMMENT.sub('', open(p, encoding='utf-8').read())

refs = set()
for t in texts.values():
    for m in REF.finditer(t):
        refs.update(k.strip() for k in m.group(1).split(','))

n = 0
for path, t in texts.items():
    for m in LABEL.finditer(t):
        lab = m.group(1)
        kind = lab.split(':')[0]
        relevant = kind in ('fig', 'tab', 'alg', 'app') or (path.endswith('appendix.tex') and kind in ('sec', 'subsec'))
        if relevant:
            n += 1
            if lab not in refs:
                print('NOT REFERENCED:', lab, 'in', path)
print(f'# {n} figure/table/algorithm/appendix labels checked')
