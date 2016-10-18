import numpy

# The 'max' key stores the maximum number for which the factorial is stored.
fact_memory = {0: 1, 1: 1, 'max': 1}

def factorial(num):
    # Factorial is defined only for non-negative numbers
    assert num >= 0

    if num <= fact_memory['max']:
        return fact_memory[num]

    for x in xrange(fact_memory['max']+1, num+1):
        fact_memory[x] = fact_memory[x-1] * x
    fact_memory['max'] = num
    return fact_memory[num]


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

print len(primesfrom2to(N))

for i in xrange(5,N):
	factorial(i)
	print i



