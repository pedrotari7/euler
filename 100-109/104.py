from math import log10

sample = set('123456789')
start = 10**9
f0,f1,k = 1,1,3

while 1:
    new_num = f0 + f1
    if new_num > start:
        if set(str(new_num % start)) == sample:
            if set(str(new_num/10**(int(log10(new_num))+1-9))) == sample:
                    break
    k+=1
    f0 = f1
    f1 = new_num

print k