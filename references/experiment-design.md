# Experiment design

Use this reference for every proposed or evaluated paywall experiment.

## Experiment gate

Run an A/B test only when the unresolved question is causal, materially affects the product decision, and cannot be answered more directly. Route other uncertainties first:

- product/configuration check for offer eligibility, store price, entitlement, and renewal behavior;
- native-language or legal review for wording and required disclosure;
- comprehension or usability study for whether users understand the offer or interaction;
- analytics review for existing funnel loss, errors, cancellation, renewal, or segment differences.

For each proposed experiment, state why a cheaper method is insufficient. If the design direction would not change under either result, do not run the experiment.

## Define exposure

Count a user only when the experimental paywall actually becomes visible and usable. An assignment or feature-flag evaluation alone may not equal exposure. Record:

- experiment and variant ID;
- placement/entry context;
- paywall impression and render success;
- offer and product identifiers;
- locale, currency, platform, App version, eligibility, and user state.

Keep assignment stable. Detect users who see multiple variants and state how they are handled; excluding them can bias uneven splits, while first-seen assignment has its own limitations.

## Event funnel

Use existing verified event names when the user's analytics schema is available. Conceptually cover:

1. eligible trigger;
2. paywall rendered/exposed;
3. plan selected;
4. CTA tapped;
5. store purchase flow started;
6. purchase completed, cancelled, failed, or pending;
7. entitlement activated;
8. renewal, cancellation, refund, and retained product use.

Do not invent production event names. If instrumentation is not available yet, mark proposed names as a specification.

## Metrics

- Primary: paid conversion per exposed eligible user, or revenue per exposed eligible user when pricing differs.
- Secondary: plan mix, purchase-flow start, trial start, trial-to-paid, and time to purchase.
- Guardrails: close rate, errors/loading failure, refund, early cancellation, renewal quality, retained product engagement, support complaints, and accidental repeated exposure.

Use trial starts or CTA clicks only as diagnostic metrics, not the sole winner criterion.

## Test construction

- Prefer one material variable per test.
- A multi-variable redesign is acceptable only as an explicitly labeled concept test.
- Predefine hypothesis, population, exposure, primary metric, guardrails, analysis window, and decision rule.
- Connect the test to one named unknown from the evidence ledger and state what decision each plausible result enables.
- Record current confidence, risk if wrong, and the earliest point at which the result can support the intended decision.
- Segment only when justified; avoid repeatedly slicing until a favorable result appears.
- Do not call a winner before enough conversions and renewal observation exist for the decision being made.

RevenueCat's experiment-analysis skill provides a useful sequence: inspect variants and paywalls, retrieve supporting revenue and funnel trends for the same time window, then interpret experiment results. PostHog's experiment skill is useful for exposure rules, metric types, test-account filtering, and multi-variant handling.
