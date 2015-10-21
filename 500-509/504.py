from itertools import product
from math import sqrt
from fractions import gcd
import time
m = 100
nums = range(1,m+1)

combs = product(nums,nums,nums,nums)

count = 0

ini = time.time()

for a,b,c,d in combs:
	
	A = (a+d)*(c+b)/2.

	i = gcd(a,b) + gcd(a,c) + gcd(c,d) + gcd(d,b)

	result = A-i/2.+1

	if sqrt(result).is_integer():
		count+=1

print count 

print time.time()-ini
