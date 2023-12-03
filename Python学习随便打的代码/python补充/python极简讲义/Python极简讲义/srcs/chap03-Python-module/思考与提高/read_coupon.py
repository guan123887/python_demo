#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:34:04 2019

@author: yhilly
"""
import json,random
# (3)验证用户序列号,读入验证文件
prize = ["一双拖鞋", "一桶花生油", "一瓶水"]
with open('coupon.json', 'r') as file:
    codes = json.load(file, encoding='UTF-8')
    key = input('请输入序列号： ')
    if key in codes.keys():
        if codes[key] == 1 :
            print('此序列号可用！\n奖品为{0}'.format(random.choice(prize)))
            codes[key] = 0
        else:
            print('抱歉，此序列号不可用！\n奖品已被领走！')    
    else:
        print('此序列号不可用！')
# 将序列号更新至json文件
with open('coupon.json', 'w', encoding = 'UTF-8') as file:
    json.dump(codes, file)