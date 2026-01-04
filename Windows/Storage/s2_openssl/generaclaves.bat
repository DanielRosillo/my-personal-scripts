@echo off

openssl genrsa -out privada.key 4096
openssl rsa -in privada.key -out publica.key -outform PEM -pubout
echo 
echo Debes enviar el  archivo publica.key para que quien te envia el archivo lo cifre. CONSERVA BAJO TOTAL SECRETO PRIVADA.KEY
echo 
