@echo off
setlocal
where py >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  py -3 "%~dp0scripts\agent_install.py" install %*
  exit /b %ERRORLEVEL%
)
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
  python "%~dp0scripts\agent_install.py" install %*
  exit /b %ERRORLEVEL%
)
echo Python 3 is required. 1>&2
exit /b 127
