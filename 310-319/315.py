from itertools import repeat
#   _     1
# | _ | 2   3
# | _ |   4
#       5   6
#         7

m = dict()
m[0] = [1,2,3,5,6,7] 
m[1] = [3,6]
m[2] = [1,3,4,5,7]
m[3] = [1,3,4,6,7]
m[4] = [2,3,4,6]
m[5] = [1,2,4,6,7]
m[6] = [1,2,4,5,6,7]
m[7] = [1,2,3,6]
m[8] = [1,2,3,4,5,6,7]
m[9] = [1,2,3,4,6,7]

def print_d(n):
    if n == None: return
    if 1 in m[n]: print '----\n',
    if 2 in m[n] and 3 in m[n]: print '|  |'
    elif 2 in m[n]: print '|'
    elif 3 in m[n]: print '   |'
    if 4 in m[n]: print '----'
    if 5 in m[n] and 6 in m[n]: print '|  |'
    elif 5 in m[n]: print '|'
    elif 6 in m[n]: print '   |'
    if 7 in m[n]: print '----'

def primes(n):
    N = n // 2
    sieve = [True] * N
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            start = i ** 2 // 2
            sieve[start::i] = repeat(False, len(range(start, N, i)))
    return set([2] + [2*i+1 for i in xrange(1, N) if sieve[i]])

def digit_root(n):
    return sum(map(int,str(n)))

def droots(n):
    dr = [n]
    while len(str(dr[-1])) > 1:
        dr.append(digit_root(dr[-1])) 
    return dr

def sam_switch_cost(a):
    return sum(len(m[d]) for d in map(int,str(a)))

def sam_droots_transition_cost(n):
    return 2*sum(map(sam_switch_cost,droots(n)))

def max_switch_cost(prev,a):
    if a == None and prev == None: return 0
    if prev == None: return sam_switch_cost(a)
    if a == None: return sam_switch_cost(prev)
    total = 0
    pad = max(len(str(prev)), len(str(a)))
    for x,y in zip(str(prev).rjust(pad),str(a).rjust(pad)):
        if x == ' ': total+=len(m[int(y)])
        elif y == ' ': total+=len(m[int(x)])
        else:
            for i in xrange(len(x)):
                total += len(set(m[int(x)]).symmetric_difference(set(m[int(y)])))
    return total

def max_droots_transition_cost(n):
    prev = None
    total = 0
    dr = droots(n) + [None]
    for d in dr:
        total += max_switch_cost(prev, d)
        prev = d 
    return total

p = [_ for _ in primes(2*10**7) if _ > 10**7]

print sum(sam_droots_transition_cost(_)-max_droots_transition_cost(_) for _ in p)