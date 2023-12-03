#!/usr/bin/env python
# coding=utf-8
"""
Created on Tue Nov  5 06:36:50 2019

@author: yhily
"""
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(0, 10 ,1)
y = 2 * x

for a,b in zip(x,y):
    plt.text(a, b, (a,b),ha = 'center',va = 'bottom',fontsize = 8)

plt.plot(x, y, 'bo-')
plt.show()

