#!/bin/sh

DEST="./MetaImages"
mkdir -p "$DEST"

### FACEBOOK ###
echo "Respaldando Facebook..."
adb pull "/storage/emulated/0/Pictures/Facebook" "$DEST/Facebook"


### MESSENGER ###
echo "Respaldando Messenger..."
adb pull "/storage/emulated/0/Pictures/Messenger" "$DEST/Messenger"


echo "Respaldo Facebook + Messenger finalizado"

