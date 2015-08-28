import itertools
pandigital = [''.join(num) for num in itertools.permutations('123456789')]
special = []
for i in xrange(2,100):
        for j in xrange(10**len(str(i)),10**(9-len(str(i)))):
                if len(str(i)+str(j)+ str(i*j)) > 9:
                        break
                elif  len(str(i)+str(j)+ str(i*j)) < 9:
                        continue
                elif any([(ele in str(j) or ele in str(i*j)) for ele in set(str(i))]):
                        continue
                elif any([ele in str(i*j) for ele in set(str(j))]):
                        continue
                if (str(i)+str(j)+ str(i*j)) in pandigital:
                        special.append(i*j)
print sum(set(special))