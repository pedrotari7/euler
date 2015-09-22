def factors(n):
    f = list(set(reduce(
        list.__add__,
        ([i, n // i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    f.remove(n)
    return sum(f)


n = 15000
limit = 10**6
d = {1: 1}
d[1] = 1

final = dict()

for i in xrange(2, n + 1):
    chain = [i]

    while 1:
        if chain[-1] not in d:
            d[chain[-1]] = factors(chain[-1])
        current = d[chain[-1]]

        if current == i:
            final[i] = chain
            break
        if current in chain or current > limit or (current in d and d[current] == current):
            break

        chain.append(current)

print max([(len(final[ele]),min(final[ele])) for ele in final])