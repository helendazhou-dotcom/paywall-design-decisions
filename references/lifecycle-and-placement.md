# Lifecycle and placement

A paywall is a state in a subscription journey, not an isolated screen. Use this reference when deciding whether a visually similar example is strategically transferable.

## Placement vocabulary

- onboarding completion;
- post-aha or value demonstration;
- premium feature gate;
- usage or credit limit;
- upgrade/settings entry;
- post-close offer;
- transaction abandonment;
- session-start promotion;
- trial or renewal risk;
- billing issue/grace period;
- win-back;
- plan upgrade.

Record the preceding user action, apparent intent, entitlement state, frequency cap, and whether the user can dismiss the surface.

## Transfer check

Before borrowing a pattern, compare:

1. Does the user at both placements have similar value awareness?
2. Is the requested decision the same: trial, direct purchase, annual selection, upgrade, or recovery?
3. Is the offer available to the same eligibility group?
4. Is urgency factual and non-resetting?
5. Could repeated presentation create fatigue or accidental purchase pressure?
6. What happens after close, purchase cancellation, loading failure, and completed purchase?

## Source guidance

Superwall's public SDK and docs are useful for placement, audience rules, post-close actions, transaction-abandon actions, presentation modes, close reasons, and loading events. RevenueCat's public AI toolkit is useful for offerings, entitlements, store state, rendered paywalls, and experiments. These describe capabilities and measurement patterns; they do not prove that a placement will perform better for the user's App.

For a post-close offer, distinguish closing the preceding product surface from dismissing a purchase sheet. They represent different intent and should not be analyzed as the same trigger.
