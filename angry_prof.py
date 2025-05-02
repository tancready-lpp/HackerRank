"""
A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (arrivalTime ≤ 0) to arrived late (arrivalTime > 0).

Given the arrival time of each student and a threshold number of attendees, determine if the class is cancelled.

Function Description

Complete the angryProfessor function.

angryProfessor has the following parameters:
- int k: the threshold number of students
- int a[n]: the arrival times of each student

Returns
- string: either "YES" or "NO"

Input Format

The first line contains an integer t, the number of test cases.

Each test case consists of two lines.
- The first line has two space-separated integers, n and k, the number of students (size of a) and the cancellation threshold.
- The second line contains n space-separated integers a[i], the arrival times of each student.

Constraints
- 1 ≤ t ≤ 10
- 1 ≤ n ≤ 1000
- 1 ≤ k ≤ n
- -100 ≤ a[i] ≤ 100

Sample Input

2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Sample Output

YES
NO

Explanation

For the first test case, k = 3. The professor wants at least 3 students in attendance, but only 2 have arrived on time (-3 and -1), so the class is cancelled.

For the second test case, k = 2. The professor wants at least 2 students in attendance, and there are 2 who arrived on time (0 and -1). The class is not cancelled.
"""

def angryProfessor(k,a):
    count = 0
    for alumn in a:
        if alumn<=0:
            count+=1
    if count>=k:
        return "NO"
    else: return "YES"