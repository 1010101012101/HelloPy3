# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:09:24 2018

@author: Administrator
"""

import os
import time

def getCpuFreq():
    infoStr = ""
    freqList = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 8):
        freq = os.popen("adb shell cat sys/devices/system/cpu/cpu{}/cpufreq/scaling_cur_freq".format(i)).read()
        infoStr += "cpu{}:".format(i) + freq
        freqList[i] = int(freq)
    print("Freq:\n"+ infoStr)
    print(freqList)
    return freqList


def cpuFreqMonitor():
#    while True:
    for i in range(10):
        getCpuFreq()
        time.sleep(1)
        

cpuFreqMonitor()

