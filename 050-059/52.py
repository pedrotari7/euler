for i in xrange(2,int(987654321/6)):
    found = True
    for mult in xrange(2,7):
        if sorted([c for c in str(i)]) != sorted([c for c in str(i*mult)]):
            found = False
            break
    if found:
        special = i
        break
print special
