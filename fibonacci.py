

def fibonacci(n):
    if n<0:
        return ValueError
    else: 
        if n==0: return 0
        elif n==1 or n==2: return 1
        else: return fibonacci(n-1) + fibonacci(n-2)

def fibo_seq(n):
    fib = []
    for i in range(n):
        fib.append(fibonacci(i))
    return fib        
        

n=13
print(fibo_seq(n))
