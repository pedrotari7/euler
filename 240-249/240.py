#!/usr/bin/python

from itertools import combinations_with_replacement,permutations,chain
import time


max_dice = 12
n = 20
top = 10
result = 70

print 'Creating all combinations...'
ini = time.time()
comb = list(combinations_with_replacement(range(1,max_dice+1),n))
print time.time() - ini

print 'Selecting the ones that meet the sum requirement...'
ini = time.time()
a = [sorted(ele) for ele in comb if sum(sorted(ele)[-top:])==result]
print time.time() - ini

print 'Creating permutations for the valid ones...'
ini = time.time()
b = [set(permutations(sorted(ele))) for ele in a]
print time.time() - ini


print 'Merging results into single set...'
ini = time.time()
c = list(chain(*b))
print time.time() - ini



print len(c)
