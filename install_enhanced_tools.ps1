# Install all enhanced tools and capabilities - Fixed for Python 3.13

Write-Host "Installing Enhanced Advanced Constructor Team Tools..." -ForegroundColor Cyan
Write-Host "="*80 -ForegroundColor Cyan

# Check Python version
$pythonVersion = python --version
Write-Host "Python version: $pythonVersion" -ForegroundColor Gray

# Install core enhanced packages (Python 3.13 compatible)
Write-Host "Installing core enhanced packages..." -ForegroundColor Yellow
$corePackages = @(
    "psutil>=5.9.0",
    "beautifulsoup4>=4.12.0",
    "selenium>=4.11.0",
    "pandas>=2.0.0",
    "numpy>=1.24.0",
    "matplotlib>=3.7.0",
    "requests>=2.31.0",
    "pydantic>=2.11.2",
    "streamlit>=1.28.0",
    "plotly>=5.17.0"
)

foreach ($package in $corePackages) {
    Write-Host "Installing $package..." -ForegroundColor Gray
    pip install $package --quiet --no-deps
}

# Install development tools
Write-Host "Installing development tools..." -ForegroundColor Yellow
$devPackages = @(
    "black>=23.0.0",
    "flake8>=6.0.0",
    "mypy>=1.5.0",
    "bandit>=1.7.5",
    "safety>=2.3.0",
    "pytest>=7.4.0",
    "coverage>=7.2.0"
)

foreach ($package in $devPackages) {
    Write-Host "Installing $package..." -ForegroundColor Gray
    pip install $package --quiet
}

# Skip TensorFlow for Python 3.13 (not yet supported)
Write-Host "Skipping TensorFlow (not compatible with Python 3.13)" -ForegroundColor Yellow

# Install PyTorch CPU version (compatible with Python 3.13)
Write-Host "Installing PyTorch CPU version..." -ForegroundColor Yellow
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu --quiet

# Install scikit-learn compatible version
Write-Host "Installing scikit-learn..." -ForegroundColor Yellow
pip install "scikit-learn>=1.3.0,<1.8.0" --quiet

# Skip pre-commit if not in git repository
Write-Host "Checking git repository..." -ForegroundColor Yellow
$isGitRepo = Test-Path ".git"
if ($isGitRepo) {
    Write-Host "Setting up pre-commit hooks..." -ForegroundColor Yellow
    try {
        pip install pre-commit --quiet
        pre-commit install
        Write-Host "✓ Pre-commit hooks installed" -ForegroundColor Green
    } catch {
        Write-Host "⚠ Pre-commit setup failed (continuing anyway)" -ForegroundColor Yellow
    }
} else {
    Write-Host "⚠ Not in git repository - skipping pre-commit hooks" -ForegroundColor Yellow
}

# Create monitoring launcher
@"
@echo off
echo Starting Advanced Constructor Team Monitor...
streamlit run monitoring_dashboard.py --server.port 8501
"@ | Out-File -FilePath "start_monitor.bat" -Encoding ASCII

# Create requirements file for enhanced tools
$enhancedRequirements = @"
# Enhanced Requirements - Python 3.13 Compatible
psutil>=5.9.0
beautifulsoup4>=4.12.0
selenium>=4.11.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.17.0
streamlit>=1.28.0
requests>=2.31.0
httpx>=0.24.0
pydantic>=2.11.2
black>=23.0.0
flake8>=6.0.0
mypy>=1.5.0
bandit>=1.7.5
safety>=2.3.0
pytest>=7.4.0
coverage>=7.2.0
scikit-learn>=1.3.0,<1.8.0
torch>=2.0.0
jupyter>=1.0.0
ipython>=8.14.0
click>=8.1.0
typer>=0.9.0
watchdog>=3.0.0
pathvalidate>=3.1.0
"@

$enhancedRequirements | Out-File -FilePath "requirements_enhanced_py313.txt" -Encoding UTF8

Write-Host "✅ Enhanced tools installation completed!" -ForegroundColor Green
Write-Host "Python 3.13 compatible packages installed" -ForegroundColor Green
Write-Host "`nNew capabilities added:" -ForegroundColor Cyan
Write-Host "• Advanced code review and analysis" -ForegroundColor White
Write-Host "• Intelligent documentation generation" -ForegroundColor White
Write-Host "• System health monitoring" -ForegroundColor White
Write-Host "• Real-time dashboard (run start_monitor.bat)" -ForegroundColor White
Write-Host "• Enhanced human-in-the-loop confirmations" -ForegroundColor White
Write-Host "• Automated testing suites" -ForegroundColor White
Write-Host "• Project template generation" -ForegroundColor White
Write-Host "• PyTorch ML capabilities" -ForegroundColor White

Write-Host "`nNote: TensorFlow skipped (Python 3.13 not yet supported)" -ForegroundColor Yellow
Write-Host "PyTorch installed as ML framework alternative" -ForegroundColor Green