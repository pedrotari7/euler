import time, copy
def is_bouncy(n):
    num = ''.join(sorted(str(n)))
    return int(num)!=n and int(num[::-1])!=n
ini = time.time()
special = []
n = 100
exp = 3

while n < 10**exp:
    if not is_bouncy(n):
        special.append(n)
    n+=1

exp += 1
count  = len(special) + 99

while exp <= 15:
    print exp
    new_special = []
    print len(special)
    for i in special:
        for j in xrange(1,10):
            test = j*10**(exp-1) + i
            #print test
            if not is_bouncy(test):
                new_special.append(test)

    count += len(new_special)
    special = copy.copy(new_special)
    exp += 1

print time.time()-ini

print count
