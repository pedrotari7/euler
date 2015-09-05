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
current_diag = []
found = False
while not found:


	tr = i**2
	tl = i**2-i+2
	bl = i**2-2*i+2
	br = i**2-3*i+3

	new = [tr,tl,bl,br] 


	max_value = max(new)

	if max_value > last:
		primes = update_primes(primes,max_value)


	for new_value in new:
		if new_value in primes:
			current_diag.append(new_value)



	per = (len(current_diag)/float(2*i-1))*100

	if per < 10 and last> 10 and int(round(per)) == 10:
		found = True
		print i
		break

	last = per

	print "n={} with {}% of primes".format(i,per) 

	if per > 10.5:
		i+=10
	elif per < 10:
		i-=1
	else:
		i+=1


