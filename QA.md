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
