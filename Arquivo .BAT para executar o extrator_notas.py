@echo off
chcp 65001 > nul
title Extrator de Notas Fiscais - Minelli Engenharia

echo ========================================
echo   EXTRATOR DE NOTAS FISCAIS
echo   Minelli Engenharia
echo ========================================
echo.

echo Verificando Python...
python --version > nul 2>&1
if errorlevel 1 (
    echo ERRO: Python não encontrado!
    echo.
    echo Por favor, instale o Python 3.8 ou superior:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo Python encontrado! Iniciando extrator...
echo.

python extrator_notas.py

pause
