"""Validate generated routes, links, language counterparts and public privacy."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import re,sys
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
class Document(HTMLParser):
    def __init__(self,text):
        super().__init__();self.links=[];self.ids=set();self.lang='';self.h1=0;self.alts=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.add(a['id'])
        if tag=='html':self.lang=a.get('lang','')
        if tag=='h1':self.h1+=1
        if tag=='img':self.alts.append(a.get('alt',''))
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
errors=[];docs={p:Document(p.read_text(encoding='utf-8')) for p in SITE.rglob('*.html')}
for path,doc in docs.items():
    if doc.h1!=1:errors.append(f'{path}: expected one h1')
    if doc.lang not in ['en','zh-CN']:errors.append(f'{path}: missing language')
    if not all(doc.alts):errors.append(f'{path}: missing image description')
    for href in doc.links:
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        if not u.path:target=path
        else:target=SITE/unquote(u.path).lstrip('/') if u.path.startswith('/') else path.parent/unquote(u.path)
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{path.relative_to(SITE)}: missing {href}')
        elif u.fragment and target in docs and unquote(u.fragment) not in docs[target].ids:errors.append(f'{path}: missing fragment {href}')
    if path.name!='404.html':
        rel=path.relative_to(SITE)
        counterpart=SITE/Path(*rel.parts[1:]) if rel.parts[0]=='zh' else SITE/'zh'/rel
        if not counterpart.exists():errors.append(f'Missing counterpart for {rel}')
for p in ROOT.rglob('*'):
    if not p.is_file() or any(x in p.parts for x in ['.git','__pycache__']):continue
    if p.suffix.lower() in ['.html','.js','.json','.py','.md','.svg','.txt','.xml','.yml']:
        t=p.read_text(encoding='utf-8-sig')
        if re.search(r'\b\d{5,}@link\.cuhk\.edu\.hk',t):errors.append(f'{p}: unmasked institutional email')
        if re.search(r'(?:\+852\s*\d[\d -]{6,}|\+86\s*\d[\d -]{9,})',t):errors.append(f'{p}: private phone')
for p in ['contact/index.html','zh/contact/index.html']:
    t=(SITE/p).read_text(encoding="utf-8")
    if '**********@link.cuhk.edu.hk' not in t or 'mailto:shurongcao0819@gmail.com' not in t:errors.append(f'{p}: contact contract')
if not (SITE/'assets/Shurong-Cao-CV.pdf').exists():errors.append('Missing public CV')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'PASS: {len(docs)} HTML documents; internal resources and anchors; bilingual counterparts; contact privacy.')
