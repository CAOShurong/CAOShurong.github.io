---
schema_version: portable-project-memory/v1
handoff_revision: 8
updated_at: "2026-09-11T10:01:01+08:00"
updated_by: Codex
base_revision: git:48b161c29a5025a0bc285901d335b9b91e7fcdc8
workspace_fingerprint: sha256:41dbf89fec42988257314e644031caa4ebf0c82c8a9fa67081ca7f98c991970d
context_fingerprint: sha256:56c1b4d3b305f7bf11c3ef01babb821eef602c3b841f7701900fa1f82115b049
status: active
---
# Project Handoff
## Current objective
Publish and live-verify version 3 at https://caoshurong.github.io/. Owner rejected V2's full-screen image and product-like hierarchy. Identity, PhD role, research and contacts must be visible immediately. Retain earlier versions for rollback.
## Confirmed state
### Completed
- V3 implementation on redesign/v3. Compact portrait/bio opening, light purple academic palette, Newsreader/Inter typography, 119-character Noto Serif SC heading subset.
- Three illustrated research directions simultaneously visible; large authored-paper figures; education/exchange rail beside publications; full-width engineering and open-source sections.
- Actual researcher websites visually inspected: Keunhong Park, Vincent Sitzmann, Matthew Tancik, Gordon Wetzstein. Lessons and URLs in DESIGN_NOTES.md.
- V1 remotely retained as v1.0.0 / archive/v1.0 at f110c82; V2 remotely retained as v2.0.0 / archive/v2.0 at 48b161c. V2 payload source 0747236 and Actions run 34547058691 remain currently deployed.
- All content/privacy/figure requirements retained. No explicit author-position labels. Actual portrait, all four institution marks, exchange entries without dates, prominent GitHub, Gmail, masked CUHK email and public CV.
### In progress
Final local layout review complete; commit, deploy and live acceptance next. Preview server session 93372 on 127.0.0.1:8765, serves site/, only for this task and must stop after live acceptance.
### Blocked
None.
## Changed artifacts
build.py, style.css, app.js, Newsreader and Noto Serif SC font assets, ASSET_SOURCES.md, ARTIFACTS.md, DESIGN_NOTES.md, PROJECT_CONTEXT.md, DECISIONS.md, QA.md and this handoff.
## Verification evidence
Full-agent capability. Current build.py, scripts/check_site.py (23 documents), node --check app.js and git diff --check PASS. 22 local browser routes at 320px passed one h1/no overflow/no failed loaded images. Personally viewed desktop/mobile EN/ZH homepage, large paper figure and modal, school marks, full-width projects, research details. Mobile project submenu, route/language/anchor switching, BibTeX copy and CV download passed. Motion pause persisted through reload and resumed. QA.md records exact scope; live V3 checks pending.
## Decisions referenced
D-20260911-004500-pages; D-20260911-004501-content; D-20260911-030000-patent; D-20260911-083000-purple; D-20260911-100000-v2design; D-20260911-100020-acadv3.
## Risks and unknowns
Owner aesthetic approval remains pending and must not be inferred from technical success. Research remains exploratory. CC BY-NC-ND p-type figure remains complete, unchanged and attributed on noncommercial site. GitHub counts are a September 11 snapshot. Physical assistive technology, OS reduced-motion emulation, mail delivery and physical printing NOT_RUN.
## Next actions
1. Commit V3, fast-forward main and push. Await actual GitHub Pages success.
2. Inspect live EN/ZH desktop/mobile, all routes at390px, core navigation/GitHub/image/CV path.
3. Record deployment SHA/run and live QA; update handoff revision/fingerprints; stop own preview server, reset viewport, show deliverable.
## User decisions required
None for authorized implementation and publishing. Subjective visual review follows delivery.
