
from math import factorial, sqrt
import numpy

def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def comb(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))


def pascal_line(n):
	line = []

	for i in xrange(1,n):
		line.append(comb(n,i))

	return set(line)


numbers = set([1])

for n in xrange(51):
	numbers.update(pascal_line(n))

final = sorted(numbers)

sprimes =[p**2 for p in primesfrom2to(int(25))]

squarefree = []

for i,pn in enumerate(final):
	is_free = True

	for s in sprimes: 
		if pn%s==0:
			is_free = False
			break
		if s>pn:
			break
	if is_free:
		squarefree.append(pn)

print sum(squarefree)





