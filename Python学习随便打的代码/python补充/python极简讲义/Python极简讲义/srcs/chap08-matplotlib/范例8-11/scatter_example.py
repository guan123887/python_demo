#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 18:11:17 2019

@author: yhilly
"""


import matplotlib.pyplot as plt
import numpy as np
#读取数据
data = []
with open('iris.csv','r') as file :
    lines = file.readlines() #读取数据行的数据
    for line in lines:        #对于每行数据进行分析
        temp = line.split(',')
        data.append(temp)

#转换为Numpy数组，方便后续处理
data_np = np.array(data)
#不读取最后一列，并将数值部分转换为浮点数
data_np = np.array(data_np[:,:-1]).astype(float)

#特征名称
feature_name = ['sepal length','sepal width','petal length','petal width']
#绘制figure，3x2个子图，figure大小为(20,10)
fig,axes = plt.subplots(3,2,figsize=(20,10))
# 为在Matplotlib中显示中文，设置特殊字体
plt.rcParams['font.sans-serif']=['SimHei']
#设置总标题
fig.suptitle('鸢尾花散点图',fontsize=25)

#获取不同的特征组合，两两组合绘制散点图。
i = 0
for x in range(data_np.shape[1]):
    for y in range(x + 1,data_np.shape[1]):
        X = data_np[:,x]
        Y = data_np[:,y]
        axes[i%3][i%2].scatter(X[:50],Y[:50],
                               marker='x',c='b',label='setosa')
        axes[i%3][i%2].scatter(X[50:100],Y[50:100],
                               marker='o',c='r',label='versicolor')
        axes[i%3][i%2].scatter(X[100:],Y[100:],
                               marker='*',c='g',label='virginica')
        axes[i%3][i%2].set_xlabel(feature_name[x],fontsize = 10)
        axes[i%3][i%2].set_ylabel(feature_name[y],fontsize = 10)
        axes[i%3][i%2].legend(loc='best')
        i += 1

plt.show()



