#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:23:59 2025

@author: tancredi
"""

"""Staircase

Staircase detail

This is a staircase of size n = 4:

   #
  ##
 ###
####

Its base and height are both equal to n. It is drawn using # symbols and spaces. 
The last line must have 0 spaces in it.

Write a program that prints a staircase of size n.

Function Description

Complete the staircase function in the editor below.

staircase has the following parameter(s):
- int n: an integer

Print
Print a staircase as described above.

Input Format

A single integer, n, denoting the size of the staircase.

Constraints

- 1 <= n <= 100

Output Format

Print a staircase of size n using # symbols and spaces.

Note: The last line must have 0 spaces.

Sample Input

6

Sample Output

     #
    ##
   ###
  ####
 #####
######

"""


def staircase(n):
    s = ""
    if 0<n<=100:
        for i in range(n,0,-1):
            s += (i-1) * " " + (n-i+1) * "#" + "\n"
        
    return s



n=4
print(staircase(n))