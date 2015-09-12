
import math,itertools

def gen_primes(n):
    primes  = [2]
    i=2
    while i <= n:
        for num in primes:
            if i%num == 0:
                break
            if num > math.sqrt(i):
                primes.append(i)
                break
        i += 1
    return primes

n = 6    

primes = [prime for prime in gen_primes(10**n) if len(str(prime))==n]

poss = list(itertools.combinations(range(1,n-1),2))

print len(primes)

primes  = [i for i in primes if max([list(str(i)).count(sd) for sd in str(i)]) >=2]

print len(primes)

final=[]

for i,prime in enumerate(primes):
	print i
	for pos in poss:

		valid = []

		for i in xrange(10):

			a = list(str(prime))
			a[pos[0]] =str(i)
			a[pos[1]] =str(i)
			a = int(''.join(a))
			if a in primes:
				valid.append(a)

		if len(valid) == 8:
			final.append(sorted(valid))
			break

print final

