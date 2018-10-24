# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:28:29 2018

@author: Administrator
"""

from libmccmd import cmd
import time


cmd("root", 'adb root')
time.sleep(2)

#sched_upmigrate default:96
#cmd("set sched_upmigrate to 90", 'adb shell "echo 90 >/proc/sys/kernel/sched_upmigrate"')
#sched_downmigrate default:90
#cmd("set sched_downmigrate to 80", 'adb shell "echo 80 >/proc/sys/kernel/sched_downmigrate"')
#sched_group_downmigrate default:120
cmd("set sched_group_downmigrate to 140", 'adb shell "echo 140 >/proc/sys/kernel/sched_group_downmigrate"')
#sched_group_upmigrate default:140
cmd("set sched_group_upmigrate to 160", 'adb shell "echo 160 >/proc/sys/kernel/sched_group_upmigrate"')


cmd("sched_downmigrate:", "adb shell cat /proc/sys/kernel/sched_downmigrate")
cmd("sched_upmigrate:", "adb shell cat /proc/sys/kernel/sched_upmigrate")
cmd("sched_group_downmigrate:", "adb shell cat /proc/sys/kernel/sched_group_downmigrate")
cmd("sched_group_upmigrate:", "adb shell cat /proc/sys/kernel/sched_group_upmigrate")
