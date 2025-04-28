#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 00:13:39 2025

@author: tancredi
"""

"""Given a  2D array, , an hourglass is a subset of values with indices falling in the following pattern:

a b c  
  d  
e f g

There are  hourglasses in a  array. The  is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in , then print the  hourglass sum.

Example


-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3
  1
8 6 6

Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Each of the  lines of inputs  contains  space-separated integers .

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output
19

Explanation

1 1 1   1 1 0
  1       0     and so on... (16 total)
1 1 1   1 1 0


 contains the following hourglasses:

The hourglass with the maximum sum (19) is:

2 4 4
  2
1 2 4 """

#!/bin/python3

# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

### --- MAIN --- ###

arr = [ 
           [1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]
       ]


def hourglassSum(arr):
    hgsum = []
    for k in range(4):
        for l in range(4):
            hg = [arr[k][l:3+l],[arr[1+k][1+l]],arr[2+k][l:3+l]]
            tmp = hg[0] + hg[1] + hg[2]
            hgsum.append(sum(tmp))
            
    return max(hgsum)
    
    
print(hourglassSum(arr))