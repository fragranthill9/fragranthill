#!/usr/bin/env python3
"""Build the three executive one-pagers in English and Chinese from one content model.
Output: framework/p1-architecture-{en,zh}.html, p2-monetisation-{en,zh}.html, p3-encore-{en,zh}.html
"""
import html as H, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# Google palette, light only
CSS = """
:root{
  --bg:#FFFFFF; --surface:#F8F9FA; --ink:#202124; --ink-2:#3C4043; --muted:#5F6368; --line:#DADCE0; --line-2:#E8EAED;
  --accent:#1A73E8;
  --p1:#EA4335; --p2:#4285F4; --p3:#34A853; --p4:#FBBC04; --p5:#A142F4;
  --p1-soft:#FCE8E6; --p2-soft:#E8F0FE; --p3-soft:#E6F4EA; --p4-soft:#FEF7E0; --p5-soft:#F3E8FD;
  --p4-ink:#202124;
  --font:"Roboto","Noto Sans SC","PingFang SC","Microsoft YaHei",system-ui,sans-serif;
  color-scheme:light;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font);font-size:14px;line-height:1.45;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 40px}
.sheet{max-width:1240px;margin:0 auto}
header{display:flex;flex-wrap:wrap;gap:10px 24px;align-items:center;justify-content:space-between;padding:18px 0 12px;border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:12px}
.seal{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;font-weight:700;font-size:13px;color:#fff;background:linear-gradient(135deg,var(--p2) 0 25%,var(--p1) 25% 50%,var(--p4) 50% 75%,var(--p3) 75% 100%)}
.brand b{font-weight:700;font-size:14px;letter-spacing:.04em;display:block}
.brand span{color:var(--muted);font-size:12px}
.docline{display:flex;align-items:center;gap:14px;font-size:12px;color:var(--muted)}
.docline b{color:var(--ink);display:block;font-size:13px}
.pages{display:flex;gap:6px}
.pages span{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;font-size:12px;font-weight:700;border:1px solid var(--line);color:var(--muted)}
.pages span.on{background:var(--accent);border-color:var(--accent);color:#fff}
.lang{font-size:12px;font-weight:500;color:var(--accent);text-decoration:none;border:1px solid var(--line);border-radius:16px;padding:4px 12px}
.grid{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:14px;margin-top:14px}
.c12{grid-column:span 12}.c8{grid-column:span 8}.c7{grid-column:span 7}.c6{grid-column:span 6}.c5{grid-column:span 5}.c4{grid-column:span 4}.c3{grid-column:span 3}
.blk{background:var(--bg);border:1px solid var(--line);border-radius:12px;padding:16px 18px;min-width:0}
.blk h2{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:0 0 10px;font-weight:700}
.title{grid-column:span 8;padding:6px 0 0}
.title h1{font-size:clamp(26px,3.4vw,38px);font-weight:700;line-height:1.1;letter-spacing:-.01em;margin:0 0 8px;text-wrap:balance}
.title p{margin:0;color:var(--ink-2);font-size:15px;max-width:64ch}
.facts{grid-column:span 4;display:grid;gap:8px;align-content:start}
.fact{background:var(--surface);border-radius:10px;padding:10px 14px;display:grid;grid-template-columns:auto 1fr;gap:12px;align-items:center}
.fact .n{font-size:24px;font-weight:700;font-variant-numeric:tabular-nums;white-space:nowrap;color:var(--accent);min-width:70px}
.fact .l{font-size:12px;color:var(--ink-2);line-height:1.3}
.fact .l i{display:block;font-style:normal;color:var(--muted);font-size:10.5px;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
.pc{border-radius:10px;border:1px solid var(--line);overflow:hidden;background:var(--bg);display:flex;flex-direction:column}
.pc .hd{padding:10px 12px;color:#fff;font-weight:700;font-size:14px;line-height:1.2}
.pc .hd small{display:block;font-weight:500;font-size:11px;opacity:.9;margin-top:2px}
.pc .bd{padding:10px 12px;font-size:12.5px;color:var(--ink-2);display:grid;gap:8px;flex:1}
.pc .k{font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:2px;font-weight:700}
.pc ul{margin:0;padding-left:16px}
.pc li{margin:1px 0}
.pc .chip{align-self:start;margin-top:auto}
.chip{display:inline-block;padding:2px 9px;border-radius:12px;font-size:10.5px;font-weight:700;letter-spacing:.03em}
.ups{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;text-align:center;color:var(--muted);font-size:16px;line-height:1;margin:6px 0}
.band{border-radius:10px;padding:12px 14px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.band.core{background:var(--p2-soft);border:1px solid #AECBFA}
.band.inputs{background:var(--surface);border:1px solid var(--line)}
.band .lbl{grid-column:1/-1;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:var(--accent);margin-bottom:-4px}
.band.inputs .lbl{color:var(--muted)}
.band b{display:block;font-size:13px;margin-bottom:2px}
.band p{margin:0;font-size:12px;color:var(--ink-2)}
figure{margin:0;overflow-x:auto}
figure svg{display:block;width:100%;height:auto}
figcaption{font-size:11.5px;color:var(--muted);margin-top:8px}
.list{display:grid;gap:10px}
.list div{display:grid;grid-template-columns:auto 1fr;gap:10px;align-items:start;font-size:13px;color:var(--ink-2)}
.list b{color:var(--ink)}
.num{width:24px;height:24px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-size:12px;font-weight:700;flex:none}
.phases{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.ph{border-radius:10px;padding:12px 14px;border:1px solid var(--line)}
.ph b{display:block;font-size:11px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px}
.ph .who{font-size:14px;font-weight:700;color:var(--ink);margin-bottom:4px}
.ph p{margin:0;font-size:12.5px;color:var(--ink-2)}
.ph .gate{margin-top:8px;padding-top:8px;border-top:1px dashed var(--line);font-size:11.5px;color:var(--ink-2)}
.ph .gate b{display:inline;font-size:10px;color:var(--muted);margin-right:4px}
.dot{display:inline-block;width:9px;height:9px;border-radius:50%;margin-right:5px;vertical-align:0}
table{width:100%;border-collapse:collapse;font-size:12.5px}
th{text-align:left;font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:700;padding:6px 8px;border-bottom:2px solid var(--line)}
td{padding:8px;border-bottom:1px solid var(--line-2);vertical-align:top;color:var(--ink-2)}
td:first-child{color:var(--ink);font-weight:700}
.mx th{text-align:center}.mx th:first-child{text-align:left}.mx td{text-align:center}.mx td:first-child{text-align:left;white-space:nowrap}
.d{display:inline-block;width:14px;height:14px;border-radius:50%}
.d.h{opacity:.3}
.streams{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.st{border-radius:10px;border:1px solid var(--line);padding:12px 14px;background:var(--surface)}
.st b{display:block;font-size:14px;margin-bottom:4px}
.st p{margin:0 0 6px;font-size:12.5px;color:var(--ink-2)}
.st .meta{display:flex;justify-content:space-between;align-items:center;gap:8px;flex-wrap:wrap}
.money{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
.mc{border-radius:10px;border-top:4px solid var(--line);background:var(--surface);padding:10px 12px;font-size:12.5px;color:var(--ink-2)}
.mc b{display:block;font-size:13px;color:var(--ink);margin-bottom:4px}
.mc i{display:block;font-style:normal;font-size:11.5px;color:var(--muted);margin-top:6px;padding-top:6px;border-top:1px dashed var(--line)}
.cols3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.cols4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.cell{border-radius:10px;background:var(--surface);padding:12px 14px;font-size:12.5px;color:var(--ink-2)}
.cell b{display:block;font-size:13px;color:var(--ink);margin-bottom:4px}
.cell ul{margin:0;padding-left:16px}
.offer{grid-column:span 4;background:var(--p4-soft);border:1px solid #FDE293;border-radius:12px;padding:14px 16px}
.offer h2{color:var(--ink);font-size:12px;letter-spacing:.08em;text-transform:uppercase;margin:0 0 8px;font-weight:700}
.offer dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:6px 12px;font-size:12.5px}
.offer dt{color:var(--muted);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;padding-top:2px;font-weight:700}
.offer dd{margin:0;color:var(--ink)}
.tier{border-radius:10px;border:1px solid var(--line);padding:12px 14px;background:var(--bg)}
.tier b{display:block;font-size:14px}
.tier small{display:block;color:var(--muted);font-size:11px;margin-bottom:6px}
.tier ul{margin:0;padding-left:16px;font-size:12.5px;color:var(--ink-2)}
.risk{border-left:4px solid var(--p1);padding:4px 12px;font-size:12.5px;color:var(--ink-2);background:var(--surface);border-radius:0 8px 8px 0}
.risk b{color:var(--ink)}
.foot{margin-top:14px;font-size:11.5px;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px 20px;justify-content:space-between}
@media (max-width:1000px){.pillars,.money{grid-template-columns:repeat(2,minmax(0,1fr))}.streams{grid-template-columns:repeat(3,minmax(0,1fr)) !important}.ups{display:none}.band{grid-template-columns:1fr 1fr}}
@media (max-width:860px){.c8,.c7,.c6,.c5,.c4,.c3,.title,.facts,.offer{grid-column:span 12}.phases,.cols3,.cols4{grid-template-columns:1fr}.streams{grid-template-columns:1fr 1fr !important}.pillars,.money,.band{grid-template-columns:1fr}}
"""

FONT_LINK = {
    "en": '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap">',
    "zh": '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Noto+Sans+SC:wght@400;500;700&display=swap">',
}

PCOL = ["p1", "p2", "p3", "p4", "p5"]
HDTXT = {"p1": "#fff", "p2": "#fff", "p3": "#fff", "p4": "var(--p4-ink)", "p5": "#fff"}

# ---------------------------------------------------------------- content
T = {}
T["en"] = dict(
  brand="Fragrant Hill Studio", sub="Editorial house · Stockholm · Europe ↔ China",
  lang_other="中文版", conf="Confidential · prepared for partner and investor discussion",
  sources="Sources: framework/research/ · figures are reported unless marked as estimates",
  pnames=["Editorial", "Advisory", "Community", "Live & Venues", "Acceleration"],
  pshort=["Editorial", "Advisory", "Community", "Live", "Acceleration"],
  psub=["the voice", "paid answers", "the vetted room", "the stage · Encore", "the pipeline"],
  pwhat=["Stories of the people building machines, Europe ↔ China",
         "Partner data plus an operator's judgement",
         "Executives and founders on both sides, two tiers",
         "Celebrity concerts and executive salons sold to brands",
         "Founders landing in the Nordics; investors finding them"],
  pprod=[["Bilingual newsletter", "Video interview series", "LinkedIn · 公众号 · 视频号"],
         ["Market-entry advisory EU ↔ CN", "Co-branded industry reports", "Expert calls and workshops"],
         ["Base membership", "Executive club", "Courses and study trips"],
         ["Encore tour sponsorship", "Executive salons", "Sponsor dinners and hospitality"],
         ["Soft-landing programme", "Scouting for investors", "Pilot matching with corporates"]],
  pbuyer=["Season sponsors, platforms, licensees",
          "Robotics and sensor firms entering Europe; European OEMs reading China",
          "Members; course and trip participants; salon sponsors",
          "Automotive, robotics, semiconductor and consumer-tech brands",
          "Founders, accelerators, investors, corporates"],
  pwhen=["Pays later", "Cash now", "Recurring", "Cash now", "Equity"],
  k_what="What", k_products="Products", k_buyer="Who pays",
  core_lbl="Shared core · every pillar runs on it",
  core=[("Editorial voice", "One theme, one tone, one host."),
        ("Relationship graph", "One CRM: guests, sponsors, members, founders, investors."),
        ("Production line", "Record once; publish in six channels, two languages."),
        ("Commercial desk + back office", "One rate card; invoicing in Stockholm and China.")],
  inputs_lbl="Inputs already held",
  inputs=[("Founder domain depth", "Sensing, robotics, automotive, dealer networks"),
          ("Stage and talent access", "Celebrity concert channel; pianist interview done"),
          ("Partner assets", "Data, reports, founder community, investors"),
          ("Two-market base", "Swedish company; operating partner in China")],
  p1_title="One core. Five pillars. One network.",
  p1_lede="Fragrant Hill is one operating system, not five businesses. Five product pillars share one editorial voice, one contact base and one production line. Each sells a different thing to a different buyer, and each feeds the next.",
  p1_doc="Page 1 of 3 · System architecture",
  sys_h="The system",
  fly_h="How the pillars feed each other",
  fly_lbl=["content", "audience", "clients", "deal flow", "sponsors, founders"],
  fly_center="ONE NETWORK",
  fly_cap="Start at Live. Each concert yields content and a guest list; the loop closes when sponsors and founders become the next stage.",
  why_h="Why one system",
  why=[("One network", "A concert sponsor is a future advisory client, an interview guest and a club member. One contact base makes that visible."),
       ("One production line", "A recording feeds the newsletter, two video channels and the Chinese channels. Cost per piece falls to near zero."),
       ("One voice", "A single theme makes the house known for something. Random content built no audience in six months; focus will.")],
  seq_h="Activation sequence · gated by conditions, not dates",
  phases=[("Phase A · Cash", "Live + Advisory", "Sells access and judgement. Needs no audience.", "Stage rights and sponsor categories confirmed; partner introductions in hand"),
          ("Phase B · Recurring", "Editorial season + Community", "One theme, one rhythm, then two membership tiers.", "A closed sponsorship funds the season; one full season published before membership is sold"),
          ("Phase C · Equity", "Acceleration", "Deal flow matched to Nordic corporates and investors.", "A vetted club and paying advisory clients exist")],
  gate="Gate",
  # page 2
  p2_doc="Page 2 of 3 · Monetisation",
  p2_title="Six revenue streams across five pillars. No single buyer.",
  p2_lede="Free editorial earns trust; the money sits in high-ticket products next to it. The best media businesses earn most from sponsored rooms, data and advisory, not from subscriptions or ads.",
  facts2=[("€34.5bn", "European sponsorship market 2025; arts and culture 28% of it", "ESA / Nielsen Sports 2026"),
          ("50–60%", "of Semafor revenue is event sponsorship; profitable in 2025", "Semafor, Nieman Lab"),
          ("<5%", "of SemiAnalysis revenue is subscriptions; research and advisory carry the rest", "The Information, estimate"),
          ("90%", "of a leading Chinese business pundit's year-end show revenue is sponsorship", "36Kr on 吴晓波年终秀")],
  streams_h="The six revenue streams",
  streams=[("Sponsorship", "Brands pay to stand beside a tour, a season or a salon", [3, 0, 2], "Cash now"),
           ("Service fees", "Clients pay retainers, project fees and programme fees", [1, 4], "Cash now"),
           ("Membership", "Members pay annual dues: base tier and executive club", [2], "Recurring"),
           ("Tickets & hospitality", "Sponsors' guests, salon attendees, trip participants", [3, 2], "Cash now"),
           ("Licences & reports", "Report buyers, platforms and media licensees", [1, 0], "Recurring"),
           ("Equity & carry", "Programme fees, scout fees, carry through the partner fund", [4], "Equity")],
  k_pillars="Pillars", k_when="Pays",
  mx_h="Pillar × revenue stream",
  mx_cols=["Sponsorship", "Service fees", "Membership", "Tickets & hospitality", "Licences & reports", "Equity & carry"],
  mx_cap="Solid: primary stream. Faded: secondary. Every pillar has at least two streams; no stream depends on one pillar.",
  money_h="How each pillar makes money",
  money=[("Season sponsorship", "One presenting sponsor per season, every free distribution window. Licensing of episodes to platforms.", "Benchmark: The Circuit runs one presenting sponsor per season."),
         ("Retainers and reports", "Retainers and projects priced on outcome; co-branded reports licensed per seat.", "Benchmark: SemiAnalysis earns over 95% from research and consulting."),
         ("Two membership tiers", "An expensable base tier; a vetted club priced on access. Courses and trips sold per seat.", "Benchmark: vetted founder clubs sustain four- to five-figure annual dues."),
         ("Sponsorship packages", "Sold on hospitality first, association second, content third, reach last. Deposit on signature.", "Benchmark: Semafor earns 50–60% of revenue from sponsored convenings."),
         ("Fees and carry", "Programme fee per company, scout fee per round, carry through the partner's fund.", "Benchmark: a16z and YC run media as a deal-flow funnel.")],
  when_h="When each stream pays",
  when_cols=[("Cash now", [3, 1], "Sponsorship, hospitality, service fees. Sold on access and judgement before an audience exists."),
             ("Recurring", [0, 2], "Membership, season sponsorship, report licences. Built on a published season and a vetted room."),
             ("Equity", [4], "Programme fees and carry. A by-product of the first four pillars.")],
  work_h="Who does the work · bird's-eye view",
  work=[("Human", "Founder and core team own the theme, the relationships and the price."),
        ("Digital agents", "Research, production, publishing, follow-up and finance run on agents built with the house skills."),
        ("Partner", "Data, founder cohorts, sponsor introductions and invoicing in China.")],
  # page 3
  p3_doc="Page 3 of 3 · The project · Encore",
  p3_eyebrow="Encore · sponsorship programme for a world-class pianist's European tour",
  p3_title="Sell the room, not the reach.",
  p3_lede="Encore packages a celebrity concert tour as a sponsorship, hospitality and content property for automotive, robotics and technology brands moving between Europe and China. Fragrant Hill holds the stage and the artist relationship. The partner holds the doors.",
  offer_h="The offer in one block",
  offer=[("Property", "A European tour leg by a pianist who sells out the largest halls; Nordic cities plus one of Hamburg, Paris, London"),
         ("Buyers", "Brands launching or scaling in Europe: EV and premium automotive, robotics, semiconductors, consumer tech"),
         ("Structure", "1 presenting partner · 3 category-exclusive official partners · up to 6 hospitality partners"),
         ("Payment", "Deposit on signature, balance before the first show"),
         ("Our revenue", "Agency commission on rights fees (industry average 20%) plus production and hospitality fees"),
         ("Repeats as", "Annual tour · executive salons on the same stages · sponsor dinners")],
  prop_h="The property · reported",
  prop=[("5,000", "Royal Albert Hall tickets sold in 48 hours for one recital", "Classic FM, 2013"),
        ("16–20M", "social followers claimed across platforms", "Slipped Disc 2025; claimed, not verified per platform"),
        ("13", "European cities on the autumn 2026 run; 2027 dates listed in London, Hamburg, Bonn", "Deutsche Grammophon tour page; listings"),
        ("0", "whole-tour presenting partners ever announced for this artist", "Research notes 3")],
  mkt_h="The market · reported",
  mkt=[("€34.5bn", "European sponsorship spend 2025, up 4.7%", "ESA / Nielsen Sports 2026"),
       ("€9.7bn", "of it is non-sport: arts, culture, entertainment (28%)", "ESA / Nielsen Sports 2026"),
       ("62%", "of brands want to sponsor culture; 61% do not yet", "ESA arts and culture survey"),
       ("0", "Chinese EV, robotics or consumer-tech brands found sponsoring classical music in Europe", "Finding of absence, research notes 3")],
  flow_h="How the money flows",
  flow=dict(sponsors="SPONSORS", s1="1 presenting partner", s2="3 official partners", s3="up to 6 hospitality partners",
            rights="rights fees", hosp="hospitality fees", prog="ENCORE PROGRAMME", pr1="contracts · category exclusivity", pr2="deposit on signature",
            out1="Tour producer", o1="artist · venues · production", out2="Fragrant Hill", o2="commission · production fees", out3="Partner", o3="share on introduced sponsors",
            back="value back: hospitality · association · content · reach"),
  flow_cap="Hospitality is what B2B sponsors measure: dealer and client evenings in a concert hall. Reach is the last argument, not the first.",
  tiers_h="Package tiers",
  tiers=[("Presenting partner", "one · \"presented by\"", ["Naming across the tour; category exclusivity", "VIP tables per city; private recital for clients", "12-month content rights; first refusal on the next edition"]),
         ("Official partner", "three · one per category", ["Category exclusivity: automotive · robotics and tech · finance or luxury", "Programme and screen branding; VIP table per city", "Shared content pack"]),
         ("Hospitality partner", "up to six", ["Premium seat blocks in two cities", "Lounge access and branding; photo and social assets"])],
  tiers_cap="Fees are set per market against the precedents below and confirmed in the first pitches.",
  prec_h="Precedents · automotive and tech in classical music",
  prec_cols=["Brand", "Property", "Since"],
  prec=[("Audi", "Salzburg Festival main sponsor, extended to 2027", "1995"),
        ("Porsche", "Gewandhaus Leipzig, incl. international tours", "2011"),
        ("BMW", "Opera for All, Munich and Berlin, to 2030", "1997"),
        ("Volvo", "Gothenburg Symphony principal sponsor", "long-running"),
        ("VW Group", "Artist cultural ambassador; presented a China tour", "2012"),
        ("Siemens", "Bayreuth Festival, about $1.4M a year", "to 2011")],
  prec_cap="Fees undisclosed except Siemens. A thirty-year playbook for European brands, unused by Chinese brands in Europe.",
  steps_h="How it proceeds",
  steps=[("Secure", "Rights, dates, venues and open sponsor categories confirmed in writing", "Fragrant Hill"),
         ("Sell", "Three tiers, warm introductions, term sheets, contracts with deposits", "Fragrant Hill + partner"),
         ("Deliver", "Production, hospitality, client evenings, tour film and content", "Fragrant Hill + contractors"),
         ("Renew", "First refusal on the next edition; salon series on the same stages", "Fragrant Hill")],
  roles_h="Who does what",
  roles=[("Fragrant Hill", ["Artist and venue relationship, rights", "Packages, pitch, contracts, collections", "Production, hospitality, content"]),
         ("Partner", ["Warm introductions in automotive, robotics, tech", "Sponsor-side champion", "Invoicing in China where needed"]),
         ("Sponsor", ["Rights and hospitality fees; activation budget", "Guest lists: dealers, clients, officials, press", "Brand assets and approvals"])],
  risks_h="Risks and controls",
  risks=[("Category conflict.", "The artist has had automotive partners. Open categories are confirmed in writing before any brand is pitched; if automotive is closed, the presenting tier goes to robotics and consumer tech."),
         ("Sales cycle.", "Six-figure sponsorships normally take 9–18 months. We pitch only through warm introductions and start from a base of three signatures."),
         ("Artist, venue, payment.", "Cancellation insurance; venues on option; non-refundable deposits; exclusivity written in so one exit does not unwind the others.")],
  rep_h="Why it repeats",
  rep=[("Annual tour edition", "Same package ladder; sponsors get first refusal. The roster can widen to other performers we can host."),
       ("Executive salons", "Salons on the same stages, two to three sponsors each. Feeds the Community pillar."),
       ("Content and network", "Every concert yields a tour film, interview material and a guest list that the other pillars reuse.")],
)

T["zh"] = dict(
  brand="香山工作室", sub="编辑内容机构 · 斯德哥尔摩 · 欧洲 ↔ 中国",
  lang_other="English", conf="保密 · 供合作伙伴与投资人讨论",
  sources="资料来源：framework/research/ · 除标注估算外，数字均为公开报道",
  pnames=["内容", "咨询", "社群", "现场与场馆", "加速"],
  pshort=["内容", "咨询", "社群", "现场", "加速"],
  psub=["声音", "付费答案", "筛选过的圈子", "舞台 · 安可 Encore", "项目通道"],
  pwhat=["讲述欧洲与中国之间「造机器的人」的故事",
         "伙伴数据 + 实业操盘者的判断",
         "两地的高管与创始人，两档会员",
         "向品牌销售的名人音乐会与高管沙龙",
         "创始人落地北欧，投资人找到他们"],
  pprod=[["双语通讯", "视频访谈系列", "LinkedIn · 公众号 · 视频号"],
         ["欧中市场进入咨询", "联名行业报告", "专家访谈与工作坊"],
         ["基础会员", "高管俱乐部", "课程与考察团"],
         ["安可巡演赞助", "高管沙龙", "赞助商晚宴与款待"],
         ["软着陆计划", "为投资人寻源", "与企业对接试点"]],
  pbuyer=["内容季赞助商、平台、授权方",
          "进入欧洲的机器人与传感器企业；研究中国的欧洲整车厂",
          "会员；课程与考察参与者；沙龙赞助商",
          "汽车、机器人、半导体与消费科技品牌",
          "创始人、加速器、投资人、企业"],
  pwhen=["稍后变现", "即时现金", "持续收入", "即时现金", "股权"],
  k_what="是什么", k_products="产品", k_buyer="谁付费",
  core_lbl="共享核心 · 每个支柱都运行在其上",
  core=[("内容之声", "一个主题、一种语调、一位主持人。"),
        ("关系图谱", "一个 CRM：嘉宾、赞助商、会员、创始人、投资人。"),
        ("生产线", "一次录制；六个渠道、两种语言发布。"),
        ("商务与后台", "一张价目表；在斯德哥尔摩与中国开票。")],
  inputs_lbl="已经持有的资源",
  inputs=[("创始人行业深度", "传感、机器人、汽车、经销商网络"),
          ("舞台与艺人资源", "名人音乐会渠道；已完成钢琴家专访"),
          ("伙伴资产", "数据、报告、创始人社群、投资人"),
          ("双市场基础", "瑞典公司；中国运营伙伴")],
  p1_title="一个核心，五大支柱，同一张关系网。",
  p1_lede="香山是一个运营系统，而不是五家公司。五个产品支柱共用同一个内容之声、同一个联系人库和同一条生产线。每个支柱卖给不同的买家，并为下一个支柱输送资源。",
  p1_doc="第 1 页 / 共 3 页 · 系统架构",
  sys_h="系统全貌",
  fly_h="支柱之间如何互相输送",
  fly_lbl=["内容", "受众", "客户", "项目源", "赞助商与创始人"],
  fly_center="同一张网",
  fly_cap="从「现场」开始。每场音乐会产生内容和嘉宾名单；当赞助商与创始人成为下一个舞台，循环闭合。",
  why_h="为什么是一个系统",
  why=[("同一张关系网", "一位音乐会赞助商就是未来的咨询客户、访谈嘉宾和俱乐部会员。一个联系人库让这一点可见。"),
       ("同一条生产线", "一次录制供给通讯、两个视频频道和中文渠道。单条内容成本趋近于零。"),
       ("同一个声音", "一个主题让机构「以某事闻名」。六个月的随机内容没有建立受众；聚焦可以。")],
  seq_h="启动顺序 · 按条件推进，不按日期",
  phases=[("阶段 A · 现金", "现场 + 咨询", "卖的是接触权与判断力，不需要受众基础。", "舞台权益与赞助品类书面确认；伙伴引荐到位"),
          ("阶段 B · 持续收入", "内容季 + 社群", "一个主题、一个节奏，然后是两档会员。", "一笔已签赞助支撑内容季；发布完整一季后再销售会员"),
          ("阶段 C · 股权", "加速", "项目源对接北欧企业与投资人。", "已有筛选过的俱乐部与付费咨询客户")],
  gate="前提",
  p2_doc="第 2 页 / 共 3 页 · 变现方式",
  p2_title="五大支柱、六类收入，不依赖单一买家。",
  p2_lede="免费内容赢得信任，钱在旁边的高客单产品里。最成功的媒体企业主要靠赞助的现场、数据和咨询赚钱，而不是订阅或广告。",
  facts2=[("€345亿", "2025 年欧洲赞助市场规模；艺术文化占 28%", "ESA / Nielsen Sports 2026"),
          ("50–60%", "Semafor 收入来自活动赞助；2025 年实现盈利", "Semafor, Nieman Lab"),
          ("<5%", "SemiAnalysis 收入来自订阅；研究与咨询贡献其余", "The Information，估算"),
          ("90%", "吴晓波年终秀收入来自赞助", "36氪")],
  streams_h="六类收入",
  streams=[("赞助", "品牌为与巡演、内容季或沙龙并列而付费", [3, 0, 2], "即时现金"),
           ("服务费", "客户支付顾问费、项目费与计划费用", [1, 4], "即时现金"),
           ("会员费", "会员支付年费：基础档与高管俱乐部", [2], "持续收入"),
           ("票务与款待", "赞助商嘉宾、沙龙参与者、考察团成员", [3, 2], "即时现金"),
           ("授权与报告", "报告买家、平台与媒体授权方", [1, 0], "持续收入"),
           ("股权与收益分成", "计划费用、寻源费、通过伙伴基金的收益分成", [4], "股权")],
  k_pillars="支柱", k_when="回款",
  mx_h="支柱 × 收入类型",
  mx_cols=["赞助", "服务费", "会员费", "票务与款待", "授权与报告", "股权与分成"],
  mx_cap="实心：主要收入。浅色：次要收入。每个支柱至少两类收入；没有一类收入依赖单一支柱。",
  money_h="每个支柱如何赚钱",
  money=[("内容季赞助", "每季一家冠名赞助商，覆盖所有免费分发渠道；节目授权给平台。", "参照：The Circuit 每季只有一家冠名赞助商。"),
         ("顾问费与报告", "按成果定价的顾问费与项目费；联名报告按席位授权。", "参照：SemiAnalysis 超过 95% 收入来自研究与咨询。"),
         ("两档会员", "可报销的基础档；按接触权定价的筛选制俱乐部。课程与考察按席位销售。", "参照：筛选制创始人俱乐部的年费可达四到五位数美元。"),
         ("赞助套餐", "先卖款待，再卖品牌联结，再卖内容，最后才是流量。签约付定金。", "参照：Semafor 50–60% 收入来自赞助的闭门会。"),
         ("费用与收益分成", "按公司收取计划费、按轮次收取寻源费、通过伙伴基金获得收益分成。", "参照：a16z 与 YC 把媒体当作项目源漏斗。")],
  when_h="各类收入何时到账",
  when_cols=[("即时现金", [3, 1], "赞助、款待、服务费。在受众形成之前，凭接触权与判断力即可销售。"),
             ("持续收入", [0, 2], "会员费、内容季赞助、报告授权。建立在已发布的内容季和筛选过的圈子之上。"),
             ("股权", [4], "计划费用与收益分成。前四个支柱的副产品。")],
  work_h="谁来做 · 鸟瞰",
  work=[("人", "创始人与核心团队掌握主题、关系和定价。"),
        ("数字代理", "研究、制作、发布、跟进与财务由基于内部技能构建的 AI 代理运行。"),
        ("伙伴", "数据、创始人营、赞助商引荐，以及在中国开票。")],
  p3_doc="第 3 页 / 共 3 页 · 项目 · 安可 Encore",
  p3_eyebrow="安可 Encore · 世界级钢琴家欧洲巡演赞助计划",
  p3_title="卖的是现场，不是流量。",
  p3_lede="安可把一场名人音乐会巡演打包成赞助、款待与内容资产，面向在欧洲与中国之间布局的汽车、机器人和科技品牌。香山掌握舞台与艺术家关系，伙伴掌握进入品牌的大门。",
  offer_h="一图看懂方案",
  offer=[("标的", "一位能售罄顶级音乐厅的钢琴家的欧洲巡演；北欧城市加汉堡、巴黎或伦敦之一"),
         ("买家", "正在进入或扩张欧洲的品牌：电动车与高端汽车、机器人、半导体、消费科技"),
         ("结构", "1 家冠名伙伴 · 3 家品类独家官方伙伴 · 最多 6 家款待伙伴"),
         ("付款", "签约付定金，首场前付尾款"),
         ("我们的收入", "权益费的代理佣金（行业平均 20%）加制作与款待服务费"),
         ("可复制为", "年度巡演 · 同一舞台上的高管沙龙 · 赞助商晚宴")],
  prop_h="标的 · 公开报道",
  prop=[("5,000", "皇家阿尔伯特音乐厅一场独奏会 48 小时售出的票数", "Classic FM, 2013"),
        ("1,600–2,000万", "各平台宣称的社交媒体粉丝总数", "Slipped Disc 2025；宣称数，未逐平台核实"),
        ("13", "2026 年秋季巡演覆盖的欧洲城市数；2027 年已排定伦敦、汉堡、波恩", "Deutsche Grammophon 巡演页；票务信息"),
        ("0", "该艺术家历史上公布过的整巡演冠名伙伴数量", "研究笔记 3")],
  mkt_h="市场 · 公开报道",
  mkt=[("€345亿", "2025 年欧洲赞助支出，同比增长 4.7%", "ESA / Nielsen Sports 2026"),
       ("€97亿", "其中非体育类：艺术、文化、娱乐（28%）", "ESA / Nielsen Sports 2026"),
       ("62%", "的品牌希望赞助文化；61% 尚未开始", "ESA 艺术文化调研"),
       ("0", "在欧洲赞助古典音乐的中国电动车、机器人或消费科技品牌", "研究笔记 3，未发现案例")],
  flow_h="资金如何流动",
  flow=dict(sponsors="赞助商", s1="1 家冠名伙伴", s2="3 家官方伙伴", s3="最多 6 家款待伙伴",
            rights="权益费", hosp="款待费", prog="安可计划", pr1="合同 · 品类独家", pr2="签约付定金",
            out1="巡演制作方", o1="艺术家 · 场馆 · 制作", out2="香山", o2="佣金 · 制作服务费", out3="伙伴", o3="引荐赞助商的分成",
            back="回馈赞助商：款待 · 品牌联结 · 内容 · 触达"),
  flow_cap="B2B 赞助商衡量的是款待：在音乐厅里的经销商与客户之夜。流量是最后一个理由，不是第一个。",
  tiers_h="赞助套餐",
  tiers=[("冠名伙伴", "1 家 · 「呈现」", ["整个巡演冠名；品类独家", "每城 VIP 桌；为客户举办私人独奏会", "12 个月内容权益；下一届优先续约权"]),
         ("官方伙伴", "3 家 · 每品类一家", ["品类独家：汽车 · 机器人与科技 · 金融或奢侈品", "节目册与屏幕品牌露出；每城一桌 VIP", "共享内容包"]),
         ("款待伙伴", "最多 6 家", ["两个城市的高级座位区", "贵宾休息室使用与品牌露出；照片与社交素材"])],
  tiers_cap="费用按市场参照下方先例设定，并在首轮提案中确认。",
  prec_h="先例 · 古典音乐中的汽车与科技品牌",
  prec_cols=["品牌", "项目", "起始"],
  prec=[("奥迪", "萨尔茨堡音乐节主赞助商，续约至 2027", "1995"),
        ("保时捷", "莱比锡布商大厦管弦乐团，含国际巡演", "2011"),
        ("宝马", "「人人歌剧」慕尼黑与柏林，续约至 2030", "1997"),
        ("沃尔沃", "哥德堡交响乐团首席赞助商", "长期"),
        ("大众集团", "艺术家文化大使；冠名中国巡演", "2012"),
        ("西门子", "拜罗伊特音乐节，约每年 140 万美元", "至 2011")],
  prec_cap="除西门子外费用均未披露。欧洲品牌已用了三十年的打法，中国品牌在欧洲尚未使用。",
  steps_h="推进步骤",
  steps=[("锁定", "书面确认权益、日期、场馆与开放的赞助品类", "香山"),
         ("销售", "三档套餐、伙伴引荐、条款书、含定金的合同", "香山 + 伙伴"),
         ("交付", "制作、款待、客户之夜、巡演影片与内容", "香山 + 外部团队"),
         ("续约", "下一届优先续约权；同一舞台上的沙龙系列", "香山")],
  roles_h="各方分工",
  roles=[("香山", ["艺术家与场馆关系、权益", "套餐、提案、合同、回款", "制作、款待、内容"]),
         ("伙伴", ["汽车、机器人、科技领域的引荐", "赞助商内部支持者", "需要时在中国开票"]),
         ("赞助商", ["权益费与款待费；激活预算", "嘉宾名单：经销商、客户、官员、媒体", "品牌素材与审批"])],
  risks_h="风险与对策",
  risks=[("品类冲突。", "该艺术家曾有汽车品牌合作。向任何品牌提案前先书面确认开放品类；若汽车品类已关闭，冠名档位转向机器人与消费科技。"),
         ("销售周期。", "六位数赞助通常需要 9–18 个月。我们只通过引荐提案，并以三份签约为基础方案。"),
         ("艺术家、场馆、付款。", "取消保险；场馆预留；定金不可退；合同写入独家条款，一家退出不影响其他。")],
  rep_h="为什么可以复制",
  rep=[("年度巡演", "同样的套餐阶梯；赞助商享有优先续约权。艺人阵容可扩展到我们能接洽的其他表演者。"),
       ("高管沙龙", "同一舞台上的沙龙，每场两到三家赞助商。为社群支柱输送。"),
       ("内容与关系网", "每场音乐会产生巡演影片、访谈素材和嘉宾名单，供其他支柱复用。")],
)

# ---------------------------------------------------------------- helpers
def e(s): return H.escape(str(s))

def head(t, lang, doc, page, other_href):
    pg = "".join(f'<span class="{"on" if i == page else ""}">{i}</span>' for i in (1, 2, 3))
    return f'''<header>
  <div class="brand"><div class="seal">香山</div><div><b>{e(t["brand"])}</b><span>{e(t["sub"])}</span></div></div>
  <div class="docline"><div><b>{e(doc)}</b>{e(t["conf"])}</div><div class="pages">{pg}</div><a class="lang" href="{other_href}">{e(t["lang_other"])} →</a></div>
</header>'''

def dots(idx):
    return "".join(f'<span class="dot" style="background:var(--{PCOL[i]})"></span>' for i in idx)

def chip(when, i):
    c = PCOL[i]
    tx = "var(--p4-ink)" if c == "p4" else f"var(--{c})"
    return f'<span class="chip" style="background:var(--{c}-soft);color:{tx}">{e(when)}</span>'

def facts_html(items):
    return "".join(f'<div class="fact"><div class="n">{e(n)}</div><div class="l">{e(l)}<i>{e(s)}</i></div></div>' for n, l, s in items)

def pentagon(t):
    L = t["fly_lbl"]
    names = [f'4 · {t["pshort"][3]}', f'1 · {t["pshort"][0]}', f'3 · {t["pshort"][2]}', f'2 · {t["pshort"][1]}', f'5 · {t["pshort"][4]}']
    cols = ["p4", "p1", "p3", "p2", "p5"]
    # positions: top, right-top, right-bottom, left-bottom, left-top
    pos = [(310, 52), (466, 166), (406, 346), (214, 346), (154, 166)]
    o = ['<svg viewBox="0 0 620 410" role="img" aria-label="Cycle: Live feeds Editorial, Editorial feeds Community, Community feeds Advisory, Advisory feeds Acceleration, Acceleration feeds Live." xmlns="http://www.w3.org/2000/svg">',
         '<defs><marker id="fa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#5F6368"/></marker></defs>']
    arrows = [("M382 64 L428 136", 426, 92, "start"), ("M466 190 L430 302", 456, 252, "start"), ("M330 346 L292 346", 310, 378, "middle"),
              ("M170 322 L146 194", 150, 262, "end"), ("M176 140 L238 62", 200, 92, "end")]
    for (d, lx, ly, anc), lbl in zip(arrows, L):
        o.append(f'<path d="{d}" stroke="#5F6368" stroke-width="1.4" fill="none" marker-end="url(#fa)"/>')
        o.append(f'<text x="{lx}" y="{ly}" font-size="12" fill="#3C4043" text-anchor="{anc}" font-weight="500">{e(lbl)}</text>')
    for (x, y), n, c in zip(pos, names, cols):
        tx = "#202124" if c == "p4" else f"var(--{c})"
        o.append(f'<rect x="{x-76}" y="{y-20}" width="152" height="40" rx="20" fill="var(--{c}-soft)" stroke="var(--{c})" stroke-width="1.4"/>')
        o.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" font-weight="700" fill="{tx}">{e(n)}</text>')
    o.append('<circle cx="310" cy="205" r="46" fill="#FFFFFF" stroke="var(--accent)" stroke-width="1.6"/>')
    o.append(f'<text x="310" y="210" text-anchor="middle" font-size="11" font-weight="700" fill="var(--accent)">{e(t["fly_center"])}</text>')
    o.append('</svg>')
    return "\n".join(o)

def moneyflow(f):
    return f'''<svg viewBox="0 0 760 300" role="img" aria-label="Sponsors pay rights and hospitality fees into the Encore programme; money goes out to the tour producer, Fragrant Hill and the partner; value returns to sponsors as hospitality, association, content and reach." xmlns="http://www.w3.org/2000/svg">
<defs><marker id="mf" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#5F6368"/></marker><marker id="mfy" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#F29900"/></marker></defs>
<rect x="10" y="80" width="180" height="130" rx="10" fill="#F8F9FA" stroke="#DADCE0"/>
<text x="24" y="106" font-size="13" font-weight="700" fill="#202124">{e(f["sponsors"])}</text>
<text x="24" y="130" font-size="12" fill="#3C4043">{e(f["s1"])}</text><text x="24" y="150" font-size="12" fill="#3C4043">{e(f["s2"])}</text><text x="24" y="170" font-size="12" fill="#3C4043">{e(f["s3"])}</text>
<path d="M190 118 H276" stroke="#F29900" stroke-width="2" marker-end="url(#mfy)"/><text x="233" y="110" font-size="11" text-anchor="middle" fill="#202124" font-weight="700">{e(f["rights"])}</text>
<path d="M190 172 H276" stroke="#F29900" stroke-width="2" marker-end="url(#mfy)"/><text x="233" y="190" font-size="11" text-anchor="middle" fill="#202124" font-weight="700">{e(f["hosp"])}</text>
<rect x="280" y="70" width="200" height="150" rx="10" fill="#FEF7E0" stroke="#FBBC04" stroke-width="1.6"/>
<text x="294" y="98" font-size="13" font-weight="700" fill="#202124">{e(f["prog"])}</text>
<text x="294" y="124" font-size="12" fill="#3C4043">{e(f["pr1"])}</text><text x="294" y="144" font-size="12" fill="#3C4043">{e(f["pr2"])}</text>
<g stroke="#5F6368" stroke-width="1.4" fill="none" marker-end="url(#mf)"><path d="M480 100 H576"/><path d="M480 145 H576"/><path d="M480 190 H576"/></g>
<rect x="580" y="80" width="170" height="40" rx="8" fill="#FFFFFF" stroke="#DADCE0"/><text x="592" y="97" font-size="12" font-weight="700" fill="#202124">{e(f["out1"])}</text><text x="592" y="112" font-size="10.5" fill="#5F6368">{e(f["o1"])}</text>
<rect x="580" y="125" width="170" height="40" rx="8" fill="#E8F0FE" stroke="#4285F4" stroke-width="1.4"/><text x="592" y="142" font-size="12" font-weight="700" fill="#1A73E8">{e(f["out2"])}</text><text x="592" y="157" font-size="10.5" fill="#3C4043">{e(f["o2"])}</text>
<rect x="580" y="170" width="170" height="40" rx="8" fill="#FFFFFF" stroke="#DADCE0"/><text x="592" y="187" font-size="12" font-weight="700" fill="#202124">{e(f["out3"])}</text><text x="592" y="202" font-size="10.5" fill="#5F6368">{e(f["o3"])}</text>
<path d="M380 220 V256 H100 V214" fill="none" stroke="#5F6368" stroke-width="1.4" stroke-dasharray="5 4" marker-end="url(#mf)"/>
<text x="240" y="276" font-size="11" text-anchor="middle" fill="#3C4043">{e(f["back"])}</text>
</svg>'''

def page_shell(t, lang, title, body):
    return f'''<title>{e(title)}</title>
<meta name="claude:viewport-fit-sides" content="cover">
{FONT_LINK[lang]}
<style>{CSS}</style>
<div class="sheet" lang="{ "zh-CN" if lang == "zh" else "en" }">
{body}
</div>'''

# ---------------------------------------------------------------- pages
def page1(t, lang, other):
    cards = []
    for i in range(5):
        c = PCOL[i]
        prods = "".join(f"<li>{e(p)}</li>" for p in t["pprod"][i])
        cards.append(f'''<div class="pc"><div class="hd" style="background:var(--{c});color:{HDTXT[c]}">{i+1} · {e(t["pnames"][i])}<small>{e(t["psub"][i])}</small></div>
<div class="bd"><div><span class="k">{e(t["k_what"])}</span>{e(t["pwhat"][i])}</div><div><span class="k">{e(t["k_products"])}</span><ul>{prods}</ul></div><div><span class="k">{e(t["k_buyer"])}</span>{e(t["pbuyer"][i])}</div>{chip(t["pwhen"][i], i)}</div></div>''')
    core = "".join(f"<div><b>{e(a)}</b><p>{e(b)}</p></div>" for a, b in t["core"])
    inputs = "".join(f"<div><b>{e(a)}</b><p>{e(b)}</p></div>" for a, b in t["inputs"])
    why = "".join(f'<div><span class="num">{i+1}</span><span><b>{e(a)}</b> {e(b)}</span></div>' for i, (a, b) in enumerate(t["why"]))
    ph_cols = ["p4", "p1", "p5"]
    ph_pill = [[3, 1], [0, 2], [4]]
    phases = ""
    for (title, who, desc, gate), c, pi in zip(t["phases"], ph_cols, ph_pill):
        tx = "#B06000" if c == "p4" else f"var(--{c})"
        phases += f'<div class="ph" style="background:var(--{c}-soft)"><b style="color:{tx}">{e(title)}</b><div class="who">{dots(pi)}{e(who)}</div><p>{e(desc)}</p><div class="gate"><b>{e(t["gate"]).upper()}</b>{e(gate)}</div></div>'
    body = head(t, lang, t["p1_doc"], 1, other) + f'''
<div class="grid">
  <div class="title"><h1>{e(t["p1_title"])}</h1><p>{e(t["p1_lede"])}</p></div>
  <div class="facts">{facts_html(t["facts2"][:3])}</div>
  <div class="blk c12"><h2>{e(t["sys_h"])}</h2>
    <div class="pillars">{"".join(cards)}</div>
    <div class="ups">{"<span>▲</span>" * 5}</div>
    <div class="band core"><div class="lbl">{e(t["core_lbl"])}</div>{core}</div>
    <div class="ups" style="margin:6px 0 4px"><span></span><span></span><span>▲</span><span></span><span></span></div>
    <div class="band inputs"><div class="lbl">{e(t["inputs_lbl"])}</div>{inputs}</div>
  </div>
  <div class="blk c6"><h2>{e(t["fly_h"])}</h2><figure>{pentagon(t)}</figure><figcaption>{e(t["fly_cap"])}</figcaption></div>
  <div class="blk c6"><h2>{e(t["why_h"])}</h2><div class="list">{why}</div>
    <h2 style="margin-top:18px">{e(t["seq_h"])}</h2><div class="phases" style="grid-template-columns:1fr">{phases}</div></div>
</div>
<div class="foot"><span>{e(t["sources"])}</span><span>{e(t["brand"])}</span></div>'''
    return page_shell(t, lang, {"en": "Fragrant Hill Architecture", "zh": "香山系统架构"}[lang], body)

def page2(t, lang, other):
    streams = ""
    for name, who, pil, when in t["streams"]:
        streams += f'<div class="st"><b>{e(name)}</b><p>{e(who)}</p><div class="meta"><span>{dots(pil)}</span>{chip(when, pil[0])}</div></div>'
    rows = ""
    # primary/secondary from streams: primary = first pillar of each stream and the pillar's listed main streams
    prim = {(3, 0), (0, 0), (1, 1), (4, 1), (2, 2), (3, 3), (1, 4), (0, 4), (4, 5), (2, 3)}
    sec = {(2, 0), (3, 1), (2, 1)}
    for i in range(5):
        cells = ""
        for j in range(6):
            if (i, j) in prim: cells += f'<td><span class="d" style="background:var(--{PCOL[i]})"></span></td>'
            elif (i, j) in sec: cells += f'<td><span class="d h" style="background:var(--{PCOL[i]})"></span></td>'
            else: cells += "<td></td>"
        rows += f'<tr><td>{dots([i])}{i+1} {e(t["pnames"][i])}</td>{cells}</tr>'
    mxh = "".join(f"<th>{e(c)}</th>" for c in t["mx_cols"])
    money = "".join(f'<div class="mc" style="border-top-color:var(--{PCOL[i]})"><b>{i+1} · {e(t["pnames"][i])} · {e(a)}</b>{e(b)}<i>{e(c)}</i></div>' for i, (a, b, c) in enumerate(t["money"]))
    when = "".join(f'<div class="cell"><b>{e(a)}</b><div style="margin-bottom:6px">{dots(p)}{", ".join(e(t["pnames"][i]) for i in p)}</div>{e(d)}</div>' for a, p, d in t["when_cols"])
    work = "".join(f'<div class="cell"><b>{e(a)}</b>{e(b)}</div>' for a, b in t["work"])
    body = head(t, lang, t["p2_doc"], 2, other) + f'''
<div class="grid">
  <div class="title"><h1>{e(t["p2_title"])}</h1><p>{e(t["p2_lede"])}</p></div>
  <div class="facts">{facts_html(t["facts2"][1:])}</div>
  <div class="blk c12"><h2>{e(t["streams_h"])}</h2><div class="streams" style="grid-template-columns:repeat(6,minmax(0,1fr))">{streams}</div></div>
  <div class="blk c7"><h2>{e(t["mx_h"])}</h2><div style="overflow-x:auto"><table class="mx"><thead><tr><th>{e(t["k_pillars"])}</th>{mxh}</tr></thead><tbody>{rows}</tbody></table></div><figcaption>{e(t["mx_cap"])}</figcaption></div>
  <div class="blk c5"><h2>{e(t["when_h"])}</h2><div class="cols3" style="grid-template-columns:1fr">{when}</div></div>
  <div class="blk c12"><h2>{e(t["money_h"])}</h2><div class="money">{money}</div></div>
  <div class="blk c12"><h2>{e(t["work_h"])}</h2><div class="cols3">{work}</div></div>
</div>
<div class="foot"><span>{e(t["sources"])}</span><span>{e(t["brand"])}</span></div>'''
    return page_shell(t, lang, {"en": "Fragrant Hill Monetisation", "zh": "香山变现方式"}[lang], body)

def page3(t, lang, other):
    offer = "".join(f"<dt>{e(a)}</dt><dd>{e(b)}</dd>" for a, b in t["offer"])
    tiers = ""
    for i, (name, cnt, items) in enumerate(t["tiers"]):
        tiers += f'<div class="tier" style="border-top:4px solid {"var(--p4)" if i < 2 else "var(--line)"}"><b>{e(name)}</b><small>{e(cnt)}</small><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>'
    prec = "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td><td>{e(c)}</td></tr>" for a, b, c in t["prec"])
    steps = "".join(f'<div class="cell"><b><span class="num" style="display:inline-grid;margin-right:8px;vertical-align:middle">{i+1}</span>{e(a)}</b>{e(b)}<div style="margin-top:6px;font-size:11px;color:var(--muted)">{e(c)}</div></div>' for i, (a, b, c) in enumerate(t["steps"]))
    roles = "".join(f'<div class="cell"><b>{e(a)}</b><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>' for a, items in t["roles"])
    risks = "".join(f'<div class="risk"><b>{e(a)}</b> {e(b)}</div>' for a, b in t["risks"])
    rep = "".join(f'<div class="cell"><b>{e(a)}</b>{e(b)}</div>' for a, b in t["rep"])
    body = head(t, lang, t["p3_doc"], 3, other) + f'''
<div class="grid">
  <div class="title"><div style="font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:#B06000;font-weight:700;margin-bottom:6px">{e(t["p3_eyebrow"])}</div><h1>{e(t["p3_title"])}</h1><p>{e(t["p3_lede"])}</p></div>
  <div class="offer"><h2>{e(t["offer_h"])}</h2><dl>{offer}</dl></div>
  <div class="blk c4"><h2>{e(t["prop_h"])}</h2><div class="facts" style="grid-column:auto">{facts_html(t["prop"])}</div></div>
  <div class="blk c4"><h2>{e(t["mkt_h"])}</h2><div class="facts" style="grid-column:auto">{facts_html(t["mkt"])}</div></div>
  <div class="blk c4"><h2>{e(t["prec_h"])}</h2><table><thead><tr>{"".join(f"<th>{e(c)}</th>" for c in t["prec_cols"])}</tr></thead><tbody>{prec}</tbody></table><figcaption>{e(t["prec_cap"])}</figcaption></div>
  <div class="blk c7"><h2>{e(t["flow_h"])}</h2><figure>{moneyflow(t["flow"])}</figure><figcaption>{e(t["flow_cap"])}</figcaption></div>
  <div class="blk c5"><h2>{e(t["tiers_h"])}</h2><div class="cols3" style="grid-template-columns:1fr">{tiers}</div><figcaption>{e(t["tiers_cap"])}</figcaption></div>
  <div class="blk c12"><h2>{e(t["steps_h"])}</h2><div class="cols4">{steps}</div></div>
  <div class="blk c6"><h2>{e(t["roles_h"])}</h2><div class="cols3">{roles}</div></div>
  <div class="blk c6"><h2>{e(t["risks_h"])}</h2><div class="list" style="gap:8px">{risks}</div></div>
  <div class="blk c12"><h2>{e(t["rep_h"])}</h2><div class="cols3">{rep}</div></div>
</div>
<div class="foot"><span>{e(t["sources"])}</span><span>{e(t["brand"])}</span></div>'''
    return page_shell(t, lang, {"en": "Encore Programme", "zh": "安可计划"}[lang], body)

LINKS = {}  # filled from links.json if present: {"p1-en": url, ...}
lp = os.path.join(ROOT, "build", "links.json")
if os.path.exists(lp):
    import json
    LINKS = json.load(open(lp))

for lang in ("en", "zh"):
    t = T[lang]
    other = "zh" if lang == "en" else "en"
    for key, fn in (("p1-architecture", page1), ("p2-monetisation", page2), ("p3-encore", page3)):
        href = LINKS.get(f"{key}-{other}", f"{key}-{other}.html")
        out = os.path.join(ROOT, f"{key}-{lang}.html")
        with open(out, "w") as f:
            f.write(fn(t, lang, href))
        print("wrote", out)
