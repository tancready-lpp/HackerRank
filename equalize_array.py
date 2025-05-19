"""Given an array of integers, determine the minimum number of elements to delete to leave only elements of equal value.

Example

arr = [1, 2, 2, 3]

Delete the 2 elements 1 and 3 leaving arr = [2, 2]. If all the elements in the result are equal, the return value is 2.

Function Description

Complete the equalizeArray function in the editor below.

equalizeArray has the following parameter(s):

- int arr[n]: an array of integers

Returns

- int: the minimum number of deletions required

Input Format

The first line contains an integer n, the number of elements in arr.
The next line contains n space-separated integers arr[i].

Constraints

- 1 <= n < 100
- 1 <= arr[i] <= 100

Sample Input

5
3 3 2 1 3

Sample Output

2

Explanation

Delete the 2 elements 1 and 2 to leave arr = [3, 3, 3]. This is the minimum number of deletions needed to make all elements equal.
"""

def equalizeArray(arr):
    a = dict.fromkeys(arr,0)
    for key in arr:
        if key in a.keys():
            a[key] += 1
        else:
            a[key] = 1
    max_key = max(a, key=a.get)
    print(a)
    print(max_key)
    return len(arr) - a[max_key]

    
    
print(equalizeArray([1,2,3,4,1,2,4,4]))