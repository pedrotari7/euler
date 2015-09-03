import math
p = []
n=1
while 1:
    new = n*(3*n-1)/2
    a = [num for num in p if new-num>0 and ((1+math.sqrt(1+24*(new+num)))/6.).is_integer() and (new-num) in p]
    if a:
        print 'found'
        print new - a[0]
        break

    p.append(new)
    n+=1