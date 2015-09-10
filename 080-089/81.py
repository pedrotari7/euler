import copy

def path(arg):
    n = len(arg)
    grid = copy.deepcopy(arg)
    for i in xrange(n):
        for j in xrange(n):
            if i > 0 and j > 0:
                grid[i][j] += min(grid[i][j-1],grid[i-1][j])
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]

    return grid

def find_path(grid,a):
    n = len(grid)
    final = [(n-1,n-1)]
    i = n-1
    j = n-1
    while i!=0 or j!=0:
        if i > 0 and j > 0:
            if grid[i-1][j] < grid[i][j-1]:
                i-=1
            else:
                j-=1
        else:
            if j==0:
                i-=1
            elif i==0:
                j-=1
        final.append((i,j))

    return [a[r][s] for r,s in final]

a = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]

with open('p081_matrix.txt','r') as f:
    a = [[int(num) for num in line.split(',')] for line in f.read().split('\r\n')]

grid = path(a)

b = find_path(grid,a)

print b
print sum(b)