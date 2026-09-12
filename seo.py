"""Search metadata for the approved bilingual academic site (no visual changes)."""
import json
from html import escape

ORIGIN = 'https://caoshurong.github.io'
NAME = 'Shurong Cao'
DESCRIPTIONS = {
    '': (
        'Shurong Cao (曹书嵘 / CAOShurong), PhD student in Electronic Engineering at CUHK. Academic homepage: semiconductor devices, BEOL, monolithic 3D integration, publications and open-source projects.',
        '曹书嵘（Shurong Cao / CAOShurong）的个人学术主页。香港中文大学电子工程博士研究生，探索半导体器件、BEOL 低温工艺与单片三维集成，展示论文、工程项目及开源工作。'),
    'research': ('Research interests of Shurong Cao (曹书嵘): BEOL-compatible devices, p-type oxide semiconductors, low-temperature fabrication and monolithic 3D integration at CUHK.', '曹书嵘 Shurong Cao 的研究兴趣：BEOL 兼容器件、p 型氧化物半导体、低温工艺与单片三维集成。香港中文大学电子工程博士研究生。'),
    'publications': ('Publications by Shurong Cao (曹书嵘), including FALCO-WAFER and Texture-AD. Paper figures, abstracts, original sources and BibTeX citations.', '曹书嵘 Shurong Cao 的学术论文：FALCO-WAFER 与 Texture-AD。查看论文核心图、摘要、原文链接和引用信息。'),
    'projects': ('Research and engineering projects by Shurong Cao (曹书嵘): advanced packaging, vacuum MOSFET sensing, FPGA robotics, BenchLineage and upstream open-source contributions.', '曹书嵘 Shurong Cao 的研究与工程项目：先进封装、真空 MOSFET 传感、FPGA 机器人、BenchLineage 及上游开源贡献。'),
    'experience': ('Education and experience of Shurong Cao (曹书嵘): CUHK PhD studies, Nanjing University, academic exchanges and selected recognition.', '曹书嵘 Shurong Cao 的教育与学术经历：香港中文大学博士阶段、南京大学本科、香港科技大学（广州）和剑桥大学交流，以及代表荣誉。'),
    'cv': ('Curriculum vitae of Shurong Cao (曹书嵘), CUHK Electronic Engineering PhD student. Education, research, publications, engineering experience and downloadable CV.', '曹书嵘 Shurong Cao 的个人简历。香港中文大学电子工程博士研究生；教育背景、科研论文、工程经历及公开简历下载。'),
    'contact': ('Contact Shurong Cao (曹书嵘) for research conversations, engineering collaborations and open-source ideas. Public email and GitHub profile.', '联系曹书嵘 Shurong Cao：研究交流、工程合作与开源协作。公开邮箱及 GitHub 主页。'),
}

def path_url(path, language):
    return ORIGIN + ('/zh/' if language else '/') + (path.strip('/')+'/' if path else '')

def metadata(path, language, title, *, not_found=False):
    page_url = path_url(path, language)
    page_title = (('曹书嵘 Shurong Cao | 香港中文大学 · 个人学术主页' if language else
                   'Shurong Cao (曹书嵘) | CUHK · Academic Homepage') if not path else
                  f'{title} | Shurong Cao · 曹书嵘')
    description = DESCRIPTIONS.get(path, (
        f'{title} — a research and engineering project by Shurong Cao (曹书嵘). Background, methods, contributions and related resources.',
        f'{title}——曹书嵘 Shurong Cao 的研究与工程项目，介绍背景、方法、个人贡献及相关资料。'))[language]
    if not_found:
        return '<title>Page not found | Shurong Cao</title><meta name="robots" content="noindex,follow">'
    tags = [f'<title>{escape(page_title)}</title>',
            f'<meta name="description" content="{escape(description, quote=True)}">',
            '<meta name="robots" content="index,follow,max-image-preview:large">',
            f'<link rel="canonical" href="{page_url}">']
    if not path:
        tags.append('<meta name="msvalidate.01" content="F8FC7CA55063C3FC824C4AF31CC5FBCF">')
    for lang, target in [('en',0),('zh-Hans',1),('x-default',0)]:
        tags.append(f'<link rel="alternate" hreflang="{lang}" href="{path_url(path,target)}">')
    for prop, value in {'og:title':page_title, 'og:description':description,
                        'og:type':'profile' if not path else 'website', 'og:url':page_url,
                        'og:site_name':'Shurong Cao · 曹书嵘',
                        'og:image':ORIGIN+'/assets/portrait-2026.jpg',
                        'og:image:alt':'Shurong Cao / 曹书嵘',
                        'og:locale':'zh_CN' if language else 'en_US'}.items():
        tags.append(f'<meta property="{prop}" content="{escape(value,quote=True)}">')
    person={'@type':'Person','@id':ORIGIN+'/#person','name':NAME,
            'alternateName':['曹书嵘','CAO Shurong','CAOShurong'],
            'url':ORIGIN+'/', 'image':ORIGIN+'/assets/portrait-2026.jpg',
            'jobTitle':'PhD student in Electronic Engineering',
            'affiliation':{'@type':'CollegeOrUniversity','name':'The Chinese University of Hong Kong','url':'https://www.cuhk.edu.hk/'},
            'alumniOf':{'@type':'CollegeOrUniversity','name':'Nanjing University','url':'https://www.nju.edu.cn/'},
            'sameAs':['https://github.com/CAOShurong']}
    website={'@type':'WebSite','@id':ORIGIN+'/#website','url':ORIGIN+'/',
             'name':'Shurong Cao · 曹书嵘','alternateName':'CAOShurong Academic Homepage','inLanguage':['en','zh-Hans']}
    page={'@type':'ProfilePage' if path in ('','cv') else 'WebPage',
          '@id':page_url+'#webpage','url':page_url,'name':page_title,'description':description,
          'inLanguage':'zh-Hans' if language else 'en','isPartOf':{'@id':ORIGIN+'/#website'},
          'about':{'@id':ORIGIN+'/#person'}}
    if path in ('','cv'):page['mainEntity']={'@id':ORIGIN+'/#person'}
    data=json.dumps({'@context':'https://schema.org','@graph':[website,person,page]},ensure_ascii=False).replace('<','\\u003c')
    tags.append(f'<script type="application/ld+json">{data}</script>')
    return ''.join(tags)
