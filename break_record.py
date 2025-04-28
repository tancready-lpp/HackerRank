#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 18:04:24 2025

@author: tancredi
"""

"""Breaking the Records

Maria plays college basketball and wants to go pro. Each season, she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.

Given the scores for a season, determine the number of times Maria breaks her records for most and least points during the season.

Function Description

Complete the breakingRecords function in the editor below.

breakingRecords has the following parameter(s):
- int scores[n]: points scored per game

Returns
- int[2]: An array with the numbers of times she broke her records. 
  Index 0 is for breaking most points records, and index 1 is for breaking least points records.

Input Format

The first line contains an integer n, the number of games.
The second line contains n space-separated integers describing the respective values of scores[0], scores[1], ..., scores[n-1].

Constraints

- 1 <= n <= 1000
- 0 <= scores[i] <= 10^8

Output Format

Print two space-separated integers describing the respective numbers of times her best (highest) score was broken and her worst (lowest) score was broken.

Sample Input 0

9
10 5 20 20 4 5 2 25 1

Sample Output 0

2 4

Explanation 0

The scores are:
Game 0: 10 (no previous scores to compare)
Game 1: 5  (lower than previous, new min record)
Game 2: 20 (higher than previous, new max record)
Game 3: 20 (no change)
Game 4: 4  (lower than previous min record)
Game 5: 5  (no change)
Game 6: 2  (lower than previous min record)
Game 7: 25 (higher than previous max record)
Game 8: 1  (lower than previous min record)

Result is [2, 4] — 2 times breaking max record, 4 times breaking min record.
"""


def breakingRecords(scores):
    r = scores[0]
    scores = dict.fromkeys(scores) #Sets are UNORDERED but will show up as ordered. DICT KEEP THE INSERTION ORDER
    hr=r
    lr=r
    lc,hc = 0,0
    for key in scores.keys():
        if key<lr:
            lc+=1
            lr = key  # update low record
        elif key>hr:
            hc +=1
            hr=key # update high recoerd
    return hc,lc


scores = [10,5, 20, 20, 4, 5, 2, 25, 1]
my_list = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

print(breakingRecords(scores))
print(breakingRecords(my_list))