import itertools

def decrypt(text,key):
	final = ''
	for i in xrange(0,len(text),3):
		for j in xrange(3):
			if i+j < len(text): 
				final = final + chr(text[i+j]^key[j])
	return final


with open('p059_cipher.txt','r') as f:
	text = [int(ele) for ele in f.read().split(',')]

	for key in itertools.permutations(range(ord('a'),ord('z')+1),3):
		new_text = decrypt(text,key)
		if ' the ' in new_text: 
			print sum([ord(ele) for ele in new_text])
			break




