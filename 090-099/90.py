import itertools

a = ['01','04','09','16','25','36','49','64','81']

combs = set([tuple(sorted(ele)) for ele in itertools.combinations(range(10),6)])

final = []
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

		valid = True
		for square in a:
			if not (int(square[0]) in comb and int(square[1]) in comb2) and not (int(square[0]) in comb2 and int(square[1]) in comb):
				valid = False
		if valid:
			final.append(ele)


print len(final)/2

