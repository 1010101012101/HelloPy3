import os
from Android.a00_utils import *


def lsof_lib(filename="libkeyadapter.so"):
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")

    print(adb_shell('adb shell "lsof system/lib/{}"'.format(filename)))


def lsof_lib64(filename="libkeyadapter.so"):
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")

    print(adb_shell('adb shell "lsof system/lib64/{}">data/lsof_lib64_{}.txt'.format(filename, filename)))


def lsof_proc(ps_name="system_server"):
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")
    pid = get_pid(ps_name)
    adb_shell('adb shell lsof -p {} >data/lsof_proc_{}.txt'.format(pid, ps_name))


if __name__ == "__main__":
    #lsof_lib64("libmedia_helper.so")
    lsof_lib64("libkeyadapter.so")
    lsof_proc()
