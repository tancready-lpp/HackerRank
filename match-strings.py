#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 09:18:02 2025

@author: tancredi
"""

"""Sparse Arrays

There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

Function Description

Complete the function matchingStrings in the editor below.

matchingStrings has the following parameters:
- string strings[n] - an array of strings to search
- string queries[q] - an array of query strings

Returns
- int[q]: an array of results for each query

Input Format

The first line contains and integer n, the size of strings[].
Each of the next n lines contains a string strings[i].

The next line contains q, the size of queries[].
Each of the next q lines contains a string queries[i].

Constraints

- 1 <= n <= 1000
- 1 <= q <= 1000
- 1 <= |strings[i]|, |queries[i]| <= 20

Sample Input 1

4
aba
baba
aba
xzxb
3
aba
xzxb
ab

Sample Output 1

2
1
0

Explanation 1

Here, "aba" occurs twice, "xzxb" occurs once and "ab" does not occur at all. The result is [2, 1, 0].
"""



def matchingStrings(stringList, queries):
    
    Constraints = (1 <= len(stringList) <= 1000 and
                   1 <= len(queries) <= 1000 and
                   all(1<=(len(stringList[i]))<=20 for i in range(len(stringList))) and 
                   all(1<=(len(queries[j]))<=20 for j in range(len(queries))))
    
    
    if Constraints:
        listcount = []
        
        for query in queries:
            # count = dict.fromkeys(query,0)
            qcount =0
            for string in stringList:
              
                if string == query:
                   print(f"{query} query match with {string} string")
                   qcount += 1 
            listcount.append(qcount)

    else:
        "Contraints are not followed"
                
    return listcount
    
    
data1 = ["aba","baba","aba","xzxb"]
queries1 = ["aba", "xzxb", "ab"]
   
data = [
    "lekgdisnsbfdzpqlkg",
    "eagemhdygyv",
    "jwvwwnrhuai",
    "urcadmrwlqe",
    "mpgqsvxrijpombyv",
    "mpgqsvxrijpombyv",
    "urcadmrwlqe",
    "mpgqsvxrijpombyv",
    "eagemhdygyv",
    "eagemhdygyv",
    "jwvwwnrhuai",
    "urcadmrwlqe",
    "jwvwwnrhuai",
    "kvugevicpsdf",
    "kvugevicpsdf",
    "mpgqsvxrijpombyv",
    "urcadmrwlqe",
    "mpgqsvxrijpombyv",
    "exdafbnobg",
    "qhootohpnfvbl",
    "suffrbmqgnln",
    "exdafbnobg",
    "exdafbnobg",
    "eagemhdygyv",
    "mpgqsvxrijpombyv",
    "urcadmrwlqe",
    "jwvwwnrhuai",
    "lekgdisnsbfdzpqlkg",
    "mpgqsvxrijpombyv",
    "lekgdisnsbfdzpqlkg",
    "jwvwwnrhuai",
    "exdafbnobg",
    "mpgqsvxrijpombyv",
    "kvugevicpsdf",
    "qhootohpnfvbl",
    "urcadmrwlqe",
    "kvugevicpsdf",
    "mpgqsvxrijpombyv",
    "lekgdisnsbfdzpqlkg",
    "mpgqsvxrijpombyv",
    "kvugevicpsdf",
    "qhootohpnfvbl",
    "lxyqetmgdbmh",
    "urcadmrwlqe",
    "urcadmrwlqe",
    "kvugevicpsdf",
    "lxyqetmgdbmh",
    "urcadmrwlqe",
    "lxyqetmgdbmh",
    "jwvwwnrhuai",
    "qhootohpnfvbl",
    "qhootohpnfvbl",
    "jwvwwnrhuai",
    "lekgdisnsbfdzpqlkg",
    "kvugevicpsdf",
    "mpgqsvxrijpombyv",
    "exdafbnobg",
    "kvugevicpsdf",
    "lekgdisnsbfdzpqlkg",
    "qhootohpnfvbl",
    "exdafbnobg",
    "qhootohpnfvbl",
    "exdafbnobg",
    "mpgqsvxrijpombyv",
    "suffrbmqgnln",
    "mpgqsvxrijpombyv",
    "qhootohpnfvbl",
    "jwvwwnrhuai",
    "mpgqsvxrijpombyv",
    "qhootohpnfvbl",
    "lekgdisnsbfdzpqlkg",
    "eagemhdygyv",
    "jwvwwnrhuai",
    "kvugevicpsdf",
    "eagemhdygyv",
    "eagemhdygyv",
    "lxyqetmgdbmh",
    "qhootohpnfvbl",
    "lxyqetmgdbmh",
    "exdafbnobg",
    "qhootohpnfvbl",
    "qhootohpnfvbl",
    "exdafbnobg",
    "suffrbmqgnln",
    "mpgqsvxrijpombyv",
    "urcadmrwlqe",
    "eagemhdygyv",
    "lxyqetmgdbmh",
    "urcadmrwlqe",
    "suffrbmqgnln",
    "qhootohpnfvbl",
    "kvugevicpsdf",
    "lekgdisnsbfdzpqlkg",
    "lxyqetmgdbmh",
    "mpgqsvxrijpombyv",
    "jwvwwnrhuai",
    "lxyqetmgdbmh",
    "lxyqetmgdbmh",
    "lekgdisnsbfdzpqlkg",
    "qhootohpnfvbl",
]
queries = [
    "exdafbnobg",
    "eagemhdygyv",
    "mpgqsvxrijpombyv",
    "kvugevicpsdf",
    "lekgdisnsbfdzpqlkg",
    "kvugevicpsdf",
    "exdafbnobg",
    "qhootohpnfvbl",
    "eagemhdygyv",
    "kvugevicpsdf",
    "suffrbmqgnln",
    "jwvwwnrhuai",
    "lekgdisnsbfdzpqlkg",
    "lekgdisnsbfdzpqlkg",
    "mpgqsvxrijpombyv",
    "jwvwwnrhuai",
    "kvugevicpsdf",
    "lekgdisnsbfdzpqlkg",
    "exdafbnobg",
    "suffrbmqgnln",
    "qhootohpnfvbl",
    "eagemhdygyv",
    "exdafbnobg",
    "suffrbmqgnln",
    "jwvwwnrhuai",
    "qhootohpnfvbl",
    "eagemhdygyv",
    "exdafbnobg",
    "exdafbnobg",
    "jwvwwnrhuai",
    "qhootohpnfvbl",
    "lxyqetmgdbmh",
    "qhootohpnfvbl",
    "suffrbmqgnln",
    "lxyqetmgdbmh",
    "qhootohpnfvbl",
    "eagemhdygyv",
    "jwvwwnrhuai",
    "eagemhdygyv",
    "qhootohpnfvbl",
    "mpgqsvxrijpombyv",
    "qhootohpnfvbl",
    "jwvwwnrhuai",
    "exdafbnobg",
    "eagemhdygyv",
    "eagemhdygyv",
    "kvugevicpsdf",
    "kvugevicpsdf",
    "jwvwwnrhuai",
    "urcadmrwlqe",
    "lxyqetmgdbmh",
    "qhootohpnfvbl",
    "exdafbnobg",
    "exdafbnobg",
    "eagemhdygyv",
    "qhootohpnfvbl",
    "exdafbnobg",
    "exdafbnobg",
    "lekgdisnsbfdzpqlkg",
    "jwvwwnrhuai",
    "eagemhdygyv",
    "urcadmrwlqe",
    "kvugevicpsdf",
    "lekgdisnsbfdzpqlkg",
    "jwvwwnrhuai",
    "eagemhdygyv",
    "lekgdisnsbfdzpqlkg",
    "exdafbnobg",
    "kvugevicpsdf",
    "jwvwwnrhuai",
    "exdafbnobg",
    "lxyqetmgdbmh",
    "exdafbnobg",
    "lxyqetmgdbmh",
    "jwvwwnrhuai",
    "mpgqsvxrijpombyv",
    "eagemhdygyv",
    "urcadmrwlqe",
    "kvugevicpsdf",
    "qhootohpnfvbl",
    "jwvwwnrhuai",
    "eagemhdygyv",
    "urcadmrwlqe",
    "urcadmrwlqe",
    "exdafbnobg",
    "qhootohpnfvbl",
    "exdafbnobg",
    "eagemhdygyv",
    "exdafbnobg",
    "jwvwwnrhuai",
    "eagemhdygyv",
    "jwvwwnrhuai",
    "mpgqsvxrijpombyv",
    "urcadmrwlqe",
    "urcadmrwlqe",
    "eagemhdygyv",
    "eagemhdygyv",
    "jwvwwnrhuai",
    "suffrbmqgnln",
    "eagemhdygyv"
]

# print(matchingStrings(data, queries))

print(matchingStrings(data1, queries1))