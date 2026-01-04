// Reset permissions
adb shell pm reset-permissions -p your.app.package
adb shell pm grant [packageName] [ Permission] // Grant a permission to an app.
adb shell pm revoke [packageName] [ Permission] // Revoke a permission from an app.
