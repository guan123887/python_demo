# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:56:43 2020

@author: Yuhong

E-mail： zhangyuhong001@gmail.com

"""

import matplotlib.pyplot as plt 
import numpy as np 
np.random.seed(0)
x = np.random.normal(0, 1, 5000) # 生成符合正态分布的5000个随机样本
plt.figure(figsize=(14,7)) #设置图片大小 14x7 inch
plt.style.use('seaborn-whitegrid') # 设置绘图风格
n, bins, patches = plt.hist(x, bins=90, facecolor = '#2ab0ff', 
                            edgecolor='#169acf', linewidth=0.5)
n = n.astype('int') # 返回值n必须是整型
# 设置显式中文的字体
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False   # 显式负号'-'
#为每个条形图设置颜色
for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(n[i]/max(n)))
#对某个特定条形（如第70个）做特别说明   
patches[49].set_fc('red') # 设置颜色
patches[49].set_alpha(1) # 设置透明度
#添加注释
plt.annotate('这是一个重要条形!', xy=(0.5, 160), xytext=(1.5, 130), fontsize=15, 
             arrowprops={'width':0.4,'headwidth':5,'color':'#333333'})
# 设置X和Y轴标题和字体大小
plt.title('正态分布', fontsize=12)
plt.xlabel('不同的间隔（bins）', fontsize=10)
plt.ylabel('频度大小', fontsize=10)
plt.show()