---
schema_version: portable-project-memory/v1
handoff_revision: 6
updated_at: "2026-09-11T07:56:21+08:00"
updated_by: Codex
base_revision: git:92c28aaf1a6965efa87cb9ff8697db4c07d57483
workspace_fingerprint: sha256:aa9afca490033d93448a7f372041d57599cd7d15dc7ff1c706a04eccac572190
context_fingerprint: sha256:ea7ab683c2701f0298b839a7531df0d3a762383b28b776d8cfb7c87a4a89f8fc
status: complete
---
# Project Handoff
## Current objective
Purple, image-led bilingual academic website revision published at https://caoshurong.github.io/ for the owner's review.
## Confirmed state
### Completed
- Latest deployed source 92c28aaf1a6965efa87cb9ff8697db4c07d57483; Actions run 34544140889 successful. Previous visual source 671d5b3, run 34544094294 also successful.
- Wider plum/lilac layout. Three substantial image-led research cards and expanded detail discussions, using credited complete literature figures. License links and sources documented in ASSET_SOURCES.md.
- Homepage FALCO architecture and Texture-AD core benchmark figure; actual author order/stars retained, explicit author-position notes removed.
- Four illustrated practice projects; official CUHK/NJU crests and HKUST (Guangzhou)/Cambridge exchange logos. Exchange dates omitted, including public PDF.
- EN default and ZH counterpart routes, prominent GitHub Profile, submenus, image dialogs, citation copying and public CV download remain functional.
- Exact user portrait retained. Public Gmail only and masked university address; original private CV/PPT untouched.
### In progress
None. Owner's subjective visual acceptance is pending; do not imply endorsement.
### Blocked
None.
## Changed artifacts
build.py, content.py, style.css, app.js, image-sizes.json, favicon.svg, make_cv.py, selected assets and provenance/QA docs. ARTIFACTS.md contains current public asset hashes.
## Verification evidence
Full-agent capability. Current build.py, scripts/check_site.py (23 HTML documents), node --check app.js PASS. Local 22-route 320px and live 22-route 390px audits PASS; desktop/mobile screenshots personally inspected. Live menu, figure, language, GitHub and project navigation exercised. Public CV actually downloaded/opened and live bytes parsed. Exact details in QA.md.
## Decisions referenced
D-20260911-004500-pages; D-20260911-004501-content; D-20260911-030000-patent; D-20260911-013000-stylev2; D-20260911-083000-purple.
## Risks and unknowns
Visual approval remains the owner's judgment. Literature figures illustrate exploration and are not the owner's work. P-type figure is CC BY-NC-ND and must remain unmodified/noncommercial with attribution. GitHub metrics are a dated September 11 snapshot. Email delivery/physical printing NOT_RUN.
## Next actions
1. Incorporate the owner's next review without reverting purple palette, core figures or author-label decisions.
2. Build/check and real browser desktop/mobile verification before publishing further changes.
3. Update asset metadata/provenance if images change; refresh handoff after material changes.
## User decisions required
No credentials or publication decision pending. Await subjective review.
