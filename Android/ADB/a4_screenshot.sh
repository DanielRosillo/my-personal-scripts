adb exec-out screencap -p > screenshot__$(date +%Y%m%d_%H%M%S).png
adb shell screencap -p /sdcard/screenshot__$(date +%Y%m%d_%H%M%S).png