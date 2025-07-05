# fix_ports.ps1 - Clean up port conflicts

Write-Host "Cleaning up port conflicts..." -ForegroundColor Yellow

# Stop any Python processes that might be holding ports
Get-Process -Name "python*" -ErrorAction SilentlyContinue | Stop-Process -Force -ErrorAction SilentlyContinue

# Wait a moment
Start-Sleep -Seconds 3

# Check if ports are now free
$port8000 = Test-NetConnection -ComputerName localhost -Port 8000 -WarningAction SilentlyContinue
$port7777 = Test-NetConnection -ComputerName localhost -Port 7777 -WarningAction SilentlyContinue

if ($port8000.TcpTestSucceeded) {
    Write-Host "Port 8000 is still in use" -ForegroundColor Red
} else {
    Write-Host "Port 8000 is now available" -ForegroundColor Green
}

if ($port7777.TcpTestSucceeded) {
    Write-Host "Port 7777 is still in use" -ForegroundColor Red
} else {
    Write-Host "Port 7777 is now available" -ForegroundColor Green
}

Write-Host "You can now run: python main.py" -ForegroundColor Green