# Get the current directory
$currentDirectory = Get-Location

# Navigate to the backend directory
Set-Location -Path ".\backend"

# Check if venv directory already exists
if (-not (Test-Path "venv")) {
    # Create a virtual environment named venv inside the backend directory
    python -m venv venv
}

# Activate the virtual environment
.\venv\Scripts\Activate.ps1

# Check if requirements are already installed
$requirementsInstalled = (pip freeze | Select-String -Pattern $(Get-Content "requirements.txt" -Raw)) -ne $null

if (-not $requirementsInstalled) {
    # Install required Python packages
    pip install -r requirements.txt
    Write-Output "Requirements installed."
} else {
    Write-Output "Requirements are already installed."
}

# Check if requirements installation was successful
if ($LASTEXITCODE -eq 0) {
    # Run the Flask server
    python runserver.py
} else {
    Write-Output "Error: Setup failed. Please check the logs for details."
}

# Deactivate the virtual environment
# deactivate

# Restore to the original directory
Set-Location -Path $currentDirectory
