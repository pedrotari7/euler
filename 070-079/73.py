def fareyrange(n,left1,left2,right):
    a1 = left1
    a2 = left2
    counter = 1
    while a2!=right:
        flr = int((n+a1[1])/a2[1])
        b = (flr*a2[0]-a1[0], flr*a2[1]-a1[1])
        a1,a2 = a2,b
        counter+=1
    return counter-1
    
print fareyrange(12000,(1,3),(4000,11999),(1,2))


