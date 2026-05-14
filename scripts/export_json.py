#!/usr/bin/env python3
# SPDX-FileCopyrightText: CLARVIA ASBL
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
EXPORT_DIR = ROOT / "exports" / "json"


def load_structured_file(path: Path) -> Any:
    if path.suffix in {".yaml", ".yml"}:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    if path.suffix == ".json":
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    raise ValueError(f"Unsupported file type: {path}")


def iter_data_files() -> list[Path]:
    files: list[Path] = []

    for pattern in ("*.yaml", "*.yml", "*.json"):
        files.extend(DATA_DIR.rglob(pattern))

    return sorted(files)


def object_type_to_collection_name(object_type: str) -> str:
    mapping = {
        "Source": "sources",
        "Institution": "institutions",
        "DocumentRequirement": "document_requirements",
        "Deadline": "deadlines",
        "Condition": "conditions",
        "Task": "tasks",
        "Workflow": "workflows",
        "Scenario": "scenarios",
        "ReviewEvent": "review_events"
    }

    return mapping.get(object_type, "unknown")


def write_json(path: Path, data: Any) -> None:
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
        file.write("\n")


def main() -> int:
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    collections: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for path in iter_data_files():
        data = load_structured_file(path)

        if not isinstance(data, dict):
            continue

        object_type = data.get("object_type")

        if not isinstance(object_type, str):
            continue

        collection_name = object_type_to_collection_name(object_type)
        collections[collection_name].append(data)

    catalog = {
        "generated_from": "workflow-data",
        "schema_version": "v0.1",
        "collections": {
            name: len(items)
            for name, items in sorted(collections.items())
        }
    }

    write_json(EXPORT_DIR / "catalog.json", catalog)

    for name, items in sorted(collections.items()):
        sorted_items = sorted(items, key=lambda item: item.get("id", ""))
        write_json(EXPORT_DIR / f"{name}.json", sorted_items)

    print(f"Exported {sum(len(items) for items in collections.values())} objects to {EXPORT_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
