max_value = 20 
i=max_value
while 1:

	if all([i%j==0 for j in xrange(2,max_value+1)]):
		break


	i = i+max_value

print i
