# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:34:58 2018

@author: Administrator
"""


from libmccmd import cmd, dumpCpuInfo, dumpCpuSchedutil, dumpClk
import time

cmd("root", 'adb root')
cmd("adb wait-for-device", "adb wait-for-device")
time.sleep(2)


reStr = cmd("set enable to 0:", 'adb shell "echo 0 >/sys/class/mmc_host/mmc0/clk_scaling/enable"')
reStr = cmd("set enable to 0:", 'adb shell "echo 0 >/sys/class/mmc_host/mmc1/clk_scaling/enable"')

#reStr = cmd("set enable to 0:", 'adb shell "echo 10 >/sys/class/mmc_host/mmc0/clk_scaling/down_threshold"')
#reStr = cmd("set enable to 0:", 'adb shell "echo 10 >/sys/class/mmc_host/mmc1/clk_scaling/down_threshold"')

#reStr = cmd("set enable to 0:", 'adb shell "echo 28 >/sys/class/mmc_host/mmc0/clk_scaling/up_threshold"')
#reStr = cmd("set enable to 0:", 'adb shell "echo 28 >/sys/class/mmc_host/mmc1/clk_scaling/up_threshold"')

#reStr = cmd("set enable to 0:", 'adb shell "echo 200 >/sys/class/mmc_host/mmc0/clk_scaling/polling_interval"')
#reStr = cmd("set enable to 0:", 'adb shell "echo 200 >/sys/class/mmc_host/mmc1/clk_scaling/polling_interval"')

dumpClk(0)
dumpClk(1)