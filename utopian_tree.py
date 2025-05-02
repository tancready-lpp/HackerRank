"""<!-- # Utopian Tree

The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

For example, if the number of growth cycles is n = 5, the calculations are as follows:

- **Cycle 0**: height = 1
- **Cycle 1**: spring → height = 2
- **Cycle 2**: summer → height = 3
- **Cycle 3**: spring → height = 6
- **Cycle 4**: summer → height = 7
- **Cycle 5**: spring → height = 14

After 5 cycles, the tree will have a height of 14 meters.

## Function Description

Complete the `utopianTree` function.

`utopianTree` has the following parameter(s):

- `int n`: the number of growth cycles to simulate

Returns:

- `int`: the height of the tree after the given number of cycles

## Input Format

The first line contains an integer, t, the number of test cases.

Each of the next t lines contains an integer, n, the number of cycles for that test case.

## Constraints

- 1 ≤ t ≤ 10
- 0 ≤ n ≤ 60

## Sample Input -->"""

def utopianTree(n):
    height = 1  
    for m in range(1,int(n/2 + 1)):
            height *= 2
            height +=1
    if n%2 ==0:
        return height
    else: return height*2 


print(utopianTree(5))