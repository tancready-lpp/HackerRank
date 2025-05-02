"""
The Hurdle Race

A video game character competes in a hurdle race. Hurdles have varying heights, and the character can jump up to a maximum height of k units. To jump higher, the character can consume a magic potion that increases their jump height by 1 unit per dose.

Objective:
Determine the minimum number of doses the character must take to be able to jump all hurdles. If the character can already clear all hurdles, return 0.

Function Description

Complete the hurdleRace function.

hurdleRace has the following parameters:
- int k: the height the character can jump naturally
- int height[n]: the heights of each hurdle

Returns
- int: the minimum number of doses required, always 0 or more

Input Format

The first line contains two space-separated integers n and k, the number of hurdles and the maximum height the character can jump naturally.
The second line contains n space-separated integers height[i], where 0 ≤ i < n.

Constraints

1 ≤ n ≤ 100
1 ≤ k ≤ 100
1 ≤ height[i] ≤ 100

Sample Input 0

5 4
1 6 3 5 2

Sample Output 0

2

Explanation 0

The character can jump a maximum of 4 units, but the tallest hurdle is 6 units high. To be able to jump all the hurdles, the character must drink 2 doses of the potion.

Sample Input 1

5 7
2 5 4 5 2

Sample Output 1

0

Explanation 1

The character can jump a maximum of 7 units, which is enough to cross all the hurdles. Therefore, no doses of the potion are needed.
"""


def hurdleRace(k, height):
    if k<=max(height):
        return max(height)-k
    else:
        return 0