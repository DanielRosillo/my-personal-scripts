#! /bin/bash
echo ""
echo "Decifrando $1 "
mv $1 tmp.file

openssl rsautl -decrypt -inkey privada.key -in simetrica.pub -out simetrica.key
openssl enc -aes-256-cbc -d -pass file:simetrica.key -in tmp.file -out $1

rm privada.key simetrica.key simetrica.pub tmp.file
echo ""
echo "Las llaves han sido eliminadas, el archivo $1 ha sido recuperado"