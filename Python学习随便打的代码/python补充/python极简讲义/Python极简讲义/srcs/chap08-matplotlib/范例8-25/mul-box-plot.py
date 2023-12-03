#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 10:42:59 2019

@author: yhilly
"""

import seaborn as sns, matplotlib.pyplot as plt
#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei'] 
#导入数据集合
df = sns.load_dataset("iris")
#设置x轴、y轴及数据源
ax = sns.boxplot(x = "species", y = "sepal_length", data=df)
 
# 计算每组的数据量和中位数显示的位置

#medians = df.groupby(['species'])['sepal_length'].median().values #和下面的语句等价

medians = df.pivot_table(index="species", values="sepal_length",aggfunc="median").values

#形成要显示的文本：每个子类的数量
nobs = df['species'].value_counts().values
nobs = [str(x) for x in nobs.tolist()]
nobs = ["数量: " + i for i in nobs]
 
# 设置要显示的箱体图的数量
pos = range(len(nobs))
#将文本分别显示在中位数线条的上方
for tick,label in zip(pos, ax.get_xticklabels()):
    ax.text(pos[tick], medians[tick] + 0.03, nobs[tick],
            horizontalalignment='center', size='x-small',
            color='w', weight='semibold')

plt.show()