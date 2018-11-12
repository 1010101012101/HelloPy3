# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 14:49:24 2018

@author: mc.meng

IO performance Debug tips
KBA-160726183346

"""

import os


def adb_shell(cmd_str):
    print("#", cmd_str)
    print(os.popen(cmd_str).read().strip())


"""
# I/O performance
  I/O performance including Benchmark, File transfer, Database operation etc. And there're aso several dementions to debug such kind of isuue.

## Benchmark
  User can run high level benchmark and driver level benchmark, to get a view of storage chipset.

# Pre-condition
  To exclude system settings influence, we need to put device at performance mode, and stop thermal-engine.Commands are:
"""
def benchmark_pre_condition():
    """
     Pre-condition
    """
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")
    adb_shell("adb shell stop thermald")
    adb_shell('adb shell "stop thermal-engine"')
    adb_shell('adb shell "echo 4 > /sys/devices/system/cpu/cpu0/core_ctl/min_cpus"')
    adb_shell('adb shell "echo 4 > /sys/devices/system/cpu/cpu4/core_ctl/min_cpus"')  # No such file or directory
    adb_shell('adb shell "echo 1 > /sys/devices/system/cpu/cpu1/online"')
    adb_shell('adb shell "echo 1 > /sys/devices/system/cpu/cpu2/online"')
    adb_shell('adb shell "echo 1 > /sys/devices/system/cpu/cpu3/online"')
    adb_shell('adb shell "echo 1 > /sys/devices/system/cpu/cpu4/online"')
    adb_shell('adb shell "echo 1 > /sys/devices/system/cpu/cpu5/online"')
    adb_shell('adb shell "echo 1 > /sys/devices/system/cpu/cpu6/online"')
    adb_shell('adb shell "echo 1 > /sys/devices/system/cpu/cpu7/online"')
    adb_shell('adb shell "echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"')
    adb_shell('adb shell "echo performance > /sys/devices/system/cpu/cpu1/cpufreq/scaling_governor"')
    adb_shell('adb shell "echo performance > /sys/devices/system/cpu/cpu2/cpufreq/scaling_governor"')
    adb_shell('adb shell "echo performance > /sys/devices/system/cpu/cpu3/cpufreq/scaling_governor"')
    adb_shell('adb shell "echo performance > /sys/devices/system/cpu/cpu4/cpufreq/scaling_governor"')
    adb_shell('adb shell "echo performance > /sys/devices/system/cpu/cpu5/cpufreq/scaling_governor"')
    adb_shell('adb shell "echo performance > /sys/devices/system/cpu/cpu6/cpufreq/scaling_governor"')
    adb_shell('adb shell "echo performance > /sys/devices/system/cpu/cpu7/cpufreq/scaling_governor"')
    adb_shell('adb shell "echo 1 > /sys/module/lpm_levels/parameters/sleep_disabled"')




"""
## Benchmark
Androbench and A1 SD Bench is popular for high level benchmark.
dd and iozone is useful for driver level benchmark.
It's IMPORTANT to test with different benchmark parameters set, including bs (block size), count, 
fs(file size). Different parameters would get different result, and get reflect the storage chip 
performance with defferent settings.
It's also IMPORTANT that which partition is to benchmark. Though both are storage benchmark,
but run on /data and /sdcard partition could get complete different result.
After benchmark, compares the result to storage chip specification if this is the limitation from chip
itself.

# debug tips
## Clock rate 
Once the driver level benchmark result is not so good, then we need to check clock rate first.
## Turn off clock scaling
"""
def turn_off_clok_scaling(mem_type="EMMC"):
    if mem_type == "EMMC":
        adb_shell('adb shell "echo 0 > /sys/class/mmc_host/mmc0/clk_scaling/enable')
        adb_shell('adb shell "echo 0 > /sys/class/mmc_host/mmc1/clk_scaling/enable')
    elif mem_type == "UFS":
        adb_shell('adb shell "echo 0 > /sys/class/scsi_host/host0/../../../clkscale_enable"')
    else:
        print("Unsupported memory type:%"%(mem_type))


"""
## Get clock rate
EMMC
cat /d/clk/gcc_sdcc1_apps_clk/measure
UFS
cat /d/clk/gcc_ufs_axi_clk/measure
"""
def get_clock_rate(mem_type="EMMC"):
    """
    Get clock rate
    """
    reval = ""
    if mem_type == "EMMC":
        reval = adb_shell('adb shell "cat /d/clk/gcc_sdcc1_apps_clk/clk_measure"')
    elif mem_type == "UFS":
        reval = adb_shell('adb shell "cat /d/clk/gcc_ufs_axi_clk/measure"')
    else:
        print("Unsupported memory type:%s"%(mem_type))
    print(reval)

"""
Chekc if chip could run at fmax as expected, and check if clock rate has influence on benchmark result. 
"""
"""
## Storage parameters
For some real use cases, we need to check storage parameters and comare with Qualcomm original design.
They are:
 - max_hw_sectors_kb
 - max_integrity_segments
 - max_sectors_kb
 - max_segment_size
 - max_segments
 - minimum_io_size
 - read_ahead_kb
 - scheduler
The read_ahead_kb value has obvious impact the file transfer performance, try to increase 
or decrease it and compare the result, make it well-tuned. 
"""

def get_storage_parameters(blk_name="mmcblk0"):
    print(adb_shell('adb shell "cat /sys/block/{}/queue/max_hw_sectors_kb"'.format(blk_name)))
    adb_shell('adb shell "cat /sys/block/{}/queue/max_integrity_segments"'.format(blk_name))
    adb_shell('adb shell "cat /sys/block/{}/queue/max_sectors_kb"'.format(blk_name))
    adb_shell('adb shell "cat /sys/block/{}/queue/max_segment_size"'.format(blk_name))
    adb_shell('adb shell "cat /sys/block/{}/queue/max_segments"'.format(blk_name))
    adb_shell('adb shell "cat /sys/block/{}/queue/minimum_io_size"'.format(blk_name))
    adb_shell('adb shell "cat /sys/block/{}/queue/read_ahead_kb"'.format(blk_name))
    adb_shell('adb shell "cat /sys/block/{}/queue/scheduler"'.format(blk_name))


def set_storage_parameters(blk_name="mmcblk0"):
    adb_shell("adb wait-for-device root")
    adb_shell("adb wait-for-device")
    #adb_shell('adb shell "echo 512 > /sys/block/{}/queue/minimum_io_size"'.format(blk_name))
    adb_shell('adb shell "echo 2048 > /sys/block/{}/queue/read_ahead_kb"'.format(blk_name))
    #adb_shell('adb shell "echo 268435456 > /sys/block/{}/queue/discard_max_bytes"'.format(blk_name))
    #adb_shell('adb shell "echo 512 > /sys/block/{}/queue/max_sectors_kb"'.format(blk_name))
    #adb_shell('adb shell "echo 1 > /sys/block/{}/queue/nomerges"'.format(blk_name))
    #adb_shell('adb shell "echo write throught > /sys/block/{}/queue/write_cache"'.format(blk_name))
    adb_shell('adb shell "echo 1 > /sys/block/{}/queue/rq_affinity"'.format(blk_name))
    adb_shell('adb shell "echo 1 > /sys/block/{}/queue/rotational"'.format(blk_name))




if __name__ == "__main__":
    benchmark_pre_condition()
    turn_off_clok_scaling()
    #get_clock_rate()
    set_storage_parameters()
    #get_storage_parameters()
