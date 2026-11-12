import glob, json, collections, sys, os
MAT = dict(w='木',p='紙',m='金属',c='土・石・陶',g='ガラス・樹脂',t='糸・布・紐',k='粒・トークン',x='レゴ・ブロック',d='3Dプリント・デジタル加工',l='水・液体',e='光・電子表示',a='機械・アクチュエータ',f='食べ物',b='生物・植物',h='人の身体',s='現地・建築スケール',o='その他・複合')
MOD = dict(V='視覚',T='触覚',A='聴覚',G='味覚・嗅覚',B='身体（歩く・並ぶ・着る）')
DAT = dict(q='数量・統計',y='時系列',g='地理・空間',n='関係・ネットワーク',s='科学・数理構造',p='個人データ',r='実時間・センサー',c='計数・記録',a='音',x='データなし（関連技術）')
USE = dict(R='記録・計算',S='科学・分析',E='教育・説明',J='報道・啓発',A='芸術表現',P='内省・個人',C='参加・対話',M='追悼・記憶',W='実用・業務',T='技術研究')
DYN = dict(s='静的',r='組み替えできる',k='自動で動く',p='参加で育つ',n='自然の過程で変わる')
def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out, errs, seen = [], [], set()
    tp = os.path.join(here, '..', 'data', 'thumbs.json')
    thumbs = json.load(open(tp, encoding='utf-8'))['thumbs'] if os.path.exists(tp) else {}
    for f in sorted(glob.glob(os.path.join(here, '..', 'data', '*.txt'))):
        for i, line in enumerate(open(f, encoding='utf-8'), 1):
            line = line.rstrip('\n')
            if not line.strip(): continue
            p = line.split('|')
            if len(p) != 11: errs.append((os.path.basename(f), i, 'fields', len(p))); continue
            year, slug, title, creator, ja, mat, mod, dat, use, dyn, flags = p
            for ch, D, nm in [(mat, MAT, 'mat'), (mod, MOD, 'mod'), (dat, DAT, 'dat'), (use, USE, 'use'), (dyn, DYN, 'dyn')]:
                for c in ch:
                    if c not in D: errs.append((os.path.basename(f), i, nm, c))
            if not mat or not mod or len(dat) != 1 or len(use) != 1 or len(dyn) != 1: errs.append((os.path.basename(f), i, 'arity', line[:40]))
            if set(flags) - set('xjn'): errs.append((os.path.basename(f), i, 'flags', flags))
            url = slug if slug.startswith('http') else f'https://dataphys.org/list/{slug}/'
            if url in seen: errs.append((os.path.basename(f), i, 'dup', slug))
            seen.add(url)
            out.append(dict(y=int(year), t=title, c=creator, d=ja, u=url, m=list(mat), s=list(mod), k=dat, p=use, v=dyn,
                            x=int('x' in flags), j=int('j' in flags), n=int('n' in flags), i=thumbs.get(slug, '')))
    out.sort(key=lambda e: (e['y'], e['t']))
    for e in errs: print('ERR', e)
    print('entries', len(out), 'errors', len(errs))
    json.dump(dict(items=out, MAT=MAT, MOD=MOD, DAT=DAT, USE=USE, DYN=DYN), open(os.path.join(here, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    C = collections.Counter
    data = [e for e in out if not e['x']]
    print('data-driven', len(data), 'related', len(out)-len(data), 'japan', sum(e['j'] for e in out), 'added', sum(e['n'] for e in out))
    print('use', C(USE[e['p']] for e in data).most_common())
    print('dat', C(DAT[e['k']] for e in data).most_common())
    print('mat', C(MAT[m] for e in data for m in e['m']).most_common())
    print('mod', C(MOD[m] for e in data for m in e['s']).most_common())
    print('dyn', C(DYN[e['v']] for e in data).most_common())
    yrs = C(e['y'] for e in out if 1990 <= e['y'] <= 2025)
    print('by year', sorted(yrs.items()))
    print('<=2012', sum(1 for e in data if e['y'] <= 2012), '>=2013', sum(1 for e in data if 2013 <= e['y'] <= 2025))
    print('with thumbnail', sum(1 for e in out if e['i']), 'without', sum(1 for e in out if not e['i']))
    print('json bytes', os.path.getsize(os.path.join(here, 'data.json')))
if __name__ == '__main__': main()
