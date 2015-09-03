
import itertools
pandigital = [''.join(num) for num in itertools.permutations('0123456789') if num[0] is not '0']
special = []
for pan in pandigital:
        if int(pan[7:10])%17==0:
                if int(pan[6:9])%13==0:
                        if int(pan[5:8])%11==0:
                                if int(pan[4:7])%7==0:
                                        if int(pan[3:6])%5==0:
                                                if int(pan[2:5])%3==0:
                                                        if int(pan[1:4])%2==0:
                                                                special.append(int(pan))
print sum(special)