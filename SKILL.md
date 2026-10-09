---
name: paywall-design-decisions
description: Make evidence-aware mobile subscription and paywall design decisions from a user's wireframe, product goal, lifecycle context, and App category. Use for quick design judgment, new research, incremental report updates, or final high-risk review. Route the work to an appropriate depth instead of rerunning the full research workflow for every change. Do not use for implementing billing SDKs or store purchase code.
---

# Paywall Design Decisions

Produce an evidence-backed design decision, not a gallery of similar pages. References are inputs to reasoning; they are not proof of effectiveness.

## Required inputs

Work from these inputs:

1. **Wireframe or current page**: an attached image, Figma frame, screenshot, local file, or clearly described structure.
2. **Decision and product goal**: the intended user decision and business outcome, including audience, entry point, preceding action, offer, trial, eligibility, decline path, and constraints.
3. **App category**: the primary App Store category or closest product category. Treat category as context, not as a causal explanation.

If a missing input changes the actual transaction or the decision being made, ask one concise question. Continue with a partial analysis when the user prefers, and label unknowns rather than inventing them.

## Route the task before working

Classify the request on two independent axes: **starting state** and **depth**. Do not treat the four common request labels as mutually exclusive.

### Starting state

- **New research**: no usable prior report or Design Contract exists, or the entry point, user decision, business goal, audience, offer mechanics, platform, or market has materially changed.
- **Incremental update**: a prior report or Design Contract exists and the core user decision remains valid. Change only the affected section and its downstream dependencies.

### Depth

1. **Quick**: a scoped critique, comparison, copy change, visual hierarchy question, data correction, or local report edit. Do not retrieve new cases, refresh unrelated sources, run subagents, or rebuild the full analysis unless the changed fact invalidates an upstream decision.
2. **Standard**: a new paywall decision, a meaningful design-direction change, or a request for evidence-backed recommendations and a Design Contract. Use a small sufficient evidence set, normally no more than three primary cases. Run one focused adversarial review only when the conclusion contains a material inference that would benefit from it.
3. **Full high-risk review**: final delivery, pre-launch review, multi-market publication, externally cited numeric evidence, or a change to price, offer eligibility, billing period, auto-renewal meaning, purchase risk, or another material transaction fact. Refresh affected sources, perform the complete adversarial review, and verify the final artifact.

### Default routing

- Scoped edit to an existing report: **incremental + quick**.
- New design requirement: **new + standard**.
- Explicit final, launch, compliance, or high-risk request: **new/incremental + full**, depending on whether the Decision Contract still holds.

Choose the route internally and proceed without naming or narrating the mode. Explain the route only when the user asks, when classification is genuinely ambiguous and would materially change the result, or before an escalation that substantially expands time or scope. The user may explicitly request a different depth at any time.

Escalate depth only when evidence discovered during the work shows that the selected mode cannot safely answer the request. Do not silently expand a quick edit into full research.

## Dependency propagation

Treat the work as a dependency chain:

`Product facts -> Decision Contract -> design principles/recommendations -> Design Contract -> copy/visuals -> HTML`

Recompute only the changed layer and its downstream dependents:

- Color, spacing, or layout change: update visuals and the artifact only.
- Ordinary copy change: update the relevant copy and artifact only.
- Source number or metadata correction: verify that source and update affected evidence/provenance only.
- Price, period, offer phase, eligibility, renewal, or decline-outcome change: update the transaction interpretation, Design Contract, copy, and artifact; reassess the Decision Contract when the user's choice changed.
- Entry point, audience, business goal, platform, market, or core choice change: treat as new research and rebuild the Decision Contract.
- New evidence that contradicts a material conclusion: reopen only the affected conclusion, comparisons, and recommendations; broaden research only if the conflict cannot be resolved locally.

Do not refresh a previously verified source merely because the report is being edited. Refresh it when the user asks for current data, its time sensitivity matters to the changed conclusion, or the verification date is no longer adequate for the intended use.

## Shared workflow

Apply only the steps required by the selected route.

1. For new research, read [references/decision-framing.md](references/decision-framing.md) and write a one-sentence **Decision Contract** covering the user, moment, choices, immediate value/cost, future commitment, and decline outcome. For incremental work, reuse it unless an upstream fact changed.
2. Build or update an evidence ledger for material claims: **Data**, **Observed**, **Inference**, and **Unknown**. In quick mode, limit this to claims affected by the request.
3. Route important unknowns to the cheapest valid verification method. Do not default every uncertainty to A/B testing.
4. Inspect the user's page visually when the change affects structure or presentation. Read [references/visual-taxonomy.md](references/visual-taxonomy.md) only when visual matching matters.
5. Retrieve cases only when a named uncertainty cannot be answered from the user's material or verified existing evidence. When retrieval is needed, read [references/retrieval-and-scoring.md](references/retrieval-and-scoring.md), keep goal/lifecycle, structure, and category match distinct, and stop when additional examples no longer change the decision.
6. Inspect the actual screenshot and source data for every new primary result. Metadata alone cannot establish visual similarity, and a screenshot cannot establish effectiveness.
7. For standard or full research, extract transferable principles with the observed pattern, plausible mechanism, prerequisites, failure conditions, product fit, and cheapest validation route.
8. Read [references/comparison-and-output.md](references/comparison-and-output.md) when producing or materially revising recommendations. Separate low-regret changes from hypotheses requiring validation.
9. Read [references/experiment-design.md](references/experiment-design.md) only for a material causal uncertainty that warrants an experiment. Read [references/benchmark-and-evidence.md](references/benchmark-and-evidence.md) before using numeric benchmarks, revenue claims, conversion claims, or category norms.
10. Read [references/lifecycle-and-placement.md](references/lifecycle-and-placement.md) only when entry context, dismissal, abandonment, renewal risk, or win-back affects the decision. Read [references/source-policy.md](references/source-policy.md) whenever PaywallPro/Open Paywall Gallery data is newly used or refreshed.
11. Apply the adversarial review level required by the selected depth, adjudicate valid critiques, and revise the conclusion rather than appending raw feedback.
12. Produce the mode-appropriate deliverable described below.

## Adversarial review

Adversarial review is conditional:

- **Quick**: no subagent review. Perform a brief internal contradiction check only when needed.
- **Standard**: use one focused independent review when a material inference, new evidence synthesis, or consequential recommendation warrants it. Skip it for mechanical or low-risk work.
- **Full**: use three independent subagent reviews at the end of reasoning and before producing the final artifact. Assign review angles that attack the conclusion rather than polish its presentation:

1. **Decision logic:** reconstruct the user's actual choice from first principles; challenge lifecycle assumptions, soft-wall versus hard-wall framing, and whether the proposed hierarchy fits the user's state.
2. **Evidence and causality:** distinguish observation from inference; identify unsupported effectiveness claims, proxy-metric traps, alternative explanations, and experiments that cannot isolate the claimed variable.
3. **Transaction, localization, and compliance:** when relevant, challenge offer accuracy, eligibility, billing-language clarity, CTA interpretation, accidental-purchase risk, local-language naturalness, and platform requirements. When these are out of scope, substitute another domain-relevant failure mode such as accessibility or experiment validity.

Give reviewers the user inputs, material evidence, and draft conclusions, but do not tell them what answer to defend. Ask each reviewer to identify:

- the strongest conclusion that survives scrutiny;
- the weakest assumption or hidden contradiction;
- a plausible counterexample or alternative explanation;
- the condition under which the recommendation reverses;
- the smallest verification that would resolve the disagreement.

When review is used, the primary agent must adjudicate conflicts against the evidence ledger and Decision Contract. Revise claims, confidence, recommendations, copy, and validation design wherever the critique is valid. Do not treat reviewer agreement as proof, include critique verbatim without resolution, or preserve the original conclusion merely for consistency. In full mode, the final answer and HTML report must reflect the revised position and briefly state material changes caused by the review.

## Research invariants

- Frame the decision before retrieval. A visually polished analysis built on the wrong user decision is invalid.
- Keep the three retrieval lenses distinct, but do not force equal counts. Use only cases that reduce a named uncertainty or expose a useful contrast.
- Prefer a small sufficient evidence set. Stop when additional examples repeat the same lesson without changing the decision.
- A report edit is not authorization to rerun research. Preserve verified evidence and unchanged conclusions.
- Do not rerender intermediate HTML after every content edit. Stabilize the affected content, then render once; rerender only to fix a verified artifact problem.
- Deduplicate the final evidence set where useful, but retain a repeated case when it genuinely teaches different lessons through different lenses. Label cross-lens matches explicitly.
- Preserve diversity within the category lens; do not return only the highest estimated MRR Apps or near-identical patterns.
- Do not present a reference as a primary result unless both its screenshot and minimum decision card have been verified. Use it only as a supplementary lead when either side is missing.
- Write `Not available` for missing source fields. Never silently omit a field in a way that implies a value is zero.
- Separate sourced facts, visual observations, strategic inferences, and unknowns at claim level. Record plausible alternative explanations for high-impact inferences.
- Label material claims using the evidence ladder. Numeric claims require a source, date, scope or sample size when available, and an evidence class.
- Treat estimated MRR, ranks, prices, and captured versions as time-bound signals, not verified current facts.
- Never use estimated MRR, category rank, or rating as evidence that a paywall design converts well. They provide product context only.
- Do not recommend copying a competitor page. A transferable principle must include a mechanism, prerequisites, failure conditions, product fit, and validation route.
- When GitHub or screenshots are unavailable, state what could not be verified and continue only with user-provided material or previously stored user-owned notes.
- Keep the report decision-first: Decision Contract > evidence ledger > critical unknowns > principles > recommendations/validation > reference evidence > commercial background > provenance.
- Keep every major chapter in a visually explicit section. Use restrained color overall, but distinguish **low-regret convention**, **mechanism-supported hypothesis**, and **not appropriate** with green, amber, and red semantic panels.
- Do not output proposed analytics event names or an event-tracking specification unless the user explicitly asks for analytics. Include only design-relevant transaction and eligibility states by default.

## Mode-appropriate deliverable

### Quick

- For a judgment request, answer in chat with the decision, evidence boundary, and actionable changes. Do not create a report unless asked.
- For an incremental artifact edit, patch the existing source and rebuild only that artifact. Preserve unrelated sections and sources.
- Include only the evidence, copy, or Design Contract fragment affected by the request.

### Standard

Produce an evidence-backed design recommendation and Design Contract. Generate a new responsive HTML report when the user requests a report or when a durable artifact is the natural outcome; otherwise answer in chat. When updating an existing report, revise it in place rather than rebuilding the research from scratch.

### Full

Produce and verify a self-contained responsive HTML decision report. Read [references/html-reporting.md](references/html-reporting.md) and use `assets/paywall-report-template.html` with `scripts/render_report.py` unless the user requests another format. Use `assets/paywall-report-commentable-template.html` only when the user explicitly asks for in-report comment controls.

For standard or full reports, lead with the decision: what to preserve, rethink, and validate. Include only sections relevant to the request, drawing from:

- interpreted input brief;
- a one-sentence Decision Contract;
- an evidence ledger and prioritized uncertainty map;
- selected references under the relevant goal/lifecycle, structure, and category lenses, with visible pages, decision cards, and explicit evidence value;
- transferable principles with prerequisites, failure conditions, and product fit;
- a normalized comparison table for the selected evidence set;
- side-by-side comparison with the user's page;
- target-language copy with a Chinese comparison version when localization is in scope;
- a concise five-check compliance summary and relevant page-state requirements;
- a **Questions and tensions** section for tradeoffs and assumptions;
- prioritized recommendations split into **Do now**, **Validate**, and **Later**; each recommendation includes confidence, the largest remaining unknown, risk if wrong, and cheapest falsification method;
- A/B hypotheses only for causal questions that cannot be resolved more cheaply, with change, rationale, primary metric, guardrail, and expected learning.

Use similarity scores only to explain ranking. They are research heuristics, not performance scores.

When an HTML report is produced, provide its clickable local file link. Keep research notes and downloaded/transient source material out of the final folder unless the user asks for them.
