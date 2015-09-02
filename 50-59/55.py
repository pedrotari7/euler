
pali = []
for i in xrange(1,10000):
	count = 0
	num = i
	while count < 50:
		new = num + int(str(num)[::-1])
		count += 1 

		if new == int(str(new)[::-1]):
			break

		num = new
		if count >= 50:
			pali.append(i)

print len(pali)