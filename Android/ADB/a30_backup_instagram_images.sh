#!/bin/sh
DEST="./InstagramImages"
mkdir -p "$DEST"

### Descargas ###
echo "Copiando descargas de Instagram..."
adb pull "/storage/emulated/0/Download/Instagram" "$DEST/Download"

### Publicaciones propias ###
echo "Copiando publicaciones guardadas..."
adb pull "/storage/emulated/0/Download/Instagram" "$DEST/Pictures"

echo "Respaldo de Instagram finalizado"
