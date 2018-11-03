# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:41:10 2018

@author: mc.meng

QCOM Dod:
    Optimize Kernel Configuration Application Note
    80-PJ035-1 A
    May 9, 2018
"""

import time


def get_filter(filter_file=None):
    if filter_file is None:
        return None
    
    f = open(filter_file, 'r')                           #以读方式打开文件
    result = list()  
    for line in f.readlines():                          #依次读取每行  
        line = line.strip()                             #去掉每行头尾空白  
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
            continue                                    #是的话，跳过不处理
        line = line.split('=')[0]

        result.append(line)                             #保存  
        result.sort()                                   #排序结果  
   # print(result)
    return result


def optimize_kernel_configuration(src_file='./data/sdm710_i7s-perf_defconfig', filter_lile="./data/filter1.txt", author = None, out_file=None):
    if out_file is None:
        out_file = src_file + ".out"

    rm_items = get_filter(filter_lile)
    if rm_items is None or len(rm_items) == 0:
        print("getFilter{} failed".format(filter_lile))
        return
    
    com_text = "#DEL BEGIN: by {} on ".format(author) + time.strftime('%Y-%m-%d', time.localtime(time.time())) + "\r"

    context = ""
    with open(src_file) as rf:
        for line in rf:
            #line = line.strip()
            if not len(line.strip()) or line.startswith('#'):
                context += line
                continue
            item = line.strip().split('=')[0]
            #print(item)
            if item in rm_items:
                print("HHHA:1======================>", item)

                line = com_text + "#" + line.strip() + "\r#DEL END\r"
                print(item, "====>", line)
            context += line
            #print(len(line), line)
            
    with open(out_file, 'w') as wf:
        wf.write(context)
    #print(context)
    

#kernel_config_ptimization("./data/sdm710_i7s-perf_defconfig", "./data/filter1.txt", "menghaocheng", "data/1.txt")
#kernel_config_ptimization("./data/sdm710_i7s-perf_defconfig", "./data/filter2.txt", "menghaocheng", "data/2.txt")
#kernel_config_ptimization("./data/sdm710_i7s-perf_defconfig", "./data/filter3.txt", "menghaocheng", "data/3.txt")




def optimize_configuration():
    """
    1.
    Optimize Kernel Configuration Application Note
    80-PJ035-1 A
    May 9, 2018
    2.
    ADB Commands for Debugging Performance Issues
    80-NR256-8 A
    May 9, 2018
    3.
    SDM670 Performance Tuning Checklist
    KBA-180129014006-1
    Dec 29, 2017
    """
    optimize_kernel_configuration("./data/sdm710_i7s-perf_defconfig", "./data/filter1.txt", "menghaocheng")
    optimize_kernel_configuration("./data/sdm710_i7s-perf_defconfig.out", "./data/filter1.txt", "menghaocheng")
    optimize_kernel_configuration("./data/sdm710_i7s-perf_defconfig.out.out", "./data/filter1.txt", "menghaocheng")


if __name__ == "__main__":
    optimize_configuration()

