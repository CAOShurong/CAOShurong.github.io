# Website acceptance record

## V3.3 link refinement — local, 11 September 2026
- PASS: build.py; check_site.py checks 23 HTML documents, resources/anchors, bilingual counterparts and contact privacy; git diff --check.
- Desktop EN/ZH homepage inspected. Actual name-to-CV and English/Chinese research-keyword-to-section navigation observed. NJU and Ni Group links reached the correct official pages.
- Actual Texture-AD title click reached arXiv 2409.06367 and the matching title. FALCO title activated the standard DOI; the browser's Zotero extension redirected IEEE to CUHK library authentication. Publisher content behind that login was not tested; no proxy settings changed.
- Actual click at the center of the CUHK education entry reached the university homepage. Keyboard Tab from the school link focused the independently clickable supervisor link; Enter activated it. Research submenu button opened its three direction links.
- Responsive checks NOT_RUN this revision: viewport overrides returned success but the browser remained 3432px wide. Overrides reset. Prior V3.2 mobile evidence remains historical, not claimed as a new run.
- Standalone design comparison is unpublished and not visually accepted. Its file URL was blocked by the browser; no workaround was attempted. This release contains links and focus/hover affordances only.

### V3.3 published acceptance
- Primary source a3b6e998475dde9227deed9b0ef0139780266832; Pages run 34569001315 succeeded.
- Existing public mirror source 4e2d6e055ebff3159a905992312d7aaabeb2618e; saved Sites version 2, id appgprj_6aa3766f6b8481919bde2fee13651b01~appgver_9e26fc3913b48191b957e9430c7d3c48. Deployment appgdep_6aa39c6bc284819183d674f0ceb48f8d succeeded at https://caoshurong.caoshurongg.chatgpt.site. Public audience unchanged; temporary source credential cleared.
- PASS: eight unauthenticated HTTP reads (EN/ZH home and publications on both origins) return 200, edition 3.3, and both original paper destinations.
- Actual primary home p-type link reached /research/#theme-02; switching to Chinese retained /zh/research/#theme-02. English primary homepage visually inspected.
- Actual mirror name link reached /cv/. Chinese mirror homepage visually inspected; its p-type intro link reached /zh/research/#theme-02 with matching Chinese content.
- Browser read-only evaluate became inconsistent with current snapshots on the mirror; verification used semantic locators, visible AX state and normal screenshots. No fresh responsive claim is made. Site handoff requested in existing in-app tab.

Date: 11 September 2026. Capability: full agent, with actual in-app browser interaction.

## Local acceptance
- PASS: generated 22 bilingual routes plus 404; internal resources, anchors, language counterparts, headings, image descriptions, and contact contract via `python scripts/check_site.py` (exit 0).
- PASS: real browser navigation across all 22 routes at 390px: no horizontal overflow or broken loaded images. Desktop home, research, publications, projects, experience, and mobile contact visually inspected.
- PASS: 320px English publications screenshot reviewed; document width within viewport.
- PASS: mobile menu, project detail navigation, reload, EN/ZH corresponding routes, anchor preservation, saved Chinese preference on reopening root and reload.
- PASS: paper details and BibTeX expansion; copy status observed. Figure modal opened and closed, large architecture image personally inspected. Versioned CSS/JS avoids stale assets after updates.
- PASS: new homepage upstream link navigated to actual contribution section.
- PASS: public CV downloaded through the actual link and opened in browser, one page; extracted PDF text privacy checked. Source originals untouched.
- PASS: DOI link clicked through to IEEE document 11399434; arXiv title/authors matched. Patent page observed inventor, assignee and grant timeline. Repository/software links HTTP checked.
- Optional HTML print button was removed after the embedded browser did not expose a print preview; CV is available through the tested PDF open/download controls.
- NOT_RUN: sending email and physical printing; neither is required to browse or contact via the displayed address.

## Published acceptance
PASS: https://caoshurong.github.io/ deployed from 472e9f95f2925d93abe971fdbded9f2d1a0bd4e2.
GitHub Actions run 34508157181: build and deploy succeeded.
- All 22 published language routes visited through the real browser at 390px; no horizontal overflow, one h1 each, no failed loaded images.
- Desktop homepage visually inspected with the new supplied portrait, both university crests, revised columns and three submenu controls.
- Live mobile Menu > Publications submenu > FALCO-WAFER navigation worked. Figure modal opened and closed; BibTeX copy showed the Chinese success message.
- EN/ZH switch preserved the publication anchor. Chinese preference persisted on reopening root and reloading; switched back to English after testing.
- Live public CV download event observed, PDF opened and personally viewed in browser. Downloaded live PDF parsed as one page with updated patent and no private phone/full institutional email.
- Contact DOM verified only Gmail mailto targets and the literal masked institutional address.
- External links returned successful HTTP responses except Google Patents' automated request (503); actual browser opened CN120352074B correctly with inventor and grant data. IEEE DOI resolved to the correct publisher page in earlier real-click verification.
- No mail was sent and no physical printing was attempted.

## Visual revision after user feedback
- Replaced portrait with exact newly supplied image; removed old portrait and generic layered illustration from current deployment assets.
- Added official CUHK and NJU crests; home composition rebuilt as publication main column and education/open-source sidebar.
- Added explicit research, publication and project submenus, project breadcrumbs and related-project navigation.
- PASS: desktop project submenu opened and FPGA detail link followed; desktop figure/content split visually reviewed.
- PASS: mobile Menu and Projects submenu expanded, vacuum-sensor detail followed, switched to Chinese counterpart and reloaded.
- PASS: all 22 revised routes visited in browser at 320px; one h1 per page, no horizontal overflow and no failed loaded images.
- PASS: desktop home, publication/education sidebar, mobile home and Chinese device project visually reviewed. New public CV remains one page after adding verified patent.

## Prominent GitHub profile entry
PASS on September 11: new bilingual hero button and primary navigation link. Desktop 900px and mobile 390px visually inspected; no horizontal overflow. Live website button clicked and reached https://github.com/CAOShurong (correct profile title). Deployment run 34508955205, source 8697688.

## Purple visual revision — 11 September 2026
Current working-tree checks (previous sections are historical):
- PASS: build.py, scripts/check_site.py (23 HTML documents), node --check app.js.
- PASS: real browser visited all 22 EN/ZH routes at 320px, no horizontal overflow, one h1, no failed loaded images.
- Visually inspected desktop homepage papers, research/practice/exchange sections, research detail; mobile Chinese research and figure dialog. Complete figures fit without cropping. Official exchange wordmarks/crests legible.
- PASS: mobile menu > Research submenu > p-type theme. EN switch preserves theme-02. Removed additive anchor scroll margin; intrinsic image sizes reserve layout space.
- PASS: research and FALCO figure dialogs open/close, home BibTeX copy reports Copied. New public CV parsed as one page, no private university address or explicit author-role emphasis.
- Research detail now explains process constraints and integration questions beyond homepage summaries. Third-party figures have DOI and linked license attribution; own papers use architecture/benchmark figures.
- PASS: deployed source 92c28aaf1a6965efa87cb9ff8697db4c07d57483, Actions run 34544140889 successful (preceding visual deployment 671d5b3, run 34544094294).
- PASS: all 22 live routes visited at 390px, one h1, no horizontal overflow or failed loaded images. Desktop live home/research figures and Chinese vacuum project visually reviewed; mobile education/exchange and Texture-AD modal reviewed.
- PASS: live mobile Menu > Publications > Texture-AD, core figure opened/closed; EN switch preserved #texture-ad. Hero GitHub Profile click reached the correct CAOShurong profile. Homepage vacuum project link reached the illustrated detail page.
- PASS: live CV download event, opened and visually viewed PDF in browser; parsed actual live response as one page with updated exchange wording and no private contacts/role emphasis. Exchange years removed from the public PDF as well.
- Subjective owner approval remains pending. External email delivery and physical printing NOT_RUN.

## Version 2 rebuild — local acceptance, 11 September 2026
- V1 saved remotely as v1.0.0 and archive/v1.0 at f110c82; implementation uses redesign/v2 before main publication.
- PASS: build.py, scripts/check_site.py (23 HTML documents), node --check app.js; all CSS local font/background references exist.
- PASS: real-browser visits to all 22 routes at 320px, one h1, no horizontal overflow or failed loaded images.
- Personally viewed 1440px home hero, portrait/about, research explorer, publication spread, offset projects and Chinese education/exchange; 390px Chinese full-width hero, research switcher and image modal. Fixed the mobile container inset and CUHK logo crop discovered in visual review.
- PASS: moving hero transform observed, pause control stopped it and persisted through reload while title stayed visible; resume works. Research panel click changes figure/text and selected state; selection and anchor persist across EN/ZH switch.
- PASS: mobile Menu > Publications > FALCO-WAFER; citation expansion and clipboard success. Research figure modal opens/closes.
- Reduced motion and no-JS readable defaults implemented; OS preference emulation and physical assistive technology NOT_RUN.
- PASS: V2 source 0747236fb4d272393adebcb7bb61f08f29e86121; GitHub Actions run 34547058691 successful.
- PASS: all 22 live routes at 390px report edition 2.0, one h1, no horizontal overflow or failed loaded images. Chinese desktop hero personally inspected after deployment, including actual loaded fonts and artwork.
- PASS: live research button > p-type panel > full figure dialog > close > English switch; panel and section anchor preserved. Live motion paused, remained paused after reload with visible heading, then resumed.
- PASS: live mobile Projects submenu > FPGA detail page. Public CV download event observed; PDF opened and visually inspected at live URL, one page with new purple palette and nonduplicate Texture-AD venue. Local PDF privacy/author-role scan PASS.
- All checks are functional/visual observations, not the owner's aesthetic approval. V1 rollback references retained.


## Version 3 — local acceptance, 11 September 2026
- PASS: `python build.py`, `python scripts/check_site.py` (23 HTML documents, resources/anchors, bilingual counterparts, contact privacy), `node --check app.js`.
- Real browser inspected researcher reference sites listed in DESIGN_NOTES.md.
- Personally inspected EN/ZH desktop homepage at 1440px; EN/ZH mobile first viewport at 390px and English 320px. Portrait, identity, research summary and contacts all visible initially. Local 320px Gmail bottom approximately 543px.
- Fixed reverse-white institutional marks by restoring their dark plum field; personally saw CUHK/NJU crests and HKUST(GZ)/Cambridge wordmarks.
- Expanded home paper visuals from small side thumbnails to full main-column figures. Personally viewed FALCO mechanism dialog and clipboard copy result `Copied`.
- PASS: 22 real browser route visits at 320px, edition 3.0, one h1, no horizontal overflow and no failed loaded images. Later home-only layout refinements require final live recheck.
- PASS: mobile Menu > Projects submenu > BenchLineage detail; corresponding Chinese route; desktop Research submenu > p-type detail > full figure modal. EN/ZH switch preserves publication anchor.
- PASS: public CV download event; motion pause state observed, persisted through reload, then resumed.
- No changes to the public PDF or paper/portrait/research image files. No original private documents edited.
- Publication and live browser checks follow below. Subjective owner approval is not inferred from technical checks.


### Version 3 — published acceptance
- PASS: deployed source `83e33256ab9bfda4da767423559e1826688bfc6b`; GitHub Actions run `34552981770` completed successfully.
- PASS: real browser visited all 22 live EN/ZH routes at 390px. Every page reports edition 3.0, one h1, no horizontal overflow and no failed loaded images.
- Personally inspected live English first viewport at 390px and 1440px. Gmail bottom 549px (mobile) / 461px (desktop); portrait, name, CUHK PhD identity, advisor, research summary and GitHub/CV/email are above those positions.
- PASS: live GitHub Profile button reached https://github.com/CAOShurong and the correct GitHub profile title.
- PASS: live mobile Menu > Publications submenu > Texture-AD; full figure dialog visually inspected and closed; Chinese switch retained /publications/#texture-ad; Chinese citation copy reported 已复制.
- PASS: live CV download event; Open PDF link opened the public PDF, personally viewed as a single page in browser.
- PASS: live motion pause persisted through reload with heading opacity 1; resumed afterward. Full literature figures use object-fit: contain.
- Publication is technically complete. The owner's subjective aesthetic assessment is still open. No mail delivery, physical printing or assistive-device claim is made.


## Version 3.1 — local acceptance, 11 September 2026
- PASS: build.py, scripts/check_site.py (23 documents, resources, internal anchors, counterparts and public contact contract), node --check app.js, git diff --check.
- PASS: 22 actual browser route visits at 320px; edition 3.1, exactly one h1, no horizontal overflow and no failed loaded images. Scope includes EN/ZH home, research, publications, projects, experience, contact, CV and four project details. Ignored `work/v31-local-route-checks.json` retains observations.
- Personally inspected EN/ZH desktop GitHub feature and all three screenshot cards; Chinese mobile first viewport and open-source section; Chinese desktop school/exchange marks, scholarship and contact note. Header SC and Chinese Noto Sans SC computed font inspected.
- PASS: actual clicks on the large GitHub feature and each of the three cards reached the correct profile/repository/PR. Both upstream destinations visibly report Merged.
- PASS: mobile menu > publications submenu > Texture-AD > full figure dialog > close; Chinese BibTeX copy reported 已复制; English switch preserved /publications/#texture-ad.
- PASS: CV download event and Open PDF navigation. One-page public PDF personally viewed in the browser, parsed as one page with Guo Xie Birong Scholarship and RMB 10,000.
- No changes to research figures, publication authors, portrait or private source documents. Live deployment verification follows separately. Subjective owner acceptance is not inferred.

- Edge live visual follow-up found an awkward final-letter wrap in the mobile contact email. Reduced its responsive size; personally rechecked local 390px and 320px. The 320px email now occupies one 31px-high line within x18–251, with no horizontal overflow.

### Version 3.1 — published acceptance
- Main refinement source `dc51bf011169e22dc6590d9726f09ac1e0a6d487`, Pages run `34556605684`: success.
- Final contact-wrap correction source `b8a9d5900f9ff6610ac02028bee069a9183f2388`, Pages run `34557215867`: success. Published CSS query `ebc921b175` observed after browser reload. Local/CI hash strings differ because of line endings; verify actual served rules, not cross-platform byte identity.
- PASS: all 22 live routes at 390px visited in the actual browser, edition 3.1, one h1, no horizontal overflow or failed loaded images. This route sweep preceded the final contact-only CSS correction; that final correction was rechecked on the affected live contact page.
- Personally inspected live English first viewport and GitHub showcase in the in-app browser. Its screenshot capture subsequently became unavailable; Edge successfully supplied further desktop and mobile visual verification.
- PASS: Edge desktop Chinese contact page, mobile Chinese contact page, final mobile email correction (20.475px, one line / height 35.8px at 390px), and final desktop Chinese GitHub showcase visually inspected. Local 320px correction also visually passed.
- PASS: live large GitHub Profile click reaches the correct profile. All three screenshot destinations were actually clicked during local acceptance and verified as the correct repository or merged PR; the same direct URLs are on the live page.
- PASS: live mobile navigation > publications submenu > Texture-AD, image dialog opens/closes. Chinese citation copy reports 已复制. English switch preserves /publications/#texture-ad.
- PASS: live motion pause persists through reload (button aria-pressed true and body class motion-paused); motion restored afterward.
- PASS: actual live CV download event and PDF open in Edge. The PDF was visually viewed, then the live HTTP response was parsed: one page, Guo Xie Birong Scholarship, RMB 10,000, no unmasked institutional identifier or private phone.
- Final screenshots retained in ignored `work/v31-live-open-source-en.png` and `work/v31-live-open-source-zh.png`. Both viewport overrides reset. Own preview server session 65592 stopped after verification.
- Mail delivery, physical printing and physical assistive technology were not tested. No subjective aesthetic approval is inferred from this acceptance.


## Version 3.2 — signature, profile entry and public mirror (11 September 2026)
- PASS: `python build.py`, `python scripts/check_site.py` (23 documents, resources/anchors, language counterparts and contact privacy), and `git diff --check` during this refinement.
- PASS: actual local desktop checks at 1280px/1024px, mobile EN/ZH at 390px/320px. Signature uses self-hosted Allura and dark purple; header and navigation do not overlap. Chinese mobile Menu > Research submenu > BEOL direction > signature returns to /zh/. Large GitHub feature personally inspected in pale lavender at desktop/mobile widths.
- PASS: primary source `737f58ea67cf54882d67ca93e41d2b6806394fe7`, Pages run `34559744576`, succeeded. Six representative live EN/ZH routes return HTTP200/edition3.2. Actual English desktop first viewport, Chinese research-to-home signature, and corresponding language switch verified. Prior 22-route V3.1 sweep remains historical; no claim it was repeated for all primary routes in V3.2.
- PASS: profile source `f29637c`; its 8 existing tests passed. New SVG homepage banner appears above all prior README content, visually inspected at the top of the actual GitHub Profile. Actual click reached the live V3.2 homepage. Website field saved through GitHub's authenticated profile UI and read back via `gh api users/CAOShurong` as https://caoshurong.github.io/. CLI account-update scope was unavailable; UI completed the same authorized update without changing credentials/scopes.
- PASS: mirror https://caoshurong.caoshurongg.chatgpt.site ; Sites project `appgprj_6aa3766f6b8481919bde2fee13651b01`, public access confirmed. Pushed mirror source `e57f11f1925cc3d6dc2454cae402acd31cfb6cb8`; version `appgprj_6aa3766f6b8481919bde2fee13651b01~appgver_4ed9d7b7a7ec81919bb28a0979b2d018`; deployment `appgdep_6aa37aa5327481919c29d5cc91774379` succeeded. Static out/ is packaged with the Sites helper. Public/ is not a supported helper output root; use out/ and Git Bash /e/ paths for packaging on Windows.
- PASS: all 22 mirror routes, matching canonical origin, signature font, two core publication figures and public PDF checked via unauthenticated HTTP with a normal browser User-Agent. Python's default User-Agent receives Cloudflare1010; ordinary browser access and unauthenticated browser-UA requests work without login.
- PASS: actual mirror desktop Publications submenu > FALCO > full mechanism dialog > close; Chinese switch preserves /publications/#falco-wafer; signature returns to Chinese home. Chinese mobile first viewport at390px has edition3.2, no overflow or failed loaded images. Mobile Menu > CV works. CV download event observed and the PDF personally viewed in the normal desktop PDF viewer; served PDF bytes match the primary public PDF.
- No factual content, research figures, authorship presentation, portrait, private source documents, or unrelated profile sections were changed. V3.1 remotely retained as v3.1.0/archive/v3.1 alongside all V1/V2/V3 references.
- Sites handoff through open_in_codex returned queued for this task. A working Edge mirror tab is retained. Mail delivery, physical printing and physical assistive-device behavior NOT_RUN.

## 2026-09-13 — final acceptance, independent backup and search visibility
Full-agent verification. Detailed commands, source/deployment IDs, actual Bing diagnosis/submissions, live browser results and limitations are recorded in SEARCH_VISIBILITY.md. Both root indexing requests succeeded; Bing live-tested Chinese URL is indexable with no SEO/GEO issues found. Completed indexing/ranking remains pending. Accepted visual body/CSS/JS preserved.

## 2026-09-13 official recognition release
Source d99592ff608cb6a4a4ee6b976070500bafab1664; Pages34707791987 success. Mirror ff0b68626f88103c89f052ce77ecac484f2fd4d4; Sites version5 appgprj_6aa3766f6b8481919bde2fee13651b01~appgver_a512ebf5c1a481919b1d38f492ed70f5; successful deployment appgdep_6aa58967e61881919021e2c258a6f5b0.
PASS: build24routes, check_site25documents, check_search24primary/mirror, Chinese font subset600characters with versioned asset URLs. Local Chinese recognition screenshot inspected and corresponding English switch tested. Live primary homepage recognition link opened Chinese detail; actual official link opened GitHub v1.12.0 New Contributors. CycloneDX official page showed CAOShurong/CUHK in browser. rclone and tox fetched named entries; tox browser confirmed actual issue4021 destination. PR API confirmed merged CycloneDX1028 and rclone9823. Evidence is selected acknowledgements, not an updated full contribution census. Mobile browser NOT_RUN.

Live mirror Chinese recognition page rendered correctly and was visually inspected after deployment.
