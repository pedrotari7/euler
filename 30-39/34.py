import math
s = [n for n in xrange(10,100000) if n == sum([math.factorial(int(i)) for i in str(n)])]
print sum(s)