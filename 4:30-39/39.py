
import math

max_p = 1000

solu = dict()

for p in xrange(120,max_p +1):
	for a in xrange(1,max_p-2):
		for b in xrange(a+1,p-a-1):

			if a+b < p:
				c = math.sqrt(a**2+b**2)

				if a + b + c == p:

					if not solu.has_key(p):
						solu[p] = [(a,b,c)]
					else:
						solu[p].append((a,b,c))

					# print 'a:' + str(a) + ' b:' + str(b) + ' c:' + str(c) + ' p:' + str(p)

sol = max([(sol,len(solu[sol])) for sol in solu],key=lambda item:item[1])

print 'Number is ' + str(sol[0]) + ' with ' + str(sol[1]) + ' solutions'