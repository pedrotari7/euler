from itertools import combinations
from operator import or_

lines = [list(comb) for comb in combinations(range(1,11),3) if sum(comb) == 14]
combs = list(combinations(lines,5))

valid_combs = []

for comb in combs:
    elements = reduce(or_, [set(ele) for ele in comb])
    if len(elements)!=10:
        continue
    not_valid = False
    count = []
    for ele in elements:
        count.append(len([combi for combi in comb if ele in combi]))
        if count[-1] > 2:
            not_valid = True
            break
        if ele == 10 and count[-1]!=1:
            not_valid = True
            break

    if count.count(2) != 5:
        continue

    elements = list(elements)
    for i,combi in enumerate(comb):
        count2 = []
        for ele in combi:
            count2.append(count[elements.index(ele)])
        if sum(count2)!=5:
            not_valid=True
            break

    if not_valid:
        continue

    valid_combs.append(comb)

print valid_combs