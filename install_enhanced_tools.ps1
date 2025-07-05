# Install all enhanced tools and capabilities

Write-Host "Installing Enhanced Advanced Constructor Team Tools..." -ForegroundColor Cyan
Write-Host "="*80 -ForegroundColor Cyan

# Install enhanced Python packages
Write-Host "Installing enhanced Python packages..." -ForegroundColor Yellow
pip install -r requirements_enhanced.txt

# Install development tools
Write-Host "Installing development tools..." -ForegroundColor Yellow
pip install pre-commit black flake8 mypy bandit safety

# Install monitoring tools
Write-Host "Installing monitoring tools..." -ForegroundColor Yellow
pip install streamlit plotly psutil py-cpuinfo

# Install AI/ML tools
Write-Host "Installing AI/ML tools..." -ForegroundColor Yellow
pip install scikit-learn tensorflow torch transformers

# Setup pre-commit hooks
Write-Host "Setting up pre-commit hooks..." -ForegroundColor Yellow
pre-commit install

# Create monitoring launcher
@"
@echo off
echo Starting Advanced Constructor Team Monitor...
streamlit run monitoring_dashboard.py --server.port 8501
"@ | Out-File -FilePath "start_monitor.bat" -Encoding ASCII

Write-Host "✅ Enhanced tools installation completed!" -ForegroundColor Green
Write-Host "New capabilities added:" -ForegroundColor Cyan
Write-Host "• Advanced code review and analysis" -ForegroundColor White
Write-Host "• Intelligent documentation generation" -ForegroundColor White
Write-Host "• System health monitoring" -ForegroundColor White
Write-Host "• Real-time dashboard (run start_monitor.bat)" -ForegroundColor White
Write-Host "• Enhanced human-in-the-loop confirmations" -ForegroundColor White
Write-Host "• Automated testing suites" -ForegroundColor White
Write-Host "• Project template generation" -ForegroundColor White