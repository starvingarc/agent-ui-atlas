#!/usr/bin/env python3
"""Validate catalog structure, language purity, references, and coverage."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_COUNTS = {
    "brand": 536,
    "general": 161,
    "game_ip_scene": 24,
    "reference": 2,
    "image_layer": 36,
    "motion_layer": 18,
}
RESOURCE_TYPES = {
    "design_spec",
    "agent_skill",
    "component_library",
    "prompt_library",
    "reference_implementation",
    "background_theme",
    "image_resource",
    "motion_resource",
}
EXPECTED_SKILL_IDS = {
    "agentation",
    "anthropic-frontend-design",
    "dembrandt",
    "designer-skills",
    "github-premium-frontend",
    "google-design-md",
    "gpt-image-2-skill",
    "hallmark",
    "impeccable",
    "interface-design",
    "interfaces",
    "lottiefiles-motion-design",
    "stitch-skills",
    "taste-skill",
    "ui-skills",
    "vercel-web-design-guidelines",
}
EXPECTED_DEFAULT_SKILLS = {
    "ui_generation": ["anthropic-frontend-design"],
    "visual_polish": ["impeccable"],
    "ui_audit": ["hallmark", "vercel-web-design-guidelines", "interfaces"],
    "design_extraction": ["ui-skills", "dembrandt"],
    "image_layer": ["gpt-image-2-skill"],
    "motion_layer": ["lottiefiles-motion-design"],
}
EXPECTED_QUICK_PICK_IDS = {
    "premium-minimal",
    "warm-editorial",
    "playful-friendly",
    "dark-technical",
    "retro-game",
    "commerce-lifestyle",
    "agent-productivity",
    "spatial-immersive",
}
NEW_STYLE_IDS = {
    "9h-nine-hours",
    "comic-book-ui",
    "corporate-clean",
    "creative-studio",
    "developer-terminal",
    "editorial-magazine",
    "fresh-market",
    "gungendo",
    "hakkaisan",
    "impressionist-oil-ui",
    "kaminashi",
    "light-marketplace",
    "maximalism",
    "neon-tokyo",
    "neo-brutalist-playful",
    "neo-brutalist-soft",
    "particle-network-ui",
    "pola-museum-of-art",
    "tokyo-metropolitan-teien-art-museum",
    "warm-dashboard",
}
MERGED_SOURCE_URLS = {
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/apple-style.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/brutalist-web.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/dark-mode.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/fluent-design.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/geometric-bold.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/github-style.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/ink-wash.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/linear-style.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/luxury-retail.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/material-design.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/minimalist-flat.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/natural-organic.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/neon-gradient.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/notion-style.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/oversized-typography.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/parallax-sections.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/pixel-art.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/retro-vintage.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/shopify-clean.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/sketch-style.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/stripe-style.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/warm-organic.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/watercolor-art.ts",
    "https://github.com/AnxForever/stylekit/blob/main/lib/styles/watercolor-style.ts",
    "https://github.com/marvkr/better-design/tree/main/components/beam-custom",
    "https://github.com/marvkr/better-design/tree/main/components/linear-quality",
    "https://github.com/marvkr/better-design/tree/main/components/pillow-light",
}
JP_RE = re.compile(r"[\u3040-\u30ff]")
CJK_RE = re.compile(r"[\u3040-\u30ff\u3400-\u9fff]")
ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
BANNED_ZH = (
    "Japanese brand reference",
    "Measured Japanese web specification",
    "Distinctive design detail",
    "Distinctive brand-specific design detail",
)


def flatten_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from flatten_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from flatten_strings(item)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_display_language(errors: list[str], context: str, value: dict) -> None:
    if not isinstance(value, dict) or "en" not in value or "zh" not in value:
        fail(errors, f"{context} must contain en and zh")
        return
    for text in flatten_strings(value["en"]):
        if CJK_RE.search(text):
            fail(errors, f"{context} English text contains CJK: {text}")
    for text in flatten_strings(value["zh"]):
        if JP_RE.search(text):
            fail(errors, f"{context} Chinese text contains Japanese kana: {text}")


def main() -> int:
    catalog = yaml.safe_load((ROOT / "catalog.yaml").read_text(encoding="utf-8"))
    errors: list[str] = []
    if catalog.get("schema_version") != 1:
        fail(errors, "schema_version must be 1")
    if catalog.get("last_reviewed") != "2026-08-01":
        fail(errors, "last_reviewed must be 2026-08-01")

    styles = catalog.get("styles", [])
    skills = catalog.get("skills", [])
    counts = Counter(style.get("category") for style in styles)
    if dict(counts) != EXPECTED_COUNTS:
        fail(errors, f"category counts mismatch: {dict(counts)}")
    if len(styles) != 777:
        fail(errors, f"expected 777 styles, found {len(styles)}")

    ids = [style.get("id") for style in styles]
    names = [style.get("name", {}).get("en") for style in styles]
    for label, values in (("id", ids), ("English name", names)):
        duplicates = [value for value, count in Counter(values).items() if count > 1]
        if duplicates:
            fail(errors, f"duplicate {label}: {duplicates[:10]}")
    style_ids = set(ids)
    if not NEW_STYLE_IDS.issubset(style_ids):
        fail(errors, f"missing planned styles: {sorted(NEW_STYLE_IDS - style_ids)}")

    sort_keys: dict[str, set[str]] = {key: set() for key in EXPECTED_COUNTS}
    all_urls: list[str] = []
    for style in styles:
        sid = style.get("id", "<missing>")
        if not ID_RE.fullmatch(sid):
            fail(errors, f"invalid style id: {sid}")
        category = style.get("category")
        if category not in EXPECTED_COUNTS:
            fail(errors, f"{sid}: invalid category {category}")
            continue
        sort_key = style.get("sort_key")
        if not sort_key:
            fail(errors, f"{sid}: missing sort_key")
        elif sort_key.casefold() in sort_keys[category]:
            fail(errors, f"{sid}: duplicate sort_key in {category}: {sort_key}")
        else:
            sort_keys[category].add(sort_key.casefold())

        for field in ("name", "aliases", "visual_cues", "best_for"):
            value = style.get(field)
            if not isinstance(value, dict) or "en" not in value or "zh" not in value:
                fail(errors, f"{sid}: {field} must contain en and zh")
                continue
            if field != "name" and (not value["en"] or not value["zh"]):
                fail(errors, f"{sid}: {field} may not be empty")
            for text in flatten_strings(value["en"]):
                if CJK_RE.search(text):
                    fail(errors, f"{sid}: English {field} contains CJK text: {text}")
            for text in flatten_strings(value["zh"]):
                if JP_RE.search(text):
                    fail(errors, f"{sid}: Chinese {field} contains Japanese kana: {text}")
                for phrase in BANNED_ZH:
                    if phrase in text:
                        fail(errors, f"{sid}: Chinese {field} contains legacy phrase: {phrase}")

        if not style.get("keywords"):
            fail(errors, f"{sid}: keywords may not be empty")
        resources = style.get("resources", [])
        if not resources:
            fail(errors, f"{sid}: must have at least one resource")
        if sum(bool(item.get("canonical")) for item in resources) > 1:
            fail(errors, f"{sid}: only one resource may be canonical")
        for resource in resources:
            if resource.get("type") not in RESOURCE_TYPES:
                fail(errors, f"{sid}: invalid resource type {resource.get('type')}")
            url = resource.get("url", "")
            if urlparse(url).scheme != "https" or not urlparse(url).netloc:
                fail(errors, f"{sid}: invalid resource URL {url}")
            else:
                all_urls.append(url)
            if not resource.get("label"):
                fail(errors, f"{sid}: resource label is required")
            else:
                validate_display_language(errors, f"{sid}: resource label", resource["label"])
        for key in ("skill_overrides", "related_styles"):
            for referenced in style.get(key, []):
                target = {skill["id"] for skill in skills} if key == "skill_overrides" else style_ids
                if referenced not in target:
                    fail(errors, f"{sid}: unknown {key} reference {referenced}")
        for layer_type, referenced_ids in style.get("recommended_layers", {}).items():
            expected = "image_layer" if layer_type == "image" else "motion_layer"
            for referenced in referenced_ids:
                target = next((item for item in styles if item["id"] == referenced), None)
                if not target or target["category"] != expected:
                    fail(errors, f"{sid}: invalid {layer_type} layer {referenced}")

    skill_ids = {skill["id"] for skill in skills}
    if len(skills) != 16 or skill_ids != EXPECTED_SKILL_IDS:
        fail(errors, f"skill catalog mismatch: {sorted(skill_ids ^ EXPECTED_SKILL_IDS)}")
    for skill in skills:
        if not ID_RE.fullmatch(skill["id"]):
            fail(errors, f"invalid skill id: {skill['id']}")
        if urlparse(skill["url"]).scheme != "https":
            fail(errors, f"invalid skill URL: {skill['url']}")
        validate_display_language(errors, f"{skill['id']}: roles", skill.get("roles"))
        validate_display_language(errors, f"{skill['id']}: summary", skill.get("summary"))
    if catalog.get("default_skills") != EXPECTED_DEFAULT_SKILLS:
        fail(errors, "default_skills do not match the approved routing contract")
    for role, configured in catalog.get("default_skills", {}).items():
        for skill_id in configured:
            if skill_id not in skill_ids:
                fail(errors, f"default role {role} references unknown skill {skill_id}")
    quick_picks = catalog.get("quick_picks", [])
    quick_pick_ids = {group.get("id") for group in quick_picks}
    if len(quick_picks) != 8 or quick_pick_ids != EXPECTED_QUICK_PICK_IDS:
        fail(errors, f"quick pick catalog mismatch: {sorted(quick_pick_ids ^ EXPECTED_QUICK_PICK_IDS)}")
    for group in quick_picks:
        validate_display_language(errors, f"quick pick {group.get('id')}: label", group.get("label"))
        if len(group.get("style_ids", [])) not in (3, 4):
            fail(errors, f"quick pick {group.get('id')} must contain 3 or 4 styles")
        for style_id in group.get("style_ids", []):
            if style_id not in style_ids:
                fail(errors, f"quick pick {group.get('id')} references unknown style {style_id}")

    jp_urls = {url for url in all_urls if "kzhrknt/awesome-design-md-jp" in url and "/design-md/" in url}
    if len(jp_urls) != 426:
        fail(errors, f"expected 426 Japanese DESIGN.md URLs, found {len(jp_urls)}")
    design_md_urls = {
        url
        for url in all_urls
        if re.search(r"getdesign\.md/[^/]+/design-md$", url)
        or "VoltAgent/awesome-design-md/blob/main/design-md/" in url
    }
    if len(design_md_urls) != 74:
        fail(errors, f"expected 74 awesome-design-md/GetDesign URLs, found {len(design_md_urls)}")
    missing_merges = MERGED_SOURCE_URLS - set(all_urls)
    if len(MERGED_SOURCE_URLS) != 27 or missing_merges:
        fail(errors, f"missing planned merged sources: {sorted(missing_merges)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(styles)} styles, {len(skills)} skills, and {len(set(all_urls))} unique resource URLs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
