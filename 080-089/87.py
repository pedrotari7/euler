import math

def gen_primes(n):
    primes = [2]
    i=2
    
    while i<n:
    	for num in primes:
    		if i%num == 0:
    			break
    		if num > math.sqrt(i):
    			primes.append(i)
    			break
    	i += 1
    return primes
    	
limit = 50*10**6
primes = gen_primes(math.sqrt(limit))

final = []
for num1 in primes:
    for num2 in primes:
        a = num1**2 + num2**3
        if a > limit:
            break
        for num3 in primes:
            a = num1**2 + num2**3 + num3**4
            if a > limit:
                break
            final.append(a)
            
print len(set(final))