#!/usr/bin/env python
# coding=utf-8


import numpy as np
import matplotlib.pyplot as plt

#pandas读取数据文件
data = pd.read_csv('iris.csv',header=None)
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
for x in range(data.columns.size - 1):
    for y in range(x+1,data.columns.size-1):
        X = data.iloc[:,x].values 
        Y = data.iloc[:,y].values
        axes[i%3][i%2].scatter(X[:50],Y[:50],
                               marker='x',c='b',label='setosa')
        axes[i%3][i%2].scatter(X[50:100],Y[50:100],
                               marker='o',c='r',label='versicolor')
        axes[i%3][i%2].scatter(X[100:],Y[100:],
                               marker='*',c='g',label='virginica')
        axes[i%3][i%2].set_xlabel(feature_name[x],fontsize = 10)
        axes[i%3][i%2].set_ylabel(feature_name[y],fontsize= 10)
        axes[i%3][i%2].legend(loc='best')
        i += 1

plt.show()
