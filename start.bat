@echo off
cd /d "%~dp0"

:: Activate venv if it exists
if exist "%USERPROFILE%\.venv\Scripts\activate.bat" (
    call "%USERPROFILE%\.venv\Scripts\activate.bat"
)

echo [MarkItDown] Checking dependencies...
pip show markitdown >nul 2>&1
if errorlevel 1 (
    echo [MarkItDown] Installing requirements...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] pip install failed. Press any key to exit.
        pause >nul
        exit /b 1
    )
)

echo [MarkItDown] Starting server at http://localhost:8000
echo [MarkItDown] Press Ctrl+C to stop.
echo.

timeout /t 2 /nobreak >nul
start "" "http://localhost:8000"

python -m uvicorn main:app --port 8000
pause
