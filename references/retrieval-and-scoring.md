# Retrieval and scoring

## Start from research questions

Before querying any source, list the high-impact unknowns from the Decision Contract and evidence ledger. Each selected reference must do at least one useful job:

- reduce a named uncertainty;
- reveal a plausible mechanism;
- show a prerequisite or failure condition;
- provide a deliberate contrast;
- document a relevant category convention or platform constraint.

Do not retrieve examples merely to fill a gallery or satisfy an equal-count quota. Goal/lifecycle, structure, and category are search lenses, not independent proof types.

## Source layers

Use the public Open Paywall Gallery as the primary page-level case source:

- Repository: `https://github.com/paywallpro/paywall-gallery`
- Manifest: `https://raw.githubusercontent.com/paywallpro/paywall-gallery/main/data/apps.csv`
- JSON manifest: `https://raw.githubusercontent.com/paywallpro/paywall-gallery/main/data/apps.json`
- Schema: `https://raw.githubusercontent.com/paywallpro/paywall-gallery/main/data/schema.json`
- Case page: `https://github.com/paywallpro/paywall-gallery/blob/main/{markdown_path}`
- Raw image: `https://raw.githubusercontent.com/paywallpro/paywall-gallery/main/{featured_image}`

Prefer the manifest and individual case pages over README examples. Record the retrieval date, `last_generated_at`, captured version, and version release date when available.

Query only what the current task needs. Do not mirror, repackage, or persist the complete dataset or screenshot collection.

Supplement it only when the task needs another evidence type:

- RevenueCat AI Toolkit: connected project offerings, rendered paywalls, chart data, and experiments;
- Superwall public docs/SDKs: placement, targeting, post-close and abandon behavior, presentation modes, and event vocabulary;
- PostHog AI Plugin: exposure and experiment-metric methodology or connected analytics;
- App Paywall Pilot: secondary index for benchmarks, lifecycle topics, evidence labels, and source discovery;
- FRAME and Google Screen Annotation: visual/structural retrieval methodology and UI-element vocabulary.

Page-level references still require a verified screenshot and data card. A methodology repository or aggregate benchmark cannot substitute for an actual reference page.

## Lens A: goal and lifecycle match — usually primary

Translate the decision into strategy signals:

- placement, preceding action, and value already experienced;
- desired behavior: trial authorization, direct purchase, plan choice, upgrade, recovery, or win-back;
- offer and renewal architecture;
- decision friction and risk reversal;
- eligibility and decline outcome;
- primary outcome and guardrails.

Use manifest fields such as `paywall_type`, `pricing`, `pricing_group_count`, `onboarding_count`, and `walkthrough_count` to form candidates; then inspect their pages. Rank primarily by decision-state similarity, offer mechanics, lifecycle placement, plausible mechanism, and evidence quality.

MRR and category rank may help prioritize inspection but are not evidence of effectiveness.

## Lens B: structure match — supporting

First derive a structural signature from the user's wireframe or page:

- presentation: full screen, sheet, modal, carousel, or embedded page;
- sequence: hero, headline, benefits, proof, plans, price, trial, CTA, legal;
- plan interaction: single offer, stacked cards, segmented control, toggle, comparison table;
- dominant visual: illustration, product UI, video, testimonial, or text-led;
- page density and scroll behavior;
- CTA placement: fixed, inline, repeated, or plan-card action;
- dismissal and restore placement.

Use this lens when the page hierarchy, density, or interaction model is itself a material design question. Retrieve plausible candidates from multiple categories, then inspect screenshots. An optional ranking heuristic is:

- 35% section order and information hierarchy;
- 20% element position and relative area;
- 15% plan-selection and price-control model;
- 15% visible-text purpose and semantics;
- 10% CTA placement and action flow;
- 5% color, imagery, and stylistic similarity.

Do not score a case without seeing its screenshot. Explain the strongest structural match and the most important mismatch. A high visual score does not make a case strategically transferable.

## Lens C: App-category match — contextual

Start with the exact category. Use an adjacent category only when exact-category evidence is thin or the user's product spans categories; state the adjacency rationale.

Use category to understand user expectations, value vocabulary, and business-model conventions. It is a contextual proxy, not a causal explanation. Select a useful spread rather than a revenue leaderboard:

- one strong category leader or high-signal case;
- one case with a comparable offer/trial model;
- one contrasting pattern that exposes a meaningful design choice.

Rank with:

- 40% category and user-job similarity;
- 25% business-model similarity;
- 20% audience/usage-frequency similarity;
- 15% evidence quality and freshness.

## Cross-lens handling and stopping rule

Create separate candidate pools when multiple lenses are needed, then deduplicate. A result can serve more than one lens only when the reason under each is explicit.

Stop retrieving when additional cases repeat the same mechanism and do not change the likely recommendation, reveal a boundary condition, or reduce a high-impact unknown. A small sufficient evidence set is better than three weak examples per lens.

Similarity scores are optional retrieval aids. Never aggregate them into a performance score, confidence score, or recommendation strength.
