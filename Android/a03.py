# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:33:20 2018

@author: Administrator
"""
import os


def doShellCmd(strcmd):
    reStr = os.popen(strcmd).read()
    print(reStr)

doShellCmd("adb shell cat sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq")

doShellCmd("adb shell stop perf-hal-1-0")
doShellCmd('adb shell "echo 1 > /sys/devices/system/cpu/cpu0/online"')
#
doShellCmd('adb shell "echo 1 > /sys/devices/system/cpu/cpu1/online"')
doShellCmd('adb shell "echo 1 > /sys/devices/system/cpu/cpu2/online"')
doShellCmd('adb shell "echo 1 > /sys/devices/system/cpu/cpu3/online"')
doShellCmd('adb shell "echo 1 > /sys/devices/system/cpu/cpu4/online"')
doShellCmd('adb shell "echo 1 > /sys/devices/system/cpu/cpu5/online"')
doShellCmd('adb shell "echo 1 > /sys/devices/system/cpu/cpu6/online"')
doShellCmd('adb shell "echo 1 > /sys/devices/system/cpu/cpu7/online"')
doShellCmd('adb shell "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')
doShellCmd('adb shell "echo performance > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor"')
doShellCmd('adb shell "echo performance > /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor"')
doShellCmd('adb shell "echo performance > /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor"')
doShellCmd('adb shell "echo performance > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor"')
doShellCmd('adb shell "echo performance > /sys/devices/system/cpu/cpu5/cpufreq/scaling_governor"')
doShellCmd('adb shell "echo performance > /sys/devices/system/cpu/cpu6/cpufreq/scaling_governor"')
doShellCmd('adb shell "echo performance > /sys/devices/system/cpu/cpu7/cpufreq/scaling_governor"')


doShellCmd('adb shell "echo 86 > /proc/sys/kernel/sched_upmigrate"')
doShellCmd('adb shell "echo 80 > /proc/sys/kernel/sched_downmigrate"')
doShellCmd('adb shell "echo 3 > /proc/sys/kernel/sched_spill_nr_run"')
doShellCmd('adb shell "echo 100000 > /proc/sys/kernel/sched_short_burst_ns"')

doShellCmd('adb shell "echo 120 > /proc/sys/kernel/sched_group_upmigrate"')
doShellCmd('adb shell "echo 100 > /proc/sys/kernel/sched_group_downmigrate"')