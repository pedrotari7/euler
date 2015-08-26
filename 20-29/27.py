def is_prime(n):
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			return False
	return True

lim_a = 1001
lim_b = 1001

max_a = None
max_b = None
max_n = 0 

for a in xrange(-lim_a,lim_a):
	for b in xrange(-lim_b,lim_b):
	
		n = 0
		count_n = 0
		while 1:
			val = n**2 + a*n + b
			if val > 0:
				if is_prime(val):
					count_n += 1
				else:
					if count_n > max_n:
						max_n = count_n
						max_a = a
						max_b = b

					break
			else:
				break

			n+=1


print "max_n: " + str(max_n)
print "max_a: " + str(max_a)
print "max_b: " + str(max_b)
print "max_a*max_b: " + str(max_a*max_b)



