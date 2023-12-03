#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 07:16:31 2019

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
labels = ['sepal length','sepal width','petal length','petal width']
plt.boxplot(data_np,labels=labels)
plt.show()
