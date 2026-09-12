# Search visibility — 2026-09-13

The owner accepted the existing V3.3 design as final. The search update preserves the accepted design. A subsequent explicit owner correction removes the three header dropdown buttons and menus, leaving direct page links.

## Diagnosis and actual submissions

- Bing URL Inspection: `/` was **Discovered but not crawled** (discovered 14 August 2026); `/zh/` was **Not discovered**. Both explicitly could not appear in Bing at inspection time.
- Requested indexing for both URLs through the verified Bing Webmaster Tools property. Both returned **Indexing requested.**
- Bing Live URL test for `/zh/`, 00:49 local time: **URL can be indexed by Bing**, **No SEO/GEO issues found**, **2 Markup types found**. This establishes current fetchability, not completed indexing or ranking.
- Submitted `https://caoshurong.github.io/sitemap.xml`; table showed one sitemap, **Processing**, zero errors/warnings. Discovery count was still pending.
- IndexNow submitted the 22 academic EN/ZH sitemap URLs at 2026-09-12T16:43:09.912068 UTC. HTTP **202** means notification received with key validation pending; it does not prove indexing.
- Google Search Console submission: **NOT_RUN**. Search position and completed indexing remain external outcomes, not delivery claims.

## Published changes

- Both names (Shurong Cao / 曹书嵘), CUHK identity, page-specific descriptions, Person/WebSite/ProfilePage structured data, and social previews.
- Primary and mirror canonical/hreflang/structured identity consistently prefer `https://caoshurong.github.io/`. Mirror navigation remains usable on its own origin.
- Public Bing verification meta tag and IndexNow ownership text file. These are intentionally public verification material, not private credentials.
- GitHub Profile README retains its prominent homepage banner and adds a bilingual name heading and explicit academic homepage link. Repository homepage/description are populated.
- Account display-name save initially returned success, but final public UI/API show `ShurongCAO`. Do not claim the account display name is currently bilingual; do not overwrite later account edits. README bilingual heading and homepage link are live.

## Release and verification

- Primary source: `decd87187ec9bcc0f78c9850da77cd2fb81ed134`; Pages run `34705915895` succeeded.
- Mirror source: `1fbe442675498db97062b75ebf84752499f6e60c`; existing Sites project `appgprj_6aa3766f6b8481919bde2fee13651b01`; version 3 `appgver_d9afa8111eb8819180bdef630101c424`; successful deployment `appgdep_6aa5811a82a48191b3172cdac8d80764`.
- Profile README source: `353a541`.
- PASS: build, `scripts/check_site.py` (23 documents), `scripts/check_search.py` (22 bilingual pages) for primary and mirror, `git diff --check`.
- Before navigation simplification, all 23 HTML body contents plus CSS/JS matched the approved D-drive snapshot. After the owner-requested navigation change, all 23 main content regions still match exactly.
- Actual browser: public GitHub README homepage link opened primary; EN to ZH switch worked and new titles appeared. Mirror screenshot showed accepted portrait, signature, figures and layout; live DOM canonical and Person identity prefer primary.
- Backup served directly from D: English home, research anchor and corresponding Chinese route worked.
- Final supplementary urllib HTTP sweep encountered 403; it is not counted as a passed anonymous sweep. Actual browser navigation and Bing live fetch succeeded.
- Fresh mobile, email delivery, printing: NOT_RUN; metadata-only update did not change layout.

## Offline preservation

`D:/CAOShurong-Website-Backup/2026-09-13-approved-v3.3` preserves approved pre-SEO source `eb0940862515006cf09f26b67ea209aeedaca888`, static website, mirror, profile, self-contained Git history bundle, restore guide, and 224 verified file hashes. Keep it intact.

The sibling `2026-09-13-final-v3.3.1` is reserved for the completed search-enhanced source/static backup. Consult its BACKUP.json and SHA256SUMS.json for the exact snapshot. Earlier Git rollback versions remain intact.

## Follow-up interpretation

Allow search engines time to crawl, process and rank. Reinspect these two URLs in Bing Webmaster Tools after processing; avoid repeated daily resubmission. If they remain excluded, use the fresh URL Inspection reason to guide the next fix. Neither a sitemap nor metadata can guarantee first place for a name query.

References: https://www.indexnow.org/documentation ; https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls ; https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl

## Final navigation correction
Owner requested removal of the visually awkward separate dropdown controls. Research, Publications and Projects now link directly to their overview pages in both languages; actual detail pages remain available from their overview content. Removed obsolete submenu markup/styles/listeners; retained the small-screen main Menu control.

Primary source `8fa92317f6dff89106ff90de85b07a0c82b9d7ab`, Pages run `34706518131` succeeded. Mirror source `6ec5221c132eca55a8ab78180f82f55ef21b1e50`, saved version `appgprj_6aa3766f6b8481919bde2fee13651b01~appgver_49f84e27dfc88191addd7cbb441a9271`, deployment `appgdep_6aa583645f2c8191a9650c97c8d0019e` succeeded. PASS: local real clicks through Research/Publications/Projects and Chinese switch; local header screenshot; live primary Research/Projects and mirror Chinese Research direct navigation. One cached primary page initially retained old markup; normal reload showed the new navigation. Build/check_site/check_search and mirror check_search passed. No new small-screen browser acceptance is claimed.

## 2026-09-13 follow-up, 01:21 local
User now finds English-name results, but Chinese-name search still lacks homepage. Bing URL Inspection currently reports Chinese root Discovered but not crawled, discovered13Sept2026 (previously Not discovered). No duplicate root indexing request made. Both Chinese-name title and structured identity remain; added ShurongCAO alias without changing English-only GitHub Profile. New /recognition/ and /zh/recognition/ submitted through IndexNow, HTTP200 receipt; indexing not established.
