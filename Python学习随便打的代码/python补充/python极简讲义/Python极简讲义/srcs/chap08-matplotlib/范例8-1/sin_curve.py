# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:07:57 2019

@author: Yuhong
"""

import math
import matplotlib.pyplot as plt

#Generate a sinusoid 正弦曲线
nbSamples = 256
xRange = (-math.pi, math.pi)

x, y = [], []

for n in range(nbSamples):
    ratio = (n + 0.5) /nbSamples
    x.append(xRange[0] + (xRange[1] - xRange[0]) * ratio)
    y.append(math.sin(x[-1]))

# Plot the sinuoid
plt.plot(x, y)
plt.show()
