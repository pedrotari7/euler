
pali = [i for i in xrange(100000,999*999) if str(i) == str(i)[::-1]]
result = False

for i in pali[::-1]:
	a = 999
	while a > 99:
		if i%a == 0:
			if i/a<999 and i/a>100:
				result = i
				print a
				print i/a
				break
		a-=1
	if result:
		break

print i 