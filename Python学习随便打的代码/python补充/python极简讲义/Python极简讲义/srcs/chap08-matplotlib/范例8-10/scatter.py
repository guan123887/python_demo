# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:33:46 2019

@author: Yuhong
"""

import matplotlib.pyplot as plt
import numpy as np

#产生50对服从正态分布的样本点
nbPointers = 50
x = np.random.standard_normal(nbPointers)
y = np.random.standard_normal(nbPointers)

# 固定种子数，以便实验结果具有可重复性
np.random.seed(19680801)
colors = np.random.rand(nbPointers)

area = (30 * np.random.rand(nbPointers))**2 
plt.scatter(x, y, s = area, c = colors, alpha = 0.5)
plt.show()