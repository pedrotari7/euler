
import math

max_p = 1000

solu = dict()

for p in xrange(3,max_p +1):
	for a in xrange(1,max_p-2):
		for b in xrange(a+1,p-a-1):

			print 'a:' + str(a) + ' b:' + str(b) + ' p:' + str(p)


			if a+b < p:
				c = math.sqrt(a**2+b**2)

				if a + b + c == p:

					if not solu.has_key(p):
						solu[p] = [(a,b,c)]
					else:
						solu[p].append((a,b,c))

					# print 'a:' + str(a) + ' b:' + str(b) + ' c:' + str(c) + ' p:' + str(p)

print solu