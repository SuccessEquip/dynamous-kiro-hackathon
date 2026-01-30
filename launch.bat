@echo off
setlocal enabledelayedexpansion

:: CORE Framework Launcher - Windows Batch

:menu
cls
echo ╔════════════════════════════════════╗
echo ║   CORE Framework Launcher          ║
echo ╚════════════════════════════════════╝
echo.
echo 1. v1 - HTML/CSS/JS (No dependencies)
echo 2. v2 - Python TUI (Terminal interface)
echo 3. v3 - React + Supabase (Full-featured)
echo 4. Exit
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto version1
if "%choice%"=="2" goto version2
if "%choice%"=="3" goto version3
if "%choice%"=="4" goto exit

echo Invalid choice. Press any key to try again...
pause >nul
goto menu

:version1
echo.
echo Launching v1 - HTML/CSS/JS...
cd /d "%~dp0v1-html"
start index.html
echo Browser should open automatically.
pause
goto menu

:version2
echo.
echo Launching v2 - Python TUI...
cd /d "%~dp0v2-python"

:: Check Python (try python, then py)
echo Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    py --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Python is not installed or not in PATH.
        echo Please install Python 3.8+ from python.org
        pause
        goto menu
    )
    set PYTHON_CMD=py
) else (
    set PYTHON_CMD=python
)

%PYTHON_CMD% --version
echo.

:: Check/create virtual environment
if not exist "venv\" (
    echo Creating virtual environment...
    %PYTHON_CMD% -m venv venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        goto menu
    )
)

:: Use venv Python
set VENV_PYTHON=venv\Scripts\python.exe

:: Check dependencies
echo Checking dependencies...
%VENV_PYTHON% -c "import textual" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies in virtual environment...
    %VENV_PYTHON% -m pip install -r requirements.txt --quiet
    if errorlevel 1 (
        echo Failed to install dependencies.
        pause
        goto menu
    )
    echo Dependencies installed.
) else (
    echo Dependencies OK.
)

echo.
echo Starting CORE Framework TUI...
%VENV_PYTHON% -m core_framework.main
pause
goto menu

:version3
echo.
echo Launching v3 - React + Supabase...
cd /d "%~dp0v3-react\frontend"

:: Check Node.js
echo Checking Node.js...
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed.
    echo Please install Node.js 18+ from nodejs.org
    pause
    goto menu
)

node --version
echo.

:: Check dependencies
if not exist "node_modules\" (
    echo Installing dependencies (this may take a minute)...
    call npm install
    if errorlevel 1 (
        echo Failed to install dependencies.
        pause
        goto menu
    )
) else (
    echo Dependencies OK.
)

echo.
echo Starting development server...
echo Server will run at http://localhost:5173
echo Press Ctrl+C to stop
echo.

:: Open browser after delay
start /b cmd /c "timeout /t 3 /nobreak >nul && start http://localhost:5173"

:: Start dev server
call npm run dev
pause
goto menu

:exit
echo.
echo Thank you for using CORE Framework!
pause
exit /b 0
