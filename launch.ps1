# CORE Framework Launcher - PowerShell

$ErrorActionPreference = "Stop"

# Get script directory
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Check Python (try python, then py)
function Test-Python {
    try {
        $version = python --version 2>&1
        Write-Host "Found: $version" -ForegroundColor Green
        return "python"
    }
    catch {
        try {
            $version = py --version 2>&1
            Write-Host "Found: $version" -ForegroundColor Green
            return "py"
        }
        catch {
            Write-Host "ERROR: Python is not installed or not in PATH." -ForegroundColor Red
            Write-Host "Please install Python 3.8+ from python.org" -ForegroundColor Yellow
            return $null
        }
    }
}

# Install dependencies
function Install-Dependencies {
    param($PythonCmd, $RequirementsFile)
    
    if (Test-Path $RequirementsFile) {
        Write-Host "Installing dependencies..." -ForegroundColor Yellow
        & $PythonCmd -m pip install -r $RequirementsFile --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Dependencies installed successfully." -ForegroundColor Green
            return $true
        }
        else {
            Write-Host "Failed to install dependencies." -ForegroundColor Red
            return $false
        }
    }
    return $true
}

# Launch v1
function Start-V1 {
    Write-Host "`nLaunching v1 - HTML/CSS/JS..." -ForegroundColor Cyan
    $path = Join-Path $ScriptDir "v1-html\index.html"
    Start-Process $path
    Write-Host "Browser should open automatically." -ForegroundColor Green
    Read-Host "Press Enter to continue"
}

# Launch v2
function Start-V2 {
    Write-Host "`nLaunching v2 - Python TUI..." -ForegroundColor Cyan
    Push-Location (Join-Path $ScriptDir "v2-python")
    
    Write-Host "Checking Python..." -ForegroundColor Yellow
    $pythonCmd = Test-Python
    if (-not $pythonCmd) {
        Pop-Location
        Read-Host "Press Enter to continue"
        return
    }
    
    # Check dependencies
    Write-Host "Checking dependencies..." -ForegroundColor Yellow
    & $pythonCmd -c "import textual" 2>$null
    if ($LASTEXITCODE -ne 0) {
        if (-not (Install-Dependencies $pythonCmd "requirements.txt")) {
            Pop-Location
            Read-Host "Press Enter to continue"
            return
        }
    }
    else {
        Write-Host "Dependencies OK." -ForegroundColor Green
    }
    
    Write-Host "`nStarting CORE Framework TUI..." -ForegroundColor Cyan
    & $pythonCmd -m core_framework.main
    Pop-Location
    Read-Host "Press Enter to continue"
}

# Launch v3
function Start-V3 {
    Write-Host "`nLaunching v3 - React + Supabase..." -ForegroundColor Cyan
    Push-Location (Join-Path $ScriptDir "v3-react\frontend")
    
    # Check Node.js
    Write-Host "Checking Node.js..." -ForegroundColor Yellow
    try {
        $nodeVersion = node --version 2>&1
        Write-Host "Found Node.js: $nodeVersion" -ForegroundColor Green
    }
    catch {
        Write-Host "ERROR: Node.js is not installed." -ForegroundColor Red
        Write-Host "Please install Node.js 18+ from nodejs.org" -ForegroundColor Yellow
        Pop-Location
        Read-Host "Press Enter to continue"
        return
    }
    
    # Check dependencies
    if (-not (Test-Path "node_modules")) {
        Write-Host "Installing dependencies (this may take a minute)..." -ForegroundColor Yellow
        npm install
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Failed to install dependencies." -ForegroundColor Red
            Pop-Location
            Read-Host "Press Enter to continue"
            return
        }
    }
    else {
        Write-Host "Dependencies OK." -ForegroundColor Green
    }
    
    Write-Host "`nStarting development server..." -ForegroundColor Cyan
    Write-Host "Server will run at http://localhost:5173" -ForegroundColor Green
    Write-Host "Press Ctrl+C to stop`n" -ForegroundColor Yellow
    
    # Open browser after delay
    Start-Job -ScriptBlock {
        Start-Sleep -Seconds 3
        Start-Process "http://localhost:5173"
    } | Out-Null
    
    npm run dev
    Pop-Location
}

# Main menu loop
while ($true) {
    Clear-Host
    Write-Host "╔════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║   CORE Framework Launcher          ║" -ForegroundColor Cyan
    Write-Host "╚════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1. v1 - HTML/CSS/JS (No dependencies)" -ForegroundColor Green
    Write-Host "2. v2 - Python TUI (Terminal interface)" -ForegroundColor Green
    Write-Host "3. v3 - React + Supabase (Full-featured)" -ForegroundColor Green
    Write-Host "4. Exit" -ForegroundColor Red
    Write-Host ""
    
    $choice = Read-Host "Enter your choice (1-4)"
    
    switch ($choice) {
        "1" { Start-V1 }
        "2" { Start-V2 }
        "3" { Start-V3 }
        "4" { 
            Write-Host "`nThank you for using CORE Framework!" -ForegroundColor Cyan
            exit 0
        }
        default {
            Write-Host "Invalid choice. Press Enter to try again..." -ForegroundColor Red
            Read-Host
        }
    }
}
