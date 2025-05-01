"""
Python Quest 1

You are given a positive integer N. Print a numerical triangle of height N - 1 like the one below:

1
22
333
4444
55555
......

Note: This triangle should consist of numbers only. There should be no blank spaces in the output.

Input Format

A single line containing integer N.

Constraints

1 <= N <= 10

Output Format

Print the numerical triangle of height N - 1.

Sample Input

5

Sample Output

1
22
333
4444
"""

n=4

for i in range(n):
    print((i+1)*f"{i}")