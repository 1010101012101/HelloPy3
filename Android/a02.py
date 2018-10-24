# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 17:05:09 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import time

def plotSin():
    plt.figure(1)
    x = np.arange(-5.0, 5.0, 0.02)
    y1 = np.sin(x)    
    plt.plot(x, y1)
    plt.show()
    

for i in range(10):
    plotSin()
    time.sleep(1)
    
#plt.subplot(212)
##设置x轴范围
#xlim(-2.5, 2.5)
##设置y轴范围
#ylim(-1, 1)
#plt.plot(x, y1)