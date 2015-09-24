import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

total = float(nCr(70,20))

p = 7*(1- nCr(60,20)/total)

print p