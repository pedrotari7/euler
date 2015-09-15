import math
result = []
L = 3

while len(result)<=5:

    part = 2*math.sqrt(5*L**2-1)/5.

    if (part-0.8).is_integer():
        b = int(part-0.8)
        print (L,b)
        result.append((L,b))
        L+=100
    elif (part+0.8).is_integer():
        b = int(part+0.8)
        print (L,b)
        result.append((L,b))
        L+=100
    L+=2

