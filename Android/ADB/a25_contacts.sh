# get
adb shell content query --uri content://contacts/people/
# count contacts
adb shell content query --uri content://contacts/people/ | wc -l
# get groups
adb shell content query --uri content://contacts/groups/
