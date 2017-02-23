from itertools import *

pyr = sorted([sum(_) for _ in product(range(1,5),repeat = 9)])
cub = sorted([sum(_) for _ in product(range(1,7),repeat = 6)])

pyr_dict = dict()
for _ in set(pyr):
	pyr_dict[_] = pyr.count(_)

cub_dict = dict()
for _ in set(cub):
	cub_dict[_] = cub.count(_)

total = len(pyr)*len(cub)

win = 0

for c in cub_dict:
	for p in pyr_dict:
		if c < p:
			win += pyr_dict[p]*cub_dict[c]


print str(round(win/float(total),7))[2:9]
