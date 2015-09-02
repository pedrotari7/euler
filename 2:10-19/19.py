
m = [0,31,0,31,30,31,30,31,31,30,31,30,31]
d = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

wd = 0
end = [31,12,2000,'']
c = [1,1,1900,'monday']
days = [tuple(c)]

while 1:

	if c[1] != 2: 
		max_month = m[c[1]]
	else:
		if c[2]%4 == 0:
			if c[2]%100 == 0:
				if c[2]%400 == 0:
					max_month = 29
				else:
					max_month = 28
			else:
				max_month = 29

		else:
			max_month = 28

	if (c[0] + 1) > max_month:
		if c[1] + 1 > 12:
			c[2] += 1
			c[1] = 1  
		else:
			c[1] += 1
		c[0]=1
	else:
		c[0]+=1 

	wd = (wd + 1) % 7

	c[3] = d[wd]

	days.append(tuple(c))

	if c[0] == end[0] and c[1] == end[1] and c[2] == end[2]:
		break

for ele in days:
	if ele[3] == 'sunday' and ele[0] == 1:
		print ele

print len([ele for ele in days if ele[3] == 'sunday' and ele[0] == 1 and ele[2] >= 1901])
