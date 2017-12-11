from collections import defaultdict
N = 10**6
n = (N+4)//4

sq = defaultdict(int)

for i in xrange(n,2,-1):
    prev = (i*4-4)
    sq[prev]+=1
    for j in xrange(i-2,2,-2):
        nex = prev+(j*4-4)
        if nex > N: break
        prev = nex
        sq[prev]+=1

print sum(sq[t] == n for t in sq for n in xrange(1,11))