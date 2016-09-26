

numbers = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def hamming(current):

	if current > 10**5:
		return
	else:
		numbers.append(current)

	for next_p in primes:
		hamming(next_p*current)


print len(primes)

current = 1
hamming(current)


print len(numbers), len(set(numbers))

