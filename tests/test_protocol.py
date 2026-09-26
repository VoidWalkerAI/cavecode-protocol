import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


validator = load_module(
    "cavecode_validator", ROOT / "tools/validator/validate_cavecode.py"
)
fixer = load_module("cavecode_fixer", ROOT / "tools/fixer/cavecode_fix_v1.py")
converter = load_module(
    "cavecode_converter", ROOT / "tools/compiler/cavecode_convert.py"
)


class ProtocolTests(unittest.TestCase):
    def assert_valid(self, path: Path, profile: str = "auto") -> None:
        result = validator.validate_file(path, profile=profile)
        self.assertTrue(result.ok, f"{path}: {result.errors}")

    def test_repository_master_map_validates(self):
        self.assert_valid(ROOT / "CAVECODE-PROTOCOL.cavecode.txt", "project")

    def test_project_template_validates(self):
        self.assert_valid(
            ROOT / "templates/cavecode_project_map_v1.0.cavecode.txt", "project"
        )

    def test_maintained_artifact_examples_validate(self):
        paths = [
            ROOT / "templates/cavecode_artifact_template_v1.0.cavecode.txt",
            ROOT / "examples/hello-world/hello-world.cavecode",
            ROOT / "examples/runner-config/runner-config.cavecode",
            ROOT / "examples/Example_A_Arcade_Game_Spec",
            ROOT / "examples/Example_B_Simple_Program_Spec_(Hello_World_in_Java)",
        ]
        for path in paths:
            with self.subTest(path=path):
                self.assert_valid(path, "artifact")

    def test_scaffold_outputs_both_profiles(self):
        script = ROOT / "tools/scaffold/cavecode_new_card.py"
        artifact = subprocess.run(
            [sys.executable, str(script), "Test Artifact"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        project = subprocess.run(
            [sys.executable, str(script), "--profile", "project", "Test Project"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
        self.assertTrue(validator.validate_text(artifact, "artifact").ok)
        self.assertTrue(validator.validate_text(project, "project").ok)

    def test_fixer_repairs_glyphs_without_renumbering(self):
        old = """🧱 BLOCK 7 — IDENTITY
🎚️ BLOCK 12 — TUNING KNOBS
🔧 BLOCK 20 — BEHAVIOR FLOW
📝 BLOCK 21 — HUMAN NOTES
"""
        fixed = fixer.fix_text(old)
        self.assertIn("🪨 BLOCK 7 — IDENTITY", fixed)
        self.assertIn("🖍️ BLOCK 12 — TUNING KNOBS", fixed)
        self.assertIn("🎮 BLOCK 20 — BEHAVIOR FLOW", fixed)
        self.assertIn("🖍️ BLOCK 21 — HUMAN NOTES", fixed)
        self.assertTrue(validator.validate_text(fixed).ok)

    def test_converter_output_validates(self):
        source = '{"title":"Monitor","threshold":10,"alert_message":"Stop"}'
        output = converter.render(converter.parse_input(source), source)
        self.assertTrue(validator.validate_text(output, "artifact").ok)

    def test_validator_rejects_legacy_block_glyph(self):
        result = validator.validate_text("🎚️ BLOCK 1 — TUNING KNOBS\nRATE: 2\n")
        self.assertFalse(result.ok)
        self.assertTrue(any("noncanonical" in error for error in result.errors))

    def test_no_active_v11_template_remains(self):
        self.assertFalse(
            (ROOT / "templates/cavecode_artifact_template_v1.1.cavecode").exists()
        )


if __name__ == "__main__":
    unittest.main()
