"""Validate canonical identity and indexing metadata on primary or mirror output."""
import json, sys, re
from pathlib import Path
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
SITE=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'site'
ORIGIN='https://caoshurong.github.io'
class Head(HTMLParser):
    def __init__(self,text):
        super().__init__();self.links=[];self.metas={};self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link':self.links.append(a)
        if tag=='meta':self.metas[a.get('name',a.get('property',''))]=a.get('content','')
count=0
for p in SITE.rglob('*.html'):
    text=p.read_text(encoding='utf-8');h=Head(text)
    if p.name=='404.html':
        assert 'noindex' in h.metas['robots'];continue
    rel=p.parent.relative_to(SITE).as_posix()
    expected=ORIGIN+('/' if rel=='.' else '/'+rel+'/')
    assert [a['href'] for a in h.links if a.get('rel')=='canonical']==[expected],p
    assert 'noindex' not in h.metas.get('robots',''),p
    assert all(a['href'].startswith(ORIGIN+'/') for a in h.links if a.get('hreflang')),p
    graph=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',text).group(1))['@graph']
    person=next(x for x in graph if x['@type']=='Person')
    assert person['name']=='Shurong Cao' and '曹书嵘' in person['alternateName']
    assert person['sameAs']==['https://github.com/CAOShurong']
    assert graph[-1]['url']==expected
    assert '曹书嵘' in h.metas['description'] and 'Shurong Cao' in h.metas['description']
    count+=1
locs=ET.parse(SITE/'sitemap.xml').findall('.//{*}loc')
assert len(locs)==count and all(x.text.startswith(ORIGIN+'/') for x in locs)
for key in (ROOT/'indexing').glob('*.txt'):
    assert (SITE/key.name).read_text()==key.stem
print(f'PASS: {count} canonical bilingual pages, Person identity, sitemap, public submission key; 404 noindex.')
