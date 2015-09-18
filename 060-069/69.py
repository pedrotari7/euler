import math

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

result = 1
for prime in gen_primes(200):
    temp = prime*result
    if temp > 10**6:
        break
    result *= prime

print result