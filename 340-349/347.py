def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return tuple(sorted(set(primfac)))


final = dict()

for n in xrange(10**7+1):
	prime_fac = primes(n)
	if len(prime_fac) == 2:
		print n
		if prime_fac not in final:
			final[prime_fac] = n
		else:
			final[prime_fac] = max(n,final[prime_fac])

print sum(final.values())
