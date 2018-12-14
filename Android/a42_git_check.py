#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Rock
import subprocess
import os
import re

ignor_git_list = [
    "radio\/aop\.img",
    "scripts\/SecImage\/signed\/integrity_check\/SecImage_log\.txt",
    "ipa_fws\/secimage\.log",
    "vendor\/chioverride\/default\/g_pipelines\.h"
]


def runCommandWithOutput(cmd, stdinstr=''):
    p = subprocess.Popen(cmd, shell=True, universal_newlines=True,
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # p.stdin.write(stdinstr)
    stdoutdata, stderrdata = p.communicate(stdinstr)
    # p.stdin.close()
    return p.returncode, stdoutdata, stderrdata


cmd = "find system/ device/ packages/ vendor/ frameworks/ kernel/  -type d -name .git"
# cmd = "find vendor/  -type d -name .git"
res = runCommandWithOutput(cmd)
pwd = os.path.dirname(os.path.abspath(__file__))
git_path_dir = []
cmd_list = []

# find git dir
pat = r'(.*?).git'
git_dir_list = re.findall(pat, res[1])

for n in range(len(git_dir_list)):
    # print(n)
    cmd = "cd " + pwd + "/" + git_dir_list[n] + "&& git status"
    res = runCommandWithOutput(cmd)

    # 排除 "nothing to commit" 影响
    pat = "nothing to commit"
    rst = re.findall(pat, res[1])
    if len(rst) == 0:
        bignore = False
    	#排除忽略列表影响
        for pat_ignore in ignor_git_list:
            rst_ignore = re.findall(pat_ignore, res[1])
            if len(rst_ignore)==1:
            	bignore = True
        if bignore==False:        	
            print('\033[1;33;44m' + git_dir_list[n] + '\033[0m')
            print(res[1])
