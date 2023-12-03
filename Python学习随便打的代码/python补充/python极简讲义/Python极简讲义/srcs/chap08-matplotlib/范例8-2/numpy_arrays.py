# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:31:26 2018

@author: Yuhong
"""


import math
import matplotlib.pyplot as plt
import numpy as np

#Generate a sinusoid 正弦曲线
nbSamples  = 256
x = np.linspace(-math.pi, math.pi, num = 256)
y = np.sin(x)

# Plot the sinuoid
plt.plot(x, y)
plt.show()