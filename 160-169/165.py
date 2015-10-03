from math import sqrt

def generate_lines(size):

	lines = []
	s = [290797]
	

	for i in xrange(size*4+1):
		s.append(s[i]*s[i]%50515093)


	for n in xrange(1,size*4,4):
		lines.append([(s[n]%500,s[n+1]%500),(s[n+2]%500,s[n+3]%500)])


	return lines


def belongs((x,y),((x1,y1),(x2,y2)),((x3,y3),(x4,y4))):
	return  min(x1,x2)<x<max(x1,x2) and min(x3,x4)<x<max(x3,x4) and min(y1,y2)<y<max(y1,y2) and min(y3,y4)<y<max(y3,y4)  


def intersect(line1, line2):
    	xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    	ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1]) #Typo was here

    	def det(a, b):
        	return a[0] * b[1] - a[1] * b[0]

    	div = float(det(xdiff, ydiff))
    	if div == 0:
       		return False

    	d = (det(*line1), det(*line2))
   	x = det(d, xdiff) / div
    	y = det(d, ydiff) / div
    
	if belongs((x,y),line1,line2):	
		return x, y

	return False



lines = generate_lines(5000)

total = 0
count = 0

for i,line in enumerate(lines):

	print i

	for other_line in lines[i+1:]:
		total+=1

		if intersect(line,other_line):
			count +=1
print count
print total


