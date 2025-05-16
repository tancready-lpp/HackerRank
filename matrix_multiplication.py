


a  = [
    [1,0,0],
    [0,1,0],
    [0,0,1]
]
b = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def matrix_mul(a,b):
    n = len(a)
    d= [[0,0,0] for i in range((len(a)))]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                d[i][j] += a[i][k]*b[k][j]
    return d
    
print(matrix_mul(a,b))
