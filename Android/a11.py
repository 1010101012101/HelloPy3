# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:05:18 2018

@author: Administrator
"""

from libmccmd import cmd, dumpCpuInfo, dumpCpuSchedutil, dumpsys
import time

#cmd("root", 'adb root')
#time.sleep(2)


dumpsys("surfaceflinger", "22.txt")

#dumpsys("com.antutu.ABenchMark", "22.txt")

