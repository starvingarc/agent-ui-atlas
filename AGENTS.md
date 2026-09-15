# Agent UI Atlas Guide

`catalog.yaml` is the source of truth. The README files are generated views for people and must not be edited directly.

## Retrieval

1. Match an explicit style name or alias first.
2. Otherwise search `keywords`, `visual_cues`, `best_for`, and `category`.
3. When confidence is low, offer three to five clearly different candidates and let the user choose.
4. Use one base style from `brand`, `general`, `game_ip_scene`, or `reference`.
5. Add no more than one `image_layer` and one `motion_layer` when they materially support the brief.

## Resource precedence

1. Use a style-specific `agent_skill` when one is available.
2. Read the canonical `design_spec`; use other specifications and component libraries as supporting evidence.
3. Treat a `reference_implementation` as visual evidence, not as a complete system.
4. Treat a `background_theme` as scene direction only, never as component or layout guidance.
5. If a linked skill cannot be installed or read, follow the available specification directly and do not claim that the skill ran.

## Default skills

Use `default_skills` only when the selected style has no `skill_overrides` or style-specific skill resource:

- `ui_generation`: produce the base interface.
- `visual_polish`: refine typography, spacing, hierarchy, and finish.
- `ui_audit`: check accessibility, responsiveness, interaction states, and generic AI-looking patterns.
- `design_extraction`: recover a design language from an existing site or codebase.
- `image_layer`: create supporting illustration or imagery after the base UI direction is fixed.
- `motion_layer`: define motion after the base UI direction is fixed.

Within `ui_audit`, use `interfaces` for evidence-based cross-discipline review of color, typography, layout, writing, accessibility, and component resilience. Its `variant` and `break` workflows are user-invoked and must not run implicitly.

Generic interface guidance never overrides domain-specific visualization, accessibility, scientific, legal, or safety requirements.

## Brand and IP boundaries

Brand and IP entries are reference directions. Do not copy protected assets, imply endorsement, or present an inspired result as official. Prefer the `-inspired` wording recorded in the catalog when the source is not an official design system.

## Maintenance

Edit `catalog.yaml`, then run:

```bash
python3 scripts/validate_catalog.py
python3 scripts/render_readmes.py
python3 scripts/render_readmes.py --check
```

Keep IDs stable, keep English and Chinese records aligned, and add a canonical HTTPS resource for every new style.
