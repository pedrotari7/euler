import itertools

a = ['01','04','09','16','25','36','49','64','81']

d1 = [0,1,2,3,4,6,8]
d2 = [1,4,9,6,5]

combs = set([tuple(sorted(ele)) for ele in itertools.combinations([0,1,2,3,4,5,7,6,8,9],6)])

print len(combs)

poss = []
for comb in combs:
	if 9 in comb:
		comb = set(list(comb) + [6])
	elif 6 in comb:
		comb = set(list(comb) + [9])
	for comb2 in combs:
		if 9 in comb2:
			comb2 = set(list(comb2) + [6])
		elif 6 in comb2:
			comb2 = set(list(comb2) + [9])
		poss.append([comb,comb2])

print len(poss)
final = []
for ele in poss:
	valid = True
	for square in a:
		if not (int(square[0]) in ele[0] and int(square[1]) in ele[1]) and not (int(square[0]) in ele[1] and int(square[1]) in ele[0]):
			valid = False
	if valid:
		final.append(ele)

print len(final)/2.

