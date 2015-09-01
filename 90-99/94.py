import math

def area(n):
    return math.sqrt(3*n*n-2*n-1)*(n+1)/4.

result = [3*i-1 for i in xrange(2,int((10**9-1)/3.)) if area(i).is_integer()]