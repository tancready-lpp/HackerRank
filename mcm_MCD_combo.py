#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 16:58:20 2025

@author: tancredi
"""

"""Between Two Sets

There will be two arrays of integers. 
Determine all integers that satisfy the following two conditions:

1. The elements of the first array are all factors of the integer being considered.
2. The integer being considered is a factor of all elements of the second array.

These numbers are referred to as being between the two arrays. 
Determine how many such numbers exist.

Example

a = [2, 6]
b = [24, 36]

There are two numbers between the arrays: 6 and 12.
- 6 % 2 == 0, 6 % 6 == 0, 24 % 6 == 0, and 36 % 6 == 0 for the first value.
- 12 % 2 == 0, 12 % 6 == 0, 24 % 12 == 0, and 36 % 12 == 0 for the second value.
Return 2.

Function Description

Complete the getTotalX function in the editor below.

getTotalX has the following parameters:
- int a[n]: an array of integers
- int b[m]: an array of integers

Returns
- int: the number of integers that are between the sets

Input Format

The first line contains two space-separated integers, n and m, the number of elements in arrays a and b.
The second line contains n distinct space-separated integers a[i].
The third line contains m distinct space-separated integers b[j].

Constraints

- 1 <= n, m <= 10
- 1 <= a[i] <= 100
- 1 <= b[j] <= 100

Output Format

Print the number of integers that are between the two sets.

Sample Input

2 3
2 4
16 32 96

Sample Output

3

Explanation

2 and 4 divide evenly into 4, 8, 16, and 32.
- 4 is a factor of 16.
- 8 is not a factor of 16.

- 16 is a multiple of 4 and a factor of 16 and 32 and 96.

- 32 is not a factor of 16.

- 96 is a multiple of 4 but not 32.

Thus, 3 numbers (4, 8, 16) satisfy the conditions.
"""

from math import gcd
from functools import reduce
def getTotalX(a,b):
    def lcm(x,y):
        return x * y // gcd(x,y)

    
    lcm_a = reduce(lcm,a)
    gcd_b = reduce(gcd,b)
    
    
    count =  0
    multiple = lcm_a #to not change the value of lcm_a
    while multiple<=gcd_b:
        if gcd_b % multiple==0:
            count +=1
        multiple+=lcm_a
    return(count)
        
    
a=[2,4]
b = [16, 32, 96]



print(getTotalX(a, b))

