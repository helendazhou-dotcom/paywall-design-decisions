# Paywall Design Decisions

An evidence-aware Codex skill for making mobile subscription and paywall design decisions.

It helps product and UI designers move from a wireframe, product goal, lifecycle context, offer mechanics, and market constraints to a clear **Decision Contract**, design recommendations, localized copy, evidence boundaries, and—when useful—a responsive HTML decision report.

## What it does

- Distinguishes observed facts, sourced data, inference, and unknowns.
- Frames the user's actual subscription decision before searching for references.
- Routes work automatically as a quick judgment, incremental update, standard study, or full high-risk review.
- Preserves verified evidence instead of rerunning the full workflow for every copy or layout edit.
- Uses competitor examples as design evidence, not as proof of conversion performance.
- Produces actionable design guidance, a Design Contract, and optional responsive HTML reports.
- Uses adversarial review only when the decision risk warrants it.

## Install

Copy this repository into your Codex skills directory:

```text
~/.codex/skills/paywall-design-decisions
```

Restart Codex if the skill does not appear immediately.

## Use

Invoke the skill by name:

```text
$paywall-design-decisions
```

Then provide the current page or wireframe, the intended user decision and business goal, the entry point and offer mechanics, and the target platform or market. The skill asks only for missing information that would materially change the transaction or design decision.

## Repository structure

```text
paywall-design-decisions/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── paywall-report-template.html
│   └── paywall-report-commentable-template.html
├── references/
│   └── *.md
└── scripts/
    └── render_report.py
```

## Evidence boundary

Ratings, category rank, estimated revenue, and captured prices provide product context only. They do not prove that a paywall design converts well. The skill keeps those claims separate and labels uncertainty rather than inventing causal certainty.
