---
schema_version: portable-project-memory/v1
project_name: CAO Shurong academic website
updated_at: "2026-09-11T10:01:01+08:00"
---
# Project Context
## Objective
Complete bilingual academic website at https://caoshurong.github.io, authorized by user on 2026-09-11 (Just do it, 开始吧). High-quality, real browser verification required before completion. User reviews in morning; do not artificially delay or claim unverified completion.
## Deliverables
English default, full Chinese equivalent, corresponding route switching and remembered language. Home, research, publications, project details, education/experience, public CV and contact. Actual paper figures and selected project visuals. Latest user supplied gray-jacket portrait; official NJU/CUHK crests and HKUST (Guangzhou)/Cambridge exchange logos, without exchange dates; no generic vertical-integration hero. Three simultaneously illustrated research directions, large publication figures, full-width engineering project grid, education/exchange side rail and explicit dropdown navigation. NJU undergraduate to CUHK PhD progression. Maintainer and upstream contributor identity. Public-safe downloadable CV. Real local and live browser acceptance. Portable project handoff.
## Scope and non-goals
Version 3 is a compact identity-first academic redesign informed by actual researcher websites: real portrait, PhD identity, research summary and contact actions within the first viewport; light purple palette, readable serif headings, scientific figures, publications beside an academic side rail, and modest purposeful motion. Versions 1 and 2 are retained as tags v1.0.0/v2.0.0 and branches archive/v1.0/archive/v2.0. No invented reference portraits/papers/dates. No unrelated visual gimmicks, irrelevant badges, empty controls or fake metrics. No paid service. Original documents untouched. Do not modify other repos.
## Project map
build.py/content.py generate site/. assets/ holds selected public images/PDF. scripts/ validation. Root Markdown holds project handoff. Raw personal source documents stay outside repository.
## Commands and verification
Build: Python build.py. Preview: python -m http.server 8765 --bind 127.0.0.1 --directory site. Deploy site/ via GitHub Actions Pages. Use real browser checks desktop/mobile, language, links, details, CV, reload and published site. Privacy scan all public source and PDFs.
## Constraints
Payloads on E:. Public contact only shurongcao0819@gmail.com. Institutional email displayed literally **********@link.cuhk.edu.hk; full local part must never be in source, links, metadata, PDF or git history. No phone. New public CV replaces old inaccurate/private version. Source truth is latest user corrections over old CV.
## Data and provenance
CUHK EE PhD year one, Prof. Ni Zhao, exploring BEOL/M3D/low-temperature/p-type oxide/complementary devices, not a fixed dissertation nor demonstrated ALD/CVD proficiency. NJU B.Eng. Integrated Circuit and System Design 2022–2026. FALCO-WAFER co-first author, IEEE ITC-Asia2025 pp43–47, DOI 10.1109/ITC-Asia67627.2025.00016; 90.7% AP@0.5,7.19% FNR,13.3M parameters,5723 images. Texture-AD arXiv2409.06367 fourth author; CVM2026 is same work. Latest presentation choice: keep publication author order and original stars, but omit explicit author-position labels and equal-contribution notes. Local September2026 CV and January2026 PPT contain useful detail but some stale authorship and metrics. Avoid uncertain GPA/rank. One granted vacuum-gauge patent is verified in D-20260911-030000-patent. 
## Runtime and capability dependencies
Python stdlib build, bundled reportlab for CV, plain HTML/CSS/JS, authenticated gh CLI. No global installs. Static local assets no analytics.
## Definition of done
Complete EN/ZH pages and relevant detail routes, actual desktop/mobile visual review, functional navigation and language persistence, paper/project/CV/contact links, refresh/reopen, actual published URL validation, privacy audit and valid handoff fingerprints. Blocked checks explicitly recorded.
## Glossary
BEOL = back-end-of-line; M3D = monolithic 3D. Upstream contributor is not automatically upstream maintainer. Confident academic writing; no repetitive evidence disclaimers on site.
