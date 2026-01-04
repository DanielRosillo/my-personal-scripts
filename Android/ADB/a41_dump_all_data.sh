#!/bin/sh
DEST="./Phone"
rm -rf $DEST
mkdir -p "$DEST"

### All ###
echo "Copiando informacion"
adb pull "/storage/emulated/0/" "$DEST/data"

echo "Respaldo de informacion finalizado"
