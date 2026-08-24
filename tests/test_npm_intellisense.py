from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.npm_intellisense import setup
from src.npm_intellisense.extension import NPMIntellisense


class TestNPMIntellisenseExtension:
    def test_extension_setup(self, app_instance) -> None:
        setup(app_instance.api)
        ext = NPMIntellisense(app_instance.api)
        pkg = '{"dependencies": {"react": "^18.0", "axios": "^1.0"}}'
        ext.load_package_json(pkg)
        res = ext.autocomplete("re")
        assert res == ["react"]
