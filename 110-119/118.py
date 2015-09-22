import math
def gen_primes(n):
    primes = [2]
    i=2
    while i<=n:
        print i
    	for num in primes:
    		if i%num == 0:
    			break
    		if num > math.sqrt(i):
    			primes.append(i)
    			break
    	i += 1
    return primes


gen_primes(10**10)