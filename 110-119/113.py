import time, copy
def is_non_bouncy(n):
    num = ''.join(sorted(str(n)))

    if len(set(num)) == 1:
        return (n,'=') 
    elif int(num)==n:
        return (n,'+') 
    elif int(num[::-1])==n:
        return (n,'-')
    else:
        return False

ini = time.time()
special = []
n = 100
exp = 3

while n < 10**exp:
    result = is_non_bouncy(n) 
    if result:
        print result
        special.append(result)
    n+=1

exp += 1
count  = len(special) + 99

while exp <= 20:
    print exp
    new_special = []
    print len(special)
    for i,mode in special:
        if mode == '+':
            scan = xrange(1,int(str(i)[0])+1)
        elif mode == '-':
            scan = xrange(9,int(str(i)[0])-1,-1)
        elif mode == '=':
            scan = xrange(1,10)
        for j in scan:
            test = j*10**(exp-1) + i
            #print test
            result = is_non_bouncy(test)
            if result:
                new_special.append(result)
    print len(new_special)
    count += len(new_special)
    special = copy.copy(new_special)
    exp += 1

print time.time()-ini

print count
print 12951-count

