#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Rock


import paramiko
import configparser
import os
import sys
import re
###########################################
HOST = "192.168.199.191"
HOST = "10.4.19.19"

USER = "root"
PORT = 22
PASSWD = "F96AEB124C"

#############################################
ignore_str = [
    r"lastlog_openseek: Couldn't stat /var/log/lastlog: No such file or directory",
    r"\d\d\/\d\d\/\d\d\d\d.*0\/0",
    r"^\r\r\n\r\r\n",
    r"^\r\r\n"
]


def exec_ssh_cmd(server, port, username, password, cmd, log):
    receive_bytes_list = []
    try:
        import select
        # # #实例化SSHClient
        connected = True
        client = paramiko.SSHClient()
        # 自动添加策略，保存服务器的主机名和密钥信息
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 服务端，以用户名和密码进行认证
        client.connect(hostname=server, port=port,
                       username=username, password=password)
        transport = client.get_transport()
        # transport.set_keepalive(1)
        channel = transport.open_session()
        channel.get_pty(width=1024, height=500)
        # print(help(channel.get_pty))
        channel.exec_command(cmd)
        # channel.exec_command(cmd)
        while connected:
            rl, wl, xl = select.select([channel], [], [], 0.0)
            if len(rl) > 0:
                # data = channel.recv(1024)
                rb = channel.recv(4096)
                if rb:
                    connected = True
                    receive_bytes_list.append(rb)
                else:
                    connected = False
        # # # 关闭连接
        client.close()
    except Exception as e:
        print(e)

    # format receive_bytes_list
    data = ""
    for x in receive_bytes_list:
        data += x.decode("utf-8")
    for ignore in ignore_str:
        data = re.sub(ignore, r'', data)
    data = re.sub(r"\r\n", r'\n', data)

    if log:
        print(data)
    return data


def main():
    # while True:
    cmd = r'''cat /sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq&& \
              cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq&& \
              cat /sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq&& \
              cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq&& \
              cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq&& \
              cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq&& \
              cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq&& \
              cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq'''


    while True:
        exec_ssh_cmd(HOST, PORT, USER, PASSWD, cmd, True)
    # exec_ssh_cmd("192.168.199.191", 22, "root", "F96AEB124C", "ls", True)



if __name__ == '__main__':
    main()
