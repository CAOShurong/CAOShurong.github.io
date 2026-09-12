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

def cards(language):
    out='<div class="credit-grid">'
    for n,c in enumerate(CREDITS,1):
        out+=f'''<article class="credit-card"><div class="credit-card-top"><span class="credit-number">0{n}</span><span class="eyebrow">{c['label'][language]}</span></div><h3>{c['name']}</h3><p class="credit-summary">{c['summary'][language]}</p><div class="credit-record"><span class="credit-record-label">{'Project record' if not language else '项目方记录'}</span><blockquote>{escape(c['quote'])}</blockquote><p>{c['credit'][language]}</p></div><div class="credit-links"><a href="{c['source']}">{'Official acknowledgement' if not language else '查看官方署名'} ↗</a><a href="{c['pr']}">{('Related issue' if not language else '相关问题') if c['name']=='tox' else ('Contribution' if not language else '查看贡献')} ↗</a></div></article>'''
    return out+'</div>'
