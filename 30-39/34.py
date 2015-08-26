import math
def fac(n):
	return math.factorial(n)

sum_fac = []
for i in xrange(1,999999999):

	print "i: " + str(i)

	if i == sum([fac(int(ele)) for ele in str(i)]):
		sum_fac.append(i)

print "sum_fac: " + str(sum_fac)