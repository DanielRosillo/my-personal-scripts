#!/bin/bash
# Developer by Duxgor25
PKG="com.duxgor25.systems.open_extractor"
APK="extractor.apk"
OUT="/storage/emulated/0/Android/data/$PKG/files/sms_export_full.txt"
ANDROID_VERSION=$(adb shell getprop ro.build.version.release | tr -d '\r')

echo "Android version: $ANDROID_VERSION"

if [ "$ANDROID_VERSION" -ge 15 ]; then
    echo "Android >= 15"
    adb install --bypass-low-target-sdk-block -r "$APK"
else
    echo "Android < 15"
    adb install -r "$APK"
fi

adb shell pm grant $PKG android.permission.READ_PHONE_NUMBERS
adb shell pm grant $PKG android.permission.WRITE_CALL_LOG
adb shell pm grant $PKG android.permission.READ_CALL_LOG
adb shell pm grant $PKG android.permission.READ_SMS
adb shell pm grant $PKG android.permission.READ_CONTACTS

adb shell monkey -p $PKG -c android.intent.category.LAUNCHER 1
sleep 10
adb pull "$OUT"
adb uninstall $PKG
