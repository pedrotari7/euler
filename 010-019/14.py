coll = [[0]]

for i in xrange(1,1000001):

	j = i
	chain = [j]
	while j != 1:

		if j%2==0:
			j = j/2
		else:
			j = 3*j + 1

		chain.append(j)

		if j < i:
			chain = chain + coll[j]
			break

	coll.append(chain)

sizes = [len(ele) for ele in coll]
value = max(sizes)
print "max length: " + str(value)
print "starting value: " + str(sizes.index(value))
