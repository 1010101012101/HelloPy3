# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:06:07 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("transcount.csv",index_col=False)
df = df.groupby("Date of introduction").aggregate(np.mean)
years = df.index.values
counts = df['Transistor count'].values
poly = np.polyfit(years, np.log(counts), deg = 1)
print("Poly", poly)
plt.semilogy(years, counts, 'o')
plt.semilogy(years, np.exp(np.polyval(poly, years)))
plt.show()