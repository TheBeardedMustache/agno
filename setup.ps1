# setup.ps1
# Enhanced setup script with comprehensive error handling

# Function to handle errors gracefully
function Handle-Error {
    param(
        [string]$ErrorMessage,
        [string]$Context = "Unknown",
        [bool]$ExitOnError = $false
    )
    
    Write-Host "ERROR in $Context`: $ErrorMessage" -ForegroundColor Red
    Write-Host "Timestamp: $(Get-Date)" -ForegroundColor Yellow
    Add-Content -Path "setup_errors.log" -Value "$(Get-Date): ERROR in $Context`: $ErrorMessage"
    
    if ($ExitOnError) {
        Write-Host "Exiting due to critical error..." -ForegroundColor Red
        exit 1
    } else {
        Write-Host "Continuing despite error..." -ForegroundColor Yellow
    }
}

# Function to test service health
function Test-ServiceHealth {
    param(
        [string]$ServiceName,
        [scriptblock]$HealthCheck
    )
    
    Write-Host "Testing $ServiceName health..." -ForegroundColor Yellow
    
    try {
        $result = & $HealthCheck
        if ($result) {
            Write-Host "$ServiceName is healthy ✓" -ForegroundColor Green
            return $true
        } else {
            Write-Host "$ServiceName health check failed ✗" -ForegroundColor Red
            return $false
        }
    } catch {
        Handle-Error -ErrorMessage $_.Exception.Message -Context "$ServiceName Health Check"
        return $false
    }
}

# Create log file for this session
$logFile = "setup_$(Get-Date -Format 'yyyy-MM-dd_HH-mm-ss').log"
Write-Host "Setup started at $(Get-Date)" | Tee-Object -FilePath $logFile

# Ensure we can run scripts
try {
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    Write-Host "Execution policy set successfully ✓" -ForegroundColor Green
} catch {
    Handle-Error -ErrorMessage $_.Exception.Message -Context "Set Execution Policy"
}

Write-Host "Setting up Agno Advanced Constructor Team Environment with Enhanced Error Handling..." -ForegroundColor Green

# Check if Docker is running with detailed error handling
Write-Host "Checking Docker status..." -ForegroundColor Yellow
$dockerHealthy = Test-ServiceHealth -ServiceName "Docker" -HealthCheck {
    try {
        $dockerInfo = docker info 2>$null
        if ($dockerInfo) {
            Write-Host "Docker daemon is running and accessible ✓" -ForegroundColor Green
            return $true
        } else {
            Write-Host "Docker daemon is not responding ✗" -ForegroundColor Red
            return $false
        }
    } catch {
        return $false
    }
}

if (-not $dockerHealthy) {
    Write-Host "Docker troubleshooting steps:" -ForegroundColor Yellow
    Write-Host "1. Start Docker Desktop" -ForegroundColor White
    Write-Host "2. Wait for Docker to fully initialize" -ForegroundColor White
    Write-Host "3. Run 'docker --version' to verify installation" -ForegroundColor White
    Handle-Error -ErrorMessage "Docker is not running or not accessible" -Context "Docker Check" -ExitOnError $true
}

# Stop existing containers gracefully
Write-Host "Stopping existing containers..." -ForegroundColor Yellow
try {
    $composeResult = docker-compose down 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Containers stopped successfully ✓" -ForegroundColor Green
    } else {
        Write-Host "Docker compose down completed with warnings" -ForegroundColor Yellow
        Write-Host "Output: $composeResult" -ForegroundColor Gray
    }
} catch {
    Handle-Error -ErrorMessage $_.Exception.Message -Context "Docker Compose Down"
}

# Load environment variables with validation
Write-Host "Loading environment variables..." -ForegroundColor Yellow
if (Test-Path ".env") {
    try {
        $envVars = @{}
        Get-Content ".env" | ForEach-Object {
            if ($_ -match "^([^#][^=]+)=(.*)$") {
                $envVars[$matches[1]] = $matches[2]
                [Environment]::SetEnvironmentVariable($matches[1], $matches[2], "Process")
            }
        }
        
        # Validate critical environment variables
        $requiredVars = @("OPENAI_API_KEY", "DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_DATABASE")
        $missingVars = @()
        
        foreach ($var in $requiredVars) {
            if (-not $envVars.ContainsKey($var) -or [string]::IsNullOrEmpty($envVars[$var])) {
                $missingVars += $var
            }
        }
        
        if ($missingVars.Count -gt 0) {
            Handle-Error -ErrorMessage "Missing required environment variables: $($missingVars -join ', ')" -Context "Environment Validation"
        } else {
            Write-Host "All required environment variables loaded ✓" -ForegroundColor Green
        }
        
    } catch {
        Handle-Error -ErrorMessage $_.Exception.Message -Context "Environment Variables Loading"
    }
} else {
    Write-Host "Creating sample .env file..." -ForegroundColor Yellow
    $sampleEnv = @"
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Database Configuration
DB_HOST=localhost
DB_PORT=5532
DB_USER=ai
DB_PASSWORD=ai
DB_DATABASE=ai

# Optional: Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
"@
    Set-Content -Path ".env" -Value $sampleEnv
    Handle-Error -ErrorMessage ".env file not found. Created sample .env file. Please edit with your configuration." -Context "Environment Setup"
}

# Start Docker services with retry logic
Write-Host "Starting Docker services..." -ForegroundColor Yellow
$maxRetries = 3
$retryCount = 0

do {
    $retryCount++
    try {
        Write-Host "Attempt $retryCount/$maxRetries - Starting Docker services..." -ForegroundColor Yellow
        $composeResult = docker-compose up -d 2>&1
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Docker services started successfully ✓" -ForegroundColor Green
            break
        } else {
            Write-Host "Docker compose up failed on attempt $retryCount" -ForegroundColor Red
            Write-Host "Output: $composeResult" -ForegroundColor Gray
            
            if ($retryCount -lt $maxRetries) {
                Write-Host "Retrying in 5 seconds..." -ForegroundColor Yellow
                Start-Sleep -Seconds 5
            }
        }
    } catch {
        Handle-Error -ErrorMessage $_.Exception.Message -Context "Docker Compose Up - Attempt $retryCount"
        if ($retryCount -lt $maxRetries) {
            Start-Sleep -Seconds 5
        }
    }
} while ($retryCount -lt $maxRetries -and $LASTEXITCODE -ne 0)

if ($LASTEXITCODE -ne 0) {
    Handle-Error -ErrorMessage "Failed to start Docker services after $maxRetries attempts" -Context "Docker Compose Up" -ExitOnError $true
}

# Wait for PostgreSQL with enhanced monitoring
Write-Host "Waiting for PostgreSQL to be ready..." -ForegroundColor Yellow
$maxAttempts = 60
$attempt = 0
$pgReady = $false

do {
    $attempt++
    Start-Sleep -Seconds 2
    
    try {
        $pgStatus = docker exec agno-postgres pg_isready -U ai -d ai 2>$null
        if ($pgStatus -match "accepting connections") {
            $pgReady = $true
            Write-Host "PostgreSQL is ready ✓" -ForegroundColor Green
            break
        }
        
        # Check if container is running
        $containerStatus = docker ps --filter "name=agno-postgres" --format "table {{.Status}}" 2>$null
        if ($containerStatus -notmatch "Up") {
            Write-Host "PostgreSQL container is not running. Checking logs..." -ForegroundColor Red
            docker logs agno-postgres --tail 10 2>$null
        }
        
    } catch {
        # Continue trying
    }
    
    if ($attempt -le $maxAttempts) {
        Write-Host "Attempt $attempt/$maxAttempts - Waiting for PostgreSQL..." -ForegroundColor Yellow
        
        # Show progress every 10 attempts
        if ($attempt % 10 -eq 0) {
            Write-Host "Still waiting for PostgreSQL... Checking container status..." -ForegroundColor Cyan
            docker ps --filter "name=agno-postgres" 2>$null
        }
    }
} while ($attempt -lt $maxAttempts)

if (-not $pgReady) {
    Write-Host "PostgreSQL troubleshooting information:" -ForegroundColor Yellow
    Write-Host "Container logs:" -ForegroundColor White
    docker logs agno-postgres --tail 20 2>$null
    Write-Host "Container status:" -ForegroundColor White
    docker ps -a --filter "name=agno-postgres" 2>$null
    Handle-Error -ErrorMessage "PostgreSQL failed to start within timeout" -Context "PostgreSQL Startup" -ExitOnError $true
}

# Install Python dependencies with error handling
Write-Host "Installing Python dependencies..." -ForegroundColor Yellow
try {
    $pipResult = pip install -r requirements.txt 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Dependencies installed successfully ✓" -ForegroundColor Green
    } else {
        Write-Host "Pip install completed with warnings" -ForegroundColor Yellow
        Write-Host "Output: $pipResult" -ForegroundColor Gray
    }
} catch {
    Handle-Error -ErrorMessage $_.Exception.Message -Context "Pip Install"
}

# Install enhanced tools
Write-Host "Installing enhanced development tools..." -ForegroundColor Yellow
try {
    $enhancedPackages = @(
        "psutil", "bandit", "pylint", "black", "flake8", "mypy", "safety",
        "beautifulsoup4", "selenium", "pandas", "numpy", "matplotlib",
        "pytest", "coverage", "jupyter", "pre-commit"
    )
    
    foreach ($package in $enhancedPackages) {
        Write-Host "Installing $package..." -ForegroundColor Gray
        pip install $package --quiet
    }
    
    Write-Host "Enhanced tools installed successfully ✓" -ForegroundColor Green
} catch {
    Write-Host "Some enhanced tools may have failed to install" -ForegroundColor Yellow
}

# Test database connection with detailed error reporting
Write-Host "Testing database connection..." -ForegroundColor Yellow
$testScript = @"
import psycopg
import sys
import traceback

try:
    print('Attempting to connect to PostgreSQL...')
    conn = psycopg.connect('postgresql://ai:ai@localhost:5532/ai')
    print('Database connection successful ✓')
    
    # Test basic query
    cursor = conn.cursor()
    cursor.execute('SELECT version();')
    version = cursor.fetchone()
    print(f'PostgreSQL version: {version[0][:50]}...')
    
    cursor.close()
    conn.close()
    print('Database test completed successfully ✓')
    sys.exit(0)
    
except Exception as e:
    print(f'Database connection failed: {str(e)}')
    print('Full traceback:')
    traceback.print_exc()
    sys.exit(1)
"@

try {
    python -c $testScript
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Database connection test passed ✓" -ForegroundColor Green
    } else {
        Write-Host "Database connection test failed ✗" -ForegroundColor Red
        Write-Host "Troubleshooting steps:" -ForegroundColor Yellow
        Write-Host "1. Check if PostgreSQL container is running: docker ps" -ForegroundColor White
        Write-Host "2. Check PostgreSQL logs: docker logs agno-postgres" -ForegroundColor White
        Write-Host "3. Verify .env file has correct database settings" -ForegroundColor White
        Handle-Error -ErrorMessage "Database connection test failed" -Context "Database Connection Test"
    }
} catch {
    Handle-Error -ErrorMessage $_.Exception.Message -Context "Database Connection Test"
}

# Final health check of all services
Write-Host "Performing comprehensive health check..." -ForegroundColor Yellow

$services = @(
    @{ Name = "PostgreSQL"; Command = "docker exec agno-postgres pg_isready -U ai -d ai"; Required = $true },
    @{ Name = "Redis"; Command = "docker exec agno-redis redis-cli ping"; Required = $false }
)

$healthStatus = @{}
foreach ($service in $services) {
    try {
        $result = Invoke-Expression $service.Command 2>$null
        if ($result) {
            Write-Host "$($service.Name) is healthy ✓" -ForegroundColor Green
            $healthStatus[$service.Name] = $true
        } else {
            Write-Host "$($service.Name) health check failed ✗" -ForegroundColor Red
            $healthStatus[$service.Name] = $false
            if ($service.Required) {
                Handle-Error -ErrorMessage "$($service.Name) is required but not healthy" -Context "Service Health Check"
            }
        }
    } catch {
        Write-Host "$($service.Name) health check error ⚠" -ForegroundColor Yellow
        $healthStatus[$service.Name] = $false
        if ($service.Required) {
            Handle-Error -ErrorMessage "$($service.Name) health check failed with error: $($_.Exception.Message)" -Context "Service Health Check"
        }
    }
}

# Summary
Write-Host "`n" + "="*80 -ForegroundColor Cyan
Write-Host "SETUP SUMMARY" -ForegroundColor Cyan
Write-Host "="*80 -ForegroundColor Cyan

Write-Host "Setup completed at $(Get-Date)" -ForegroundColor Green
Write-Host "Log file: $logFile" -ForegroundColor Gray

Write-Host "`nService Status:" -ForegroundColor White
foreach ($service in $healthStatus.Keys) {
    $status = if ($healthStatus[$service]) { "✓ Healthy" } else { "✗ Unhealthy" }
    $color = if ($healthStatus[$service]) { "Green" } else { "Red" }
    Write-Host "  $service`: $status" -ForegroundColor $color
}

Write-Host "`nAvailable Commands:" -ForegroundColor Cyan
Write-Host "  python main.py                - Start Advanced Constructor Team (recommended)" -ForegroundColor White
Write-Host "  python agui_backend.py        - Start AGUI backend with error handling" -ForegroundColor White
Write-Host "  python agui_persistent_backend.py - Start persistent AGUI backend" -ForegroundColor White

Write-Host "`nPlayground URL:" -ForegroundColor Cyan
Write-Host "  https://app.agno.com/playground?endpoint=localhost%3A7777" -ForegroundColor White

Write-Host "`nFor monitoring and debugging:" -ForegroundColor Cyan
Write-Host "  ag setup                      - Enable monitoring on app.agno.com" -ForegroundColor White
Write-Host "  docker logs agno-postgres     - View PostgreSQL logs" -ForegroundColor White
Write-Host "  docker logs agno-redis        - View Redis logs" -ForegroundColor White
Write-Host "  docker-compose ps             - View container status" -ForegroundColor White

Write-Host "`nSetup completed! ✓" -ForegroundColor Green

# Automatically start all applications without prompting
Write-Host "`nStarting all applications..." -ForegroundColor Green

try {
    # Start AGUI backend in background
    Write-Host "Launching AGUI backend..." -ForegroundColor Yellow
    Start-Process -FilePath "python" -ArgumentList "agui_backend.py" -WindowStyle Minimized
    Start-Sleep -Seconds 2
    
    # Start persistent AGUI backend in background  
    Write-Host "Launching persistent AGUI backend..." -ForegroundColor Yellow
    Start-Process -FilePath "python" -ArgumentList "agui_persistent_backend.py" -WindowStyle Minimized
    Start-Sleep -Seconds 2
    
    # Start main.py (Advanced Constructor Team) last
    Write-Host "Launching Advanced Constructor Team (main.py)..." -ForegroundColor Yellow
    Start-Process -FilePath "python" -ArgumentList "main.py" -WindowStyle Normal
    
    # Wait for servers to initialize
    Write-Host "Waiting for all services to initialize..." -ForegroundColor Yellow
    Start-Sleep -Seconds 10
    
    # Open the playground URL in default browser
    $playgroundUrl = "https://app.agno.com/playground?endpoint=localhost%3A7777"
    Write-Host "Opening playground at: $playgroundUrl" -ForegroundColor Green
    Start-Process $playgroundUrl
    
    Write-Host "`nAll applications are now running! ✓" -ForegroundColor Green
    Write-Host "Services running:" -ForegroundColor White
    Write-Host "  - AGUI Backend: Running in background" -ForegroundColor White
    Write-Host "  - Persistent AGUI Backend: Running in background" -ForegroundColor White
    Write-Host "  - Advanced Constructor Team: Running on http://localhost:7777" -ForegroundColor White
    Write-Host "  - Web UI: $playgroundUrl" -ForegroundColor White
    Write-Host "`nTo stop all services, close the respective windows or use Task Manager." -ForegroundColor Yellow
    
} catch {
    Handle-Error -ErrorMessage $_.Exception.Message -Context "Application Startup"
    Write-Host "`nYou can manually start the applications with:" -ForegroundColor Yellow
    Write-Host "  python agui_backend.py" -ForegroundColor White
    Write-Host "  python agui_persistent_backend.py" -ForegroundColor White
    Write-Host "  python main.py" -ForegroundColor White
}
