
i = 1855
n = 1
while i>1:
	print i
	for k in range(n):
	    n = (1777 * n) % 10**8
	 
	i-=1

print n