import math,itertools

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

primes = set(gen_primes(5000)) - set(gen_primes(2000))

perms = list(itertools.combinations(primes,2))

limit = 10**7
final = []
for perm in perms:
    n = perm[0]*perm[1]
    if n < limit:
        #print perm[0],perm[1],n
        tot = (perm[0]-1)*(perm[1]-1)
        if sorted(str(n)) == sorted(str(tot)):
            final.append([n/float(tot),tot,perm,n])

print min(final)[-1]