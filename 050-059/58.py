import math
import time

def update_primes(primes,max_value,last):

	i=last

	new_primes = []

	while i<max_value+1:

		for num in primes:

			if i%num == 0:
				break

			if num > math.sqrt(i):
				new_primes.append(i)
				last = i
				break
		i += 1

	new_set = primes | set(new_primes)
	return last, new_set


def get_diag_numbers(grid):
	diag = []

	for i in xrange(len(grid)):
		for j in xrange(len(grid)):
			if j == i or j+i == len(grid)-1:
				diag.append(grid[i][j])

	return diag


def create_grid(n,grid=[]):

	if n == 1:
		grid = [1]
		return grid
 	
	start = n-3
	if n > 3:
		j = grid[start][start]
	else:
		grid  = [[5,4,3],[6,1,2],[7,8,9]]
		return grid

	while sum([len(line) for line in grid]) < n*n:

		for ind in xrange(n-3,-1,-1):
			j+=1
			grid[ind].append(j)

		grid = [range(j+n,j,-1)] + grid
		j += n
		
		for ind in xrange(1,n-1):
			j+=1
			grid[ind] = [j] + grid[ind]


		grid = grid + [range(j+1,j+1+n)]
		j += n

	return grid



grid = [1]
primes = set([2])
i = 3
last =2
per = 100
while per>10:
	ini1 = time.time()
	grid = create_grid(i,grid)
	stop1 = time.time()-ini1


	ini = time.time()
	diag = get_diag_numbers(grid)
	stop2 = time.time()-ini

	max_value = max(diag)

	ini = time.time()
	if max_value > last:
		last,primes = update_primes(primes,max_value,last)
	stop3 = time.time()-ini

	ini = time.time()

	per = int(round(sum([num in primes for num in diag])/float(len(diag))*100))
	stop4 = time.time()-ini

	print "n={} with {}% of primes".format(i,per) 
	#print "grid:" + str(int(stop1*100))
	#print "diag:" + str(int(stop2*1000))
	#print "primes:" + str(int(stop3*1000))
	#print "per1:" + str(int(stop4*1000))
	#print "per2:" + str(int(stop5*1000))
	#print "total:" + str(int((time.time()-ini1)*1000))

	i+=2