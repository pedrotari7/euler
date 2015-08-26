def factors(n):
	f = list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
	f.remove(n)
	return f

def is_abundant(n):
	return sum(factors(n)) > n

def is_perfect(n):
	return sum(factors(n)) == n

abund = []
for n in range(1,28124):
	if is_perfect(n):
		abund.append(n)

print abund