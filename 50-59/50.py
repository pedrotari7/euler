import math

def gen_primes(n):
    primes = [2]
    i=2
    while i<=n:
    	for num in primes:
    		if i%num == 0:
    			break
    		if num > math.sqrt(i):
    			primes.append(i)
    			break
    	i += 1
    return primes


max_sim = (0,0)
primes = gen_primes(10**6)
stop = False
for i in xrange(len(primes)):
    for j in xrange(i+2,len(primes)):
        if sum(primes[i:j]) ==2:
            continue
        if sum(primes[i:j]) < primes[-1]:
            if sum(primes[i:j]) in primes:
                if (j-i) > max_sim[1]:
                    max_sim = (sum(primes[i:j]),j-i)
        else:
            stop = True
            break
    if stop:
        break

print max_sim