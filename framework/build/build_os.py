#!/usr/bin/env python3
"""Generate framework/03-operating-system.html with five swimlane workflow SVGs."""
import html

import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "03-operating-system.html")

LANES = [("Lan · human", 30), ("AI agents", 102), ("Partner · contractor", 174)]
LANE_C = {0: 66, 1: 138, 2: 210}
BW, BH = 172, 58
XS = [150, 330, 510, 690, 870, 1050]

def wrap2(t, n=30):
    if len(t) <= n: return t, ""
    cut = t.rfind(" ", 0, n+1)
    if cut < 10: cut = n
    return t[:cut].rstrip(" ;,"), t[cut:].strip()

def wf(pillar, color, soft, steps, loop_text):
    """steps: list of (lane, title, sub). Returns svg string."""
    n = len(steps)
    w = 1232
    h = 284 if loop_text else 250
    o = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Swimlane workflow for {html.escape(pillar)}: {html.escape(", ".join(s[1] for s in steps))}" xmlns="http://www.w3.org/2000/svg" font-family="Archivo, system-ui, sans-serif">']
    o.append(f'<defs><marker id="m{color}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="var(--ink-2)"/></marker></defs>')
    for i, (name, y) in enumerate(LANES):
        fill = "var(--surface)" if i % 2 == 0 else "var(--bg)"
        o.append(f'<rect x="0" y="{y}" width="{w}" height="72" fill="{fill}"/>')
        o.append(f'<line x1="0" y1="{y}" x2="{w}" y2="{y}" stroke="var(--line)"/>')
        o.append(f'<text x="12" y="{y+40}" font-size="11" font-weight="700" fill="var(--muted)" letter-spacing=".08">{html.escape(name).upper()}</text>')
    o.append(f'<line x1="0" y1="246" x2="{w}" y2="246" stroke="var(--line)"/>')
    # arrows first (under boxes)
    for i in range(n - 1):
        l1, l2 = steps[i][0], steps[i + 1][0]
        x1 = XS[i] + BW; y1 = LANE_C[l1]
        x2 = XS[i + 1]; y2 = LANE_C[l2]
        if l1 == l2:
            d = f"M{x1} {y1} H{x2-1}"
        else:
            mid = x1 + 4
            d = f"M{x1} {y1} H{mid} V{y2} H{x2-1}"
        o.append(f'<path d="{d}" fill="none" stroke="var(--ink-2)" stroke-width="1.2" marker-end="url(#m{color})"/>')
    for i, (lane, title, sub) in enumerate(steps):
        x = XS[i]; cy = LANE_C[lane]; y = cy - BH // 2
        o.append(f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="3" fill="var(--{soft})" stroke="var(--{color})" stroke-width="1.2"/>')
        o.append(f'<text x="{x+10}" y="{y+17}" font-size="12" font-weight="700" fill="var(--ink)">{i+1} · {html.escape(title)}</text>')
        l1, l2 = wrap2(sub)
        o.append(f'<text x="{x+10}" y="{y+33}" font-size="10.5" fill="var(--ink-2)">{html.escape(l1)}</text>')
        if l2: o.append(f'<text x="{x+10}" y="{y+47}" font-size="10.5" fill="var(--ink-2)">{html.escape(l2)}</text>')
    if loop_text:
        lx1 = XS[n - 1] + BW // 2; ly = LANE_C[steps[-1][0]] + BH // 2
        o.append(f'<path d="M{lx1} {ly} V264 H{XS[0]+BW//2} V{LANE_C[steps[0][0]]+BH//2+1}" fill="none" stroke="var(--accent)" stroke-width="1.4" stroke-dasharray="4 3" marker-end="url(#m{color})"/>')
        o.append(f'<text x="{(XS[0]+XS[n-1]+BW)//2}" y="278" font-size="10.5" text-anchor="middle" fill="var(--accent)" font-weight="600">{html.escape(loop_text)}</text>')
    o.append('</svg>')
    return "\n".join(o)

WFS = [
 dict(num="P1", name="Editorial", color="p1", soft="p1-soft",
  thesis="One studio day, six channels, two languages.",
  problem="Six months of recording produced no audience because every piece was a one-off: a new guest, a hired crew, one channel, no theme. The fix is a repeatable line, not more effort.",
  steps=[(0,"Plan the season","12 guests, 1 theme, 1 sponsor slot"),
         (1,"Brief and book","research memo, outreach draft; Lan sends"),
         (2,"Record","Riverside remote or crew day; 2 guests per day"),
         (1,"Produce","Descript cut, OpusClip shorts, HeyGen ZH/EN dub"),
         (1,"Publish","YouTube, LinkedIn, newsletter, 公众号, 视频号, Bilibili"),
         (0,"Sell and report","season sponsor, recap, rate card")],
  loop="analytics and sponsor feedback shape the next season",
  cadence="Weekly: Monday plan, Tuesday record two guests, Thursday the AI pipeline delivers cuts for review, Friday publish everywhere. Monthly: one sponsor recap. Quarterly: one season.",
  kpi="Month 6: 2,000 email subscribers, 3,000 LinkedIn, 1,500 YouTube, first season sponsor. Month 12: 6,000 / 10,000 / 5,000 and €500–1,000 per newsletter slot."),
 dict(num="P2", name="Advisory", color="p2", soft="p2-soft",
  thesis="Turn partner data and the founder's seat into paid answers.",
  problem="The partner holds data, reports, analysis and a founder network that currently earn nothing in Europe. A Swedish operator with an automotive and sensing background is the missing translator.",
  steps=[(0,"Intake","client question; scope and price in 48 hours"),
         (2,"Source","partner reports, datasets, expert calls"),
         (1,"Digest and model","NotebookLM, Claude Project, Elicit; sourced draft"),
         (0,"Thesis and workshop","Lan owns the answer; half-day with client"),
         (2,"Package","designer lays out report; translation QA"),
         (0,"Convert","retainer, co-branded report, next project")],
  loop="every project becomes an anonymised insight for Editorial and a member for Community",
  cadence="Two advisory days a week maximum, so Editorial keeps its rhythm. Quarterly: one co-branded report sold under licence.",
  kpi="Day rate €1,500–3,000. Target by month 12: two retainers at €4–6k a month plus one report licence a quarter."),
 dict(num="P3", name="Community", color="p3", soft="p3-soft",
  thesis="From audience to a vetted room, in two tiers.",
  problem="Memberships only work with trust already built. This pillar starts after Editorial has 2,000 real subscribers and Live has filled one room.",
  steps=[(0,"Define the promise","who is in, who is not, what they get"),
         (1,"Segment and invite","CRM scoring, personal invitations drafted"),
         (0,"Vet","15-minute call; revenue or role bar"),
         (2,"Host the platform","Circle in Europe, 知识星球 in China; logistics for trips"),
         (1,"Run the programme","monthly digest, salon prep, course material"),
         (0,"Renew","engagement score flags, Lan calls the top 20")],
  loop="members become guests, sponsors and advisory clients",
  cadence="Monthly salon (hosted on a Live stage), quarterly course, one study trip a year in each direction.",
  kpi="Base tier €400 a year, vetted club €4,000–8,000 a year. Month 12: 80 base members, 15 club members. Month 24: 300 and 50."),
 dict(num="P4", name="Live & Venues · Encore", color="p4", soft="p4-soft",
  thesis="From stage access to sponsor cash, in one quarter.",
  problem="This is the entry pillar. It is the only line that sells on access and association rather than follower counts, so it can close before the audience exists.",
  steps=[(0,"Secure the property","artist dates, venues, rights in writing"),
         (1,"Package","rate card and deck from the proposal skill; Lan prices"),
         (2,"Introduce","partner opens doors to automotive and robotics brands"),
         (0,"Pitch and close","three tiers, category exclusivity, 50% on signature"),
         (2,"Deliver","production, hospitality, sponsor content cut-downs"),
         (0,"Renew","first refusal on the next tour; salon series")],
  loop="every concert yields content for Editorial and a guest list for Community",
  cadence="One flagship tour a year, four executive salons a year on the same stages, one sponsor dinner per city.",
  kpi="Year 1: one presenting partner and two official partners. Fragrant Hill margin 20–30% of gross sponsorship plus production fees."),
 dict(num="P5", name="Acceleration", color="p5", soft="p5-soft",
  thesis="From deal flow to carry, without running a fund.",
  problem="Deal flow is a by-product of the other four pillars. Economics sit in the partner's fund and in programme fees, so this pillar carries no fixed cost.",
  steps=[(2,"Scout","partner cohorts; 500+ founders"),
         (1,"Screen","scorecard against Nordic demand, pilot readiness"),
         (0,"Soft-landing programme","Nordic intros, dealers, pilots, press"),
         (2,"Match","investors and corporates from the shared CRM"),
         (0,"Economics","programme fee, scout fee, carry via partner")],
  loop="portfolio founders become the next interviews and the next salon speakers",
  cadence="One cohort a year of 6–8 companies, timed with the Stockholm salon and a Live stage.",
  kpi="Programme fee €15–25k per company, scout fee 2–5% of round, carry negotiated with the partner. First cohort in year 2."),
]

css = """
/* Layout: one column of five workflow sheets, each with a swimlane diagram, then the stack map and the operating calendar. */
:root{
  --bg:#F4F4F1; --surface:#FFFFFF; --ink:#16191D; --ink-2:#4B5159; --muted:#7A808A; --line:#DADBD6; --line-2:#EBECE8;
  --accent:#B42318; --accent-soft:#F7E4E1;
  --p1:#B42318; --p2:#1D4ED8; --p3:#0E9F8A; --p4:#C2410C; --p5:#7C3AED;
  --p1-soft:#F8E6E3; --p2-soft:#E3EAFB; --p3-soft:#DDF3EF; --p4-soft:#FAE7DE; --p5-soft:#EEE5FB;
  --display:"Archivo",system-ui,sans-serif; --body:"Source Serif 4",Georgia,serif;
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
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--body);font-size:15px;line-height:1.5;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 48px}
.sheet{max-width:1240px;margin:0 auto}
header{display:flex;flex-wrap:wrap;gap:16px 32px;align-items:flex-end;justify-content:space-between;padding:28px 0 18px;border-bottom:2px solid var(--ink)}
.brand{display:flex;align-items:center;gap:14px}
.seal{width:44px;height:44px;border:2px solid var(--accent);color:var(--accent);display:grid;place-items:center;font-family:var(--display);font-weight:700;font-size:15px;border-radius:4px}
.brand b{font-family:var(--display);font-weight:700;font-size:15px;letter-spacing:.08em;text-transform:uppercase;display:block}
.brand span{color:var(--muted);font-size:13px;font-family:var(--display)}
.doc{font-family:var(--display);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);text-align:right}
.doc b{color:var(--ink);display:block;font-size:13px}
h1{font-family:var(--display);font-weight:800;font-size:clamp(28px,4vw,46px);line-height:1.02;letter-spacing:-.02em;margin:28px 0 8px;text-wrap:balance;max-width:22ch}
.lede{font-size:17px;max-width:66ch;color:var(--ink-2);margin:0 0 22px}
.core{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-bottom:8px}
.core div{background:var(--surface);border:1px solid var(--line);padding:14px 16px}
.core b{font-family:var(--display);font-size:13px;display:block;margin-bottom:4px}
.core p{margin:0;font-size:14px;color:var(--ink-2)}
section.wf{margin-top:34px;border-top:2px solid var(--pc);padding-top:12px}
section.wf .eyebrow{font-family:var(--display);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--pc);font-weight:700}
section.wf h2{font-family:var(--display);font-size:24px;letter-spacing:-.01em;margin:4px 0 6px;text-wrap:balance}
section.wf .problem{margin:0 0 12px;color:var(--ink-2);max-width:78ch}
figure{margin:0;background:var(--surface);border:1px solid var(--line);padding:0 0 4px;overflow-x:auto}
figure svg{display:block;min-width:1000px;width:100%;height:auto}
figcaption{font-family:var(--display);font-size:12px;color:var(--muted);padding:8px 14px 6px}
.meta{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:10px 28px;margin-top:12px;font-size:14px;color:var(--ink-2)}
.meta b{font-family:var(--display);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:2px}
.meta p{margin:0}
h2.sec{font-family:var(--display);font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);margin:36px 0 10px;padding-top:10px;border-top:2px solid var(--accent)}
.twrap{overflow-x:auto}
table{width:100%;border-collapse:collapse;font-family:var(--display);font-size:12.5px;min-width:900px}
th{text-align:left;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:600;padding:8px;border-bottom:2px solid var(--ink)}
td{padding:8px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--ink-2)}
td:first-child{color:var(--ink);font-weight:700;white-space:nowrap}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:8px;vertical-align:-1px}
.cal{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.cal div{background:var(--surface);border:1px solid var(--line);padding:12px 14px;font-size:14px;color:var(--ink-2)}
.cal b{font-family:var(--display);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);display:block;margin-bottom:6px}
.team{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.team div{background:var(--surface);border:1px solid var(--line);padding:12px 14px;font-size:14px;color:var(--ink-2)}
.team b{font-family:var(--display);font-size:13px;color:var(--ink);display:block;margin-bottom:4px}
.num{font-family:var(--display);font-variant-numeric:tabular-nums}
.foot{margin-top:28px;padding-top:12px;border-top:1px solid var(--line);font-family:var(--display);font-size:12px;color:var(--muted);display:flex;flex-wrap:wrap;gap:8px 24px;justify-content:space-between}
@media (max-width:900px){.core,.cal,.team{grid-template-columns:1fr}.meta{grid-template-columns:1fr}.doc{text-align:left}}
"""

parts = []
parts.append('<title>Fragrant Hill Operating System</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,400..800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..600;1,8..60,400&display=swap">\n<style>' + css + '</style>\n<div class="sheet">')
parts.append('''<header>
  <div class="brand"><div class="seal">香山</div><div><b>Fragrant Hill Studio</b><span>Editorial house · Stockholm · Europe ↔ China</span></div></div>
  <div class="doc"><b>Document 3 of 5 · Operating system</b>Five workflows · v1.0 · November 2026</div>
</header>
<h1>Five workflows, three lanes, one calendar.</h1>
<p class="lede">Each pillar runs as a swimlane: what Lan does, what AI agents do, what a partner or contractor does. The rule is simple. Humans own the thesis, the relationship and the price. Agents own research, production, distribution and follow-up. Partners own what they already have: data, cohorts, venues, invoicing in China. Nothing here needs a full-time hire in year one.</p>
<div class="core">
  <div><b>Shared core · Relationship graph</b><p>One CRM (Attio or HubSpot) holds every guest, sponsor, member, founder and investor with a pillar tag. Agents read and write it; Lan sees one pipeline.</p></div>
  <div><b>Shared core · Production pipeline</b><p>Riverside → Descript → OpusClip → HeyGen → scheduled posts via n8n. Lean stack runs at roughly $350–600 a month, rising to $900–1,400 with agents and API usage.</p></div>
  <div><b>Shared core · Back office</b><p>Swedish AB invoices Europe. A Chinese partner entity issues fapiao and remits net of its fee, which avoids the 6% withholding on services paid to a foreign company.</p></div>
</div>''')

for w in WFS:
    parts.append(f'<section class="wf" style="--pc:var(--{w["color"]})">')
    parts.append(f'<div class="eyebrow">{w["num"]} · {html.escape(w["name"])}</div>')
    parts.append(f'<h2>{html.escape(w["thesis"])}</h2>')
    parts.append(f'<p class="problem">{html.escape(w["problem"])}</p>')
    parts.append('<figure>')
    parts.append(wf(w["name"], w["color"], w["soft"], w["steps"], w["loop"]))
    parts.append(f'<figcaption>Workflow {w["num"]}. Boxes sit in the lane of whoever does the work; the dashed red return is the loop that feeds the next pillar.</figcaption>')
    parts.append('</figure>')
    parts.append(f'<div class="meta"><div><b>Cadence</b><p>{html.escape(w["cadence"])}</p></div><div><b>Targets and unit economics</b><p>{html.escape(w["kpi"])}</p></div></div>')
    parts.append('</section>')

parts.append('''
<h2 class="sec">Stack map · skills, connectors and agents by pillar</h2>
<div class="twrap">
<table>
<thead><tr><th>Pillar</th><th>Claude skills (built / to build)</th><th>Connectors and tools</th><th>Agents (what runs unattended)</th><th>Human</th><th>Partner / contractor</th></tr></thead>
<tbody>
<tr><td><span class="dot" style="background:var(--p1)"></span>1 Editorial</td><td>fh-content-pipeline (built) · fh-design-system (built) · fh-guest-brief (to build)</td><td>Riverside, Descript, OpusClip, CapCut, HeyGen, ElevenLabs, Beehiiv, YouTube, LinkedIn, 微信公众号, 视频号, Bilibili, Metricool</td><td>Researcher: guest memo and questions · Producer: transcript, cuts, dubs · Publisher: six-channel scheduling and captions · Analyst: weekly numbers</td><td>Host, editor-in-chief, final cut approval, sponsor relationship</td><td>Part-time video editor for flagship episodes; Chinese-language QA</td></tr>
<tr><td><span class="dot" style="background:var(--p2)"></span>2 Advisory</td><td>fh-advisory-report (to build) · fh-meeting-prep (to build, extends the interview-prep work already in this repo)</td><td>Claude Projects, NotebookLM, Perplexity, Elicit, Google Drive, Attio CRM, expert-network calls</td><td>Digester: reads partner reports and client docs into a sourced brief · Modeller: first-draft market sizing and supplier maps · Scheduler: follow-ups</td><td>Thesis, client workshop, pricing, sign-off</td><td>Partner data and analysts; freelance designer for report layout</td></tr>
<tr><td><span class="dot" style="background:var(--p3)"></span>3 Community</td><td>fh-member-digest (to build) · fh-salon-runbook (to build)</td><td>Circle (EU), 知识星球 and 小鹅通 (China), Luma, Stripe, 企业微信, Attio</td><td>Concierge: onboarding, monthly digest, event reminders · Scorer: engagement and renewal flags</td><td>Vetting calls, salon host, renewals with the top 20</td><td>Community coordinator (part-time), trip logistics agency</td></tr>
<tr><td><span class="dot" style="background:var(--p4)"></span>4 Live &amp; Encore</td><td>fh-sponsorship-proposal (built) · fh-sponsor-recap (to build)</td><td>Attio pipeline, Passionfroot inbound, Luma, DocuSign, venue and artist management contacts, Descript for sponsor cut-downs</td><td>Sales desk: rate card, deck, follow-up sequence, pipeline hygiene · Producer: sponsor content cut-downs within 72 hours of the show</td><td>Artist and venue relationship, pricing, pitch, close</td><td>Partner introductions to sponsors; production company; hospitality caterer</td></tr>
<tr><td><span class="dot" style="background:var(--p5)"></span>5 Acceleration</td><td>fh-founder-scorecard (to build) · fh-soft-landing-plan (to build)</td><td>Attio, partner cohort data, Business Sweden and Nordic investor lists, Luma</td><td>Screener: scorecard per company · Matcher: investor and corporate shortlist from the CRM</td><td>Programme design, Nordic introductions, negotiation of economics</td><td>Partner's cohorts and fund; Nordic law firm and accountant for landing</td></tr>
<tr><td>All pillars</td><td>fh-english-coach (built, for every document and speech)</td><td>n8n or Zapier as glue; Google Drive as archive; one shared Attio</td><td>Finance clerk: invoices, collections, monthly P&amp;L by pillar</td><td>Lan: 60% Editorial and Live, 30% Advisory, 10% the rest in year one</td><td>Swedish accountant; Chinese partner entity for fapiao</td></tr>
</tbody>
</table>
</div>

<h2 class="sec">Operating calendar</h2>
<div class="cal">
  <div><b>Weekly</b>Monday: plan and pipeline review (30 min). Tuesday: record two guests. Thursday: review AI cuts, approve. Friday: publish in six channels, send sponsor follow-ups.</div>
  <div><b>Monthly</b>One salon on a Live stage (60–100 guests, 2–3 sponsors). One sponsor recap. One member digest. One P&amp;L by pillar.</div>
  <div><b>Quarterly</b>One editorial season closes and the next opens. One co-branded report. One executive dinner per market. Board-style review with the partner.</div>
  <div><b>Yearly</b>One flagship tour (Encore). One study trip in each direction. One cohort of founders. One "Requests for Companies" list published.</div>
</div>

<h2 class="sec">Team shape · year one</h2>
<div class="team">
  <div><b>Lan Wu · founder</b>Editor-in-chief, host, commercial lead. The only full-time human. Benchmarks for AI-native houses run <span class="num">$150–450k</span> revenue per head (Every, Not Boring, The Rundown).</div>
  <div><b>Contractors · 1.5 FTE equivalent</b>Part-time producer-editor, part-time community coordinator, designer on call, Chinese-language QA. Paid per deliverable, not per month.</div>
  <div><b>Agents · six roles</b>Researcher, Producer, Publisher, Sales desk, Concierge, Finance clerk. Built on the skills in this repo and the Claude Agent SDK; monthly cost below one junior salary.</div>
</div>

<div class="foot"><span>Tool prices and benchmarks: framework/research/04-ai-operating-stack-and-benchmarks.md</span><span>Reads with: 1 Benchmark · 2 Architecture · 4 Encore proposal · 5 Partner pitch</span></div>
</div>''')

with open(OUT, "w") as f:
    f.write("\n".join(parts))
print("wrote", OUT)
