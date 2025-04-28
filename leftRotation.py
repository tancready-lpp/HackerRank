#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 11:01:51 2025

@author: tancredi
"""

"""Left Rotation

A left rotation operation on an array shifts each of the array's elements one unit to the left.
For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

Given an array a of n integers and a number d, perform d left rotations on the array and return the updated array.

Function Description

Complete the function rotateLeft in the editor below.

rotateLeft has the following parameters:
- int d: the number of rotations
- int a[n]: the array to rotate

Returns

- int[n]: the updated array after performing the rotations

Input Format

The first line contains two space-separated integers n and d, the size of a and the number of left rotations you must perform.
The second line contains n space-separated integers a[i].

Constraints

- 1 <= n <= 100000
- 1 <= d <= n
- 1 <= a[i] <= 1000000

Sample Input

5 4
1 2 3 4 5

Sample Output

5 1 2 3 4

Explanation

When we perform 4 left rotations, the array undergoes the following sequence:
- [1, 2, 3, 4, 5] → [2, 3, 4, 5, 1]
- [2, 3, 4, 5, 1] → [3, 4, 5, 1, 2]
- [3, 4, 5, 1, 2] → [4, 5, 1, 2, 3]
- [4, 5, 1, 2, 3] → [5, 1, 2, 3, 4]

Thus, the final array is [5, 1, 2, 3, 4].
"""

def leftRotation(d, arr):    
    
    constraints = (1<=len(arr)<=1e5) and (1<=d<=len(arr)) and 1<=max(arr)<=1e6
    
    while constraints:
        for k in range(d):
            first = arr[0]
            for i in range(len(arr)-1):
                # print("i",i)            
                arr[i] = arr[i+1]
            arr[-1] = first
            # print(arr)
        return arr

def leftRotationSlicing(d, arr): #basically with slicing it could be tìdone the same
    
    constraints = ((1<=len(arr)<=1e5) and (1<=d<=len(arr)) and (1<=max(arr)<=1e6))
    if constraints is True:
        for k in range(d):
            head = [arr[0]]
            arr = arr[1:]
            arr +=head
        return arr
    else:
        return "Contrains not respected"

import time

arr = [i*i for i in range(int(1e7))]
d1 =342323
d2 = 132344


s=time.time()
# print(arr, "original\n")
leftRotation(d1, arr)
a = time.time()

leftRotation(d2, arr)
b = time.time()
leftRotationSlicing(d1, arr)
c=time.time()
leftRotationSlicing(d2, arr)
d = time.time()

print(f"computation time {d1} rotations is {(a-s)*1000:.2e}ms")
print(f"computation time {d2} rotations is {(b-a)*1000:.2e}ms")

print(f"computation time {d1} rotations SLICE is {(c-b):.2e}s")
print(f"computation time {d2} rotations SLICE is {(d-c):.2e}s")

print("The slicing method is just way faster!") 
