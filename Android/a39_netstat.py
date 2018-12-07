from Android.a00_utils import *


def netstat():
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")

    adb_shell('adb shell netstat -natup', True)

netstat()