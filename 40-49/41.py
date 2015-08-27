import itertools,math
def gen_primes():
        special = []
        primes  = [2]
        i=2
        while i <= int(math.sqrt(987654321)):
                for num in primes:
                        if i%num == 0:
                                break
                        if num > math.sqrt(i):
                                primes.append(i)
                                break
                i += 1
        return primes
primes = gen_primes()
pandigital = []
start = '123456789'
while start != '':
        pandigital += [int(''.join(num)) for num in itertools.permutations(start)]
        start = start[:-1]
special = []
for i in sorted(pandigital):
        for prime in primes:
                if i%prime == 0:
                        break
                if prime > math.sqrt(i):
                        special.append(i)
                        break
print max(special)