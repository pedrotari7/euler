import itertools
pandigital = sorted([int(''.join(num)) for num in itertools.permutations('123456789')])
special = []
i = 192
while i<10000:
        if i == 1000: i = 5000
        pand = ''
        for num in xrange(1,10):
                pand += str(num*i)
                if len(pand)>=9:
                         break
        if int(pand) in pandigital:
                special.append(int(pand))
        i += 1
print max(special)
