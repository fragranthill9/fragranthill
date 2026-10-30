# Raw research findings: teleoperated physical racing as esport + long-distance robot competitions
Compiled 2026-10-30. Sources are web-search snippets; direct page fetches of wikipedia/arxiv/ericsson/huawei/engadget/motor1 were blocked by the session network allowlist, so those are cited from search snippets only. Items marked [UNVERIFIED] rest on a single vendor/secondary source.

---------------------------------------------------------------
## PART A — LANDSCAPE
---------------------------------------------------------------

### A1. Teleoperated real-vehicle / RC racing as entertainment or esport

**Surrogate.tv (Espoo, Finland) — DEAD (bankrupt, Oct 2022)**
- Remote-play platform: real 1:43 RC cars ("Race Real Cars 1:43") raced over the internet in a browser, live races vs other humans; overhead GoPro + low-latency streaming. Also ran an unofficial remote-play Mario Kart Live: Home Circuit tournament (Oct 2020).
- Funding: $2M pre-seed (2019), $2.5M seed Dec 2020 (Supernode Global, PROfounders, Brighteye, Business Finland).
- Wikipedia (SurroRTG): founded 2018, defunct 8 Oct 2022, fate "bankrupted". TechCrunch noted "enough lag in the remote operation to make control something of an issue" in the Mario Kart tournament. No published ms latency figure.
- https://en.wikipedia.org/wiki/SurroRTG ; https://techcrunch.com/2020/12/18/remote-physical-gaming-site-surrogate-tv-raises-a-2-5m-seed ; https://techcrunch.com/2020/10/26/mario-kart-live-home-circuit-gets-unofficial-remote-play-on-surrogate-tv/ ; https://www.hackster.io/news/race-real-miniature-cars-from-thousands-of-miles-away-6652777ae0ea ; https://interestingengineering.com/culture/redefining-videogames-this-company-lets-you-control-the-physical-world-online
- Verdict: closest real precedent for "remote physical racing over the internet as a game", but hobby-scale, no league/broadcast product, and it failed commercially.

**Avicar "Remote Reality" A-0 league (USA) — announced Mar 2023, status UNVERIFIED (no coverage after launch)**
- Private motorsports league: "zero-seat" electric sports cars (Gen0, quoted $1.1M each, 11 cars planned), 360° cameras, video to driver's VR/mobile via 5G/satellite/Wi-Fi; Siemens Advanta engineering partner + digital-twin sim to vet drivers.
- No evidence any race has been held or broadcast. Treat as vaporware until confirmed.
- https://www.motor1.com/news/656304/avicar-remote-reality-drivers-race-remotely/ ; https://news.siemens.com/no-no/avicar-selects-siemens-tech-partner-remote-reality-motorsports-racting/ ; https://hypebeast.com/2023/3/avicar-zero-seat-a-0-remote-reality-motorsports-racing-info ; https://carbuzz.com/news/remote-controlled-racing-league-puts-real-cars-on-track

**Soliton Systems / 5G Hub Eindhoven racing-car remote drive (NL, May 2021) — one-off demo**
- With VodafoneZiggo + Ericsson; remote driver drove a real racing car via live video over 5G; Soliton claims "as low as 35 ms" device-to-driver video latency [vendor claim, UNVERIFIED]; RASCOW2 protocol bonds multiple cellular networks.
- https://solitonsystems.com/news/soliton-systems-and-5g-hub-join-forces-to-demonstrate-remote-control-of-racing-car-via-5g/ ; https://www.eenewseurope.com/en/remote-control-of-racing-car-via-5g-to-be-demonstrated ; https://www.solitonsystems.com/innovation-hub-racing-car

**Volkswagen "Rival Road" internet-connected RC track (2016)** — one-off marketing livestream with multiple camera angles. https://www.geeky-gadgets.com/vw-creates-internet-connected-rc-track-27-07-2016/

**Mario Kart Live: Home Circuit (Nintendo, Oct 2020) — ACTIVE product, local-only**
- RC kart with camera controlled by Switch over local Wi-Fi; no internet remote play (Surrogate hacked it). Sales: ~1.27M (one 2022 article) vs 1.73M shipped (VGChartz, Dec 2022) — figures conflict.
- https://en.wikipedia.org/wiki/Mario_Kart_Live:_Home_Circuit ; https://www.vgchartz.com/game/227275/mario-kart-live-home-circuit/sales

**Anki Overdrive — DEAD (Anki shut down Apr/May 2019; assets to Digital Dream Labs Dec 2019)** — app-controlled slot-car-like toy racing, local only. https://en.wikipedia.org/wiki/Anki_(American_company) ; https://support.anki.bot/article/4-what-happened-to-anki

**Chinese consumer "real-scene RC" apps (实景遥控车) — small, active, not esports**
- App Store listings: 华制远控 (Suzhou), 实景遥控车 (Shandong), 飞车乐园 (pay-per-minute FPV driving), 我的赛车 (claims 4G/5G 异地操控, in-app race sign-up, clubs). No user/revenue data, no broadcast. https://apps.apple.com/cn/app/id6449483018 ; https://apps.apple.com/ch/app/%E5%AE%9E%E6%9A%BB%E9%81%A5%E6%8E%A7%E8%BD%A6/id1547766268 ; https://apps.apple.com/rs/app/%E6%88%91%E7%9A%84%E8%B5%9B%E8%BD%A6-%E7%9C%9F%E5%AE%9E%E8%B5%9B%E8%BD%A6%E9%A9%BE%E9%A9%B6%E5%99%A8/id6470180296

**Student projects**: UCF senior design "RACE" internet RC racing (2024–25); hackster ESP8266/RPi internet RC cars. Not products. https://www.ece.ucf.edu/seniordesign/fa2024sp2025/g30

### A2. Autonomous / hybrid racing leagues (not teleoperated, but the "comparable" a Western audience knows)

**Roborace (UK) — DEAD.** Season Alpha (2019), Season Beta 2020–21 (7 teams, same chassis, own AI; streamed on Twitch). Arrival bought it in 2020 for $10,000, renamed "Arrival R", wrote it off in Apr/May 2022 and confirmed the programme was not continuing. DevBot cars had a human-driver mode but it was never a teleop series. https://www.autocar.co.uk/car-news/business-tech%2C-development-and-manufacturing/arrival-writes-roborace-autonomous-racing ; https://blogs.nvidia.com/blog/roborace-second-season-nvidia-drive ; https://e-formula.news/e-serien/roborace

**A2RL — Abu Dhabi Autonomous Racing League — ACTIVE, broadcast.** Season 1 Apr 2024; Season 2 opened 11 Apr 2025, Grand Final Yas Marina 15 Nov 2025 (11 teams, $2.25M prize pool), broadcast Abu Dhabi Media Network, StarzPlay, Motorsport TV, A2RL YouTube. "Human vs AI" showcase: Daniil Kvyat vs TUM "HAILEY" — gap ~1–1.6 s (sources conflict on who was ahead). A2RL Drone Championship (with DCL): Apr 2025 MAVLab AI beat human; Jan 2026 at UMEX human FPV pilot MinChan Kim beat TII AI 5–4 in best-of-nine. Fully autonomous, not teleoperated — but it IS the live-broadcast "robot racing" precedent. https://en.wikipedia.org/wiki/2025_Abu_Dhabi_Autonomous_Racing_League ; https://www.pmw-magazine.com/news/race-series-news/worlds-largest-autonomous-racing-league-returns.html ; https://www.bernama.com/en/news.php?id=2492592 ; https://www.khaleejtimes.com/uae/abu-dhabi-human-pilot-ai-drones-race ; https://dronedj.com/2026/01/27/a2rl-human-vs-drone-championship/

**Formula E Ghost Racing (Virtually Live, 2019)** — mobile app letting fans race CGI "ghosts" of real drivers using live telemetry during races; no evidence of shutdown found, but no activity reported after 2020 (likely dormant) [UNVERIFIED]. https://www.motorsport.com/formula-e/news/ghost-mobile-game-android-ios/4375916 ; https://www.topgear.com/car-news/electric/formula-es-ghost-racing-game-lets-you-race-real-drivers-live

**Drone Racing League (DRL, NYC) — status UNCLEAR, likely dormant.** Pilots fly FPV (goggles, line-of-sight RF video + control in-venue, not internet teleop). Aired on ESPN, NBC/NBCSN, Twitter; 2023-24 season claimed 260M digital views; Wikipedia now describes DRL in past tense; no 2025/2026 season found. Active FPV leagues instead: Drone Champions League (DCL, 2026 season, Riyadh) and MultiGP (2026 Championship Dallas, winner Minchan Kim; MultiGP also runs a simulator esports season). Digital FPV links: DJI claims 28 ms end-to-end; ExpressLRS control links. https://en.wikipedia.org/wiki/Drone_Racing_League ; https://prnewswire.com/news-releases/the-drone-racing-league-and-us-air-force-elevate-stem-careers-through-expanded-partnership-301885721.html ; https://dronechampionsleague.com/dcl-season-2026/ ; https://www.multigp.com/multigp-championship-2026/

### A3. Telecom 5G remote-driving demos (one-off, not sport)

| Demo | Date | Distance | Latency claim | Source |
|---|---|---|---|---|
| Ericsson + Telefónica (+KTH haptics), MWC Barcelona → Idiada track Tarragona | Feb 2017 | ~50–70 km | "ultra-low", no ms figure; 15 GHz trial band, 4K video + haptics | https://www.ericsson.com/en/press-releases/latin-america/2017/2/5g-can-make-remote-driving-a-reality-telefonica-and-ericsson-demonstrate-at-mwc |
| Vodafone + Cisco + Ericsson, BMW on Düsseldorf test track | 2017 | local | none | https://blogs.cisco.com/sp/driving-by-cellular-cisco-vodafone-and-ericsson-push-the-possibilities-of-5g |
| Huawei + China Mobile + SAIC, MWC Shanghai | Jun 2017 (Huawei CN release dated Jun 2018 — year conflict) | >30 km | "<10 ms E2E control" (English PR) vs "~20 ms E2E" (Huawei CN PR); 240° multi-camera view; 8 cm brake distance at 30 km/h | https://www.huawei.com/en/news/2017/6/5g-based-remote-driving ; https://www.huawei.com/cn/news/2018/6/Huawei-ChinaMobile-SAIC-Vehicles-5G ; https://www.telecomtv.com/content/5g/huawei-demonstrates-5g-based-remote-driving-with-china-mobile-and-saic-motor-27493/ |
| Phantom Auto, CES: car on Las Vegas Strip driven from Mountain View CA | Jan 2018 | ~500–550 miles (~850 km) | "<100 ms" (CEO claim); multi-network bonding | https://spectrum.ieee.org/ces-2018-phantom-auto-demonstrates-first-remotecontrolled-car-on-public-roads ; https://www.technologyreview.com/2018/01/11/67419/i-rode-in-a-car-in-las-vegas-its-driver-was-in-silicon-valley/ |
| Toyota T-HR3 humanoid via NTT Docomo 5G (28 GHz) | Nov 2018 | 10 km; long distance SIMULATED with delay-adding device | "similar to wired" | https://global.toyota/en/newsroom/corporate/25576825.html ; https://www.docomo.ne.jp/english/info/media_center/pr/2018/1129_01.html |
| Einride T-pod truck, MWC Barcelona → AstaZero (Gothenburg) | Feb 2019 | ~1,200–1,517 mi / ~2,500 km | "barely perceptible delay, mostly propagation" (IEEE Spectrum); gaming wheel+pedals rig | https://www.engadget.com/2019-02-28-einride-t-pod-truck-5g-remote-drive-hands-on.html ; https://spectrum.ieee.org/mwc-barcelona-2019-on-the-road-to-selfdriving-cars-5g-will-make-us-better-drivers |
| China Mobile Xiongan remote driving | 2019 | 20 km | "network latency ≤6 ms" | https://news.cgtn.com/news/7949444f306b7a6333566d54/index.html |
| China Mobile + China General Technology "open-road 5G remote driving", World Internet Conference Wuzhen | Oct 2019 | n/a | "system latency ≤15 ms" with MEC | https://www.cac.gov.cn/2019-10/22/c_1573276511420881.htm |
| Deutsche Telekom + Ottopia: driver in Stuttgart, car on Tel Aviv test track | Feb 2020 | ~4,000 km (cross-continent) | none published; AI predicts network quality seconds ahead to adapt bitrate | https://www.telekom.com/en/newsroom/latest-updates/media-information/2020/2/the-new-long-distance-drivers-in-the-office-and-4-000-kilomete |
| DENSO + DriveU.auto: vehicle in USA driven from Abashiri, Japan | ~2022 | transpacific | none published [UNVERIFIED] | https://driveu.auto/blog/denso-validates-driveu-auto-connectivity-platform-for-autonomous-vehicle-teleoperation/ |
| Ericsson + Deutsche Telekom + Vay, MWC Barcelona → Berlin, 5G with L4S (RFC 9330) | Feb 2023 | ~1,500 km direct; routed via Sweden+London ≈5,000 km path | Vay: video frame latency "never exceeds 200 ms" with L4S; spikes trigger minimum-risk maneuver | https://www.ericsson.com/en/news/2023/2/ericsson-dt-and-vay-demo-5g-teledriving ; https://vay.io/deep-dive-how-to-break-the-congestion-barrier-achieving-low-latency-with-high-throughput-for-safe-teledriving/ |
| CTAG "Remote Driver" (Nokia, UPM, UC3M): operator in Valencia, car on CTAG track Galicia | Mar (2024?) | ~744 km (LinkedIn claim) | none; goal "high-speed" | https://ctag.com/en/ctag-demonstrates-remote-driving-of-high-speed-vehicles-using-5g-networks-in-galicia/ |
| NTT Docomo + Keio Univ.: haptic bilateral robot teleop over commercial 5G SA w/ Configured Grant, shown MWC 2026 | Feb 2026 | in Japan | reduced avg latency/jitter vs std 5G SA | https://www.docomo.ne.jp/english/info/media_center/pr/2026/0225_00.html |

### A4. Teledriving companies (commercial status)
- **Vay (Berlin / Las Vegas) — ACTIVE.** Commercial remote-driven car-sharing in Las Vegas since Jan 2024 (teledrivers local in US); fleet 50 (Mar 2025) → ~175 (Apr 2026, Hoodline/RJ); >10,000 riders; $60M from Grab Nov 2025 (Sacra, unverified); uses NVIDIA DRIVE AGX; says teledriving needs "tens of ms" latency; auto safe-stop on link loss. https://techcrunch.com/2025/01/08/vay-expands-driverless-car-sharing-fleet-in-las-vegas ; https://hoodline.com/2026/04/remote-drivers-invade-downtown-as-vay-supercharges-vegas-fleet/ ; https://sacra.com/c/vay
- **Halo.Car (Las Vegas) — status UNKNOWN** (launched driverless remote-piloted EV rental delivery Jun 2023 on T-Mobile 5G; no coverage found after 2023). https://techcrunch.com/2023/06/29/halo-car-launches-remotely-piloted-rental-car-deliveries-in-las-vegas
- **Phantom Auto (Mountain View) — DEAD** (shut Mar 2024 after $95M raised; assets + Swedish subsidiary Voysys bought by Serve Robotics Sep 2025 for ~$5.75M; Voysys claims glass-to-glass "as low as 50 ms" with multi-link redundancy [vendor]). https://techcrunch.com/2024/03/12/remote-driving-startup-phantom-auto-is-shutting-down/ ; https://investors.serverobotics.com/news-releases/news-release-details/following-acquisition-phantom-auto-serve-robotics-adds-voysys
- **Ottopia (Israel) — active** (teleop software; dynamic receive buffer; AI network prediction). https://medium.com/ottopia/teleoperation-safety-principles-and-indirect-methods-of-control-f47404bfd86e
- **DriveU.auto (Israel) — active** (cellular bonding of multiple 4G/5G links; DENSO validation). https://driveu.auto/blog/using-5g-for-teleoperation-of-autonomous-vehicles/
- **Fernride (Munich) — active** (teleoperated/autonomous yard trucks; series production 2024; uses Steinwurf "Rely" low-latency FEC). https://www.steinwurf.com/blog/fernride-uses-rely-fec-software-to-improve-driverless-logistics
- **Einride (Sweden) — active** (remote operators supervise/drive Pods; Telia+Ericsson 5G at DB Schenker Jönköping). https://www.einride.tech/press/einride-showcases-new-teleoperation-solution-at-mobile-world-congress
- **MIRA + Deutsche Telekom** teleoperated shuttles pilot, Bonn, Aug 2023. https://www.telekom.com/en/newsroom/latest-updates/media-information/2023/8/5g-telekom-and-mira-test-teleoperated-shuttles-in-bonn

### A5. Robot competitions — how were robots controlled?

**ANA Avatar XPRIZE Finals (Long Beach, 1–5 Nov 2022)** — 17 teams/10 countries; $10M purse, NimbRo (Univ. Bonn) won $5M grand prize. Operators were XPRIZE judges (not team members) in a separate operator room in the SAME venue; link via Internet/WiFi (NimbRo: pure UDP, redundant WiFi, ~14 Mbit/s, low-latency HEVC + Opus, spherical rendering to hide head-motion latency). NOT long-distance. https://cosmiclog.com/2022/11/06/german-robotics-team-wins-avatar-xprize-showdown/ ; https://arxiv.org/abs/2303.03297 ; https://www.ais.uni-bonn.de/behnke/talks/IROS_2023_Keynote_Sven_Behnke.pdf

**Beijing E-Town humanoid half-marathon (19 Apr 2025)** — ~20–21 robot teams, separate lane; rules allowed manual remote control (incl. semi-autonomous) or full autonomy; each robot had ~3 humans (engineer/controller/pacer) running alongside with handheld controllers; Tiangong Ultra won 2:40:42. Nearby-operator, not long-distance. https://english.beijing.gov.cn/latest/news/202504/t20250417_4067731.html ; https://www.chinadaily.com.cn/a/202504/19/WS68032499a3104d9fd3820604_3.html

**CMG World Robot Competition — Mecha Fighting Series, Hangzhou (25 May 2025)** — 4 Unitree G1 robots, 3 rounds × 2 min, broadcast nationally on CCTV; "human-machine collaborative": pilots stood RINGSIDE with handheld controllers (voice/motion-sensing shown pre-match but matches were joystick); moves pre-trained via mocap of pro fighters, balance autonomous; winner "AI Strategist" piloted by Lu Xin. Unitree said future editions would add motion-sensing control. https://www.livescience.com/technology/robotics/china-pits-rival-humanoids-against-each-other-in-worlds-first-robot-boxing-tournament ; https://www.yicai.com/news/102634073.html ; https://english.henan.gov.cn/2025/05-26/3162232.html

**World Humanoid Robot Games, Beijing (14–17 Aug 2025; 2nd edition 22–26 Aug 2026)** — 2025: ~280 teams/16 countries/26 events; rules allowed "manual remote control" or full autonomy; freestyle/dance required autonomy; timed track events applied coefficients favouring autonomy (reported 0.8× for autonomous, or 1.2× penalty for remote — sources conflict); Tiangong Ultra was the only fully autonomous 100 m entrant; 5v5 soccer fully autonomous (B-Human won 2026). 2026: 2,056 robots/666 teams/16 countries/51 disciplines; Tiangong Ultra 100 m 8.64 s. Remote control = operator in venue with controller. No cross-border remote. https://english.beijing.gov.cn/latest/news/202505/t20250509_4085788.html ; https://investinchina.chinadaily.com.cn/s/202508/20/WS68a56cac498ee5cca9a583c5/humanoids-compete-in-global-robot-game.html ; https://english.beijing.gov.cn/beijinginfo/sci/latesttrends/202608/t20260825_4836357.html

**RoboMaster (DJI, Shenzhen, annual since 2015)** — 7v7 MOBA-style robot combat; robots human-piloted from the arena side via PC with first-person camera feed ("looks exactly like a video game"), sentry robot autonomous; finals livestreamed on Twitch (2017–2019, millions of views) and Youku. Closest Chinese "robot esport with broadcast" precedent — but pilots are on-site. https://dji.com/newsroom/news/dji-brings-robomaster-2017-finals-to-twitch ; https://www.tubefilter.com/2018/07/26/robomaster-robot-combat-live-stream-twitch/ ; https://qz.com/1342950/dji-is-turning-robot-battles-into-the-next-college-sport-advantage-china

**BattleBots / Robot Wars** — commercially available RC (2.4 GHz) only, tethered control banned, max 2 operators per bot standing at the arena, mandatory radio fail-safe that kills drive+weapons on link loss. Line-of-sight, in-venue. https://battlebots.com/wp-content/uploads/2015/12/BattleBots-Design-Rules.Rev-2018.0.pdf ; https://runamok.tech/rules/BB_season3_rules.html

**RoboCup** — robots must act autonomously during play (Humanoid League rule since at least 2006; MSL: "no human intervention during a match"). https://humanoid.robocup.org/wp-content/uploads/HumanoidLeagueRules2002.pdf ; https://en.wikipedia.org/wiki/RoboCup_Middle_Size_League

**Telexistence (Tokyo)** — Model-T (2020, FamilyMart trial, VR operator ~5 miles away at TX office; KDDI-verified 50 ms end-to-end video with H.265); TX SCARA restocking robots in ~300 FamilyMart stores (rollout to Mar 2025), autonomous 98% of time, remote VR operator takes over on failure. Commercial teleop, not competition. https://tx-inc.com/?p=10624 ; https://www.therobotreport.com/restocking-robots-deployed-in-300-japanese-convenience-stores/

**Sanctuary AI (Vancouver)** — Phoenix humanoid teleoperated by in-house pilots to gather training data (single-site studio); Jul 2026 rebrand to "Physical AI" [UNVERIFIED]. Not competition. https://www.therobotreport.com/sanctuary-ai-integrates-tactile-sensors-into-phoenix-general-purpose-robots/

**Honda avatar robot** — multi-fingered hand teleop demos at Humanoids Summit Tokyo (May 2026) and CEATEC Chiba (Oct 2026), operator in small control room on-site. https://global.honda/en/topics/2026/c_2026-10-05ceng.html

### A6. Actual cross-site / cross-border remote-robot COMPETITIONS (the only ones found)
- **Mercury Remote Robot Challenge (Oklahoma State University, annual since 2010)** — student robots must be driven over the Internet from ≥50 miles (some say >100 miles) away; teams from US, Colombia, Brazil, Mexico, Guatemala; Latin-American regional round in Bogotá. Academic, no broadcast. https://news.okstate.edu/articles/engineering-architecture-technology/2018/mercury-remote-robot-challenge-oklahoma-state-unviersity ; https://www.k-state.edu/media/newsreleases/2019-05/mercuryrover5619.html ; https://www.elespectador.com/?p=2996780
- **Japan–China–Thailand–Taiwan university "internet robot remote control competition"** (since ~2007) — paired teams, one robot controlled remotely over the Internet from another country. Academic. (search.isc.ac records) https://search.isc.ac/inventory/49/3111999.htm
- **Robothon Grand Challenge / "Towards Remote Robotic Competitions"** (arXiv 2201.09565) — 9 robot platforms on 4 continents scored remotely on a shared internet-connected task board (robots autonomous/local, remote scoring). https://arxiv.org/abs/2201.09565
- No evidence found (EN or ZH) of any cross-border, broadcast, teleoperated robot or vehicle competition.

### A7. Verdicts
(a) Remote physical racing as a broadcast esport: NO established precedent. Surrogate.tv (dead 2022) proved the browser-to-real-RC-car concept at hobby scale; Avicar announced a VR-driven real-car league in 2023 but has shown nothing since; Soliton/VW did one-off demos. Everything with real broadcast/esports framing is either autonomous (A2RL, Roborace), FPV line-of-sight (DRL/DCL/MultiGP), or on-site pilots (RoboMaster).
(b) Cross-border teleoperated robot competition: NO precedent at scale; only academic contests (Mercury Challenge ≥50 mi; JP-CN-TH-TW university contest). ANA Avatar XPRIZE, Beijing humanoid events and the Hangzhou G1 fights all used operators inside the venue.
Closest comparables a Western audience knows: Drone Racing League (FPV pilots, TV broadcast), BattleBots (RC combat on Discovery), A2RL (autonomous racing with TV/YouTube broadcast, "human vs AI" storyline), RoboMaster (Twitch-streamed robot esport), and Vay/Phantom Auto (teledriving as a commercial service).

---------------------------------------------------------------
## PART B — TECHNOLOGY
---------------------------------------------------------------

### B1. Standards & requirements
- 3GPP TS 22.186 Table 5.5-1 "Remote driving": max E2E latency 5 ms (UE ↔ V2X application server), reliability 99.999%, UL 25 Mbps, DL 1 Mbps. https://www.itecspec.com/3gpp/22.186/s/5.5
- 3GPP Rel-15 URLLC: 1 ms user-plane radio latency, 99.999% reliability (radio-only target, NOT an end-to-end budget). Tele-operated driving commonly cited at ~20 ms E2E in URLLC literature. https://arxiv.org/pdf/1810.06938 ; https://arxiv.org/pdf/2508.20205
- 5GAA ToD (as cited by secondary papers): 100 ms uplink service-level latency, 99% reliability; 4 cameras × 8 Mbps = 32 Mbps UL; RTT is the governing metric; network-level budget ~40–45 ms within a 100 ms app budget. https://arxiv.org/pdf/2507.20438 ; https://arxiv.org/pdf/2606.17654
- Vendor rule of thumb (Soliton): ≤100 ms glass-to-glass for high-speed remote driving. https://blog.solitonsystems.com/blog/the-critical-importance-of-cellular-bonding-technology-in-teleoperations-and-teledriving

### B2. Measured / claimed latencies
- Commercial 5G (Kia Soul EV study, arXiv 2503.14186, 2025): avg glass-to-glass 202 ms with network RTT only 47 ms → video pipeline, not the radio, is the bottleneck. https://arxiv.org/abs/2503.14186
- TU/e 4G vs 5G remote-driving architecture (Frontiers 2022): network adequate only at relatively low speeds (<40 km/h). https://www.frontiersin.org/articles/10.3389/ffutr.2021.801567/full
- ZTE + China Unicom + Shandong Lingong 5G remote excavator (2019): air-interface 1 ms, control-signal total 25 ms, video 300 ms. https://www.zte.com.cn/global/about/news/20190426e1.html
- Huawei 5G-A at Yimin open-pit mine (2025, 100 autonomous XCMG trucks, Huaneng): 500 Mbps UL, 20 ms latency (vendor). https://thedriven.io/2025/05/20/100-autonomous-electric-trucks-begin-work-in-giant-mongolia-mine ; China Mobile + Huawei 5G remote-control mining trucks at Bayan Obo (2019). https://www.xinhuanet.com/english/2019-05/17/c_138065799.htm
- Qingdao Port (Ericsson + China Unicom + ZPMC, 2019): 5G-controlled automated quay cranes, 30+ HD camera streams + PLC control over 5G. https://www.worldports.org/ericsson-to-launch-smart-5g-harbour-at-major-chinese-port/ ; Ningbo-Zhoushan Meishan terminal 5G crane control (China Mobile, Apr 2019). https://govt.chinadaily.com.cn/s/201904/22/WS5cbe8241498e079e6801ec05/ningbo-zhoushan-port-gets-5g-upgrade.html ; Gwangyang (KR) 5G+MEC RTG cranes <100 ms. https://container-news.com/gwangyang-port-and-lg-unit-to-create-5g-container-cranes
- China Mobile 5G-A remote robot at MWC Shanghai 2025: "<20 ms" transmission latency. https://china.huanqiu.com/article/4NiQ09WutK1
- Vendor G2G claims: Voysys "as low as 50 ms"; Soliton "as low as 35 ms"; Telexistence 50 ms (KDDI-verified, H.265, 2020); DJI digital FPV 28 ms; Phantom Auto "<100 ms" over 850 km (2018); Vay ≤200 ms frame latency Barcelona→Berlin via 5,000 km path with L4S.
- Jetson pipeline examples: Jetson Nano + H.265 ≈110 ms G2G incl. ~10 ms radio; Jetson TX2 H.264 1-camera processing ~10 ms + ~1 ms LAN + display frame interval. https://support.doodlelabs.com/portal/en/kb/articles/low-latency-c-c-and-video-streaming-with-the-nvidia-jetson-nano-video-streaming ; https://www.ximea.com/support/wiki/allprod/Low_latency_H264_streaming
- Intercontinental network RTT (China–Europe): China Telecom Global quotes Shanghai–Frankfurt 161–168 ms (2013–15 SLA figures); Hats Network probes HK–Frankfurt 150.7 ms, Taipei–Frankfurt 166 ms (2026); Areapac Beijing–Frankfurt 113 ms (outlier). https://hatsnet.io/docs/network/latency/pairs/hkg-fra-rtt ; https://www.hkex.com.hk/-/media/HKEX-Market/Services/Connectivity/Hosting-Services/Subscriber-Notices-and-Guidance-Note/Roy-Ng-Connect-the-leading-Global-Financial-Centres-by-Ultra-Low-latency-network.pdf

### B3. Physics floor (computed, great-circle, c = 299,792 km/s, fiber n ≈ 1.468 → ~204,000 km/s)
| Pair | Great-circle km | One-way vacuum | RTT vacuum | One-way fiber | RTT fiber (straight) | RTT fiber ×1.3 route factor |
|---|---|---|---|---|---|---|
| Shanghai–Stockholm | 7,764 | 25.9 ms | 51.8 ms | 38.0 ms | 76 ms | ~99 ms |
| Beijing–Stockholm | 6,708 | 22.4 | 44.8 | 32.8 | 66 | ~85 |
| Shanghai–Frankfurt | 8,820 | 29.4 | 58.8 | 43.2 | 86 | ~112 |
| Shanghai–London | 9,197 | 30.7 | 61.4 | 45.0 | 90 | ~117 |
| Shanghai–Los Angeles | 10,435 | 34.8 | 69.6 | 51.1 | 102 | ~133 |
| Shanghai–Abu Dhabi | 6,541 | 21.8 | 43.6 | 32.0 | 64 | ~83 |
Real Internet RTT Shanghai↔Europe is ~150–170 ms (above), i.e. ~1.5–2× the fiber floor due to cable routing (via Mongolia/Russia or via Indian Ocean/Suez) and router hops.

### B4. Human factors
- Simple visual reaction time ~200–250 ms (lab); expected-event driver brake response ~0.7–0.75 s, unexpected ~1.25 s. https://ar5iv.labs.arxiv.org/html/2208.08651
- Teleoperated-driving studies: 150 ms added delay no significant impairment; 300 ms clear degradation (esp. complex scenarios); >170 ms "detrimental", ≤250 ms "tolerable"; performance maintained up to 300 ms in a 20-participant study; 50 vs 150 ms difference insignificant on safety measures (2025). https://cris.iucc.ac.il/en/publications/effects-of-simulated-time-delay-on-teleoperators-performance-in-i/ ; https://mediatum.ub.tum.de/doc/1695113/document.pdf ; https://arxiv.org/abs/2605.15952
- Patent (remote driving) proposes max E2E latency settings ~240–300 ms. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12537921
- Worked example (truck teleop patent): at 30 m/s with 200 ms one-way latency the truck is 12 m ahead of where the operator sees it (two-way). https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11740624
- Sim racing / esports: 60 Hz frame = 16.7 ms; typical PC total system latency 30–80 ms; "<100 ms" considered good for console rigs (forum rules-of-thumb, not authoritative); NVIDIA Reflex claims 10–25 ms reductions [vendor].

### B5. Architecture elements (with sources where available)
- Cellular bonding / multi-SIM: Phantom Auto, Soliton RASCOW2, Voysys multi-link, DriveU ("5G-like performance from multiple 4G links"), 5G-MOBIX single vs multi-SIM trial (link selection + aggregation reduce outages/frozen video). https://www.5g-mobix.com/assets/files/5G-MOBIX_Trials_results_FI-TS_webinar_062022.pdf ; https://bohrium.dp.tech/paper/arxiv/2410.19791
- L4S (RFC 9330) ECN-based congestion signalling in RAN keeps queueing delay low; T-Mobile US rolled L4S on 5G-A, Vay reports predictable latency. https://www.rcrwireless.com/?p=421977
- Network slicing needs 5G SA core; MEC brings the control server to the edge (Wuzhen 2019 demo used MEC; Gwangyang port 5G+MEC). https://driveu.auto/?p=1636
- Predictive display / latency compensation: show predicted vehicle position ahead by v×RTT (truck patent); NimbRo spherical rendering hides head-motion latency; Ottopia AI predicts network quality seconds ahead and adapts bitrate; dynamic receive-buffer sizing.
- Fail-safe: BattleBots mandatory radio fail-safe; Vay vehicle "puts itself into a safe state within milliseconds" / minimum-risk maneuver on latency spike; BattleBots max 2 operators.
- Codec/transport: low-latency HEVC + Opus over UDP (NimbRo); H.265 at 50 ms (Telexistence); WebRTC typical sub-500 ms (vendor figures 50–300+ ms), SRT ~0.5–2 s, HLS 6–30 s (vendor comparisons). https://antmedia.io/?p=125850 ; https://metered.ca/blog/webrtc-vs-hls-which-is-best-for-you
- T-Box (telematics box): vehicle's remote communication unit = cellular modem (4G/5G module, e.g., Huawei MH5000) + automotive MCU (e.g., NXP S32K344 / LPC5516, Renesas) + CAN/CAN-FD/Ethernet gateway to the in-vehicle network + GNSS + Wi-Fi/BT + accelerometer + eSIM/security element; collects bus data and can perform remote control of vehicle functions; China passenger-car T-Box 4G share 93% in Q1 2020, now moving to 5G; market ~$2.8B (2023). https://nxp.com/assets/block-diagram/en/T-BOX.pdf ; https://www.arrow.com/en/research-and-events/articles/t-box-reference-design-and-solutions-for-internet-of-vehicles ; https://www.businesswire.com/news/home/20200807005337/en/Global-China-Telematics-Box-T-Box-Industry-Report-2020
- Digital twin: Siemens built a digital-twin sim for Avicar to vet drivers; A2RL/Roborace use sims for AI development.
