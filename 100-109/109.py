from itertools import combinations_with_replacement


def possible(n):

	single = [ele for ele in range(1,21) + [25] if ele <= n]

	double = [['D',j] for j in [2*ele for ele in single] if j <= n]

	triple = [['T',ele] for ele in range(3,61,3) if ele <= n]

	valid = []

	if ['D',n] in double:
		valid.append(['D',n])

	for comb in combinations_with_replacement(single+double+triple,2):

		current = sum([ele[1] for ele in comb if isinstance(ele,list)]) + sum([ele for ele in comb if not isinstance(ele,list)])

		if current < n:
			rest = n - current

			if ['D',rest] in double and (comb[0],comb[1],['D',rest]) not in valid:

				valid.append((comb[0],comb[1],['D',rest]))

		elif current == n and  isinstance(comb[1],list) and comb[1] in double and comb not in valid:
			valid.append(comb)

		if isinstance(comb[0],list):
			current = comb[0][1]
		else:
			current = comb[0]

		if 	['D',n-current] in double and (comb[0],['D',n-current]) not in valid:
			valid.append((comb[0],['D',n-current]))

	return valid


final = []

for i in xrange(2,100):
	p = len(possible(i))
	final.append(p)
	print i,p

print sum(final)
