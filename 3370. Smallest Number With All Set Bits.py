n=3
def smallestNumber(n):
    b=bin(n)
    c=b[2:]

    if '0' in str(c):
            return smallestNumber(n + 1)  
    else:
            return n
    

print(smallestNumber(n))