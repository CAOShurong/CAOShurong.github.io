---
schema_version: portable-project-memory/v1
handoff_revision: 14
updated_at: "2026-09-11T11:57:16+08:00"
updated_by: Codex
base_revision: git:737f58ea67cf54882d67ca93e41d2b6806394fe7
workspace_fingerprint: sha256:49da1b336416ab692ac560a28e4334fdd6dbfa1c5089413d002cc6a2611bd627
context_fingerprint: sha256:e3e57273c620d3c9f77553e486e543f564ef3848bf4ee02c0e1a5fea5f1bedf3
status: complete
---
# Project Handoff
## Current objective
V3.2 requested polish is published at https://caoshurong.github.io/ and the free public mirror https://caoshurong.caoshurongg.chatgpt.site/. GitHub Profile prominently links to the primary homepage. Preserve this accepted composition and all prior versions.
## Confirmed state
### Completed
- Primary website source737f58ea67cf54882d67ca93e41d2b6806394fe7; Pages34559744576 succeeded.
- Dark-purple cursive CAOShurong header link replaces SC and adjacent duplicate name. Self-hosted Allura; pale lavender large GitHub Profile feature with dark text. Small SC favicon unchanged.
- Profile repo ../caoshurong at f29637c adds a linked SVG banner above all existing README content. Public account website now https://caoshurong.github.io/, saved in real GitHub UI and verified through API.
- Separate Sites checkout ../academic-website-mirror, manifest project_id appgprj_6aa3766f6b8481919bde2fee13651b01, static out/. Mirror source e57f11f1925cc3d6dc2454cae402acd31cfb6cb8; deployment appgdep_6aa37aa5327481919c29d5cc91774379 succeeded with public audience. Full version ID and checks in QA.md. Credentials are not persisted.
- Earlier V1/V2/V3/V3.1 remotely retained as version tags and archive branches. V3.1=v3.1.0/archive/v3.1 at8a7d51f. Restore through normal commits; no history rewriting.
- Existing factual/privacy/imagery constraints preserved: Gmail-first contact, masked university address, Guo Xie Birong Scholarship RMB10,000, gray-jacket portrait, four institution marks, date-free exchanges, exploratory research, real paper figures/authors without position emphasis, bilingual routes and detail menus.
### In progress
None. All requested public changes and relevant real-user journeys are complete.
### Blocked
None.
## Changed artifacts
build.py, style.css, Allura font/CSS/license, scripts/sync_mirror.py and project documentation. Profile README.md/assets/website-link.svg and website field; separate registered static mirror checkout. Research content and private source documents unchanged.
## Verification evidence
Full-agent capability. Build/check_site23 documents and git diff check passed. Local signature/navigation checks at320/390/1024/1280px; actual Chinese submenu and home-link clicks. Live primary EN/ZH home/research and GitHub roundtrip verified. Profile8 tests passed and top banner visually seen. Mirror22 routes and critical assets respond without login; real desktop/mobile menu, language, paper dialog, CV download and desktop PDF view passed. QA.md records exact limits and deployment IDs.
## Decisions referenced
D-20260911-004500-pages; D-20260911-004501-content; D-20260911-030000-patent; D-20260911-083000-purple; D-20260911-100020-acadv3; D-20260911-120000-v31pol; D-20260911-114600-v32sign.
## Risks and unknowns
Aesthetic judgment remains the owner's. Research remains exploratory; metrics are dated snapshots. P-type figure stays complete/unmodified/noncommercial and attributed under CC BY-NC-ND4.0. No scholarship year inferred. Future mirror updates are explicit sync/publish operations, not automatic. Python default User-Agent is blocked by Cloudflare1010 on mirror; browser access works. Mail delivery/physical printing/assistive hardware NOT_RUN.
## Next actions
1. Incorporate new owner feedback without losing earlier constraints or rollback references.
2. Primary: build/check, publish via Pages. Mirror: run scripts/sync_mirror.py CHECKOUT --origin https://caoshurong.caoshurongg.chatgpt.site then review, commit/push and publish existing Sites project using sites-hosting. Never recreate the site. Use static out/ and Git Bash /e/ paths with package-site.sh.
3. Refresh Noto Sans SC subset for public Chinese text changes; rebuild and visually verify. Do not place private source docs or credentials in any repo.
## User decisions required
None for the completed scope.
