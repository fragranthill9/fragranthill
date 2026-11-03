#!/usr/bin/env python3
"""Build three visual executive one-pagers (EN + ZH) from one content model.
Output: framework/p1-architecture-{en,zh}.html, p2-monetisation-{en,zh}.html, p3-encore-{en,zh}.html
Everything that carries meaning is drawn: a layered architecture map, a buyer-to-pillar flow, charts, icon figures.
"""
import html as H, os, json

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# ----------------------------------------------------------------- palette (Google)
C = dict(blue="#4285F4", red="#EA4335", yellow="#FBBC04", green="#34A853", purple="#A142F4",
         ink="#202124", ink2="#3C4043", muted="#5F6368", line="#DADCE0", line2="#E8EAED", surface="#F8F9FA", accent="#1A73E8",
         blueS="#E8F0FE", redS="#FCE8E6", yellowS="#FEF7E0", greenS="#E6F4EA", purpleS="#F3E8FD", amber="#F29900", yellowD="#B06000")
PC = ["red", "blue", "green", "yellow", "purple"]          # pillar colours 1..5
PS = ["redS", "blueS", "greenS", "yellowS", "purpleS"]
PT = ["#fff", "#fff", "#fff", C["ink"], "#fff"]            # text on pillar header
PICON = ["mic", "compass", "people", "piano", "rocket"]

ICONS = {
 "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4M8 22h8"/>',
 "compass": '<circle cx="12" cy="12" r="10"/><path d="M16 8l-2.5 5.5L8 16l2.5-5.5z"/>',
 "people": '<circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M2 20c0-4 3-6 7-6s7 2 7 6M15 15c3 0 6 1.5 6 5"/>',
 "piano": '<rect x="2" y="5" width="20" height="14" rx="1"/><path d="M6 5v8M10 5v8M14 5v8M18 5v8"/>',
 "rocket": '<path d="M14 4c3 0 6 3 6 6l-8 8-6-6z"/><circle cx="14" cy="10" r="1.5"/><path d="M6 14l-3 1 2-5M10 18l-1 3 5-2M5 19l4-4"/>',
 "building": '<rect x="4" y="3" width="16" height="18"/><path d="M8 7h3M13 7h3M8 11h3M13 11h3M8 15h3M13 15h3M10 21v-3h4v3"/>',
 "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 12h18"/>',
 "coins": '<ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v6c0 1.7 3.6 3 8 3s8-1.3 8-3V6M4 12v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/>',
 "doc": '<path d="M6 2h8l5 5v15H6z"/><path d="M14 2v5h5M9 12h7M9 16h7"/>',
 "ticket": '<path d="M3 9a2 2 0 0 0 2-2V5h14v2a2 2 0 0 0 0 4v2a2 2 0 0 0 0 4v2H5v-2a2 2 0 0 0-2-2z"/><path d="M13 5v14" stroke-dasharray="2 2"/>',
 "star": '<path d="M12 2l3 7 7 .6-5.3 4.6L18.5 21 12 17l-6.5 4 1.8-6.8L2 9.6 9 9z"/>',
 "shield": '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z"/>',
 "door": '<rect x="5" y="2" width="14" height="20" rx="1"/><circle cx="15" cy="12" r="1"/><path d="M19 2l-7 2v18l7-2"/>',
 "net": '<circle cx="12" cy="12" r="3"/><circle cx="4" cy="6" r="2"/><circle cx="20" cy="6" r="2"/><circle cx="4" cy="18" r="2"/><circle cx="20" cy="18" r="2"/><path d="M6 7l4 3M18 7l-4 3M6 17l4-3M18 17l-4-3"/>',
 "film": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M3 15h18M8 4v16M16 4v16"/>',
 "repeat": '<path d="M17 2l4 4-4 4"/><path d="M3 11V9a4 4 0 0 1 4-4h14M7 22l-4-4 4-4"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/>',
 "handshake": '<path d="M2 9l4-4h5l3 3-3 3 4 4 3-3M22 9l-4-4h-3M8 13l3 3M11 16l2 2M14 18l2 2"/>',
 "flag": '<path d="M5 22V3h12l-2 4 2 4H5"/>',
 "chart": '<path d="M3 21h18M6 17V9M11 17V4M16 17v-6"/>',
 "check": '<circle cx="12" cy="12" r="10"/><path d="M8 12l3 3 5-6"/>',
 "pen": '<path d="M3 21l4-1 11-11-3-3L4 17z"/><path d="M14 6l3 3"/>',
 "truck": '<rect x="2" y="7" width="13" height="9"/><path d="M15 10h4l3 3v3h-7z"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>',
 "seat": '<path d="M6 11V6a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v5"/><rect x="3" y="11" width="18" height="6" rx="2"/><path d="M5 17v3M19 17v3"/>',
 "key": '<circle cx="8" cy="14" r="5"/><path d="M12 11l9-9M17 6l3 3M14 9l2 2"/>',
}
def icon(name, x, y, s=1.0, color=C["ink"], sw=2):
    return f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>'

def e(s): return H.escape(str(s))
def wrap(s, n):
    if any(ord(ch) > 0x2E80 for ch in s): n = n // 2 + 2
    out, cur = [], ""
    for w in s.replace("; ", " · ").split(" "):
        if cur and len(cur) + 1 + len(w) > n: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    if cur: out.append(cur)
    return out
def tx(x, y, s, size=12, w=400, fill=None, anc="start", extra=""):
    fill = fill or C["ink"]
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anc}" {extra}>{e(s)}</text>'
MK = '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#5F6368"/></marker><marker id="arb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#1A73E8"/></marker><marker id="ary" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#F29900"/></marker></defs>'

# ----------------------------------------------------------------- CSS
CSS = """
:root{--bg:#FFFFFF;--surface:#F8F9FA;--ink:#202124;--ink-2:#3C4043;--muted:#5F6368;--line:#DADCE0;--accent:#1A73E8;
--font:"Roboto","Noto Sans SC","PingFang SC","Microsoft YaHei",system-ui,sans-serif;color-scheme:light}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);font-size:14px;line-height:1.45;
padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 40px}
.sheet{max-width:1240px;margin:0 auto}
header{display:flex;flex-wrap:wrap;gap:10px 24px;align-items:center;justify-content:space-between;padding:16px 0 12px;border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:12px}
.seal{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;font-weight:700;font-size:13px;color:#fff;background:conic-gradient(#4285F4 0 25%,#EA4335 25% 50%,#FBBC04 50% 75%,#34A853 75% 100%)}
.brand b{font-weight:700;font-size:14px;display:block}.brand span{color:var(--muted);font-size:12px}
.docline{display:flex;align-items:center;gap:14px;font-size:12px;color:var(--muted)}.docline b{color:var(--ink);display:block;font-size:13px}
.pages{display:flex;gap:6px}.pages span{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;font-size:12px;font-weight:700;border:1px solid var(--line);color:var(--muted)}
.pages span.on{background:var(--accent);border-color:var(--accent);color:#fff}
.lang{font-size:12px;font-weight:500;color:var(--accent);text-decoration:none;border:1px solid var(--line);border-radius:16px;padding:4px 12px}
.hero{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:20px;align-items:center;padding:14px 0 2px}
h1{font-size:clamp(24px,3vw,34px);font-weight:700;line-height:1.1;letter-spacing:-.01em;margin:0 0 8px;text-wrap:balance}
.hero p{margin:0;color:var(--ink-2);font-size:15px;max-width:60ch}
.kpis{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.kpi{background:var(--surface);border-radius:12px;padding:10px 12px}
.kpi .n{font-size:22px;font-weight:700;color:var(--accent);font-variant-numeric:tabular-nums;line-height:1.1}
.kpi .l{font-size:11.5px;color:var(--ink-2);margin-top:4px;line-height:1.3}.kpi .l i{display:block;font-style:normal;color:var(--muted);font-size:10px;margin-top:2px}
.grid{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:14px;margin-top:14px}
.c12{grid-column:span 12}.c8{grid-column:span 8}.c7{grid-column:span 7}.c6{grid-column:span 6}.c5{grid-column:span 5}.c4{grid-column:span 4}
.fig{border:1px solid var(--line);border-radius:12px;padding:14px 16px;min-width:0;background:var(--bg)}
.fig h2{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:0 0 8px;font-weight:700;display:flex;align-items:center;gap:8px}
.fn{width:20px;height:20px;border-radius:50%;background:var(--accent);color:#fff;display:inline-grid;place-items:center;font-size:11px;letter-spacing:0}
figure{margin:0;overflow-x:auto}figure svg{display:block;width:100%;height:auto}
figcaption{font-size:11.5px;color:var(--muted);margin-top:8px;line-height:1.4}
.foot{margin-top:14px;font-size:11.5px;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px 20px;justify-content:space-between}
@media (max-width:900px){.hero{grid-template-columns:1fr}.c8,.c7,.c6,.c5,.c4{grid-column:span 12}.kpis{grid-template-columns:1fr 1fr}}
"""
FONT = {"en": '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap">',
        "zh": '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Sans+SC:wght@400;500;700&display=swap">'}

# ----------------------------------------------------------------- content
T = {}
T["en"] = dict(
 brand="Fragrant Hill Studio", sub="Editorial house · Stockholm · Europe ↔ China", other="中文版", conf="Confidential · for partner and investor discussion",
 sources="Sources in framework/research/ · figures are reported unless marked estimate",
 P=["Editorial", "Advisory", "Community", "Live & Venues", "Acceleration"], Pshort=["Editorial", "Advisory", "Community", "Live", "Acceleration"],
 Psub=["the voice", "paid answers", "the vetted room", "the stage · Encore", "the pipeline"],
 Pprod=[["Interview series", "Bilingual newsletter", "Video · LinkedIn · 公众号"], ["Market-entry advisory", "Co-branded reports", "Expert calls"],
        ["Base membership", "Executive club", "Courses · study trips"], ["Encore tour sponsorship", "Executive salons", "Sponsor dinners"],
        ["Soft-landing programme", "Investor scouting", "Corporate pilots"]],
 Pwhen=["pays later", "cash now", "recurring", "cash now", "equity"],
 buyers=["Brands & sponsors", "Clients", "Members", "Brands & sponsors", "Founders & investors"],
 buyers_pay=["season sponsorship", "retainers · reports", "annual dues", "tour packages · tables", "fees · carry"],
 lbl_buyers="WHO PAYS", lbl_pillars="FIVE PRODUCT PILLARS", lbl_core="SHARED CORE · every pillar runs on it", lbl_inputs="INPUTS ALREADY HELD",
 core=[("Editorial voice", "one theme · one host"), ("Relationship graph", "one CRM for all five"), ("Production line", "record once · 6 channels · 2 languages"), ("Commercial desk", "one rate card · invoicing SE + CN")],
 core_icons=["mic", "net", "film", "coins"],
 inputs=[("Founder domain depth", "sensing · robotics · automotive"), ("Stage & talent access", "celebrity concerts · pianist interview"), ("Partner assets", "data · reports · founders · investors"), ("Two-market base", "Swedish AB · China partner")],
 inputs_icons=["compass", "piano", "doc", "building"],
 p1_doc="Page 1 of 3 · System architecture", p1_title="One core. Five pillars. One network.",
 p1_lede="Buyers at the top pay five pillars. One shared core runs all five on inputs we already hold.",
 fig_sys="The system · who pays, what we sell, what it runs on", fig_sys_cap="Read top to bottom: buyers pay the pillars, the pillars run on one core, the core is built from what already exists.",
 fig_cycle="How the pillars feed each other", cycle=["content", "audience", "clients", "deal flow", "sponsors, founders"], cycle_center="ONE NETWORK",
 fig_cycle_cap="Start at Live; the loop closes when sponsors and founders become the next stage.",
 fig_seq="Activation sequence · gated by conditions, not dates", seq=[("A · CASH", "Live + Advisory", "sells access and judgement"), ("B · RECURRING", "Editorial season + Community", "one theme, one rhythm, two tiers"), ("C · EQUITY", "Acceleration", "deal flow to investors")],
 gates=["rights and categories confirmed", "a sponsorship funds the season", "club and advisory clients exist"],
 fig_seq_cap="Each step starts only when the gate below it is true.",
 facts=[("€34.5bn", "European sponsorship market 2025; arts and culture 28%", "ESA / Nielsen Sports 2026"), ("50–60%", "of Semafor revenue is event sponsorship; profitable 2025", "Semafor, Nieman Lab"), ("<5%", "of SemiAnalysis revenue is subscriptions", "The Information, estimate")],
 # page 2
 p2_doc="Page 2 of 3 · Monetisation", p2_title="Four kinds of buyer, six revenue streams, five pillars.",
 p2_lede="Follow the money left to right: who pays, through which stream, into which pillar.",
 fig_flow="Where the money comes from and where it lands",
 flow_buyers=["Brands & sponsors", "Clients", "Members & guests", "Founders & investors"],
 streams=["Sponsorship", "Service fees", "Membership", "Tickets & hospitality", "Licences & reports", "Equity & carry"],
 fig_flow_cap="Band colour follows the pillar; widths are equal because this is structure, not a forecast.",
 fig_bench="Where proven media houses actually earn · share of revenue", bench=[("Semafor · sponsored events", 55, "reported 2025"), ("吴晓波年终秀 · sponsorship", 90, "reported"), ("SemiAnalysis · research & advisory", 95, "estimate"), ("得到 Dedao · online courses", 64, "reported 2021"), ("The Information · subscriptions", 90, "reported")],
 fig_bench_cap="Sponsored rooms, research and courses carry the benchmarks; subscriptions only at The Information's scale.",
 fig_when="When each pillar pays", when_lanes=[("CASH NOW", [3, 1]), ("RECURRING", [0, 2]), ("EQUITY", [4])],
 fig_when_cap="Live and Advisory pay before an audience exists; Acceleration pays last.",
 fig_unit="What one sale looks like", units=[("Season package", "one sponsor per season", "mic"), ("Retainer · report", "outcome-priced · per-seat licence", "doc"), ("Annual seat", "base tier · vetted club", "key"), ("Tour package · table", "naming · VIP tables · content", "ticket"), ("Programme fee · carry", "per company, per round", "rocket")],
 fig_work="Who does the work", work=[("Human", "theme · relationships · price", "people"), ("Digital agents", "research · production · publishing · finance", "net"), ("Partner", "data · cohorts · introductions · China invoicing", "handshake")],
 # page 3
 p3_doc="Page 3 of 3 · The project · Encore", p3_eyebrow="ENCORE · SPONSORSHIP PROGRAMME FOR A WORLD-CLASS PIANIST'S EUROPEAN TOUR", p3_title="Sell the room, not the reach.",
 p3_lede="A celebrity tour packaged as sponsorship, hospitality and content for automotive, robotics and tech brands. Fragrant Hill holds the stage; the partner holds the doors.",
 kp3=[("5,000", "Royal Albert Hall tickets sold in 48 hours for one recital", "Classic FM, 2013"), ("0", "whole-tour presenting partners ever announced for this artist", "research notes 3"), ("62%", "of European brands want to sponsor culture; 61% do not yet", "ESA arts survey")],
 fig_ladder="The package ladder · what each tier buys", ladder=[("1 Presenting partner", ["naming across the tour", "category exclusivity", "VIP tables · private recital", "12-month content rights"]), ("3 Official partners", ["one per category", "programme and screen branding", "VIP table per city", "content pack"]), ("6 Hospitality partners", ["premium seat blocks", "lounge access and branding", "photo and social assets"])],
 ladder_cap="Fees set per market against precedents; deposit on signature, balance before the first show.",
 fig_money="How the money flows", money=dict(sp="SPONSORS", rights="rights fees", hosp="hospitality fees", prog="ENCORE", p1="contracts · exclusivity", p2="deposit on signature", o=[("Tour producer", "artist · venues · production", "piano"), ("Fragrant Hill", "commission · fees", "star"), ("Partner", "share on introduced sponsors", "handshake")], back="value back: hospitality · association · content · reach"),
 money_cap="B2B sponsors measure hospitality: dealer and client evenings in a concert hall.",
 fig_prec="Automotive and finance brands in classical music · years of partnership", prec=[("Deutsche Bank · Berlin Phil", 1989, 2030), ("Audi · Salzburg Festival", 1995, 2027), ("BMW · Opera for All", 1997, 2030), ("Rolex · Vienna Philharmonic", 2008, 2026), ("Porsche · Gewandhaus Leipzig", 2011, 2026), ("VW Group · artist ambassador", 2012, 2026)],
 prec_cap="A thirty-year playbook for European brands, unused so far by Chinese brands in Europe.",
 fig_mkt="European sponsorship 2025 · € billion", mkt=[("Sport", 24.8, "blue"), ("Arts, culture, entertainment", 9.7, "yellow")], mkt_countries=[("Germany", 6.26), ("UK", 6.15), ("Spain", 2.18), ("Italy", 2.01), ("France", 1.85)],
 mkt_cap="ESA / Nielsen Sports 2026 · total €34.5bn, up 4.7%.",
 fig_steps="How it proceeds", steps=[("Secure", "rights · dates · open categories", "key"), ("Sell", "three tiers · warm introductions · deposits", "handshake"), ("Deliver", "production · hospitality · content", "film"), ("Renew", "first refusal · salon series", "repeat")],
 steps_owner=["Fragrant Hill", "Fragrant Hill + partner", "Fragrant Hill + contractors", "Fragrant Hill"],
 fig_roles="Three parties, one exchange", roles=dict(fh="FRAGRANT HILL", pa="PARTNER", sp="SPONSOR", fh_sp="stage · packages · hospitality · content", sp_fh="rights fees · guest lists", pa_fh="warm introductions", fh_pa="share on closed deals"),
 fig_risk="Risks and controls", risks=[("Category conflict", "open categories confirmed in writing before any pitch", "shield"), ("Sales cycle", "warm introductions only; base of three signatures", "flag"), ("Artist · venue · payment", "insurance · venue options · non-refundable deposits", "check")],
 fig_rep="Why it repeats", rep=[("Annual tour edition", "repeat"), ("Executive salons on the same stages", "people"), ("Content and guest lists for every pillar", "film")],
)

T["zh"] = dict(
 brand="香山工作室", sub="编辑内容机构 · 斯德哥尔摩 · 欧洲 ↔ 中国", other="English", conf="保密 · 供合作伙伴与投资人讨论",
 sources="资料来源见 framework/research/ · 除标注估算外均为公开报道",
 P=["内容", "咨询", "社群", "现场与场馆", "加速"], Pshort=["内容", "咨询", "社群", "现场", "加速"],
 Psub=["声音", "付费答案", "筛选过的圈子", "舞台 · 安可", "项目通道"],
 Pprod=[["访谈系列", "双语通讯", "视频 · LinkedIn · 公众号"], ["市场进入咨询", "联名报告", "专家访谈"],
        ["基础会员", "高管俱乐部", "课程 · 考察团"], ["安可巡演赞助", "高管沙龙", "赞助商晚宴"],
        ["软着陆计划", "为投资人寻源", "企业试点对接"]],
 Pwhen=["稍后变现", "即时现金", "持续收入", "即时现金", "股权"],
 buyers=["品牌与赞助商", "客户", "会员", "品牌与赞助商", "创始人与投资人"],
 buyers_pay=["内容季赞助", "顾问费 · 报告", "年费", "巡演套餐 · VIP 桌", "费用 · 收益分成"],
 lbl_buyers="谁付费", lbl_pillars="五大产品支柱", lbl_core="共享核心 · 每个支柱都运行在其上", lbl_inputs="已经持有的资源",
 core=[("内容之声", "一个主题 · 一位主持人"), ("关系图谱", "五个支柱共用一个 CRM"), ("生产线", "一次录制 · 6 个渠道 · 2 种语言"), ("商务与后台", "一张价目表 · 瑞典与中国开票")],
 core_icons=["mic", "net", "film", "coins"],
 inputs=[("创始人行业深度", "传感 · 机器人 · 汽车"), ("舞台与艺人资源", "名人音乐会 · 钢琴家专访"), ("伙伴资产", "数据 · 报告 · 创始人 · 投资人"), ("双市场基础", "瑞典公司 · 中国伙伴")],
 inputs_icons=["compass", "piano", "doc", "building"],
 p1_doc="第 1 页 / 共 3 页 · 系统架构", p1_title="一个核心，五大支柱，同一张关系网。",
 p1_lede="上方的买家付费给五大支柱；一个共享核心运行全部五个支柱，建立在已有资源之上。",
 fig_sys="系统全貌 · 谁付费、我们卖什么、靠什么运行", fig_sys_cap="自上而下：买家付费给支柱，支柱运行在一个核心上，核心由已有资源构成。",
 fig_cycle="支柱之间如何互相输送", cycle=["内容", "受众", "客户", "项目源", "赞助商与创始人"], cycle_center="同一张网",
 fig_cycle_cap="从「现场」开始；当赞助商与创始人成为下一个舞台，循环闭合。",
 fig_seq="启动顺序 · 按条件推进，不按日期", seq=[("A · 现金", "现场 + 咨询", "卖的是接触权与判断力"), ("B · 持续收入", "内容季 + 社群", "一个主题、一个节奏、两档会员"), ("C · 股权", "加速", "项目源对接企业与投资人")],
 gates=["舞台权益与赞助品类已确认", "一笔赞助支撑内容季", "已有俱乐部与咨询客户"],
 fig_seq_cap="只有下方的前提成立，才进入下一步。",
 facts=[("€345亿", "2025 年欧洲赞助市场；艺术文化占 28%", "ESA / Nielsen Sports 2026"), ("50–60%", "Semafor 收入来自活动赞助；2025 年盈利", "Semafor, Nieman Lab"), ("<5%", "SemiAnalysis 收入来自订阅", "The Information，估算")],
 p2_doc="第 2 页 / 共 3 页 · 变现方式", p2_title="四类买家，六类收入，五大支柱。",
 p2_lede="从左到右跟着钱走：谁付费、经过哪类收入、落到哪个支柱。",
 fig_flow="钱从哪里来，落到哪里",
 flow_buyers=["品牌与赞助商", "客户", "会员与嘉宾", "创始人与投资人"],
 streams=["赞助", "服务费", "会员费", "票务与款待", "授权与报告", "股权与分成"],
 fig_flow_cap="色带颜色跟随支柱。宽度相同，因为这是结构图，不是预测。",
 fig_bench="成熟媒体机构真正的收入来源 · 占总收入比例", bench=[("Semafor · 赞助活动", 55, "2025 年报道"), ("吴晓波年终秀 · 赞助", 90, "报道"), ("SemiAnalysis · 研究与咨询", 95, "估算"), ("得到 · 在线课程", 64, "2021 年报道"), ("The Information · 订阅", 90, "报道")],
 fig_bench_cap="赞助的现场、研究和课程支撑了对标企业；订阅只在 The Information 的规模下成立。",
 fig_when="每个支柱何时回款", when_lanes=[("即时现金", [3, 1]), ("持续收入", [0, 2]), ("股权", [4])],
 fig_when_cap="现场与咨询在受众形成前即可回款；加速最后。",
 fig_unit="一笔交易长什么样", units=[("内容季套餐", "每季一家冠名赞助商", "mic"), ("顾问费 · 报告", "按成果定价，按席位授权", "doc"), ("年度席位", "基础档 · 筛选制俱乐部", "key"), ("巡演套餐 · VIP 桌", "冠名、VIP 桌、内容权益", "ticket"), ("计划费 · 收益分成", "按公司、按轮次", "rocket")],
 fig_work="谁来做", work=[("人", "主题 · 关系 · 定价", "people"), ("数字代理", "研究 · 制作 · 发布 · 财务", "net"), ("伙伴", "数据 · 创始人营 · 引荐 · 中国开票", "handshake")],
 p3_doc="第 3 页 / 共 3 页 · 项目 · 安可", p3_eyebrow="安可 ENCORE · 世界级钢琴家欧洲巡演赞助计划", p3_title="卖的是现场，不是流量。",
 p3_lede="把名人巡演打包成赞助、款待与内容资产，卖给汽车、机器人与科技品牌。香山掌握舞台，伙伴掌握大门。",
 kp3=[("5,000", "皇家阿尔伯特音乐厅一场独奏会 48 小时售出的票数", "Classic FM, 2013"), ("0", "该艺术家历史上公布过的整巡演冠名伙伴数量", "研究笔记 3"), ("62%", "的欧洲品牌希望赞助文化；61% 尚未开始", "ESA 艺术调研")],
 fig_ladder="赞助阶梯 · 每一档买到什么", ladder=[("1 家冠名伙伴", ["整个巡演冠名", "品类独家", "VIP 桌 · 私人独奏会", "12 个月内容权益"]), ("3 家官方伙伴", ["每品类一家", "节目册与屏幕露出", "每城一桌 VIP", "内容包"]), ("6 家款待伙伴", ["高级座位区", "贵宾室使用与露出", "照片与社交素材"])],
 ladder_cap="费用按市场参照先例设定；签约付定金，首场前付尾款。",
 fig_money="资金如何流动", money=dict(sp="赞助商", rights="权益费", hosp="款待费", prog="安可计划", p1="合同 · 品类独家", p2="签约付定金", o=[("巡演制作方", "艺术家 · 场馆 · 制作", "piano"), ("香山", "佣金 · 制作服务费", "star"), ("伙伴", "引荐赞助商的分成", "handshake")], back="回馈赞助商：款待 · 品牌联结 · 内容 · 触达"),
 money_cap="B2B 赞助商衡量的是款待：音乐厅里的经销商与客户之夜。",
 fig_prec="古典音乐中的汽车与金融品牌 · 合作年限", prec=[("德意志银行 · 柏林爱乐", 1989, 2030), ("奥迪 · 萨尔茨堡音乐节", 1995, 2027), ("宝马 · 人人歌剧", 1997, 2030), ("劳力士 · 维也纳爱乐", 2008, 2026), ("保时捷 · 莱比锡布商大厦", 2011, 2026), ("大众集团 · 艺术家大使", 2012, 2026)],
 prec_cap="欧洲品牌已用了三十年的打法，中国品牌在欧洲尚未使用。",
 fig_mkt="2025 年欧洲赞助市场 · 十亿欧元", mkt=[("体育", 24.8, "blue"), ("艺术、文化、娱乐", 9.7, "yellow")], mkt_countries=[("德国", 6.26), ("英国", 6.15), ("西班牙", 2.18), ("意大利", 2.01), ("法国", 1.85)],
 mkt_cap="ESA / Nielsen Sports 2026 · 总计 345 亿欧元，同比增长 4.7%。",
 fig_steps="推进步骤", steps=[("锁定", "权益 · 日期 · 开放品类", "key"), ("销售", "三档套餐 · 引荐 · 定金", "handshake"), ("交付", "制作 · 款待 · 内容", "film"), ("续约", "优先续约权 · 沙龙系列", "repeat")],
 steps_owner=["香山", "香山 + 伙伴", "香山 + 外部团队", "香山"],
 fig_roles="三方，一个交换", roles=dict(fh="香山", pa="伙伴", sp="赞助商", fh_sp="舞台 · 套餐 · 款待 · 内容", sp_fh="权益费 · 嘉宾名单", pa_fh="引荐", fh_pa="成交分成"),
 fig_risk="风险与对策", risks=[("品类冲突", "提案前书面确认开放品类", "shield"), ("销售周期", "只通过引荐；以三份签约为基础", "flag"), ("艺术家 · 场馆 · 付款", "保险 · 场馆预留 · 定金不退", "check")],
 fig_rep="为什么可以复制", rep=[("年度巡演", "repeat"), ("同一舞台上的高管沙龙", "people"), ("为每个支柱提供内容与嘉宾名单", "film")],
)

# ----------------------------------------------------------------- shell
def head(t, doc, page, other):
    pg = "".join(f'<span class="{"on" if i == page else ""}">{i}</span>' for i in (1, 2, 3))
    return f'''<header><div class="brand"><div class="seal">香山</div><div><b>{e(t["brand"])}</b><span>{e(t["sub"])}</span></div></div>
<div class="docline"><div><b>{e(doc)}</b>{e(t["conf"])}</div><div class="pages">{pg}</div><a class="lang" href="{other}">{e(t["other"])} →</a></div></header>'''

def kpis(items):
    return '<div class="kpis">' + "".join(f'<div class="kpi"><div class="n">{e(n)}</div><div class="l">{e(l)}<i>{e(s)}</i></div></div>' for n, l, s in items) + '</div>'

def shell(t, lang, title, body):
    return f'<title>{e(title)}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONT[lang]}\n<style>{CSS}</style>\n<div class="sheet" lang="{"zh-CN" if lang=="zh" else "en"}">{body}</div>'

FIGN = [0]
def fig(cls, h2, svg, cap):
    FIGN[0] += 1
    capo = f'<figcaption>{e(cap)}</figcaption>' if cap else ''
    return f'<div class="fig {cls}"><h2><span class="fn">{FIGN[0]}</span>{e(h2)}</h2><figure>{svg}</figure>{capo}</div>'

# ----------------------------------------------------------------- page 1 figures
def sys_map(t):
    W = 1240; colw = 232; gap = 14; x0 = 12
    xs = [x0 + i * (colw + gap) for i in range(5)]
    o = [f'<svg viewBox="0 0 {W} 660" role="img" aria-label="Layered system map: five buyers at the top pay five pillars; the pillars run on a shared core of four modules; the core is built on four inputs already held." xmlns="http://www.w3.org/2000/svg">', MK]
    # buyers row
    o.append(tx(x0, 22, t["lbl_buyers"], 11, 700, C["muted"], extra='letter-spacing=".1em"'))
    bicons = ["building", "briefcase", "people", "building", "coins"]
    for i, x in enumerate(xs):
        o.append(f'<rect x="{x}" y="32" width="{colw}" height="58" rx="10" fill="{C["surface"]}" stroke="{C["line"]}"/>')
        o.append(icon(bicons[i], x + 12, 44, 1.4, C["ink2"]))
        o.append(tx(x + 54, 54, t["buyers"][i], 13, 700))
        o.append(tx(x + 54, 74, t["buyers_pay"][i], 11, 400, C["muted"]))
        cx = x + colw / 2
        o.append(f'<path d="M{cx} 92 V124" stroke="{C["amber"]}" stroke-width="2.2" marker-end="url(#ary)"/>')
        o.append(tx(cx + 8, 112, "€", 12, 700, C["amber"]))
    # pillars
    o.append(tx(x0, 146, t["lbl_pillars"], 11, 700, C["muted"], extra='letter-spacing=".1em"'))
    for i, x in enumerate(xs):
        c = C[PC[i]]
        o.append(f'<rect x="{x}" y="156" width="{colw}" height="206" rx="12" fill="#fff" stroke="{C["line"]}"/>')
        o.append(f'<path d="M{x} 168a12 12 0 0 1 12-12h{colw-24}a12 12 0 0 1 12 12v50H{x}z" fill="{c}"/>')
        o.append(icon(PICON[i], x + 14, 168, 1.3, PT[i], 2.2))
        o.append(tx(x + 54, 182, f'{i+1} · {t["P"][i]}', 15, 700, PT[i]))
        o.append(tx(x + 54, 200, t["Psub"][i], 11, 500, PT[i], extra='opacity=".9"'))
        for k, pr in enumerate(t["Pprod"][i]):
            o.append(f'<circle cx="{x+22}" cy="{238 + k*26}" r="3.5" fill="{c}"/>')
            o.append(tx(x + 34, 242 + k * 26, pr, 12.5, 500, C["ink2"]))
        # when chip
        soft = C[PS[i]]; tcol = C["yellowD"] if PC[i] == "yellow" else c
        o.append(f'<rect x="{x+14}" y="322" width="118" height="26" rx="13" fill="{soft}"/>')
        o.append(tx(x + 73, 339, t["Pwhen"][i], 11.5, 700, tcol, "middle"))
        cx = x + colw / 2
        o.append(f'<path d="M{cx} 396 V366" stroke="{C["muted"]}" stroke-width="1.6" marker-end="url(#ar)"/>')
    # core
    o.append(f'<rect x="{x0}" y="400" width="{W-2*x0}" height="100" rx="12" fill="{C["blueS"]}" stroke="#AECBFA"/>')
    o.append(tx(x0 + 16, 420, t["lbl_core"], 11, 700, C["accent"], extra='letter-spacing=".1em"'))
    cw = (W - 2 * x0 - 32) / 4
    for i, (a, b) in enumerate(t["core"]):
        x = x0 + 16 + i * cw
        o.append(icon(t["core_icons"][i], x, 434, 1.5, C["accent"]))
        o.append(tx(x + 46, 450, a, 14, 700))
        o.append(tx(x + 46, 470, b, 11.5, 400, C["ink2"]))
        if i:
            o.append(f'<line x1="{x-12}" y1="434" x2="{x-12}" y2="490" stroke="#AECBFA"/>')
    for i in range(4):
        cx = x0 + 16 + i * cw + cw / 2
        o.append(f'<path d="M{cx} 534 V504" stroke="{C["muted"]}" stroke-width="1.6" marker-end="url(#ar)"/>')
    # inputs
    o.append(f'<rect x="{x0}" y="538" width="{W-2*x0}" height="100" rx="12" fill="{C["surface"]}" stroke="{C["line"]}"/>')
    o.append(tx(x0 + 16, 558, t["lbl_inputs"], 11, 700, C["muted"], extra='letter-spacing=".1em"'))
    for i, (a, b) in enumerate(t["inputs"]):
        x = x0 + 16 + i * cw
        o.append(icon(t["inputs_icons"][i], x, 572, 1.5, C["ink2"]))
        o.append(tx(x + 46, 588, a, 14, 700))
        o.append(tx(x + 46, 608, b, 11.5, 400, C["ink2"]))
        if i:
            o.append(f'<line x1="{x-12}" y1="572" x2="{x-12}" y2="628" stroke="{C["line"]}"/>')
    o.append('</svg>')
    return "\n".join(o)

def cycle_fig(t):
    L = t["cycle"]; names = [f'4 · {t["Pshort"][3]}', f'1 · {t["Pshort"][0]}', f'3 · {t["Pshort"][2]}', f'2 · {t["Pshort"][1]}', f'5 · {t["Pshort"][4]}']
    cols = ["yellow", "red", "green", "blue", "purple"]; icons_ = ["piano", "mic", "people", "compass", "rocket"]
    pos = [(310, 56), (470, 170), (408, 352), (212, 352), (150, 170)]
    o = ['<svg viewBox="0 0 620 420" role="img" aria-label="Cycle of five pillars with one network in the centre." xmlns="http://www.w3.org/2000/svg">', MK]
    arrows = [("M388 66 L432 138", 428, 94, "start"), ("M470 196 L432 304", 462, 256, "start"), ("M328 352 L292 352", 310, 386, "middle"), ("M166 326 L140 196", 148, 266, "end"), ("M176 142 L236 66", 206, 94, "end")]
    for (d, lx, ly, anc), lbl in zip(arrows, L):
        o.append(f'<path d="{d}" stroke="{C["muted"]}" stroke-width="1.6" fill="none" marker-end="url(#ar)"/>')
        o.append(tx(lx, ly, lbl, 12, 500, C["ink2"], anc))
    for (x, y), n, c, ic in zip(pos, names, cols, icons_):
        tcol = C["yellowD"] if c == "yellow" else C[c]
        o.append(f'<rect x="{x-80}" y="{y-22}" width="160" height="44" rx="22" fill="{C[c+"S"]}" stroke="{C[c]}" stroke-width="1.6"/>')
        o.append(icon(ic, x - 66, y - 12, 1.0, tcol))
        o.append(tx(x + 8, y + 5, n, 13, 700, tcol, "middle"))
    o.append(f'<circle cx="310" cy="210" r="48" fill="#fff" stroke="{C["accent"]}" stroke-width="1.8"/>')
    o.append(icon("net", 298, 184, 1.0, C["accent"]))
    o.append(tx(310, 228, t["cycle_center"], 10.5, 700, C["accent"], "middle"))
    o.append('</svg>')
    return "\n".join(o)

def seq_fig(t):
    o = ['<svg viewBox="0 0 620 300" role="img" aria-label="Three rising steps: cash, recurring, equity, each with a gate condition." xmlns="http://www.w3.org/2000/svg">', MK]
    cols = ["yellow", "red", "purple"]; pil = [[3, 1], [0, 2], [4]]
    for i, ((a, b, c), col, pi) in enumerate(zip(t["seq"], cols, pil)):
        x = 14 + i * 204; top = 150 - i * 60; h = 300 - top - 60
        tcol = C["yellowD"] if col == "yellow" else C[col]
        o.append(f'<rect x="{x}" y="{top}" width="190" height="{h}" rx="10" fill="{C[col+"S"]}" stroke="{C[col]}" stroke-width="1.4"/>')
        o.append(tx(x + 14, top + 24, a, 11.5, 700, tcol, extra='letter-spacing=".08em"'))
        for k, p in enumerate(pi):
            o.append(f'<circle cx="{x+22+k*20}" cy="{top+44}" r="7" fill="{C[PC[p]]}"/>')
        o.append(tx(x + 14, top + 70, b, 13.5, 700))
        o.append(tx(x + 14, top + 90, c, 11.5, 400, C["ink2"]))
        if i < 2:
            o.append(f'<path d="M{x+192} {top-30} H{x+202}" stroke="{C["muted"]}" stroke-width="1.6" marker-end="url(#ar)"/>')
        # gate
        o.append(f'<rect x="{x}" y="252" width="190" height="38" rx="8" fill="#fff" stroke="{C["line"]}" stroke-dasharray="4 3"/>')
        o.append(icon("key", x + 8, 259, 0.9, C["muted"]))
        o.append(tx(x + 34, 276, t["gates"][i], 10.5, 500, C["ink2"]))
    o.append('</svg>')
    return "\n".join(o)

def page1(t, lang, other):
    FIGN[0] = 0
    body = head(t, t["p1_doc"], 1, other) + f'''
<div class="hero"><div><h1>{e(t["p1_title"])}</h1><p>{e(t["p1_lede"])}</p></div>{kpis(t["facts"])}</div>
<div class="grid">
{fig("c12", t["fig_sys"], sys_map(t), t["fig_sys_cap"])}
{fig("c6", t["fig_cycle"], cycle_fig(t), t["fig_cycle_cap"])}
{fig("c6", t["fig_seq"], seq_fig(t), t["fig_seq_cap"])}
</div><div class="foot"><span>{e(t["sources"])}</span><span>{e(t["brand"])}</span></div>'''
    return shell(t, lang, {"en": "Fragrant Hill Architecture", "zh": "香山系统架构"}[lang], body)

# ----------------------------------------------------------------- page 2 figures
def flow_fig(t):
    W, Hh = 1240, 560
    L = [(40, 70 + i * 120, 220, 72) for i in range(4)]                 # buyers
    M = [(500, 36 + i * 86, 220, 60) for i in range(6)]                 # streams
    R = [(980, 50 + i * 100, 220, 72) for i in range(5)]                # pillars
    lm = [(0, 0), (0, 3), (1, 1), (1, 4), (2, 2), (2, 3), (3, 1), (3, 5)]          # buyer -> stream
    mr = [(0, 3), (0, 0), (0, 2), (1, 1), (1, 4), (2, 2), (3, 3), (3, 2), (4, 1), (4, 0), (5, 4)]  # stream -> pillar
    o = [f'<svg viewBox="0 0 {W} {Hh}" role="img" aria-label="Flow from four buyer types through six revenue streams into five pillars." xmlns="http://www.w3.org/2000/svg">']
    def band(x1, y1, x2, y2, color, op=.55, w=16):
        mx = (x1 + x2) / 2
        return f'<path d="M{x1} {y1} C{mx} {y1} {mx} {y2} {x2} {y2}" stroke="{color}" stroke-width="{w}" fill="none" opacity="{op}" stroke-linecap="butt"/>'
    # offsets to spread multiple links per node
    from collections import defaultdict
    outL = defaultdict(list); inM = defaultdict(list); outM = defaultdict(list); inR = defaultdict(list)
    for a, b in lm: outL[a].append(b); inM[b].append(a)
    for a, b in mr: outM[a].append(b); inR[b].append(a)
    def slot(lst, key, n_total, y, h):
        k = lst.index(key); return y + h * (k + 1) / (n_total + 1)
    for a, b in lm:
        x1, y1, w1, h1 = L[a]; x2, y2, w2, h2 = M[b]
        o.append(band(x1 + w1, slot(outL[a], b, len(outL[a]), y1, h1), x2, slot(inM[b], a, len(inM[b]), y2, h2), C["muted"], .28))
    for a, b in mr:
        x1, y1, w1, h1 = M[a]; x2, y2, w2, h2 = R[b]
        o.append(band(x1 + w1, slot(outM[a], b, len(outM[a]), y1, h1), x2, slot(inR[b], a, len(inR[b]), y2, h2), C[PC[b]], .6))
    bic = ["building", "briefcase", "people", "coins"]
    for i, (x, y, w, h) in enumerate(L):
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{C["surface"]}" stroke="{C["line"]}"/>')
        o.append(icon(bic[i], x + 14, y + 22, 1.2, C["ink2"]))
        o.append(tx(x + 52, y + 43, t["flow_buyers"][i], 13.5, 700))
    sic = ["star", "briefcase", "key", "ticket", "doc", "rocket"]
    for i, (x, y, w, h) in enumerate(M):
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fff" stroke="{C["ink2"]}" stroke-width="1.4"/>')
        o.append(icon(sic[i], x + 12, y + 18, 1.0, C["ink2"]))
        o.append(tx(x + 46, y + 36, t["streams"][i], 13, 700))
    for i, (x, y, w, h) in enumerate(R):
        c = C[PC[i]]
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c}"/>')
        o.append(icon(PICON[i], x + 14, y + 22, 1.2, PT[i], 2.2))
        o.append(tx(x + 52, y + 32, f'{i+1} · {t["P"][i]}', 13.5, 700, PT[i]))
        o.append(tx(x + 52, y + 48, t["units"][i][0], 11, 500, PT[i], extra='opacity=".95"'))
        o.append(tx(x + 52, y + 62, t["Pwhen"][i], 10.5, 400, PT[i], extra='opacity=".85"'))
    o.append(tx(40, 24, t["lbl_buyers"] if "lbl_buyers" in t else "", 11, 700, C["muted"], extra='letter-spacing=".1em"'))
    o.append('</svg>')
    return "\n".join(o)

def bench_fig(t):
    o = ['<svg viewBox="0 0 620 250" role="img" aria-label="Horizontal bars: share of revenue from the main non-advertising source for five benchmarked media businesses." xmlns="http://www.w3.org/2000/svg">']
    for i, (name, v, src) in enumerate(t["bench"]):
        y = 18 + i * 46
        o.append(tx(0, y + 14, name, 12, 500, C["ink"]))
        o.append(f'<rect x="0" y="{y+20}" width="{v*4.4:.0f}" height="14" rx="3" fill="{C["blue"]}"/>')
        o.append(tx(v * 4.4 + 8, y + 32, f"{v}%", 12, 700, C["ink"]))
        o.append(tx(620, y + 14, src, 10.5, 400, C["muted"], "end"))
    o.append('</svg>')
    return "\n".join(o)

def when_fig(t):
    o = ['<svg viewBox="0 0 620 230" role="img" aria-label="Three lanes, cash now, recurring, equity, with pillar markers placed in sequence." xmlns="http://www.w3.org/2000/svg">', MK]
    cols = ["yellow", "green", "purple"]
    for i, ((lbl, pil), col) in enumerate(zip(t["when_lanes"], cols)):
        y = 16 + i * 70
        tcol = C["yellowD"] if col == "yellow" else C[col]
        o.append(f'<rect x="0" y="{y}" width="620" height="58" rx="10" fill="{C[col+"S"]}"/>')
        o.append(tx(14, y + 34, lbl, 11, 700, tcol, extra='letter-spacing=".1em"'))
        for k, p in enumerate(pil):
            x = 130 + i * 120 + k * 180
            c = C[PC[p]]
            o.append(f'<rect x="{x}" y="{y+11}" width="170" height="36" rx="18" fill="#fff" stroke="{c}" stroke-width="1.6"/>')
            o.append(icon(PICON[p], x + 12, y + 17, 1.0, C["yellowD"] if PC[p] == "yellow" else c))
            o.append(tx(x + 44, y + 34, f'{p+1} · {t["P"][p]}', 12.5, 700, C["ink"]))
    o.append(f'<path d="M30 212 H600" stroke="{C["muted"]}" stroke-width="1.6" marker-end="url(#ar)"/>')
    o.append('</svg>')
    return "\n".join(o)

def units_fig(t):
    o = ['<svg viewBox="0 0 1240 120" role="img" aria-label="Five tiles describing the unit of sale per pillar." xmlns="http://www.w3.org/2000/svg">']
    for i, (a, b, ic) in enumerate(t["units"]):
        x = 12 + i * 246; c = C[PC[i]]; tcol = C["yellowD"] if PC[i] == "yellow" else c
        o.append(f'<rect x="{x}" y="8" width="232" height="100" rx="12" fill="{C["surface"]}"/>')
        o.append(f'<rect x="{x}" y="8" width="232" height="6" rx="3" fill="{c}"/>')
        o.append(icon(ic, x + 14, 34, 1.5, tcol))
        o.append(tx(x + 60, 46, a, 14, 700))
        o.append(tx(x + 60, 68, b, 11.5, 400, C["ink2"]))
        o.append(tx(x + 60, 92, f'{i+1} · {t["P"][i]}', 10.5, 700, tcol))
    o.append('</svg>')
    return "\n".join(o)

def work_fig(t):
    o = ['<svg viewBox="0 0 1240 92" role="img" aria-label="Three tiles: human, digital agents, partner." xmlns="http://www.w3.org/2000/svg">']
    for i, (a, b, ic) in enumerate(t["work"]):
        x = 12 + i * 410
        o.append(f'<rect x="{x}" y="8" width="396" height="76" rx="12" fill="{C["surface"]}"/>')
        o.append(icon(ic, x + 16, 26, 1.6, C["accent"]))
        o.append(tx(x + 64, 40, a, 15, 700))
        o.append(tx(x + 64, 64, b, 12, 400, C["ink2"]))
    o.append('</svg>')
    return "\n".join(o)

def page2(t, lang, other):
    FIGN[0] = 0
    body = head(t, t["p2_doc"], 2, other) + f'''
<div class="hero"><div><h1>{e(t["p2_title"])}</h1><p>{e(t["p2_lede"])}</p></div>{kpis(t["facts"])}</div>
<div class="grid">
{fig("c12", t["fig_flow"], flow_fig(t), t["fig_flow_cap"])}
{fig("c6", t["fig_bench"], bench_fig(t), t["fig_bench_cap"])}
{fig("c6", t["fig_when"], when_fig(t), t["fig_when_cap"])}
</div><div class="foot"><span>{e(t["sources"])}</span><span>{e(t["brand"])}</span></div>'''
    return shell(t, lang, {"en": "Fragrant Hill Monetisation", "zh": "香山变现方式"}[lang], body)

# ----------------------------------------------------------------- page 3 figures
def ladder_fig(t):
    o = ['<svg viewBox="0 0 620 300" role="img" aria-label="Pyramid of three sponsor tiers with what each tier receives." xmlns="http://www.w3.org/2000/svg">']
    tiers = t["ladder"]
    geo = [(170, 20, 280, 80, C["yellow"], C["ink"]), (120, 110, 380, 80, "#FDD663", C["ink"]), (70, 200, 480, 80, C["yellowS"], C["ink"])]
    for (x, y, w, h, fill, tc), (name, items) in zip(geo, tiers):
        o.append(f'<path d="M{x+20} {y} H{x+w-20} L{x+w} {y+h} H{x} Z" fill="{fill}" stroke="#F29900" stroke-width="1.2"/>')
        o.append(tx(x + w / 2, y + 30, name, 14, 700, tc, "middle"))
        o.append(tx(x + w / 2, y + 52, " · ".join(items[:2]), 10.5, 500, tc, "middle"))
        o.append(tx(x + w / 2, y + 68, " · ".join(items[2:]), 10.5, 500, tc, "middle"))
    o.append('</svg>')
    return "\n".join(o)

def money_fig(t):
    f = t["money"]
    o = ['<svg viewBox="0 0 760 290" role="img" aria-label="Money flow from sponsors into the Encore programme and out to the tour producer, Fragrant Hill and the partner; value returns to sponsors." xmlns="http://www.w3.org/2000/svg">', MK]
    o.append(f'<rect x="10" y="70" width="180" height="140" rx="12" fill="{C["surface"]}" stroke="{C["line"]}"/>')
    o.append(icon("building", 24, 84, 1.3, C["ink2"]))
    o.append(tx(64, 104, f["sp"], 14, 700))
    for k, s in enumerate(["1", "3", "6"]):
        o.append(f'<circle cx="34" cy="{134+k*24}" r="10" fill="{C["yellow"]}"/>')
        o.append(tx(34, 138 + k * 24, s, 11, 700, C["ink"], "middle"))
    labels = {"en": ["presenting", "official", "hospitality"], "zh": ["冠名伙伴", "官方伙伴", "款待伙伴"]}["zh" if f["sp"] == "赞助商" else "en"]
    for k, l in enumerate(labels): o.append(tx(52, 138 + k * 24, l, 12, 500, C["ink2"]))
    o.append(f'<path d="M190 112 H276" stroke="{C["amber"]}" stroke-width="2.4" marker-end="url(#ary)"/>'); o.append(tx(233, 104, f["rights"], 11, 700, C["ink"], "middle"))
    o.append(f'<path d="M190 168 H276" stroke="{C["amber"]}" stroke-width="2.4" marker-end="url(#ary)"/>'); o.append(tx(233, 186, f["hosp"], 11, 700, C["ink"], "middle"))
    o.append(f'<rect x="280" y="62" width="200" height="156" rx="12" fill="{C["yellowS"]}" stroke="{C["yellow"]}" stroke-width="1.8"/>')
    o.append(icon("piano", 294, 76, 1.3, C["yellowD"]))
    o.append(tx(334, 96, f["prog"], 14, 700, C["ink"]))
    o.append(tx(294, 130, f["p1"], 12, 500, C["ink2"])); o.append(tx(294, 150, f["p2"], 12, 500, C["ink2"]))
    o.append(icon("coins", 294, 164, 1.1, C["amber"])); o.append(icon("film", 330, 164, 1.1, C["amber"])); o.append(icon("seat", 366, 164, 1.1, C["amber"]))
    for k, (a, b, ic) in enumerate(f["o"]):
        y = 72 + k * 50
        o.append(f'<path d="M480 {y+20} H576" stroke="{C["muted"]}" stroke-width="1.6" marker-end="url(#ar)"/>')
        hi = k == 1
        o.append(f'<rect x="580" y="{y}" width="170" height="42" rx="10" fill="{C["blueS"] if hi else "#fff"}" stroke="{C["blue"] if hi else C["line"]}" stroke-width="{1.6 if hi else 1}"/>')
        o.append(icon(ic, 590, y + 9, 1.0, C["accent"] if hi else C["ink2"]))
        o.append(tx(622, y + 18, a, 12.5, 700, C["accent"] if hi else C["ink"]))
        o.append(tx(622, y + 34, b, 10.5, 400, C["ink2"]))
    o.append(f'<path d="M380 218 V252 H100 V214" fill="none" stroke="{C["muted"]}" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#ar)"/>')
    o.append(tx(240, 272, f["back"], 11, 500, C["ink2"], "middle"))
    o.append('</svg>')
    return "\n".join(o)

def prec_fig(t):
    y0, y1 = 1985, 2032; scale = 400 / (y1 - y0); x0 = 212
    o = ['<svg viewBox="0 0 620 250" role="img" aria-label="Timeline bars of long-running brand partnerships in classical music." xmlns="http://www.w3.org/2000/svg">']
    for yr in range(1990, 2031, 10):
        x = x0 + (yr - y0) * scale
        o.append(f'<line x1="{x:.0f}" y1="14" x2="{x:.0f}" y2="214" stroke="{C["line2"]}"/>')
        o.append(tx(x, 232, str(yr), 10.5, 400, C["muted"], "middle"))
    for i, (name, a, b) in enumerate(t["prec"]):
        y = 24 + i * 32
        o.append(tx(x0 - 8, y + 12, name, 11.5, 500, C["ink"], "end"))
        xa = x0 + (a - y0) * scale; xb = x0 + (b - y0) * scale
        o.append(f'<rect x="{xa:.0f}" y="{y}" width="{xb-xa:.0f}" height="16" rx="4" fill="{C["blue"]}"/>')
        o.append(tx(xa + 6, y + 12, str(a), 10, 700, "#fff"))
    xn = x0 + (2026 - y0) * scale
    o.append(f'<line x1="{xn:.0f}" y1="14" x2="{xn:.0f}" y2="214" stroke="{C["red"]}" stroke-dasharray="3 3"/>')
    o.append(tx(xn + 4, 24, "2026", 10, 700, C["red"]))
    o.append('</svg>')
    return "\n".join(o)

def mkt_fig(t):
    o = ['<svg viewBox="0 0 620 252" role="img" aria-label="Stacked bar of European sponsorship split between sport and non-sport, and bars for the five largest country markets." xmlns="http://www.w3.org/2000/svg">']
    total = sum(v for _, v, _ in t["mkt"]); x = 0
    for name, v, col in t["mkt"]:
        w = v / total * 600
        o.append(f'<rect x="{x:.0f}" y="16" width="{w-2:.0f}" height="34" rx="4" fill="{C[col]}"/>')
        if col == "blue": o.append(tx(x + 10, 38, f"{name} · €{v}bn · {v/total*100:.0f}%", 12, 700, "#fff"))
        else: o.append(tx(x + w - 2, 68, f"{name} · €{v}bn · {v/total*100:.0f}%", 12, 700, C["ink"], "end"))
        x += w
    for i, (name, v) in enumerate(t["mkt_countries"]):
        y = 92 + i * 30
        o.append(tx(0, y + 12, name, 12, 500, C["ink"]))
        o.append(f'<rect x="90" y="{y}" width="{v*60:.0f}" height="16" rx="4" fill="{C["blue"]}"/>')
        o.append(tx(90 + v * 60 + 8, y + 12, f"€{v}bn", 11.5, 700, C["ink"]))
    o.append('</svg>')
    return "\n".join(o)

def steps_fig(t):
    o = ['<svg viewBox="0 0 1240 130" role="img" aria-label="Four chevrons: secure, sell, deliver, renew, with owners." xmlns="http://www.w3.org/2000/svg">']
    for i, ((a, b, ic), owner) in enumerate(zip(t["steps"], t["steps_owner"])):
        x = 12 + i * 306; w = 300
        o.append(f'<path d="M{x} 10 H{x+w-22} L{x+w} 50 L{x+w-22} 90 H{x} L{x+22 if i else x} 50 Z" fill="{C["yellowS"] if i%2==0 else C["blueS"]}"/>')
        o.append(icon(ic, x + 30, 32, 1.4, C["ink2"]))
        o.append(tx(x + 72, 44, f"{i+1} · {a}", 15, 700))
        o.append(tx(x + 72, 66, b, 11.5, 400, C["ink2"]))
        o.append(tx(x + 30, 118, owner, 11, 700, C["accent"]))
    o.append('</svg>')
    return "\n".join(o)

def roles_fig(t):
    r = t["roles"]
    o = ['<svg viewBox="0 0 620 300" role="img" aria-label="Triangle of Fragrant Hill, partner and sponsor with labelled exchanges." xmlns="http://www.w3.org/2000/svg">', MK]
    nodes = [(310, 50, r["fh"], C["blue"], C["blueS"], "star"), (110, 240, r["pa"], C["green"], C["greenS"], "handshake"), (510, 240, r["sp"], C["yellowD"], C["yellowS"], "building")]
    o.append(f'<path d="M330 92 L488 206" stroke="{C["muted"]}" stroke-width="1.6" marker-end="url(#ar)"/>'); o.append(tx(430, 136, r["fh_sp"], 11, 500, C["ink2"]))
    o.append(f'<path d="M466 232 L352 98" stroke="{C["amber"]}" stroke-width="2.2" marker-end="url(#ary)"/>'); o.append(tx(606, 196, r["sp_fh"], 11, 700, C["amber"], "end"))
    o.append(f'<path d="M150 206 L280 100" stroke="{C["muted"]}" stroke-width="1.6" marker-end="url(#ar)"/>'); o.append(tx(176, 134, r["pa_fh"], 11, 500, C["ink2"], "end"))
    o.append(f'<path d="M264 96 L128 230" stroke="{C["amber"]}" stroke-width="2.2" marker-end="url(#ary)"/>'); o.append(tx(14, 196, r["fh_pa"], 11, 700, C["amber"]))
    for x, y, n, c, s, ic in nodes:
        o.append(f'<rect x="{x-84}" y="{y-26}" width="168" height="52" rx="26" fill="{s}" stroke="{c}" stroke-width="1.8"/>')
        o.append(icon(ic, x - 68, y - 12, 1.0, c))
        o.append(tx(x + 10, y + 5, n, 13, 700, c, "middle"))
    o.append('</svg>')
    return "\n".join(o)

def risk_fig(t):
    o = ['<svg viewBox="0 0 620 120" role="img" aria-label="Three risk tiles with controls." xmlns="http://www.w3.org/2000/svg">']
    for i, (a, b, ic) in enumerate(t["risks"]):
        x = 4 + i * 206
        o.append(f'<rect x="{x}" y="8" width="196" height="104" rx="12" fill="{C["redS"]}"/>')
        o.append(icon(ic, x + 14, 22, 1.3, C["red"]))
        o.append(tx(x + 52, 42, a, 12.5, 700))
        lines = wrap(b, 27)
        for k, ln in enumerate(lines[:3]): o.append(tx(x + 14, 68 + k * 16, ln, 11, 400, C["ink2"]))
    o.append('</svg>')
    return "\n".join(o)

def rep_fig(t):
    o = ['<svg viewBox="0 0 620 120" role="img" aria-label="Three tiles on why Encore repeats." xmlns="http://www.w3.org/2000/svg">']
    for i, (a, ic) in enumerate(t["rep"]):
        x = 4 + i * 206
        o.append(f'<rect x="{x}" y="8" width="196" height="104" rx="12" fill="{C["greenS"]}"/>')
        o.append(icon(ic, x + 14, 22, 1.4, C["green"]))
        words = a.split(" ")
        if len(a) > 22 and " " in a:
            mid = len(words) // 2
            o.append(tx(x + 14, 78, " ".join(words[:mid]), 12.5, 700)); o.append(tx(x + 14, 96, " ".join(words[mid:]), 12.5, 700))
        else:
            o.append(tx(x + 14, 84, a, 12.5, 700))
    o.append('</svg>')
    return "\n".join(o)

def page3(t, lang, other):
    FIGN[0] = 0
    body = head(t, t["p3_doc"], 3, other) + f'''
<div class="hero"><div><div style="font-size:11.5px;letter-spacing:.06em;color:#B06000;font-weight:700;margin-bottom:6px">{e(t["p3_eyebrow"])}</div><h1>{e(t["p3_title"])}</h1><p>{e(t["p3_lede"])}</p></div>{kpis(t["kp3"])}</div>
<div class="grid">
{fig("c7", t["fig_money"], money_fig(t), t["money_cap"])}
{fig("c5", t["fig_ladder"], ladder_fig(t), t["ladder_cap"])}
{fig("c6", t["fig_prec"], prec_fig(t), t["prec_cap"])}
{fig("c6", t["fig_mkt"], mkt_fig(t), t["mkt_cap"])}
{fig("c12", t["fig_steps"], steps_fig(t), "")}
{fig("c6", t["fig_roles"], roles_fig(t), "")}
{fig("c6", t["fig_risk"], risk_fig(t), "")}
</div><div class="foot"><span>{e(t["sources"])}</span><span>{e(t["brand"])}</span></div>'''
    return shell(t, lang, {"en": "Encore Programme", "zh": "安可计划"}[lang], body)

# ----------------------------------------------------------------- build
LINKS = {}
lp = os.path.join(ROOT, "build", "links.json")
if os.path.exists(lp): LINKS = json.load(open(lp))
for lang in ("en", "zh"):
    t = T[lang]; other = "zh" if lang == "en" else "en"
    for key, fn in (("p1-architecture", page1), ("p2-monetisation", page2), ("p3-encore", page3)):
        href = LINKS.get(f"{key}-{other}", f"{key}-{other}.html")
        out = os.path.join(ROOT, f"{key}-{lang}.html")
        open(out, "w").write(fn(t, lang, href)); print("wrote", out)
