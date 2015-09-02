cubes = []
for i in xrange(0,100000):
    cubes.append(''.join(sorted(str(i**3))))
    if cubes.count(cubes[-1]) == 5:
        index = cubes.index(cubes[-1])
        print index**3
        break