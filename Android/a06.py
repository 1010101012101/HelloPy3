# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:44:13 2018

@author: Administrator
"""

from libmccmd import cmd, dumpSchedPara
import time


cmd("root", 'adb root')
time.sleep(2)

#default:0
cmd("set sched_boost to 1", 'adb shell "echo 1 >/proc/sys/kernel/sched_boost"')


cmd("sched_boost:", "adb shell cat /proc/sys/kernel/sched_boost")


