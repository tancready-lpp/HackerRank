
"""Permutation Equation
Given a sequence of integers \(p(1), p(2), ..., p(n)\) where each element is distinct and satisfies \(1 \le p(x) \le n\), find the sequence \(y(1), y(2), ..., y(n)\) such that each element in \(y\) satisfies the equation:

\[
y(i) = p^{-1}(p^{-1}(i))
\]

where \(p^{-1}\) is the inverse of function \(p\). In other words, for each \(i\) from 1 to \(n\), find the position of \(i\) in the sequence and then find the position of that position.

Example  
\(p = [5, 2, 1, 3, 4]\)  

For each \(i\) from 1 to 5:  
- \(p(1) = 5\), \(p^{-1}(5) = 4\)  
- \(p(2) = 2\), \(p^{-1}(2) = 2\)  
- \(p(3) = 1\), \(p^{-1}(1) = 3\)  
- \(p(4) = 3\), \(p^{-1}(3) = 5\)  
- \(p(5) = 4\), \(p^{-1}(4) = 1\)  

The result is \(y = [4, 2, 5, 1, 3]\).

Function Description  
Complete the permutationEquation function in the editor below.  

permutationEquation has the following parameter(s):  
- int p[n]: an array of integers  

Returns  
- int[n]: the values of \(y\) for all \(i\) in the sequence  

Input Format  
The first line contains an integer \(n\), the number of elements in the sequence.  
The second line contains \(n\) space-separated integers \(p[i]\) where 1 ≤ \(p[i]\) ≤ \(n\).  

Constraints  
- 1 ≤ \(n\) ≤ 50  

Sample Input  """

def permutationEquation(p):
    n = len(p)
    x = [z for z in range(1,n+1)]
    ind1 = [p.index(xval) + 1 for xval in x]
    ind2 = [p.index(ival) +1 for ival in ind1]
    # print(ind1, "IND1")
    return ind2
    
    
    
    
    
    
    


