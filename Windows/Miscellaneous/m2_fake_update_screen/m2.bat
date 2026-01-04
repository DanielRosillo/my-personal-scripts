@echo off
setlocal
:: Crear el archivo VBS
echo Set WshShell = CreateObject("WScript.Shell") > C:\Users\Public\script.vbs
echo WshShell.Run "msedge.exe --new-window {FAKE_SCREEN_URL}" >> C:\Users\Public\script.vbs
:: Esperar 3 segundos.
echo WScript.Sleep 3000 >> C:\Users\Public\script.vbs
:: Presionar f11 pantalla completa.
echo WshShell.SendKeys "{F11}" >> C:\Users\Public\script.vbs
:: Ejecutar el archivo VBS
cscript //nologo C:\Users\Public\script.vbs
:: Eliminar para no dejar rastro.
del C:\Users\Public\script.vbs
endlocal