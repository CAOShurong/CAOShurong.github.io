---
schema_version: portable-project-memory/v1
handoff_revision: 16
updated_at: "2026-09-11T14:22:41+08:00"
updated_by: Codex
base_revision: git:a3b6e998475dde9227deed9b0ef0139780266832
workspace_fingerprint: sha256:79e4d61e08e78cc9cca847887b173b31d14cc5303e9336c942061105b05a502b
context_fingerprint: sha256:134955078372e2242fa3614df8b188ce6bea1b63e3f4660d3a8302b992914c20
status: complete
---
# Project Handoff
## Current objective
V3.3 direct-link refinement is published on both existing public hosts. The owner likes the current homepage; preserve it and all old rollback versions. The request to explore better structure/palette and less monotonous subpages is documented as a proposal, not a shipped redesign. The owner explicitly means destination pages by second-level content.
## Confirmed state
### Completed
- Primary https://caoshurong.github.io/: source a3b6e998475dde9227deed9b0ef0139780266832; Pages 34569001315 succeeded.
- Linked bilingual identity to CV, PhD role/research terms to matching research sections, affiliation/supervisor to official sites, paper titles to DOI/arXiv, and education/exchange content to official institutions. Education card overlay preserves separate supervisor keyboard access. Existing dropdown arrows are clearer.
- Preserved Allura CAOShurong signature, pale GitHub feature, compact academic layout, real imagery and all factual/privacy constraints.
- Public mirror https://caoshurong.caoshurongg.chatgpt.site/: source 4e2d6e055ebff3159a905992312d7aaabeb2618e; Sites version 2 and successful deployment appgdep_6aa39c6bc284819183d674f0ceb48f8d. Full IDs in QA.md. Exact project remains appgprj_6aa3766f6b8481919bde2fee13651b01 with static out/. Source credentials not persisted.
- GitHub Profile ../caoshurong remains f29637c with its prominent homepage banner and account website. No profile changes this revision.
- V1/V2/V3/V3.1/V3.2 remain remotely retained. V3.2=v3.2.0/archive/v3.2 at 3ea4904; V3.3=v3.3.0/archive/v3.3 at 399865a. Restore through ordinary commits, never history rewriting.
### Design exploration
- DESIGN_NOTES.md proposes near-white surfaces/dark-purple hierarchy; chapter/question-led research, year/figure/result-led papers, and contribution-led project cases. No replacement palette/layout selected or published.
- Ignored work/make_design_exploration.py generated an English comparison at E:/Codex/Workspaces/Dated/2026-09-11/fancy-github/outputs/design-exploration/preview.html. It remains unverified and separate from site/. The browser rejected the file URL and prohibited workaround access. Do not serve or open it indirectly to circumvent that rejection.
### Blocked
No blocker for the published link scope. Fresh responsive verification was unavailable: viewport set returned success while actual width remained 3432px; overrides reset. Do not claim current mobile acceptance based on historical V3.2 results.
## Changed artifacts
build.py, style.css, DESIGN_NOTES.md, DECISIONS.md, PROJECT_CONTEXT.md, QA.md and this handoff. Mirror README.md and generated out/ synchronized. No public images, fonts, PDFs, profile content, or private source documents changed.

## Verification evidence
Full-agent capability. Build/check_site23 documents and diff check passed. Actual local EN/ZH links, arXiv title, institution entry center click, supervisor keyboard navigation, and submenu expansion tested. FALCO DOI was intercepted by existing Zotero proxy and reached CUHK library login; no settings changed or authenticated publisher access claimed. Primary live keyword and corresponding-language anchor tested. Mirror live name-to-CV and Chinese keyword-to-section tested. Primary EN and mirror ZH homepage screenshots inspected. Eight anonymous HTTP checks across both origins passed with edition 3.3 and original paper links. QA.md records exact limits.
## Decisions referenced
D-20260911-004500-pages; D-20260911-004501-content; D-20260911-030000-patent; D-20260911-083000-purple; D-20260911-100020-acadv3; D-20260911-120000-v31pol; D-20260911-114600-v32sign; D-20260911-141200-v33links.
## Risks and unknowns
Aesthetic selection remains the owner's. The external-file design draft is not visually accepted. Browser evaluate became inconsistent with mirror snapshots; use documented semantic/AX interactions and normal screenshots. Research remains exploratory. P-type figure stays complete, unmodified, noncommercial and source/license linked. No scholarship year inferred. Full institutional address/private phone must never be public. Mail delivery, printing and physical assistive hardware NOT_RUN.
## Next actions
1. Incorporate owner feedback on the separate subpage/palette proposals; preserve current accepted homepage and all old versions.
2. After source edits: build/check, publish primary through Pages. Sync mirror using scripts/sync_mirror.py CHECKOUT --origin https://caoshurong.caoshurongg.chatgpt.site; commit/push/package and publish the existing Sites project. Use static out/ and Git Bash /e/ paths.
3. Refresh Noto Sans SC subset for public Chinese text changes and visually inspect. Never add private source documents or credentials to either repository.
## User decisions required
No decision needed for the completed link release. Design alternatives remain proposals for further discussion.
