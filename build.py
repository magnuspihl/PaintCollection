#!/usr/bin/env python3
"""Build index.html from src/template.html + data/paints.json (no dependencies)."""
import json
from pathlib import Path

root = Path(__file__).parent
data = json.loads((root / "data/paints.json").read_text(encoding="utf-8"))
tpl = (root / "src/template.html").read_text(encoding="utf-8")
(root / "index.html").write_text(tpl.replace("__DATA__", json.dumps(data, separators=(",", ":"), ensure_ascii=False)), encoding="utf-8")
print("wrote index.html")
