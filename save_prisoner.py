"""Save the Prisoner!

A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners in a circle, numbered from 1 to n. The jailer then starts handing out treats, beginning with the prisoner at seat number s. Each prisoner receives one treat until all treats have been distributed. The jailer warns that the last piece of candy will make the prisoner at that seat angry. Determine the chair number of the prisoner who will receive the last candy.

Example
n = 4  
m = 6  
s = 2  

There are 4 prisoners, 6 pieces of candy, and distribution starts at seat 2. The prisoners arrange themselves in seats numbered 1 to 4. Distribution starts at 2, so the candies go to prisoners 2, 3, 4, 1, 2, 3. The 6th candy goes to prisoner 3.

Function Description
Complete the saveThePrisoner function in the editor below.

saveThePrisoner has the following parameter(s):
- int n: the number of prisoners
- int m: the number of sweets
- int s: the chair number to begin passing out sweets from

Returns
- int: the chair number of the prisoner who receives the last sweet

Input Format
The first line contains an integer, t, the number of test cases.  
The next t lines each contain 3 space-separated integers:  
- n (the number of prisoners)  
- m (the number of sweets)  
- s (the chair number to start distribution)

Constraints
- 1 ≤ t ≤ 100  
- 1 ≤ n ≤ 10^9  
- 1 ≤ m ≤ 10^9  
- 1 ≤ s ≤ n  

Sample Input
2  
5 2 1  
5 2 2  

Sample Output
2  
3

Explanation
In the first query, there are 5 prisoners and 2 sweets. Distribution starts at seat 1. Prisoner 1 gets the first sweet, and prisoner 2 gets the second (last) sweet.  
In the second query, distribution starts at seat 2, so prisoner 2 gets the first sweet and prisoner 3 gets the second (last) sweet."""

def prisoner_candy(n,m,s):
    if m==n: return n
    else: 
        if m<n:
            if s<=m:
                return s + (m-1)
            else:
                return s +(m-n) -1
        else:
            return s + (m%n) -1
    

# Sample Test Cases for Save the Prisoner!

# Test Case 1: Basic example
print(prisoner_candy(5, 2, 1))  # Expected output: 2

# Test Case 2: Starting from the middle
print(prisoner_candy(5, 2, 2))  # Expected output: 3

# Test Case 3: Wrapping around the circle
print(prisoner_candy(4, 6, 2))  # Expected output: 3

# Test Case 4: Single prisoner
print(prisoner_candy(1, 1, 1))  # Expected output: 1

# Test Case 5: Maximum prisoners and sweets
print(prisoner_candy(1000000000, 1000000000, 1))  # Expected output: 1000000000

# Test Case 6: Multiple wraps around the circle
print(prisoner_candy(7, 19, 2))  # Expected output: 6

# Test Case 7: Sweets exactly divisible by prisoners
print(prisoner_candy(6, 12, 3))  # Expected output: 2

# Test Case 8: Last prisoner
print(prisoner_candy(10, 5, 10))  # Expected output: 4

# Test Case 9: Starting at the last seat
print(prisoner_candy(5, 3, 5))  # Expected output: 2

# Test Case 10: Large numbers with small start
print(prisoner_candy(1000000000, 999999999, 1))  # Expected output: 999999999