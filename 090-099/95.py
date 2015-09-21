import time

def factors(n):
	f = list(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
	f.remove(n)
	return sum(f)

def len_chain(key,d,chain_len):
    chain = [key]
    while 1:
        print d[key],len(chain)
        current = d[chain[-1]]
        chain.append(current)
        if current in chain_len:
            if chain_len[current] + len(chain) < n:
                chain_len[key] = chain_len[current] + len(chain)
            return chain_len[current] + len(chain),chain_len
            
            
        if chain.count(current)==2 or current > limit or current > n or current not in d or d[current]==current:
            if current in chain:
                print chain[:-1]

                chain_len[key] = len(chain)
                return len(chain),chain_len

        


ini = time.time()
n = 100000
limit = 10**6
d = dict()
d[1] = 1
for i in xrange(2,n+1):
    temp = factors(i)
    if temp < limit:
        d[i] = temp


print 'start'

longest = 0


chain_len=dict()

for key in d:
    len_chain(key,d,chain_len)
    
print len(d.keys())
print longest
print time.time()-ini