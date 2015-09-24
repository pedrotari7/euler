from itertools import permutations

def trig(n):
    return n*(n+1)//2

def quad(n):
    return n*n

def penta(n):
    return n*(3*n-1)//2

def hexa(n):
    return n*(2*n-1)

def hepta(n):
    return n*(5*n-3)//2

def octo(n):
    return n*(3*n-2)

def ajout(d,k,x):
    try:
        d[k].append(x)
    except:
        d[k]=[x]

listef=[trig,quad,penta,hexa,hepta,octo]
listedict=[dict() for i in range(6)]    
listenb=[[f(n) for n in range(150) if f(n)>=1000 and f(n)<=9999 and str(f(n))[-2]!='0'] for f in listef]
for i in range(6):
    for x in listenb[i]:
        ajout(listedict[i],x//100,x)

liste_possibilites=[]
for p in permutations([0,1,2,3,4]):
    for x in listenb[-1]: 
        chaines=[[x]]
        for i in range(5):
            chaines2=[]
            for c in chaines:
                try:
                    nb=c[-1]
                    listecontinuation=listedict[p[i]][nb%100]
                    for y in listecontinuation:
                        chaines2.append(c+[y])
                except:
                    continue
            chaines=chaines2
        liste_possibilites+=chaines
solutions=[x for x in liste_possibilites if x[-1]%100==x[0]//100]
solution=solutions[0]
print(sum(solution))