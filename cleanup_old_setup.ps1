# cleanup_old_setup.ps1 - Remove redundant files after unification

Write-Host "="*80 -ForegroundColor Cyan
Write-Host "CLEANUP - REMOVING REDUNDANT FILES" -ForegroundColor Cyan
Write-Host "="*80 -ForegroundColor Cyan

Write-Host "This script will remove files that are no longer needed:" -ForegroundColor White
Write-Host "• agui_backend.py (functionality moved to main.py)" -ForegroundColor White
Write-Host "• agui_persistent_backend.py (functionality moved to main.py)" -ForegroundColor White
Write-Host "• startup.py (functionality moved to main.py)" -ForegroundColor White
Write-Host "• Log files from old backends" -ForegroundColor White

# Ask for confirmation
$response = Read-Host "`nProceed with cleanup? (y/N)"
if ($response -ne "y" -and $response -ne "Y") {
    Write-Host "Cleanup cancelled." -ForegroundColor Yellow
    exit 0
}

# Create backup directory
$backupDir = "backup_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss')"
New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
Write-Host "Created backup directory: $backupDir" -ForegroundColor Green

# Files to remove/backup
$filesToCleanup = @(
    "agui_backend.py",
    "agui_persistent_backend.py", 
    "startup.py",
    "agui_backend.log",
    "agui_persistent_backend.log"
)

foreach ($file in $filesToCleanup) {
    if (Test-Path $file) {
        try {
            # Create backup
            Copy-Item $file "$backupDir\$file" -Force
            Write-Host "Backed up: $file" -ForegroundColor Yellow
            
            # Remove original
            Remove-Item $file -Force
            Write-Host "Removed: $file" -ForegroundColor Green
        } catch {
            Write-Host "Failed to remove: $file - $($_.Exception.Message)" -ForegroundColor Red
        }
    } else {
        Write-Host "Not found: $file" -ForegroundColor Gray
    }
}

Write-Host "`nCleanup completed!" -ForegroundColor Green
Write-Host "All functionality is now unified in main.py" -ForegroundColor Green
Write-Host "Backup files are in: $backupDir" -ForegroundColor Yellow
Write-Host "`nTo start the unified application:" -ForegroundColor Cyan
Write-Host "  .\setup.ps1" -ForegroundColor White
Write-Host "  or" -ForegroundColor White
Write-Host "  python main.py" -ForegroundColor White