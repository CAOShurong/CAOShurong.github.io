---
schema_version: portable-project-memory/v1
handoff_revision: 5
updated_at: "2026-09-11T01:35:06+08:00"
updated_by: Codex
base_revision: git:86976883d94aedf2f9ba9b62af7b027416d8a236
workspace_fingerprint: sha256:e99a5425bff77c6edc706a5d16eb7d44a55ff1c30fb39f8e610e815acb2533f9
context_fingerprint: sha256:520681b76180f3052f27ea15f50122ca3bd76b5c1af42799f15e3ad133948cdb
status: complete
---
# Project Handoff
## Current objective
Published bilingual academic website ready for the owner's review at https://caoshurong.github.io/.
## Confirmed state
### Completed
- Prominent GitHub Profile / GitHub 主页 button in home hero and GitHub link in primary navigation; live click verified. Latest deployment: 8697688, Actions run 34508955205.
- Full EN/ZH site: 22 routes, research, papers, projects and details, experience, contact and public CV.
- Visual revision after owner rejected first pass: exact new portrait, official NJU/CUHK crests, no generic stack graphic, publication main column and academic/open-source sidebar.
- Research/publications/projects dropdowns, mobile navigation, breadcrumbs, related projects, figure modal, BibTeX copy and PDF download.
- GitHub Pages deployment 472e9f95f2925d93abe971fdbded9f2d1a0bd4e2, Actions run 34508157181 successful. Site payload only site/.
- Local 320px and live 390px route audits; actual desktop/mobile screenshots and main interactions inspected. See QA.md.
- Public Gmail only; institutional email masked. One-page PDF checked from the actual live URL. Original personal documents untouched.
### In progress
None in the implementation. Owner's subjective visual approval is still pending; do not claim they endorsed this design.
### Blocked
None.
## Changed artifacts
build.py, content.py, style.css, app.js, make_cv.py; assets/ manifest in ARTIFACTS.md. QA.md records acceptance. Source repository: https://github.com/CAOShurong/CAOShurong.github.io.
## Verification evidence
Full-agent capability. `python build.py`, `python scripts/check_site.py`, `node --check app.js`: PASS, exit 0. GitHub Actions and real published browser checks: PASS on September 11, deployed revision above. Live public PDF: one page, patent present, privacy PASS. Detailed observations in QA.md.
## Decisions referenced
D-20260911-004500-pages; D-20260911-004501-content; D-20260911-030000-patent; D-20260911-013000-stylev2.
## Risks and unknowns
External mail delivery and physical printing not run. User may request further aesthetic refinement; preserve the current factual content and privacy constraints. GitHub contribution figures are a dated September 11 snapshot, not a live counter.
## Next actions
1. Incorporate the owner's visual review if provided; current implementation is deployed and functioning.
2. Edit content.py and build.py, regenerate CV only when relevant, build/check, inspect real desktop/mobile UI, then push main for Pages deployment.
3. Refresh this handoff and artifact hashes after material changes. Never publish private source CV/PPT or unmasked university contact details.
## User decisions required
No deployment or credentials decision is pending. Visual acceptance remains the owner's judgment.
