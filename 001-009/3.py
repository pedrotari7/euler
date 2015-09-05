number = 600851475143

factors = []
d = 2
while number > 1:
    while number % d == 0:
        factors.append(d)
        number /= d
    d = d + 1

print factors