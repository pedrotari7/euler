
import math, time
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy.random as rnd

def calculate_line_equation((x1,y1),(x2,y2)):
	if (x2-x1) == 0:
		m = 0
	else:
		m = (y2-y1)/float((x2-x1))

	b = y1-m*x1

	return (m,b)

def calculate_tang_equation((x2,y2)):

	if y2 == 0:
		m = 0
	else:	
		m = -4*x2/float(y2)

	b = y2+m*x2

	return (m,b)

def calculate_angle_between_lines((m1,b1),(m2,b2)):

	if 1+m1*m2 == 0:
		return math.radians(90) 
	else:
		return math.radians(180) - 2*math.atan(abs((m1-m2)/float(1+m1*m2)))

def rotate_line((m1,b1),angle):

	d = float(math.cos(angle) - m1*math.sin(angle))

	if d == 0:
		m = 0
	else:
		m = (m1*math.cos(angle)+math.sin(angle))/d

	b = b1/d

	return (m,b)

def find_intersection((ml,bl),(xl,yl)):

	a = 1 + (ml**2)/4.
	b = 2*ml*bl/4.
	c = (bl**2)/4. - 25

	p1 = -b/(2*a)
	p2 = math.sqrt(b**2-4*a*c)/(2*a)

	x1 = p1-p2
	x2 = p1+p2

	if x1 == xl:
		x = x2
	else:
		x = x1

	y = ml*x+bl

	return (x,y) 

def is_final(p2,final,tol):

	return abs(p2[0]-final[0]) < tol and abs(p2[1]-final[1]) < tol

final = (0,10.1)
tol = 0.01
p1 = (0,10.1)
p2 = (1.4,-9.6)


e = Ellipse(xy=(0.,0.), width=2*5., height=2*10.)

fig = plt.figure(0)

ax = fig.add_subplot(111, aspect='equal')

ax.add_artist(e)
e.set_clip_box(ax.bbox)
e.set_alpha(0.1)
e.set_facecolor((0,0,0))

plt.plot([p1[0],p2[0]],[p1[1],p2[1]])

plt.axis([-7, 7, -12,12])

plt.ion()
plt.show()

while not is_final(p2,final,tol):

	l1 = calculate_line_equation(p1,p2)
	l2 = calculate_tang_equation(p2)

	theta = calculate_angle_between_lines(l1,l2)

	print math.degrees(theta)

	new_line = rotate_line(l1,theta)

	new_point = find_intersection(new_line,p2)

	p1 = p2
	p2 = new_point

	plt.plot([p1[0],p2[0]],[p1[1],p2[1]])

	plt.draw()

	time.sleep(5)