"""
Picking Numbers

Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.

Function Description

Complete the pickingNumbers function in the editor below.

pickingNumbers has the following parameter(s):
- int a[n]: an array of integers

Returns
- int: the length of the longest subarray that meets the criterion

Input Format

The first line contains a single integer n, the size of the array a.
The second line contains n space-separated integers, each an a[i].

Constraints

- 2 <= n <= 100
- 0 < a[i] < 100
- The answer will be >= 2.

Sample Input 0

6
4 6 5 3 3 1

Sample Output 0

3

Explanation 0

We choose the following multiset of integers from the array: {3, 3, 4}. Each pair in the multiset has an absolute difference <= 1 (i.e., |3 - 3| = 0 and |3 - 4| = 1), so we print the number of chosen integers, 3, as our answer.

Sample Input 1

6
1 2 2 3 1 2

Sample Output 1

5

Explanation 1

We choose the following multiset of integers from the array: {1, 2, 2, 1, 2}. Each pair in the multiset has an absolute difference <= 1 (i.e., |1 - 2| = 1, |1 - 1| = 0, and |2 - 2| = 0), so we print the number of chosen integers, 5, as our answer.
"""

def pickingNumbers(a):      
    counts = {}
    for num in a:
        counts[num] = counts.get(num, 0) + 1

    sub =[[a1,a2] for a1 in counts for a2 in counts if abs(a1-a2)<=1]

    max_key = max(counts, key = counts.get) # The key and .get command make me take the key with associated max value
    adjacent_keys = [key for key in (max_key+1,max_key-1) if key in counts] # a list with the only existing adjacent key (if in counts)

    if adjacent_keys:
        end_key = max(adjacent_keys, key = counts.get) #.get tries to retrieve the key with max value in the adjacent_keys list
        return counts[max_key] + counts[end_key]
    else:
        return counts[max_key] 

a = [4, 6, 5, 3, 3, 1]
b = [4,4,4,4,4,4]
c = [4,5,4,5,4,5,4,5]
d = [1,2,3,4]
e = [1,1,1,2,2,2,2,3]
ex =[a,b,c,d,e]
print(pickingNumbers(e), "result")
print(pickingNumbers([4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]), "result")