"""Given a set of integers, determine the size of the largest subset 
such that the sum of any two numbers in the subset is **not** evenly divisible by k.

**Function Description**

Complete the function `nonDivisibleSubset` in the editor below.  
The function must return an integer representing the size of the maximum subset.

nonDivisibleSubset has the following parameter(s):
- int k: the modulus factor
- int s[n]: an array of integers

**Input Format**

The first line contains two space-separated integers, **n** (the number of values in **s**) and **k**.  
The second line contains **n** space-separated integers **s[i]**.

**Constraints**

- 1 ≤ n ≤ 10<sup>5</sup>  
- 1 ≤ k ≤ 100  
- 1 ≤ s[i] ≤ 10<sup>9</sup>

**Output Format**

Print a single integer denoting the size of the largest possible subset.

**Sample Input**"""


#TO BE FINISHED

def nonDivisibleSubset(k, s):
    def check_cond(sub):
        return all((sub[i] + sub[j])%k!=0 for i in range(len(s)) for j in range(len(s)))
    
    sub = s
    i=0
    while check_cond(sub) is False:
        i+=1
        print(check_cond(sub))
        
    
s = [1,7,2,4,2,3]
k = 3
print(nonDivisibleSubset(k,s))