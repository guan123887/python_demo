#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:20:42 2019

@author: yhilly
"""

import string
import random

#(1) 生成500个随机验证码

coupon_dict = {"".join(random.choices(string.printable[:62], k = 7)) : 1
        
            for _ in range(500) }

# (2)序列化到本地
import json 

with open('coupon.json', 'w') as f:
    json.dump(coupon_dict, f)
