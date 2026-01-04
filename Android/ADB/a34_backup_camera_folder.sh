#!/bin/sh
DEST="./CAMERA"
rm -rf $DEST
mkdir -p "$DEST"

### DCIM ###
echo "Copiando fotos"
adb pull "/storage/emulated/0/DCIM/Camera" "$DEST/DCIM"

echo "Respaldo de fotos finalizado"
