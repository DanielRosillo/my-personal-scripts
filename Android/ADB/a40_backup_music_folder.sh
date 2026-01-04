#!/bin/sh
DEST="./Music"
rm -rf $DEST
mkdir -p "$DEST"

### Music ###
echo "Copiando musica"
adb pull "/storage/emulated/0/Music" "$DEST/data"

echo "Respaldo de musica finalizado"
