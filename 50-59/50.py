import math
primes = [2]
i=2

while i<1000001:

	for num in primes:

		if i%num == 0:
			break

		if num > math.sqrt(i):
			primes.append(i)
			break


	i += 1


max_sim = (0,0)

for i in xrange(len(primes)):
	for j in xrange(i+2,len(primes)):
		#print '({},{})'.format(i,j)
		if sum(primes[i:j]) ==2:
			continue
		if sum(primes[i:j]) < primes[-1]:
			if sum(primes[i:j]) in primes:
				#print 'solution = ({},{})'.format(j-i,sum(primes[i:j]))
				if (j-i) > max_sim[1]:
					max_sim = (sum(primes[i:j]),j-i)
					#print primes[i:j]
					print max_sim
		else:
			break

print max_sim