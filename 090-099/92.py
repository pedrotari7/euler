import time
count = 0
final = []
exp = 7
max_value = 10**exp
ini = time.time()
for i in xrange(1,exp*9**2+1):
    current = i
    chain = [i]
    while current not in [1,89]:
        new = 0
        for n in str(current):
            new += int(n)*int(n)
        current = new
        if current in final:
            final = final + chain
            count += 1
            break

        if current == 89:
            final = final + chain
            count += 1

        chain.append(current)

final.append(89)
final = list(set(final))

a = [i for i in xrange(1,max_value) if sum([int(d)**2 for d in str(i)]) in final]
print len(a)

print time.time() - ini