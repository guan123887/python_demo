#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 15:39:43 2019

@author: yhilly
"""

import json                    #导入json模块
data = {                       #定义一个字典data
    'name'   :  'ACME',
    'shares'  :  100,
    'price'  :  542.23
}
json_str = json.dumps(data)    #将字典data序列化为json对象
print(json_str)

data1 = json.loads(json_str)
print(data1)

