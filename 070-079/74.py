def gen_next(n):
    from math import factorial
    return sum([factorial(int(i)) for i in str(n)])

special = 0
chains = dict()
for i in xrange(1,10**6):
    print i
    if i not in chains:
        chains[i] = [i]
    while 1:
        next_num = gen_next(chains[i][-1])
        if next_num in chains:
            chains[i] += chains[next_num] 
            break
        if next_num in chains[i]:
            break
        
        chains[i].append(next_num)
    if len(chains[i]) == 60:
        special+=1
print special