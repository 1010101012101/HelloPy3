import os


def adb_shell(cmd_str, print_flag=False):
    print(cmd_str)
    restr = os.popen(cmd_str).read()
    if print_flag is True:
        print(restr)
    return restr


def lsof_lib(filename="libkeyadapter.so"):
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")

    print(adb_shell('adb shell "lsof system/lib/{}"'.format(filename)))


def lsof_lib64(filename="libkeyadapter.so"):
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")

    print(adb_shell('adb shell "lsof system/lib64/{}"'.format(filename)))


def get_pid(ps_name="system_server"):
    resStr = adb_shell('adb shell "ps -ef|grep {}"'.format(ps_name))
    pid = resStr.split()[1]
    return pid