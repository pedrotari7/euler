t0,t1 = 2,3

for i in xrange(2,100):
    k = 2 * ( i + 1 ) / 3 if i % 3 == 2 else 1
    next_num = k * t1 + t0
    t0 = t1
    t1 = next_num

print sum([int(j) for j in str(next_num)])