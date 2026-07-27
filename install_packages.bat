@echo off
chcp 65001 > nul
echo Installing required libraries: pywebview, colorama, tomli-w...s
echo.

python -m pip install --upgrade pip
python -m pip install pywebview colorama tomli-w

if %errorlevel% equ 0 (
    echo.
    echo Successfully installed the required libraries.
) else (
    echo.
    echo Error occurred while installing the required libraries.
)

echo.
pause