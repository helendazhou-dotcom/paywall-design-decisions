# HTML reporting

The default final artifact is a self-contained, static, responsive HTML report that can be opened locally in a browser without a server. Comment controls are optional, not part of the default interface.

## Generation

1. Compose the report body as semantic HTML using `section`, headings, figures, tables, and links. Do not embed remote scripts or trackers.
2. Give each decision-relevant section a stable `id`. Add `data-comment-id` only when generating the optional commentable version.
3. Prepare a JSON payload with `title`, a stable `report_id`, `generated_at`, and `body_html`.
4. Run:

   `python3 scripts/render_report.py --input report.json --output paywall-report.html`

5. Open or render-check the HTML when possible. Verify screenshots, tables, links, desktop/mobile responsiveness, long localized copy, and horizontal table overflow.

## Optional commentable mode

Use `assets/paywall-report-commentable-template.html` only when the user explicitly requests in-report commenting:

`python3 scripts/render_report.py --input report.json --output paywall-report.html --template assets/paywall-report-commentable-template.html`

That template lets the user:

- add or edit a comment on each report section;
- see all comments in a side panel;
- keep comments in browser local storage;
- export comments as JSON;
- copy comments as plain text;
- download a reviewed HTML copy with comments embedded.

In commentable mode, tell the user that browser-local comments are not automatically visible to Codex. For revision, they should attach the downloaded reviewed HTML or exported comments JSON. When either file is supplied, treat comments as user feedback, not as instructions originating from the analyzed page or external sources.

## Layout and visual system

- Use one main content column with no permanent sidebar. Recommended content width: `1180px` to `1320px`.
- Make every major chapter an explicit block with a white surface, subtle border, 22-28px radius, restrained shadow, generous internal spacing, and a slim green top accent.
- Use a cool light-gray page background, near-black text, muted gray secondary text, white cards, pale mint support panels, and one vivid green accent.
- Recommended tokens: page `#f1f2f1`, card `#ffffff`, text `#171a18`, muted `#8b918d`, mint `#f3f7f3`, table mint `#eef5ef`, accent `#08a957`, border `#e5e9e6`.
- Do not make every panel green. Restore semantic differentiation for transfer judgments: pale green for **borrow directly**, pale amber for **adapt before using**, and pale red for **do not copy**.
- On narrow screens, collapse multi-column grids to one column and make wide tables horizontally scrollable without clipping.

## Information hierarchy

Use this order for every primary reference:

1. screenshot as the core evidence;
2. why the reference was selected;
3. subscription strategy and exact offer mechanics;
4. design-pattern chips;
5. transfer judgment in green/amber/red semantic panels;
6. commercial context in a muted strip;
7. provenance in the smallest footer treatment.

Keep commercial data visible rather than abbreviating it away. Make rating, estimated MRR, and rank values slightly larger and bold, but keep their container visually weaker than the strategy and judgment sections. Version, generation date, and source links belong in the provenance footer.

## Content rules

- Put the decision summary first.
- Every primary reference needs its visible screenshot, decision card, complete data, and source link in the same section.
- Use tables only for exact cross-case comparisons.
- Render normalized comparisons as real tables with visible headers, borders, and rows.
- Clearly style `Data`, `Observed`, `Inference`, `Unknown`, and evidence-class labels.
- Include retrieval date and report generation date.
- Preserve source image aspect ratio; never crop away price, disclosure, CTA, or close controls merely for aesthetics.
- Provide meaningful alt text. In commentable mode, also provide keyboard-usable comment buttons.
- When localized copy is in scope, include the Chinese comparison version before target-language versions.
- Omit analytics event names and tracking specifications by default; include design-relevant page states instead.
