p=[1]
n = 1           
while True:
    i = 0;
    penta = 1;
    p.append(0);
 
    while n<100:  
        sign = -1 if i % 4 > 1 else 1
        p[n] += sign * p[n - penta]
        p[n] %= 1000000
        i+=1
                  
        j = (i / 2 + 1) if (i % 2 == 0) else -(i / 2 + 1)
        penta = j * (3 * j - 1) / 2
                 
    if p[n] == 0: break
    n+=1
    
print n

