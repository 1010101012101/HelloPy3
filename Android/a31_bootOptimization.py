# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 11:41:10 2018

@author: Administrator
"""

import time

def getFilter(filterFile="./data/sdm710_i7s-perf_defconfig"):
    if filterFile == None:
        return None
    
    f = open(filterFile, 'r')                           #以读方式打开文件
    result = list()  
    for line in f.readlines():                          #依次读取每行  
        line = line.strip()                             #去掉每行头尾空白  
        if not len(line) or line.startswith('#'):       #判断是否是空行或注释行  
            continue                                    #是的话，跳过不处理  
        result.append(line)                             #保存  
        result.sort()                                   #排序结果  
   # print(result)
    return result


def bootOptimization(buildType='user', filterFile="./data/filter1.txt", comText = None, outFile="./data/out.txt", ):
    if  buildType == 'user':
        srcFile = "./data/sdm710_i7s-perf_defconfig"
    elif buildType == "userdebug":
        srcFile = "./data/sdm710_i7s_defconfig"
    else:
        print("Unexpect buldType")
        return;
    outFile = srcFile + ".out"
    rmItems = getFilter(filterFile)
    if rmItems == None or len(rmItems) == 0:
        print("getFilter{} failed".format(filterFile))
        return
    
    comText = " //del by {} on ".format(comText) + time.strftime('%Y-%m-%d',time.localtime(time.time())) + "\r\n"

    print(rmItems)
    context = ""
    with open(srcFile) as rf:
        for line in rf:
            #line = line.strip()
            if not len(line.strip()) or line.startswith('#'):
                context += line
                continue
            item = line.strip().split('=')[0]
            #print(item)
            if item in rmItems:
                #print("HHHA:1======================>", item)
                line = "#" + line.strip() + comText
                print(item, "====>", line)
            context += line
            #print(len(line), line)
            
    with open(outFile, 'w') as wf:
        wf.write(context)
    print(context)
    


bootOptimization("user", "./data/filter0.txt", "mc.meng")

#getFilter()