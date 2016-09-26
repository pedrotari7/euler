
N = 10**25

chains = []

def powers(chain, poss):
	s = sum(chain)

	if s == N:
		chains.append(chain)
		return True
	elif s > N:
		return True

	for i,n in enumerate(poss):
		if chain.count(n) < 2:
			if powers(chain +[n],poss[i:]):
				break

numbers = [2**i for i in xrange(83)]


powers([],numbers)

print len(chains)	