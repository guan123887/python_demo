#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
nbSamples = 128

x = np.linspace(-np.pi,np.pi,nbSamples)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,color='g',linewidth=4,linestyle='--',label=r'$y=sin(x)$')
plt.plot(x,y2,'*',markersize=8,markerfacecolor='r',
         markeredgecolor='k',label=r'$y=cos(x)$')

plt.legend(loc='best')
plt.show()
