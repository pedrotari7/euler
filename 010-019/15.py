def path(n):
    n += 1
    grid =[n*[0] for k in xrange(n)]
    
    for i in xrange(n):
        for j in xrange(n):
            if j == 0:
                grid[i][j] = 1
            elif i == j:
                grid[i][j] = 2*grid[i][j-1]
            elif i > j:
                grid[i][j] = grid[i][j-1] + grid[i-1][j]
    return grid

initial = (0,0)
dim = 20
ways = path(dim)

print '\n' + str(ways[-1][-1])