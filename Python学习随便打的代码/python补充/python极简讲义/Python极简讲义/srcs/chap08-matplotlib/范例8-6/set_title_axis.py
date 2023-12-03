#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(-5,5,0.05)
y1 = np.sin(x)
y2 = np.cos(x)

# 为在Matplotlib中显示中文，设置特殊字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('双曲线')

plt.ylim(-1.2,1.2)
plt.xlim(-6,6)
plt.xticks(ticks  = np.arange(-1.5 * np.pi, 2 * np.pi,0.5 * np.pi),
           labels = ['$-\\frac{3}{2}\pi$','$-\pi$','$-\\frac{1}{2}\pi$',
                     '0','$\\frac{1}{2}\pi$','$\pi$','$\\frac{3}{2}\pi$'])
plt.yticks(ticks = [-1,0,1])
plt.xlabel('我是$X$轴')
plt.ylabel('我是$Y$轴')

plt.plot(x,y1,'r-',label='$y_1=sin(x)$')
plt.plot(x,y2,'b:',label='$y_2=cos(x)$')

plt.legend(loc = 'best')
plt.figure(figsize = (9, 6), dpi=100)
plt.show()
