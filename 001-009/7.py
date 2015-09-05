import math
primes = [2]
i=2

while len(primes)<10001:

	for num in primes:

		if i%num == 0:
			break

		if num > math.sqrt(i):
			primes.append(i)
			break

	i += 1

print primes[-1]