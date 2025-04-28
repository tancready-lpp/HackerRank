#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 09:26:38 2025

@author: tancredi
"""

"""Time Conversion

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below.

timeConversion has the following parameter(s):
- string s: a time in 12-hour format

Returns
- string: the time in 24-hour format

Input Format

A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

Constraints

- All input times are valid

Sample Input

07:05:45PM

Sample Output

19:05:45"""

def timeConversion(s):
    k = s[0:2]
    if "AM" in s:
        if k == "12":
            k="00"
    elif "PM" in s:
        if k != "12":
            k = str(int(k)+12)
    
    s = k +  ":" + s[3:-2] 
    
    return s        
        
s = "01:02:22PM"

print(timeConversion(s))