N = 10**6
n = (N+4)//4

total=0

for i in xrange(n,2,-1):
    prev = (i*4-4)
    total += 1
    for j in xrange(i-2,2,-2):
        nex = prev+(j*4-4)
        if nex > N: break
        prev = nex
        total += 1

print total