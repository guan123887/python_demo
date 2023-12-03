# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:26:28 2019

@author: Yuhong
"""
#导入Numpy包，用于计算
import numpy as np
#导入matplotlib包，用于绘图
import matplotlib.pyplot as plt

#设置随机数种子 
np.random.seed(1)
#随机设置点的x和y坐标

x = np.random.rand(10)
y = np.random.rand(10)
 
colors = np.random.rand(10)
area = (40 * np.random.rand(20))**2

#设置散点图参数
plt.scatter(x,y,s = area, c = colors, alpha = 0.4)
#绘制散点图
plt.show()
