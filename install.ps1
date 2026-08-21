# Installs AI-Mise under a name you choose, so that name is what you type.
# Touches only your own skills folders.

$ErrorActionPreference = 'Stop'
$here = (Get-Location).Path
$src  = Join-Path $PSScriptRoot 'skills\ai-mise'
if (-not (Test-Path (Join-Path $src 'SKILL.md'))) {
  Write-Host 'Run this from the repository root.'; exit 1
}

$raw = Read-Host 'What would you like to call it? [ai-mise]'
if ([string]::IsNullOrWhiteSpace($raw)) { $raw = 'ai-mise' }

$name = [regex]::Replace($raw.ToLower(), '[^a-z0-9]+', '-').Trim('-')
if ($name.Length -gt 64) { $name = $name.Substring(0, 64).Trim('-') }
if ([string]::IsNullOrEmpty($name)) {
  Write-Host 'That leaves nothing usable. Letters and numbers work best.'; exit 1
}
if ($name -ne $raw) {
  Write-Host "Using '$name' - the format allows lowercase letters, numbers and hyphens."
}

$roots = @((Join-Path $HOME '.claude\skills'), (Join-Path $HOME '.agents\skills'))

foreach ($root in $roots) {
  if (Test-Path (Join-Path $root $name)) {
    Write-Host "$(Join-Path $root $name) already exists. Nothing was touched."
    Write-Host 'Choose another name, or move that folder aside first.'
    exit 1
  }
}

foreach ($root in $roots) {
  $dest = Join-Path $root $name
  New-Item -ItemType Directory -Path $dest -Force | Out-Null
  Copy-Item -Path (Join-Path $src '*') -Destination $dest -Recurse -Force
  $skill = Get-Content (Join-Path $src 'SKILL.md') -Raw
  $skill = [regex]::Replace($skill, '(?m)^name: .*$', "name: $name")
  Set-Content -Path (Join-Path $dest 'SKILL.md') -Value $skill -NoNewline
  Write-Host "installed  $dest"
}

Write-Host ''
Write-Host "Type /$name in Claude Code, `$$name in Codex, /$name in Grok Build."
$zip = Join-Path $here "$name.zip"
Compress-Archive -Path (Join-Path $roots[0] $name) -DestinationPath $zip -Force
Write-Host "wrote      $zip"
Write-Host 'For Claude on your phone: upload that at claude.ai, Customize, Skills.'
Write-Host 'To remove it, delete the folders named above. Nothing else was changed.'
