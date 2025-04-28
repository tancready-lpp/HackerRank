#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 22:36:13 2025

@author: tancredi
"""

# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal = 1+5+9=15.
# The right-to-left diagonal = 3+5+9+=17.
# Their absolute difference is |15-17|=2.

# Function description

# Complete the  function with the following parameter:

# : a 2-D array of integers
# Return

# : the absolute difference in sums along the diagonals
# Input Format

# The first line contains a single integer, , the number of rows and columns in the square matrix .
# Each of the next  lines describes a row, , and consists of  space-separated integers .

# Constraints

# Sample Input

# STDIN      Function
# -----      --------
# 3           arr[][] sizes n = 3, m = 3
# 11 2 4     arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# 4 5 6
# 10 8 -12
# Sample Output

# 15
# Explanation

# The primary diagonal is:

# 11
#    5
#      -12
# Sum across the primary diagonal: .

# The secondary diagonal is:

#      4
#    5
# 10
# Sum across the secondary diagonal: 
# Difference: 

# Note: |x| is the absolute value of x."

#!/bin/python3

import math
import random
import numpy as np
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    print(arr)
    
    forw = sum(arr)
    
    back = sum(arr[-i][i] for i in range(len(arr)))
    print(back)
    print(arr[i][i] for i in range(len(arr)))
    
    print(forw)
    return abs(forw-back)
    
def random_matrix():
     # Dimensioni della matrice
     # Dimensioni della matrice
     righe = np,random.randint(0, 100)
     colonne = int(np,random.randint(0, 100))
     print(righe ,colonne)
    
     # Matrice con numeri float casuali tra 0 e 1
     matrice = np.random.randint(righe, colonne)     
     return matrice

print(random_matrix())
# diagonalDifference(random_matrix())    
    
