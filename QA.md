# Website acceptance record

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
