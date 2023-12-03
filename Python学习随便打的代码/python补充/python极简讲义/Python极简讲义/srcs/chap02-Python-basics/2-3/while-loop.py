# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:32:12 2018

@author: Yuhong
"""

numbers = [34,78,13,65,10, -8]
even = []
odd  = []
while len(numbers) > 0:
    num = numbers.pop()
    print(num,"\t")
    if (num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)
print ("Even: ", even)
print ("Odd: ", odd)
