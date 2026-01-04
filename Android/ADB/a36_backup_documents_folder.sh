#!/bin/sh
DEST="./Documents"
rm -rf $DEST
mkdir -p "$DEST"

### Documents ###
echo "Copiando documentos"
adb pull "/storage/emulated/0/Documents" "$DEST/data"

echo "Respaldo de documentos finalizado"
