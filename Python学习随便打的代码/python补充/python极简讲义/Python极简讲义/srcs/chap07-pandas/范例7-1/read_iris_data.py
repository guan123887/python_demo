#!/usr/bin/env python
# coding=utf-8
import pandas as pd 

iris_data = pd.read_csv('iris.csv',sep=',',header = None)
#read_csv读取csv文件，默认分隔符为逗号，可以使用sep参数修改分隔符

print("iris_data数据类型为：")
print(type(iris_data))

columns = ['sepal_length','speal_width','peatal_leagth','petal_width','species']
iris_data.columns = columns

print("查看前面5行数据")
print(iris_data.head())

print("查看后面5行数据")
print(iris_data.tail())

print("iris_data统计信息")
print(iris_data.describe()) #返回一个DataFrame，描述数据一些统计信息

print("相关系数矩阵")
print(iris_data.corr())

print("协方差矩阵")
print(iris_data.cov())

