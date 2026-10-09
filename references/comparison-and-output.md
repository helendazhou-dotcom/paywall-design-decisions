# Comparison and output

## Compare the user's page

Evaluate the user's page against the selected references on:

- entry context and readiness to pay;
- preceding action, eligibility, repeat-exposure risk, and lifecycle placement;
- above-the-fold hierarchy;
- clarity and specificity of the value proposition;
- benefit order and proof;
- plan count, selection control, and default state;
- price anchoring, billing-period clarity, savings, and trial timeline;
- CTA wording, placement, and relationship to the selected plan;
- reassurance, cancellation language, trust, and social proof;
- close, restore purchase, terms, privacy, and disclosure visibility;
- cognitive load, readability, touch targets, and likely accessibility risks.

Do not treat category conventions as requirements. Explain when the user's differentiated approach is strategically better than the reference pattern.

## Evidence labels

Use these labels or equivalent clear wording:

- **Data**: directly present in structured source fields.
- **Observed**: visibly present in a screenshot or the user's wireframe.
- **Inference**: a reasoned interpretation that has not been validated by experiment.
- **Unknown**: important information that the available source cannot establish.

Before presenting references, include a compact evidence ledger for the claims most likely to change the design. For high-impact inferences, show at least one plausible alternative explanation and the cheapest valid verification route.

## Mandatory decision card

Every primary reference must include a decision card immediately beside or below its screenshot. Keep field names consistent so references can be compared. A card should answer **what to use, what to adapt, what not to copy, and why** before it behaves like a database record.

Use this visual and content order:

1. **Evidence value**: the named uncertainty or design question this case helps examine, retrieval lens, optional heuristic score, strongest similarity, and most important mismatch.
2. **Subscription strategy**: target action, exact offer and prices, trial/renewal mechanics, CTA, and risk-reversal language.
3. **Design patterns**: concise named chips such as `Trial Timeline`, `Benefit List`, `Single Plan`, or `Risk Reversal`.
4. **Transfer judgment**:
   - **Low-regret convention**: supported by product truth, platform expectations, or clear usability logic; still not proof of conversion lift;
   - **Mechanism-supported hypothesis**: plausible and relevant, but requires adaptation or validation;
   - **Not appropriate**: prerequisites do not match, or the pattern risks confusion, pressure, or false claims.
5. **Commercial background**: category, rating, estimated MRR, and category rank. Keep this visually secondary, but make the numeric values slightly larger and bold enough to scan.
6. **Provenance**: paywall type, offer-set count, captured version/release date, source `last_generated_at`, onboarding/walkthrough counts, source class, retrieval date, evidence limitations, original case link, and screenshot source. Render this as the weakest footer treatment.

Required facts across that hierarchy:

- App name and App Store category;
- the retrieval lens and heuristic match score when one was used;
- paywall type;
- pricing periods and exact visible prices;
- introductory price, trial duration, renewal price, and discount when available;
- pricing/offer-set count;
- estimated MRR and category rank, explicitly labeled as directional estimates;
- App Store rating when available;
- captured App version and version release date;
- source `last_generated_at` date;
- onboarding and walkthrough preview counts when relevant;
- original case link and screenshot source;
- retrieval date, source class, and evidence limitations;
- strongest selection reason and most important mismatch with the user's page.

Use `Not available` rather than dropping a field. Do not calculate a discount without naming the comparison price and formula. Do not infer renewal terms from a crossed-out price.

Estimated MRR, category rank, and rating are product-context signals only. Never use them as proof that the paywall design caused conversion or revenue performance.

After the individual cards, add one normalized, visibly bordered comparison table for every selected reference and the user's page. Prefer columns such as **page**, **entry/goal**, **subscription strategy**, **design patterns**, and **decision value for the user's product**. The table must make differences in offer, renewal, benefits, urgency, and layout directly visible; it must not become a flat metadata inventory.

## Recommended report shape

### 1. Decision Contract and summary

State the one-sentence Decision Contract, then the 3-5 decisions that matter most. Lead with outcomes, not research steps.

### 2. Evidence ledger and critical unknowns

Separate Data, Observed, Inference, and Unknown. Rank the unknowns most likely to change the design and show their verification routes. Summarize the wireframe signature, product goal, category, offer assumptions, and missing information.

### 3. Reference evidence

Organize references under only the lenses that answer a material question:

- **Goal/lifecycle evidence**: comparable decision state, offer, renewal logic, and risk reversal;
- **Structure evidence**: comparable information hierarchy or interaction model;
- **Category evidence**: relevant norms, language, and business-model context.

Do not force equal counts. Show the page images and mandatory decision cards. State what each case can and cannot establish.

### 4. Transferable principles

For each principle include observed pattern, plausible mechanism, prerequisites, failure conditions, fit to the user's product, and validation route. Include a counterexample or contrast when it materially clarifies the boundary.

### 5. User-page comparison

Use a matrix only when it improves clarity. Compare the user's page, recurring reference pattern, and implication for the user's goal.

### 6. Questions and tensions

Surface competing choices, for example:

- choice simplicity versus plan discovery;
- annual-plan emphasis versus price shock;
- trial prominence versus expectation clarity;
- persuasive density versus cognitive load;
- category familiarity versus brand differentiation.

Include questions that require product data or stakeholder decisions. Do not hide them inside recommendations.

### 7. Recommendations and validation

Split into:

- **Do now**: low-regret corrections grounded in product truth, platform requirements, or clear usability logic;
- **Validate**: mechanism-supported hypotheses with meaningful uncertainty;
- **Later**: improvements dependent on data, content, or product changes.

For each recommendation include the problem, proposed change, reason, supporting evidence, confidence level, largest remaining unknown, risk if wrong, cheapest falsification method, and tradeoff.

### 8. Localized copy when relevant

When the task includes market localization, show a Chinese comparison/source version before the target-language versions. On wide screens, a Chinese + two-locale set may use three columns; collapse to one column on mobile. Prices, currencies, billing periods, and eligibility text must come from the store billing response or verified product configuration, not a static translation file.

### 9. Compliance and page states

Keep compliance concise and decision-oriented. Prefer five checks:

1. trial and renewal terms appear together;
2. language, currency, and price formatting are fully localized;
3. the user is truly eligible for the displayed offer;
4. exit, restore purchase, terms, privacy, and subscription management are reachable;
5. loading, ineligible, product-load failure, pending purchase, already-subscribed, and close/dismiss states are designed.

Do not output proposed event names or an analytics tracking specification unless the user explicitly asks for analytics implementation.

### 10. Experiment or verification plan

Choose the method that matches the unknown:

- configuration check for price, eligibility, entitlement, and billing behavior;
- localization/legal review for language and disclosure;
- comprehension/usability study for understanding and interaction;
- analytics review for existing behavior and failures;
- controlled experiment for causal impact.

Only for a genuine A/B hypothesis provide:

- hypothesis;
- exact variable to change;
- control and variant;
- primary metric;
- guardrail metric;
- segment or entry context;
- what decision the result will enable.

Also specify the exposure condition, analysis window, eligibility filters, assignment persistence, and how users exposed to multiple variants are treated. Describe measurement requirements in product language. Name analytics events only when the user explicitly asks for an event specification, and clearly mark them as proposals when the real analytics schema has not been inspected.

Avoid multi-variable tests unless the user explicitly wants a concept test.

## Quality bar

- The report must make clear why each reference was selected.
- A screenshot without a data card does not satisfy the reference requirement.
- Verify that every primary reference exposes price/offer data, freshness, and its source link before finalizing.
- Recommendations must trace back to the user's goal and observed page, not popularity alone.
- Every recommendation must trace through an explicit inference or platform/product fact; a reference screenshot alone is insufficient support.
- Avoid false precision. Similarity scores are heuristics.
- Never claim higher conversion without actual experiment data.
- State that a competitor case proves adoption of a pattern, not that the pattern outperforms alternatives.
- Deliver the final report as a static, responsive HTML artifact unless the user explicitly requests another format or comment controls.
