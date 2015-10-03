from itertools import product

n = 4

dice = [sum(ele) for ele in product(range(1,n+1),range(1,n+1))]

dice_poss = [(ele,dice.count(ele)/float(len(dice))) for ele in set(dice)]


squares = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']

mono = dict()

for i,square in enumerate(squares):
	mono[square] = []

	for jump,prob in dice_poss:

		next_square = squares[(i+jump)%len(squares)]

		mono[square].append((next_square,prob)) 

result = []

for square in squares:
	count = 0
	for key in mono:
		count += sum([ele[1]/float(len(mono[key])) for ele in mono[key] if ele[0]==square])
	result.append((count,square))

print result
