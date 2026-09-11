# Version 2 design

The intended audience is a prospective research collaborator, institution, or employer. The owner requested visual impact, exploration, academic credibility, purple and motion, while retaining real evidence and a complete bilingual site.

The first screen introduces Shurong Cao and the device/fabrication/M3D identity against an original semiconductor horizon. Bright reading sections then introduce the person, current research questions, authored papers, practical work and open-source contribution. Alternating scale, full-width paper spreads and offset projects replace uniform card grids.

Design guidance consulted: Sites building visual-direction guidance; the live Linear homepage was inspected for restrained dark contrast, typography hierarchy, and progressive product disclosure. No layout, assets, text, code or brand marks were copied from that site.

Motion: slow atmospheric drift, staggered entrance typography, one-time scroll reveals, research panel transitions, reading progress and hover responses. A persistent pause control and prefers-reduced-motion override support comfortable browsing. Native navigation remains usable without JavaScript; research panels default to all visible before enhancement.

Typography: Instrument Serif for English display headings; Inter for body/interface; Noto Serif SC for Chinese heading characters used in the site. Public CV is kept simple and printable with the purple text palette.

## Rollback

Version 1 is preserved at Git tag `v1.0.0` and branch `archive/v1.0`, both based on `f110c82`. Its deployed payload came from `92c28aa`. Roll back through a normal reviewed commit restoring that tagged source; do not rewrite main history. The archive is a reference, not an approved visual design.

## Hero generation

Built-in image_gen. Saved website asset: `assets/hero-frontier.webp`.

Prompt: Premium science-journal quality macro concept of a single thin silicon-wafer horizon, viewed at a low oblique angle, intricate rectilinear microcircuit etching, soft violet interference light and a few distant light points. Almost-black aubergine, imperial purple, platinum and restrained lavender. Place most detail on the right and lower-right; keep the left dark for typography. Scientific curiosity and frontier exploration. No text, logos, people, literal planets, spaceships, rainbow colors, HUDs, floating cubes or cyberpunk. Decorative conceptual art, not a claimed device measurement.


# Version 3: identity-first academic homepage

The owner rejected V2's full-viewport artwork because visitors had to scroll to meet the researcher, and the result resembled a product presentation. V1 and V2 remain rollback references, not approved designs. V3 puts the real portrait, name, CUHK PhD identity, advisor, research summary, GitHub, CV and Gmail together in the initial viewport.

## Researcher references actually inspected

The live pages below were opened and visually reviewed on 11 September 2026. They informed hierarchy and reading rhythm; no code, text, personal assets or research images were copied.

- https://keunhong.com/ — portrait beside a concise personal introduction; restrained serif headings and direct academic links; visual highlights follow immediately.
- https://www.vincentsitzmann.com/ — compact academic identity and contact links; highlighted work uses real imagery and citations rather than a decorative landing page.
- https://www.matthewtancik.com/ — distinctive name typography and authentic research imagery create visual interest inside a compact publication list.
- https://web.stanford.edu/~gordonwz/ — clear identity and contact information. Its older table-based appearance was not the visual model.

## Implemented composition

- A pale paper background, plum text and restrained purple accents, Newsreader headings and Inter body text. Chinese uses a locally hosted Noto Serif SC heading subset.
- A compact portrait-and-bio opening with a direct purple GitHub Profile button. At 320px, the name, photo, PhD role and all contact actions remain within the initial 800px viewport; Gmail ends at approximately 543px in the observed local render.
- Three current research directions are simultaneously illustrated and titled. Complete literature figures retain source and linked license attribution. No p-type figure modification or cropping.
- Authored papers have large mechanism/benchmark figures, citations, abstracts and expandable BibTeX. Explicit author-position labels remain omitted.
- Education and exchange form a side rail beside publications. Engineering projects then regain the full content width; the side rail does not leave a blank column throughout the rest of the page.
- The supplied portrait, all four institution marks, exchange wording without dates, patent, project detail pages, public CV, Gmail and masked institutional email are retained.
- Short entrance and scroll-reveal transitions, hover responses and reading progress support browsing. Pause persists across reload and reduced-motion is respected. Removed the unused V2 research-switcher code; all directions are now visible without interaction.

## Version preservation

- V1: annotated tag `v1.0.0`, branch `archive/v1.0`, source `f110c82ff5e0ee36a68f6a764c624c4775dfb14e` (deployed payload `92c28aa`).
- V2: annotated tag `v2.0.0`, branch `archive/v2.0`, source `48b161c29a5025a0bc285901d335b9b91e7fcdc8` (deployed payload `0747236`). Both were pushed before V3 work.
- V3 is implemented on `redesign/v3`. Restore older versions through a new normal commit; never delete or rewrite version history.

The earlier V2 design and generation prompt above are intentionally preserved.


## Version 3.1 — refinement of the accepted direction
The owner prefers V3 to V1/V2 and asks for targeted polish. Preserve its compact identity, pale purple academic palette, real figures and overall hierarchy.
- Replace the minor scholarship in selected recognition with Guo Xie Birong Scholarship, Nanjing University · RMB 10,000. Repeat the same fact in experience, CV pages and one-page public PDF.
- Make the GitHub Profile a full-width plum invitation with an unmistakable handle, platform mark and direct action. Three real repository/merged-PR screenshots explain maintained research software, infrastructure contributions and scientific computing. Counts become a small secondary line.
- Set Chinese content in locally hosted Noto Sans SC with measured 400/500/600 weights and more breathing room in paragraphs. Retain Newsreader/Inter in English; adjust emphasis and optical spacing.
- Replace `sc.` typesetting with a drawn SC monogram and coordinated favicon. Both remain simple at navigation size.
- Place the Gmail-first institutional-contact sentence directly under the contact email. Keep the institutional address masked and non-actionable.
- V3 rollback also pushed before edits: annotated tag `v3.0.0` and `archive/v3.0` at `2dd3d6e`. V1/V2 references remain intact. V3.1 uses `polish/v3.1`.


## V3.2 final polish
Use an Allura signature in deep purple (#503269), with no adjacent duplicate name. The full signature is a homepage link in both languages. The open-source feature now uses a light lavender gradient (#f0e8f6 to #e2d2ed) with dark-purple typography. Preserve the V3.1 academic composition, evidence imagery, and existing English/Chinese type system.

## V3.3 links and subpage exploration
The owner accepts the current homepage and clarified that the monotonous second-level content means destination pages. The highlighted identity, affiliation, research terms, paper titles, education entries and exchanges now link to the corresponding biography, research sections, original papers and official institutions. Keep text colors and understated hover/focus feedback. Existing submenu arrows get a clearer background.

Proposals below are not a published redesign:
- Keep the compact homepage and purple identity. Prefer near-white pages, dark plum text, and lavender reserved for selected sections over tinting every surface. A warmer mulberry variant is worth comparing but is not selected.
- Research: connect the three research questions through an overview and chapter navigation; alternate complete scientific figures with question-led explanations. Retain exploratory language and linked source/license attribution.
- Publications: use a year rail, clear title/authors/venue hierarchy, large core figures and compact results strips. Keep citations expandable without adding author-position labels.
- Project details: organize each case around its problem, personal contribution, mechanism/prototype, and documented result. Different content types should have different compositions.
- An English comparison draft is retained outside the public payload. It has not passed visual verification: the browser disallowed its local file URL. Do not represent it as an accepted or published design.
