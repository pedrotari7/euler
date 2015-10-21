from numpy.linalg import tensorsolve as solve

def u(n):
	return 1+sum([((-1)**i)*(n**i) for i in xrange(1,11)])

def OP(level,seq):

	A = [[i**(num) for num in xrange(level)] for i in xrange(1,level+1)]

	quoc = solve(A,seq[:level])

	return sum([q*(level+1)**i for i,q in enumerate(quoc)])

N = 10

seq = [u(i) for i in xrange(1,N+1)]

print int(sum([OP(level,seq) for level in xrange(1,N+1)]))