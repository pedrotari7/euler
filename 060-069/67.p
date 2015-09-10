with open('p067_triangle.txt','r') as f:
    tri = [[int(num)for num in line.split()] for line in  f.read().split('\r\n')]

for i in xrange(len(tri)-2,-1,-1):
    for j in xrange(len(tri[i])):
        tri[i][j] += max(tri[i+1][j],tri[i+1][j+1])

print tri[0][0]