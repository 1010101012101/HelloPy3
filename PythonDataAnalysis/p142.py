# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:05:57 2018

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("transcount.csv")
df = df.groupby("Date of introduction").aggregate(np.mean)

gpu = pd.read_csv("gpu_transcount.csv")
gpu = gpu.groupby("Date of introduction").aggregate(np.mean)

df = pd.merge(df, gpu, how="outer", left_index=True, right_index=True)
df = df.replace(np.nan, 0)

print(df)
years = df.index.values
counts = df['Transistor count_x'].values
gpu_counts = df['Transistor count_y'].values
cnt_log= np.log(counts)
plt.scatter(years, cnt_log, c = 200*years, s=20+200*gpu_counts/gpu_counts.max(), alpha=0.5)
plt.show()
