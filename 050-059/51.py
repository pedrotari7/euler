
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

n = 5  

primes = [prime for prime in gen_primes(10**n) if len(str(prime))==n]

poss = list(itertools.combinations(range(1,n-1),2))

print len(primes)

primes  = [i for i in primes if max([list(str(i)).count(sd) for sd in str(i)])==2]

print len(primes)


for comb in itertools.combinations(primes):
	

