import math
import time

def update_primes(primes,max_value):

	i=primes[-1]

	while i<max_value+1:

		for num in primes:

			if i%num == 0:
				break

			if num > math.sqrt(i):
				primes.append(i)
				break
		i += 1

	return primes


primes = [2]
i = 1
last =100
per = 100
current_diag = 0
found = False
while not found:

	tl = i**2-i+2
	bl = i**2-2*i+2
	br = i**2-3*i+3

	new = [tl,bl,br] 


	max_value = max(new)

	if max_value > last:
		primes = update_primes(primes,max_value)


	for new_value in new:
		if new_value in primes[-1000:]:
			current_diag+=1

	per = (current_diag/float(2*i-1))*100

	if per < 10  and int(round(per)) == 10:
		found = True
		print i
		break

	print "n={} with {}% of primes".format(i,per) 

	i+=1


