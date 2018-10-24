# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:53:54 2018

@author: Administrator
"""


from libmccmd import cmd
import time


cmd("root", 'adb root')
time.sleep(2)


cmd("stop thermal", 'adb shell stop thermal')
