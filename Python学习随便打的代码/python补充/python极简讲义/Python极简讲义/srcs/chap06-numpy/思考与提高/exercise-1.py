# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:34:00 2019

@author: Yuhong
"""

import numpy as np

#读取数据
data = []
with open('Grid, solar, and EV data from three homes.csv','r') as file :
    lines = file.readlines() #读取数据行的数据
    for line in lines:        #对于每行数据进行分析
        temp = line.split(',')
        data.append(temp)

#分割表头
header = data[0]
#分割数据
data_np = np.array(data[1:])
#提取日期列
date = data_np[:,0]
#构造纽约市表头
NY_header = header[: 4]
#构造Austin表头
Austin_header = header[0:1] + header[4:7]
#构造Boulder表头
Boulder_header = header[0:1] + header[7:]

#分割纽约市数据
NY_data = data_np[:,: 4]
#写入纽约数据
with open ('1-NY.csv', 'w') as file:
    file.write(','.join(Austin_header) + '\n')
    for line in NY_data:
        file.write(",".join(line)  + '\n')

#Austin数据不连续，需要拼接
Austin_data = np.hstack((data_np[:,0].reshape(-1,1),data_np[:, 4 : 7]))
#写入Austin数据
with open ('1-Austin.csv', 'w') as file:
    file.write(','.join(Austin_header) + '\n')
    for line in Austin_data:
        file.write(",".join(line)  + '\n')
##Boulder数据不连续，需要拼接
Boulder_data = np.column_stack((data_np[:,0], data_np[:, 7:]))
#写入Boulder数据
with open ('1-Boulder.csv', 'w') as file:
    file.write(','.join(Boulder_header) + '\n')
    for line in Boulder_data:
        file.write(",".join(line)  + '\n')

