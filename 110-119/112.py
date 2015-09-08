special = 0
n = 99
pre = 0
while pre < 0.99:
    num = ''.join(sorted(str(n)))
    if int(num)!=n and int(num[::-1])!=n:
        special+=1
    pre = float(special)/float(n)
    n+=1

print n-1