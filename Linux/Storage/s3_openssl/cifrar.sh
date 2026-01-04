#! /bin/bash
echo "Cifrando $1 y simetrica.key" 

mv $1 file.tmp

openssl rand -base64 100 -out simetrica.key
openssl enc -aes-256-cbc -pass file:simetrica.key -in file.tmp -out $1
openssl rsautl -encrypt -in simetrica.key -out simetrica.pub -inkey publica.key -pubin

rm simetrica.key publica.key file.tmp

echo ""
echo "Los archivos que debes enviar son:  $1 y simetrica.pub"