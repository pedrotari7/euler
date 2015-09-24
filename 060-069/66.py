import math

def solve_pell(D):
    if(D==0):return
    L,a_0,p_0,q_0=[],int(math.sqrt(D)),0,1
    L.append(a_0)
    while(True):
        p_1=a_0*q_0-p_0
        q_1=(D-p_1**2)//q_0
        a_1=(L[0]+p_1)//q_1
        L.append(a_1)
        if(a_1==2*L[0]):break
        p_0,q_0,a_0=p_1,q_1,a_1
    r=len(L)-2
    if(r%2==0):
        r=2*r+1
        T=L;
        L[len(L):]=T[1:]
         
    p0,p1,p2=L[0],L[0]*L[1]+1,0;
    q0,q1,q2=1,L[1],0;
    for i in range(2,r+1):
        p2=p1*L[i]+p0
        q2=q1*L[i]+q0
        #print p2,' ',q2
        p0,p1=p1,p2
        q0,q1=q1,q2

    return p1,q1;
    
    
solu = []
for D in [i for i in xrange(2,1000) if not math.sqrt(i).is_integer()]:
    solu.append((solve_pell(D)[0],D))
    
print max(solu)
print max(solu)[1]