import math

print len( [(n,r) for n in xrange(23,101) for r in [r  for r in xrange(2,n+1) if math.factorial(n) > (10**6)*math.factorial(r)*math.factorial(n-r)]])
