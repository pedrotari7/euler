from math import factorial
print len( [(n,r) for n in xrange(23,101) for r in [r  for r in xrange(2,n+1) if factorial(n) > (10**6)*factorial(r)*factorial(n-r)]])
