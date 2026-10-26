#!/usr/bin/env python3
"""Exporta el contrato OpenAPI 3.1.0 de la aplicación FastAPI a openapi/openapi.yaml (y JSON)."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from app.main import app  # noqa: E402

schema = app.openapi()
openapi_dir = ROOT / "openapi"
openapi_dir.mkdir(exist_ok=True)

json_path = openapi_dir / "openapi.json"
json_path.write_text(json.dumps(schema, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

try:
    import yaml

    yaml_path = openapi_dir / "openapi.yaml"
    yaml_path.write_text(
        yaml.safe_dump(schema, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
except ImportError:
    pass

print(f"OpenAPI 3.1 schema exported successfully ({len(schema.get('paths', {}))} paths).")
