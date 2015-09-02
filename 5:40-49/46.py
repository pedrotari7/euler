import math

def gen_next_prime(primes):
    i=primes[-1]+1
    while 1:
        for num in primes:
            if i%num == 0:
                break
            if num > math.sqrt(i):
                primes.append(i)
                return primes
        i += 1
    
    
primes = [2,3,5,7]
special = []
i = 7

while special == []:
    while 1:
        while i > primes[-1]:
            primes = gen_next_prime(primes)
    
        if i not in primes and i%2!=0:
            break
        i+=1
        
    found = False
    for num in primes[:-1]:
        n = 0
        while 1:
            if (num + 2*n*n) == i:
                #print '{} = {} + 2x{}^2'.format(i,num,n)
                found = True
                break
            if (num + 2*n) > i:
                break
            n+=1
        if found:
            break
    if not found:
        special.append(i)
    i+=1

print special
