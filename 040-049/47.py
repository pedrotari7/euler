import math

def get_factors(number):
    factors = []
    d = 2
    while number > 1:
        while number % d == 0:
            factors.append(d)
            number /= d
        d = d + 1
    return factors

def gen_primes(max_value):
	primes  = [2]
	i=2
	while i <= int(math.sqrt(max_value)):

        	for num in primes:
                	if i%num == 0:
                        	break
                	if num > math.sqrt(i):
                        	primes.append(i)
				break
		i += 1
	return primes


max_value = 150000
primes = gen_primes(max_value)
size = 4
final = []
for i in xrange(10**5,max_value):
    factors = get_factors(i)
    if all([factor in primes for factor in factors]):
        if len(set(factors)) == size:
            if final == [] or i-1 in final:
                final.append(i)
                if len(final) == size:
                    break
                continue
    final = []

print final