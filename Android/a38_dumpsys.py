from Android.a00_utils import *


def dumpsys(name = "input"):
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")

    adb_shell('adb shell "dumpsys {}" > data/dumpsys_{}.txt'.format(name, name))


def dumpsys_input():
    dumpsys("input")


def dumpsys_list():
    adb_shell('adb shell "dumpsys -l" > data/dumpsys_list.txt')

def service_list():
    adb_shell('adb shell "service list" > data/service_list.txt')


def dumpsys_settings():
    dumpsys("settings")


def dumpsys_usagestats():
    dumpsys("usagestats")

def dumpsys_wifi():
    dumpsys("wifi")


if __name__ == "__main__":
    dumpsys_list()
    #service_list()
    #dumpsys_input()
    #dumpsys_permission()
    #dumpsys("package")
    #dumpsys("settings")
    #dumpsys("storaged")
    #dumpsys("usb")
    #dumpsys("window")
    #dumpsys("jobscheduler")
    dumpsys("media.camera")
    dumpsys("media.camera.proxy")