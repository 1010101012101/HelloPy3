# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:06:59 2018

@author: Administrator
"""

from libmccmd import cmd, dumpCpuInfo, dumpCpuSchedutil
import time

cmd("root", 'adb root')
time.sleep(2)


cmd("set scaling_governor to performance", 'adb shell "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')
cmd("set scaling_governor to performance", 'adb shell "echo performance > /sys/devices/system/cpu/cpu6/cpufreq/scaling_governor"')
#cmd("set sched_latency_ns to 20000000", 'adb shell "echo 20000000 >/proc/sys/kernel/sched_latency_ns"')


dumpCpuInfo()
