import math, itertools
def gen_primes():
        special = []
        primes  = [2]
        i=2
        while i < 10000:
                for num in primes:
                        if i%num == 0:
                                break
                        if num > math.sqrt(i):
                                primes.append(i)
                                break
                i += 1
        return primes
primes = gen_primes()
special = []
for prime in primes:
        perm = [int(''.join(num)) for num in itertools.permutations(str(prime))]
        current = sorted(set([ele for ele in perm if ele in primes and len(str(ele))==4 ]))
        if len(current) >= 3:
                combs = itertools.combinations(current,3)
                for comb in combs:
                        comb = sorted(comb)
                        if comb[1]-comb[0] == comb[2] - comb[1] and comb not in special:
                                special.append(comb)
print ''.join([str(ele) for ele in special[1]])