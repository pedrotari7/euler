import itertools

def factors(n):
	f = list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
	f.remove(n)
	return f

abund = [n for n in range(1,28124) if sum(factors(n)) > n]

nums = set([combi[0]+combi[1] for combi in itertools.combinations(abund+abund,2) if combi[0]+combi[1] < 28124])

special = []
for num in range(1,28124):
    if num not in nums:
        special.append(num)

print sum(special)