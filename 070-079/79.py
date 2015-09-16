from itertools import chain,permutations

def check_valid(num,logins):
    for login in logins:
        if not (num.index(login[0]) < num.index(login[1]) < num.index(login[2])):
            return False
    return True

with open('p079_keylog.txt','r') as f:
    logins = [[int(d) for d in  ele] for ele in f.read().split()]

a = set(list(chain(*logins)))

for num in permutations(a):
    if check_valid(num,logins):
        print ''.join([str(i) for i in num])
        break