from decimal import Context,Decimal
import math
dot100 = Context(prec=105)
print sum([sum([int(d) for d in str(Decimal(i).sqrt(dot100))[:101] if d.isdigit()]) for i in xrange(1,100) if not math.sqrt(i).is_integer()])
