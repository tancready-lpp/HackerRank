"""Jumping on the Clouds: Revisited

Aerith is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. Her character must jump from cloud to cloud until it reaches the starting cloud again.

There is an array of clouds, \(c\), where each cloud is either a cumulus cloud (0) or a thunderhead (1). Aerith can jump from any cloud \(i\) to cloud \((i + k) \% n\) until she returns to the starting cloud. The game ends when Aerith lands back on cloud 0.

Aerith loses 1 unit of energy each time she jumps to a cloud and an additional 2 units of energy if it is a thunderhead.

Given the values of \(n\), \(k\), and the cloud configuration, determine the final energy level after the game ends.

Function Description  
Complete the jumpingOnClouds function in the editor below.  

jumpingOnClouds has the following parameter(s):  
- int c[n]: the cloud types  
- int k: the jump distance  

Returns  
- int: the energy level remaining after the game  

Input Format  
The first line contains two space-separated integers, \(n\) (the number of clouds) and \(k\) (the jump distance).  
The second line contains \(n\) space-separated integers describing the cloud array \(c\) where each element is either 0 (cumulus) or 1 (thunderhead).  

Constraints  
- 2 ≤ \(n\) ≤ 25  
- 1 ≤ \(k\) ≤ \(n\)  
- \(c[i] \) ∈ {0, 1}  

Sample Input  """

def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    pos=0
    
    while True:
        pos = (pos+k)%k
        e-=1
        if c[pos]==1:
            e-=2
        if pos ==0:
            break
    return e
    
c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2
print(jumpingOnClouds(c,k))