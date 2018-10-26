from libmccmd import cmd, dumpCpuInfo, dumpCpuSchedutil, dumpClk
import time

cmd("root", 'adb root')
time.sleep(2)


reStr = cmd("set enable to 0:", 'adb shell "echo 0 >/sys/class/mmc_host/mmc0/clk_scaling/enable"')
reStr = cmd("set enable to 0:", 'adb shell "echo 0 >/sys/class/mmc_host/mmc1/clk_scaling/enable"')

dumpClk(0)