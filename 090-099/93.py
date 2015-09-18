from itertools import combinations,combinations_with_replacement,permutations,chain

op = ['+','-','*','/']
op_perms = list(chain(*[list(permutations(ele)) for ele in list(combinations_with_replacement(op,3))]))

def max_consecutive(nums):

	valid = []

	perms = list(permutations(nums))
	for perm in perms:
	    perm = [ele+'.' for ele in perm]
	     
	    for ope in op_perms:
	        num = eval(''.join(list(sum(zip(perm,ope),()))+[perm[-1]]))
	        if num > 0 and num.is_integer():
	            valid.append((list(sum(zip(perm,ope),()))+[perm[-1]],num))

	valid = set([int(ele[1]) for ele in valid])

	for i in xrange(1,max(valid)):
		if i not in valid:
			return i-1

results = []
for num in combinations('123456789',4):
	num = ''.join(num)
	results.append((max_consecutive(num),num))

print max(results)