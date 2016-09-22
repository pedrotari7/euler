from itertools import product
from math import factorial
from operator import mul

def single_prob(case):
	return reduce(mul, [i+1 for i,v in enumerate(case) if v=='R'], 1)

n = 15

winners = [a for a in product(['B','R'],repeat=n) if a.count('B')>a.count('R')]

total = sum([single_prob(w) for w in winners])

print "total: " + str(int(float(factorial(n+1))/total))