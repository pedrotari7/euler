def factors(n):
	f = list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
	f.remove(n)
	return f

d = [0] + [sum(factors(i)) for i in xrange(1,10001)]

ami = []
for num in xrange(0,10001):
	if d[num] <= 10000 and d[num] != num:
		if d[d[num]] == num:
			ami.append((num,d[num]))


print ami
print sum([ele[0] for ele in ami])
