---
schema_version: portable-project-memory/v1
handoff_revision: 11
updated_at: "2026-09-11T10:55:50+08:00"
updated_by: Codex
base_revision: git:2dd3d6e606b1b9a7cd65c84f22ca15a06ff7c779
workspace_fingerprint: sha256:f1ac786af89d5555f80fc96777f6b2abb57bfc563111e775c222649983b24c90
context_fingerprint: sha256:986a7f9861acabe459c2cd96903f44ca126f9792414f6d4fc87f2b5f57fcf7b8
status: active
---
# Project Handoff
## Current objective
Polish V3.1 on polish/v3.1: prioritize Guo Xie Birong Scholarship (RMB 10,000), large GitHub Profile entrance with three actual contribution screenshots, Gmail-first school-email note, Chinese typography and SC monogram. Retain V3's identity-first academic composition and all earlier versions.
## Confirmed state
### Completed
- V3 source 83e33256ab9bfda4da767423559e1826688bfc6b; Actions run 34552981770 successful. Implemented on redesign/v3 and fast-forwarded main. Compact portrait/bio opening, light purple academic palette, Newsreader/Inter typography, 119-character Noto Serif SC heading subset.
- Three illustrated research directions simultaneously visible; large authored-paper figures; education/exchange rail beside publications; full-width engineering and open-source sections.
- Actual researcher websites visually inspected: Keunhong Park, Vincent Sitzmann, Matthew Tancik, Gordon Wetzstein. Lessons and URLs in DESIGN_NOTES.md.
- V1 remotely retained as v1.0.0 / archive/v1.0 at f110c82; V2 remotely retained as v2.0.0 / archive/v2.0 at 48b161c. V2 deployed payload was source 0747236 and Actions run 34547058691.
- All content/privacy/figure requirements retained. No explicit author-position labels. Actual portrait, all four institution marks, exchange entries without dates, prominent GitHub, Gmail, masked CUHK email and public CV.
### In progress
V3.1 implementation and local checks complete. Ready to commit/publish from polish/v3.1; live verification pending. Own preview HTTP server at 127.0.0.1:8765, exec session 65592, serves only this local review; stop after live acceptance.
### Blocked
None.
## Changed artifacts
V3.1: build.py, content.py, style.css, favicon.svg, three GitHub screenshots, Noto Sans SC fonts/license, scripts/refresh_chinese_font.py, make_cv.py, public PDF, image-sizes.json and project documentation. app.js unchanged.
## Verification evidence
Full-agent capability. Current build.py, scripts/check_site.py (23 documents), node --check app.js and git diff --check PASS. 22 local browser routes at 320px passed one h1/no overflow/no failed loaded images. Personally viewed desktop/mobile EN/ZH homepage, large paper figure and modal, school marks, full-width projects, research details. Mobile project submenu, route/language/anchor switching, BibTeX copy and CV download passed. Motion pause persisted through reload and resumed. QA.md records exact scope. All 22 live routes at390px passed edition3.0/one h1/no overflow/no failed loaded images. Live GitHub Profile jump, mobile publication submenu, Texture-AD modal, Chinese citation copy, language/anchor preservation, public PDF download/open/view and motion persistence passed. Live desktop/mobile identity remains fully visible in the first viewport.
## Decisions referenced
D-20260911-004500-pages; D-20260911-004501-content; D-20260911-030000-patent; D-20260911-083000-purple; D-20260911-100000-v2design; D-20260911-100020-acadv3; D-20260911-120000-v31pol.
## Risks and unknowns
Owner aesthetic approval remains pending and must not be inferred from technical success. Research remains exploratory. CC BY-NC-ND p-type figure remains complete, unchanged and attributed on noncommercial site. GitHub counts are a September 11 snapshot. Physical assistive technology, OS reduced-motion emulation, mail delivery and physical printing NOT_RUN.
## Next actions
1. Finish desktop/mobile interaction and route checks, publish, then verify the live result.
2. V3 is also preserved remotely at v3.0.0 / archive/v3.0 (2dd3d6e). Preserve v1/v2 references.
3. Chinese now uses Noto Sans SC; run scripts/refresh_chinese_font.py after content changes and rebuild. Update asset provenance, QA and project fingerprints before completion.
## User decisions required
None for this delivered revision. Subjective visual review remains open.
