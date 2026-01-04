#!/bin/sh
DEST="./Downloads"
rm -rf $DEST
mkdir -p "$DEST"

### Descargas ###
echo "Copiando descargas"
adb pull "/storage/emulated/0/Download" "$DEST/data"

echo "Respaldo de Descargas finalizado"
