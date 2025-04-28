#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 11:01:42 2025

@author: tancredi
"""

"""Kangaroo

You are choreographing a circus show with various animals. 
For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e., toward positive infinity).

- The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
- The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.

You have to figure out whether they will land at the same location at the same time. 
Write a function to return YES if they can land on the same location at the same time; otherwise, return NO.

Function Description

Complete the kangaroo function in the editor below.

kangaroo has the following parameters:
- int x1, int v1: starting position and jump distance for kangaroo 1
- int x2, int v2: starting position and jump distance for kangaroo 2

Returns
- string: either "YES" or "NO"

Input Format

A single line of four space-separated integers denoting the respective values of x1, v1, x2, and v2.

Constraints

- 0 <= x1 < x2 <= 10000
- 1 <= v1 <= 10000
- 1 <= v2 <= 10000

Output Format

Print YES if they can land on the same position at the same time; otherwise, print NO.

Sample Input 0

0 3 4 2

Sample Output 0

YES

Explanation 0

The two kangaroos jump through the following sequence of locations:

Kangaroo 1 moves: 0 → 3 → 6 → 9 → 12 → 15
Kangaroo 2 moves: 4 → 6 → 8 → 10 → 12 → 14

They both land at 6 on the second jump.
"""


def kangaroo(x1, v1, x2, v2):
    steps = 0
    if 1 <= v1 <= 1e4 and 1 <= v2 <= 1e4:
        while x1 != x2 and 0 <= x1 <= 1e4 and 0 <= x2 <= 1e4:
            x1 += v1
            x2 += v2
            steps += 1
        if 0 <= x1 <= 1e4 and x1 == x2: # recheck that they are equal because the while has more conditions!!!
            return print("YES")
        return print("NO")
    

def kangaroo_math(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    else:
        t = (x2 - x1) / (v1 - v2)
        if t >= 0 and t.is_integer():
            return "YES"
        else:
            return "NO"



kangaroo(1571, 4240, 9023, 4234)