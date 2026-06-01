@echo off
cd /d "%~dp0"

set VENV_PYTHON=%USERPROFILE%\.venv\Scripts\python.exe
set SYSTEM_PYTHON=python

:: Pick python executable
if exist "%VENV_PYTHON%" (
    set PYTHON=%VENV_PYTHON%
) else (
    set PYTHON=%SYSTEM_PYTHON%
)

echo [MarkItDown] Installing/checking requirements...
"%PYTHON%" -m pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] pip install failed. Press any key to exit.
    pause >nul
    exit /b 1
)

echo [MarkItDown] Starting server at http://localhost:8000
echo [MarkItDown] Press Ctrl+C to stop.
echo.

timeout /t 2 /nobreak >nul
start "" "http://localhost:8000"

"%PYTHON%" -m uvicorn main:app --port 8000
pause
