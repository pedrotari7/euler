import math
def fac(n):
	return math.factorial(n)

a = [0,1,2,3,4,5,6,7,8,9]

num = ''

while 1:
	for i in range(9,0,-1):
		print "i: " + str(i)
		for j in xrange(1,10):
			print "j: " + str(j)
			print "fac(i)*j: " + str(fac(i)*j)
			if fac(i)*j > 1000000:
				print "a[j-2]: " + str(a[j-2])
				num = num + str(a[j-2])
				a.remove(a[j-2])
				print "a: " + str(a)
				print "num: " + str(num)
				break
		print "num: " + str(num)
		if a==[]:
			break
	if a == []:
		break
print num 