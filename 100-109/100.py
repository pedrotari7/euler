from math import sqrt

def find_next_solution(n_b, step):
    while True:
        n_b+= step
        T = 2*n_b*(n_b-1)
        S = int(sqrt(T))
        if S*(S+1) == T:
            return int(n_b), S+1  # blues, total

tot = 0
step = 5
blues = 15
while True:
    blues, tot = find_next_solution(blues, step)
    step = blues//step
    if tot > 10**12:
        break


print blues