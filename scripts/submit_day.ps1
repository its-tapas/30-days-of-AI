param(
  [Parameter(Mandatory = $true)]
  [ValidatePattern('^day\d+$')]
  [string]$Day,

  # Kept for backward compatibility (currently not used)
  [string]$Name = "",

  # Which labs to verify/reset (default: all lab* folders under the day)
  [string[]]$Labs = @(),

  # By default we verify lab tests before resetting.
  [switch]$SkipVerify,

  # Optional: also remove untracked files under the lab folders (DANGEROUS).
  [switch]$CleanUntracked
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

$venvPython = Join-Path $repoRoot '.venv\Scripts\python.exe'
$pythonExe = if (Test-Path $venvPython) { $venvPython } else { 'python' }

$dayPath = Join-Path $repoRoot $Day
if (-not (Test-Path $dayPath)) {
  throw "Day folder not found: $Day"
}

if ($Labs.Count -eq 0) {
  $Labs = @(Get-ChildItem -Path $dayPath -Directory -Filter 'lab*' | Select-Object -ExpandProperty Name)
}

if ($Labs.Count -eq 0) {
  throw "No labs found under $Day (expected folders like $Day/lab1, $Day/lab2, ...)"
}

foreach ($labName in $Labs) {
  if ($labName -notmatch '^lab\d+$') {
    throw "Invalid lab name '$labName' (expected lab1/lab2/...)"
  }
}

if (-not $SkipVerify) {
  foreach ($labName in $Labs) {
    $labTestsPath = Join-Path $dayPath ("$labName\\tests")
    if (-not (Test-Path $labTestsPath)) {
      throw "Cannot verify: tests folder not found: $labTestsPath (expected $Day/$labName/tests)"
    }

    Write-Host "Verifying tests for $Day/$labName..." -ForegroundColor Cyan
    & $pythonExe -m pytest -q "$Day/$labName/tests"
    if ($LASTEXITCODE -ne 0) {
      throw "Verification failed: tests did not pass for $Day/$labName. Fix tests, then re-run submit."
    }
  }
}

Write-Host "Resetting labs back to starter code (git restore)..." -ForegroundColor Cyan

foreach ($labName in $Labs) {
  & git restore --staged --worktree "$Day/$labName"
  if ($LASTEXITCODE -ne 0) {
    throw "git restore failed for $Day/$labName. Ensure this repo is a git clone and retry."
  }

  if ($CleanUntracked) {
    & git clean -fd -- "$Day/$labName"
    if ($LASTEXITCODE -ne 0) {
      throw "git clean failed for $Day/$labName."
    }
  }
}

Write-Host "Done." -ForegroundColor Green
Write-Host "Tip: reference solutions live in $Day/solution/" -ForegroundColor Yellow
