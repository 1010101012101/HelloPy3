import os


def adb_shell(cmd_str):
    print(cmd_str)
    return os.popen(cmd_str).read()


def get_pid(ps_name="system_server"):
    resStr = adb_shell('adb shell "ps -ef|grep {}"'.format(ps_name))
    pid = resStr.split()[1]
    return pid


def simpleperf(ps_name="system_server"):
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")
    pid = get_pid(ps_name)
    adb_shell('adb shell "simpleperf record -p {} -o data/perf.data --duration 10"'.format(pid))
    adb_shell('adb shell "simpleperf report -i data/perf.data">data/perf.data')


if __name__ == "__main__":
    simpleperf("system_server")