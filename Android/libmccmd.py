# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:27:17 2018

@author: mc.meng
"""
import os


def cmd(lable, strcmd, printFlag=True):
    reStr = os.popen(strcmd).read()
    if printFlag:
        print(lable , reStr)
    return reStr


def adbShell(strcmd):
    print(strcmd)
    return os.popen(strcmd).read()


def cat(path):
    reStr = os.popen('adb shell "cat {}"'.format(path)).read()
    print(reStr)
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


def catClockScaling():
    cmd("EMMC clk_measure:", 'adb shell "cat /d/clk/gcc_sdcc1_apps_clk/clk_measure"')
    cmd("UFS clk_measure:", 'adb shell "cat /d/clk/gcc_ufs_phy_axi_clk/clk_measure"')


def dumpClk(index):
    print('HHH1:====>/sys/class/mmc_host/mmc{}/clk_scaling"'.format(index))
    reStr = cmd("dumpCpuInfo", 'adb shell "ls /sys/class/mmc_host/mmc{}/clk_scaling"'.format(index), False)
    
    results = reStr.split()
    lists = list()
    for para in results:
        cmd(para+":", 'adb shell "cat /sys/class/mmc_host/mmc{}/clk_scaling/{}"'.format(index, para))
        lists.append(para)
    #cmd("EMMC clk_measure:", 'adb shell "cat /d/clk/gcc_sdcc1_apps_clk/clk_measure"')
    #cmd("UFS clk_measure:", 'adb shell "cat /d/clk/gcc_ufs_phy_axi_clk/clk_measure"')
    return lists


def traceBackgound():
    #adbShell( 'adb shell "atrace -z -b 20960 -t 12 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle load sync workq memreclaim > /data/local/tmp/atrace.out &"')
    adbShell('adb shell "atrace -z -b 20960 -t 12 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle workq memreclaim > /data/local/tmp/atrace.out &"')

def debugPreSet():
    adbShell('adb shell "stop thermald"')
    adbShell('adb shell "stop thermal-engine"')
    adbShell('adb shell "echo 4 > /sys/devices/system/cpu/cpu0/core_ctl/min_cpus"')
    adbShell('adb shell "echo 4 > /sys/devices/system/cpu/cpu4/core_ctl/min_cpus"')
    adbShell('adb shell "echo 1 > /sys/devices/system/cpu/cpu1/online"')
    adbShell('adb shell "echo 1 > /sys/devices/system/cpu/cpu2/online"')
    adbShell('adb shell "echo 1 > /sys/devices/system/cpu/cpu3/online"')
    adbShell('adb shell "echo 1 > /sys/devices/system/cpu/cpu4/online"')
    adbShell('adb shell "echo 1 > /sys/devices/system/cpu/cpu5/online"')
    adbShell('adb shell "echo 1 > /sys/devices/system/cpu/cpu6/online"')
    adbShell('adb shell "echo 1 > /sys/devices/system/cpu/cpu7/online"')
    adbShell('adb shell "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')
    adbShell('adb shell "echo performance > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor"')
    adbShell('adb shell "echo performance > /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor"')
    adbShell('adb shell "echo performance > /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor"')
    adbShell('adb shell "echo performance > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor"')
    adbShell('adb shell "echo performance > /sys/devices/system/cpu/cpu5/cpufreq/scaling_governor"')
    adbShell('adb shell "echo performance > /sys/devices/system/cpu/cpu6/cpufreq/scaling_governor"')
    adbShell('adb shell "echo performance > /sys/devices/system/cpu/cpu7/cpufreq/scaling_governor"')
    adbShell('adb shell "echo 1 > /sys/module/lpm_levels/parameters/sleep_disabled"')

if __name__ == "__main__":
    #dumpSchedPara()
    #dumpCpuInfo()
    #dumpGpuInfo()
    #getPid()
    #coreDump("com.ireadygo.app.systemupgrade", "debuggerd.txt")
    #bootTime()
    
    #catClockScaling()
    #dumpClk(0)
    #dumpClk(1)
    #debugPreSet()
    #dumpCpuInfo()
    traceBackgound()