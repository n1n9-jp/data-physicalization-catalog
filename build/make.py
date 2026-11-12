import json, os
here = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(here, 'data.json'), encoding='utf-8'))
t = open(os.path.join(here, 'template.html'), encoding='utf-8').read()
nadd = sum(e['n'] for e in d['items']); nlist = len(d['items']) - nadd
js = json.dumps(d, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
out = t.replace('__DATA__', js).replace('__NLIST__', str(nlist)).replace('__NADD__', str(nadd))

open(os.path.join(here, '..', 'index.html'), 'w', encoding='utf-8').write(out)
print('written', len(out), 'bytes; list', nlist, 'added', nadd)
