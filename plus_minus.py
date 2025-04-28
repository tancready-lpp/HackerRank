#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 19:24:48 2025

@author: tancredi
"""

"""Plus Minus

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

Function Description

Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):
- int arr[n]: an array of integers

Print
Print the ratios of positive, negative, and zero values in the array. 
Each value should be printed on a separate line with 6 digits after the decimal.

Input Format

The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[i].

Constraints

- 0 < n <= 100
- -100 <= arr[i] <= 100

Output Format

Print the following 3 lines, each to 6 decimals:
1. Proportion of positive values
2. Proportion of negative values
3. Proportion of zeros

Sample Input

6
-4 3 -9 0 4 1

Sample Output

0.500000
0.333333
0.166667

Explanation

There are 6 elements in the array.
- 3 are positive: 3, 4, 1
- 2 are negative: -4, -9
- 1 is zero: 0

The proportions are:
- Positive: 3/6 = 0.500000
- Negative: 2/6 = 0.333333
- Zeros: 1/6 = 0.166667
"""


def plusMinus(arr):
    p,m,z = 0,0,0,
    for value in arr:
        if value <0 :
            m+=1
        elif value > 0:
            p+=1
        else:
            z+=1
    p/=len(arr)
    m/=len(arr)
    z/=len(arr)
    
    return print(f"{p:.6f}\n{m:.6f}\n{z:.6f}")


arr = [1,2,3,0,0,-5,-6,-7,7]

plusMinus(arr)