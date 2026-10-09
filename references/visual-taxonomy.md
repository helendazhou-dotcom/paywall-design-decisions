# Visual taxonomy and similarity

Use this reference when a wireframe or screenshot is supplied and visual similarity affects retrieval.

## Parse the page

Represent the user's page and each candidate with the same fields:

- presentation surface: full screen, sheet, modal, drawer, carousel, embedded;
- viewport and scroll behavior;
- ordered sections and their approximate height ratios;
- hero type and dominant visual area;
- headline, subheadline, benefits, proof, pricing, CTA, reassurance, legal;
- plan-control type and number of visible choices;
- CTA position, width, fixed/inline behavior, and repetition;
- close, restore, terms, privacy, and billing disclosure positions;
- density, whitespace, contrast, and visual focal points;
- OCR text themes: outcome, feature, savings, urgency, trust, billing.

Use normalized positions rather than raw pixels when device sizes differ.

## Similarity model

For screenshot-based retrieval, prefer this fused heuristic:

- 35% section order and information hierarchy;
- 20% element position and relative area;
- 15% plan and price-control structure;
- 15% on-screen text purpose and semantics;
- 10% CTA position and action flow;
- 5% color, imagery, and stylistic similarity.

The weights are explanatory heuristics, not learned performance predictions. Adjust them when the user explicitly values a different dimension.

## Advanced method

The `SageSELab/FRAME` repository demonstrates a stronger retrieval architecture combining full-screen and component visual embeddings, OCR text embeddings, and a graph of spatial relationships. Use that method as design guidance when implementing automated retrieval. Do not require its heavy model pipeline for ordinary analyses.

Google's `screen_annotation` dataset provides a useful vocabulary for element type, location, OCR text, and image description. It can inform the schema, but it is not a paywall-performance dataset and should not be used to infer conversion.

## Inspection rule

Automated similarity creates candidates only. A primary reference still requires human-visible screenshot inspection, verified data, a stated match reason, and the strongest mismatch.
