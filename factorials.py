"""Extra Long Factorials

Problem Statement:

Calculate and print the factorial of a given integer n.

For example, if n = 25, we calculate 25! = 25 × 24 × 23 × ... × 2 × 1 and get 15511210043330985984000000.

Function Description:

Complete the extraLongFactorials function in the editor below. It should print the result and return.

extraLongFactorials has the following parameter(s):
- int n: an integer

Note: Factorials of n can't be stored even in a long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby, etc., can handle big integers, but we need to write additional code in C/C++ to handle huge values. We recommend solving this challenge using BigIntegers.

Input Format:

A single integer n.

Constraints:

1 <= n <= 100

Output Format:

Print the factorial of n.

Sample Input:

25

Sample Output:

15511210043330985984000000
"""

def extraLongFactorials(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

extraLongFactorials(40)