import math,copy

octnum,heptnum,hexnum,pennum,squarenum,trinum = [],[],[],[],[],[]


for i in xrange(1,10**4):

	if len(str(i*(3*i-2)))==4:
		octnum.append(i*(3*i-2))

	if len(str(i*(5*i-3)/2))==4:
		heptnum.append(i*(5*i-3)/2)

	if len(str(i*(2*i-1)))==4:
		hexnum.append(i*(2*i-1))

	if len(str(i*(3*i-1)/2))==4:
		pennum.append(i*(3*i-1)/2)

	if len(str(i*i))==4:
		squarenum.append(i*i)

	if len(str(i*(i+1)/2))==4:
		trinum.append([i*(i+1)/2])

list_num = [squarenum,pennum,hexnum,heptnum,octnum]

new = trinum

for i in xrange(len(list_num)):
	new_temp = copy.copy(new)
	new = []
	for num in new_temp:
		for numx in list_num[i]:
			if str(num[-1])[:2] == str(numx)[-2:]:
				new.append(num + [numx])

print new