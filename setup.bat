@echo off
echo Setting up Agno Advanced Constructor Team Environment...

REM Check if PowerShell is available
powershell -Command "Get-Host" >nul 2>&1
if %errorlevel% neq 0 (
    echo PowerShell is not available. Please install PowerShell.
    pause
    exit /b 1
)

REM Run the PowerShell script with proper execution policy
powershell -ExecutionPolicy Bypass -File "setup.ps1"

if %errorlevel% neq 0 (
    echo Setup failed. Please check the error messages above.
    pause
    exit /b 1
)

echo Setup completed successfully!
pause
