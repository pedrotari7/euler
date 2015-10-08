from itertools import permutations, chain
from math import sqrt
import time

def is_prime(x):
    if x in [1,2,3,5]:
        return True
    if not x % 2 or not x % 3:
        return False
    else:
        div = 5
        while div <= sqrt(x):
            if not x % div:
                return False
            else:
                div += 2
        return True


def all_substr(string):
    for i in xrange(len(string)):

        if i == len(string) - 1:
            yield string

        first_part = string[0:i+1]
        second_part = string[i+1:]

        for j in all_substr(second_part):
            yield ','.join([first_part, j])



perms = permutations('123456789')

result = set()

print 'start'

ini = time.time()

for i,perm in enumerate(perms):
	print ''.join(perm)
	for poss in all_substr(''.join(perm)):
		if all([(is_prime(int(num)) and num!='1')  for num in poss.split(',')]):
			result.add(tuple(sorted([int(num) for num in poss.split(',')])))

print time.time() - ini

print len(result)
