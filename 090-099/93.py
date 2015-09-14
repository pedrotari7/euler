from itertools import combinations_with_replacement,permutations,chain

valid = []
nums = '12345'
op = ['+','-','*','/']
# [list(ele) for ele in list(combinations_with_replacement(op,4)) if op[0] == '-']
op_perms = list(chain(*[list(permutations(ele)) for ele in list(combinations_with_replacement(op,3))]))
perms = list(permutations(nums))
#perms = perms[0:1]

for perm in perms:
    perm = [ele+'.' for ele in perm]
    for ope in op_perms:
        num = eval(''.join(list(sum(zip(perm,ope),()))+[perm[-1]]))
        if num > 0 and num.is_integer():
            valid.append((list(sum(zip(perm,ope),()))+[perm[-1]],num))


valid_set = set([int(ele[1]) for ele in valid])


