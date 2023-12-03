#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:40:20 2019

@author: yhilly
"""

import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

fig = plt.figure() 

axes_1 = fig.add_axes([ 0.1, 0.1, 0.5, 0.5])
axes_2 = fig.add_axes([0.2, 0.2, 0.5, 0.5])
axes_3 = fig.add_axes([0.3, 0.3, 0.5, 0.5])
axes_4 = fig.add_axes([0.4, 0.4, 0.5, 0.5])
axes_4.plot(x, y)

plt.show()