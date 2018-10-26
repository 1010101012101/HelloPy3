from libmccmd import adbShell

def traceSetEvents():
    adbShell('adb shell "echo 0 > /sys/kernel/debug/tracing/tracing_on"')
    adbShell('adb shell "echo > /sys/kernel/debug/tracing/trace"')
    adbShell('adb shell "echo > /d/tracing/set_event"')
    adbShell('adb shell "echo 1 > /sys/kernel/debug/tracing/events/msm_bus/bus_update_request/enable"')
    adbShell('adb shell "echo 1 > /sys/kernel/debug/tracing/events/msm_bus/bus_update_request_end/enable"')
    adbShell('adb shell "echo 1 > /d/tracing/events/rpm_smd/enable"')
    adbShell('adb shell "echo 1 > /sys/kernel/debug/tracing/events/power/clock_set_rate/enable"')
    adbShell('adb shell "echo 1 > /sys/kernel/debug/tracing/events/mdss/mdp_videw_underrun_done/enable"')
    adbShell('adb shell "echo 1 > /sys/kernel/debug/tracing/tracing_on"')
    adbShell('adb shell "cat /sys/kernel/debug/tracing/trace_pipe" > data/trace_pipe.txt')

def traceBackgound():
    #adbShell( 'adb shell "atrace -z -b 20960 -t 12 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle load sync workq memreclaim > /data/local/tmp/atrace.out &"')
    adbShell('adb shell "atrace -z -b 20960 -t 12 gfx input audio view webview wm am hal app res dalvik rs bionic power sched freq idle workq memreclaim > /data/local/tmp/atrace.out &"')


def pullAtraceFile():
    adbShell("adb pull /data/local/tmp/atrace.out")

if __name__ == "__main__":
    #traceBackgound()
    #pullAtraceFile()
    traceSetEvents()