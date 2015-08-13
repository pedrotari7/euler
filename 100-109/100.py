import math

NT = 1000000000000

while 1:

	NB = 1/2. + (1/2.)*math.sqrt( 1 + 2*NT*(NT - 1))

	print "NT: " + str(long(NT))
	print "NB: " + "%0.2f" % NB

	if NB.is_integer():
		print "%0.2f" % NB
		print "%0.2f" % (NT-NB)
		break
	NT += 1

