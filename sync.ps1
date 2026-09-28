$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
python generate.py
Set-Location site
if (-not (Test-Path node_modules)) { npm install }
npm run build
Set-Location $PSScriptRoot
if (-not (Test-Path .git)) {
    Write-Host "Pas encore un dépôt git."
    exit 1
}
git add -A
git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "Rien de nouveau."
    exit 0
}
git commit -m "Met à jour la documentation depuis Rivals BP."
git push
