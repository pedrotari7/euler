from itertools import product
import time

limit = 20
count = 0

def new_num(current):

	global count

	if len(current) == limit:
		count += 1
		return

	for new_d in xrange(9-sum(current[-2:])+1):
		new_num(current + [new_d])


poss = [list(ele) for ele in product(range(10),range(10),range(10)) if sum(ele)<10 and ele[0]!=0]

ini = time.time()

for i,pos in enumerate(poss):
	print i+1,'/',len(poss)
	new_num(list(pos))

print time.time() - ini
print count
