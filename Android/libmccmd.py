# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:27:17 2018

@author: Administrator
"""
import os

def cmd(lable, strcmd, printFlag=True):
    reStr = os.popen(strcmd).read()
    if printFlag:
        print(lable , reStr)
    return reStr


def dumpSchedPara():
    reStr = cmd("dumpSchedPara:", 'adb shell "ls /proc/sys/kernel/"', False)
    
    results = reStr.split()
    lists = list()
    for para in results:
        if not para.startswith("sched"):
            continue
        cmd(para+":", 'adb shell cat /proc/sys/kernel/{}'.format(para))
        lists.append(para)
    #print(lists)

def dumpCpuInfo(index=0):
    reStr = cmd("dumpCpuInfo", 'adb shell "ls /sys/devices/system/cpu/cpu{}/cpufreq"'.format(index), False)
    
    results = reStr.split()
    lists = list()
    for para in results:
        if not para.startswith("scaling"):
            continue
        cmd(para+":", 'adb shell cat ls /sys/devices/system/cpu/cpu{}/cpufreq/{}'.format(index, para))
        lists.append(para)
    #print(lists)

def dumpCpuSchedutil(index=0):
    reStr = cmd("dumpCpuInfo", 'adb shell "ls /sys/devices/system/cpu/cpu{}/cpufreq/schedutil"'.format(index), False)
    
    results = reStr.split()
    lists = list()
    for para in results:
        #if not para.startswith("scaling"):
        #    continue
        cmd(para+":", 'adb shell cat ls /sys/devices/system/cpu/cpu{}/cpufreq/schedutil/{}'.format(index, para))
        lists.append(para)
    #print(lists)

def dumpGpuInfo():
    reStr = cmd("dumpGpuInfo", 'adb shell "ls /sys/class/kgsl/kgsl-3d0/devfreq"', False)
    
    results = reStr.split()
    lists = list()
    for para in results:
        #if not para.startswith("scaling"):
        #    continue
        cmd(para+":", 'adb shell cat ls /sys/class/kgsl/kgsl-3d0/devfreq//{}'.format(para))
        lists.append(para)
    print(lists)
    

def dumpsys(para="surfaceflinger", outFile="1.txt"):
    reStr = cmd("dump {}".format(para), 'adb shell dumpsys meminfo {}'.format(para))
    with open(outFile, 'w') as wf:
        wf.write(reStr)
    
    
def getPid(para="com.ireadygo.app.systemupgrade"):
    reStr = cmd("#ps |grep{}:\r\n".format(para).format(para), 'adb shell "ps|grep {}"'.format(para))
    reStr = reStr.split()[2]
    print("PID:", reStr)
    return reStr

def coreDump(para, outFile="1.txt"):
    pid = getPid(para)
    cmd("debuggerd [{}]:".format(para), 'adb shell "debuggerd -b {}" > {}'.format(pid, outFile))
    #with open(outFile, 'w') as wf:
    #    wf.write(reStr)



def bootTime(outFile="1.txt"):
    reStr = cmd("bootTime:", 'adb shell "logcat -b events|grep boot"')
    with open(outFile, 'w') as wf:
        wf.write(reStr)
    
if __name__ == "__main__":
    #dumpSchedPara()
    #dumpCpuInfo()
    #dumpGpuInfo()
    #getPid()
    #coreDump("com.ireadygo.app.systemupgrade", "debuggerd.txt")
    bootTime()