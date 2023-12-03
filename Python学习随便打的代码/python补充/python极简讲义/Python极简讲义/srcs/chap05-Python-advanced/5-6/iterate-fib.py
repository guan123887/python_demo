# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:40:22 2019

@author: Yuhong
"""
from itertools import islice

from itertools import islice

class Fibonacci:
    def __init__(self):
        self.previous,  self.current = 0, 1
   
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.current        
        self.previous, self.current = self.current, self.current + self.previous      
        return value
    
f = Fibonacci()
a = list (islice(f, 0, 10))
print (a)
b = list (islice(f, 0, 10))
print (b)   
