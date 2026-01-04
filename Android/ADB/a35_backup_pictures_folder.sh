#!/bin/sh
DEST="./Pictures"
rm -rf $DEST
mkdir -p "$DEST"

### Pictures ###
echo "Copiando imagenes"
adb pull "/storage/emulated/0/Pictures" "$DEST/data"

echo "Respaldo de imagenes finalizado"
