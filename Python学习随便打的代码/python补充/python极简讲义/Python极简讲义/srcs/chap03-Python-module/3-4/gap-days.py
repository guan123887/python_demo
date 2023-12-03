# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:08:58 2019

@author: Yuhong
"""

from datetime import datetime
list_1 = ["2020-10-07",'2013-09-01']
day1 = datetime.strptime(list_1[0], '%Y-%m-%d')
day2 = datetime.strptime(list_1[1], '%Y-%m-%d')

deltadays =  day1 - day2

print(deltadays.days)