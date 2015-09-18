from itertools import combinations_with_replacement as comb_r, permutations,chain,combinations

def is_right((a,b)):
    d1 = a[0]**2+a[1]**2
    d2 = b[0]**2+b[1]**2
    d3 = (a[0]-b[0])**2+(a[1]-b[1])**2
    d = [d1,d2,d3]
    h = max(d)
    d.remove(h)
    return d[0]+d[1] == h

n = 50

points = list(set(chain(*[permutations(ele) for ele in comb_r(range(n+1),2)])))
points.remove((0,0))

tri = [ele for ele in combinations(points,2) if is_right(ele)]

print len(tri)