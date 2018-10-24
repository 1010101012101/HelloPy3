# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:27:52 2018

@author: Administrator
"""

from libmccmd import cmd, dumpCpuInfo, dumpCpuSchedutil
import time

cmd("root", 'adb root')
time.sleep(2)


cmd("set scaling_governor to performance", 'adb shell "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')
cmd("set scaling_governor to performance", 'adb shell "echo performance > /sys/devices/system/cpu/cpu6/cpufreq/scaling_governor"')

'''小核:'''
#cmd("set scaling_min_freq to 748800", 'adb shell "echo 748800 >/sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq"')
#cmd("set scaling_max_freq to 1612800", 'adb shell "echo 1612800 >/sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq"')


'''大核:'''
#cmd("set scaling_min_freq to 825600", 'adb shell "echo 825600 >/sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq"')


#schedutil
#cmd("set scaling_min_freq to 80", 'adb shell "echo 80 >/sys/devices/system/cpu/cpu0/cpufreq/schedutil/hispeed_load"')
#cmd("set scaling_min_freq to 80", 'adb shell "echo 80 >/sys/devices/system/cpu/cpu6/cpufreq/schedutil/hispeed_load"')


#cmd("set scaling_min_freq to 1324800", 'adb shell "echo 1324800 >/sys/devices/system/cpu/cpu0/cpufreq/schedutil/hispeed_freq"')
#cmd("set scaling_min_freq to 1536000", 'adb shell "echo 1536000 >/sys/devices/system/cpu/cpu6/cpufreq/schedutil/hispeed_freq"')

#cmd("set pl to 1", 'adb shell "echo 1 >/sys/devices/system/cpu/cpu0/cpufreq/schedutil/pl"')
#cmd("set pl to 1", 'adb shell "echo 1 >/sys/devices/system/cpu/cpu6/cpufreq/schedutil/pl"')
#cmd("set rate_limit_us to 1", 'adb shell "echo 1 >/sys/devices/system/cpu/cpu0/cpufreq/schedutil/rate_limit_us"')
#cmd("set rate_limit_us to 1", 'adb shell "echo 1 >/sys/devices/system/cpu/cpu6/cpufreq/schedutil/rate_limit_us"')



#print("HHHA:0====>")
#dumpCpuInfo(0)

print("HHHA:1====>")
dumpCpuInfo(3)
#dumpCpuSchedutil(0)
#dumpCpuSchedutil(6)