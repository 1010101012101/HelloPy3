# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:49:24 2018

@author: mc.meng
"""

import os


def adb_shell(cmd_str):
    print(cmd_str)
    return os.popen(cmd_str).read()


def trace_background():
    """
    Issue not seen with USB/Wifi/Charger connected
    1.connect USB
    2. adb shell
    3. atrace -z -b 20960 -t 12 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle load sync workq memreclaim > /data/local/tmpatrace.out &
    4. Unplug USB and reproduce your issue
    5. adb pull /data/local/tmp/atrace.out
    6. python systrace.py --from-file atrace.out
    7. Note:
        a)-b is for buffer size and -t is for atrace duration in second, -z is for compress; you may have to repeat step 3 several times until your issue reproduced
        b)if you atrace runs failed, please run atrace -list to list all supported categories, and change your atrace parameter accordingly.
    """

    #adb_shell('adb shell "atrace -z -b 20960 -t 12 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle load sync workq memreclaim > /data/local/tmpatrace.out &"')


def low_frequency_issue():
    """
    Consider to run atrace with async style
    1. Connect USB
    2. adb shell atrace --async_start -z -b 20960 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle load sync workq memreclaim
    3. Unplug USB and reproduce your issue
    4. Once issue get replicated, plugin USB immediately and run
    5. adb shell atrace --async_dump -z -b 20960 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle load sync workq memreclaim > atrace.out
    6. python systrace/systrace.py --from-file atrace.out
    """


def crash_issue():
    """
    Consider to run atrace background,steps
    1. Connect USB
    2. adb shell
    3. atrace -z -b 20960 -t 12 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle load sync workq memreclaim > /data/local/tmp/atrace.out &
    4. Unplug USB and reproduce your issue
    5. Provide ramdump to Qualcomm with your issue replicated
    """


def tracing_set_events_settings():
    """
    Most kernel modules have tracing configuration, customer can switch on/off tracing event accordingly.
    For example, if you only care about buss vote, following settings is preferred.
    :return:
    """
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")
    adb_shell('adb shell "echo 0 > /sys/kernel/debug/tracing/tracing_on')
    adb_shell('adb shell "echo > /sys/kernel/debug/tracing/trace')
    adb_shell('adb shell "echo > /d/tracing/set_event"')
    adb_shell('adb shell "echo 1 > /sys/kernel/debug/tracing/events/msm_bus/bus_update_request/enable"')
    adb_shell('adb shell "echo 1 > /sys/kernel/debug/tracing/events/msm_bus/bus_update_request_end/enable"')
    adb_shell('adb shell "echo 1 > /d/tracing/events/rpm_smd/enable"')  # 该文件找不到
    adb_shell('adb shell "echo 1 > /sys/kernel/debug/tracing/events/power/clock_set_rate/enable"')  # 该文件找不到
    adb_shell('adb shell "echo 1 > /sys/kernel/debug/tracing/tracing_on"')
    adb_shell('adb shell "cat /sys/kernel/debug/tracing/trace_pipe > data/trace_pipe.txt"')


def reference():
    """
    SYSTRACE LOGGING(80-P0803-2)
    http://developer.android.com/tools/help/systrace.html
    :return:
    """

if __name__ == "__main__":
    tracing_set_events_settings()
