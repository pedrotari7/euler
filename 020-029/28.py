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

while i<1002:
	grid = create_grid(i,grid)
	i+=2

diag = get_diag_numbers(grid)

print sum(diag)