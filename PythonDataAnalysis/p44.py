# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:48:55 2018

@author: Administrator
"""

import scipy.misc
import matplotlib.pyplot as plt
import numpy as np

lena = scipy.misc.ascent()

def get_indices(size):
    arr = np.arange(size)
    return arr % 4 == 0

lena1 = lena.copy()
xindices = get_indices(lena.shape[0])
yinidces = get_indices(lena.shape[1])
lena1[xindices, yinidces] = 0
plt.subplot(211)
plt.imshow(lena1)
lena2 = lena.copy()
lena2[(lena > lena.max()/4) & (lena < 3*lena.max()/4)] = 0
plt.subplot(212)
plt.imshow(lena2)
plt.show()
