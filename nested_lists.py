"""Nested Lists

Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]

The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that score: ["beta", "alpha"]. Ordered alphabetically, the names are printed as:

alpha
beta

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

- 2 <= N <= 5
- There will always be at least two students

Output Format

Print the name(s) of any student(s) having the second lowest grade in alphabetical order.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry

Sample Input 1

5
Harsh
20
Beria
20
Varun
19
Kakashi
19
Vikas
21

Sample Output 1

Beria
Harsh
"""

if __name__ == '__main__':
    names, scores= [] ,[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    l = list(zip(names, scores))
    
    l= sorted(l, key = lambda x: x[ 1])
    min_score = min(l, key = lambda x: x[1])[1]
    ls = [c for c in l if c[1]!=min_score]
    n = []
    a = min(ls, key = lambda x:x[1])[1]
    for c in ls:
        if c[1] == min(ls, key = lambda x:x[1])[1]:
            n.append(c[0])
    n = sorted(n)
    for p in n:
        print(p)
    
        
