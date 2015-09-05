
a = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

with open('22.txt','r') as f:
	print sum([sum([a.index(car)+1 for car in name])*(i+1) for i,name in enumerate(sorted(f.read().replace('"','').split(',')))])


	



