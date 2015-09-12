
m = 12000

frac = []
for n in xrange(2,m+1):
	for d in xrange(n+1,m+1):
		val = float(n)/float(d)
		if val > 1/3. and val < 1/2.:
			frac.append((n,d)) 


frac = sorted(frac,key=lambda x: x[0]/float(x[1]))

print frac