#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2025 Clarvia ASBL
"""
validate.py — Validate all Clarvia workflow-data JSON files against v0.1 schemas.

Usage:
    python scripts/validate.py [--schema-dir schemas/v0.1] [--data-dir data]

Exits 0 if all files pass, 1 if any validation errors are found.
"""
