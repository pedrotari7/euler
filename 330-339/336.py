from itertools import permutations

perm = list(permutations(['A','B','C','D']))

for i in perm:
	print i

print len(perm)
print ''.join(perm[10])