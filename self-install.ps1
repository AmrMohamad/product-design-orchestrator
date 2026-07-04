param(
  [ValidateSet("codex", "claude", "both")][string]$Agent = "both",
  [ValidateSet("project", "user")][string]$Scope = "project",
  [string]$Project = ".",
  [ValidateSet("full", "orchestrated")][string]$Profile = "full",
  [switch]$DryRun,
  [switch]$NoGuidance,
  [switch]$ActivateGlobal,
  [switch]$Force
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonArgs = @("$Root/scripts/agent_install.py", "install", "--agent", $Agent, "--scope", $Scope, "--project", $Project, "--profile", $Profile)
if ($DryRun) { $PythonArgs += "--dry-run" }
if ($NoGuidance) { $PythonArgs += "--no-guidance" }
if ($ActivateGlobal) { $PythonArgs += "--activate-global" }
if ($Force) { $PythonArgs += "--force" }
if (Get-Command py -ErrorAction SilentlyContinue) {
  & py -3 @PythonArgs
} elseif (Get-Command python3 -ErrorAction SilentlyContinue) {
  & python3 @PythonArgs
} elseif (Get-Command python -ErrorAction SilentlyContinue) {
  & python @PythonArgs
} else {
  throw "Python 3 is required."
}
exit $LASTEXITCODE
