basic = ['one','two','three','four','five','six','seven','eight','nine']
b = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

numbers = []
for i in xrange(1,1000):
	number = ''


	if len(str(i)) == 1:
		number += basic[i-1]

	if len(str(i)) == 3:
		initial_digit = int(str(i)[0]) 

		number += basic[initial_digit-1] + ' hundred'

		if int(str(i)[1:]) !=0:
			number += ' and ' 


	if len(str(i)) > 1:
		last_digit = int(str(i)[-1])

		if int(str(i)[-2:]) < 20 and int(str(i)[-2:])>0:
			
			if int(str(i)[-2:]) < 10:
				number += basic[last_digit-1]
			else:
				number += b[last_digit]

		else:
			first_digit = int(str(i)[-2]) 
			if last_digit == 0:
				if first_digit != 0:
					number += c[first_digit-1]
			else:
				number += c[first_digit-1]+'-'+basic[last_digit-1]


	numbers.append((i,number))

numbers.append((1000,'one thousand'))

for ele in numbers:
	print str(ele) + '\n'

print  len(''.join([ele[1].replace(' ','').replace('-','') for ele in numbers]))

