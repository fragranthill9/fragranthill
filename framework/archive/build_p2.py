#!/usr/bin/env python3
"""Generate framework/p2-workflow.html: five pillar workflows as compact owner-tagged chains, plus functional blocks."""
import html, os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "p2-workflow.html")

OWNER = {  # chip label, fill, text colour
    "H": ("HUMAN", "var(--ink)", "var(--surface)"),
    "A": ("AGENT", "var(--accent)", "#FFFFFF"),
    "P": ("PARTNER", "var(--muted)", "#FFFFFF"),
    "C": ("CONTRACTOR", "var(--line)", "var(--ink)"),
}

PILLARS = [
 ("1", "Editorial", "p1", "Record once, six channels", [
   ("Plan the season", ["H"], "theme · 12 guests · sponsor slot"),
   ("Brief and book", ["A", "H"], "research memo · outreach · Lan sends"),
   ("Record", ["H", "C"], "Riverside remote · crew day · 2 guests"),
   ("Produce", ["A"], "Descript · OpusClip · HeyGen ZH/EN"),
   ("Publish", ["A"], "YouTube · LinkedIn · newsletter · 公众号 · 视频号"),
   ("Sell and report", ["H", "A"], "season sponsor · recap · rate card"),
 ]),
 ("2", "Advisory", "p2", "Data in, paid answers out", [
   ("Intake and scope", ["H"], "client question · price in 48 h"),
   ("Source", ["P"], "partner reports · data · expert calls"),
   ("Digest and model", ["A"], "NotebookLM · Claude Project · Elicit"),
   ("Thesis and workshop", ["H"], "Lan owns the answer · half-day"),
   ("Package", ["C", "A"], "designer layout · translation QA"),
   ("Convert", ["H"], "retainer · report licence · next project"),
 ]),
 ("3", "Community", "p3", "Audience in, members out", [
   ("Define promise and tiers", ["H"], "who is in · base tier · club tier"),
   ("Segment and invite", ["A"], "CRM scoring · personal invitations"),
   ("Vet", ["H"], "15-minute call · role or revenue bar"),
   ("Host", ["C"], "Circle (EU) · 知识星球 (CN) · trip logistics"),
   ("Run the programme", ["A", "C"], "monthly digest · salon prep · course"),
   ("Renew", ["A", "H"], "engagement flags · Lan calls top 20"),
 ]),
 ("4", "Live & Venues · Encore", "p4", "Stage in, sponsor cash out", [
   ("Secure the property", ["H"], "artist · venues · rights · categories"),
   ("Package", ["A", "H"], "rate card · deck · Lan sets price"),
   ("Introduce", ["P"], "warm doors: automotive · robotics · tech"),
   ("Pitch and close", ["H", "A"], "three tiers · exclusivity · deposit"),
   ("Deliver", ["C", "A"], "production · hospitality · cut-downs"),
   ("Renew", ["H"], "first refusal · salon series"),
 ]),
 ("5", "Acceleration", "p5", "Deal flow in, carry out", [
   ("Scout", ["P"], "partner cohorts · founder community"),
   ("Screen", ["A"], "scorecard: Nordic demand · pilot-ready"),
   ("Soft-land", ["H"], "Nordic intros · dealers · pilots · press"),
   ("Match", ["A", "H"], "investors and corporates from CRM"),
   ("Economics", ["H", "P"], "programme fee · scout fee · carry"),
   ("Feed back", ["A"], "founders → guests, members, speakers"),
 ]),
]

def chain(num, name, color, io, steps):
    W, H = 1240, 100
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Workflow for pillar {num} {html.escape(name)}: {html.escape(" → ".join(s[0] for s in steps))}" xmlns="http://www.w3.org/2000/svg">']
    o.append('<defs><marker id="w%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--ink-2)"/></marker></defs>' % num)
    # label block
    o.append(f'<rect x="0" y="8" width="150" height="84" rx="3" fill="var(--{color})"/>')
    o.append(f'<text x="12" y="34" font-size="13" font-weight="800" fill="#FFFFFF">{num} · {html.escape(name.split(" · ")[0]).upper()}</text>')
    if " · " in name:
        o.append(f'<text x="12" y="50" font-size="11" font-weight="700" fill="#FFFFFF">{html.escape(name.split(" · ")[1])}</text>')
    o.append(f'<text x="12" y="{70 if " · " in name else 56}" font-size="10" fill="#FFFFFF" opacity=".9">{html.escape(io)}</text>')
    x0, bw, gap = 164, 168, 12
    for i, (title, owners, tool) in enumerate(steps):
        x = x0 + i * (bw + gap)
        o.append(f'<rect x="{x}" y="8" width="{bw}" height="84" rx="3" fill="var(--surface)" stroke="var(--line)"/>')
        o.append(f'<rect x="{x}" y="8" width="{bw}" height="3" fill="var(--{color})"/>')
        o.append(f'<text x="{x+9}" y="31" font-size="11.5" font-weight="700" fill="var(--ink)">{i+1} · {html.escape(title)}</text>')
        cx = x + 9
        for ow in owners:
            lbl, fill, tc = OWNER[ow]
            w = 8 + len(lbl) * 6.2
            o.append(f'<rect x="{cx}" y="39" width="{w:.0f}" height="14" rx="2" fill="{fill}"/>')
            o.append(f'<text x="{cx + w/2:.0f}" y="49.5" font-size="8.5" font-weight="700" text-anchor="middle" fill="{tc}" letter-spacing=".06">{lbl}</text>')
            cx += w + 5
        # tool line, wrap at ~28 chars
        t = tool
        if len(t) > 29:
            cut = t.rfind(" ", 0, 30)
            l1, l2 = t[:cut].rstrip(" ·"), t[cut:].strip(" ·")
        else:
            l1, l2 = t, ""
        o.append(f'<text x="{x+9}" y="70" font-size="10" fill="var(--ink-2)">{html.escape(l1)}</text>')
        if l2:
            o.append(f'<text x="{x+9}" y="83" font-size="10" fill="var(--ink-2)">{html.escape(l2)}</text>')
        if i < len(steps) - 1:
            o.append(f'<path d="M{x+bw} 50 H{x+bw+gap-1}" stroke="var(--ink-2)" stroke-width="1.2" marker-end="url(#w{num})"/>')
    o.append('</svg>')
    return "\n".join(o)

css = """
/* Layout: investor one-pager on a 12-column block grid. Header, reading key, sequence band, five workflow chains, functional-block grid, tool stack, rhythm. */
:root{
  --bg:#F4F4F1; --surface:#FFFFFF; --ink:#16191D; --ink-2:#4B5159; --muted:#7A808A; --line:#DADBD6; --line-2:#EBECE8;
  --accent:#B42318; --accent-soft:#F7E4E1;
  --p1:#B42318; --p2:#1D4ED8; --p3:#0E9F8A; --p4:#C2410C; --p5:#7C3AED;
  --p1-soft:#F8E6E3; --p2-soft:#E3EAFB; --p3-soft:#DDF3EF; --p4-soft:#FAE7DE; --p5-soft:#EEE5FB;
  --display:"Archivo",system-ui,sans-serif;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --bg:#121416; --surface:#1B1E22; --ink:#ECEDE9; --ink-2:#B9BDC3; --muted:#858B94; --line:#2E3338; --line-2:#24282D;
  --accent:#E0523F; --accent-soft:#3A1F1C;
  --p1:#E0523F; --p2:#5B8CFF; --p3:#2BBFA7; --p4:#F0763B; --p5:#A77BFF;
  --p1-soft:#33201E; --p2-soft:#1C2740; --p3-soft:#17302C; --p4-soft:#36251B; --p5-soft:#2A2238; color-scheme:dark }}
:root[data-theme="dark"]{
  --bg:#121416; --surface:#1B1E22; --ink:#ECEDE9; --ink-2:#B9BDC3; --muted:#858B94; --line:#2E3338; --line-2:#24282D;
  --accent:#E0523F; --accent-soft:#3A1F1C;
  --p1:#E0523F; --p2:#5B8CFF; --p3:#2BBFA7; --p4:#F0763B; --p5:#A77BFF;
  --p1-soft:#33201E; --p2-soft:#1C2740; --p3-soft:#17302C; --p4-soft:#36251B; --p5-soft:#2A2238; color-scheme:dark }
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--display);font-size:13.5px;line-height:1.4;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 40px}
.sheet{max-width:1280px;margin:0 auto}
header{display:flex;flex-wrap:wrap;gap:12px 32px;align-items:center;justify-content:space-between;padding:20px 0 12px;border-bottom:2px solid var(--ink)}
.brand{display:flex;align-items:center;gap:12px}
.seal{width:40px;height:40px;border:2px solid var(--accent);color:var(--accent);display:grid;place-items:center;font-weight:700;font-size:14px;border-radius:4px}
.brand b{font-weight:700;font-size:14px;letter-spacing:.08em;text-transform:uppercase;display:block}
.brand span{color:var(--muted);font-size:12px}
.doc{font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);text-align:right}
.doc b{color:var(--ink);display:block;font-size:12.5px}
.grid{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:12px;margin-top:12px}
.blk{background:var(--surface);border:1px solid var(--line);padding:12px 14px;min-width:0}
.blk h2{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin:0 0 8px;font-weight:700}
.c12{grid-column:span 12}.c8{grid-column:span 8}.c6{grid-column:span 6}.c4{grid-column:span 4}.c3{grid-column:span 3}
.title{grid-column:span 8;background:transparent;border:0;padding:4px 0}
.title h1{font-size:clamp(26px,3.6vw,40px);font-weight:800;line-height:1.02;letter-spacing:-.02em;margin:0 0 8px;text-wrap:balance}
.title p{margin:0;color:var(--ink-2);font-size:15px;max-width:62ch}
.key{grid-column:span 4;display:grid;gap:6px;align-content:start}
.key div{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:center;font-size:12px;color:var(--ink-2)}
.chip{display:inline-block;padding:2px 8px;border-radius:2px;font-size:9.5px;font-weight:700;letter-spacing:.06em;min-width:92px;text-align:center}
.chip.H{background:var(--ink);color:var(--surface)} .chip.A{background:var(--accent);color:#fff} .chip.P{background:var(--muted);color:#fff} .chip.C{background:var(--line);color:var(--ink)}
figure{margin:0;overflow-x:auto}
figure svg{display:block;width:100%;height:auto;min-width:1000px}
figcaption{font-size:11px;color:var(--muted);margin-top:4px}
.wf{display:grid;gap:8px}
.fb{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.fb div{border:1px solid var(--line);padding:9px 11px;background:var(--bg);font-size:11.5px;color:var(--ink-2)}
.fb b{display:block;font-size:12px;color:var(--ink);margin-bottom:3px}
.fb .tag{font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:4px}
.dots{margin-top:5px}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:3px}
table{width:100%;border-collapse:collapse;font-size:11.5px}
th{text-align:left;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:600;padding:5px 6px;border-bottom:2px solid var(--ink)}
td{padding:6px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2)}
td:first-child{color:var(--ink);font-weight:700;white-space:nowrap}
.rh{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.rh div{border:1px solid var(--line);padding:9px 11px;background:var(--bg);font-size:11.5px;color:var(--ink-2)}
.rh b{display:block;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);margin-bottom:3px}
.foot{margin-top:12px;font-size:11px;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px 20px;justify-content:space-between}
@media (max-width:900px){.c8,.c6,.c4,.c3,.title,.key{grid-column:span 12}.fb,.rh{grid-template-columns:1fr 1fr}.doc{text-align:left}}
"""

seq_svg = """
<svg viewBox="0 0 1240 150" role="img" aria-label="Sequence band: Phase A cash runs Live and Advisory; it hands content, guest lists and clients to Phase B which runs Editorial and Community; Phase B hands audience and members to Phase C which runs Acceleration; Phase C returns founders and sponsors to Phase A." xmlns="http://www.w3.org/2000/svg">
<defs><marker id="sq" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--ink-2)"/></marker><marker id="sqa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--accent)"/></marker></defs>
<rect x="0" y="10" width="380" height="96" rx="3" fill="var(--p4-soft)" stroke="var(--p4)"/>
<text x="14" y="32" font-size="11" font-weight="800" letter-spacing=".1" style="fill:var(--p4)">PHASE A · CASH</text>
<text x="14" y="52" font-size="12.5" font-weight="700" fill="var(--ink)">4 Live &amp; Encore  +  2 Advisory</text>
<text x="14" y="70" font-size="11" fill="var(--ink-2)">sells access and judgement; needs no audience</text>
<text x="14" y="92" font-size="10.5" fill="var(--ink-2)">GATE: rights and sponsor categories confirmed · partner intros in hand</text>
<path d="M380 58 H426" stroke="var(--ink-2)" stroke-width="1.3" marker-end="url(#sq)"/>
<text x="403" y="46" font-size="9.5" fill="var(--muted)" text-anchor="middle">content</text><text x="403" y="78" font-size="9.5" fill="var(--muted)" text-anchor="middle">guests</text>
<rect x="430" y="10" width="380" height="96" rx="3" fill="var(--p1-soft)" stroke="var(--p1)"/>
<text x="444" y="32" font-size="11" font-weight="800" letter-spacing=".1" style="fill:var(--p1)">PHASE B · AUDIENCE AND RECURRING</text>
<text x="444" y="52" font-size="12.5" font-weight="700" fill="var(--ink)">1 Editorial season  +  3 Community</text>
<text x="444" y="70" font-size="11" fill="var(--ink-2)">one theme, weekly rhythm, then two membership tiers</text>
<text x="444" y="92" font-size="10.5" fill="var(--ink-2)">GATE: a closed sponsorship funds the season · one season published</text>
<path d="M810 58 H856" stroke="var(--ink-2)" stroke-width="1.3" marker-end="url(#sq)"/>
<text x="833" y="46" font-size="9.5" fill="var(--muted)" text-anchor="middle">members</text><text x="833" y="78" font-size="9.5" fill="var(--muted)" text-anchor="middle">clients</text>
<rect x="860" y="10" width="380" height="96" rx="3" fill="var(--p5-soft)" stroke="var(--p5)"/>
<text x="874" y="32" font-size="11" font-weight="800" letter-spacing=".1" style="fill:var(--p5)">PHASE C · EQUITY</text>
<text x="874" y="52" font-size="12.5" font-weight="700" fill="var(--ink)">5 Acceleration</text>
<text x="874" y="70" font-size="11" fill="var(--ink-2)">deal flow matched to Nordic corporates and investors</text>
<text x="874" y="92" font-size="10.5" fill="var(--ink-2)">GATE: vetted club and paying advisory clients exist</text>
<path d="M1050 106 V130 H190 V110" fill="none" stroke="var(--accent)" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#sqa)"/>
<text x="620" y="144" font-size="10.5" font-weight="600" text-anchor="middle" style="fill:var(--accent)">founders and sponsors return as the next stage, the next guests, the next members</text>
</svg>
"""

parts = []
parts.append('<title>Fragrant Hill Workflow</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,400..800&display=swap">\n<style>' + css + '</style>\n<div class="sheet">')
parts.append('''<header>
  <div class="brand"><div class="seal">香山</div><div><b>Fragrant Hill Studio</b><span>Editorial house · Stockholm · Europe ↔ China</span></div></div>
  <div class="doc"><b>Page 2 of 3 · Workflow</b>How each pillar runs and which blocks it needs</div>
</header>
<div class="grid">
  <div class="title">
    <h1>Each pillar is a six-step line. Every step has an owner.</h1>
    <p>Owners are functional blocks, not job titles: a human on the team, a digital agent, the partner, or a contractor paid per deliverable. Humans keep the thesis, the relationship and the price. Agents run everything repeatable.</p>
  </div>
  <div class="key">
    <div><span class="chip H">HUMAN</span><span>Founder and core team. Hosts, decides, prices, closes.</span></div>
    <div><span class="chip A">AGENT</span><span>Digital agent on the Claude Agent SDK with the house skills. Research, production, publishing, follow-up, finance.</span></div>
    <div><span class="chip P">PARTNER</span><span>Partner organisation: data, cohorts, introductions, China invoicing.</span></div>
    <div><span class="chip C">CONTRACTOR</span><span>Editor, designer, event producer, community coordinator. Paid per deliverable.</span></div>
  </div>
  <div class="blk c12"><h2>Sequence · in which order the pillars switch on, and what passes between them</h2><figure>''' + seq_svg + '''</figure></div>
  <div class="blk c12"><h2>Five workflows · one line per pillar, left to right</h2><div class="wf">''')
for num, name, color, io, steps in PILLARS:
    parts.append('<figure>' + chain(num, name, color, io, steps) + '</figure>')
parts.append('''</div><figcaption>Each line loops: step 6 writes back to the relationship graph and sets up step 1 of the next cycle. Tools named are current choices, replaceable without changing the line.</figcaption></div>

  <div class="blk c8"><h2>Functional blocks · the twelve units the system needs</h2>
  <div class="fb">
    <div><span class="tag">Human</span><b>Editor-in-chief and host</b>Owns the theme, interviews, final cut, sponsor and client relationships. Year one: the founder.<div class="dots"><span class="dot" style="background:var(--p1)"></span><span class="dot" style="background:var(--p2)"></span><span class="dot" style="background:var(--p3)"></span><span class="dot" style="background:var(--p4)"></span><span class="dot" style="background:var(--p5)"></span></div></div>
    <div><span class="tag">Human</span><b>Commercial lead</b>Prices packages, pitches, closes, renews. Year one: same person as above; first hire when Live repeats.<div class="dots"><span class="dot" style="background:var(--p2)"></span><span class="dot" style="background:var(--p4)"></span></div></div>
    <div><span class="tag">Agent</span><b>Research agent</b>Guest memos, client briefs, sourced digests of partner reports, scorecards for founders.<div class="dots"><span class="dot" style="background:var(--p1)"></span><span class="dot" style="background:var(--p2)"></span><span class="dot" style="background:var(--p5)"></span></div></div>
    <div><span class="tag">Agent</span><b>Production agent</b>Transcripts, cuts, shorts, dubbing EN ↔ ZH, sponsor cut-downs within 72 hours of a show.<div class="dots"><span class="dot" style="background:var(--p1)"></span><span class="dot" style="background:var(--p4)"></span></div></div>
    <div><span class="tag">Agent</span><b>Publishing agent</b>Schedules six channels in two languages, captions, weekly numbers.<div class="dots"><span class="dot" style="background:var(--p1)"></span></div></div>
    <div><span class="tag">Agent</span><b>Sales-desk agent</b>Rate cards, decks, follow-up sequences, pipeline hygiene in the CRM.<div class="dots"><span class="dot" style="background:var(--p2)"></span><span class="dot" style="background:var(--p4)"></span></div></div>
    <div><span class="tag">Agent</span><b>Concierge agent</b>Member onboarding, monthly digest, salon reminders, renewal flags.<div class="dots"><span class="dot" style="background:var(--p3)"></span></div></div>
    <div><span class="tag">Agent</span><b>Finance agent</b>Invoices, collections, monthly P&amp;L by pillar; hands exceptions to the accountant.<div class="dots"><span class="dot" style="background:var(--p1)"></span><span class="dot" style="background:var(--p2)"></span><span class="dot" style="background:var(--p3)"></span><span class="dot" style="background:var(--p4)"></span><span class="dot" style="background:var(--p5)"></span></div></div>
    <div><span class="tag">Partner</span><b>Data, cohorts, introductions</b>Reports and datasets, founder community, sponsor and investor doors, fapiao invoicing in China.<div class="dots"><span class="dot" style="background:var(--p2)"></span><span class="dot" style="background:var(--p4)"></span><span class="dot" style="background:var(--p5)"></span></div></div>
    <div><span class="tag">Contractor</span><b>Video editor and designer</b>Flagship episode cuts, report layout, tour film. Per deliverable.<div class="dots"><span class="dot" style="background:var(--p1)"></span><span class="dot" style="background:var(--p2)"></span><span class="dot" style="background:var(--p4)"></span></div></div>
    <div><span class="tag">Contractor</span><b>Event producer and hospitality</b>Venue, production, catering, VIP logistics for concerts and salons.<div class="dots"><span class="dot" style="background:var(--p3)"></span><span class="dot" style="background:var(--p4)"></span></div></div>
    <div><span class="tag">Contractor</span><b>Community coordinator and accountant</b>Member care and trip logistics; Swedish bookkeeping and tax.<div class="dots"><span class="dot" style="background:var(--p3)"></span><span class="dot" style="background:var(--p5)"></span></div></div>
  </div></div>

  <div class="blk c4"><h2>Tool stack · current choices by pillar</h2>
  <table>
    <tbody>
      <tr><td><span class="dot" style="background:var(--p1)"></span>Editorial</td><td>Riverside · Descript · OpusClip · CapCut · HeyGen · Beehiiv · 公众号 · 视频号 · Bilibili · Metricool</td></tr>
      <tr><td><span class="dot" style="background:var(--p2)"></span>Advisory</td><td>Claude Projects · NotebookLM · Perplexity · Elicit · Google Drive · expert-network calls</td></tr>
      <tr><td><span class="dot" style="background:var(--p3)"></span>Community</td><td>Circle (EU) · 知识星球 and 小鹅通 (CN) · Luma · 企业微信 · Stripe</td></tr>
      <tr><td><span class="dot" style="background:var(--p4)"></span>Live</td><td>Attio pipeline · Passionfroot inbound · Luma · e-signature · Descript</td></tr>
      <tr><td><span class="dot" style="background:var(--p5)"></span>Acceleration</td><td>Attio · partner cohort data · Nordic investor lists · Luma</td></tr>
      <tr><td>Shared</td><td>Attio CRM · n8n glue · Claude Agent SDK with house skills · Google Drive archive</td></tr>
    </tbody>
  </table>
  <figcaption>Published list prices put the core stack at roughly $350–600 a month; agents and API usage add to that. Research notes 4.</figcaption>
  <h2 style="margin-top:12px">Operating rhythm · the implementable version</h2>
  <div class="rh" style="grid-template-columns:1fr 1fr">
    <div><b>Weekly</b>Plan · record two guests · review cuts · publish · sponsor follow-ups</div>
    <div><b>Monthly</b>One salon on a Live stage · sponsor recap · member digest · P&amp;L by pillar</div>
    <div><b>Per season</b>Twelve guests · one season sponsor · one co-branded report</div>
    <div><b>Per edition</b>One Encore tour · one study trip each way · one founder cohort</div>
  </div></div>
</div>
<div class="foot"><span>Fragrant Hill Studio · confidential · built from the skills in skills/ and research in framework/research/</span><span>Page 1: system architecture · Page 3: Encore, the piano tour sponsorship programme</span></div>
</div>''')

with open(OUT, "w") as f:
    f.write("\n".join(parts))
print("wrote", OUT)
