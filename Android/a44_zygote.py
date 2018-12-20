"""
3.3.1 Zygote守护进程的启动

在init.rc中，通过init进程启动了Zygote服务：

service zygote/system/bin/app_process -Xzygote /system/bin --zygote --start-system-server

    socket zygote stream 666

……

通过上面init.rc的代码可知。Zygote服务相应程序为/system/bin/app_process。服务名为zygote，參数列表为：-Xzygote/system/bin --zygote --start-system-server。

在启动zygote 服务时，在/dev/socket/文件夹下建立一个streamsocket文件：zygote。权限为666。

我们能够通过以下的命令来查找Zygote进程的源代码：

find ./ -nameAndroid.mk  -exec grep -l app_process {}\;

注：find命令用于查找一个文件，-exec  xxx {} \;表示：在前面命令的结果里执行grep 命令。

由上述命令结果可知，Zygote进程代码为frameworks/base/cmds/app_process/app_main.cpp

找到该程序的main入口函数：

"""