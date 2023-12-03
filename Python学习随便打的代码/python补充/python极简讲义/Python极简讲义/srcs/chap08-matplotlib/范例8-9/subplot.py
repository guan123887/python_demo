#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:12:38 2019

@author: yhilly
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

#第一种添加子图的方法
fig = plt.figure()
axis = fig.add_subplot(211)
#plt.subplot(211)
axis.grid(True)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

#第二种添加子图的方法
plt.subplot(2,1,2)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.savefig('sub-plots.jpg',dpi=600)
plt.show()