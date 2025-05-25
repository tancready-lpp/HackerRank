"""
You are given a number of sticks of varying lengths. You will iteratively cut the sticks down to the length of the shortest stick, until there are no sticks left.

At each iteration you need to:
1. Find the length of the shortest stick.
2. Cut that length from each of the longer sticks.
3. Discard the sticks that are left with zero length.
4. Print the number of sticks that are cut in that iteration.

The process continues until there are no sticks left to cut.

Example:
Input: [5, 1, 2, 3]
Output:
4  (all sticks are cut by 1)
3  (remaining: [4, 1, 2]; cut by 1)
2  (remaining: [3, 1]; cut by 1)
1  (remaining: [2]; cut by 2)
(then all sticks are gone)

Function Signature:
def cutTheSticks(arr: List[int]) -> List[int]

Input:
- A single list `arr` of integers representing the lengths of the sticks.

Output:
- A list of integers representing the number of sticks cut in each iteration."""

def cut_sticks(arr):
    res = []
    while len(arr)!=0:
        m = min(arr)
        arr = [arr[j] - m for j in range(len(arr))]
        res.append(len(arr))
        del_i = []
        for i in range(len(arr)):
            if arr[i] ==0:
                del_i.append(i)
        arr = [x for x in arr if x!=0]
    return res

arr = [1,3,4,3,1,2]
cut_sticks(arr)
