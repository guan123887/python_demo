#!/usr/bin/env python
# coding=utf-8
import numpy as np  #导入numpy

rdm = np.random.RandomState() #定义种子类
#np.random.seed(19680101) #定义全局种子,与上面的取一种即可。

#生成2*3的二维随机数组，随机数服从均匀分布有几个参数就生成几维数据
rand = np.random.rand(2,3) 
print("rand(d0,d1,...,dn):产生均匀分布的随机数\n",rand)

randn = np.random.randn(2,3) #生成2*3的二维随机数组，随机数服从标准正态分布
print("randn(d0,d1,...,dn):产生标准正态分布的随机数\n",randn)

randint = np.random.randint(1,10,(2,3)) #生成 2*3 的1～10范围内的随机整数
print("randint(low,high,size,dtype):产生随机整数\n",randint)

random = np.random.random((2,3)) 
print("random(size):在[0,1)内产生随机数\n",random)
