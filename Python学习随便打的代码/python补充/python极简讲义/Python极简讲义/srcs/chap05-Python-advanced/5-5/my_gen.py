#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:50:21 2019

@author: yhilly
"""

def my_gen():
    print('我是第1次返回')
    yield (1)
    print('我是第2次返回')
    yield(2)
    print('我是第3次返回')
    yield(3)