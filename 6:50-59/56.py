max_sum = 0
for a in xrange(1,100):
    for b in xrange(1,100):
        dig_sum = sum([int(d) for d in str(a**b)])
        if dig_sum > max_sum:
            max_sum = dig_sum

print max_sum