from itertools import combinations_with_replacement as comb, chain

n = 20
nums = range(1,n)

combi = [list(comb(nums,i)) for i in xrange(2,n+1)]
combi = list(chain(*combi))
print len(combi)

result = [ele for ele in combi if sum(ele) == n]
print len(result)
