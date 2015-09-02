from math import log

with open('p099_base_exp.txt','r') as f:
    exps = [[int(n) for n in line.split(',')] for line in f.read().split()]

    max_exp = [1,1]
    index = 0
    for i,exp in enumerate(exps):
        if exp[1]*log(exp[0]) > max_exp[1]*log(max_exp[0]):
            max_exp = exp
            index = i+1
    
    print max_exp
    print index
