#!/bin/sh
DEST="./Movies"
rm -rf $DEST
mkdir -p "$DEST"

### Movies ###
echo "Copiando videos"
adb pull "/storage/emulated/0/Movies" "$DEST/data"

echo "Respaldo de videos finalizado"
