from itertools import product


pyramidal =  [sum(w) for w in product([1,2,3,4],repeat=9)]

cubic =  [ sum(w) for w in product([1,2,3,4,5,6],repeat=6)]

print len(pyramidal)

print len(cubic)

a = [(x,y) for x in pyramidal for y in cubic]

print len(a)