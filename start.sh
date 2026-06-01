#!/usr/bin/env bash
set -e

cd "$(dirname "$0")"

echo "[MarkItDown] Checking dependencies..."
if ! pip show markitdown &>/dev/null; then
    echo "[MarkItDown] Installing requirements..."
    pip install -r requirements.txt
fi

echo "[MarkItDown] Starting server at http://localhost:8000"
open http://localhost:8000 2>/dev/null || xdg-open http://localhost:8000 2>/dev/null || true
python3 -m uvicorn main:app --port 8000
