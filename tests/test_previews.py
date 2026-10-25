"""Guard the distinction between a visual preview and implementation resources."""

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from render_readmes import preview_links, quick_pick_rows
from validate_catalog import validate_previews


class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.preview = {
            "url": "https://example.com/demo",
            "kind": "interactive_demo",
            "label": {"en": "Try", "zh": "体验"},
            "checked_on": "2026-10-26",
        }

    def test_missing_preview_is_not_a_broken_link_or_a_claim_of_absence(self):
        self.assertEqual(preview_links({}, "en"), "Not yet listed")
        self.assertEqual(preview_links({}, "zh"), "暂未收录")
        errors = []
        validate_previews(errors, "legacy", {})
        self.assertEqual(errors, [])

    def test_both_languages_explain_the_preview_kind(self):
        record = {"previews": [self.preview]}
        self.assertIn("[Try](https://example.com/demo) (Interactive demo)", preview_links(record, "en"))
        self.assertIn("[体验](https://example.com/demo) (交互演示)", preview_links(record, "zh"))

    def test_quick_pick_keeps_canonical_spec_even_when_not_first(self):
        style = {
            "name": {"en": "Example", "zh": "示例"},
            "resources": [
                {"url": "https://example.com/secondary"},
                {"url": "https://example.com/spec", "canonical": True},
            ],
            "previews": [self.preview],
        }
        catalog = {"quick_picks": [{"label": {"en": "Intent"}, "style_ids": ["example"]}]}
        row = quick_pick_rows(catalog, "en", {"example": style})[0]
        self.assertIn("[Example](https://example.com/demo)", row)
        self.assertIn("[spec](https://example.com/spec)", row)
        self.assertNotIn("secondary", row)
        del style["previews"]
        row = quick_pick_rows(catalog, "en", {"example": style})[0]
        self.assertIn("[Example](https://example.com/spec)", row)

    def test_invalid_urls_kind_dates_and_missing_translations_are_rejected(self):
        for key, value in [
            ("url", "javascript:alert(1)"),
            ("url", "https:///missing-host"),
            ("url", "https://user:secret@example.com/"),
            ("url", "https://example.com/a b"),
            ("kind", "source_code"),
            ("checked_on", "2026-02-30"),
            ("label", {"en": "Try"}),
            ("label", {"en": "Try", "zh": ""}),
        ]:
            with self.subTest(key=key, value=value):
                p = copy.deepcopy(self.preview)
                p[key] = value
                errors = []
                validate_previews(errors, "example", {"previews": [p]})
                self.assertTrue(errors)

    def test_duplicate_and_malformed_previews_are_rejected(self):
        for value in [[self.preview, self.preview], "https://example.com", [None]]:
            with self.subTest(value=value):
                errors = []
                validate_previews(errors, "example", {"previews": value})
                self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
