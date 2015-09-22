def farey (n):
	trigg = False
	a = (0, 1)
	if trigg: yield a
	b = (1, n)
	while b[0] < n:
		k = (n + a[1]) // b[1]
		a, b = b, (k * b[0] - a[0], k * b[1] - a[1])
		if a == (1, 3): trigg = True
		if a == (1, 2): return
		if trigg: yield a

print len(list(farey(12000))) - 1