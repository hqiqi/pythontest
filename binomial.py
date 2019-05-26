from factorial import factorial

def binomial(n, k):
    x = factorial(n)
    y = factorial(k) * factorial(n-k)
    return x // y
