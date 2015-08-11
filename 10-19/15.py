
def path(point,ways,dim):

	if ways == []:
		ways.append([point])
	else:	
		ways[-1].append(point)

	if point == (dim,dim):
		print ways[-1]
		ways.append([])
		return ways

	if point[0]+1 < dim+1:
		ways = path((point[0]+1,point[1]),ways,dim)

	if point[1]+1 < dim+1:
		ways = path((point[0],point[1]+1),ways,dim)


	return ways



initial = (0,0)
dim = 4
ways = path(initial,[],dim)

for ele in ways:
	print str(ele)
print len(ways)-1