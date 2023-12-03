# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:25:33 2018

@author: Yuhong
"""

names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]

#过滤长度小于2的字符串
names_1 = [temp_str.upper() for temp_str in names if len(temp_str) > 2 ]

#首字符大写
names_2 = [name[0].upper() + name[1:].lower() for name in names_1]

print(names_2)

#方案1：
a_dict = {}
#初始化字典
for key in names_2 : 
     a_dict[key] = 0
#统计个数
for key in names_2 : 
     a_dict[key] = a_dict[key] + 1
    
print(a_dict)

'''

#方案2
#集合 去重
a_set = set(names_2)
#初始化字典value
a_dict = {name : 0 for name in a_set}
print(a_dict)

'''