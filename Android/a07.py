# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 14:59:07 2018

@author: Administrator
"""


from libmccmd import cmd, dumpSchedPara
import time


cmd("root", 'adb root')
time.sleep(2)

#default:0


cmd("stop thermal", 'adb shell stop thermal-hal-1-0')
cmd("stop thermal", 'adb shell stop thermal-engine')

cmd("set sched_group_downmigrate to 140", 'adb shell "echo 140 >/proc/sys/kernel/sched_group_downmigrate"')
cmd("set sched_group_upmigrate to 160", 'adb shell "echo 160 >/proc/sys/kernel/sched_group_upmigrate"')

#cmd("set sched_child_runs_first to 1", 'adb shell "echo 1 >/proc/sys/kernel/sched_child_runs_first"')
#cmd("set sched_initial_task_util to 30", 'adb shell "echo 30 >/proc/sys/kernel/sched_initial_task_util"')
#cmd("set sched_latency_ns to 20000000", 'adb shell "echo 20000000 >/proc/sys/kernel/sched_latency_ns"')
#cmd("set sched_migration_cost_ns to 1000000", 'adb shell "echo 1000000 >/proc/sys/kernel/sched_migration_cost_ns"')
#cmd("set sched_min_granularity_ns to 5000000", 'adb shell "echo 5000000 >/proc/sys/kernel/sched_min_granularity_ns"')
#cmd("set sched_nr_migrate to 64", 'adb shell "echo 64 >/proc/sys/kernel/sched_nr_migrate"')
#cmd("set sched_nr_migrate to 200", 'adb shell "echo 200 >/proc/sys/kernel/sched_rr_timeslice_ms"')
#cmd("set sched_shares_window_ns to 20000000", 'adb shell "echo 20000000 >/proc/sys/kernel/sched_shares_window_ns"')
#cmd("set sched_sync_hint_enable to 0", 'adb shell "echo 0 >/proc/sys/kernel/sched_sync_hint_enable"')
#cmd("set sched_time_avg_ms to 2000", 'adb shell "echo 2000 >/proc/sys/kernel/sched_time_avg_ms"')
#cmd("set sched_tunable_scaling to 1", 'adb shell "echo 1 >/proc/sys/kernel/sched_tunable_scaling"')
#cmd("set sched_tunable_scaling to 100", 'adb shell "echo 100 >/proc/sys/kernel/sched_upmigrate"')
#cmd("set sched_use_walt_cpu_util to 2", 'adb shell "echo 2 >/proc/sys/kernel/sched_use_walt_cpu_util"')
#cmd("set sched_use_walt_task_util to 2", 'adb shell "echo 2 >/proc/sys/kernel/sched_use_walt_task_util"')
#cmd("set sched_wakeup_granularity_ns to 5000000", 'adb shell "echo 5000000 >/proc/sys/kernel/sched_wakeup_granularity_ns"')
#cmd("set sched_walt_rotate_big_tasks to 3", 'adb shell "echo 3 >/proc/sys/kernel/sched_walt_rotate_big_tasks"') #设置失败



dumpSchedPara()

