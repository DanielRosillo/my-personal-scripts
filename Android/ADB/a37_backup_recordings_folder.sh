#!/bin/sh
DEST="./Recordings"
rm -rf $DEST
mkdir -p "$DEST"

### Recordings ###
echo "Copiando grabaciones"
adb pull "/storage/emulated/0/Recordings" "$DEST/data"

echo "Respaldo de grabaciones finalizado"
