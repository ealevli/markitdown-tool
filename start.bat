@echo off
cd /d "%~dp0"

echo [MarkItDown] Checking dependencies...
pip show markitdown >nul 2>&1
if errorlevel 1 (
    echo [MarkItDown] Installing requirements...
    pip install -r requirements.txt
)

echo [MarkItDown] Starting server at http://localhost:8000
start "" http://localhost:8000
uvicorn main:app --port 8000
