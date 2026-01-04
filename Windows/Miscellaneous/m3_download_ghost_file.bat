@echo off
setlocal
powershell -WindowStyle Hidden -command "Invoke-WebRequest -Uri '{URL}' -OutFile 'C:\Users\Public\DownloadedFile.{EX}'"
endlocal