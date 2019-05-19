import sys


def factor(n,k):
    if n == 0 or k == 0:
        return 1
    elif n < 0 or k < 0 or k>=n:
        raise ValueError
    return str(factorial(n)/(factorial(k)*factorial(n-k)))

def factorial(n):
    a = 1
    if n == 0:
        return 1
    elif n < 0:
        raise ValueError
    while n>0:
        a = a*n
        n-=1
    return a

    
n = int(sys.argv[1])
k = int(sys.argv[2])
print(factor(n,k))