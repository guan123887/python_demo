# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:30:36 2019

@author: Yuhong
"""

import csv
import numpy as np
from datetime import datetime

filename = ['1-NY.csv', '1-Austin.csv', '1-Boulder.csv']

def power_stats(file):
    #读取文件数据
    with open(file,'r') as f:
        reader = csv.reader(f)
        #跳过空行
        data = [line for line in reader if len(line) > 0 ]
    #除掉表头，提取数据
    np_array = np.array(data[1:]) 
    #分割日期
    dates_str = np_array[:, 0] 
    #分割用电数据
    elec_data = np_array[:, 1:]  
    #数据预处理，否则类型转换会出错
    elec_data[elec_data == ''] = '0' 
    #转换数据类型
    elec_data = elec_data.astype(float)  
    
    #转换为日期对象
    dates = [datetime.strptime(date,'%Y/%m/%d %H:%M') for date in dates_str]
    #并提取三月份的数据索引
    index_month3 = [date.month == 3 for date in dates]
    index_month4 = [date.month == 4 for date in dates]
    index_month5 = [date.month == 5 for date in dates]
    
    elec3 = elec_data[index_month3] 
    elec4 = elec_data[index_month4] 
    elec5 = elec_data[index_month5]
    
    month3_ratio = np.sum(elec3, axis = 0) / np.sum(elec3)
    month4_ratio = np.sum(elec4, axis = 0) / np.sum(elec4)
    month5_ratio = np.sum(elec5, axis = 0) / np.sum(elec5)
    
    return month3_ratio, month4_ratio, month5_ratio

out = []
[out.extend(power_stats(file)) for file in filename]
with open('./3.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(out)
