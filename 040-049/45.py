t,p,h = [],[],[]
n=144
while 1:
    t.append(n*(n+1)/2)
    p.append(n*(3*n-1)/2)
    h.append(n*(2*n-1))

    if h[-1] in p:
        print '!!! {} !!!'.format(h[-1])
        break
    n+=1
