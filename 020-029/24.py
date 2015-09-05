import itertools
print sorted([int(''.join(num)) for num in itertools.permutations('0123456789')])[999999]