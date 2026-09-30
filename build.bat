@echo off
setlocal
chcp 65001 > nul
REM ===========================================================================
REM  MSF_Respect_V build  --  just double-click this file.
REM
REM  No SCMDraft compile and no EUD Editor (e3s) build needed:
REM      1) tepc     : main.lua -> triggers  (map: "Respect V_BGM.scx" in this folder)
REM      2) euddraft : EUD Editor data copied in build\  (DataEditor, RequireData, tbl)
REM                    sounds come from C:\euddraft0.9.2.0\Respect_V_BGM
REM      3) CPLP     : protector  ->  *_out.scx  (the map to play)
REM
REM  Output goes to  C:\Program Files (x86)\StarCraft\Maps\
REM  Terrain/units changed?   save "Respect V_BGM.scx" in SCMDraft, then run this again.
REM  EUD Editor data changed? build once in EUD Editor, then:  build.bat --refresh-data
REM  Only the trigger step:   build.bat --tepc-only
REM  Keep this file ASCII-only: the console codepage mangles anything else.
REM ===========================================================================

set "PROJ=%~dp0"
if "%PROJ:~-1%"=="\" set "PROJ=%PROJ:~0,-1%"

where python >nul 2>nul
if errorlevel 1 (
    echo [build] python was not found in PATH.
    goto :fail
)
if not exist "%PROJ%\tools\build.py" (
    echo [build] tools\build.py is missing.
    goto :fail
)

REM  Some setups set NoDefaultCurrentDirectoryInExePath=1, which makes cmd
REM  refuse bare exe names. Clear it for child processes.
set "NoDefaultCurrentDirectoryInExePath="
set "PYTHONIOENCODING=utf-8"

echo.
echo  ========================================================
echo   MSF_Respect_V  full build  (tepc -^> euddraft -^> CPLP)
echo  ========================================================
echo.

python "%PROJ%\tools\build.py" %*

if %ERRORLEVEL% NEQ 0 goto :fail

echo.
echo  ========================================================
echo   DONE.  Play the *_out.scx file:
echo.
dir /b "C:\Program Files (x86)\StarCraft\Maps\*RESPECT_V_Test*.scx" 2>nul
echo  ========================================================
echo.
pause
exit /b 0

:fail
echo.
echo [build] FAILED - the error is printed above.
pause
exit /b 1
