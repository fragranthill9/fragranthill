#!/usr/bin/env python3
"""Build one self-contained bilingual HTML file (English / 中文 switch) with all three pages, readable on any device."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pages as B  # importing also regenerates the six single pages

CSS_EXTRA = """
.top{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:8px 16px;align-items:center;justify-content:space-between;padding:10px 0}
.top .tabs{display:flex;gap:6px;flex-wrap:wrap}
.top .tabs a{text-decoration:none;color:var(--ink-2);border:1px solid var(--line);border-radius:16px;padding:5px 12px;font-size:12.5px;font-weight:500}
.top .lg button{border:1px solid var(--line);background:#fff;border-radius:16px;padding:5px 12px;font-size:12.5px;font-weight:700;cursor:pointer;color:var(--ink-2)}
.top .lg button.on{background:var(--accent);border-color:var(--accent);color:#fff}
:root[data-lang="en"] .L.zh{display:none}:root[data-lang="zh"] .L.en{display:none}
.L header .lang,.L header .pages{display:none}
.pg{padding-top:8px;border-top:4px solid var(--line);margin-top:28px}.L .pg:first-child{border-top:0;margin-top:0}
"""

JS = """<script>
function setLang(l){document.documentElement.setAttribute('data-lang',l);document.documentElement.lang=(l==='zh'?'zh-CN':'en');
 document.getElementById('b-en').classList.toggle('on',l==='en');document.getElementById('b-zh').classList.toggle('on',l==='zh');
 try{localStorage.setItem('fh-lang',l)}catch(e){}}
(function(){var l='en';try{l=localStorage.getItem('fh-lang')||((navigator.language||'').toLowerCase().indexOf('zh')===0?'zh':'en')}catch(e){}setLang(l)})();
</script>"""

def body_of(html):
    inner = html.split('<div class="sheet"', 1)[1]
    inner = inner.split(">", 1)[1]
    return inner.rsplit("</div>", 1)[0]

parts = []
for lang in ("en", "zh"):
    t = B.T[lang]
    secs = []
    for key, fn in (("p1", B.page1), ("p2", B.page2), ("p3", B.page3)):
        secs.append('<section class="pg" id="%s-%s">%s</section>' % (key, lang, body_of(fn(t, lang, "#"))))
    parts.append('<div class="L %s">%s</div>' % (lang, "".join(secs)))

tabs = {"en": ["Architecture", "Monetisation", "Encore"], "zh": ["系统架构", "变现方式", "安可计划"]}
tab_html = "".join('<div class="tabs L %s">%s</div>' % (l, "".join('<a href="#p%d-%s">%d · %s</a>' % (i + 1, l, i + 1, n) for i, n in enumerate(tabs[l]))) for l in ("en", "zh"))
top = ('<div class="top"><div class="brand"><div class="seal">香山</div><div><b>Fragrant Hill Studio · 香山工作室</b>'
       '<span>Editorial house · Stockholm · Europe ↔ China</span></div></div>%s'
       '<div class="lg"><button id="b-en" onclick="setLang(\'en\')">English</button> <button id="b-zh" onclick="setLang(\'zh\')">中文</button></div></div>') % tab_html

doc = ('<!doctype html><html lang="en" data-lang="en"><head><meta charset="utf-8">'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
       '<title>Fragrant Hill Studio · 香山工作室 · Proposal</title>%s<style>%s%s</style></head>'
       '<body><div class="sheet">%s%s</div>%s</body></html>') % (B.FONT["zh"], B.CSS, CSS_EXTRA, top, "".join(parts), JS)

out = os.path.join(B.ROOT, "fragrant-hill-proposal.html")
open(out, "w").write(doc)
print("wrote", out, len(doc), "bytes")
