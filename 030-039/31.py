
import itertools

a = [0.01,0.05,0.1,0.2,0.5,1]

lst = [list(ele) for ele in list(itertools.product([0, 1], repeat=len(a)))]

combinations = []


for comb in lst:

	w = comb

	for w1 in xrange(1,201):
		if w[0] != 0:
			w[0] = w1
		for w2 in xrange(1,101):
			if w[1] != 0:
				w[1] = w2
			for w3 in xrange(1,21):
				if w[2] != 0:
					w[2] = w3
				for w4 in xrange(1,11):
					if w[3] != 0:
						w[3] = w4
					for w5 in xrange(1,5):
						if w[4] != 0:
							w[4] = w5
						for w6 in xrange(1,2):
							if w[5] != 0:
								w[5] = w6

							if  sum([c*b for c,b in zip(a,w)]) == 2:
								combinations.append(w)
								print len(combinations)
								break


print combinations
print len(combinations)


# add +1 beacause of 200p coin