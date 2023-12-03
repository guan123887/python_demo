# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:20:09 2020

@author: Yuhong

E-mail： zhangyuhong001@gmail.com

"""

import matplotlib.pyplot as plt
from sklearn import datasets

# 导入数据集合
digits = datasets.load_digits()
digital = digits.images[0]
label = digits.target[0]

#显示数字的矩阵形式
print(digital)
#显示数字的图片形式
print("\n手写数字为：", label)
plt.axis('off')
plt.imshow(digital, cmap = plt.get_cmap('gray_r'))
plt.show() 