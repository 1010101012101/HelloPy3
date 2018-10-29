import time
import os
import shutil


def adb_shell(cmd_str):
    print(cmd_str)
    return os.popen(cmd_str).read()


def pull_file(path, out_dir):
    adb_shell('adb pull {}'.format(path))
    filename = os.path.basename(path)
    src_file = os.path.join(os.getcwd(), filename)
    des_file = os.path.join(out_dir, filename)
    if os.path.exists(src_file):
        shutil.move(src_file, des_file)
    else:
        raise FileNotFoundError("get {} failed".format(path))


def log_capture_boot_speed(out_dir=None):
    '''
    开关机速度：Kernel log, events log, logcat log 及kernel configuration
    抓取方法：
    adb wait-for-device root
    adb wait-for-device
    adb shell dmesg > dmesg.txt
    adb logcat -v threadtime -b events -d > logcat_events.txt
    adb logcat -v threadtime -d *:V > logcat.txt
    :param out_dir: log output dir(default: data/log-<YYYYmmdd.HM>)
    :return: None
    '''
    out_dir = out_dir or "data/log." + time.strftime('%Y%m%d.%H%M', time.localtime(time.time()))
    os.makedirs(out_dir, exist_ok=True)
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")
    adb_shell('adb shell dmesg > {out}'.format(out=os.path.join(out_dir, "dmesg.txt")))
    adb_shell('adb logcat -v threadtime -b events -d > {}'.format(os.path.join(out_dir, "logcat_events.txt")))
    adb_shell('adb logcat -v threadtime -d *:V > {}'.format(os.path.join(out_dir, "logcat.txt")))
    #内核配置了CONFIG_IKCONFIG=y   #CONFIG_IKCONFIG_PROC=y才能从设备获取config.gz，
    #如果没配置，可以查找工程目录的out/target/product/<chipset>/obj/KERNEL_OBJ/.config
    pull_file('/proc/config.gz', out_dir)





if __name__ == "__main__":
    #log_capture_boot_speed("data/out")
    log_capture_boot_speed()