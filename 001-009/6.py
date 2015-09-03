n = 100

SUM = (n+1)*(n)/2
squared_sum = SUM*SUM

print squared_sum

sum_squares = sum([i*i for i in xrange(1,n+1)])

print sum_squares

diff = squared_sum - sum_squares

print diff