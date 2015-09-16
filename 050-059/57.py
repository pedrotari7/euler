from fractions import Fraction as frac

count = 0
previous = frac('7/5')
for i in xrange(998):
    next_frac = frac(1) + frac(1)/frac((frac(2)+previous-frac(1)))
    if len(str(next_frac.numerator)) > len(str(next_frac.denominator)):
        count +=1
    previous = next_frac

print count
