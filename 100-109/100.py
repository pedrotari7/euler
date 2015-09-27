from decimal import Context,Decimal
from math import sqrt
dot100 = Context(prec=105)

limit = 10**12

K = ((2*10**12-1)**2-1)/8.

NB = int((1+(1+4*Decimal(K)).sqrt())/2)+1



while 1:

    NT = (1+ sqrt(1+8*NB*(NB-1)))/2.

    print NT

    if NT.is_integer():
        print "%d" % NT
        print "%d" % NB
        print "%d" % (NT-NB)
        break


    NB += 1

