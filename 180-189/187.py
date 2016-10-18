from itertools import combinations_with_replacement

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


N = 10**8

primes = list(primesfrom2to(int(N/2.+1)))

# print primes

numbers = []

for i in xrange(0,len(primes)):
    for j in xrange(0,len(primes)):
        print(primes[i],primes[j])
    	new = primes[i]*primes[j]
    	if new < N:
     		# print "Added: ",new
    		numbers.append(new)
        else:
            break

final = sorted(set(numbers))

# print final
print len(final)

