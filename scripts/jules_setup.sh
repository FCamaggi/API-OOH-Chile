#!/usr/bin/env bash
set -euo pipefail
export USE_IN_MEMORY_DB=true
pip install --quiet -r requirements.txt || true
python3 -m unittest discover -s tests -v
