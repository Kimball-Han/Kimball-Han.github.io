#!/usr/bin/env python3
"""Check all public HTML links, asset references, fragments and basic page metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(); self.links=[]; self.ids=set(); self.lang=''; self.title=False; self.viewport=False; self.h1=0
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang','')
        if tag=='title': self.title=True
        if tag=='h1': self.h1+=1
        if tag=='meta' and a.get('name')=='viewport': self.viewport=True
        if 'id' in a: self.ids.add(a['id'])
        for key in ['src','href']:
            if key in a:self.links.append(a[key])
paths=[ROOT/'index.html',*sorted((ROOT/'kimdrop').rglob('*.html')),*sorted((ROOT/'filebridge').rglob('*.html')),*sorted((ROOT/'kimgames').rglob('*.html'))]
pages={p:Page(p.read_text()) for p in paths}
errors=[]; count=0
for p,page in pages.items():
    if not(page.lang and page.title and page.viewport and page.h1==1): errors.append(f'{p.relative_to(ROOT)}: language/title/viewport/h1 missing or invalid')
    for ref in page.links:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        target=(ROOT/unquote(u.path).lstrip('/') if u.path.startswith('/') else p.parent/unquote(u.path)).resolve() if u.path else p
        if not target.is_relative_to(ROOT): errors.append(f'{p.name}: path escapes root: {ref}');continue
        if target.is_dir():target=target/'index.html'
        if not target.is_file(): errors.append(f'{p.relative_to(ROOT)}: missing {ref}');continue
        if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids: errors.append(f'{p.name}: missing fragment {ref}')
        count+=1
for page in ['index.html','support/index.html','privacy/index.html','en/index.html','en/support/index.html','en/privacy/index.html']:
    if ROOT/'kimdrop'/page not in pages: errors.append(f'Missing required KimDrop page: {page}')
if errors: raise SystemExit('\n'.join(errors))
print(f'OK: {len(pages)} pages; {count} internal links/assets; both KimDrop languages and existing Kim Games checked.')
