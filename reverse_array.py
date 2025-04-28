#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 00:04:39 2025

@author: tancredi
"""

"Your task is to reverse an array of integers."

a = [123,3,4,45,5]

def reverseArray(a):
    tmp = a.copy()
    for i in range(len(a)):
        a[i] = tmp[-i-1]
    return a
    
print(a, "input")
b = reverseArray(a)
print(b, "reverse")