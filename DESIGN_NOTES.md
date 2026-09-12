# Editorial refinement — 13 September 2026

The owner rejected repeated lavender panels and then the green alternative, and authorized rethinking the overall design after reading design references. Preserve all factual content, language privacy, direct navigation and previous rollback versions.

## Sources read
- Nielsen Norman Group, Visual Hierarchy in UX: https://www.nngroup.com/articles/visual-hierarchy-ux-definition/ — establish importance through scale, proximity and restrained contrast; excessive containers add clutter.
- USWDS, Using color: https://designsystem.digital.gov/design-tokens/color/overview/ — assign colors to roles, use a limited subset, and check contrast. No claim that a palette universally looks beautiful.
- W3C, Chinese Layout Requirements: https://www.w3.org/TR/clreq/#four_commonly_used_typefaces_for_chinese_composition — distinguish Song, Kai and Hei roles. Choose locally hosted Noto Serif SC headings and Noto Sans SC body; avoid whole-page cursive styling.
- Vincent Sitzmann: https://www.vincentsitzmann.com/ — inspected identity-first introduction, compact research image/text pairs, neutral space and links.
- Keenan Crane: https://www.cs.cmu.edu/~kmcrane/ — inspected strongly illustrated research and direct navigation; did not copy dense tables or saturated orange/gray styling.

## Applied decisions
Purple remains the signature, link and active-state color. Warm white and charcoal carry content; images supply natural variation. Homepage retains the accepted researcher identity and real science figures. Inner-page titles use a split title/summary composition. Research alternates figure/text placement on desktop; publications use paired full figures and reading columns; projects use an image gallery; contributions have two editorial highlights followed by a compact source-linked ledger and selected software screenshots. Mobile returns to a consistent reading order.

Contributions unifies the former repeated home sections. Eight official records cover CycloneDX, GitHub MCP Server, TheELNFileFormat, eLabFTW, Plotly.js, Syft, rclone and tox. eLabFTW is shown as a retained integration test, not an unverified textual homepage acknowledgement. All sources live in credits.py.

Navigation: Home, Research, Publications, Contributions, Projects, Experience, Contact. CV entry points removed; old CV URL remains available for existing inbound links. English is determined by the root URL, never a saved language preference. Explicit /zh/ routes stay Chinese.
