for a in xrange(1,1000):
	for b in xrange(1,1000):

		if b>a:
			if (a + b) == (a*b/1000 + 500):
			 	c = 1000-a-b
			 	if c > b:
			 		if (a*a + b*b) == c*c:
					 	print a*b*c