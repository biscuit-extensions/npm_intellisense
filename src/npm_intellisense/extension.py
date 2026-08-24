from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


import json

class NPMIntellisense(Extension):
    """Autocomplete npm module imports from package.json and node_modules."""

    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)
        self.api = api
        self.modules: set[str] = set()
        self.api.logger.info("npm Intellisense extension initialised.")

    def load_package_json(self, raw_json: str) -> None:
        data = json.loads(raw_json)
        self.modules.update(data.get("dependencies", {}).keys())
        self.modules.update(data.get("devDependencies", {}).keys())

    def autocomplete(self, prefix: str = "") -> list[str]:
        return sorted([m for m in self.modules if m.startswith(prefix)])

    def install(self) -> None:
        self.api.logger.info("npm Intellisense extension installed.")
