from math import sqrt

n = 10**8

limit = int(sqrt(n))

result = set()

for i in xrange(1,limit+1):
	num = i**2
	for j in xrange(i+1,limit+1):
		num += j**2
		if num <= n:
			if str(num) == str(num)[::-1]:
				result.add(num)
		else:
			break

print len(result)
print sum(result)
