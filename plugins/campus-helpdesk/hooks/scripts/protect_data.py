#!/usr/bin/env python3

import json
import os
import sys

try:
    tool_input = json.load(sys.stdin)
except (json.JSONDecodeError, ValueError):
    print("Invalid hook input.", file=sys.stderr)
    sys.exit(2)

file_path = (
    tool_input.get("tool_input", {}).get("file_path")
    or tool_input.get("tool_input", {}).get("path")
    or ""
)

if not file_path:
    sys.exit(0)

project_root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()

protected_dir = os.path.realpath(
    os.path.join(project_root, "data")
)

target_path = os.path.realpath(
    os.path.join(project_root, file_path)
)

try:
    is_protected = (
        os.path.commonpath([protected_dir, target_path])
        == protected_dir
    )
except ValueError:
    is_protected = False

if is_protected:
    print(
        "BLOCKED: Direct writes to the protected data folder are not allowed.",
        file=sys.stderr
    )
    sys.exit(2)

sys.exit(0)
