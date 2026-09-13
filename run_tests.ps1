# =========================================
# OrangeHRM Automation Test Execution
# =========================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "========================================="
Write-Host " OrangeHRM Automation Test Execution"
Write-Host "========================================="


# -----------------------------------------
# 1. Check Python Virtual Environment
# -----------------------------------------

Write-Host ""
Write-Host "[1/5] Checking Python virtual environment..."

$venvPython = ".\.venv\Scripts\python.exe"

if (-not (Test-Path $venvPython)) {
    Write-Host "ERROR: Virtual environment not found."
    exit 1
}

Write-Host "Python environment found."


# -----------------------------------------
# 2. Clean Allure Results and Report
# -----------------------------------------

Write-Host ""
Write-Host "[2/5] Cleaning old Allure results and report..."

if (Test-Path "allure-results") {
    Remove-Item -Recurse -Force "allure-results"
}

if (Test-Path "allure-report") {
    Remove-Item -Recurse -Force "allure-report"
}

Write-Host "Cleanup completed."


# -----------------------------------------
# 3. Run Pytest
# -----------------------------------------

Write-Host ""
Write-Host "[3/5] Running Pytest..."
Write-Host ""

if ($args.Count -gt 0) {

    Write-Host "Selected pytest arguments:"

    $args | ForEach-Object {
        Write-Host "  $_"
    }

    Write-Host ""

    & $venvPython -m pytest @args -v

}
else {

    Write-Host "Running complete test suite..."
    Write-Host ""

    & $venvPython -m pytest -v
}

$testExitCode = $LASTEXITCODE

Write-Host ""

if ($testExitCode -eq 0) {
    Write-Host "Pytest execution completed successfully."
}
else {
    Write-Host "Pytest execution completed with failures."
}


# -----------------------------------------
# 4. Generate Allure Report
# -----------------------------------------

Write-Host ""
Write-Host "[4/5] Generating Allure report..."

allure generate allure-results -o allure-report

$allureExitCode = $LASTEXITCODE

if ($allureExitCode -ne 0) {
    Write-Host "ERROR: Allure report generation failed."
    exit $allureExitCode
}

Write-Host "Allure report generated successfully."

# Create ZIP file for easy sharing
Write-Host ""
Write-Host "Creating Allure report ZIP..."

Compress-Archive `
    -Path "allure-report\*" `
    -DestinationPath "allure-report.zip" `
    -Force

Write-Host "Allure report ZIP created: allure-report.zip"

# -----------------------------------------
# 5. Open Allure Report
# -----------------------------------------

Write-Host ""
Write-Host "[5/5] Opening Allure report..."

# Start Allure server without opening
# another PowerShell window.
#
# Allure 3 can serve the generated report.
# The command is started as a background
# process.

Start-Process `
    -FilePath "allure" `
    -ArgumentList "open", "allure-report" `
    -WindowStyle Hidden

Write-Host "Allure report opened."


# -----------------------------------------
# Final Status
# -----------------------------------------

Write-Host ""
Write-Host "========================================="

if ($testExitCode -eq 0) {
    Write-Host " TEST EXECUTION PASSED"
}
else {
    Write-Host " TEST EXECUTION FAILED"
}

Write-Host " ALLURE REPORT GENERATED"
Write-Host "========================================="
Write-Host ""

exit $testExitCode