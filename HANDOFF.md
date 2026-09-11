---
schema_version: portable-project-memory/v1
handoff_revision: 9
updated_at: "2026-09-11T10:06:13+08:00"
updated_by: Codex
base_revision: git:83e33256ab9bfda4da767423559e1826688bfc6b
workspace_fingerprint: sha256:540eff59d3b84f29c8fa48bb5a6fb81a6062e175f7a4cb704428c1a1ae1741b6
context_fingerprint: sha256:d2a717bd0df708c8a762c9b54c55877cfbd4bc0beaca53504b7e69cac6d26499
status: complete
---
# Project Handoff
## Current objective
Version 3 is published and live-verified at https://caoshurong.github.io/. Owner rejected V2's full-screen image and product-like hierarchy. Identity, PhD role, research and contacts must be visible immediately. Retain earlier versions for rollback.
## Confirmed state
### Completed
- V3 source 83e33256ab9bfda4da767423559e1826688bfc6b; Actions run 34552981770 successful. Implemented on redesign/v3 and fast-forwarded main. Compact portrait/bio opening, light purple academic palette, Newsreader/Inter typography, 119-character Noto Serif SC heading subset.
- Three illustrated research directions simultaneously visible; large authored-paper figures; education/exchange rail beside publications; full-width engineering and open-source sections.
- Actual researcher websites visually inspected: Keunhong Park, Vincent Sitzmann, Matthew Tancik, Gordon Wetzstein. Lessons and URLs in DESIGN_NOTES.md.
- V1 remotely retained as v1.0.0 / archive/v1.0 at f110c82; V2 remotely retained as v2.0.0 / archive/v2.0 at 48b161c. V2 deployed payload was source 0747236 and Actions run 34547058691.
- All content/privacy/figure requirements retained. No explicit author-position labels. Actual portrait, all four institution marks, exchange entries without dates, prominent GitHub, Gmail, masked CUHK email and public CV.
### In progress
None in implementation. Awaiting owner visual review.
### Blocked
None.
## Changed artifacts
build.py, style.css, app.js, Newsreader and Noto Serif SC font assets, ASSET_SOURCES.md, ARTIFACTS.md, DESIGN_NOTES.md, PROJECT_CONTEXT.md, DECISIONS.md, QA.md and this handoff.
## Verification evidence
Full-agent capability. Current build.py, scripts/check_site.py (23 documents), node --check app.js and git diff --check PASS. 22 local browser routes at 320px passed one h1/no overflow/no failed loaded images. Personally viewed desktop/mobile EN/ZH homepage, large paper figure and modal, school marks, full-width projects, research details. Mobile project submenu, route/language/anchor switching, BibTeX copy and CV download passed. Motion pause persisted through reload and resumed. QA.md records exact scope. All 22 live routes at390px passed edition3.0/one h1/no overflow/no failed loaded images. Live GitHub Profile jump, mobile publication submenu, Texture-AD modal, Chinese citation copy, language/anchor preservation, public PDF download/open/view and motion persistence passed. Live desktop/mobile identity remains fully visible in the first viewport.
## Decisions referenced
D-20260911-004500-pages; D-20260911-004501-content; D-20260911-030000-patent; D-20260911-083000-purple; D-20260911-100000-v2design; D-20260911-100020-acadv3.
## Risks and unknowns
Owner aesthetic approval remains pending and must not be inferred from technical success. Research remains exploratory. CC BY-NC-ND p-type figure remains complete, unchanged and attributed on noncommercial site. GitHub counts are a September 11 snapshot. Physical assistive technology, OS reduced-motion emulation, mail delivery and physical printing NOT_RUN.
## Next actions
1. Incorporate the owner's next visual assessment without losing facts, imagery, privacy or rollback references.
2. Preserve v1/v2 tags and archive branches; restore through normal commits if requested.
3. Before future publication, build/check and inspect affected routes in the real browser. Extend the Chinese heading subset for new glyphs.
## User decisions required
None for this delivered revision. Subjective visual review remains open.
