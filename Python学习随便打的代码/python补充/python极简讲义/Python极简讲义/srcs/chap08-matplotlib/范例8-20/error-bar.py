# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 09:24:29 2019

@author: Yuhong
"""

import math
import matplotlib.pyplot as plt
import numpy as np
#正确显示负号
plt.rcParams['axes.unicode_minus'] = False
#生成正弦曲线
x = np.linspace(-math.pi, math.pi, num = 48)
y = np.sin(x + 0.05 * np.random.standard_normal(len(x)))
y_error = 0.1 * np.random.standard_normal(len(x))

 #Axis setup
fig = plt.figure()
axis = fig.add_subplot(111) 

#绘制图形
axis.set_ylim(-0.5 * math.pi, 0.5 * math.pi)    #Set the y-axis view limits.
#plt.figure(figsize=(9, 6), dpi=100)
plt.plot(x, y, 'r--', label= 'sin(x)')
plt.errorbar(x, y, yerr = y_error,fmt='o')

plt.legend(loc = 'best')
plt.show()
