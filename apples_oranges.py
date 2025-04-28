#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 09:45:13 2025

@author: tancredi
"""

"""Apple and Orange

Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
Using the information given below, determine the number of apples and oranges that land on Sam's house.

In the diagram below:
- The red region denotes the house, where s is the start point, and t is the endpoint. 
- The apple tree is to the left of the house, and the orange tree is to its right.

Assume the trees are located on a number line, meaning a fruit falls at a point determined by its distance from its tree.

Function Description

Complete the countApplesAndOranges function in the editor below.

countApplesAndOranges has the following parameter(s):
- int s: starting point of Sam's house location
- int t: ending location of Sam's house location
- int a: location of the Apple tree
- int b: location of the Orange tree
- int apples[m]: distances at which each apple falls from the tree
- int oranges[n]: distances at which each orange falls from the tree

Print
Two integers on two different lines:
- The first integer: the number of apples that fall on Sam's house.
- The second integer: the number of oranges that fall on Sam's house.

Input Format

- The first line contains two space-separated integers denoting the respective values of s and t.
- The second line contains two space-separated integers denoting the respective values of a and b.
- The third line contains two space-separated integers denoting the respective number of apples and oranges.
- The fourth line contains m space-separated integers denoting the distances at which each apple falls from the tree.
- The fifth line contains n space-separated integers denoting the distances at which each orange falls from the tree.

Constraints

- 1 <= s, t, a, b, m, n <= 10^5
- -10^5 <= distance fallen <= 10^5

Output Format

Print two integers on two different lines:
- The first integer: the number of apples that fall on Sam's house.
- The second integer: the number of oranges that fall on Sam's house.

Sample Input

7 11
5 15
3 2
-2 2 1
5 -6

Sample Output

1
1

Explanation

- The first apple falls at position 5 + (-2) = 3 (outside the house).
- The second apple falls at position 5 + 2 = 7 (on the house).
- The third apple falls at position 5 + 1 = 6 (before the house).

- The first orange falls at position 15 + 5 = 20 (after the house).
- The second orange falls at position 15 + (-6) = 9 (on the house).

Thus, we print:
1
1"""

# OK but too slow for Hackerrank!
def countApplesAndOranges(s,t,a,b,apples, oranges):
    
    cons = (a<s<t<b) and (all(-1e5<=value<=1e5 for value in oranges or apples)) and 1<=s,t,a,len(apples), len(oranges)<=1e5
    
    if cons:
        house = [i for i in range(s,t+1)]
        nA = 0 # fallen in house #len(apples) #number of apples thrown
        nO = 0 #len(oranges) #number of oranges thrown
        apples = [ap + a for ap in apples]
        oranges = [o + b for o in oranges]
        nA = sum(1 for apple in apples if apple in house)            
        nO = sum(1 for orange in oranges if orange in house)               

    return print(f"{nA}\n{nO}")


countApplesAndOranges(s= 3, t = 5, a =1, b =6, apples = [-1, 2, 1], oranges = [2,-1,-2])

### ---- CHATGPT SUPER FAST METHOD --- ###
def countApplesAndOranges(s, t, a, b, apples, oranges):
    nA = sum(1 for apple in apples if s <= a + apple <= t)
    nO = sum(1 for orange in oranges if s <= b + orange <= t)
    print(nA)
    print(nO)
