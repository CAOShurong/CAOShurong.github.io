---
schema_version: portable-project-memory/v1
handoff_revision: 13
updated_at: "2026-09-11T11:47:00+08:00"
updated_by: Codex
base_revision: git:8a7d51ff497d7ba78ff2aec7ab552103690f5899
workspace_fingerprint: sha256:28bc3120a69d3f096a09e0c1eb8d8c83681632ed3c7976d5010503420abd3943
context_fingerprint: sha256:e3e57273c620d3c9f77553e486e543f564ef3848bf4ee02c0e1a5fea5f1bedf3
status: in_progress
---
# Project Handoff
## Current objective
V3.2 signature and lavender panel are locally verified; publish primary site, prominent GitHub Profile entry, and free public Sites mirror. Preserve all earlier versions.
## Confirmed state
### Completed
- Source dc51bf0 provides the V3.1 refinement; final source b8a9d5900f9ff6610ac02028bee069a9183f2388 also fixes mobile contact-email wrapping. Pages run 34557215867 successful (prior run 34556605684 successful).
- Guo Xie Birong Scholarship / 郭谢碧蓉奖学金, Nanjing University, RMB 10,000 now prioritized in home/experience/CV and the one-page public PDF. Receipt and amount supplied by owner; NJU primary source verifies spelling. No personal award year inferred.
- Large plum GitHub Profile feature, direct handle/link, actual BenchLineage/GitHub MCP Server/Astropy screenshot cards with concrete contribution descriptions. Counts are secondary. Maintainer role applies to BenchLineage, not the external upstream repos.
- Noto Sans SC self-hosted across Chinese content (565 glyphs, variable weights 400–600); Newsreader/Inter retained in English. Original curved SC vector mark and coordinated favicon.
- Gmail-first school-email contact note in EN/ZH. Institutional email remains **********@link.cuhk.edu.hk, with no private phone. Source personal documents untouched.
- Previous versions remotely preserved: v1.0.0 / archive/v1.0 at f110c82; v2.0.0 / archive/v2.0 at 48b161c; v3.0.0 / archive/v3.0 at 2dd3d6e. No history rewriting.
- All previous real paper/research figures, supplied portrait, four institution marks, exchanges without dates, research exploration wording, bilingual routes, submenus and public-safe contacts retained.
### In progress
V3.2 publication and live verification, GitHub Profile banner, and public mirror.
### Blocked
None. In-app screenshot capture became unavailable late in verification; Edge supplied the remaining visual checks successfully.
## Changed artifacts
build.py, content.py, style.css, favicon.svg, image-sizes.json, make_cv.py, public PDF, three actual GitHub screenshots, Noto Sans SC fonts/licenses, scripts/refresh_chinese_font.py, and project documentation. app.js and research/paper/portrait images unchanged.
## Verification evidence
Full-agent capability. Build/check_site (23 documents), JS syntax, git diff check passed. 22 local routes at320px and 22 live routes at390px passed edition3.1/one h1/no overflow/no failed loaded images. Actual desktop/mobile EN/ZH views, GitHub links, mobile submenu, paper modal, clipboard, language/anchor preservation, CV download/open/parse and persisted motion preference exercised. Contact mobile letter-wrap found visually, fixed, then rechecked locally at390/320 and live at390. QA.md records exact scope and source/deploy IDs. Own preview server session65592 stopped; browser viewport overrides reset.
## Decisions referenced
D-20260911-004500-pages; D-20260911-004501-content; D-20260911-030000-patent; D-20260911-083000-purple; D-20260911-100020-acadv3; D-20260911-120000-v31pol.
## Risks and unknowns
The owner's subjective aesthetic assessment remains open. Research interests remain exploratory. P-type figure remains complete, unmodified, noncommercial and attributed under CC BY-NC-ND4.0. GitHub counts are a September11 snapshot. Scholarship year not inferred. Mail delivery, physical printing and assistive-device behavior NOT_RUN.
## Next actions
1. Incorporate owner feedback within the current V3.1 direction unless they request a new design.
2. Preserve all rollback references. Restore older versions through normal commits, never deletion/history rewriting.
3. For public Chinese text changes: build, run scripts/refresh_chinese_font.py, rebuild, check all relevant typography. Use browser reload when validating a newly deployed CSS hash.
## User decisions required
None for this delivered refinement. Owner visual review remains open.
