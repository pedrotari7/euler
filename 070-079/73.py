def fareyNeighbor(n, a = 2, b = 5, c = 3, d = 7):
    '''Given a / b and c / d, where a / b and c / d are two farey neighbors 
    in a valid farey sequence, returns the neighbor of c / d in the nth farey 
    sequence''' 
    while b + d < n:
        a = a + c
        b = b + d
    return a, b

def fareyGenerator(n, a=0, b=1, c=1, d = None):
    '''Given a / b and c / d, where a / b and c / d are two farey neighbors
    in an nth farey sequence, returns the next item in the farey sequence''' 
    if d == None:
        d = n
    while c <= n:
        k = int((n+b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        yield Fraction(a, b)

def fareyRange(n):
    '''Return number of items between 1/3 and 1/2 in the nth farey sequence'''
    (a, b) = fareyNeighbor(n, 2, 7, 1, 3) # calculate item to the left of 1/3
    f_gen = fareyGenerator(n, a, b, 1, 3) # generate next item using (a, b)
    p_q = f_gen.next()
    count = 0
    while p_q < Fraction(1, 2):
        if p_q > Fraction(1, 3): count += 1
        p_q = f_gen.next()
    return count



