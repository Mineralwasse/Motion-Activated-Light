@echo off
echo Konfiguriere Git Credential Helper...
"C:\Program Files\Git\cmd\git.exe" config --global credential.helper store
echo Initialer Fetch...
"C:\Program Files\Git\cmd\git.exe" fetch origin
echo Git Setup abgeschlossen.
pause
