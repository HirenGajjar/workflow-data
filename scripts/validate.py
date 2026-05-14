#!/usr/bin/env python3
# SPDX-FileCopyrightText: CLARVIA ASBL
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SCHEMA_DIR = ROOT / "schemas" / "v0.1"


SCHEMA_BY_OBJECT_TYPE = {
    "Source": SCHEMA_DIR / "source.schema.json",
    "Institution": SCHEMA_DIR / "institution.schema.json",
    "DocumentRequirement": SCHEMA_DIR / "document_requirement.schema.json",
    "Deadline": SCHEMA_DIR / "deadline.schema.json",
    "Condition": SCHEMA_DIR / "condition.schema.json",
    "Task": SCHEMA_DIR / "task.schema.json",
    "Workflow": SCHEMA_DIR / "workflow.schema.json",
    "Scenario": SCHEMA_DIR / "scenario.schema.json",
    "ReviewEvent": SCHEMA_DIR / "review_event.schema.json"
}


def load_structured_file(path: Path) -> Any:
    if path.suffix in {".yaml", ".yml"}:
        with path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    if path.suffix == ".json":
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)

    raise ValueError(f"Unsupported file type: {path}")


def load_schema(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def iter_data_files() -> list[Path]:
    files: list[Path] = []

    for pattern in ("*.yaml", "*.yml", "*.json"):
        files.extend(DATA_DIR.rglob(pattern))

    return sorted(files)


def validate_file(path: Path, schemas: dict[str, dict[str, Any]]) -> list[str]:
    errors: list[str] = []

    try:
        data = load_structured_file(path)
    except Exception as exc:
        return [f"{path}: could not parse file: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: top-level value must be an object"]

    object_type = data.get("object_type")

    if not isinstance(object_type, str):
        return [f"{path}: missing or invalid object_type"]

    schema = schemas.get(object_type)

    if schema is None:
        return [f"{path}: unsupported object_type: {object_type}"]

    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    for error in sorted(validator.iter_errors(data), key=lambda err: list(err.path)):
        location = ".".join(str(part) for part in error.path) or "<root>"
        errors.append(f"{path}: {location}: {error.message}")

    return errors


def main() -> int:
    missing_schema_paths = [
        path for path in SCHEMA_BY_OBJECT_TYPE.values()
        if not path.exists()
    ]

    if missing_schema_paths:
        for path in missing_schema_paths:
            print(f"Missing schema: {path}", file=sys.stderr)
        return 1

    schemas = {
        object_type: load_schema(path)
        for object_type, path in SCHEMA_BY_OBJECT_TYPE.items()
    }

    files = iter_data_files()

    if not files:
        print("No data files found.")
        return 0

    all_errors: list[str] = []

    for path in files:
        all_errors.extend(validate_file(path, schemas))

    if all_errors:
        print("Validation failed:", file=sys.stderr)
        for error in all_errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validation passed for {len(files)} data files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
