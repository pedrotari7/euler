
N = 10**9
numbers = set()
primes5 = [2, 3, 5]
primes100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def hamming(current,prev):
	if current > N:
		return False
	numbers.add(current)
	for next_p in [_ for _ in primes100 if _ >= prev]:
		if not hamming(next_p*current,next_p): break
	return True

hamming(1,1)

print len(numbers)

