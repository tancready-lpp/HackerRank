# exercise on factorial computation using the recursive function method

def factorial(n):
    if n<0: return ValueError
    if n==0: return 1
    elif n==1: return 1
    else: return factorial(n-1)*n
    
    
print(factorial(-1))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(10))