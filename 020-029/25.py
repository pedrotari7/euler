i = 2
fib = (1,1)
size = 1

while size < 1000:

	fib = (fib[1], fib[0] + fib[1])

	size =len(str(fib[1]))

	i +=1


print i 