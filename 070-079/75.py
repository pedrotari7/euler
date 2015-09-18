
import math

max_p = 10**5

solu = dict()

m,n,k = 2,1,0

while 1:

	n += 1
	m +=1

	for k in xrange(int(round(math.sqrt(m**2*n/float(2*m+n)))),int(math.sqrt(m*n))):

		a = n*(m**2+k**2)
		b = m*(n**2+k**2)
		c = (m+n)*(m*n-k**2)

		if a+b+c < max_p:
			solu[a+b+c] = (a,b,c) 
		else:
			break

