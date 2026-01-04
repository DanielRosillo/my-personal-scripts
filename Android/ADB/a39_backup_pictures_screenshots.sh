#!/bin/sh
DEST="./Screenshots"
rm -rf $DEST
mkdir -p "$DEST"

### Screenshots ###
echo "Copiando screenshots"
adb pull "/storage/emulated/0/DCIM/Screenshots" "$DEST/data"

echo "Respaldo de screenshots finalizado"
