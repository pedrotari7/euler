# Sieve of Eratosthenes
def gen_primes(n):
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while q < n:
        if q not in D:

            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def find_n(p1,p2):
    p1_str = str(p1)

    i = 3;
    while True:
        n = i*p2
        if str(n).endswith(p1_str):
            return n
        i+=2


primes = [i for i in gen_primes(10**6)][2:]

S = []

for i in xrange(len(primes)-1):
    print primes[i],primes[i+1]
    n = find_n(primes[i],primes[i+1])
    S.append(n)

#18612760000617135
#2352901000003
print S
print sum(S)
