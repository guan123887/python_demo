#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:02:46 2019

@author: yhilly
"""

def fibonacci(xterms):
    n, a, b = 0, 0, 1
    while n < xterms:
        yield b
        a, b = b, a + b
        n = n + 1
    return '输出完毕'
