DEST="./ScreenRecords"
mkdir -p "$DEST"

adb shell screenrecord --time-limit 60 --verbose /storage/emulated/0/demo.mp4
adb pull "/storage/emulated/0/demo.mp4" "$DEST"

