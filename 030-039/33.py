from fractions import Fraction


frac1 = [(d,n) for d in xrange(10,100) for n in xrange(d+1,100) if set(str(d)) & set(str(n))]

new_n,new_d= 1,1

final = []
for n,d in frac1:
	c = list(set(str(d)) & set(str(n)))[0]
	if (str(n).find(str(c))) != (str(d).find(str(c))):
		new_frac = (int(str(n)[(str(n).find(str(c))+1)%2]),int(str(d)[(str(d).find(str(c))+1)%2]))
		if new_frac[1]!=0 and n/float(d)==new_frac[0]/float(new_frac[1]):
			new_n*= n
			new_d*= d

print (Fraction(new_n)/Fraction(new_d)).denominator