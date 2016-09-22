# from itertools import combinations,combinations_with_replacement,permutations,chain

# op = ['+','-','*','/']
# op_perms = list(chain(*[list(permutations(ele)) for ele in list(combinations_with_replacement(op,3))]))

# def max_consecutive(nums):

# 	valid = []

# 	perms = list(permutations(nums))
# 	for perm in perms:
# 	    perm = [ele+'.' for ele in perm]
	     
# 	    for ope in op_perms:
# 	        num = eval(''.join(list(sum(zip(perm,ope),()))+[perm[-1]]))
# 	        if num > 0 and num.is_integer():
# 	            valid.append((list(sum(zip(perm,ope),()))+[perm[-1]],num))

# 	valid = set([int(ele[1]) for ele in valid])

# 	for i in xrange(1,max(valid)):
# 		if i not in valid:
# 			return i-1

# results = []
# for num in combinations('123456789',4):
# 	num = ''.join(num)
# 	results.append((max_consecutive(num),num))

# print max(results)

from __future__ import division
import itertools

pos = [
    " {minus}{a} {0} {b} {1} {c} {2} {d} ",
    " {minus}({a} {0} {b}) {1} {c} {2} {d} ",
    " {minus}({a} {0} {b}) {1} ({c} {2} {d}) ",
    " {minus}{a} {0} ({b} {1} {c}) {2} {d} ",
    " {minus}{a} {0} (({b} {1} {c}) {2} {d}) ",
    " {minus}{a} {0} {b} {1} ({c} {2} {d}) ",
    " {minus}{a} {0} ({b} {1} {c} {2} {d}) ",
    " {minus}({a} {0} {b} {1} {c}) {2} {d} ",
    " {minus}{a} {0} ({b} {1} ({c} {2} {d})) ",
    " {minus}({a} {0} ({b} {1} {c})) {2} {d} ",
    " {minus}(({a} {0} {b}) {1} {c}) {2} {d} "
]


def find_n(s):
	i = 1
	while True:
		if i not in s:
			return i-1
		i+=1


def get_nums(signals, nums):
	s = set()
	minus = ['-','+']
	for opt in pos:
		for signal in signals:
			for m in minus:

				end_str = ''
				end_str  = opt.format(signal[0], signal[1], signal[2], a=nums[0], b=nums[1], c=nums[2], d=nums[3], minus=m)
				try:
					val = abs(eval(end_str))
					if val.is_integer():
						s.add(int(val))
				except:
					pass
				end_str = ''
	return s

b = list(itertools.product(['-','+','*','/'],repeat=3))

a = list(itertools.combinations(range(1,10),4))

result = []

for r in a:
	print r
	final = set()
	for l in itertools.permutations(list(r)+[-1*i for i in r],4):
		if len(set([abs(i) for i in l])) == 4:
	 		final.update(get_nums(b, l))

	result.append([find_n(final),r])

print max(result)[1]
print max(result)[0]
print int(''.join([str(i) for i in max(result)[1]]))


# final = set()
# for l in itertools.permutations([1,2,3,4]+[-1,-2,-3,-4],4):
# 	print l
# 	print set([abs(i) for i in l]), len(set([abs(i) for i in l]))
# 	if len(set([abs(i) for i in l])) == 4:
#  		final.update(get_nums(b, l))

# print sorted(final)
# print find_n(final), len(final)
