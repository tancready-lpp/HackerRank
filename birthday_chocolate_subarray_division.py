"""
Subarray Division (Birthday Chocolate)

Two children, Lily and Ron, want to share a chocolate bar. 
Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:
- The length of the segment matches Ron's birth month, and
- The sum of the integers on the squares is equal to his birth day.

Determine how many ways she can divide the chocolate.

Function Description

Complete the birthday function in the editor below.

birthday has the following parameters:
- int s[n]: the numbers on each of the squares of chocolate
- int d: Ron's birth day
- int m: Ron's birth month

Returns
- int: the number of ways the bar can be divided

Input Format

- The first line contains an integer n, the number of squares of chocolate.
- The second line contains n space-separated integers s[i], the numbers on the chocolate squares.
- The third line contains two space-separated integers, d and m, Ron's birth day and his birth month.

Constraints

- 1 <= n <= 100
- 1 <= s[i] <= 5
- 1 <= d <= 31
- 1 <= m <= 12

Output Format

Print an integer denoting the total number of ways that Lily can divide the chocolate.

Sample Input 0

5
1 2 1 3 2
3 2

Sample Output 0

2

Explanation 0

Lily wants to give Ron a piece of chocolate with a length of 2 squares (birth month = 2) where the sum of the numbers is 3 (birth day = 3).

The following two segments meet the criteria:
- [1, 2] => 1 + 2 = 3
- [2, 1] => 2 + 1 = 3"""

def birthday(s:list[int],d:int,m:int):
    n = len(s)
    count = 0

    for i in range(len(s)-m+1):
        sub = s[i:i+m]
        print(len(sub), m)
        if sum(sub) == d:
            count+=1

    return count
    
print(birthday([1, 2, 1, 3, 2],3,2))
