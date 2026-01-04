@echo off

echo Cifrando %1 y simetrica.key

ren %1 file.tmp

openssl rand -base64 100 -out simetrica.key
openssl enc -aes-256-cbc -pass file:simetrica.key -in file.tmp -out %1
openssl rsautl -encrypt -in simetrica.key -out simetrica.pub -inkey publica.key -pubin

del simetrica.key publica.key file.tmp

echo 
echo Los archivos que debes enviar son:  %1 y simetrica.pub
