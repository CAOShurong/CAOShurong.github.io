"""Build a dependency-free bilingual academic website."""
from pathlib import Path
from html import escape as esc
import shutil
import json
import hashlib
from content import *

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'site'
IMAGE_SIZES=json.loads((ROOT/'image-sizes.json').read_text(encoding='utf-8'))
ORIGIN='https://caoshurong.github.io'
ASSET_VERSION=hashlib.sha256((ROOT/'app.js').read_bytes()+(ROOT/'style.css').read_bytes()).hexdigest()[:10]
def tx(en,zh,l): return zh if l else en
def url(path='',l=0): return ('/zh/' if l else '/')+(path.strip('/')+'/' if path else '')
def img(name,alt,cls='',eager=False):
    w,h=IMAGE_SIZES.get(name,(1,1))
    return f'<img src="/assets/{name}" alt="{esc(alt)}" width="{w}" height="{h}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async">'
def link(href,label,cls=''):return f'<a href="{esc(href)}" class="{cls}">{label}</a>'
def heading(kicker,title,desc=''):
    return f'<header class="page-heading"><p class="eyebrow">{kicker}</p><h1>{title}</h1>{f"<p class=lead>{desc}</p>" if desc else ""}</header>'
def section(title,more='',href=''):
    return f'<div class="section-title"><h2>{title}</h2>{link(href,more+" <span aria-hidden=true>↗</span>") if href else ""}</div>'
def portrait(l):return img('portrait-2026.jpg',tx('Portrait of Shurong Cao','曹书嵘个人照片',l),'portrait',True)

def paper(p,l,full=False):
    short=''
    links=''.join(link(u,('代码' if l and t=='Code' else t)+' ↗') for t,u in p['links'])
    body=f'<p class="paper-summary">{p["summary"][l]}</p>'
    if full:
        body+=f'<details><summary>{tx("About this work","关于这项研究",l)}</summary><p>{p["abstract"][l]}</p></details>'
        body+=f'<details class="citation"><summary>{tx("Cite this work","引用这篇论文",l)}</summary><pre>{esc(p["bib"])}</pre><button type="button" class="copy-cite" data-copy="{p["id"]}">{tx("Copy BibTeX","复制 BibTeX",l)}</button><a href="/assets/{p["id"]}.bib" download>{tx("Download .bib","下载 .bib",l)}</a><span role="status" class="copy-status"></span></details>'
    display_image=p['image']
    display_alt=tx('FALCO-WAFER attention visualizations on wafer defects','FALCO-WAFER 晶圆缺陷注意力可视化',l) if display_image=='falco-results.webp' else p['alt'][l]
    figure_url = '/assets/'+display_image if full else url('publications',l)+'#'+p['id']
    return f'<article class="paper" id="{p["id"]}"><a class="paper-figure" href="{figure_url}" aria-label="{esc(p["title"])}">{img(display_image,display_alt)}</a><div><div class="paper-top"><span class="eyebrow">{p["short"]}</span>{short}</div><h3>{p["title"]}</h3><p class="authors">{p["authors"]}</p><p class="venue">{p["venue"]}</p>{body}<div class="text-links">{links}</div></div></article>'

def research_figure(v,l):
    return f'<figure class="research-figure"><a class="figure-link" href="/assets/{v["image"]}" aria-label="{esc(v["alt"][l])}">{img(v["image"],v["alt"][l])}</a><figcaption><span>{v["caption"][l]}</span>{link(v["source"],v["credit"]+" ↗")}<small>{link("https://creativecommons.org/licenses/"+("by-nc-nd" if "NC" in v["license"] else "by")+"/4.0/",v["license"])}</small></figcaption></figure>'

def research_grid(l):
    cards=[]
    for r,v in zip(RESEARCH,RESEARCH_VISUALS):
        cards.append(f'<article class="research-card">{research_figure(v,l)}<div class="research-card-copy"><p class="eyebrow">{v["tags"][l]}</p><h3>{link(url("research",l)+"#theme-"+r[0],r[2 if l else 1])}</h3><p>{r[6 if l else 5]}</p>{link(url("research",l)+"#theme-"+r[0],tx("Explore this direction","了解这一方向",l)+" ↗","direction-link")}</div></article>')
    return '<div class="research-grid">'+''.join(cards)+'</div>'

def exchanges(l):
    return f'<div class="exchange-grid"><article><a class="exchange-logo" href="https://www.hkust-gz.edu.cn/">{img("hkust-gz-logo.png",tx("HKUST Guangzhou logo","香港科技大学（广州）校徽与校名",l))}</a><div><p class="eyebrow">{tx("Research experience","科研交流",l)}</p><h3>{tx("HKUST (Guangzhou)","香港科技大学（广州）",l)}</h3><p>{tx("Visiting research in nanophotonics and optoelectronic devices, connecting simulation, geometry optimization and device characterization.","围绕纳米光子学与光电器件开展科研交流，连接仿真、结构优化与器件表征。",l)}</p></div></article><article><a class="exchange-logo" href="https://www.cam.ac.uk/">{img("cambridge-logo.svg",tx("University of Cambridge logo","剑桥大学校徽与校名",l))}</a><div><p class="eyebrow">{tx("Academic exchange","学术交流",l)}</p><h3>{tx("Cambridge · St Catharine’s College","剑桥 · 圣凯瑟琳学院",l)}</h3><p>{tx("Hardware design programme; team leader and commencement speaker. A collaborative engineering experience in an international academic setting.","参加硬件设计交流项目，担任团队负责人及结业发言人，在国际学术环境中开展协作式工程实践。",l)}</p></div></article></div>'

def education(l):
    return f'<div class="education"><article><span class="school-crest cuhk-crest"><img src="/assets/cuhk-logo.png" alt="CUHK crest"></span><div><span class="date">2026 — {tx("present","至今",l)}</span><h3>{tx("The Chinese University of Hong Kong","香港中文大学",l)}</h3><p>{tx("PhD student · Electronic Engineering","电子工程博士研究生",l)}</p><p class="muted">{tx("Supervisor: Prof. Ni Zhao","导师：Prof. Ni Zhao",l)}</p></div></article><article><span class="school-crest"><img src="/assets/nju-crest.svg" alt="Nanjing University crest"></span><div><span class="date">2022 — 2026</span><h3>{tx("Nanjing University","南京大学",l)}</h3><p>{tx("B.Eng. · Integrated Circuit and System Design","工学学士 · 集成电路设计与集成系统",l)}</p><p class="muted">{tx("School of Integrated Circuits · Suzhou Campus","集成电路学院 · 苏州校区",l)}</p></div></article></div>'

def project_card(p,l):
    visual=img(p['image'],p.get('caption',p['title'])[l]) if p.get('image') else f'<div class="project-symbol" aria-hidden="true">{ "<span>V</span><small>DEVICE · SENSING</small>" if p["id"]=="vacuum-sensor" else "<span>BL</span><small>EXPERIMENT · PROVENANCE</small>"}</div>'
    return f'<article class="project-card"><a class="project-visual" href="{url("projects/"+p["id"],l)}" aria-label="{esc(p["title"][l])}">{visual}</a><div class="project-content"><p class="eyebrow">{p["tag"][l]}</p><h3>{link(url("projects/"+p["id"],l),p["title"][l]+"&nbsp;↗")}</h3><p>{p["summary"][l]}</p></div></article>'

def home(l):
    intro=tx('I am a PhD student in Electronic Engineering at The Chinese University of Hong Kong, advised by Prof. Ni Zhao. My current interests centre on emerging semiconductor devices, low-temperature fabrication, and monolithic 3D integration.','我是香港中文大学电子工程博士研究生，导师为 Prof. Ni Zhao。目前关注新型半导体器件、低温制造工艺与单片三维集成，正在探索材料、器件和工艺之间的连接。',l)
    s=f'<section class="hero"><div class="portrait-panel">{portrait(l)}<p>{tx("Hong Kong · Electronic Engineering","香港 · 电子工程",l)}</p></div><div class="hero-copy"><p class="eyebrow">{tx("Semiconductor devices & integration","半导体器件与集成",l)}</p><h1>{tx("Shurong Cao","曹书嵘",l)}<span class="name-secondary">{tx("曹书嵘","Shurong Cao",l)}</span></h1><p class="hero-role">{tx("PhD Student · The Chinese University of Hong Kong","博士研究生 · 香港中文大学",l)}</p><div class="hero-rule"></div><p class="intro">{intro}</p><p class="intro secondary-intro">{tx("An integrated-circuit foundation, with experience spanning device simulation, industrial vision, and open-source research software.","以集成电路为基础，连接器件仿真、工业视觉与开源科研软件。",l)}</p><div class="hero-actions">{link(url("research",l),tx("Research interests","研究方向",l)+" ↗","button")}{link(url("cv",l),tx("Curriculum vitae","个人简历",l),"button secondary")}{link("https://github.com/CAOShurong",tx("GitHub Profile","GitHub 主页",l)+" ↗","button secondary github-profile")}{link("mailto:"+EMAIL,tx("Email","邮件联系",l)+" ↗","quiet-link")}</div></div></section>'
    s+=f'<section class="research-strip" id="research-interests">{section(tx("Current research interests","当前研究兴趣",l),tx("Research overview","研究概览",l),url("research",l))}<p class="research-introduction">{tx("Exploring how materials, low-temperature processing and device architecture can work together above completed silicon circuits. Selected literature below illustrates the questions and approaches informing my research.","探索材料、低温工艺与器件结构如何协同工作，在已完成的硅基电路之上构建新的功能。以下代表性文献图展示了我正在关注的问题与技术路径。",l)}</p>{research_grid(l)}</section>'
    s+=f'<section class="section home-publications">{section(tx("Selected publications","代表论文",l),tx("All publications","全部论文",l),url("publications",l))}<div class="publication-grid">'+''.join(paper(p,l,True) for p in PAPERS)+'</div></section>'
    s+=f'<section class="section home-practice" id="research-practice">{section(tx("Research into practice","从研究到实践",l),tx("All projects","全部项目",l),url("projects",l))}<div class="projects-grid home-projects">'+''.join(project_card(p,l) for p in PROJECTS)+'</div></section>'
    s+=f'<section class="section academic-journey" id="academic-exchange">{section(tx("Education & academic exchange","教育与学术交流",l),tx("Full experience","完整经历",l),url("experience",l))}{education(l)}{exchanges(l)}</section>'
    s+=f'<section class="open-source-band"><div><p class="eyebrow">{tx("Maintainer & upstream contributor","开源维护与上游贡献",l)}</p><h2>{tx("Building beyond my own projects.","让工程实践延伸到更广的社区。",l)}</h2><p>{tx("37 merged contributions across 22 external repositories, including Astropy, cibuildwheel and GitHub MCP Server.","37 个上游贡献被 22 个外部仓库接纳，包括 Astropy、cibuildwheel 与 GitHub MCP Server。",l)}</p></div><div>{link("https://github.com/CAOShurong",tx("GitHub Profile","GitHub 主页",l)+" ↗","button")}{link(url("projects",l)+"#upstream",tx("Explore contributions","查看贡献",l)+" ↗","quiet-link")}</div></section>'
    s+=f'<section class="contact-band"><div><p class="eyebrow">{tx("Research & collaboration","研究与合作",l)}</p><h2>{tx("Let’s exchange ideas.","期待与你交流。",l)}</h2></div>{link("mailto:"+EMAIL,EMAIL+" ↗")}</section>'

    return s

def research(l):
    s=heading(tx('Research','研究',l),tx('Devices, fabrication,<br>and the next dimension.','器件、工艺与<br>新的集成维度。',l),tx('My research direction is developing around semiconductor devices and practical routes to vertically integrated electronics.','我的研究方向正在围绕半导体器件与垂直集成电子系统的实际工艺路径逐步展开。',l))
    s+='<div class="research-detail">'
    for r,v,context in zip(RESEARCH,RESEARCH_VISUALS,RESEARCH_CONTEXT):s+=f'<article id="theme-{r[0]}">{research_figure(v,l)}<div><p class="eyebrow">{v["tags"][l]}</p><h2>{r[2 if l else 1]}</h2><p>{r[6 if l else 5]}</p><p>{context[l]}</p></div></article>'
    s+='</div>'
    s+=f'<section class="approach"><p class="eyebrow">{tx("How I approach research","研究思路",l)}</p><h2>{tx("From physical mechanisms<br>to integration choices.","从物理机制出发，<br>理解集成选择。",l)}</h2><p>{tx("I am drawn to questions where materials, process history, defects, and interfaces determine device behavior. My integrated-circuit background informs an interest in how those device-level choices translate into circuit function and manufacturable systems.","我关注材料、工艺历史、缺陷与界面如何共同决定器件行为。集成电路背景也使我重视这些器件层面的选择如何进一步影响电路功能与可制造的系统。",l)}</p><div class="process-line">{tx("Materials → Process → Interfaces → Devices → Integration","材料 → 工艺 → 界面 → 器件 → 集成",l)}</div></section>'
    s+=f'<section class="section">{section(tx("Earlier foundations","此前的研究基础",l))}<p>{tx("My earlier work spans nano-TSV optimization, advanced-packaging simulation, semiconductor sensing, nanophotonics, and wafer inspection. These experiences connect computational methods with physical devices and engineering implementation.","此前的工作涵盖 nano-TSV 优化、先进封装仿真、半导体传感、纳米光子学与晶圆检测。这些经历将计算方法、物理器件与工程实现连接起来。",l)}</p>{link(url("projects",l),tx("View selected projects","查看代表项目",l)+" ↗")}</section>'
    return s

def publications(l):return heading(tx('Publications','论文',l),tx('Research, shared.','研究与分享。',l),tx('Research in wafer inspection and industrial anomaly detection.','晶圆检测与工业异常检测中的研究工作。',l))+''.join(paper(p,l,True) for p in PAPERS)

def projects(l):
    s=heading(tx('Projects & open source','项目与开源',l),tx('Ideas made tangible.','让想法成为成果。',l),tx('Selected work across devices, simulation, intelligent hardware, and software for research.','器件、仿真、智能硬件与科研软件中的代表工作。',l))
    s+='<div class="projects-grid">'+''.join(project_card(p,l) for p in PROJECTS)+'</div>'
    s+=f'<section class="section">{section(tx("Maintained software","维护中的软件",l))}<div class="software-list"><article><h3>{link("https://github.com/CAOShurong/termscope","TermScope ↗")}</h3><p>{tx("A terminal serial plotter for live data from Arduino, ESP32, and STM32 over UART, pipes, or SSH.","终端串口绘图工具，可通过 UART、管道或 SSH 查看 Arduino、ESP32 与 STM32 的实时数据。",l)}</p></article><article><h3>{link("https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32",tx("STM32 multifunction robot car","STM32 多功能小车",l)+" ↗")}</h3><p>{tx("An embedded project combining line tracking, ultrasonic ranging, obstacle avoidance, Bluetooth control, and OLED output.","结合循迹、超声测距、避障、蓝牙控制与 OLED 显示的嵌入式项目。",l)}</p></article></div></section>'
    s+=f'<section class="section upstream" id="upstream">{section(tx("Contributing upstream","参与上游开源",l))}<div class="contribution-intro"><div class="stat"><strong>37</strong><span>{tx("merged upstream PRs","个上游已合并 PR",l)}</span></div><p>{tx("Accepted contributions across 22 external repositories, from scientific computing and laboratory data to software infrastructure.","贡献被 22 个外部仓库接纳，涉及科学计算、实验室数据与软件基础设施。",l)}<small>{tx("GitHub snapshot · 11 September 2026 · Excludes my own repositories.","GitHub 快照 · 2026 年 9 月 11 日 · 不含本人仓库。",l)}</small></p></div><div class="pr-list">'+''.join(f'<article>{link(p[1],p[0]+" ↗")}<p>{p[3 if l else 2]}</p></article>' for p in PRS)+'</div>'+link('https://github.com/search?q=author%3ACAOShurong+is%3Apr+is%3Amerged+-user%3ACAOShurong&type=pullrequests',tx('View the contribution record','查看贡献记录',l)+' ↗')+'</section>'
    return s

def project_detail(p,l):
    s=f'<div class=breadcrumbs>{link(url("",l),tx("Home","首页",l))}<span>/</span>{link(url("projects",l),tx("Projects","项目",l))}<span>/</span><span>{p["title"][l]}</span></div>'+heading(p['tag'][l],p['title'][l],p['summary'][l])
    s+='<div class="project-detail-layout">'
    if p.get('image'):s+=f'<figure class="detail-figure {p["id"]}">{img(p["image"],p["caption"][l])}<figcaption>{p["caption"][l]}</figcaption></figure>'
    s+='<div class="reading">'+''.join(f'<section><h2>{b[1 if l else 0]}</h2><p>{b[3 if l else 2]}</p></section>' for b in p['body'])+'</div>'
    s+='</div>'
    if p.get('links'):s+='<div class="text-links">'+''.join(link(u,t+' ↗') for t,u in p['links'])+'</div>'
    s+=f'<section class=related-projects><h2>{tx("Explore other projects","继续了解其他项目",l)}</h2><div>'+''.join(link(url('projects/'+q['id'],l),q['title'][l]+' ↗') for q in PROJECTS if q['id']!=p['id'])+'</div></section>'
    return s

def experience(l):
    s=heading(tx('Experience','经历',l),tx('An integrated-circuit foundation.<br>A device-focused next chapter.','以集成电路为基础，<br>走向器件与工艺。',l))
    s+=education(l)+exchanges(l)
    rows=[('', 'Research visit · HKUST(GZ)','暑期研究 · 香港科技大学（广州）','COMSOL modeling of optical neuromemristors and nano-antennas, geometry optimization, and device-characterization work.','开展光学神经忆阻器与纳米天线的 COMSOL 建模、几何结构优化和器件表征工作。'),('2024–2025','Advanced-packaging research · Nanjing University','先进封装研究 · 南京大学','Python-assisted equivalent modeling and thermo-mechanical simulation of 2.5D chip stacks with Prof. Sunan Ding.','在丁孙安教授指导下，开展 Python 辅助等效建模与 2.5D 芯片堆叠热力耦合仿真。'),('2024–2026','Industrial inspection research · Nanjing University','工业检测研究 · 南京大学','Wafer defect detection and texture anomaly detection, including FALCO-WAFER and Texture-AD.','开展晶圆缺陷检测与纹理异常检测研究，包括 FALCO-WAFER 和 Texture-AD。'),('','Academic exchange · Cambridge','硬件设计项目 · 剑桥','Team leader and commencement speaker at St Catharine’s College. Led a six-person hardware project and delivered the closing presentation.','在剑桥大学圣凯瑟琳学院项目中担任团队负责人及结业发言人，带领六人团队完成硬件项目并作结业展示。')]
    s+=f'<section class="section">{section(tx("Research & engineering experience","研究与工程经历",l))}<div class="timeline">'+''.join(f'<article><span class="date">{r[0]}</span><div><h3>{r[2 if l else 1]}</h3><p>{r[4 if l else 3]}</p></div></article>' for r in rows)+'</div></section>'
    s+=f'<section class="section">{section(tx("Selected recognition","代表性荣誉",l))}<ul class="recognition"><li><strong>{tx("National Second Prize · 2024","全国二等奖 · 2024",l)}</strong><p>{tx("FPGA Innovation Design Track Finals, 7th National College Embedded Chip and System Design Competition.","第七届全国大学生嵌入式芯片与系统设计竞赛，FPGA 创新设计赛道决赛。",l)}</p></li><li><strong>{tx("People’s Scholarship · 2023 & 2024","人民奖学金 · 2023、2024",l)}</strong><p>{tx("Nanjing University","南京大学",l)}</p></li></ul></section>'
    s+=f'<figure class="campus">{img("cuhk-campus.jpg",tx("The Chinese University of Hong Kong campus overlooking Tolo Harbour","俯瞰吐露港的香港中文大学校园",l))}<figcaption>{tx("The Chinese University of Hong Kong. Photograph: ","香港中文大学。图片来源：",l)}{link("https://www.cuhk.edu.hk/english/campus/campus.html","CUHK")}</figcaption></figure>'
    return s

def contact(l):
    return heading(tx('Contact','联系',l),tx('Let’s exchange ideas.','期待与你交流。',l),tx('For research conversations, open-source work, or engineering collaboration, email is the best way to reach me.','如需交流研究、开源工作或工程合作，欢迎通过邮件联系。',l))+f'<div class="contact-layout"><div><p class="eyebrow">{tx("Public contact","公开联系方式",l)}</p><a class="email-large" href="mailto:{EMAIL}">{EMAIL} ↗</a><p>{link("https://github.com/CAOShurong","GitHub / CAOShurong ↗")}</p><div class="institutional"><h2>{tx("Institutional email","校内邮箱",l)}</h2><p class="masked">{MASKED}</p><p>{tx("For my CUHK email address, please contact me through Gmail.","如需我的 CUHK 校内邮箱，请先通过 Gmail 联系。",l)}</p></div></div><aside><p class="eyebrow">{tx("Affiliation","所在单位",l)}</p><h2>{tx("The Chinese University of Hong Kong","香港中文大学",l)}</h2><p>{tx("Department of Electronic Engineering","电子工程学系",l)}<br>{tx("Hong Kong","香港",l)}</p></aside></div>'

def cv(l):
    s=heading('Curriculum vitae' if not l else '个人简历',tx('Shurong Cao','曹书嵘',l),tx('PhD student in Electronic Engineering · The Chinese University of Hong Kong','香港中文大学 · 电子工程博士研究生',l))
    s+=f'<div class="cv-actions">{link("/assets/Shurong-Cao-CV.pdf",tx("Open PDF · English","打开 PDF · 英文",l)+" ↗","button")}<a class="button secondary" href="/assets/Shurong-Cao-CV.pdf" download>{tx("Download CV","下载简历",l)} ↓</a></div>'
    s+=f'<section class="section">{section(tx("Education","教育",l))}{education(l)}</section>'
    s+=f'<section class="section">{section(tx("Research interests","研究兴趣",l))}<p>{tx("Semiconductor devices and fabrication; BEOL-compatible electronics; oxide and p-type semiconductors; low-temperature processing; monolithic 3D and complementary integration.","半导体器件与工艺、BEOL 兼容电子器件、氧化物与 p 型半导体、低温加工、单片三维与互补集成。",l)}</p></section>'
    s+=f'<section class="section">{section(tx("Publications","论文",l))}'+''.join(f'<article class="cv-publication"><h3>{p["title"]}</h3><p>{p["authors"]}</p><p>{p["venue"]}</p></article>' for p in PAPERS)+'</section>'
    s+=f'<section class="section">{section(tx("Selected experience","代表经历",l))}<ul class="cv-list">'+''.join(f'<li><strong>{p["title"][l]}</strong><p>{p["summary"][l]}</p></li>' for p in PROJECTS)+'</ul>'+link(url('experience',l),tx('Education, research experience & recognition','教育、研究经历与荣誉',l)+' ↗')+'</section>'
    s+=f'<section class="section">{section(tx("Contact","联系",l))}<p>{link("mailto:"+EMAIL,EMAIL)} · {link("https://github.com/CAOShurong","GitHub")}</p></section>'
    return s

def shell(path,l,body,title):
    language='zh-CN' if l else 'en'
    alt=url(path,1-l)
    nav=''
    for p,en,zh in NAV:
        current='aria-current="page"' if path.split('/')[0]==p else ''
        item=f'<a href="{url(p,l)}" {current}>{zh if l else en}</a>'
        children=[]
        if p=='research':children=[(url(p,l)+'#theme-'+r[0],r[2 if l else 1]) for r in RESEARCH]
        if p=='projects':children=[(url('projects/'+r['id'],l),r['title'][l]) for r in PROJECTS]+[(url('projects',l)+'#upstream',tx('Upstream contributions','上游开源贡献',l))]
        if p=='publications':children=[(url(p,l)+'#'+r['id'],r['short']) for r in PAPERS]
        if children:
            label=tx(en+' submenu',zh+'子菜单',l)
            item=f'<div class="nav-group">{item}<button class="submenu-toggle" aria-expanded="false" aria-controls="sub-{p}" aria-label="{label}">⌄</button><div class="submenu" id="sub-{p}">'+''.join(link(u,t) for u,t in children)+'</div></div>'
        nav+=item
    description=tx('Shurong Cao, PhD student in Electronic Engineering at CUHK. Semiconductor devices, BEOL-compatible electronics, monolithic 3D integration, and open-source engineering.','曹书嵘，香港中文大学电子工程博士研究生。探索半导体器件、BEOL 兼容工艺与单片三维集成，参与工程实践和开源协作。',l)
    return f'''<!doctype html>
<html lang="{language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#503b69"><title>{esc(title)} | {tx('Shurong Cao','曹书嵘',l)}</title><meta name="description" content="{description}"><link rel="canonical" href="{ORIGIN+url(path,l)}"><link rel="alternate" hreflang="en" href="{ORIGIN+url(path,0)}"><link rel="alternate" hreflang="zh-Hans" href="{ORIGIN+url(path,1)}"><link rel="alternate" hreflang="x-default" href="{ORIGIN+url(path,0)}"><meta property="og:title" content="{esc(title)} | Shurong Cao"><meta property="og:description" content="{description}"><meta property="og:type" content="website"><meta property="og:url" content="{ORIGIN+url(path,l)}"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css?v={ASSET_VERSION}"><script src="/app.js?v={ASSET_VERSION}" defer></script></head>
<body data-language="{language}" data-route="{path}"><a class="skip" href="#main">{tx('Skip to content','跳转到正文',l)}</a><header class="site-header"><div class="header-inner"><a class="wordmark" href="{url('',l)}">{tx('Shurong Cao','曹书嵘',l)}<span>{tx('曹书嵘','Shurong Cao',l)}</span></a><button type="button" class="menu-toggle" aria-expanded="false" aria-controls="navigation">{tx('Menu','菜单',l)} <span aria-hidden="true">☰</span></button><nav id="navigation" aria-label="{tx('Main navigation','主导航',l)}">{nav}<a href="{url('contact',l)}" {"aria-current=page" if path=='contact' else ''}>{tx('Contact','联系',l)}</a><a class="github-nav" href="https://github.com/CAOShurong">GitHub ↗</a></nav><a class="language-switch" href="{alt}" lang="{'en' if l else 'zh-CN'}" hreflang="{'en' if l else 'zh-Hans'}" aria-label="{tx('切换到中文','Switch to English',l)}">{tx('中文','EN',l)}</a></div></header><main id="main" class="container { 'home' if not path else 'inner-page'}">{body}</main><footer class="site-footer"><div class="container"><div><a class="wordmark" href="{url('',l)}">{tx('Shurong Cao','曹书嵘',l)}</a><p>{tx('Semiconductor devices · Fabrication · Integration','半导体器件 · 工艺 · 集成',l)}</p></div><div class="footer-links">{link('https://github.com/CAOShurong','GitHub ↗')}{link('mailto:'+EMAIL,tx('Email','邮件',l)+' ↗')}{link(url('contact',l),tx('Contact','联系',l))}</div><p class="copyright">© 2026 Shurong Cao · {tx('Updated September 2026','更新于 2026 年 9 月',l)}</p></div></footer></body></html>'''

def build():
    if OUT.resolve().parent != ROOT.resolve() or OUT.name != "site": raise RuntimeError("Unexpected build destination")
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir(exist_ok=True)
    shutil.copytree(ROOT/'assets',OUT/'assets',dirs_exist_ok=True)
    for f in ['style.css','app.js','favicon.svg']:shutil.copy2(ROOT/f,OUT/f)
    routes=[('',home,('Home','首页')),('research',research,('Research','研究')),('publications',publications,('Publications','论文')),('projects',projects,('Projects','项目')),('experience',experience,('Experience','经历')),('contact',contact,('Contact','联系')),('cv',cv,('CV','简历'))]
    for p in PROJECTS:routes.append(('projects/'+p['id'],lambda l,p=p:project_detail(p,l),p['title']))
    paths=[]
    for l in [0,1]:
        for path,fn,title in routes:
            target=OUT/url(path,l).strip('/');target.mkdir(parents=True,exist_ok=True)
            (target/'index.html').write_text(shell(path,l,fn(l),title[l]),encoding='utf-8')
            paths.append(ORIGIN+url(path,l))
    for p in PAPERS:(OUT/'assets'/f'{p["id"]}.bib').write_text(p['bib'],encoding='utf-8')
    (OUT/'404.html').write_text(shell('',0,heading('404','This page has moved.','Return to the homepage to continue exploring.')+link('/','Back to home →','button'),'Page not found'),encoding='utf-8')
    (OUT/'.nojekyll').touch()
    (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+ORIGIN+'/sitemap.xml\n')
    (OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in paths)+'</urlset>',encoding='utf-8')
    print(f'Built {len(paths)} bilingual routes in {OUT}')

if __name__=='__main__':build()
