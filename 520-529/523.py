
from itertools import permutations

def expected(s):
	final = 0
	s_set = set(s)
	for value in s_set:
		final +=  value * (float(s.count(value))/float(len(s)))
	return final

def first_sort(a):

	base = range(1,len(a)+1)
	count = 0 
	aux = 0 
	while a != base:
		
		if a[aux] > a[aux+1]:
			b = [a[aux+1]]
			a.remove(a[aux+1])
			a = b + a
			aux = 0
		else:
			aux += 1
			continue

		count += 1

	return count

n = 30

base = range(1,n+1)

perms =  permutations(base)
steps = []
for perm in perms:
	print 'perm: ' + str(perm)
	steps.append(first_sort(list(perm)))
	print 'count: ' +  str(steps[-1])

#print steps

print expected(steps)

