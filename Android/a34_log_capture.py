
import time
import os
import shutil


def adb_shell(strcmd):
    print(strcmd)
    return os.popen(strcmd).read()


def pull_file(path, out_dir):
    adb_shell('adb pull {}'.format(path))
    filename = os.path.basename(path)
    src_file = os.path.join(os.getcwd(), filename)
    des_file = os.path.join(out_dir, filename)
    if os.path.exists(src_file):
        shutil.move(src_file, des_file)
    else:
        raise FileNotFoundError("get {} failed".format(path))


def log_capture_boot_speed(out_dir=None, zip=False):
    '''
    抓取开机速度日志及kernel configuration
    :param out_dir: 日志输出目录
    :return: 无
    '''
    out_dir = out_dir or "data/log-" + time.strftime('%Y-%m-%d', time.localtime(time.time()))
    os.makedirs(out_dir, exist_ok=True)
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")
    adb_shell('adb shell dmesg >{out}'.format(out=os.path.join(out_dir, "dmesg.txt")))
    adb_shell('adb logcat -v threadtime -b events -d >{}'.format(os.path.join(out_dir, "logcat_events.txt")))
    adb_shell('adb logcat -v threadtime -d *:V >{}'.format(os.path.join(out_dir, "logcat.txt")))
    adb_shell('/proc/config.gz', out_dir)



if __name__ == "__main__":
    log_capture_boot_speed("data/out")
