"""create_tool — dynamically create new YAML definitions and reload the searcher."""

from __future__ import annotations

import os
from pathlib import Path
from typing import TYPE_CHECKING, Any

import yaml

if TYPE_CHECKING:
    from searcher.definition_searcher import DefinitionSearcher


def _definitions_dir() -> Path:
    return Path(__file__).resolve().parent.parent / "definitions"


def create_tool(
    searcher: DefinitionSearcher,
    name: str,
    category: str,
    description: str = "",
    block_type: str | None = None,
    stream_type: str | None = None,
    properties: list[dict] | None = None,
) -> str:
    """Create a new tool definition by writing a YAML file to definitions/.

    After writing, the searcher is reloaded so the new properties are
    immediately discoverable.
    """
    data: dict[str, Any] = {"category": category}
    if block_type:
        data["block_type"] = block_type
    if stream_type:
        data["stream_type"] = stream_type
    if description:
        data["description"] = description
    if properties:
        data["properties"] = properties

    # Determine file path from category  (e.g. "blocks/mixer" -> definitions/blocks/mixer.yaml)
    parts = category.split("/")
    base = _definitions_dir()
    if len(parts) > 1:
        file_path = base / "/".join(parts[:-1]) / f"{parts[-1]}.yaml"
    else:
        file_path = base / f"{parts[0]}.yaml"

    os.makedirs(file_path.parent, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    searcher.reload()

    return f"Tool definition saved to {file_path}. Searcher reloaded — new properties are now discoverable."
