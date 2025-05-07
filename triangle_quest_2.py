



n=5
#Using string methods
for j in range(1, n+1):
    print("".join([str(i) for i in range(1,j)]) + "".join([str(i) for i in range(j,0,-1)]))
    
# Using only integers
for i in range(1, n+1):
    # Use (10 ** i // 9) to create a sequence of 1 to i as a number
    # Then square it to create the full palindrome
    print((10 ** i // 9) ** 2)