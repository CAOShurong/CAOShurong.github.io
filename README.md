# CAO Shurong — academic website

English / Chinese academic website for GitHub Pages. No paid services, runtime dependencies, analytics, or tracking.

Edit `content.py` and `build.py` for content, and `style.css` for appearance. Run `python build.py`, then `python scripts/check_site.py`. Preview with `python -m http.server 8765 --bind 127.0.0.1 --directory site`. GitHub Actions builds and publishes only `site/`. There is no custom domain. The root contains authoring source, not a second copy of the site.

## Content maintenance

- Academic background comes from the owner's supplied biography. Research interests are not represented as completed experimental results.
- Two publications: FALCO-WAFER (co-first author, IEEE ITC-Asia 2025) and Texture-AD (fourth author, arXiv 2024 / CVM 2026). Do not double-count conference/preprint versions.
- Public CV: `assets/Shurong-Cao-CV.pdf`, generated with `make_cv.py` using ReportLab. It is checked in so the ordinary website build needs only Python's standard library.
- Public email is Gmail. The institutional address is a literal mask only; never put the original in metadata, link targets, source, PDF, or Git history. No private phone numbers.
- The upstream contribution snapshot was checked on 2026-09-11: 37 merged PRs across 22 repositories and 21 owners, excluding CAOShurong-owned repositories. Refresh the query before changing the count: `author:CAOShurong is:pr is:merged -user:CAOShurong`.
- Selected software descriptions are grounded in the respective public repositories. Project links and individual PRs let readers inspect the work.

See `ASSET_SOURCES.md` for visual provenance and `AI_START_HERE.md` for agent handoff. `QA.md` records executed acceptance checks and their limits.


## Public mirror

Primary: https://caoshurong.github.io/

Free public alternate: https://caoshurong.caoshurongg.chatgpt.site/

The separate mirror checkout is `../academic-website-mirror`. After building and validating the primary site, run `python scripts/sync_mirror.py ../academic-website-mirror --origin https://caoshurong.caoshurongg.chatgpt.site`. Review and publish that existing Sites project; updates are explicit, not automatic. See HANDOFF.md and QA.md for the active deployment and rollback references.
