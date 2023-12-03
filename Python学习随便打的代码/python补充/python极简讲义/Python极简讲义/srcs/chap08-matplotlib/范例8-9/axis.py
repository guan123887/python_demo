#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 20:42:45 2019

@author: yhilly
"""

#import matplotlib.pyplot as plt 
#import numpy as np

#fig, axes_lst = plt.subplots(2, 2)  

#x = np.linspace(0, 2*np.pi, 400)
#y = np.sin(x**2)
#在第1行1列的子图中绘图
#axes_lst[1, 1].plot(x, y)
#plt.subplot(2,2,4)
#plt.plot(x, y)
#plt.show()

import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)


fig = plt.figure() 

left1, bottom1, width1, height1 = 0.1, 0.1, 0.8, 0.8
axes_1 = fig.add_axes([left1, bottom1, width1, height1])
axes_1.scatter(x, y)
axes_1.set_xlabel('x')
axes_1.set_ylabel('y')
axes_1.set_title('title')


left2, bottom2, width2, height2 = 0.6, 0.6, 0.25, 0.25
axes_2 = fig.add_axes([left2, bottom2, width2, height2])
axes_2.plot(x, y)
axes_2.set_title('title inside')


plt.show()