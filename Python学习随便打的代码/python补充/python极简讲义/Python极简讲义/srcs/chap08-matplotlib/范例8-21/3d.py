#!/usr/bin/env python
# coding=utf-8
import numpy as np 
import matplotlib.pyplot as plt 
#导入绘制三维图形模块
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(20,10))

#绘制三维曲线图
ax1 = fig.add_subplot(221,projection='3d')
theta = np.linspace(-4*np.pi,4*np.pi,500)
z = np.linspace(-2,2,500)
r = z**2 + 1
x = r*np.sin(theta)
y = r*np.cos(theta)
#方法与绘制二维曲线图相同
ax1.plot(x,y,z)
ax1.set_xlabel('x',fontsize=15)
ax1.set_ylabel('y',fontsize=15)
ax1.set_zlabel('z',fontsize=15)

#绘制三维点图
ax2 = fig.add_subplot(222,projection='3d')
x = np.random.randn(500)
y = np.random.randn(500)
z = np.random.randn(500)
#方法同二维散点图
ax2.scatter(x,y,z,c='r')
ax2.set_xlabel('x',fontsize=15)
ax2.set_ylabel('y',fontsize=15)
ax2.set_zlabel('z',fontsize=15)

#绘制三维曲面图
ax3 = fig.add_subplot(223,projection='3d')
x = np.linspace(-2,2,500)
y = np.linspace(-2,2,500)
x,y = np.meshgrid(x,y)
z = np.sqrt(x**2 + y**2)
ax3.plot_surface(x,y,z,cmap=plt.cm.winter)
ax3.set_xlabel('x',fontsize=15)
ax3.set_ylabel('y',fontsize=15)
ax3.set_zlabel('z',fontsize=15)

#绘制三维柱状图
ax4 = fig.add_subplot(224,projection='3d')
for z in np.arange(0,40,10):
    x = np.arange(20)
    y = np.random.rand(20)
    ax4.bar(x,y,zs=z,zdir='y')
ax4.set_xlabel('x',fontsize=15)
ax4.set_ylabel('y',fontsize=15)
ax4.set_zlabel('z',fontsize=15)

plt.show()
