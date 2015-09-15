def dot(P,Q):
     return sum(p*q for p,q in zip(P,Q))

def is_inside(A,B,C,P=(0,0)):

    v0 = (C[0]-A[0],C[1]-A[1])
    v1 = (B[0]-A[0],B[1]-A[1])
    v2 = (P[0]-A[0],P[1]-A[1])

    d00 = dot(v0,v0)
    d01 = dot(v0,v1)
    d02 = dot(v0,v2)
    d11 = dot(v1,v1)
    d12 = dot(v1,v2)

    invDenom = 1 / float(d00 * d11 - d01 * d01)
    u = (d11 * d02 - d01 * d12) * invDenom
    v = (d00 * d12 - d01 * d02) * invDenom

    return (u >= 0) and (v >= 0) and (u + v < 1)


A = (-340,495)
B = (-153,-910)
C = (835,-947)

X = (-175,41)
Y = (-421,-714)
Z = (574,-645)

print is_inside(X,Y,Z)

with open('p102_triangles.txt','r') as f:
    triangles = []
    a = f.read()
    for tri in a.split('\n'):
            ele = tri.split(',')
            triangles.append([(int(ele[0]),int(ele[1])),(int(ele[2]),int(ele[3])),(int(ele[4]),int(ele[5]))])

count = 0
for tri in triangles:
    if is_inside(tri[0],tri[1],tri[2]):
        count+=1