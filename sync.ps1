$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
python build.py
if (-not (Test-Path .git)) {
    Write-Host "Pas encore un dépôt git. Lance d'abord la création du repo."
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
