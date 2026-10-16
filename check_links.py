#!/usr/bin/env python3
"""Check every internal href/src in the site's HTML points to a real file or anchor."""
import os, re, sys
from html.parser import HTMLParser
ROOT = os.path.dirname(os.path.abspath(__file__))
class P(HTMLParser):
    def __init__(s): super().__init__(); s.links=[]; s.ids=set()
    def handle_starttag(s, t, a):
        a = dict(a)
        if 'id' in a: s.ids.add(a['id'])
        for k in ('href', 'src'):
            if a.get(k): s.links.append(a[k])
def parse(f):
    p = P(); p.feed(open(f, encoding='utf-8').read()); return p
def target(page, url):
    path = url.split('#')[0]
    base = ROOT if path.startswith('/') else os.path.dirname(page)
    t = os.path.normpath(os.path.join(base, path.lstrip('/'))) if path else page
    if os.path.isdir(t): t = os.path.join(t, 'index.html')
    return t
errs, n = [], 0
for d, _, fs in os.walk(ROOT):
    if '.git' in d: continue
    for f in fs:
        if not f.endswith('.html'): continue
        page = os.path.join(d, f); p = parse(page)
        for u in p.links:
            if re.match(r'^(https?:|mailto:|tel:|sms:)', u): continue
            n += 1
            if u.startswith('/'):
                errs.append(f'{os.path.relpath(page,ROOT)}: root-relative link {u} (breaks on project site)'); continue
            if u.startswith('#') and (u.startswith('#affiliate-') or u == '#stripe-payment-link-TODO'): continue
            t = target(page, u)
            if not os.path.isfile(t): errs.append(f'{os.path.relpath(page,ROOT)}: missing {u}'); continue
            frag = u.split('#', 1)[1] if '#' in u else ''
            if frag and t.endswith('.html') and frag not in parse(t).ids:
                errs.append(f'{os.path.relpath(page,ROOT)}: missing anchor {u}')
print(f'Checked {n} internal links.'); print('\n'.join(errs) or 'All internal links OK.')
sys.exit(1 if errs else 0)
