@echo off
color 5
chcp 65001 > nul

net session >nul 2>&1
if %errorlevel%==0 goto :run_app

echo Starting with administrator privileges...
powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process -FilePath '%comspec%' -ArgumentList '/c "%~f0" %*' -Verb RunAs"
exit /B

:run_app
    set "ROOT=%~dp0..\.."
    set "PYTHON=%ROOT%\.venv\Scripts\python.exe"
    if not exist "%PYTHON%" (
        echo.
        echo [ERROR] Python not found: %PYTHON%
        echo Make sure that the virtual environment is created.
        pause
        exit /B 1
    )
    pushd "%~dp0"
    call "%PYTHON%" "main.py"
    popd
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] An error occurred while running.
        echo lol.
        pause
    )