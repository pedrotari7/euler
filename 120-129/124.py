def rad(number):
    factors = []
    d = 2
    while number > 1:
        while number % d == 0:
            factors.append(d)
            number /= d
        d = d + 1
    return reduce(lambda x,y:x*y, set(factors))

final = [1]
for i in xrange(2,10**5+1):
 	final.append((rad(i),i))


print sorted(final)[10000-1]