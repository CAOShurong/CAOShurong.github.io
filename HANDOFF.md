---
schema_version: portable-project-memory/v1
handoff_revision: 18
updated_at: "2026-09-13T00:55:00+08:00"
updated_by: Codex
base_revision: git:f4ebe069ec75a011c79d624eaec385af1b9c01f8
workspace_fingerprint: sha256:a0f9bdb02f3e0292816e8447b2877a70177e54f2d6bfc97dc5e77d9d77e49ca0
context_fingerprint: sha256:d0d745e6c654b4f0598a30ffc32f9a2c0341e6b45f52ffd103080892aa270b44
status: complete
---
# Project Handoff
## Current objective
The owner accepted V3.3 as final, then requested a small header correction: remove the three separate dropdown buttons/menus, keep direct page links. Both hosts now publish this correction and search metadata. No redesign is pending.
## Confirmed state
- Primary source 8fa92317f6dff89106ff90de85b07a0c82b9d7ab, successful Pages run 34706518131. Search metadata source decd871.
- Mirror source 6ec5221c132eca55a8ab78180f82f55ef21b1e50; existing public project appgprj_6aa3766f6b8481919bde2fee13651b01; successful deployment appgdep_6aa583645f2c8191a9650c97c8d0019e. Primary https://caoshurong.github.io/; mirror https://caoshurong.caoshurongg.chatgpt.site/.
- Profile README source353a541 adds bilingual heading/explicit homepage link; actual click reaches primary. Account display-name save initially succeeded but final API/UI show ShurongCAO; do not overwrite subsequent edits or claim bilingual account name.
- Independent D:/CAOShurong-Website-Backup/2026-09-13-approved-v3.3 snapshot preserves eb094086 source and 224 validated hashes, static primary/mirror, Profile and self-contained Git history. Final search/navigation snapshot is the sibling 2026-09-13-final-v3.3.1; inspect BACKUP.json for exact source.
- Earlier V1/V2/V3/V3.1/V3.2/V3.3 rollback references remain; no history rewrite. Final release uses v3.3.1/archive/v3.3.1.
## Search evidence
Bing property verified; sitemap submitted, Processing with zero errors/warnings. Root was Discovered but not crawled; Chinese root Not discovered. Requested indexing for both and observed Indexing requested. Bing Live URL test for Chinese root: URL can be indexed, no SEO/GEO issues, two markup types. IndexNow22 URLs returned202, key validation pending. Actual indexing/rank remains pending; no first-place guarantee. Google Console NOT_RUN. Full evidence and IDs: SEARCH_VISIBILITY.md.
## Verification evidence
Full-agent. Build/check_site23 documents, check_search22 routes on primary/mirror, diff check passed. All23 main regions identical to approved backup; only navigation and search head changed. Actual D-backed homepage/research/language journey passed. Actual local direct Research/Publications/Projects clicks and corresponding Chinese route passed. Live primary Research/Projects and mirror Chinese Research verified. Header and mirror screenshots inspected. Cached old primary page resolved with normal reload. Fresh mobile, email delivery and printing NOT_RUN. A supplementary urllib sweep hit403, not counted as success; browser and Bing live fetch succeeded.
## Durable constraints
Retain masked university email, Gmail-first contact, actual portrait/figures and full attributions, scholarship without invented year, exploratory research wording, author order/stars without role labels. No private CV/email/phone/credentials in repository. Public verification meta/key file are intentionally public.
## Archival note
DESIGN_NOTES.md and the old ignored external-file design preview are archival. Browser previously prohibited workaround access to that draft; do not serve it indirectly. Final acceptance supersedes exploration as next task.
## Next actions
No implementation pending. After search processing, reinspect root and /zh/ using Bing Webmaster Tools if requested; use fresh exclusion reason before further changes. Maintain primary canonical on mirror. No automation requested.
## Decisions referenced
D-20260913-005000-finalseo; D-20260913-005400-navlink; prior factual/privacy decisions remain effective.

## Changed artifacts
seo.py, build.py, app.js, style.css, indexing/, scripts/check_search.py, scripts/sync_mirror.py, README.md and project documentation. Mirror static output and Profile README updated.
## Risks and unknowns
Search engine processing and ranking remain external and pending. Fresh mobile interaction verification was unavailable. Preserve the latest account display name rather than overwriting possible parallel edits.
## User decisions required
None for completed backup/navigation/search submissions.
