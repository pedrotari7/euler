import time
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def totient(n):
    return len([k for k in xrange(1,n) if gcd(n,k)==1])

def gen_primes(n):
    import math
    primes  = [2]
    i=2
    while i <= n:
        for num in primes:
            if i%num == 0:
                break
            if num > math.sqrt(i):
                primes.append(i)
                break
        i += 1
    return primes

top = 10**3

values = gen_primes(top)[2:]
print len(values)
values = [i for i in values if (i-1)%2==0 and ((i-1)/2)%2!=0]
values = values[:int(len(values)/4)]
print len(values)

phi_values = dict()
phi_values[1] = 1

for j in xrange(2,10):
    phi_values[j]=totient(j)

max_phi = (0,0)
ini = time.time()
for n in values:
    n = n-1
    print n
    if n in phi_values:
        for i in xrange(1,10):
            if gcd(n,i) == 1:
                phi_values[n*i] = phi_values[n]*phi_values[i]
    else:
        phi_values[n] = totient(n)

    if float(n)/float(phi_values[n]) > max_phi[1]:
        max_phi = (n,float(n)/float(phi_values[n]))


print (time.time() - ini)

print max_phi