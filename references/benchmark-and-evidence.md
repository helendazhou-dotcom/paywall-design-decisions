# Benchmark and evidence policy

Use an evidence ladder so the report does not present every claim with equal authority.

## Evidence ladder

1. **Platform rule**: Apple or Google review, billing, or store requirement.
2. **Platform guidance/capability**: official HIG, StoreKit, Play Billing, or store documentation.
3. **Vendor aggregate data**: a published multi-App dataset with date, scope, and methodology.
4. **Peer-reviewed or reproducible research**: published research with an inspectable method or repository.
5. **Vendor case study**: one App or a small selected group; useful but not generally causal.
6. **Observed pattern**: visible in a verified screenshot or documented implementation.
7. **Strategic hypothesis**: plausible for this product but requires testing.

Never relabel vendor advice or developer reports as a platform rule.

## Numeric claims

For each decision-relevant number capture:

- the exact claim and unit;
- source title and URL;
- publication or capture date;
- sample size and population when available;
- geography, platform, category, and measurement window;
- evidence class;
- known limitations.

If any essential qualifier is unavailable, say so. Do not transplant a global benchmark into the user's category as a target without explaining the mismatch.

## Useful GitHub sources

- Open Paywall Gallery: page-level screenshots and structured metadata.
- `Nikolai-Iakubovskii/app-paywall-pilot`: source-manifest and evidence-routing patterns. Treat it as a secondary index; follow important numbers to their original source before relying on them.
- `RevenueCat/ai-toolkit`: current project, paywall, chart, and experiment analysis when the user has connected RevenueCat.
- `PostHog/ai-plugin`: experiment exposure and metric methodology when PostHog data is available.

Do not copy these repositories wholesale into this skill. Query the relevant current source during the task and record the retrieval date.

## Causal language

- Allowed: “The reference uses annual-plan anchoring.”
- Allowed: “The source reports a higher conversion rate for this cohort.”
- Not allowed without a controlled result: “This layout increased conversion.”
- Preferred recommendation wording: “Test this because it may reduce decision friction; measure paid conversion and renewal quality.”
