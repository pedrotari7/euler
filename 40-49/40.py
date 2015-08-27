import math

d = '0'
i = 1
while 1:

	d += str(i)

	if len(d) > 10**6 :
		break


	i += 1

print int(d[1])*int(d[10])*int(d[10**2])*int(d[10**3])*int(d[10**4])*int(d[10**5])*int(d[10**6]) 
