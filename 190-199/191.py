import time
n = 30
valid = 0

def move(previous):
    global valid
    if len(previous) == n:
        valid +=1
        return

    if previous[-2:]!='AA':
        move(previous +'A')

    if 'L' not in previous:
        move(previous +'L')

    move(previous +'O')

ini = time.time()
move('')
print time.time()-ini
print valid