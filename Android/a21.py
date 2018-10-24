# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 15:17:04 2018

@author: Administrator
"""

from libmccmd import cmd, dumpCpuInfo, dumpCpuSchedutil
import time

#cmd("root", 'adb root')
#time.sleep(2)


reStr = cmd("tombstones", 'adb shell ls /data/tombstones')

reStr = reStr.split()[-1]
cmd("pull {}".format(reStr), 'adb pull /data/tombstones/{}'.format(reStr))
#lists = list()



#cmd("set sched_latency_ns to 20000000", 'adb shell "echo 20000000 >/proc/sys/kernel/sched_latency_ns"')

