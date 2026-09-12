"""Selected upstream acknowledgements, checked against official sources 2026-09-13."""
from html import escape

CREDITS = [
    dict(name='GitHub MCP Server', label=('Official release · v1.12.0', '官方发布记录 · v1.12.0'),
         quote='@CAOShurong made their first contribution',
         summary=('Enabled URL-based feature flags for headerless hosted connections, while preserving OAuth query handling.', '为无自定义请求头的托管连接加入 URL 功能开关，并保持 OAuth 查询参数处理的一致性。'),
         source='https://github.com/github/github-mcp-server/releases/tag/v1.12.0', pr='https://github.com/github/github-mcp-server/pull/3146',
         credit=('Named in the release’s New Contributors section.', '在该版本的 New Contributors 栏目中获得署名。')),
    dict(name='CycloneDX', label=('Official contributor directory', '官网贡献者名录'),
         quote='CAOShurong · CUHK',
         summary=('Improved XML schema loading for encoded filesystem paths in the CycloneDX Python library.', '改进 CycloneDX Python 库对编码文件路径的 XML Schema 加载处理。'),
         source='https://cyclonedx.org/participate/contributors/', pr='https://github.com/CycloneDX/cyclonedx-python-lib/pull/1028',
         credit=('Listed by account name and university in the project’s contributor directory.', '项目官网贡献者名录列出账号，并标注 CUHK。')),
    dict(name='rclone', label=('Official changelog', '官方更新日志'),
         quote='Treat UploadPart success without ETag as retryable error (CAOShurong)',
         summary=('Made S3 multipart uploads retry when a successful response omits the required ETag.', '当 S3 分块上传返回成功却缺少必要的 ETag 时，将其识别为可重试错误。'),
         source='https://rclone.org/changelog/', pr='https://github.com/rclone/rclone/pull/9823',
         credit=('The S3 changelog credits the fix directly to CAOShurong.', '官方 S3 更新记录直接署名 CAOShurong。')),
    dict(name='tox', label=('Official release history', '官方版本历史'),
         quote='by @CAOShurong · #4021',
         summary=('Provisioned the requested tox version before reading env_list, allowing newer configuration syntax to work correctly.', '在读取 env_list 之前准备所需的 tox 版本，使新版本配置语法能够正确解析。'),
         source='https://tox.wiki/en/latest/changelog.html', pr='https://github.com/tox-dev/tox/issues/4021',
         credit=('The project’s release history names the contributor alongside the fix.', '项目版本历史在修复条目中标注贡献者账号。')),
]

CREDITS.extend([
    dict(name='Plotly.js', label=('Official changelog · two acknowledgements', '官方更新日志 · 两处致谢'),
         quote='with thanks to @CAOShurong for the contribution!',
         summary=('Fixed numeric color ordering in parallel-categories bundles and clarified axis spike behavior across hover modes.', '修复平行类别图中数值颜色的排序，并明确不同悬停模式下坐标轴尖峰线的行为。'),
         source='https://github.com/plotly/plotly.js/blob/main/CHANGELOG.md', pr='https://github.com/plotly/plotly.js/pull/7959',
         extra='https://github.com/plotly/plotly.js/pull/7981',
         credit=('Two changelog entries credit these contributions by account name.', '两条更新记录直接署名账号，分别对应数值排序修复与文档改进。')),
    dict(name='Syft', label=('Official release · v1.51.1', '官方发布记录 · v1.51.1'),
         quote='detect multi-arch ingress-nginx · #5179 @CAOShurong',
         summary=('Extended binary detection for multi-architecture ingress-nginx, improving software identification in generated SBOMs.', '扩展多架构 ingress-nginx 的二进制识别，改善软件物料清单中的组件识别。'),
         source='https://github.com/anchore/syft/releases/tag/v1.51.1', pr='https://github.com/anchore/syft/pull/5179',
         credit=('The release names CAOShurong beside the merged fix.', '正式发布记录在已合并的修复旁标注 CAOShurong。')),
    dict(name='TheELNFileFormat', label=('Upstream example · BenchLineage', '上游收录示例 · BenchLineage'),
         quote='examples/BenchLineage',
         summary=('Contributed a reproducible BenchLineage exchange archive demonstrating the mapping from research provenance to the ELN file format.', '贡献可复现的 BenchLineage 交换档案示例，展示科研溯源信息与 ELN 文件格式之间的映射。'),
         source='https://github.com/TheELNConsortium/TheELNFileFormat/tree/master/examples/BenchLineage', pr='https://github.com/TheELNConsortium/TheELNFileFormat/pull/152',
         credit=('The official repository hosts the example and links to BenchLineage, its documentation and package.', '官方仓库直接收录示例，并链接至 BenchLineage 仓库、文档与软件包。')),
])
CREDITS.append(dict(name='eLabFTW', label=('Upstream integration test', '上游集成测试'),
    quote='testImportBenchLineage',
    summary=('Added a BenchLineage archive to the electronic lab notebook’s import tests, covering experiment creation and 20 linked uploads.', '将 BenchLineage 档案纳入电子实验记录平台的导入测试，覆盖实验创建与 20 个关联附件。'),
    source='https://github.com/elabftw/elabftw/blob/master/tests/unit/Import/ElnTest.php',
    pr='https://github.com/elabftw/elabftw/pull/7267',
    credit=('The merged test and fixture are retained in the project’s official repository.', '已合并的测试与示例档案保留在项目官方仓库中。')))
# Official directory, published release, reusable scientific-software examples.
CREDITS = [CREDITS[i] for i in (1,0,6,7,4,5,2,3)]

def cards(language, full=True):
    out='<div class="credit-grid credit-featured">'
    selected=CREDITS if full else [CREDITS[i] for i in (0,1,2,4)]
    for n,c in enumerate(selected,1):
        if full and n==3:
            out+='</div><div class="section-title ledger-title"><h2>'+('Upstream work' if not language else '上游贡献')+'</h2></div><div class="credit-ledger">'
        record=f'<div class="credit-record"><span class="credit-record-label">{"Project record" if not language else "项目方记录"}</span><blockquote>{escape(c["quote"])}</blockquote><p>{c["credit"][language]}</p></div>' if full and n<3 else f'<p class="credit-proof">{c["credit"][language]}</p>'
        more=f'<a href="{c["extra"]}">{"Second contribution" if not language else "另一项贡献"} ↗</a>' if full and c.get('extra') else ''
        out+=f'''<article class="credit-card"><div class="credit-heading"><div class="credit-card-top"><span class="credit-number">{n:02}</span><span class="eyebrow">{c['label'][language]}</span></div><h3><a href="{c['source']}">{c['name']} ↗</a></h3></div><div class="credit-body"><p class="credit-summary">{c['summary'][language]}</p>{record}</div><div class="credit-links"><a href="{c['source']}">{'Official record' if not language else '官方记录'} ↗</a><a href="{c['pr']}">{('Related issue' if not language else '相关问题') if c['name']=='tox' else ('Contribution' if not language else '查看贡献')} ↗</a>{more}</div></article>'''
    return out+'</div>'
