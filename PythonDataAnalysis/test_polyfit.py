# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:10:54 2018

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

poly = np.polyfit(x_data, y_data, deg = 1)

plt.plot(x_data, y_data, 'o')
plt.plot(x_data, np.polyval(poly, x_data))
plt.xlabel("x")
plt.ylabel("y=0.1x + 3)")
plt.legend()
plt.title("polyfit/polyval")
plt.show()



