def fareyNeighbor(n, (a, b), (c,d)):
    while b + d < n:
        a = a + c
        b = b + d
    return a, b

print fareyNeighbor(10**6, (2,5),(3,7))[0]