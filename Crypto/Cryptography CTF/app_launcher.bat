@echo off
cd /d "%~dp0" 
start cmd /k "cd ./CryptoCTF && py app.py"
timeout /t 2 /nobreak > nul
start "" http://127.0.0.1:5000