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

 
N = 10**9      

primes = gen_primes(math.sqrt(N))

for i,a in enumerate(primes):
    if a*(a-1)+(a+1)*(a+1-2) > N:
        print a*(a-1)+(a+1)*(a+1-2),i+1
        break