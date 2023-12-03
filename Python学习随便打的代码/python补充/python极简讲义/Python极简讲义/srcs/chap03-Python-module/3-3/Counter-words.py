#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:53:40 2019

@author: yhilly
"""

from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'yellow']
result = Counter(colors)
print (dict(result))

print (result.most_common(2))