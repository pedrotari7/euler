
import math,itertools
primes = [2]
i=2

while i<1000000:

	for num in primes:

		if i%num == 0:
			break

		if num > math.sqrt(i):
			primes.append(i)
			break
	i += 1

primes = [p for p in primes if '0' not in str(p) and '2' not in str(p) and '4' not in str(p) and '5' not in str(p) and '6' not in str(p) and '8' not in str(p)]

special = [2,5]
for i in primes:
	if i in special:
		continue
	perms = [i]
	for ind in xrange(len(str(i))):
		perms.append(int(str(perms[-1])[1:] + str(perms[-1])[0]))
		if perms[-1] == i:
			break

	add = True
	for perm in perms: 
		if perm not in primes:
			add = False
			break
	if not add:
		continue
	special += perms

print len(sorted(list(set(special))))