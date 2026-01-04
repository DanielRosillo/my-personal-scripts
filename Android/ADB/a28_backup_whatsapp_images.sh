#!/bin/sh
# Developer by Duxgor25
DEST="./WhatsAppImages"
rm -rf $DEST
mkdir -p "$DEST"

SRC="/storage/emulated/0/Pictures/WhatsApp"

echo "Copiando desde:"
echo "   $SRC"
echo "Hacia:"
echo "   $DEST"

adb pull "$SRC" "$DEST"

