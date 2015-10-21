import math


def factors(n):

	factors = []
	d = 2
	while n > 1:
	    while n % d == 0:
	        factors.append(d)
	        n /= d
	    d = d + 1

	return factors


print factors(1260)

# n = 1
# while 1:
# 	f = factors(n)
# 	size = len(f)
# 	print n,size


# 	if size > 1000:
# 		print n
# 		break

# 	n +=1