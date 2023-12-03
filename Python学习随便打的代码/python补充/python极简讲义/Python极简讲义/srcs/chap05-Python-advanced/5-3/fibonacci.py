#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 17:01:16 2019

@author: yhilly
"""

def fibonacci(xterms):
    n, a, b = 0, 0, 1
    while n < xterms:
        print(b)
        a, b = b, a + b
        n = n + 1
    return '输出完毕'

fibonacci(10)
