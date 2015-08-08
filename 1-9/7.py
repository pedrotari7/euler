import time

def factorize(number):
	factors = []
	d = 2
	while number > 1:
	    while number % d == 0:
	    	if len(factors) == 1:
	    		return False
	    	factors.append(d)
	    	number /= d
	    d = d + 1

	return True

if __name__ == '__main__':
	
	primes = [2]
	i=2

	while len(primes)<10001:
		if i % 2 ==0 or i% 3 ==0 or i ==5:
			i += 1
			continue
		
		if factorize(i):
			primes.append(i)

		# time.sleep(0.001)

		i += 1

	print primes[-2]
