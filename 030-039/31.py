a = [1,2,5,10,20,50,100]
ways = 0
m = 200
for w0 in xrange(0,m/a[0]+1):
    for w1 in xrange(0,m/a[1]+1):
        if  w0*a[0] + w1*a[1] > m:
            break
        for w2 in xrange(0,m/a[2]+1):
            if w0*a[0]+w1*a[1]+w2*a[2] > m:
                break
            for w3 in xrange(0,m/a[3]+1):
                if w0*a[0]+w1*a[1]+w2*a[2]+w3*a[3] > m:
                    break
                for w4 in xrange(0,m/a[4]+1):
                    if w0*a[0]+w1*a[1]+w2*a[2]+w3*a[3]+w4*a[4] > m:
                        break
                    for w5 in xrange(0,m/a[5]+1):
                        if w0*a[0]+w1*a[1]+w2*a[2]+w3*a[3]+w4*a[4]+w5*a[5] > m:
                            break
                        for w6 in xrange(0,m/a[6]+1):
                            total = w0*a[0]+w1*a[1]+w2*a[2]+w3*a[3]+w4*a[4]+w5*a[5]+w6*a[6]
                            if total > m:
                                break
                            elif total == m:
                                ways +=1
                                print w0,w1,w2,w3,w4,w5,w6

print ways+1
# add +1 beacause of 200p coin