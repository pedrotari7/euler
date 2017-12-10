def reverse(n):
    return int(str(n)[::-1])

def allodd(n):
    return all(int(d)%2 for d in str(n))

N = 10**7
total = 0
for i in xrange(N):
    i_rev = reverse(i)
    if len(str(i)) == len(str(i_rev)) and allodd(i+i_rev):
        total+=1

print total