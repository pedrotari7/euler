
final = []

for n in xrange(2,9):

	for x in xrange(2,10000):
		num = x**n
		if sum([int(ele) for ele in str(num)]) == x:
			final.append((num,x,n))

print len(final)

print final[-1]