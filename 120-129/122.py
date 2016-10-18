
def is_available(a, num):

	for poss in 

	return False


n = 15

a = {1:(0,[]),2:(1,[]),3:(2,[2]),4:(2,[2])}


for n in xrange(5,n+1):

	poss = [(n-i-1,i+1) for i in xrange(2,n-1)]	
	print n, poss
	
	temp= []
	for p in poss:
		if p[0] == p[1]:
			temp.append((a[p[0]][0]+1),a[p[0]][1])
		else:
			temp = (1,[])
			if is_available(a,p[0]):
				temp[0]+= a[p[0]][0]
			temp[1].append(a[p[0]][0])

			if is_available(a,p[1]):
				temp[0]+= a[p[1]][0]
			temp[1].append(a[p[1]][0])

				

	print temp

	a[n] = min(temp)

	print min(temp)

print a
