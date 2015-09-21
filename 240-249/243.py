from fractions import Fraction as frac
import math

def resilience(n):
    return frac(sum([i==(frac(i)/frac(n)).numerator for i in xrange(1,n)]))/frac((n-1))

def gen_primes(max_value):
	primes  = [2]
	i=2
	while i <= max_value:

        	for num in primes:
                	if i%num == 0:
                        	break
                	if num > math.sqrt(i):
                        	primes.append(i)
				break
		i += 1
	return primes


for n in xrange(2,100):
    result = n*reduce(lambda x, y: x*y,[1-1/float(num) for num in gen_primes(n)])/(n-1)
    if result < float(15499)/float(94744):
        n = gen_primes(n)[-2]
        break

result = n*reduce(lambda x, y: x*y,[1-1/float(num) for num in gen_primes(n)])
ini  = reduce(lambda x, y: x*y,[num for num in gen_primes(n)])

for i in xrange(1,10):
    if (2*result)/float(n*2**i-1) < float(15499)/float(94744):
        print 2**i*ini
        break


