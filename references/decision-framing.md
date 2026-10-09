# Decision framing and uncertainty

Use this reference before retrieving paywall examples. The purpose is to prevent visual similarity or category familiarity from defining the problem.

## Decision Contract

Write one sentence using this structure:

> At **[placement and moment]**, **[eligible user and prior value awareness]** chooses between **[accept action]** and **[decline action]**. Accepting provides **[immediate value]**, costs **[today's payment or authorization]**, creates **[future billing commitment]**, and declining leads to **[continued access or exit outcome]**.

The contract must distinguish starting a free trial, authorizing future billing, subscribing immediately, choosing a plan, upgrading, restoring, and accepting a win-back offer. If these cannot be distinguished, mark the transaction as unknown before making copy or hierarchy recommendations.

## Decision anatomy

Record only what changes the design decision:

- placement and preceding user action;
- value already experienced versus only promised;
- entitlement and offer eligibility;
- choices available now, including dismissal;
- immediate benefit and immediate monetary cost;
- trial length, first charge, renewal cadence, and cancellation path;
- consequence of declining or closing;
- primary business outcome and user-harm guardrails.

## Evidence ledger

Maintain one row for each material claim:

| Field | Meaning |
|---|---|
| Claim | The design-relevant statement being considered |
| Evidence class | Data, Observed, Inference, or Unknown |
| Evidence | Exact field, screenshot region, user input, or source |
| Alternative explanation | Another plausible reason for the same observation |
| Decision impact | What would change if the claim is wrong |
| Verification route | Cheapest valid way to resolve it |

Use these evidence classes:

- **Data**: directly supplied by verified product configuration, store response, analytics, or a structured source.
- **Observed**: visibly present in the user's page or a verified reference screenshot.
- **Inference**: a mechanism or interpretation that remains unvalidated for this product.
- **Unknown**: information the available evidence cannot establish.

Do not transform an observation into a recommendation without exposing the inference between them.

## Prioritize unknowns

Prioritize an unknown when it is both likely to change the design and costly if assumed incorrectly. Avoid false numeric precision; use high, medium, or low for:

- decision impact;
- current uncertainty;
- harm or reversibility if wrong.

Research the high-impact unknowns first. Do not spend report space resolving metadata gaps that cannot change the design.

## Choose the cheapest valid verification

- **Product/configuration check**: offer eligibility, price, trial period, renewal, entitlement, close behavior.
- **Localization or legal review**: grammar, cultural naturalness, mandatory disclosure, currency formatting.
- **Comprehension or usability study**: whether users understand value, charge timing, cancellation, or interaction.
- **Analytics review**: existing funnel, eligibility, errors, abandonment, cancellation, renewal, or segment differences.
- **Controlled experiment**: whether one design treatment causes a meaningful outcome change.

Do not use A/B testing to answer a question that configuration inspection, native-language review, or a small comprehension study can answer more directly.

## Transferable principle schema

For every principle extracted from references, record:

1. **Observed pattern**: what the cases visibly do.
2. **Plausible mechanism**: which user uncertainty, motivation, or cost it may change.
3. **Prerequisites**: conditions required for that mechanism to operate.
4. **Failure conditions**: when it may confuse, mislead, overload, or fail.
5. **Product fit**: whether the user's placement, offer, audience, and product truth meet those conditions.
6. **Validation route**: how to verify the remaining uncertainty.

A label such as `Trial Timeline` or `Single Plan` is a pattern name, not yet a transferable principle.
