"""Refresh the self-hosted Noto Sans SC subset from built public text.

Run build.py first and rebuild after this script. Google Fonts serves the
OFL-licensed variable font; unicode ranges keep the local subsets disjoint.
"""
from pathlib import Path
from html.parser import HTMLParser
import re
import hashlib
import sys
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = ''
    def handle_data(self, data):
        self.text += data
    def handle_starttag(self, tag, attrs):
        self.text += ''.join(value or '' for key, value in attrs if key in ('alt', 'aria-label', 'title'))

reader = Text()
for path in (ROOT/'site').rglob('*.html'):
    reader.feed(path.read_text(encoding='utf-8'))
reader.text += (ROOT/'app.js').read_text(encoding='utf-8')
chars = ''.join(sorted(set(re.findall('[\u3000-\u303f\u3400-\u9fff\uff00-\uffef]', reader.text))))
serif = '--serif' in sys.argv
family = 'Noto Serif SC' if serif else 'Noto Sans SC'
slug = 'noto-serif-sc' if serif else 'noto-sans-sc'
css = []
for i, offset in enumerate(range(0, len(chars), 350)):
    group = chars[offset:offset+350]
    query = urllib.parse.urlencode({'family':family+':wght@400..600','text':group,'display':'swap'})
    request = urllib.request.Request('https://fonts.googleapis.com/css2?'+query, headers={'User-Agent':'Mozilla/5.0 Chrome/130.0.0.0 Safari/537.36'})
    response = urllib.request.urlopen(request, timeout=45).read().decode()
    remote = re.search(r'url\(([^)]+)\)', response).group(1)
    data = urllib.request.urlopen(remote, timeout=45).read()
    filename = f'{slug}-{i}.woff2'
    (ROOT/'assets/fonts'/filename).write_bytes(data)
    ranges = ','.join(f'U+{ord(c):04X}' for c in group)
    css.append(f"@font-face{{font-family:'{family}';font-style:normal;font-weight:400 600;font-display:swap;src:url('/assets/fonts/{filename}?v={hashlib.sha256(data).hexdigest()[:10]}') format('woff2');unicode-range:{ranges};}}")
    print(f'{filename}: {len(group)} characters, {len(data)} bytes')
(ROOT/f'assets/fonts/{slug}.css').write_text('\n'.join(css)+'\n', encoding='utf-8')
style_path=ROOT/'style.css'
style=style_path.read_text(encoding='utf-8')
version=hashlib.sha256((ROOT/f'assets/fonts/{slug}.css').read_bytes()).hexdigest()[:10]
rule=f"@import url('/assets/fonts/{slug}.css?v={version}');"
pattern=rf"@import url\('/assets/fonts/{slug}\.css[^']*'\);"
style=re.sub(pattern,rule,style) if re.search(pattern,style) else rule+'\n'+style
style_path.write_text(style,encoding='utf-8')
print(f'Subset covers {len(chars)} unique characters.')
