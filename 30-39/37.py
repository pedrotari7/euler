import math
primes = [2]
special = []
i=2
while len(special) < 11:
        for num in primes:
                if i%num == 0:
                        break
                if num > math.sqrt(i):
                        primes.append(i)
                        if len(str(i)) > 1:
                                is_special = True
                                for dig in xrange(1,len(str(i))):
                                        if int(str(i)[dig:]) not in primes:
                                                is_special = False
                                                break
                                        if int(str(i)[:dig]) not in primes:
                                                is_special = False
                                                break
                                if is_special:
                                        special.append(i)
                                        print 'special prime :' + str(i)
                                break
        i += 1
print sum(special)