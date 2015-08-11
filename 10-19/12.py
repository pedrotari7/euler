def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

i = 1

trig = [0]
size = 0

while  size < 500:

	trig.append(trig[-1] + i) 

	size = len(factors(trig[-1]))

	i += 1

print trig[-1]
print size